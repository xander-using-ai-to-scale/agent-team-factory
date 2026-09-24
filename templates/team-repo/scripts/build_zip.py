#!/usr/bin/env python3
"""Rebuild dist/<team_slug>-kit-v<kit_version>.zip from the kit/ folder.

The zip contains a top-level `kit/` folder, so `kit/INSTALL.md` is the same
path in the zip and in the repo. The slug and version come from team.json
(`team_slug`, `kit_version`). Older zips of this team's kit in dist/ are
removed so only the current one ships. Hidden files and folders (such as
.obsidian/) and __pycache__ folders are left out. Timestamps are fixed so
identical content gives an identical zip.

Run scripts/check_kit.py first: a kit ships only at 0 errors and 0 warnings.

Usage:
    python scripts/build_zip.py
"""
from __future__ import annotations

import json
import re
import sys
import zipfile
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
KIT = ROOT / "kit"
TEAM_JSON = ROOT / "team.json"
DIST = ROOT / "dist"
FIXED_TIME = (2026, 1, 1, 0, 0, 0)
FILE_MODE = 0o644 * 0x10000  # Unix permissions rw-r--r--, stored in the high 16 bits
SLUG = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
VERSION = re.compile(r"^[0-9]+\.[0-9]+\.[0-9]+$")


def team_values() -> tuple[str, str]:
    """(team_slug, kit_version) from team.json."""
    try:
        team = json.loads(TEAM_JSON.read_text(encoding="utf-8"))
    except FileNotFoundError:
        sys.exit(f"team.json not found: {TEAM_JSON}")
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        sys.exit(f"team.json is not valid JSON: {exc}")
    if not isinstance(team, dict):
        sys.exit("team.json must be a JSON object")
    slug, version = team.get("team_slug"), team.get("kit_version")
    if not isinstance(slug, str) or not SLUG.match(slug):
        sys.exit(f"team_slug in team.json is not a valid slug: {slug!r}")
    if not isinstance(version, str) or not VERSION.match(version):
        sys.exit(f"kit_version in team.json is not X.Y.Z: {version!r}")
    return slug, version


def included(path: Path) -> bool:
    """False for hidden files and folders (.obsidian/, .DS_Store) and __pycache__."""
    return not any(
        part.startswith(".") or part == "__pycache__" for part in path.relative_to(KIT).parts
    )


def main() -> None:
    slug, version = team_values()
    if not KIT.is_dir():
        sys.exit(f"kit/ folder not found: {KIT}")
    DIST.mkdir(exist_ok=True)
    out = DIST / f"{slug}-kit-v{version}.zip"

    older = re.compile("^" + re.escape(slug) + r"-kit-v[0-9]+\.[0-9]+\.[0-9]+\.zip$")
    for old in DIST.glob("*.zip"):
        if old != out and older.match(old.name):
            old.unlink()

    files = sorted(
        (p for p in KIT.rglob("*") if p.is_file() and included(p)),
        key=lambda p: p.relative_to(KIT).as_posix(),
    )
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in files:
            arcname = (Path("kit") / path.relative_to(KIT)).as_posix()
            info = zipfile.ZipInfo(arcname, date_time=FIXED_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = FILE_MODE
            zf.writestr(info, path.read_bytes())

    size_kb = out.stat().st_size / 1024
    print(f"Built {out.relative_to(ROOT).as_posix()} · {len(files)} files · {size_kb:.1f} KB")


if __name__ == "__main__":
    main()
