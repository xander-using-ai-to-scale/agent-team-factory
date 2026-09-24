#!/usr/bin/env python3
"""Scaffold a new team kit from the factory templates (stage 2, last step).

Reads <team folder>/team.json, then copies every file in templates/team-repo/
into the team folder:
  - replaces every <<TOKEN>> with its value from team.json (FACTORY-SPEC §6),
  - copies each per-item template (_name) once per item and renames it (§5),
  - renames kit/vault/ to kit/<vault_folder>/ and gitignore.txt to .gitignore,
  - never overwrites a file that already exists (team.json, docs/TEAM-BRIEF.md,
    and docs/TEAM-SPEC.md are written before scaffolding and are kept); only the
    build-time tokens inside kept .md files are filled in,
  - writes each Hermes skill's name, description, and body for its agent.

After this runs, the only things left to write are the FILL comments.

Usage:
    python scripts/scaffold_team.py <team folder>
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

FACTORY = Path(__file__).resolve().parent.parent
TEMPLATES = FACTORY / "templates" / "team-repo"
TOKEN = re.compile("<" + "<([A-Z][A-Z0-9_]*)>" + ">")
REQUIRED_KEYS = [
    "kit_version", "release_date", "team_name", "team_slug", "team_purpose",
    "vault_name", "vault_folder", "output_unit", "output_unit_plural",
    "routine_name", "lead", "qa", "specialists", "brain_files", "banks", "schedules",
]


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    sys.exit(1)


def load_team(team_dir: Path) -> dict:
    path = team_dir / "team.json"
    if not path.exists():
        fail(f"{path} not found. Write team.json first (process/02-blueprint.md).")
    try:
        team = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"team.json is not valid JSON: {exc}")
    missing = [key for key in REQUIRED_KEYS if key not in team]
    if missing:
        fail(f"team.json is missing: {', '.join(missing)}")
    if not team["specialists"]:
        fail("team.json has no specialists")
    if not team["banks"]:
        fail("team.json has no banks")
    return team


def token_values(team: dict) -> dict[str, str]:
    lead_file = team["lead"]["file"]
    return {
        "TEAM_NAME": team["team_name"],
        "TEAM_SLUG": team["team_slug"],
        "TEAM_PURPOSE": team["team_purpose"],
        "VAULT_NAME": team["vault_name"],
        "VAULT_FOLDER": team["vault_folder"],
        "LEAD_NAME": team["lead"]["name"],
        "LEAD_SHORT": team["lead"]["short"],
        "LEAD_FILE": lead_file[:-3] if lead_file.endswith(".md") else lead_file,
        "KIT_VERSION": team["kit_version"],
        "RELEASE_DATE": team["release_date"],
        "OUTPUT_UNIT": team["output_unit"],
        "OUTPUT_UNIT_PLURAL": team["output_unit_plural"],
        "ROUTINE_NAME": team["routine_name"],
        "SPECIALIST_COUNT": str(len(team["specialists"])),
        "SUBAGENT_COUNT": str(len(team["specialists"]) + 1),
        "BRAIN_FILE_COUNT": str(len(team["brain_files"])),
    }


ARTICLE_BEFORE_TOKEN = re.compile(r"\b([Aa]) (?=" + "<" + "<([A-Z][A-Z0-9_]*)>" + ">)")


def article(word: str) -> str:
    """'a' or 'an' for the start of word (hour → an, unit/user/one → a, HR/SEO → an)."""
    raw = word.strip()
    if len(raw) >= 2 and raw[:2].isalpha() and raw[:2].isupper():
        return "an" if raw[0] in "AEFHILMNORSX" else "a"  # acronyms: said letter by letter
    w = raw.lower()
    if w.startswith(("hour", "honest", "honor", "heir")):
        return "an"
    if w.startswith(("uni", "use", "usu", "uti", "ure", "eu", "one", "once")):
        return "a"
    return "an" if w[:1] in ("a", "e", "i", "o", "u") else "a"


def fix_articles(text: str, values: dict[str, str]) -> str:
    """Make 'a <<TOKEN>>' read 'an <value>' when the value starts with a vowel sound."""
    def repl(match: re.Match) -> str:
        value = values.get(match.group(2))
        if value is None:
            return match.group(0)
        chosen = article(value)
        return (chosen.capitalize() if match.group(1) == "A" else chosen) + " "
    return ARTICLE_BEFORE_TOKEN.sub(repl, text)


YOUR_VAULT = re.compile(r"\b([Yy])our (?=" + "<" + "<VAULT_NAME>" + ">)")


def fix_wording(text: str, values: dict[str, str]) -> str:
    """Before tokens are replaced: "your The Ledger" becomes "The Ledger"."""
    if values.get("VAULT_NAME", "").startswith("The "):
        text = YOUR_VAULT.sub("", text)
    return text


def fix_counts(text: str) -> str:
    """After tokens are replaced: "1 specialists" becomes "1 specialist"."""
    text = re.sub(r"\b1 specialists\b", "1 specialist", text)
    return re.sub(r"\b1 rows\b", "1 row", text)


def stem(file_name: str) -> str:
    return file_name[:-3] if file_name.endswith(".md") else file_name


SKILL_TEMPLATE = "kit/hermes-skills/_agent-skill/SKILL.md"
FILL_BLOCK = re.compile(r"<!-- FILL:.*?-->\n?", re.S)
LEAD_TEXT = re.compile(r"^- - - - -\n(.*?)\n- - - - -$", re.S | re.M)


def skill_agents(team: dict) -> list[tuple[str, str, str, bool]]:
    """(destination, agent name, charter stem, is lead) for every Hermes skill copy."""
    agents = [(team["lead"]["name"], team["lead"]["file"], True), (team["qa"]["name"], team["qa"]["file"], False)]
    agents += [(s["name"], s["file"], False) for s in team["specialists"]]
    return [(f"kit/hermes-skills/{stem(f)}/SKILL.md", n, stem(f), lead) for n, f, lead in agents]


def skill_trigger(team: dict, name: str, file_stem: str, is_lead: bool) -> str:
    """The shortest-fitting 'Use when ...' text: Hermes refuses descriptions over 60 characters."""
    if is_lead:
        options = [f"working as the {name} for the client", f"working as the {name}", f"running the {team['team_name']}"]
    else:
        options = [f"doing {article(name)} {name} job for the {team['team_name']}",
                   f"doing {article(name)} {name} job", f"doing {file_stem} work"]
    for option in options:
        if len(f"Use when {option}.") <= 60:
            return option
    return options[-1][:49]


def fill_skill(text: str, team: dict, name: str, file_stem: str, is_lead: bool) -> tuple[str, bool]:
    """Resolve the per-agent placeholders of one Hermes skill copy (the FILLs in the template)."""
    lead = LEAD_TEXT.search(text)
    if lead is None or len(FILL_BLOCK.findall(text)) != 2 or "# AGENT-NAME" not in text:
        return text, False  # unexpected template shape: leave the FILLs for the builder
    lead_text = lead.group(1)
    text = FILL_BLOCK.sub("", text)
    if is_lead:
        text = text[: text.index("# AGENT-NAME")] + lead_text + "\n"
    text = text.replace("AGENT-FILE-STEM", file_stem).replace("AGENT-NAME", name)
    text = text.replace("AGENT-JOB-TRIGGER", skill_trigger(team, name, file_stem, is_lead))
    return re.sub(r"\n{3,}", "\n\n", text), True


def destinations(rel: str, team: dict) -> list[str]:
    """Where one template file goes in the team repo (empty list = nowhere)."""
    vault = team["vault_folder"]
    if rel == "gitignore.txt":
        return [".gitignore"]
    if rel == "kit/vault/01-brain/_brain-file.md":
        return [f"kit/{vault}/01-brain/{b['file']}" for b in team["brain_files"] if not b.get("core")]
    if rel == "kit/vault/03-banks/_bank.md":
        return [f"kit/{vault}/03-banks/{b['file']}" for b in team["banks"]]
    if rel == "kit/vault/04-agents/_lead-agent.md":
        return [f"kit/{vault}/04-agents/{team['lead']['file']}"]
    if rel == "kit/vault/04-agents/_specialist-agent.md":
        return [f"kit/{vault}/04-agents/{s['file']}" for s in team["specialists"]]
    if rel == "kit/hermes-skills/_agent-skill/SKILL.md":
        agents = [team["lead"]["file"], team["qa"]["file"]] + [s["file"] for s in team["specialists"]]
        return [f"kit/hermes-skills/{stem(f)}/SKILL.md" for f in agents]
    if rel.startswith("kit/vault/"):
        return [f"kit/{vault}/" + rel[len("kit/vault/"):]]
    return [rel]


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 1
    team_dir = Path(sys.argv[1]).resolve()
    if team_dir == FACTORY or FACTORY in team_dir.parents:
        fail("build the team repo outside the factory folder (next to it).")
    team = load_team(team_dir)
    values = token_values(team)

    skills = {dest: (name, file_stem, lead) for dest, name, file_stem, lead in skill_agents(team)}
    created, kept, per_item, unknown, skill_notes = [], [], [], set(), []
    for template in sorted(p for p in TEMPLATES.rglob("*") if p.is_file()):
        rel = template.relative_to(TEMPLATES).as_posix()
        if "__pycache__" in rel:
            continue
        for dest_rel in destinations(rel, team):
            dest = team_dir / dest_rel
            if dest.exists():
                kept.append(dest_rel)
                continue
            dest.parent.mkdir(parents=True, exist_ok=True)
            if template.suffix == ".py":
                dest.write_bytes(template.read_bytes())
            else:
                text = template.read_text(encoding="utf-8")
                for name in TOKEN.findall(text):
                    if name not in values:
                        unknown.add(f"{rel}: {name}")
                text = fix_articles(fix_wording(text, values), values)
                text = fix_counts(TOKEN.sub(lambda m: values.get(m.group(1), m.group(0)), text))
                if rel == SKILL_TEMPLATE and dest_rel in skills:
                    text, done = fill_skill(text, team, *skills[dest_rel])
                    skill_notes.append(f"{dest_rel}: {'filled' if done else 'left for the builder (template shape changed)'}")
                dest.write_text(text, encoding="utf-8", newline="\n")
            created.append(dest_rel)
            if template.name.startswith("_") or template.parent.name.startswith("_"):
                per_item.append(f"{dest_rel}  (from {rel})")

    # Files written before the scaffold (TEAM-BRIEF.md, TEAM-SPEC.md) keep their text,
    # but their build-time tokens are filled in too.
    tokens_filled = []
    for dest_rel in kept:
        path = team_dir / dest_rel
        if path.suffix != ".md":
            continue
        text = path.read_text(encoding="utf-8")
        if not TOKEN.search(text):
            continue
        for name in TOKEN.findall(text):
            if name not in values:
                unknown.add(f"{dest_rel}: {name}")
        text = TOKEN.sub(lambda m: values.get(m.group(1), m.group(0)), fix_articles(text, values))
        path.write_text(text, encoding="utf-8", newline="\n")
        tokens_filled.append(dest_rel)

    print(f"Scaffolded {team['team_name']} into {team_dir}")
    if tokens_filled:
        print(f"  tokens filled in kept files: {', '.join(tokens_filled)}")
    print(f"  created: {len(created)} files")
    print(f"  kept (already existed): {len(kept)} files" + (f" ({', '.join(kept)})" if kept else ""))
    print("  per-item files:")
    for line in per_item:
        print(f"    {line}")
    if skill_notes:
        print("  Hermes skills (name, description, and lead body written automatically):")
        for line in skill_notes:
            print(f"    {line}")
    if unknown:
        print("ERROR: unknown tokens (not in FACTORY-SPEC §6):")
        for item in sorted(unknown):
            print(f"    {item}")
        return 1
    fills = sum(
        (team_dir / d).read_text(encoding="utf-8").count("<!-- FILL")
        for d in created if not d.endswith(".py")
    )
    print(f"Next: write the {fills} FILL sections (process/03-question-design.md, then process/04-build.md).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
