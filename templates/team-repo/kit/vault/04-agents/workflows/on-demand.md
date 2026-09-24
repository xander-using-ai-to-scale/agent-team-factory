---
type: workflow
name: on-demand
kit_version: <<KIT_VERSION>>
owner: <<LEAD_FILE>>
---

# On-demand

> Single pieces of work, rewrites, and full <<OUTPUT_UNIT_PLURAL>> on a topic that the client asks for between <<OUTPUT_UNIT_PLURAL>>, with the same reading, receipts, and QA as every <<OUTPUT_UNIT>>.

## Purpose

1. Produce what the client asks for outside the <<ROUTINE_NAME>>: 1 piece from 1 specialist, 1 rewrite of a delivered piece, or 1 full <<OUTPUT_UNIT>> on a topic.
2. Keep every rule of a normal <<OUTPUT_UNIT>>: read the routing row, start every file with a LOADED receipt, run QA on every file, deliver through `DELIVERY.md`.
3. Ask the client at most 1 clarifying message per request.

## Triggers

| The client says (or means) | Deliverable | Go to |
|---|---|---|
<!-- FILL: one row per on-demand request type, in the same order as the on-demand rows of "Client commands" in the lead charter: the command pattern in backticks with {{placeholders}} for the variable parts (for example `write a {{output}} about {{topic}}`), the deliverable with its quantity, and "Step 1". Source: the lead charter "Client commands" (on-demand rows); TEAM-SPEC §12.7 and §17 (client commands); team.json specialists[] (on_demand_only). Length: 1 to 4 rows. Example: kit/The-Almanac/04-agents/workflows/on-demand.md, Triggers, rows 1 to 3. -->
| A delivered piece plus "make this shorter", or any other rewrite instruction | 1 rewritten piece | Rewrites of delivered pieces |
| `make a <<OUTPUT_UNIT>> about {{topic}}` | 1 full <<OUTPUT_UNIT>> | Full <<OUTPUT_UNIT>> on a topic |

## Must read (in this order)

Rows R0 and R11 of the routing table:

1. `00-START-HERE.md` (full)
2. `04-agents/workflows/on-demand.md` (full)
3. then the row for the specialist doing the work (R12 and up)

| Specialist doing the work | Row |
|---|---|
<!-- FILL: one row per specialist in team.json order: the specialist's name, then its routing row (the row value in team.json, R12 and up). Source: team.json specialists[] (name, row). Length: 1 row per specialist. Example: kit/The-Almanac/04-agents/workflows/on-demand.md, Must read table. -->
| QA Agent (every file) | R6 |

The full rows are in the routing table in `00-START-HERE.md`. Each ticket copies its row with real paths (Step 3).

## The gate

