#!/usr/bin/env python3
"""Validate the Agent Team Factory repo itself.

Run it after changing a template, a process file, or a doc. The contract is
docs/FACTORY-SPEC.md; the section numbers below are its sections.

Errors (exit code 1):
  1. Template inventory: the files under templates/team-repo/ differ from the
     list in §17 (missing or unexpected files; __pycache__ is ignored), or
     §17's heading states a different file count than its list holds.
  2. A double-angle-bracket token used under templates/ is not declared in
     the §6 table.
  3. A FILL comment under templates/ is not closed, or has no "Source:".
     Checks 2 and 3 skip the two scripts in templates/team-repo/scripts/
     (they avoid complete markers on purpose) and templates/README.md (it
     documents the markers and is never copied into a kit).
  4. A vault template (templates/team-repo/kit/vault/**/*.md) has no YAML
     frontmatter or an unknown type (§8), or a kit-owned type whose
     kit_version is not the KIT_VERSION token.
  5. Required ## headings (§9) are missing or out of order in _lead-agent.md,
     _specialist-agent.md, and qa-agent.md; company.md, voice.md, plan.md,
     and _brain-file.md do not start with TL;DR, keep their core sections in
     order, and end with Open questions, then Changelog; a workflow other
     than README.md does not start with Purpose or does not end with a
     heading that ends in "Checklist". HTML comments (FILL and guidance
     comments) are ignored for these checks.
  6. A relative markdown link, or a backticked path that starts with
     process/, docs/, templates/, scripts/, or examples/, in README.md,
     FACTORY-PROMPT.md, process/*.md, docs/*.md, or examples/*.md does not
     resolve. Backticked paths may also resolve inside templates/team-repo/
     (a team kit's own paths, such as docs/USER-GUIDE.md), and templates/
     paths inside the vault template's 04-agents/ (templates/delivery.md).
     URLs, #anchors, and paths holding < > { } * are skipped; so are listed
     files that do not exist yet.
  7. templates/team-repo/team.json is not valid JSON.
  8. A .py file in the factory does not compile (compiled into a temporary
     folder, so no __pycache__ is left behind).

Warnings (reported, not fatal):
  - An em dash in any template, in process/, docs/, README.md, or
    FACTORY-PROMPT.md.

Output: every error and warning, then "N checks · N errors · N warnings",
where N checks counts the individual file and path checks that ran.

Usage:
    python scripts/check_factory.py
"""
from __future__ import annotations

import json
import os
import py_compile
import re
import sys
import tempfile
from functools import lru_cache
from pathlib import Path
from urllib.parse import unquote

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
SPEC = ROOT / "docs" / "FACTORY-SPEC.md"
TEMPLATES = ROOT / "templates"
TEAM_REPO = TEMPLATES / "team-repo"
VAULT = TEAM_REPO / "kit" / "vault"
AGENTS = VAULT / "04-agents"
KIT_SCRIPTS = {TEAM_REPO / "scripts" / "check_kit.py", TEAM_REPO / "scripts" / "build_zip.py"}
# Skipped by the token and FILL checks: the kit scripts avoid complete markers on purpose,
# and templates/README.md documents the markers (it is never copied into a kit).
MARKER_SKIP = KIT_SCRIPTS | {TEMPLATES / "README.md"}
LINK_SOURCES = ["README.md", "FACTORY-PROMPT.md", "process/*.md", "docs/*.md", "examples/*.md"]
EM_DASH_FOLDERS = ["templates", "process", "docs"]
EM_DASH_FILES = ["README.md", "FACTORY-PROMPT.md"]
SKIP_DIRS = {".git", "__pycache__"}

KNOWN_TYPES = {
    "start-here", "brain", "charter", "workflow", "question-bank",
    "template", "bank", "log", "readme", "install",
}
VERSIONED_TYPES = {
    "start-here", "brain", "charter", "workflow", "question-bank",
    "template", "readme", "install",
}
VERSION_TOKEN = "<<KIT_VERSION>>"

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
CHARTER_TEMPLATES = {
    "_lead-agent.md": LEAD_HEADINGS,
    "_specialist-agent.md": SPECIALIST_HEADINGS,
    "qa-agent.md": QA_HEADINGS,
}
# Brain templates and their fixed core sections (_brain-file.md has none: a FILL writes them).
BRAIN_TEMPLATES = {
    "company.md": ["What we sell", "Who we serve", "How we make money",
                   "What we believe", "What makes us different", "Key facts"],
    "voice.md": ["How we sound", "How we never sound", "Phrases we use",
                 "Banned words and phrases", "Formatting habits", "Spoken voice",
                 "Written voice", "Good examples", "Bad examples",
                 "Rules learned from edits"],
    "plan.md": ["Goal", "Outputs and quantities", "Rhythm", "Delivery", "Authority",
                "Team and handoff", "Areas to avoid"],
    "_brain-file.md": [],
}
BRAIN_END = ["Open questions", "Changelog"]

