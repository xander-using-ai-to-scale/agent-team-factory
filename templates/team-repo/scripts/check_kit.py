#!/usr/bin/env python3
"""Validate a team kit built by the Agent Team Factory.

The rules are FACTORY-SPEC section 15 (docs/FACTORY-SPEC.md in the factory).
Everything team-specific comes from team.json, the approved blueprint in the
repo root: the vault folder, the agents, the brain files, the banks, and the
schedules. This file is identical in every team kit; never edit it for one team.

Errors (exit code 1):
   1. team.json is missing, is not valid JSON, or breaks a blueprint rule (§7):
      required keys and types; team_slug and file-name formats; qa is exactly
      {"name": "QA Agent", "file": "qa-agent.md"}; 1-8 specialists with rows
      R12, R13, ... and output files 01-, 02-, ... in order; depends_on names
      specialists listed earlier; the 3 core brain files first with their
      fixed sections, then 0-3 domain brain files; 1-5 banks with unique
      one-letter id prefixes (never E, W, or Q); the 4 fixed schedules first;
      platforms ["grokbot", "hermes"].
   2. A text file (.md .json .txt .yml .yaml, .gitignore) outside scripts/,
      dist/, and .git/ still holds a build-time token (an uppercase name in
      double angle brackets) or an unresolved FILL comment.
   3. A vault markdown file has no YAML frontmatter or an unknown `type`, or a
      kit-owned file's kit_version differs from team.json. 00-START-HERE.md
      must be type start-here; kit/INSTALL.md and kit/INSTALL-HERMES.md are
      checked like vault files and must be type install.
   4. A visible vault folder has no README.md, or a fixed vault file (§4) is
      missing.
   5. A [[wikilink]] points to a missing file or a missing #section.
   6. A backticked path (`01-brain/voice.md`) points to a missing file.
      Runtime paths are skipped: 05-outputs/ (except its README), 02-sources/
      files other than READMEs, tickets/, dated names (2026-10-12-...),
      00-summary.md, qa-report.md, DELIVERY.md, and every specialist's
      output_file. kit/, docs/, and scripts/ paths start at the repo root;
      INSTALL.md, INSTALL-HERMES.md, and hermes-skills/ paths start in kit/.
   7. Required ## headings (§9) are missing or out of order: the lead, QA, and
      specialist charters; every brain file (TL;DR, its team.json sections,
      Open questions, Changelog); every workflow (the first ## is Purpose, the
      last ## ends with "Checklist"). Also: a brain or bank file listed in
      team.json is missing, or 01-brain/ or 03-banks/ holds a file team.json
      does not list.
   8. The charters in 04-agents/ differ from team.json (lead, QA Agent,
      specialists).
   9. An agent name is missing from START-HERE's "Who works here" section,
      kit/INSTALL.md, or kit/INSTALL-HERMES.md.
  10. An R<number> in the vault has no routing-table row in START-HERE; a
      fixed row R0-R11 or a specialist's row is missing; a specialist's row
      does not name its charter file; a row from R12 up belongs to no
      specialist.
  11. A schedule name is missing from START-HERE, the lead charter, or
      04-agents/workflows/setup.md.
  12. A bank's next_id does not start with its id_prefix and a hyphen.
  13. The manifest in kit/INSTALL.md or kit/INSTALL-HERMES.md does not match
      the vault (--write-manifest regenerates both).
  14. Obsidian-only syntax (callouts, %% comments, dataview blocks).
  15. When team.json platforms include hermes: kit/hermes-skills/README.md is
      missing, an agent has no kit/hermes-skills/<file stem>/SKILL.md, or a
      SKILL.md has no top-level name and description in its frontmatter, a name
      other than <team_slug>-<file stem> (lowercase, 64 characters or less), a
      description that does not start with "Use when" or is over 60 characters,
      or a leftover AGENT-* placeholder. team_slug must not contain ignore,
      override, system, secret, or hidden (Hermes flags these words).

Warnings (reported, not fatal):
  - Weasel words in charters and workflows ("try to", "consider", "ideally",
    "maybe", "as appropriate").
  - Em dashes inside example sections (examples must follow the default
    anti-AI list).
  - Bare file names in backticks that match no file.

Paths are matched with exact letter case, like the file systems the bots use.
While a kit is being built, the text inside FILL comments is ignored by every
check except the leftover scan (check 2 reports each FILL comment itself).
A kit ships only at 0 errors and 0 warnings.

Usage:
    python scripts/check_kit.py                   # check
    python scripts/check_kit.py --write-manifest  # regenerate both manifests, then check
"""
from __future__ import annotations

import json
import os
import re
import sys
from datetime import date
from functools import lru_cache
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
KIT = ROOT / "kit"
TEAM_JSON = ROOT / "team.json"
INSTALLS = [KIT / "INSTALL.md", KIT / "INSTALL-HERMES.md"]
SKILLS = KIT / "hermes-skills"
VAULT = KIT / "vault"  # replaced by kit/<vault_folder> from team.json in main()
START_HERE = VAULT / "00-START-HERE.md"

KNOWN_TYPES = {
    "start-here", "brain", "charter", "workflow", "question-bank",
    "template", "bank", "log", "readme", "install",
}
VERSIONED_TYPES = {
    "start-here", "brain", "charter", "workflow", "question-bank",
    "template", "readme", "install",
}