1. Run [[04-agents/workflows/production#The gate]] before Step 1: `setup_status: complete` and all <<BRAIN_FILE_COUNT>> brain files with `status: approved`. If it fails, send its template and stop.
2. The request must be work a specialist in the Step 3 table does. Anything else (an action, a message to someone, a task no specialist covers): tell the client in 1 line what the team can prepare instead, as a draft, within [[01-brain/plan#Authority]].
<!-- FILL: request-specific preconditions, numbered from 3, one line each, for example "A request about a product or service: it must be listed in `01-brain/company.md` → What we sell; if it is not, ask in Step 1." Delete this comment when there are none. Source: TEAM-SPEC §12.7 (the on-demand table); the charters of the specialists that work on demand. Length: 0 to 3 lines. Example: kit/The-Almanac/04-agents/workflows/on-demand.md, The gate, item 2 (the offer must be listed before a VSL). -->

## Step 1 · Clarify (only if needed)

Ask only when at least 1 of these is unknown. Otherwise go to Step 2.

1. Which output: the request names none, and 2 or more rows of the Step 3 table fit it. With exactly 1 row, use it.
2. Topic: the request names no topic. Offer 2 usable entries from the source bank named in [[04-agents/workflows/routine]] → Bank <<OUTPUT_UNIT>> procedure, newest first, plus "your own topic".
<!-- FILL: team-specific unknowns, numbered from 3, each with when to ask (for example "Length: always ask, unless the client already named it."). Delete this comment when there are none. Source: TEAM-SPEC §12.7 (the on-demand table); the "If something is wrong" section of each on-demand specialist's charter (options a ticket must name). Length: 0 to 3 lines. Example: kit/The-Almanac/04-agents/workflows/on-demand.md, Step 1, items 3 and 4 (the offer for a VSL; the VSL length). -->

Put every open question in 1 message, max 80 words, with lettered options. Show only the questions you need. The output options are the fitting rows of the Step 3 table, then "other". Example (fictional):

```
Quick check before we start:
1) Which one? a) job post b) interview guide c) other
2) How long? a) short b) standard c) long
Reply like "1a 2b".
```

No reply: do nothing. Never send a reminder.

## Step 2 · Create the on-demand <<OUTPUT_UNIT>>

1. `output_id` = `YYYY-MM-DD-od-{slug}`, built with the naming rule in [[04-agents/workflows/production]] Step 1: the date is today; the slug is 2–5 lowercase words from the topic. Example (fictional): `2026-10-08-od-remote-work-policy`.
2. Create `05-outputs/{{output_id}}/` and `05-outputs/{{output_id}}/tickets/`.
3. Create `05-outputs/{{output_id}}/00-summary.md` from [[04-agents/templates/output-summary]], with the frontmatter exactly as the template shows: this unit's `output_id`, `kind: on-demand`, `status: in-progress`, `created: {{today}}`, and `delivered` empty.
4. The folder holds only the requested file(s), `00-summary.md`, `qa-report.md`, `DELIVERY.md`, and `tickets/`.

## Step 3 · Ticket

1. Pick the specialist, the output file, and the quantity:

| Request | Specialist | Agent file name | Output file | Quantity |
|---|---|---|---|---|
<!-- FILL: one row per kind of work the client can ask for on demand, in the order of the Triggers table: the request in plain words, the specialist's name, its charter file name without .md, its output_file from team.json, and the quantity for 1 on-demand request (for example "1 post, or 3 when the client asks for a set"). When the request needs another output first (TEAM-SPEC §12.7), end the Quantity cell with "after <that output in plain words>". Every specialist that can work alone gets a row, including every on_demand_only specialist. Source: team.json specialists[] (name, file, output_file, on_demand_only); TEAM-SPEC §12.7 (the on-demand table). Length: 1 row per request type. Example: kit/The-Almanac/04-agents/workflows/on-demand.md, Step 3, the table. -->

2. Write `05-outputs/{{output_id}}/tickets/{{agent-file-name}}.md` with [[04-agents/workflows/production#Writing and sending a ticket]], with these on-demand rules:
   1. `## Task`: the deliverable and quantity from the table.
   2. `## Must read (in this order)`: rows R0 + the specialist's row with real paths. An item that has no file in a single-piece <<OUTPUT_UNIT>> is written with `none (on-demand)`, for example `the answers file: none (on-demand)` and each output it depends on: `none (on-demand)`.
   3. `## Depends on`: `none (on-demand): {{topic and brief}}`. A single piece never waits for outputs this <<OUTPUT_UNIT>> does not have. The one exception: when the table's Quantity cell ends with "after <an output>", write, send, and QA that output first in this <<OUTPUT_UNIT>> (its own ticket, same rules), then list it under `## Depends on`.
   4. `## Brief`: 3–6 bullets. Bullet 1 = the focus in 1 sentence. The other bullets come from the client's request (copy the client's words exactly) and from matching bank entries.
   5. `## Allowed material`: IDs only, or `none`: `public-ok` entries that match the topic and meet every use condition in their bank's Rules, max 2 per bank.
   6. `## Requirements`: every exact line to copy, limit, and choice the request sets (for example a length the client picked in Step 1), each with its source; or `none`.
   7. `## Output`, `## Packet`, and `## Revision notes`: as in Writing and sending a ticket.
   <!-- FILL: on-demand ticket rules for one request type or for one ticket section, numbered from 8, one line each (for example which exact line goes under `## Requirements` for a given request). Delete this comment when there are none. Source: TEAM-SPEC §12.7 (the on-demand table); the charters of the specialists that work on demand. Length: 0 to 3 lines. Example: kit/The-Almanac/04-agents/workflows/on-demand.md, Step 3, item 2.7 (the call to action per piece type). -->
3. Send the ticket with your platform's sub-agent feature. Message: `Read 00-START-HERE.md, then your charter, then every file in your job ticket: 05-outputs/{{output_id}}/tickets/{{agent-file-name}}.md`
4. Check the reply and the file as [[04-agents/workflows/production#Writing and sending a ticket]] says (items 4 and 5). Packet mode, Mode fallback, and Timeouts and failures apply exactly as written in [[04-agents/workflows/production]].

## Step 4 · QA and deliver

1. Run the QA loop exactly as in [[04-agents/workflows/production#QA loop]]: max 3 rounds per file.
2. Compile a short `05-outputs/{{output_id}}/DELIVERY.md` from [[04-agents/templates/delivery]], as [[04-agents/workflows/production#Compile DELIVERY.md]] says, with these differences:
   1. The title uses today's date and the title of the piece (or the topic).
   2. Leave out `## This <<OUTPUT_UNIT>> in 30 seconds` (single pieces only).
   3. The piece's section uses the name the template gives its output and the template's numbering: a single piece is section 1; a file from an agent that runs only on demand has no number.
3. Deliver as [[01-brain/plan#Delivery]] says, following [[04-agents/workflows/production#Deliver]] items 2–4. A Google Doc is titled with the title line of `DELIVERY.md`. Use this intro (max 80 words):

   ```
   Here's your {{piece in plain words}}: "{{title or first line}}".
   {{Before using it, check the {{n}} items at the end. | Nothing to check before using it.}}
   Edit freely and send back anything you change.
   ```

4. Update `00-summary.md`: `status: delivered`, `delivered: {{today}}`. Record bank use as [[04-agents/workflows/production#After delivery]] items 1–3 say.
5. Actions the piece prepared: as [[04-agents/workflows/production#After delivery]] item 7 says.
6. Held back after round 3: set `00-summary.md` → `status: held` and send:

   ```
   I couldn't get this {{piece in plain words}} past my quality checks after 3 tries, so I'm not sending it.
   a) Try again from a different angle
   b) Drop it
   ```

   Reply a: start again at Step 2 with a new focus bullet and a new `output_id`. Reply b: stop.
7. Log the session at the top of `06-log/session-log.md`:

   ```
   ## {{YYYY-MM-DD HH:MM}} · On-demand
   - Did:
     - {{piece}} about "{{topic}}" {{delivered | held back}}
   - Changed: 05-outputs/{{output_id}}/ (created), {{banks changed | nothing else}}
   - State: On-demand {{output_id}} {{delivered | held}}
   - Next: {{next action + when}}
   - Waiting on client: {{item | nothing}}
   ```

## Rewrites of delivered pieces

Trigger: the client sends or names a delivered piece and adds an instruction. Example (fictional): "make this shorter", "turn this into a checklist".

1. Find the original piece as in [[04-agents/workflows/learning-loop]] Part A, step 2. Unsure: send its "Which piece" template.
2. Create a new on-demand <<OUTPUT_UNIT>> (Step 2) whose slug names the piece. Example (fictional): `2026-10-09-od-shorter-welcome-email`. Never change the files of the delivered <<OUTPUT_UNIT>>.
3. Pick the specialist: the one that made the original when the kind of output stays the same; the specialist for the new kind (Step 3 table) when the instruction turns the piece into another kind of output.
4. Write the ticket as in Step 3, with these differences:
   - `## Task`: 1 piece, in the format the instruction asks for.
   - `## Depends on`: the outputs under the original ticket's `## Depends on`, linked in the original <<OUTPUT_UNIT>>'s folder, when they exist there with `qa-pass`; the Must read lines for them then name those files. Otherwise: `none (on-demand): {{topic and brief}}`.
   - `## Brief`, `## Allowed material`, and `## Requirements`: copied from the original ticket. When the kind of output changes, keep only the requirements that apply to the new kind.
   - `## Revision notes`:

     ```
     ### Rewrite · {{YYYY-MM-DD}}
     Client instruction: "{{the client's words, exactly}}"
     Original ({{original_output_id}} · {{file}} · {{unit}}):
     {{the original piece, word for word}}
     Apply the instruction. Keep everything the instruction does not change.
     ```

5. Send the ticket (Step 3, item 3), then run Step 4. The rewrite is round 1 of a new file, so it gets up to 3 QA rounds.
6. Voice preference: when the instruction names a style (length, tone, formality, specific words, emojis, questions, "sounds like …"), also run [[04-agents/workflows/learning-loop]] Part A from step 6, with Before = the original excerpt and After = the client's instruction in quotes. An instruction that only changes the kind of output, the format, or facts is not a voice preference.

## Full <<OUTPUT_UNIT>> on a topic

Trigger: `make a <<OUTPUT_UNIT>> about {{topic}}`.

1. Run The gate, then Step 1 (only if the topic is missing), then Step 2 (`kind: on-demand`).
2. Run [[04-agents/workflows/production]] from Step 2 through After delivery, with these inputs:
   - The focus: the client's topic as 1 sentence, in bullet 1 of the first ticket's `## Brief`. The key points come from the client's message (exact words) and from matching bank entries.
   - The answers file: `none (on-demand)`. If the client sent a voice note or text about the topic, save it word for word to `02-sources/routine-answers/{{YYYY-MM-DD}}-od-{{slug}}.md` and list that file as the answers file.
   - The outputs: every output production Step 1, item 5 lists, and the full `DELIVERY.md` layout, including `## This <<OUTPUT_UNIT>> in 30 seconds`.
3. Leave the schedules unchanged: the next <<ROUTINE_NAME>> still runs on its day.

## Checklist

1. The gate passed before any file was created.
2. At most 1 clarifying message went out, with lettered options, and every unknown in the Step 1 list was known before the ticket.
3. The `output_id` has the form `YYYY-MM-DD-od-{slug}` with today's date, and `00-summary.md` shows `kind: on-demand`.
4. The ticket copies the specialist's row with real paths and `none (on-demand)` for items without a file.
5. Every single-piece ticket has `## Depends on` = `none (on-demand): …`, or names the output its Step 3 table row says comes first, and that output reached `qa-pass` before the ticket went out.
6. Every file went through the QA loop, and `DELIVERY.md` holds only `qa-pass` files.
7. Rewrites live in their own on-demand <<OUTPUT_UNIT>>; the delivered <<OUTPUT_UNIT>> is unchanged.
8. Every rewrite instruction that names a style started learning-loop Part A.
9. The session-log entry exists.
<!-- FILL: 0 to 2 more lines, numbered from 10, for the team-specific on-demand rules above (for example "Every ticket for <request> named the option the client picked."). Delete this comment when there are none. Source: the on-demand rules in Step 1 and Step 3 above; TEAM-SPEC §12.7 (the on-demand table). Length: 0 to 2 lines. Example: kit/The-Almanac/04-agents/workflows/on-demand.md, Checklist, items 2 and 6. -->
