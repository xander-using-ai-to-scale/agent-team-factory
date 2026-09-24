---
type: log
name: edits-log
updated: ""
next_id: E-001
---

# Edits log

Client edits to our drafts, 1 entry per distinct pattern, each with the voice rule proposed from it.
Approved rules move into [[01-brain/voice#Rules learned from edits]].

## Entry format
```
### E-001 · {{YYYY-MM-DD}} · {{output label}}
- Draft: [[05-outputs/{{output_id}}/{{output file name without .md}}]] ({{unit}})
- What the client changed: {{short description}}
- Before: "{{excerpt}}"
- After: "{{excerpt}}"
- Pattern: {{one sentence}}
- Proposed rule: {{one sentence, testable}}
- Client decision: {{pending | approved | rejected}}
- Applied: {{voice vN on YYYY-MM-DD | not applied}}
```

## Rules
1. 1 entry per distinct pattern, not per word. Several changes that share 1 pattern are 1 entry.
2. Before adding, search the entries for the same pattern. If it is already logged as `pending` or `approved`, add nothing.
3. Heading: the date the client sent the edit, and 1 output label from [[06-log/README]].
4. `Draft`: a wikilink to the output file (full vault path, no `.md`), then the unit in parentheses, as in the format. The unit is the item's label in the specialist's charter plus its number, for example `email 2`.
5. `Before` and `After`: verbatim excerpts, max 40 words each.
6. `Proposed rule`: testable, so QA can mark it pass or fail. Example (fictional): "Never open an email with a question." Not testable: "Sound more natural."
7. `Client decision` stays `pending` until the client answers. Ask "Make this a rule? yes / no", max 5 patterns per message.
8. On `approved`: add the rule to [[01-brain/voice#Rules learned from edits]] through the brain change procedure in [[04-agents/workflows/learning-loop]], then set `Applied: voice vN on YYYY-MM-DD` with the new version.
9. On `rejected`: set `Applied: not applied`. Never propose that pattern again unless the client raises it.
10. After logging, only `Client decision` and `Applied` change.

## Entries
<!-- Newest first. No entries yet. -->
