---
type: template
name: output-summary
kit_version: <<KIT_VERSION>>
---

# Template: output summary (00-summary.md)

The <<LEAD_SHORT>> creates `05-outputs/{{output_id}}/00-summary.md` from this template at the start of every <<OUTPUT_UNIT>> (Step 1 of [[04-agents/workflows/production]]) and keeps it current until delivery. It is the control sheet of the <<OUTPUT_UNIT>>: status, files, receipts, QA results, delivery. The client never sees it.

## How to use

1. Create `05-outputs/{{output_id}}/00-summary.md` and copy everything inside the fenced block below into it.
2. Fill `## At a glance` right away.
3. Add one row to `## Files` for every file this <<OUTPUT_UNIT>> will contain (one per specialist that gets a ticket). Update the row after every QA round.
4. Change the frontmatter `status` as the work moves: `in-progress` (work being written) → `in-qa` (QA running) → `delivered` (sent to the client) or `held` (a file that other jobs depend on was held back and the <<OUTPUT_UNIT>> stopped).
5. Add every proposed brain change to `## Proposed brain changes` the moment you note it. [[04-agents/workflows/production]] sends them to the client in 1 batch after delivery.
6. Fill `## Delivery` when you deliver.

## The summary

```markdown
---
type: output-summary
output_id: {{output_id}}
kind: {{routine | bank | on-demand}}
status: in-progress
created: {{YYYY-MM-DD}}
delivered: ""
---

# Output summary · {{output_id}}

## At a glance
- Delivery day: {{YYYY-MM-DD}}
- Core idea: {{one sentence, from the brief}}
- Built from: {{02-sources/routine-answers/YYYY-MM-DD-routine-answers.md | bank entries {{IDs}} | on-demand request of YYYY-MM-DD}}
- Brain versions used: company v{{n}} · voice v{{n}} · plan v{{n}} · {{each domain brain file as name v{{n}}}}

## Files
| File | Agent | Status | QA rounds | Receipt |
|---|---|---|---|---|
| {{NN-name.md}} | {{Agent name}} | {{draft / qa-pass / qa-fix / qa-fail / held-back}} | {{0-3}} | {{the LOADED line}} |

## Material used
- {{bank entry ID or source file}} → {{the files that used it}}

## Held back
- {{file · reason | none}}

## Delivery
- Delivered: {{YYYY-MM-DD HH:MM}} via {{chat | chat + google-doc}}
- Google Doc: {{link | not used}}
- Brain changes proposed after delivery: {{count}} · Result: {{yes / no per item}}

## Proposed brain changes
<!-- 1 line per proposal collected while processing the answers and building this output unit. The production workflow sends them to the client in 1 batch after delivery. -->
- {{file}} → {{section}}: "{{before, or (new)}}" → "{{after}}" ({{source}})

## Notes
- {{anything the next session must know | none}}
```
