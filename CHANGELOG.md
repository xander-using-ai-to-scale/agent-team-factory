# Changelog

## 1.0.1 · 2026-09-25

End-to-end test: a small SEO team was built with the factory and passed its checker (0 errors, 0 warnings). Fixes from that test:

- Scaffold: picks "a" or "an" before names, writes "The Ledger" instead of "your The Ledger", "1 specialist" and "1 row" in the singular, fills tokens in TEAM-BRIEF and TEAM-SPEC, and writes every Hermes skill automatically.
- Checker: validates Hermes skill names and descriptions (60-character limit) and bans words Hermes flags in team slugs.
- Build process: fill TEAM-SPEC and the START-HERE routing table before starting helper agents.
- Templates: a Notes column on plan.md outputs, rule 10 allows named fallbacks, clearer pushback-round targets, excerpts allowed for long example outputs, and smaller wording fixes.

## 1.0.0 · 2026-09-25

First release.

- Six-stage process: intake, blueprint, question design, build, check, ship, plus the builder charter.
- FACTORY-SPEC: team-kit and vault layout, template markers, 16 tokens, the team.json contract, fixed names, required headings, the 18 universal rules, routing rows, authority levels, platform mapping, writing rules, checker rules, and the 55-file template inventory.
- 55 templates generalized from the Content Grokbot kit v1.0.0: the full Obsidian vault, lead, QA, and specialist charters, 6 workflows, question-bank skeletons, output templates, Grokbot and Hermes installs, Hermes skills, user guide, TEAM-BRIEF and TEAM-SPEC.
- Question design as a method, not a question list: the rules, techniques, coverage map, and checklist the builder uses to write each team's own questions.
- Scripts: `scaffold_team.py` (templates + tokens from team.json), a team.json-driven `check_kit.py` and `build_zip.py` for every kit, and `check_factory.py` for the factory itself.
- Hermes support built from the Hermes Agent docs (see docs/HERMES-NOTES.md).