TOKEN = re.compile(r"<<([^<>\n]+?)>>")
DECLARED_TOKEN = re.compile(r"`<<([^<>`]+)>>`")
FILL = re.compile(r"<!--\s*FILL")
EM_DASH = chr(0x2014)  # written as a code point so this file holds no em dash
HEADING = re.compile(r"^(#{1,6})\s+(.+?)\s*#*\s*$")
COMMENT = re.compile(r"<!--.*?-->", re.S)
INLINE_CODE = re.compile(r"`[^`\n]*`")
MD_LINK = re.compile(r"\[[^\]\n]*\]\(([^)\s]+)[^)\n]*\)")
REPO_PATH = re.compile(r"`((?:process|docs|templates|scripts|examples)/[^`\s]*)`")
URL = re.compile(r"^[A-Za-z][A-Za-z0-9+.-]*:")

errors: list[str] = []
warnings: list[str] = []
texts: dict[Path, str] = {}
checks = 0


# --- helpers ---------------------------------------------------------------

def rel(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return path.as_posix()


def error(path: Path, msg: str) -> None:
    errors.append(f"ERROR {rel(path)}: {msg}")


def warn(path: Path, msg: str) -> None:
    warnings.append(f"WARN  {rel(path)}: {msg}")


def tick(count: int = 1) -> None:
    global checks
    checks += count


def read(path: Path) -> str:
    """The file's text, read once. Unreadable or non-UTF-8 files are reported and read as ""."""
    if path not in texts:
        try:
            texts[path] = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            texts[path] = ""
            error(path, "not valid UTF-8 text")
        except OSError as exc:
            texts[path] = ""
            error(path, f"cannot be read ({exc.strerror})")
    return texts[path]


@lru_cache(maxsize=None)
def listing(folder: Path) -> frozenset:
    try:
        return frozenset(os.listdir(folder))
    except OSError:
        return frozenset()


def exists(path: Path) -> bool:
    """True if the path exists with exactly this letter case (GitHub and Linux care)."""
    path = Path(os.path.normpath(path))
    try:
        parts = path.relative_to(ROOT).parts
    except ValueError:
        return path.exists()
    folder = ROOT
    for part in parts:
        if part not in listing(folder):
            return False
        folder = folder / part
    return True


def inside_root(path: Path) -> bool:
    try:
        Path(os.path.normpath(path)).relative_to(ROOT)
    except ValueError:
        return False
    return True


def walk_files(folder: Path) -> list[Path]:
    """Every file under `folder`, skipping .git/ and __pycache__/."""
    found = []
    for here, dirs, files in os.walk(folder):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        found += [Path(here) / name for name in files]
    return sorted(found, key=rel)


def frontmatter(text: str) -> dict[str, str] | None:
    """Top-level keys of the YAML frontmatter, or None if the file has none."""
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


def h2_headings(path: Path) -> list[str]:
    """The file's ## headings outside fenced blocks and HTML comments."""
    text = COMMENT.sub(lambda m: "\n" * m.group(0).count("\n"), read(path))
    found = []
    for _, line in outside_fences(text):
        match = HEADING.match(line)
        if match and len(match.group(1)) == 2:
            found.append(match.group(2).strip())
    return found


def check_heading_order(path: Path, found: list[str], required: list[str]) -> None:
    for heading in required:
        if heading not in found:
            error(path, f'missing "## {heading}"')
    present = [h for h in found if h in required]
    expected = [h for h in required if h in found]
    if present != expected:
        index = next((i for i, (a, b) in enumerate(zip(present, expected)) if a != b), None)
        if index is None:
            detail = f'"## {present[len(expected)]}" appears twice'
        else:
            detail = f'"## {present[index]}" comes where "## {expected[index]}" belongs'
        error(path, f"required ## headings are out of order ({detail})")


# --- FACTORY-SPEC.md -----------------------------------------------------------

def spec_section(text: str, number: int) -> tuple[str, list[str]] | None:
    """The heading line and body lines of the "## <number>." section."""
    lines = text.splitlines()
    start, fenced = None, False
    for index, line in enumerate(lines):
        if line.lstrip().startswith("```"):
            fenced = not fenced
            continue
        if fenced or not line.startswith("## "):
            continue
        if start is not None:
            return lines[start], lines[start + 1:index]
        if line.startswith(f"## {number}."):
            start = index
    return (lines[start], lines[start + 1:]) if start is not None else None


def check_inventory(spec_text: str) -> None:
    """§17: the files under templates/team-repo/ are exactly the listed ones."""
    section = spec_section(spec_text, 17)
    listed: list[str] = []
    if section is not None:
        fenced = False
        for line in section[1]:
            if line.strip().startswith("```"):
                if fenced:
                    break  # end of the first fenced block
                fenced = True
            elif fenced and line.strip():
                listed.append(line.strip())
    if not listed:
        error(SPEC, 'no file list found in a fenced block under "## 17."')
        return
    stated = re.search(r"(\d+) files", section[0]) if section else None
    if stated and int(stated.group(1)) != len(listed):
        error(SPEC, f"§17 says {stated.group(1)} files but lists {len(listed)}")
    for path in sorted({p for p in listed if listed.count(p) > 1}):
        error(SPEC, f"§17 lists `{path}` more than once")

    expected = set(listed)
    actual = {p.relative_to(TEAM_REPO).as_posix() for p in walk_files(TEAM_REPO)}
    tick(len(expected | actual))
    for path in sorted(expected - actual):
        error(TEAM_REPO / path, "missing (listed in FACTORY-SPEC §17)")
    for path in sorted(actual - expected):
        error(TEAM_REPO / path, "not in the FACTORY-SPEC §17 inventory")


def declared_tokens(spec_text: str) -> set[str]:
    """The backticked tokens in the §6 table."""
    section = spec_section(spec_text, 6)
    names: set[str] = set()
    for line in section[1] if section else []:
        if line.lstrip().startswith("|"):
            names.update(DECLARED_TOKEN.findall(line))
    return names


# --- templates -----------------------------------------------------------------

def check_tokens(files: list[Path], declared: set[str]) -> None:
    for path in files:
        if path in MARKER_SKIP:
            continue
        tick()
        for number, line in enumerate(read(path).splitlines(), 1):
            for name in TOKEN.findall(line):
                if name not in declared:
                    error(path, f"line {number}: token <<{name}>> is not declared in FACTORY-SPEC §6")


def check_fills(files: list[Path]) -> None:
    for path in files:
        if path in MARKER_SKIP:
            continue
        text = read(path)
        for match in FILL.finditer(text):
            tick()
            number = text.count("\n", 0, match.start()) + 1
            end = text.find("-->", match.end())
            next_comment = text.find("<!--", match.end())
            if end == -1 or -1 < next_comment < end:
                error(path, f"line {number}: FILL comment is not closed")
            elif "Source:" not in text[match.start():end]:
                error(path, f'line {number}: FILL comment has no "Source:"')


def check_vault_frontmatter() -> None:
    paths = [p for p in walk_files(VAULT) if p.suffix == ".md"] if VAULT.is_dir() else []
    for path in paths:
        tick()
        fm = frontmatter(read(path))
        if fm is None:
            error(path, "no YAML frontmatter")
            continue
        ftype = fm.get("type", "")
        if ftype not in KNOWN_TYPES:
            error(path, f'unknown or missing type "{ftype}"')
        elif ftype in VERSIONED_TYPES and fm.get("kit_version") != VERSION_TOKEN:
            error(path, f'type "{ftype}" is kit-owned: set kit_version: {VERSION_TOKEN}')


def check_template_headings() -> None:
    for name, required in CHARTER_TEMPLATES.items():
        path = AGENTS / name
        if exists(path):  # a missing template is reported by the inventory check
            tick()
            check_heading_order(path, h2_headings(path), required)

    for name, core in BRAIN_TEMPLATES.items():
        path = VAULT / "01-brain" / name
        if not exists(path):
            continue
        tick()
        found = h2_headings(path)
        check_heading_order(path, found, ["TL;DR", *core, *BRAIN_END])
        if "TL;DR" in found and found[0] != "TL;DR":
            error(path, f'the first "## " heading must be "TL;DR" (found "{found[0]}")')
        if all(h in found for h in BRAIN_END) and found[-2:] != BRAIN_END:
            error(path, 'the last "## " headings must be "Open questions", then "Changelog"')

    workflows = AGENTS / "workflows"
    paths = [p for p in walk_files(workflows) if p.parent == workflows and p.suffix == ".md"] \
        if workflows.is_dir() else []
    for path in paths:
        if path.name == "README.md":
            continue
        tick()
        found = h2_headings(path)
        first = found[0] if found else "none"
        last = found[-1] if found else "none"
        if first != "Purpose":
            error(path, f'the first "## " heading must be "Purpose" (found "{first}")')
        if not last.lower().endswith("checklist"):
            error(path, f'the last "## " heading must end with "Checklist" (found "{last}")')


def check_team_json() -> None:
    path = TEAM_REPO / "team.json"
    if not path.is_file():
        return  # reported by the inventory check
    tick()
    try:
        json.loads(read(path))
    except json.JSONDecodeError as exc:
        error(path, f"not valid JSON ({exc})")


# --- docs, links, Python -------------------------------------------------------

def check_em_dashes() -> None:
    files: list[Path] = []
    for folder in EM_DASH_FOLDERS:
        if (ROOT / folder).is_dir():
            files += walk_files(ROOT / folder)
    files += [ROOT / name for name in EM_DASH_FILES if (ROOT / name).is_file()]
    for path in files:
        tick()
        for number, line in enumerate(read(path).splitlines(), 1):
            if EM_DASH in line:
                warn(path, f"line {number}: em dash")


def skipped(target: str) -> bool:
    return bool(URL.match(target)) or target.startswith("#") or any(c in target for c in "<>{}*")


def check_links() -> None:
    sources: list[Path] = []
    for pattern in LINK_SOURCES:
        sources += sorted((p for p in ROOT.glob(pattern) if p.is_file()), key=rel)
    for source in sources:  # files not written yet are simply not found
        for number, line in outside_fences(read(source)):
            for target in MD_LINK.findall(INLINE_CODE.sub("", line)):
                if skipped(target):
                    continue
                clean = unquote(target.split("#", 1)[0].split("?", 1)[0])
                if not clean:
                    continue
                tick()
                base = ROOT if clean.startswith("/") else source.parent
                resolved = base / clean.lstrip("/")
                if not inside_root(resolved):
                    error(source, f"line {number}: link ({target}) points outside the factory repo")
                elif not exists(resolved):
                    error(source, f"line {number}: broken link ({target})")
            for path_text in REPO_PATH.findall(line):
                if skipped(path_text):
                    continue
                tick()
                clean = path_text.split("#", 1)[0]
                bases = [ROOT, TEAM_REPO] + ([AGENTS] if clean.startswith("templates/") else [])
                if not any(exists(base / clean) for base in bases):
                    error(source, f"line {number}: missing path `{path_text}`")


def check_python() -> None:
    files = [p for p in walk_files(ROOT) if p.suffix == ".py"]
    with tempfile.TemporaryDirectory() as tmp:
        for index, path in enumerate(files):
            tick()
            try:
                py_compile.compile(str(path), cfile=os.path.join(tmp, f"{index}.pyc"), doraise=True)
            except py_compile.PyCompileError as exc:
                value = exc.exc_value
                line = getattr(value, "lineno", None)
                where = f"line {line}: " if line else ""
                error(path, f"does not compile: {where}{exc.exc_type_name}: {getattr(value, 'msg', value)}")
            except OSError as exc:
                error(path, f"cannot be compiled ({exc.strerror})")


def main() -> int:
    template_files = walk_files(TEMPLATES) if TEMPLATES.is_dir() else []
    if not SPEC.is_file():
        error(SPEC, "missing: the inventory and token checks need it")
    else:
        spec_text = read(SPEC)
        check_inventory(spec_text)
        declared = declared_tokens(spec_text)
        if declared:
            check_tokens(template_files, declared)
        else:
            error(SPEC, 'no token table found under "## 6."')
    check_fills(template_files)
    check_vault_frontmatter()
    check_template_headings()
    check_team_json()
    check_em_dashes()
    check_links()
    check_python()

    for line in errors + warnings:
        print(line)
    print(f"\n{checks} checks · {len(errors)} errors · {len(warnings)} warnings")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
