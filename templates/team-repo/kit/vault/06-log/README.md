---
type: readme
folder: 06-log
kit_version: <<KIT_VERSION>>
---

# 06-log

## Purpose
History: what happened in each session, what the client changed, what performed, what is still unknown, and which <<ROUTINE_NAME>> questions were asked.

## What goes here
Exactly these 5 files. Never create another file here.
- [[06-log/session-log]]: 1 entry per session. The newest `State:` line is where the next session resumes.
- [[06-log/edits-log]]: client edits to drafts and the voice rule proposed from each pattern (E-###).
- [[06-log/winners]]: work the client reports as performing well (W-###).
- [[06-log/open-questions]]: facts still missing from a brain file (Q-###).
- [[06-log/questions-asked]]: every <<ROUTINE_NAME>> question sent, so none repeats within 8 weeks.

## What never goes here
- Raw client answers and documents: [[02-sources/README]]. Approved facts and voice rules: [[01-brain/README]].
- Bank entries: [[03-banks/README]]. Drafts, tickets, QA reports: [[05-outputs/README]].

## File naming
Fixed names: `session-log.md`, `edits-log.md`, `winners.md`, `open-questions.md`, `questions-asked.md`. Never rename them.

## Frontmatter for files here
```
---
type: log
name: {{session-log | edits-log | winners | open-questions | questions-asked}}
updated: {{YYYY-MM-DD}}
next_id: {{E-### | W-### | Q-###}}
---
```
Only `edits-log.md` (E-###), `winners.md` (W-###), and `open-questions.md` (Q-###) have `next_id`. `session-log.md` and `questions-asked.md` leave that line out.

## Who writes
The <<LEAD_NAME>> (<<LEAD_SHORT>>) only. Sub-agents never write here.

## Who reads
- <<LEAD_SHORT>> at every session start: the newest 3 entries in `session-log.md` and the open items in `open-questions.md`.
- <<LEAD_SHORT>> during work: `questions-asked.md` (writing <<ROUTINE_NAME>> questions), `edits-log.md` (learning loop), and `open-questions.md`, `winners.md`, `edits-log.md` in full (monthly review).
- No sub-agent reads this folder.

## Rules
1. Newest first in every log: each new entry goes directly under the comment line in `## Entries`; in `questions-asked.md`, new rows go directly under the table's 2 header rows.
2. Each log holds its exact entry format under `## Entry format`. Copy it and fill every field.
3. IDs: prefix + 3 digits, zero-padded. Take the ID from `next_id`, then increase `next_id` by 1. Never reuse or renumber an ID.
4. Set `updated` to today's date whenever you add or change an entry.
5. Never delete an entry. After writing, change only the fields that the log's own rules allow.
6. Dates `YYYY-MM-DD`; times 24-hour `HH:MM` in the client's timezone from [[01-brain/plan#Rhythm]] (device time until it is set).
7. Output labels in headings: the output file's name without its number and `.md` (for example article, from 01-article.md).
8. Write each log entry in the same session as the event it records.