LEAD_HEADINGS = [
    "What it is", "Your job", "Must read (in this order)", "Session start",
    "Session end", "Handling client messages", "Capturing what the client tells you",
    "How you talk to the client", "Your team", "Delegating work", "Workflows you run",
    "Scheduled tasks you own", "Client commands", "Owning the brain files",
    "What you never do", "If something is wrong",
]
SPECIALIST_HEADINGS = [
    "What it is", "When it runs", "Must read (in this order)", "Inputs you get",
    "What you produce", "What you never produce", "Rules for this work",
    "How to do the work (step by step)", "Quality checklist (run before you hand in)",
    "Output template", "Example (fictional)", "If something is wrong",
]
QA_HEADINGS = [
    "What it is", "When it runs", "Must read (in this order)", "Inputs you get",
    "What you produce", "What you never do", "The checks", "Verdict rules",
    "How to write fixes", "Output template", "Example (fictional)",
    "If something is wrong",
]
# The 3 core brain files, in team.json order, with their fixed sections.
# Domain sections may follow them.
CORE_BRAIN = {
    "company.md": ["What we sell", "Who we serve", "How we make money",
                   "What we believe", "What makes us different", "Key facts"],
    "voice.md": ["How we sound", "How we never sound", "Phrases we use",
                 "Banned words and phrases", "Formatting habits", "Spoken voice",
                 "Written voice", "Good examples", "Bad examples",
                 "Rules learned from edits"],
    "plan.md": ["Goal", "Outputs and quantities", "Rhythm", "Delivery", "Authority",
                "Team and handoff", "Areas to avoid"],
}
BRAIN_FRAME = ("TL;DR", "Open questions", "Changelog")  # every brain file has these
QA_AGENT = {"name": "QA Agent", "file": "qa-agent.md"}
PLATFORMS = ["grokbot", "hermes"]
FIXED_SCHEDULES = ["routine-send", "routine-reminder", "feedback-check", "monthly-review"]
RESERVED_PREFIXES = "EWQ"  # log IDs: E-### client edit, W-### winner, Q-### open question
FIRST_SPECIALIST_ROW = 12
FIXED_ROWS = [f"R{n}" for n in range(FIRST_SPECIALIST_ROW)]

# Vault files every team has (§4). Brain files, banks, and charters come from team.json.
FIXED_VAULT_FILES = [
    "00-START-HERE.md",
    "01-brain/README.md",
    "02-sources/README.md",
    "02-sources/interview/README.md",
    "02-sources/routine-answers/README.md",
    "02-sources/transcripts/README.md",
    "02-sources/documents/README.md",
    "02-sources/other/README.md",
    "03-banks/README.md",
    "04-agents/README.md",
    "04-agents/workflows/README.md",
    "04-agents/workflows/setup.md",
    "04-agents/workflows/routine.md",
    "04-agents/workflows/production.md",
    "04-agents/workflows/learning-loop.md",
    "04-agents/workflows/monthly-review.md",
    "04-agents/workflows/on-demand.md",
    "04-agents/question-banks/README.md",
    "04-agents/question-banks/setup-interview.md",
    "04-agents/question-banks/routine-questions.md",
    "04-agents/templates/README.md",
    "04-agents/templates/job-ticket.md",
    "04-agents/templates/output-summary.md",
    "04-agents/templates/qa-report.md",
    "04-agents/templates/delivery.md",
    "05-outputs/README.md",
    "06-log/README.md",
    "06-log/session-log.md",
    "06-log/edits-log.md",
    "06-log/winners.md",
    "06-log/open-questions.md",
    "06-log/questions-asked.md",
]

# Runtime files that exist only once the team works (output folders).
# Every specialist's output_file from team.json is added to these.
RUNTIME_NAMES = {"00-summary.md", "qa-report.md", "DELIVERY.md"}

# The leftover scan reads these text files everywhere except these top-level folders.
LEFTOVER_SKIP = {"scripts", "dist", ".git"}
TEXT_SUFFIXES = {".md", ".json", ".txt", ".yml", ".yaml"}

# Built from pieces so this file never contains a complete marker itself:
# builders search team repos for leftovers.
TOKEN = re.compile("<" * 2 + "[A-Z][A-Z0-9_]*" + ">" * 2)
FILL = re.compile("<!" + r"--\s*FILL")
FILL_BLOCK = re.compile("<!" + r"--\s*FILL.*?(?:-->|\Z)", re.S)
EM_DASH = chr(0x2014)  # written as a code point so this file holds no em dash

KEBAB = r"[a-z0-9]+(?:-[a-z0-9]+)*"
SLUG = re.compile("^" + KEBAB + "$")
SLUG_BANNED = ("ignore", "override", "system", "secret", "hidden")
SKILL_NAME = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
SKILL_PLACEHOLDERS = ("AGENT-" + "NAME", "AGENT-" + "FILE-STEM", "AGENT-" + "JOB-TRIGGER")
MD_NAME = re.compile("^" + KEBAB + r"\.md$")
OUTPUT_NAME = re.compile(r"^(\d\d)-" + KEBAB + r"\.md$")
SEMVER = re.compile(r"^\d+\.\d+\.\d+$")
ROW_ID = re.compile(r"^R\d+$")
ROW_CELL = re.compile(r"^\|\s*(R\d+)\s*\|")
ROW_REF = re.compile(r"\bR\d+\b")
DATED = re.compile(r"^\d{4}-\d{2}-\d{2}-")
OUTSIDE_KIT = re.compile(r"^(?:[~/.$]|[A-Za-z]:)")  # home, absolute, hidden, or drive paths
WEASEL = re.compile(r"\b(try to|consider|ideally|maybe|as appropriate)\b", re.I)
WIKILINK = re.compile(r"\[\[([^\]]+)\]\]")
BACKTICK_PATH = re.compile(r"`([^`\s]+?\.md)`")
HEADING = re.compile(r"^(#{1,6})\s+(.+?)\s*#*\s*$")
MANIFEST = re.compile(r"<!-- MANIFEST:START -->.*?<!-- MANIFEST:END -->", re.S)

