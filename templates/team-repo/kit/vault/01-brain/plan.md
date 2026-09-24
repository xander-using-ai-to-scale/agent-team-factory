---
type: brain
file: plan
version: 0
status: empty
updated: ""
approved_on: ""
kit_version: <<KIT_VERSION>>
---

# Plan

Holds how the team works for this client: the goal, which outputs are on and how much of each, the rhythm, how each <<OUTPUT_UNIT>> is delivered, what the team may do on its own (Authority), who handles the work after delivery, and the areas to avoid. The <<LEAD_NAME>> (<<LEAD_SHORT>>) fills it during setup from the interview and any optional drops, proposing the outputs and the Authority table for the client to approve.
Read by the <<LEAD_SHORT>>, every specialist, and the QA Agent (which sections: routing table in [[00-START-HERE]]); every schedule runs on ## Rhythm. Read-only: sub-agents never edit it, and after approval the <<LEAD_SHORT>> changes it only through [[04-agents/workflows/learning-loop#Brain change procedure]].

<!-- Fill rules (<<LEAD_SHORT>>): write only facts the client confirmed. Unknown → log a Q-### in [[06-log/open-questions]], write UNKNOWN (Q-###) in the field, add its pointer under ## Open questions; a section below its minimum count gets a Q-### too. Never guess.
Replace every {{placeholder}}. A placeholder holding a value, like {{no}} or {{1}}, is the default: confirm it with the client, then drop the braces. Delete unused template rows and blocks. Empty list → "- none"; empty table → one row with none in the first cell. Never edit guidance comments; {{ }} inside them are format examples.
Set status: draft when you start filling; status: approved needs the client's OK and zero {{ }} outside comments. Agents: UNKNOWN is not a fact; never fill it in; if your job needs it, reply BLOCKED. -->

## TL;DR
<!-- Agents read this first. The <<LEAD_SHORT>> writes it last, from the sections below, and updates it in the same edit as any change to this file. Max 10 lines (this comment not counted); no {{ }} once approved.
Example (fictional). Good: "- Rhythm: weekly · delivery day Tuesday · questions Monday 10:00 · America/New_York". Bad: "- Rhythm: regular work". -->
- Goal: {{primary_goal}} · metric: {{metric_to_watch}}
- Active outputs: {{active_outputs_with_quantities_in_one_line}}
- Rhythm: {{cadence}} · delivery day {{weekday}} · questions {{weekday}} {{HH:MM}} · {{timezone}}
- Delivery: {{chat / chat + google-doc}} · paused until: {{no / YYYY-MM-DD}}
- Allowed: {{allowed_actions_in_one_line, or none}}
- With approval: {{approval_actions_in_one_line, or none}}
- Avoid: {{areas_to_avoid_in_one_line}}
<!-- FILL: one TL;DR line per plan.md domain section that most jobs need, as "- <Label>: {{placeholder_in_snake_case}}", keeping the TL;DR at max 10 lines; delete this comment when plan.md has no domain sections. Source: team.json brain_files[plan.md].sections after the 7 core sections. Length: max 3 lines. Example: kit/The-Almanac/01-brain/strategy.md ## TL;DR ("- Pillars: {{pillar_names}}"). -->

## Goal
<!-- One primary goal the team's work serves, the one metric that shows it is working (with a target), and an optional secondary goal.
Example (fictional). Good: "Primary goal (one): 4 booked discovery calls a month". Bad: "Primary goal (one): growth". -->
- Primary goal (one): {{primary_goal}}
- Metric to watch: {{metric_and_target}}
- Secondary goal (optional): {{secondary_goal, or none}}

## Outputs and quantities
<!-- One row per specialist. Active = yes: that agent gets a ticket for every <<OUTPUT_UNIT>>. no: it gets none. on demand: it works only when the client asks ([[04-agents/workflows/on-demand]]); that row always stays "on demand". An agent whose output an active output depends on gets a ticket whenever that output runs, whatever its own row says, and its output is delivered with the rest. Quantity per <<OUTPUT_UNIT>> holds the kit defaults; change a number only when the client asks. Notes hold per-client exceptions and options for that output (a length, a format, an option switched on); job tickets copy them word for word, and QA checks them. Write none when there are none. Replace each {{yes/no}}.
Example (fictional). Good: "Summary | Summary Agent | yes | 1 summary of 300–500 words | none". Bad: "Summary | Summary Agent | sometimes | a few | various". -->

