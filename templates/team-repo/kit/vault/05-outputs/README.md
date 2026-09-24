---
type: readme
folder: 05-outputs
kit_version: <<KIT_VERSION>>
---

# 05-outputs

## Purpose
Output. Every <<OUTPUT_UNIT>> gets 1 folder here holding its tickets, drafts, QA report, and the client deliverable.

## What goes here
1 folder per <<OUTPUT_UNIT>>, named `{{output_id}}`, holding only the files for work actually done:
```
05-outputs/{{output_id}}/
├── 00-summary.md       <<LEAD_SHORT>>: status, contents, receipts, QA verdicts
<!-- FILL: one tree line per specialist, in team.json order: "├── <output_file>   <specialist name> (<when it runs: every <<OUTPUT_UNIT>>, if active, or on demand only>)", with the descriptions aligned like the lines around it. Source: team.json specialists[].output_file, .name, .on_demand_only; plan.md Outputs and quantities defaults. Length: 1 line per specialist. Example: kit/The-Almanac/05-packs/README.md tree, lines 01-pillar.md to 08-vsl.md. -->
├── qa-report.md        QA Agent
├── DELIVERY.md         <<LEAD_SHORT>>: the client deliverable
└── tickets/            One job ticket per specialist
```
On-demand <<OUTPUT_UNIT_PLURAL>> hold only the requested file(s), `00-summary.md`, `qa-report.md`, `DELIVERY.md`, and `tickets/`. `tickets/` holds 1 job ticket per specialist, named after the specialist's charter file. Example (fictional): `tickets/report-agent.md`.

## What never goes here
- Client answers and documents: [[02-sources/README]]. New bank entries: [[03-banks/README]]. Blank templates: [[04-agents/templates/README]].
- Client edits and reported winners: [[06-log/edits-log]], [[06-log/winners]]. Loose files: nothing sits directly in `05-outputs/` except this README.

## File naming
- From <<ROUTINE_NAME>> answers: `YYYY-MM-DD-{{slug}}`; bank <<OUTPUT_UNIT>>: `YYYY-MM-DD-bank-{{slug}}`; on-demand <<OUTPUT_UNIT>>: `YYYY-MM-DD-od-{{slug}}`.
- Date = the delivery day the <<OUTPUT_UNIT>> is for (on-demand: the day the client asked). Slug = 2 to 5 lowercase words from the core idea (on-demand: the requested topic), kebab-case, max 40 characters.
Example (fictional): `2026-10-12-spring-price-update`, `2026-10-26-bank-referral-habits`, `2026-10-14-od-welcome-letter`

## Frontmatter for files here
Output files (the specialists' files):
```
---
type: output-file
output_id: {{output_id}}
agent: {{exact agent name}}
status: draft
revision: 1
created: {{YYYY-MM-DD}}
---
```
- `00-summary.md`: frontmatter exactly as in [[04-agents/templates/output-summary]].
- Tickets: frontmatter exactly as in [[04-agents/templates/job-ticket]].
- `qa-report.md`: frontmatter exactly as in [[04-agents/templates/qa-report]].
- `DELIVERY.md`: no frontmatter; it starts with its H1, as in [[04-agents/templates/delivery]].
- Output file statuses: `draft` (waiting for QA) · `qa-pass` (every QA check passed) · `qa-fix` (exact fixes listed, waiting for a revision) · `qa-fail` (must be rewritten) · `held-back` (no pass after 3 QA rounds; listed under `## Held back` in `DELIVERY.md`).

## Who writes
The tree above names each file's writer. The <<LEAD_NAME>> (<<LEAD_SHORT>>) also writes every ticket and, in packet mode or mode fallback, saves the agent's reply to that agent's file. The QA Agent sets `qa-pass`, `qa-fix`, or `qa-fail` on the file it checked; only the <<LEAD_SHORT>> sets `held-back`.

## Who reads
Each specialist: its own ticket, plus the outputs its routing row lists (the outputs it depends on). QA Agent: the draft, the draft's ticket, and the outputs the draft depends on. <<LEAD_SHORT>>: every file. The client: `DELIVERY.md` only.

## Rules
1. `DELIVERY.md` is the only client deliverable. Never send the client any other file from this folder.
2. Latest <<OUTPUT_UNIT>> = the folder with the newest date prefix. For the latest regular or bank <<OUTPUT_UNIT>>, skip `-od-` folders.
3. Never delete, rename, or move an output folder or file, however old.
4. Every output file starts with its LOADED receipt on the first line after the frontmatter. `DELIVERY.md` has the `Built from:` line directly under its H1 instead.
5. A revision replaces the file's content, increases `revision` by 1, and resets `status` to `draft`. Max 3 QA rounds per file.
6. No ticket goes out before every output it depends on has `status: qa-pass` (rule 10 in [[00-START-HERE]]).
7. Once `00-summary.md` shows `status: delivered`, never change any file in that folder.