errors: list[str] = []
warnings: list[str] = []
texts: dict[Path, str | None] = {}  # every file read, once
contents: dict[Path, str | None] = {}  # the same, with FILL comments blanked out


# --- helpers ---------------------------------------------------------------

def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def err(path: Path, msg: str) -> None:
    errors.append(f"ERROR {rel(path)}: {msg}")


def warn(path: Path, msg: str) -> None:
    warnings.append(f"WARN  {rel(path)}: {msg}")


def read(path: Path) -> str | None:
    """The file's text, read once. None (reported as an error) if unreadable."""
    if path not in texts:
        try:
            texts[path] = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            texts[path] = None
            err(path, "not valid UTF-8 text")
        except OSError as exc:
            texts[path] = None
            err(path, f"cannot be read ({exc.strerror})")
    return texts[path]


def content(path: Path) -> str | None:
    """The file's text with FILL comments blanked out (line numbers kept).

    A FILL comment is a build instruction, reported as a leftover by itself;
    its text (content-kit examples, sample rows) is not part of the kit, so
    every other check reads the file without it."""
    if path not in contents:
        text = read(path)
        contents[path] = None if text is None else FILL_BLOCK.sub(
            lambda m: "\n" * m.group(0).count("\n"), text)
    return contents[path]


@lru_cache(maxsize=None)
def listing(folder: Path) -> frozenset:
    try:
        return frozenset(os.listdir(folder))
    except OSError:
        return frozenset()


def exists(path: Path) -> bool:
    """True if the path exists with exactly this letter case.

    Windows and macOS ignore case; the bots' file systems do not."""
    try:
        parts = path.relative_to(ROOT).parts
    except ValueError:
        return path.exists()
    folder = ROOT
    for part in parts:
        if part in (".", ".."):
            return path.exists()
        if part not in listing(folder):
            return False
        folder = folder / part
    return True


def frontmatter(text: str) -> dict[str, str] | None:
    """Top-level keys of the YAML frontmatter, or None if the file has none.

    Indented lines (nested YAML such as a metadata: block), list items, and
    comments are skipped."""
    if not text.startswith("---\n") and not text.startswith("---\r\n"):
        return None
    data: dict[str, str] = {}
    for line in text.splitlines()[1:]:
        if line.strip() == "---":
            return data
        if line[:1] in ("", " ", "\t", "-", "#") or ":" not in line:
            continue
        key, _, value = line.partition(":")
        data[key.strip()] = value.strip().strip("\"'")
    return None


def outside_fences(text: str) -> list[tuple[int, str]]:
    """(line number, line) pairs that are not inside ``` fenced blocks."""
    result, fenced = [], False
    for number, line in enumerate(text.splitlines(), 1):
        if line.lstrip().startswith("```"):
            fenced = not fenced
            continue
        if not fenced:
            result.append((number, line))
    return result


def headings_of(text: str, level: int | None = None) -> list[str]:
    found = []
    for _, line in outside_fences(text):
        match = HEADING.match(line)
        if match and (level is None or len(match.group(1)) == level):
            found.append(match.group(2).strip())
    return found


def section_text(text: str, title: str) -> str | None:
    """The lines under the first heading containing `title` (any case), up to the
    next heading of the same or a higher level. None if there is no such heading."""
    collected: list[str] | None = None
    level, fenced = 0, False
    for line in text.splitlines():
        if line.lstrip().startswith("```"):
            fenced = not fenced
        match = None if fenced else HEADING.match(line)
        if collected is None:
            if match and title in match.group(2).lower():
                collected, level = [], len(match.group(1))
            continue
        if match and len(match.group(1)) <= level:
            break
        collected.append(line)
    return None if collected is None else "\n".join(collected)


def mentions(text: str, word: str) -> bool:
    """True if `word` appears in `text` as a whole name (not inside a longer name)."""
    return re.search(r"(?<![\w-])" + re.escape(word) + r"(?![\w-])", text) is not None


def names_schedule(text: str, name: str) -> bool:
    """Like mentions(), but a workflow path or file name (monthly-review.md) does not count."""
    pattern = r"(?<![\w/.-])" + re.escape(name) + r"(?![\w/-])(?!\.md)"
    return re.search(pattern, text) is not None


def is_placeholder(value: str) -> bool:
    return any(token in value for token in ("{{", "}}", "YYYY", "*", "<", ">"))


def visible(path: Path) -> bool:
    """False for anything inside a hidden folder such as .obsidian/ (created by the Obsidian app)."""
    return not any(part.startswith(".") for part in path.relative_to(VAULT).parts)


def check_heading_order(path: Path, text: str, required: list[str]) -> None:
    found = headings_of(text, level=2)
    for heading in required:
        if heading not in found:
            err(path, f'missing "## {heading}"')
    present = [h for h in found if h in required]
    expected = [h for h in required if h in found]
    if present != expected:
        index = next((i for i, (a, b) in enumerate(zip(present, expected)) if a != b), None)
        if index is None:
            detail = f'"## {present[len(expected)]}" appears twice'
        else:
            detail = f'"## {present[index]}" comes where "## {expected[index]}" belongs'
        err(path, f"required ## headings are out of order ({detail})")


