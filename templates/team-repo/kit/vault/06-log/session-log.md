---
type: log
name: session-log
updated: ""
---

# Session log

What the <<LEAD_NAME>> (<<LEAD_SHORT>>) did in each session, newest first.
The `State:` line of the newest entry is where the next session resumes.

## Entry format
```
## {{YYYY-MM-DD HH:MM}} · {{Setup | Routine | Production | Feedback | Monthly review | On-demand | Install | Other}}
- Did: {{1–3 bullets}}
- Changed: {{files created or changed, or "nothing"}}
- State: {{e.g. "Setup 3/6 · Company section · Q4 of 7" or "<<OUTPUT_UNIT>> 2026-10-05-spring-update delivered"}}
- Next: {{next action + when}}
- Waiting on client: {{item, or "nothing"}}
```
Example (fictional):
```
## 2026-10-06 16:40 · Setup
- Did:
  - Finished the Company section (7 questions, 2 skipped as Q-003 and Q-004)
  - Drafted the company file and sent its TL;DR for review
- Changed: 01-brain/company.md, 02-sources/interview/2026-10-06-setup-interview.md, 06-log/open-questions.md
- State: Setup 4/6 · Company section · draft sent, waiting for approval
- Next: apply the client's fixes, then ask the first question of the next section as soon as the client replies
- Waiting on client: fixes or OK on the company file draft
```

## Rules
1. The <<LEAD_SHORT>> writes 1 entry at the end of every session. A session ends when you finish a workflow run, deliver the <<OUTPUT_UNIT>>, or stop to wait for the client or a schedule. During setup, write 1 entry per finished interview section and 1 whenever the client pauses.
2. Put each new entry directly under the comment line in `## Entries`. Never remove that comment.
3. `State:` must let a session with zero memory resume without asking the client: for setup, the step, section, and question number; for production, the output id and the workflow step. Never write only "in progress".
   Example (fictional): `State: <<OUTPUT_UNIT>> 2026-10-12-spring-price-update · step 5 · QA round 2 on the report file`
4. `Did:` holds 1 to 3 items, each on its own line as a nested bullet (2 spaces, then `- `).
5. `Changed:` lists vault paths from the vault root, separated by commas, or `nothing`.
6. At every session start, read the newest 3 entries, then resume from the newest `State:` line.
7. If the vault shows work newer than the newest entry (for example, interview answers saved after its time), write the missing entry first, with `State:` taken from the files.
8. Heading time: 24-hour, in the client's timezone from [[01-brain/plan#Rhythm]] (device time until it is set). Heading type: exactly 1 of the 8 types in the format.
9. Never edit or delete an entry. Correct a mistake with a new entry.

## Entries
<!-- Newest first. No entries yet. -->
