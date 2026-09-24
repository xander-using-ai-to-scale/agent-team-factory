---
type: readme
folder: 04-agents/templates
kit_version: <<KIT_VERSION>>
---

# templates

## Purpose
Exact formats the <<LEAD_SHORT>> copies when it creates working files. Using the same format every time makes each <<OUTPUT_UNIT>> easy to check, resume, and compare.

## What lives here
| Template | Creates | Used in |
|---|---|---|
| [[04-agents/templates/job-ticket]] | `05-outputs/{{output_id}}/tickets/{{agent-file-name}}.md` | Every job sent to a specialist |
| [[04-agents/templates/output-summary]] | `05-outputs/{{output_id}}/00-summary.md` | The control sheet of every <<OUTPUT_UNIT>> |
| [[04-agents/templates/qa-report]] | `05-outputs/{{output_id}}/qa-report.md` | The QA record of every <<OUTPUT_UNIT>> |
| [[04-agents/templates/delivery]] | `05-outputs/{{output_id}}/DELIVERY.md` | The client deliverable |

## What never goes here
- Filled-in tickets, summaries, reports, or deliveries. Those live in the output folder in [[05-outputs/README]].
- Anything about the client.

## File naming
Template names are fixed. Never rename them; workflows link to them by name.

## Frontmatter for files here
```yaml
---
type: template
name: {{template name}}
kit_version: <<KIT_VERSION>>
---
```

## Who writes
Nobody during normal work. These files are kit-owned and are replaced when the kit is updated.

## Who reads
The <<LEAD_SHORT>> (to create working files) and the QA Agent (to check the format of the QA report).

## Rules
1. Copy the fenced block, not the explanation around it.
2. Keep every section and its order. Fill every `{{field}}`.
3. Never leave a `{{field}}` in a file that goes to the client.