# --- team.json (§7) ----------------------------------------------------------

def team_err(msg: str) -> None:
    err(TEAM_JSON, msg)


def text_of(obj: dict, key: str, where: str = "") -> str | None:
    """obj[key] if it is a non-empty string; otherwise report it and return None."""
    value = obj.get(key)
    if isinstance(value, str) and value.strip():
        return value
    team_err(f"{where}{key} must be a non-empty string")
    return None


def md_name_of(obj: dict, key: str, where: str) -> str | None:
    """obj[key] if it is a lowercase kebab-case .md file name; otherwise report it."""
    value = text_of(obj, key, where)
    if value is not None and not MD_NAME.match(value):
        team_err(f'{where}{key} "{value}" must be lowercase kebab-case ending in .md')
        return None
    return value


def list_of(data: dict, key: str, low: int, high: int | None = None) -> list:
    """data[key] if it is a list (its length is checked); otherwise report it and return []."""
    value = data.get(key)
    if not isinstance(value, list):
        team_err(f"{key} must be a list")
        return []
    if len(value) < low or (high is not None and len(value) > high):
        allowed = f"{low} to {high}" if high is not None else f"at least {low}"
        team_err(f"{key} has {len(value)} entries (allowed: {allowed})")
    return value


def report_duplicates(label: str, values: list) -> None:
    for value in sorted({v for v in values if values.count(v) > 1}):
        team_err(f'{label} "{value}" is used more than once')


def valid_date(value: str) -> bool:
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        return False
    try:
        date.fromisoformat(value)
    except ValueError:
        return False
    return True


def load_team() -> dict | None:
    if not TEAM_JSON.is_file():
        err(TEAM_JSON, "missing (the approved blueprint, FACTORY-SPEC §7)")
        return None
    text = read(TEAM_JSON)
    if text is None:
        return None
    try:
        data = json.loads(text)
    except json.JSONDecodeError as exc:
        err(TEAM_JSON, f"not valid JSON ({exc})")
        return None
    return check_team(data)


