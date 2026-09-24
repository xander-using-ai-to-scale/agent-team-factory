---
type: template
name: delivery
kit_version: <<KIT_VERSION>>
---

# Template: DELIVERY.md (the client deliverable)

`05-outputs/{{output_id}}/DELIVERY.md` is the only file the client receives. The <<LEAD_SHORT>> compiles it after QA ([[04-agents/workflows/production]]) from files with `status: qa-pass` only. It has no frontmatter.

## How to compile

1. Copy everything inside the fenced block below into `05-outputs/{{output_id}}/DELIVERY.md`. In the title line, `{{delivery_day}}` = this <<OUTPUT_UNIT>>'s date (the first 10 characters of `output_id`) and `{{title}}` = the title noted in Step 2 of [[04-agents/workflows/production]].
2. Keep one numbered section per `qa-pass` file, in production order (the order of the output files' numbers), with the section names shown below. Number them continuously (1, 2, 3…): never skip a number when an output is inactive or held back. A file from an agent that runs only on demand goes last, under its own section name, without a number.
3. For each included file, copy its client-facing text **exactly**, word for word, as QA passed it, and move every heading in it 1 level down (`##` becomes `###`, `###` becomes `####`). A `# ` title line becomes a `### ` heading placed first in its section. Remove only these internal parts:
   - the frontmatter and the `LOADED` receipt line
   - <!-- FILL: the internal parts of this team's output files that the client never sees, 1 line per output file that has any: the section headings to remove and the line prefixes to remove (count and check lines). Take them from the parts each specialist charter marks "internal" in "What you produce". Write nothing more when no output file has internal parts. Source: each specialist charter's "What you produce" and "Output template". Length: 1 line per file. Example: kit/The-Almanac/04-agents/templates/pack.md, "How to compile", item 3. -->
4. `## Check before using`: every `[BRACKETED CAPS]` marker in the included text, each marker once, with where it appears. Example (fictional): `[BOOKING LINK]: section 2, item 3`. Then every item on the `Check before using:` line of each included file's last section in `qa-report.md`. If there is nothing, write `Nothing. Ready to use.`
5. `## Held back`: 1 line per held-back or not-written file: `{{output in plain words}}: {{reason in plain words}}`. Delete the section when nothing was held back.
6. Fill the `Built from:` line from the brain versions in `00-summary.md`.
7. Never add work that did not pass QA. Never rewrite anything while compiling. Never write "ticket", "receipt", "sub-agent", "frontmatter", or "routing table" in this file.
8. On-demand single pieces: leave out the "in 30 seconds" section.

## The delivery

```markdown
# Your <<OUTPUT_UNIT>> · {{delivery_day}} · {{title}}
Built from: company v{{n}} · voice v{{n}} · plan v{{n}} · {{each domain brain file as name v{{n}}}} · QA: {{all passed | {{n}} passed, {{n}} held back}}

## This <<OUTPUT_UNIT>> in 30 seconds
- Core idea: {{the core idea in 1 line}}
- Inside: {{count per output, in plain words}}
- Suggested order: {{the order in 01-brain/plan.md → Team and handoff if it gives one; otherwise the section order}}
<!-- FILL: 0-2 more lines the client needs first, each "- <Label>: {{value}}" (for example the one item the other parts depend on, or a deadline the work is for). Write nothing when the 3 lines above are enough. Source: TEAM-SPEC §15 (output specs); team.json specialists. Length: 0-2 lines. Example: kit/The-Almanac/04-agents/templates/pack.md, "This week in 30 seconds" (the "Lead magnet" line). -->

<!-- FILL: one section per specialist output that can appear in a regular delivery, in production order (team.json specialists order, skipping on_demand_only agents), each written as "## {{n}}. <section name in plain client words>" followed by 1 line in braces naming what goes in it (for example "{{every part of 01-report.md except its internal parts}}"); then one section per on-demand-only specialist, "## <section name>", with no number, last. {{n}} is the section's position among the included sections (How to compile, item 2). Source: team.json specialists (name, output_file, on_demand_only); TEAM-SPEC §11.5 and §15 (the client-facing names). Length: 2 lines per section. Example: kit/The-Almanac/04-agents/templates/pack.md, "The pack", sections "## 1. Newsletter (pillar)" to "## 7. Instagram", and "How to compile", item 2 (the section that goes last). -->

## Check before using
- {{[MARKER]: where it appears}}
- {{item from a qa-report "Check before using:" line}}

## Held back
- {{output in plain words}}: {{reason in plain words}}

## 2-minute feedback
Paste any piece you edit, even a small change. When something performs, say "winner:" + the piece + what happened.
```
