---
type: log
name: open-questions
updated: ""
next_id: Q-001
---

# Open questions

Facts still missing from a brain file: questions the client skipped or could not answer, and gaps found later.
Open items are read at every session start and asked again in the monthly review.

## Entry format
```
### Q-001 · {{brain file}} · {{YYYY-MM-DD}}
- Question: {{…}}
- Why it matters: {{one sentence}}
- Status: {{open | answered YYYY-MM-DD | dropped}}
```

## Rules
1. Log a Q-### when the client says "skip" or "don't know" to a setup question, or when a fact a brain file needs is missing.
2. Heading: exactly 1 brain file (its file name without `.md`, for example `company`, `voice`, or `plan`) and the date you log it.
3. `Question`: plain words, ready to send to the client as written.
4. `Status`: `open` when logged; `answered YYYY-MM-DD` when the client answers; `dropped` when the client says it does not matter or no longer applies. After logging, only `Status` changes.
5. On `answered`: apply the answer to the brain file through the brain change procedure in [[04-agents/workflows/learning-loop]].
6. Every Q-### must also be pointed to from the `## Open questions` section of its brain file with the line `- Q-### · {{question}} (see [[06-log/open-questions]])`. Add it while that brain file is being drafted (setup or `redo`). For an `approved` brain file, include the line in the next change the client approves for that file, and update it the same way when the status changes.
7. Monthly review: ask up to 3 `open` questions, oldest first.
8. Never log the same question twice: search the entries before adding.

## Entries
<!-- Newest first. No entries yet. -->