def check_team(data: object) -> dict | None:
    """Check team.json against §7 and return what the vault checks need.

    Malformed entries are reported and left out, so the other checks still run.
    Returns None when the vault cannot be located."""
    if not isinstance(data, dict):
        team_err("must be a JSON object")
        return None

    for key in ("factory_version", "kit_version"):
        value = text_of(data, key)
        if value is not None and not SEMVER.match(value):
            team_err(f'{key} "{value}" is not X.Y.Z')
    release = text_of(data, "release_date")
    if release is not None and not valid_date(release):
        team_err(f'release_date "{release}" is not a YYYY-MM-DD date')
    for key in ("team_name", "vault_name", "output_unit", "output_unit_plural", "routine_name"):
        text_of(data, key)
    purpose = text_of(data, "team_purpose")
    if purpose is not None and purpose.rstrip().endswith("."):
        team_err("team_purpose must not end with a period")
    slug = text_of(data, "team_slug")
    if slug is not None and not SLUG.match(slug):
        team_err(f'team_slug "{slug}" must be lowercase letters, digits, and hyphens')
    if slug is not None and any(word in slug for word in SLUG_BANNED):
        team_err(f'team_slug "{slug}" must not contain {", ".join(SLUG_BANNED)} (Hermes flags these words)')
    folder = text_of(data, "vault_folder")
    vault_name = data.get("vault_name")
    if folder is not None and isinstance(vault_name, str):
        wanted = vault_name.replace(" ", "-")
        if folder != wanted:
            team_err(f'vault_folder "{folder}" must be vault_name with spaces replaced by hyphens: "{wanted}"')
    platforms = data.get("platforms")
    if platforms != PLATFORMS:
        team_err(f"platforms must be {json.dumps(PLATFORMS)}")

    agents: list[tuple[str, str]] = []  # (name, file) for the lead, the QA Agent, each specialist
    lead_entry = None
    lead = data.get("lead")
    if isinstance(lead, dict):
        name = text_of(lead, "name", "lead.")
        text_of(lead, "short", "lead.")
        file = md_name_of(lead, "file", "lead.")
        if name and file:
            lead_entry = (name, file)
            agents.append(lead_entry)
    else:
        team_err("lead must be an object with name, short, and file")
    if data.get("qa") != QA_AGENT:
        team_err('qa must be exactly {"name": "QA Agent", "file": "qa-agent.md"}')
    agents.append((QA_AGENT["name"], QA_AGENT["file"]))

    specialists: list[dict] = []
    entries = list_of(data, "specialists", 1, 8)
    order = [entry.get("file") if isinstance(entry, dict) else None for entry in entries]
    for index, entry in enumerate(entries):
        where = f"specialists[{index}]."
        if not isinstance(entry, dict):
            team_err(f"specialists[{index}] must be an object")
            continue
        name = text_of(entry, "name", where)
        file = md_name_of(entry, "file", where)
        text_of(entry, "job", where)
        row = entry.get("row")
        wanted_row = f"R{FIRST_SPECIALIST_ROW + index}"
        if row != wanted_row:
            team_err(f'{where}row is {json.dumps(row)}, expected "{wanted_row}"')
        output = entry.get("output_file")
        match = OUTPUT_NAME.match(output) if isinstance(output, str) else None
        if not match or int(match.group(1)) != index + 1:
            team_err(f'{where}output_file is {json.dumps(output)}, expected "{index + 1:02d}-<slug>.md"')
        depends = entry.get("depends_on")
        if not isinstance(depends, list) or not all(isinstance(dep, str) for dep in depends):
            team_err(f"{where}depends_on must be a list of specialist file names")
        else:
            for dep in depends:
                if dep == file:
                    team_err(f'{where}depends_on lists the specialist itself ("{dep}")')
                elif dep not in order:
                    team_err(f'{where}depends_on "{dep}" is not a specialist file')
                elif order.index(dep) > index:
                    team_err(f'{where}depends_on "{dep}" comes later in the list (specialists are in production order)')
        if not isinstance(entry.get("on_demand_only"), bool):
            team_err(f"{where}on_demand_only must be true or false")
        if name and file:
            specialists.append({
                "name": name,
                "file": file,
                "row": row if isinstance(row, str) else None,
                "output_file": output if isinstance(output, str) else None,
            })
            agents.append((name, file))
    report_duplicates("agent name", [name for name, _ in agents])
    report_duplicates("agent file", [file for _, file in agents])

    brain: list[dict] = []
    core_files = list(CORE_BRAIN)
    for index, entry in enumerate(list_of(data, "brain_files", 3, 6)):
        where = f"brain_files[{index}]."
        if not isinstance(entry, dict):
            team_err(f"brain_files[{index}] must be an object")
            continue
        file = md_name_of(entry, "file", where)
        text_of(entry, "title", where)
        sections = entry.get("sections")
        if (not isinstance(sections, list) or not sections
                or not all(isinstance(s, str) and s.strip() for s in sections)):
            team_err(f"{where}sections must be a non-empty list of heading names")
            sections = None
        else:
            report_duplicates(f"{where}sections entry", sections)
            for heading in BRAIN_FRAME:
                if heading in sections:
                    team_err(f'{where}sections must not list "{heading}" (every brain file has it)')
            sections = [s for s in sections if s not in BRAIN_FRAME]
        if index < len(core_files):
            core_file = core_files[index]
            if file != core_file:
                team_err(f'{where}file must be "{core_file}" (the 3 core brain files come first, in order)')
            if entry.get("core") is not True:
                team_err(f"{where}core must be true")
            fixed = CORE_BRAIN[core_file]
            if sections is not None and sections[:len(fixed)] != fixed:
                team_err(f"{where}sections must start with the core sections of {core_file}: {', '.join(fixed)}")
        elif entry.get("core") is not False:
            team_err(f"{where}core must be false (only the first 3 brain files are core)")
        if file and sections is not None:
            brain.append({"file": file, "sections": sections})
    report_duplicates("brain file", [entry["file"] for entry in brain])

    banks: list[dict] = []
    for index, entry in enumerate(list_of(data, "banks", 1, 5)):
        where = f"banks[{index}]."
        if not isinstance(entry, dict):
            team_err(f"banks[{index}] must be an object")
            continue
        file = md_name_of(entry, "file", where)
        text_of(entry, "title", where)
        prefix = entry.get("id_prefix")
        if not isinstance(prefix, str) or not re.fullmatch("[A-Z]", prefix):
            team_err(f"{where}id_prefix must be one uppercase letter")
            prefix = None
        elif prefix in RESERVED_PREFIXES:
            team_err(f'{where}id_prefix "{prefix}" is reserved for the logs (E, W, Q)')
        if file and prefix:
            banks.append({"file": file, "prefix": prefix})
    report_duplicates("bank file", [entry["file"] for entry in banks])
    report_duplicates("bank id_prefix", [entry["prefix"] for entry in banks])

    schedules: list[str] = []
    for index, entry in enumerate(list_of(data, "schedules", len(FIXED_SCHEDULES))):
        where = f"schedules[{index}]."
        if not isinstance(entry, dict):
            team_err(f"schedules[{index}] must be an object")
            continue
        name = text_of(entry, "name", where)
        text_of(entry, "default_time", where)
        text_of(entry, "does", where)
        if name:
            schedules.append(name)
    if isinstance(data.get("schedules"), list) and schedules[:len(FIXED_SCHEDULES)] != FIXED_SCHEDULES:
        team_err(f"schedules must start with {', '.join(FIXED_SCHEDULES)}, in this order")
    report_duplicates("schedule name", schedules)

    if folder is None:
        return None
    if folder in (".", "..") or "/" in folder or "\\" in folder:
        team_err(f'vault_folder "{folder}" must be a single folder name')
        return None
    version = data.get("kit_version")
    return {
        "version": version if isinstance(version, str) and version.strip() else None,
        "slug": slug if isinstance(slug, str) else "",
        "vault_folder": folder,
        "platforms": platforms if isinstance(platforms, list) else [],
        "lead": lead_entry,
        "agents": agents,
        "specialists": specialists,
        "brain": brain,
        "banks": banks,
        "schedules": schedules,
    }


# --- leftovers ---------------------------------------------------------------

def repo_text_files() -> list[Path]:
    """Every text file the leftover scan reads (outside scripts/, dist/, and .git/)."""
    found = []
    for folder, dirs, files in os.walk(ROOT):
        here = Path(folder)
        if here == ROOT:
            dirs[:] = [d for d in dirs if d not in LEFTOVER_SKIP]
        dirs[:] = [d for d in dirs if d not in (".git", "__pycache__")]
        for name in files:
            path = here / name
            if path.suffix.lower() in TEXT_SUFFIXES or name == ".gitignore":
                found.append(path)
    return sorted(found, key=rel)


