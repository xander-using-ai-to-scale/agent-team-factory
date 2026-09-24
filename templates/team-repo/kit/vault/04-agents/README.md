---
type: readme
folder: 04-agents
kit_version: <<KIT_VERSION>>
---

# 04-agents

## Purpose
How the team works. This folder holds the job description of every agent (charters), the step-by-step procedures the <<LEAD_SHORT>> runs (workflows), the setup interview and the <<ROUTINE_NAME>> questions (question banks), and the exact formats for working files (templates). It is the team's procedural memory.

## What lives here

**Charters** (one per agent; each agent reads its own before every job):

| Charter | Agent | Runs |
|---|---|---|
| [[04-agents/<<LEAD_FILE>>]] | <<LEAD_NAME>> | always |
| [[04-agents/qa-agent]] | QA Agent | every output file, every QA round |
<!-- FILL: one row per specialist in team.json order: "| [[04-agents/<file without .md>]] | <exact name> | <runs> |", where <runs> is "if active" (switched in 01-brain/plan.md Outputs and quantities) or "on demand" (on_demand_only: true), plus ", after <names of the agents it depends on>" when depends_on is not empty. Source: team.json specialists (name, file, depends_on, on_demand_only); TEAM-SPEC §9 (roster). Length: one row per specialist. Example: kit/The-Almanac/04-agents/README.md, "What lives here", charter table. -->

**Subfolders:**
- [[04-agents/workflows/README|workflows/]]: setup, the <<ROUTINE_NAME>>, production, learning loop, monthly review, on-demand.
- [[04-agents/question-banks/README|question-banks/]]: the setup interview and the <<ROUTINE_NAME>> question bank.
- [[04-agents/templates/README|templates/]]: job ticket, output summary, QA report, delivery.

## What never goes here
- Facts about the client → [[01-brain/README|01-brain/]].
- Bank entries (reusable material from the client) → [[03-banks/README|03-banks/]].
- Tickets, output files, QA reports, and deliveries → [[05-outputs/README|05-outputs/]].
- Questions actually sent to the client → [[06-log/questions-asked]].

## File naming
Lowercase kebab-case, fixed names. Charters are named after the agent (`qa-agent.md`). Never rename a file here: other files link to these exact names.

## Frontmatter for files here
Charters:
```yaml
---
type: charter
agent: {{exact agent name}}
kit_version: <<KIT_VERSION>>
runs: {{always | if-active | on-demand}}
output_file: {{the agent's file in 05-outputs/{{output_id}}/, e.g. qa-report.md | none}}
---
```
`runs` values: `always` = the <<LEAD_SHORT>> and the QA Agent; `if-active` = a specialist that works when [[01-brain/plan#Outputs and quantities]] marks its output Active = yes (the only on/off switch); `on-demand` = a specialist that works only when the client asks. `output_file` = the specialist's output file, `qa-report.md` for the QA Agent, and `none` for the <<LEAD_SHORT>>.

Workflows use `type: workflow`, `name`, `kit_version`, `owner: <<LEAD_FILE>>`. Question banks use `type: question-bank`, `name`, `kit_version`. Templates use `type: template`, `name`, `kit_version`.

## Who writes
Nobody during normal work. Everything here is **kit-owned**: it is replaced when the kit is updated. Client-specific facts never go here.

## Who reads
- Each agent reads its own charter before every job.
- The <<LEAD_SHORT>> reads the workflows, question banks, and templates named in its routing row.
- The QA Agent reads the charter of the agent whose output file it checks.

## Rules
1. A charter is the complete job description of its agent. If a charter and a workflow disagree, the order of authority in [[00-START-HERE]] §6 decides (charter before workflow).
2. Never store client facts, output files, or logs here.
3. Agent names in charters must match the names used at install exactly.