| Output | Agent | Active | Quantity per <<OUTPUT_UNIT>> | Notes |
|---|---|---|---|---|
<!-- FILL: one row per specialist, in team.json order: | <output in plain words> | <specialist name> | {{yes/no}}, or "on demand" when on_demand_only is true | <the default quantity and its core size, for example "1 article of 900–1,400 words"> | <default options for this output as {{placeholders}} the client confirms, for example "Checklist version: {{no}}", or none> |. Source: team.json specialists (name, output_file, on_demand_only); TEAM-SPEC outputs and default quantities. Length: 1 row per specialist. Example: kit/The-Almanac/01-brain/strategy.md ## Platforms and quantities (rows, the Notes column, and the "on demand" VSL row). -->

This table is the only on/off switch for outputs.

## Rhythm
<!-- Every schedule uses these values. Changing Cadence, Delivery day, Question time, or Timezone = brain change procedure, then delete and recreate every schedule in the schedules table of [[00-START-HERE]] (the 4 fixed ones: routine-send, routine-reminder, feedback-check, monthly-review, plus any extra ones listed there). A change to ## Delivery needs no schedule change.
Paused until: set by "pause questions for N weeks" (the command is the client's approval). The schedules keep running; while this is a future date, routine-send, routine-reminder, and feedback-check do nothing. The first routine-send on or after the date sets it back to no; "resume questions" sets it to no at once. The first date in Delivery day anchors every-2-weeks cycles.
Example (fictional). Good: "Delivery day: Tuesday (first: 2026-10-06)". Bad: "Delivery day: early in the week". -->
- Cadence: {{weekly / every-2-weeks}}
- Delivery day: {{weekday}} (first: {{YYYY-MM-DD}})
- Question time: {{weekday}} {{HH:MM}} (when routine-send sends the <<ROUTINE_NAME>> questions; default: the day before delivery day, 10:00)
- Timezone: {{iana_timezone}} (IANA name, e.g. America/New_York)
- Paused until: {{no}} (while paused: the resume date, YYYY-MM-DD)

## Delivery
<!-- How each <<OUTPUT_UNIT>> reaches the client. Chat and the vault always: the <<LEAD_SHORT>> saves DELIVERY.md in the <<OUTPUT_UNIT>>'s folder in 05-outputs/ and sends it in chat. A Google Doc copy is optional: set chat + google-doc only after the setup test worked. If a Google Doc fails later, the <<LEAD_SHORT>> delivers in chat only and tells the client in 1 line; this setting stays until the client changes it.
Example (fictional). Good: "Delivery: chat + google-doc (setup test passed 2026-10-05)". Bad: "Delivery: whatever works". -->
- Delivery: {{chat / chat + google-doc}} (default chat; chat + google-doc only after the setup test worked)

## Authority
<!-- What the team may do for this client, by level (rule 5 in [[00-START-HERE]]). Draft-only is the default for everything not listed. With approval: the <<LEAD_SHORT>> asks the client about that exact action each time and acts only after a yes. Allowed: low-risk, reversible actions the team takes without asking. The With approval and Allowed rows start as the kit's proposal; the client confirms or changes them in setup, and every later change goes through the brain change procedure. Write each action as a verb plus an object the QA Agent can check; write none when a level has no actions. The Never row is fixed: nobody can change it, and a client request for a Never action gets a one-line no and a draft instead.
Example (fictional). Good: "With approval | Send the confirmation email to a booked guest, after the client says yes to that exact email". Bad: "With approval | Handle emails". -->

| Level | What it means | Actions for this client |
|---|---|---|
| Draft-only (default) | The team prepares; the client acts. | Everything not listed in the rows below. |
| With approval | The team may take the listed action after the client says yes to that exact action, each time. | <!-- FILL: the blueprint's proposed With approval actions, separated by "; ", each wrapped as a default placeholder for the <<LEAD_SHORT>> to confirm with the client in setup, for example "{{Send the approved reminder email to one customer}}". Write none when the blueprint proposes none. Source: TEAM-SPEC Authority; Team Brief field 7 (Authority). Length: max 5 actions, each max 15 words. Example: kit/The-Almanac/01-brain/strategy.md ## Platforms and quantities (default values in braces, such as "Document carousel: {{no}}"). --> |
| Allowed | The team may take the listed low-risk, reversible actions without asking. | <!-- FILL: the blueprint's proposed Allowed actions, separated by "; ", each wrapped as a default placeholder for the <<LEAD_SHORT>> to confirm with the client in setup, for example "{{Save drafts to the client's shared folder}}". Write none when the blueprint proposes none. Source: TEAM-SPEC Authority; Team Brief field 7 (Authority). Length: max 5 actions, each max 15 words. Example: kit/The-Almanac/01-brain/strategy.md ## Platforms and quantities (default values in braces, such as "Document carousel: {{no}}"). --> |
| Never | Cannot be allowed by anyone. | Spending money, entering passwords or payment details, deleting accounts or data, changing account settings. |