def check_leftovers(files: list[Path]) -> None:
    for path in files:
        text = read(path)
        if text is None:
            continue
        for number, line in enumerate(text.splitlines(), 1):
            for token in TOKEN.findall(line):
                err(path, f"line {number}: leftover token {token}")
            if FILL.search(line):
                err(path, f"line {number}: leftover FILL comment")


# --- vault files -------------------------------------------------------------

def resolve_backtick(path_text: str) -> Path | None:
    """Return the file a backticked path should point to, or None to skip it."""
    if is_placeholder(path_text) or OUTSIDE_KIT.match(path_text) or "\\" in path_text:
        return None  # a placeholder, or a path outside the kit
    if path_text.startswith(("kit/", "docs/", "scripts/")):
        return ROOT / path_text
    if path_text in ("INSTALL.md", "INSTALL-HERMES.md"):
        return KIT / path_text
    if path_text.startswith(("hermes-skills/", VAULT.name + "/")):
        return KIT / path_text
    if "/" not in path_text:
        return None  # bare names are handled as warnings
    parts = path_text.split("/")
    if parts[0] == "tickets":
        return None  # runtime ticket files inside an output folder
    if parts[0] == "05-outputs" and path_text != "05-outputs/README.md":
        return None  # runtime output files
    if parts[0] == "02-sources" and parts[-1] != "README.md":
        return None  # runtime source files
    if any(DATED.match(part) for part in parts):
        return None  # dated runtime names
    return VAULT / path_text


def is_bare_name(path_text: str) -> bool:
    """A plain file name: no folder, not a placeholder, not a dated runtime name."""
    return (not re.search(r"[/\\~$]", path_text) and not is_placeholder(path_text)
            and not DATED.match(path_text))


def check_file(path: Path, version: str | None, all_names: set, runtime: set) -> None:
    text = content(path)
    if text is None:
        return
    fm = frontmatter(text)
    if fm is None:
        err(path, "no YAML frontmatter")
        return
    ftype = fm.get("type", "")
    if ftype not in KNOWN_TYPES:
        err(path, f'unknown or missing type "{ftype}"')
    if path == START_HERE and ftype != "start-here":
        err(path, 'type must be "start-here"')
    if path in INSTALLS and ftype != "install":
        err(path, 'type must be "install"')
    if version is not None and ftype in VERSIONED_TYPES and fm.get("kit_version") != version:
        err(path, f'kit_version "{fm.get("kit_version")}" != {version} (team.json)')

    manifest_lines = range(0)  # check_manifest() compares the manifest block with the vault
    block = MANIFEST.search(text) if path in INSTALLS else None
    if block:
        manifest_lines = range(text.count("\n", 0, block.start()) + 1,
                               text.count("\n", 0, block.end()) + 2)

    in_example = False
    for number, line in outside_fences(text):
        heading = HEADING.match(line)
        if heading:
            in_example = "example" in heading.group(2).lower()
        if re.match(r"^\s*>\s*\[!", line):
            err(path, f"line {number}: Obsidian callout (use plain markdown)")
        if "%%" in line:
            err(path, f"line {number}: Obsidian %% comment")
        if in_example and EM_DASH in line:
            warn(path, f"line {number}: em dash inside an example section")
        if ftype in {"charter", "workflow"}:
            weasel = WEASEL.search(line)
            if weasel and "never" not in line.lower() and '"' not in line:
                warn(path, f'line {number}: weasel word "{weasel.group(1)}"')

        for link in WIKILINK.findall(line):
            target = link.split("|", 1)[0]
            if is_placeholder(target):
                continue
            file_part, _, section = target.partition("#")
            file_part = file_part.strip()
            target_path = VAULT / (file_part if file_part.endswith(".md") else file_part + ".md")
            if not exists(target_path):
                err(path, f"line {number}: broken link [[{link}]]")
                continue
            if section:
                body = content(target_path)
                if body is not None and section.strip() not in headings_of(body):
                    err(path, f'line {number}: [[{link}]] section "{section}" not found')

        for path_text in [] if number in manifest_lines else BACKTICK_PATH.findall(line):
            target_path = resolve_backtick(path_text)
            if target_path is not None:
                if not exists(target_path):
                    err(path, f"line {number}: missing file `{path_text}`")
            elif is_bare_name(path_text) and path_text not in all_names and path_text not in runtime:
                warn(path, f"line {number}: `{path_text}` matches no file")

    if "```dataview" in text:
        err(path, "dataview block")


def check_layout() -> None:
    """Every visible vault folder has a README.md; every fixed vault file (§4) exists."""
    folders = sorted((p for p in VAULT.rglob("*") if p.is_dir() and visible(p)), key=rel)
    for folder in folders:
        if not exists(folder / "README.md"):
            err(folder, "folder has no README.md")
    for name in FIXED_VAULT_FILES:
        path = VAULT / name
        if exists(path) or (path.name == "README.md" and exists(path.parent)):
            continue  # a folder without its README is reported above
        err(path, "missing (fixed vault file, FACTORY-SPEC §4)")


def check_agents(team: dict) -> None:
    """The charters in 04-agents/ are exactly the lead, the QA Agent, and the specialists."""
    folder = VAULT / "04-agents"
    expected = {file: name for name, file in team["agents"]}
    found = {p.name for p in folder.glob("*.md") if p.name != "README.md"} if folder.is_dir() else set()
    for file in sorted(set(expected) - found):
        err(folder / file, f"missing: {expected[file]} has no charter")
    for file in sorted(found - set(expected)):
        err(folder / file, "charter is not in team.json")


