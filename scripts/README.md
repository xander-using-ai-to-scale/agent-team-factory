# scripts/

| Script | When | What it does |
|---|---|---|
| `scaffold_team.py` | Stage 2, after team.json is written | Copies the 55 templates into the team folder, replaces every token from team.json, creates the per-item files, and keeps files that already exist. Usage: `python agent-team-factory/scripts/scaffold_team.py <team folder>` |
| `check_factory.py` | After any change to the factory | Validates the factory itself: the template inventory, tokens, FILL markers, required headings, links, team.json template, and Python syntax. Usage: `python scripts/check_factory.py` |

The scripts every team kit gets (`check_kit.py`, `build_zip.py`) live in `templates/team-repo/scripts/` and are copied into each kit by the scaffold.

Python 3.8 or newer, standard library only.