## Team and handoff
<!-- Who handles each <<OUTPUT_UNIT>> after delivery, 1 row per person. The <<LEAD_SHORT>> delivers only to the client and never messages anyone else, unless ## Authority lists that exact message; the client forwards work to their people.
Example (fictional). Good: "Office manager | Prints and mails the letters | the letters file | delivery day + 1". Bad: "Team | helps | stuff | later". -->

| Person | Role | Gets | When |
|---|---|---|---|
| {{client_name}} | Owner: approves and acts | `DELIVERY.md` | On delivery |
| {{person}} | {{role}} | {{output_files}} | {{when}} |

## Areas to avoid
<!-- Banned territory for every agent: topics, claims, people, places, or kinds of work no output may touch (rule 7 in [[00-START-HERE]]). The QA Agent fails any draft that touches one, even in 1 sentence. 1 per line, each with the client's reason. "- none" if the client names none.
Example (fictional). Good: "Politics and elections · reason: the client keeps the brand neutral". Bad: "Controversial stuff". -->
- {{area}} · reason: {{reason}}
- {{area}} · reason: {{reason}}

<!-- FILL: only if team.json lists extra sections for plan.md after "Areas to avoid": for each one, in order, write "## <Section>" exactly as in team.json, then a guidance comment in the style of the sections above (what goes here, a count range, who reads it, which setting it controls, and a last line "Example (fictional). Good: "..." Bad: "..."" with no em dashes), then a placeholder body of 2 to 6 lines or a table with {{snake_case}} placeholders. Otherwise delete this comment. Source: team.json brain_files[plan.md].sections after the 7 core sections; TEAM-SPEC brain files. Length: 3 to 15 body lines per section. Example: kit/The-Almanac/01-brain/strategy.md ## Script style and ## Calls to action. -->

## Open questions
<!-- Pointers only: each question lives in [[06-log/open-questions]], which is always the full list. Update pointers only while drafting in setup or inside an approved brain change. "- none" when empty.
Example (fictional). Good: "- Q-014 · Which day do you want your work delivered? (see [[06-log/open-questions]])". Bad: "- schedule?". -->
- Q-### · {{question}} (see [[06-log/open-questions]])

## Changelog
<!-- Newest first, one line per version; never edit old lines. Format: - vN · YYYY-MM-DD · {{change}} ({{E-### | client request | setup}}); client request = any other change the client approved (monthly review, post-delivery proposals, answered questions).
Every approved version: version +1, updated and approved_on = that date, one line here.
Example (fictional). Good: "- v2 · 2026-10-12 · Delivery day changed from Tuesday to Thursday (client request)". Bad: "- schedule update". -->
- v0 · template · installed from kit <<KIT_VERSION>>