def check_brain_and_banks(team: dict) -> None:
    """Brain and bank files match team.json; each bank's next_id starts with its id_prefix."""
    for folder, entries, kind in ((VAULT / "01-brain", team["brain"], "brain file"),
                                  (VAULT / "03-banks", team["banks"], "bank file")):
        listed = {entry["file"] for entry in entries}
        for file in sorted(listed):
            if not exists(folder / file):
                err(folder / file, f"missing ({kind} listed in team.json)")
        if folder.is_dir():
            for path in sorted(folder.glob("*.md"), key=rel):
                if path.name != "README.md" and path.name not in listed:
                    err(path, f"{kind} is not in team.json")
    for bank in team["banks"]:
        path = VAULT / "03-banks" / bank["file"]
        text = content(path) if exists(path) else None
        fm = frontmatter(text) if text is not None else None
        if fm is None:
            continue  # a missing file or missing frontmatter is reported elsewhere
        next_id = fm.get("next_id", "")
        prefix = bank["prefix"] + "-"
        if not next_id.startswith(prefix):
            err(path, f'next_id "{next_id}" does not start with "{prefix}" (id_prefix in team.json)')


def check_required(path: Path, required: list[str]) -> None:
    if not exists(path):
        return  # reported by the charter, brain-file, or layout checks
    text = content(path)
    if text is not None:
        check_heading_order(path, text, required)


def check_headings(team: dict) -> None:
    """Required ## headings (§9): charters, brain files, workflows."""
    agents_dir = VAULT / "04-agents"
    charters = [(QA_AGENT["file"], QA_HEADINGS)]
    if team["lead"]:
        charters.insert(0, (team["lead"][1], LEAD_HEADINGS))
    charters += [(spec["file"], SPECIALIST_HEADINGS) for spec in team["specialists"]]
    for file, required in charters:
        check_required(agents_dir / file, required)
    for entry in team["brain"]:
        required = [BRAIN_FRAME[0], *entry["sections"], *BRAIN_FRAME[1:]]
        check_required(VAULT / "01-brain" / entry["file"], required)

    workflows = agents_dir / "workflows"
    paths = sorted(workflows.glob("*.md"), key=rel) if workflows.is_dir() else []
    for path in paths:
        text = content(path) if path.name != "README.md" else None
        if text is None:
            continue
        found = headings_of(text, level=2)
        first = found[0] if found else "none"
        last = found[-1] if found else "none"
        if first != "Purpose":
            err(path, f'the first "## " heading must be "Purpose" (found "{first}")')
        if not last.lower().endswith("checklist"):
            err(path, f'the last "## " heading must end with "Checklist" (found "{last}")')


def check_routing(team: dict, vault_md: list[Path]) -> None:
    """START-HERE's routing table (§11) and every R<number> in the vault."""
    text = content(START_HERE)
    if text is None:
        return
    rows: dict[str, str] = {}
    for number, line in outside_fences(text):
        match = ROW_CELL.match(line.strip())
        if not match:
            continue
        if match.group(1) in rows:
            err(START_HERE, f"line {number}: routing-table row {match.group(1)} appears twice")
        else:
            rows[match.group(1)] = line
    for row in FIXED_ROWS:
        if row not in rows:
            err(START_HERE, f"routing table has no row {row} (rows R0 to R11 are fixed)")
    owned = set()
    for spec in team["specialists"]:
        row, stem = spec["row"], spec["file"][:-3]
        if not row or not ROW_ID.match(row):
            continue  # reported in team.json
        owned.add(row)
        if row not in rows:
            err(START_HERE, f"routing table has no row {row} for {spec['name']}")
        elif not mentions(rows[row], stem):
            err(START_HERE, f"routing-table row {row} does not name {spec['name']}'s charter file ({stem})")
    for row in rows:
        if int(row[1:]) >= FIRST_SPECIALIST_ROW and row not in owned:
            err(START_HERE, f"routing-table row {row} belongs to no specialist in team.json")
    for path in vault_md:
        body = content(path)
        if body is None:
            continue
        for number, line in outside_fences(body):
            for ref in dict.fromkeys(ROW_REF.findall(line)):
                if ref not in rows:
                    err(path, f"line {number}: {ref} has no routing-table row in 00-START-HERE.md")


def check_agent_names(team: dict, installs: list[Path]) -> None:
    """Every agent name is in START-HERE's "Who works here" section and in both INSTALL files."""
    names = [name for name, _ in team["agents"]]
    text = content(START_HERE) if exists(START_HERE) else None
    if text is not None:
        section = section_text(text, "who works here")
        if section is None:
            err(START_HERE, 'no "Who works here" section')
        else:
            for name in names:
                if not mentions(section, name):
                    err(START_HERE, f'agent "{name}" is missing from the "Who works here" section')
    for path in installs:
        body = content(path)
        if body is None:
            continue
        for name in names:
            if not mentions(body, name):
                err(path, f'agent "{name}" is not named in this runbook')


def check_schedules(team: dict) -> None:
    """Every schedule name is in START-HERE, the lead charter, and workflows/setup.md."""
    targets = [START_HERE]
    if team["lead"]:
        targets.append(VAULT / "04-agents" / team["lead"][1])
    targets.append(VAULT / "04-agents" / "workflows" / "setup.md")
    for path in targets:
        text = content(path) if exists(path) else None
        if text is None:
            continue  # a missing file is reported by the layout or charter checks
        for name in team["schedules"]:
            if not names_schedule(text, name):
                err(path, f"schedule `{name}` is not named")


