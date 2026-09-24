---
type: template
name: job-ticket
kit_version: <<KIT_VERSION>>
---

# Template: job ticket

The <<LEAD_SHORT>> uses this template for every job sent to a specialist. (The QA Agent gets a QA request instead: [[04-agents/qa-agent]] → Inputs you get.) The sections and their order are fixed.

## How to use

1. Create a new file at `05-outputs/{{output_id}}/tickets/{{agent-file-name}}.md` (`{{agent-file-name}}` = the agent's charter file name without `.md`).
2. Copy everything inside the fenced block below into it.
3. Fill every `{{field}}`:
   - **Task**: the deliverable and its quantity from the agent's row in [[01-brain/plan#Outputs and quantities]], plus that row's Notes word for word when they are not empty.
   - **Must read**: copy the agent's routing row (R12 and up in `00-START-HERE.md`) with real paths: the real output folder, the real source files, and the exact bank entry IDs. If a file in the row does not exist for this job, keep the line and write `none ({{reason}})` in place of the path. Example (fictional): `the answers file: none (bank <<OUTPUT_UNIT>>; use the entries named in this ticket)`.
   - **Depends on**: one wikilink per line to each output file this job depends on (the order in [[04-agents/workflows/production]]), each with `status: qa-pass`; or `none (first step)` when the agent depends on no other job; or `none (on-demand): {{topic and brief in 1 sentence}}` when an on-demand job runs without its usual dependencies.
   - **Brief**: 3-6 bullets. Bullet 1 = the focus sentence (the core idea). Bullets 2-6 = the points to cover. When a bullet restates something the client said, copy the client's words exactly.
   - **Allowed material**: the bank entries the agent may use, IDs only, and any source file its Must read list does not already name. Only entries with `Permission: public-ok` that meet every use condition in their bank's Rules (for example `Verified by client: yes`, or a reuse wait, which an ID written as `{{ID}} (repeat ok)` overrides). Write `none` if there are none.
   - **Requirements**: every exact line, limit, or choice this job must meet, one per bullet, each copied character for character from its source and followed by that source in parentheses. [[04-agents/workflows/production]] says what each agent's requirements hold. Write `none` if there are none.
4. Leave `## Packet` empty unless `packet_mode: yes` in `00-START-HERE.md`. In packet mode, paste each required file (or the required sections) under `### {{path}} · {{version}}`.
5. Leave `## Revision notes` empty on round 1. For each later round, add the block exactly as [[04-agents/workflows/production]] shows it (`### Round {{n+1}}`, the line `QA round {{n}} verdict: {{FIX | FAIL}}`, then the QA Agent's fixes pasted word for word).
6. Send the agent: `Read 00-START-HERE.md, then your charter, then every file in your job ticket: 05-outputs/{{output_id}}/tickets/{{agent-file-name}}.md`. In packet mode, send the full ticket text.

## The ticket

```markdown
---
type: job-ticket
ticket: {{output_id}}/{{agent-file-name}}
output_id: {{output_id}}
agent: {{Agent name}}
created: {{YYYY-MM-DD}}
---

# Job ticket: {{Agent name}} · {{output_id}}

## Task
Write {{quantity}} {{deliverable}}, exactly as your charter's "What you produce" defines.

## Must read (in this order)
1. `00-START-HERE.md` (full)
2. `04-agents/{{agent-file-name}}.md` (full)
3. This ticket: `05-outputs/{{output_id}}/tickets/{{agent-file-name}}.md`
4. {{the rest of the agent's routing row, one file per line, with real paths and the same "(full)" / "(sections: …)" markers}}

## Depends on
{{[[05-outputs/{{output_id}}/{{output file without .md}}]] (one per line) | none (first step) | none (on-demand): {{topic and brief}}}}

## Brief
- Core idea: {{one sentence}}
- {{point 1}}
- {{point 2}}
- {{up to 3 more}}

## Allowed material
{{bank entry IDs and extra source paths | none}}

## Requirements
- {{exact line, limit, or choice}} ({{source}})

## Output
- Save to: `05-outputs/{{output_id}}/{{output file name}}`
- The first line after the frontmatter is your LOADED receipt.
- Then reply to the <<LEAD_SHORT>> with your LOADED line and one line: `Done: {{file}} · {{counts}}`. Or reply BLOCKED.

## Packet

## Revision notes
```

## Example (fictional)

<!-- FILL: one complete filled ticket in a fenced block tagged markdown, for the first specialist that depends on another job (when none does, the first specialist, row R12), for a fictional client of the kind this team serves: the frontmatter; the "# Job ticket" line; ## Task with a quantity from the kit defaults in 01-brain/plan.md; ## Must read copying that agent's routing row with real paths, every "(full)" / "(sections: ...)" marker, real bank file names with 1-3 fictional IDs, and at least 1 line written as `none (<reason>)`; ## Depends on (a wikilink to the dependency's output file, or `none (first step)`); ## Brief (a core idea and 2-4 points in the fictional client's words); ## Allowed material (the same fictional IDs, using this team's bank prefixes); ## Requirements (1-3 exact lines, each with its source); ## Output with the agent's real output file name and its real Done line; empty ## Packet and ## Revision notes. A fictional business and people, dates in 2026, no em dashes. Source: team.json specialists (row, file, output_file, depends_on) and banks (file, id_prefix); TEAM-SPEC §10 (routing table). Length: 35-60 lines. Example: kit/The-Almanac/04-agents/templates/job-ticket.md, "Example (fictional)". -->
