# process/

The factory's step-by-step process. The builder (Claude Code) reads [00-builder-charter.md](00-builder-charter.md) first, then works through the stages in order.

| File | Stage | Output | Gate |
|---|---|---|---|
| [00-builder-charter.md](00-builder-charter.md) | Rules for the builder | | Read before stage 1 |
| [01-intake.md](01-intake.md) | 1. Intake | `docs/TEAM-BRIEF.md` | All 12 fields answered; no design-changing gap |
| [02-blueprint.md](02-blueprint.md) | 2. Blueprint | Approved blueprint, `team.json`, `docs/TEAM-SPEC.md`, scaffold | Written approval |
| [03-question-design.md](03-question-design.md) | 3. Questions | Setup interview + routine questions | Full coverage; every question passes the checklist |
| [04-build.md](04-build.md) | 4. Build | Every FILL written | Zero FILL markers left |
| [05-check.md](05-check.md) | 5. Check | Clean kit | Checker 0/0; review and dry run fixed |
| [06-ship.md](06-ship.md) | 6. Ship | Repo, zip, handoff | Requester has both start prompts |

Rules for editing these files:
1. Change [../docs/FACTORY-SPEC.md](../docs/FACTORY-SPEC.md) first when a change touches layout, names, tokens, or checks.
2. Keep stage numbers and file names stable: kits and chats refer to them.
3. Run `python scripts/check_factory.py` after any change.