def vault_files() -> list[str]:
    return sorted(
        p.relative_to(VAULT).as_posix() for p in VAULT.rglob("*") if p.is_file() and visible(p)
    )


def manifest_block(files: list[str]) -> str:
    body = [f"Total: {len(files)} files.", ""]
    body += [f"- `{name}`" for name in files]
    return "<!-- MANIFEST:START -->\n" + "\n".join(body) + "\n<!-- MANIFEST:END -->"


def write_manifests() -> None:
    """--write-manifest: regenerate the manifest block in both INSTALL files.

    Keeps each file's line endings (CRLF or LF)."""
    block = manifest_block(vault_files())
    for path in INSTALLS:
        if not path.is_file():
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue  # reported by the checks
        if not MANIFEST.search(text):
            continue  # reported by check_manifest
        new_text = MANIFEST.sub(lambda _: block, text)
        if new_text != text:
            newline = "\r\n" if b"\r\n" in path.read_bytes() else "\n"
            with open(path, "w", encoding="utf-8", newline=newline) as handle:
                handle.write(new_text)


def check_manifest(path: Path, files: list[str]) -> None:
    text = content(path)
    if text is None:
        return
    match = MANIFEST.search(text)
    if not match:
        err(path, "manifest markers not found")
        return
    block = match.group(0)
    listed = set(re.findall(r"^- `([^`]+)`$", block, re.M))
    missing, extra = sorted(set(files) - listed), sorted(listed - set(files))
    for name in missing:
        err(path, f"manifest is missing `{name}` (run with --write-manifest)")
    for name in extra:
        err(path, f"manifest lists `{name}`, which does not exist")
    total = re.search(r"^Total: (\d+) files\.$", block, re.M)
    if not missing and not extra and (not total or int(total.group(1)) != len(files)):
        err(path, f'manifest total is not "Total: {len(files)} files." (run with --write-manifest)')


def check_skills(team: dict) -> None:
    """Hermes: kit/hermes-skills/README.md, one SKILL.md per agent, valid name and description in each."""
    if not exists(SKILLS / "README.md"):
        err(SKILLS / "README.md", "missing (kit/hermes-skills/ needs a README.md)")
    expected = {}
    for name, file in team["agents"]:
        skill = SKILLS / file[:-3] / "SKILL.md"
        expected[skill] = f'{team["slug"]}-{file[:-3]}'
        if not exists(skill):
            err(skill, f"missing: {name} has no Hermes skill")
    skills = sorted(SKILLS.rglob("SKILL.md"), key=rel) if SKILLS.is_dir() else []
    for skill in skills:
        text = content(skill)
        if text is None:
            continue
        fm = frontmatter(text)
        if fm is None:
            err(skill, "no YAML frontmatter")
            continue
        for key in ("name", "description"):
            if not fm.get(key):
                err(skill, f"frontmatter has no top-level {key}")
        name, description = fm.get("name", ""), fm.get("description", "")
        if name and (not SKILL_NAME.match(name) or len(name) > 64):
            err(skill, f'name "{name}" must be lowercase letters, digits, and hyphens, 64 characters or less')
        if name and skill in expected and name != expected[skill]:
            err(skill, f'name "{name}" should be "{expected[skill]}" (team_slug + charter file stem)')
        if description and (not description.startswith("Use when") or len(description) > 60):
            err(skill, "description must start with \"Use when\" and be 60 characters or less (Hermes refuses longer)")
        for placeholder in SKILL_PLACEHOLDERS:
            if placeholder in text:
                err(skill, f"leftover placeholder {placeholder}")


def check_vault(team: dict, repo_files: list[Path]) -> None:
    runtime = RUNTIME_NAMES | {s["output_file"] for s in team["specialists"] if s["output_file"]}
    installs = []
    for path in INSTALLS:
        if exists(path):
            installs.append(path)
        else:
            err(path, "missing (install runbook)")

    check_layout()
    vault_md = sorted((p for p in VAULT.rglob("*.md") if p.is_file() and visible(p)), key=rel)
    all_names = {p.name for p in repo_files if p.suffix == ".md"}
    for path in vault_md + installs:
        check_file(path, team["version"], all_names, runtime)

    check_agents(team)
    check_brain_and_banks(team)
    check_headings(team)
    if exists(START_HERE):
        check_routing(team, vault_md)
    check_agent_names(team, installs)
    check_schedules(team)
    files = vault_files()
    for path in installs:
        check_manifest(path, files)
    if "hermes" in team["platforms"]:
        check_skills(team)


def main() -> int:
    global VAULT, START_HERE
    write_manifest = "--write-manifest" in sys.argv
    repo_files = repo_text_files()
    team = load_team()
    if team is not None:
        VAULT = KIT / team["vault_folder"]
        START_HERE = VAULT / "00-START-HERE.md"
        if not exists(VAULT):
            err(VAULT, "vault folder not found (kit/<vault_folder> from team.json)")
            team = None
    if team is not None and write_manifest:
        write_manifests()

    check_leftovers(repo_files)
    if team is not None:
        check_vault(team, repo_files)

    for line in errors + warnings:
        print(line)
    print(f"\n{len(texts)} files checked · {len(errors)} errors · {len(warnings)} warnings")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
