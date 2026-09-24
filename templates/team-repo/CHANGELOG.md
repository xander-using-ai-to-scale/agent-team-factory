# Changelog

All kit versions. The rule for changes: edit `docs/TEAM-SPEC.md` first (and `team.json` when the blueprint changes), then the kit files, then this file. Run `python scripts/check_kit.py` (0 errors, 0 warnings), then rebuild the zip with `python scripts/build_zip.py`. Add upgrade steps for existing installs to the "Version notes" section of `kit/INSTALL.md` and `kit/INSTALL-HERMES.md`.

## <<KIT_VERSION>> · <<RELEASE_DATE>>

First release. Built with the Agent Team Factory v1.0.0.

- **<<LEAD_NAME>>** lead agent + <<SUBAGENT_COUNT>> sub-agents: QA Agent, <!-- FILL: every specialist's exact name in team.json → specialists order, comma-separated, ending with a period. Source: team.json → specialists (name). Length: 1 line. Example: content kit CHANGELOG.md, first bullet. -->
- **<<VAULT_NAME>>** vault: 01-brain, 02-sources, 03-banks, 04-agents, 05-outputs, 06-log, with a README in every folder and a router file (`00-START-HERE.md`).
- **<<BRAIN_FILE_COUNT>> brain files**: company, voice (with a default anti-AI banned list), plan (with the client-approved Authority list)<!-- FILL: ", " plus each domain brain file name without .md, in team.json order; no domain files: delete this comment. Source: team.json → brain_files (core: false). Length: 1 line. Example: content kit CHANGELOG.md, third bullet. -->.
- **Banks**: <!-- FILL: every bank title with its ID prefix in parentheses, comma-separated, for example "Ideas (I-###)". Source: team.json → banks (title, id_prefix). Length: 1 line. Example: content kit CHANGELOG.md has no bank bullet; follow the brain files bullet above. -->
- **Setup interview**: interview-first, optional drops (never homework), exact-words-from-memory questions, a 5-question pushback round, a 60-second voice memo, this-or-that voice calibration, and client approval of the output mix and the authority lists.
- **The <<ROUTINE_NAME>>**: 5 questions the day before delivery day, answered by voice memo or text; no question repeats within 8 weeks.
- **Production**: dependencies first → QA (10 universal checks plus this team's checks, max 3 rounds) → `DELIVERY.md`.
- **Authority**: draft-only by default; the client approves what the team may do alone and what needs a yes each time; spending money, passwords and payment details, deleting accounts or data, and account settings are never allowed.
- **Learning loop**: client edits become voice rules (client-approved); winners are logged with why they worked.
- **Enforced read-first**: routing table, LOADED receipts, BLOCKED replies, hard stop, TL;DR headers.
- **Schedules**: routine-send, routine-reminder, feedback-check, monthly-review.
- **Platforms**: Grokbot (`kit/INSTALL.md`) and Hermes (`kit/INSTALL-HERMES.md`, `kit/hermes-skills/`), one shared vault.
- **Fallbacks**: packet mode (sub-agents can't read the vault), mode fallback (sub-agent unavailable).
<!-- FILL: 3 to 5 bullets on what is specific to this team, in the same "**Label**: detail" format: the production order in one line, the default contents of one <<OUTPUT_UNIT>>, the team's own QA checks, the number of <<ROUTINE_NAME>> question categories, and any extra schedule. Source: TEAM-SPEC §1 (blueprint), §11.6 (team checks), §12.3, §12.4, §14, §15. Length: 3 to 5 bullets, max 25 words each. Example: content kit CHANGELOG.md, the "Ritual" and "Pillar-first waterfall" bullets. -->
