---
type: log
name: questions-asked
updated: ""
---

# Questions asked

Every <<ROUTINE_NAME>> question sent to the client, exactly as sent, newest first.
Read it before writing new <<ROUTINE_NAME>> questions so none repeats within 8 weeks.

## Entry format
```
| Date | Category | Question (as sent) | Answered |
|---|---|---|---|
| 2026-09-27 | {{category}} | {{question}} | yes |
```

## Rules
1. Log the questions the moment you send them: 1 row each, added as 1 block directly under the table's 2 header rows, in the order sent (Q1 on top). The newest <<ROUTINE_NAME>> is always on top.
2. `Date`: the day the questions were sent, the same date as that <<ROUTINE_NAME>>'s answers file in `02-sources/routine-answers/`.
3. `Category`: the category name exactly as written in [[04-agents/question-banks/routine-questions]].
4. `Question (as sent)`: the exact wording sent, personalization included. Replace any `|` with `/` so the table stays intact.
5. `Answered`: `no` when logged; `yes` when an answer to that question arrives; `skipped` when the client says to skip it.
6. Never repeat a question within 8 weeks: before sending, read every row dated in the last 56 days and never send a question that asks for the same thing, even in different words.
7. Log only <<ROUTINE_NAME>> questions. Setup interview questions and monthly review questions never go here.
8. Never delete a row. After logging, only `Answered` changes.

## Entries
| Date | Category | Question (as sent) | Answered |
|---|---|---|---|
