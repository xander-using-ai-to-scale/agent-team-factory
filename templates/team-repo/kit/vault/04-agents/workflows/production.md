---
type: workflow
name: production
kit_version: <<KIT_VERSION>>
owner: <<LEAD_FILE>>
---

# Production

> The waterfall: 1 focus becomes 1 <<OUTPUT_UNIT>>. Each specialist starts only after every output it depends on has passed QA, the QA Agent checks every file, and only passed files reach the client.

## Purpose

1. Turn 1 focus (from the <<ROUTINE_NAME>> answers, a bank entry, or a client topic) into 1 <<OUTPUT_UNIT>> in `05-outputs/`.
2. Keep the order: a ticket goes out only after every output it depends on has `status: qa-pass` (rule 10).
3. Deliver only files with `status: qa-pass`. Every other file goes under `## Held back`.
4. You, the <<LEAD_NAME>> (<<LEAD_SHORT>>), run this workflow. Sub-agents only receive job tickets.

## When it runs

1. Unit from answers (`kind: routine`): [[04-agents/workflows/routine]] has saved the answers and picked the focus (routine Part 4).
2. Bank unit (`kind: bank`): the client says `bank` or `bank <<OUTPUT_UNIT>>`, or replies "bank" to the <<ROUTINE_NAME>> reminder. Use the focus block made in the routine's Bank <<OUTPUT_UNIT>> procedure. If none was made, run that procedure now, steps 2–7, then continue here.
3. Full on-demand unit (`kind: on-demand`): [[04-agents/workflows/on-demand]] (Full <<OUTPUT_UNIT>> on a topic) creates the unit and starts this workflow at Step 2, with the client's topic as the focus.

## Must read (in this order)

Briefing the <<OUTPUT_UNIT>>, before The gate and every step up to the QA loop (rows R0 + R5):

1. `00-START-HERE.md` (full)
2. `04-agents/workflows/production.md` (full)
3. `04-agents/templates/job-ticket.md` (full)
4. `01-brain/plan.md` (full)
5. the answers file
<!-- FILL: items 6 and up, one numbered line each: every bank the <<LEAD_SHORT>> picks allowed entries from, as "`03-banks/<file>.md` (full)". The whole list must equal row R5 in 00-START-HERE.md §4: same files, same order, same markers. Source: 00-START-HERE §4 row R5; TEAM-SPEC §10 (routing table); team.json banks[]. Length: 1 to 5 lines. Example: kit/The-Almanac/04-agents/workflows/pack-production.md, Must read, first list, items 6 and 7. -->

Compiling and delivering, before Compile DELIVERY.md, Deliver, and After delivery (rows R0 + R7):

1. `00-START-HERE.md` (full)
2. `04-agents/workflows/production.md` (full)
3. `04-agents/templates/delivery.md` (full)
4. `04-agents/templates/output-summary.md` (full)
5. the <<OUTPUT_UNIT>>'s `qa-report.md`
6. every output file of the <<OUTPUT_UNIT>>
7. `01-brain/plan.md` (sections: Rhythm, Delivery, Team and handoff)

The answers file is `02-sources/routine-answers/{{YYYY-MM-DD}}-routine-answers.md`. Bank units and on-demand units have no answers file: skip item 5 of the first list, and every ticket writes `none ({{reason}})` in its place (Writing and sending a ticket, item 2).

## The gate

Run the gate before Step 1, every time.

1. Open `00-START-HERE.md`: `setup_status` must be `complete`.
2. Open the frontmatter of all <<BRAIN_FILE_COUNT>> brain files in `01-brain/`: each `status` must be `approved`.
3. All checks pass: go to Step 1.
4. Any check fails: stop. Create no <<OUTPUT_UNIT>> folder and send no ticket.
5. Tell the client exactly what is missing, with template A (a brain file is not approved) or template B (setup is not complete). Name files in plain words: "your company file", "your voice file", "your plan file", and each other brain file by its title.
6. Reply a: for template A, run Stage 4 of [[04-agents/workflows/setup]] for each listed file; for template B, resume [[04-agents/workflows/setup]] where the session log says it stopped. Then run The gate again.
7. Reply b, or no reply: write a session-log entry with `Waiting on client: approval of {{files}}` (or `setup`). Ask again, once, at the start of the next session.

Template A:

```
I can't build your <<OUTPUT_UNIT>> yet. These still need your OK: {{your voice file, your plan file}}.
a) Review them now (about {{5 × number of files}} minutes)
b) Later. I'll ask again next time we talk.
```

Template B:

```
Your setup isn't finished, so I can't build your <<OUTPUT_UNIT>> yet. We stopped at: {{section in plain words}}.
a) Finish it now (about {{minutes left}} minutes)
b) Later. I'll ask again next time we talk.
```

## Step 1 · Create the <<OUTPUT_UNIT>>

1. Build the `output_id`. This item is the naming rule for every <<OUTPUT_UNIT>>, including on-demand ones:
   - Unit from answers: `YYYY-MM-DD-{slug}`. The date is the delivery day this unit is for: after a scheduled `routine-send`, the delivery day that follows the send date; after "questions now", the day the focus was picked (the unit is delivered that day).
   - Bank unit: `YYYY-MM-DD-bank-{slug}`. The date is the next delivery day on or after today, from [[01-brain/plan#Rhythm]].
   - On-demand unit: `YYYY-MM-DD-od-{slug}`. The date is today (created in [[04-agents/workflows/on-demand]]).
   - Slug: 2–5 lowercase words from the focus's core idea (on-demand: the requested topic), joined with hyphens, using only `a–z`, `0–9`, and `-`, max 40 characters.
   - If `05-outputs/{{output_id}}/` already exists, add `-2` to the end of the slug (then `-3`).
   - Example (fictional): the focus "Short onboarding checklists beat long handbooks" becomes `2026-10-05-short-onboarding-checklists`.
2. Create the folder `05-outputs/{{output_id}}/` and the folder `05-outputs/{{output_id}}/tickets/`.
3. Create `05-outputs/{{output_id}}/00-summary.md` from [[04-agents/templates/output-summary]], with the frontmatter exactly as the template shows: this unit's `output_id`, `kind: {{routine | bank | on-demand}}`, `status: in-progress`, `created: {{today}}`, and `delivered` empty until Deliver. Fill every other field the template shows.
4. Copy the proposed brain changes from the routine (routine Part 3) into `00-summary.md` → `## Proposed brain changes`, in the format After delivery gives. Add every further proposal from this <<OUTPUT_UNIT>> to the same list.
5. Decide which outputs this <<OUTPUT_UNIT>> gets and give each one a row in `00-summary.md` → `## Files`: every output whose row in [[01-brain/plan#Outputs and quantities]] says Active = yes, plus every output an active output depends on (directly or through another output), whatever its own row says. A row that says `on demand` gets no ticket in a unit from answers or a bank unit.

## Writing and sending a ticket

Every step below uses this procedure for each specialist it names.

1. Write `05-outputs/{{output_id}}/tickets/{{agent-file-name}}.md` from [[04-agents/templates/job-ticket]] (`{{agent-file-name}}` = the specialist's charter file name without `.md`), with the frontmatter exactly as the template shows: the ticket `{{output_id}}/{{agent-file-name}}`, this unit's `output_id`, `agent: {{Agent name}}`, `created: {{today}}`.
2. Fill the sections in the template's order:
   1. `# Job ticket: {{Agent name}} · {{output_id}}`
   2. `## Task`: the deliverable and its quantity, as the step says.
   3. `## Must read (in this order)`: rows R0 + the specialist's row (R12 and up) with real paths: the real <<OUTPUT_UNIT>> folder, the real answers file, and the exact bank entry IDs. When a file in the row does not exist for this <<OUTPUT_UNIT>>, keep the line and write `none ({{reason}})` in place of the path. Example (fictional): `the answers file: none (bank <<OUTPUT_UNIT>>; use the entries named in this ticket)`.
   4. `## Depends on`: 1 wikilink per output this job depends on, as the step says (`[[05-outputs/{{output_id}}/{{output file without .md}}]]`), or `none ({{reason}})`.
   5. `## Brief`: as the step says. Bullet 1 is always the focus sentence (the core idea); the other bullets are the points to cover. When a bullet restates something the client said, copy the client's words exactly.
   6. `## Allowed material`: bank entry IDs only, plus any extra source file the step names, or `none`. List only entries with `Permission: public-ok` that meet every use condition in their bank's Rules (for example a reuse wait, unless you write the ID followed by `(repeat ok)`).
   7. `## Requirements`: as the step says: every exact line, limit, or choice this job must meet, 1 per bullet, each copied character for character from its source and followed by that source in parentheses; or `none`.
   8. `## Output`: the template's lines, with the real save path `05-outputs/{{output_id}}/{{output file}}`.
   9. `## Packet`: empty (see Packet mode). `## Revision notes`: empty.
3. Send the ticket with your platform's sub-agent feature (your install runbook says how). Message: `Read 00-START-HERE.md, then your charter, then every file in your job ticket: 05-outputs/{{output_id}}/tickets/{{agent-file-name}}.md`. When a step names several specialists, send every ticket at once if your platform runs sub-agents in parallel; otherwise send them one at a time, in the order the step lists them.
4. Receive the reply. Its first line must start with `LOADED:`. A BLOCKED reply, a late reply, or a reply without a LOADED line goes to Timeouts and failures.
5. Open the output file. It must exist, and its first line after the frontmatter must be the LOADED line. Copy that line into `00-summary.md`. File missing: switch to Packet mode.
6. Run the QA loop on the file.
7. After `qa-pass` the file is locked: nobody edits it again.
8. A step starts only when every output its specialists depend on has `qa-pass` (rule 10). A file without `qa-pass` never feeds a later step.

<!-- FILL: one "## Step N · <the job in plain words>" section per production step, numbered from Step 2, in dependency order: Step 2 holds the specialists whose depends_on is empty; each later step holds the specialists whose depends_on outputs all come from earlier steps. Specialists with on_demand_only: true get no step. List the specialists of one step in team.json order. Each step is a numbered list that says: (1) when it runs: "Run this step for each specialist below whose output is in this <<OUTPUT_UNIT>> (Step 1, item 5)."; (2) each ticket to write, with the specialist's name, its routing row (R12 and up), the ticket path `05-outputs/{{output_id}}/tickets/<file stem>.md`, and the output path `05-outputs/{{output_id}}/<output_file>`, written and sent per Writing and sending a ticket; (3) the `## Task` line: the deliverable with its quantity per <<OUTPUT_UNIT>> from [[01-brain/plan#Outputs and quantities]], with a fictional example; (4) the `## Depends on` lines: one wikilink per depends_on output, or `none (first step)`; (5) what the `## Brief` must contain after the focus bullet: the points to cover and where each comes from (the focus block, a named section of an output it depends on, the client's words); (6) the `## Requirements` lines: every exact line to copy with its source file and section (copied character for character), every limit, and every choice, plus what the ticket uses instead when the source of a line is an output this job does not depend on and that output is off or held back in this <<OUTPUT_UNIT>>; (7) which bank entries may go under `## Allowed material`, from which banks, and how many; (8) "Start only when every output under `## Depends on` has `qa-pass`. Run the QA loop on each file as it arrives."; (9) Step 2 only: which output's title line the <<OUTPUT_UNIT>> uses, noted as `{{title}}` for Compile DELIVERY.md and Deliver. Name the shared sections (Writing and sending a ticket, QA loop, Held-back outputs) instead of repeating their rules. Source: team.json specialists[] (name, file, job, row, output_file, depends_on, on_demand_only); TEAM-SPEC §12.4 ("This team's order"), §9.1 (contracts), and §15 (output specs); each specialist's charter ("Inputs you get"). Length: 6 to 14 numbered items per step. Example: kit/The-Almanac/04-agents/workflows/pack-production.md, Steps 2 to 4 (the pillar step, the lead magnet step with its 8-week list, and the platform step with its dispatch order and default angles). -->

## QA loop

Run this loop for every output file, in every step. The QA Agent works from routing row R6.

1. Before the first QA request of the <<OUTPUT_UNIT>>, set `00-summary.md` → `status: in-qa`.
2. Send the QA Agent this request with your platform's sub-agent feature:

   ```
   Read `00-START-HERE.md`, then your charter, then every file in this QA request.
   QA request · {{output_id}} · round {{n}}
   Output file: `05-outputs/{{output_id}}/{{file}}`
   Specialist's charter: `04-agents/{{agent-file-name}}.md`
   Ticket: `05-outputs/{{output_id}}/tickets/{{agent-file-name}}.md`
   ```

3. Read the reply. Line 1 is the LOADED line. Line 2 is `Verdict: {{PASS | FIX | FAIL}} · {{file}} · round {{n}} · fixes: {{count}}`. Check that `qa-report.md` has the new section and that the file's `status` changed (in packet mode, save both yourself). Record `{{file}} · round {{n}} · {{verdict}}` in `00-summary.md`.
4. PASS: the file is locked. Continue with the step that sent it here.
5. FIX in round 1 or 2: add this block at the end of the specialist's ticket, under `## Revision notes`:

   ```
   ### Round {{n+1}}
   QA round {{n}} verdict: FIX
   {{the numbered list under "Fixes (exact):" in qa-report.md, pasted word for word}}
   ```

   Then send the specialist: `Read 00-START-HERE.md, then your charter, then every file in your job ticket: {{ticket path}}. Round {{n+1}}: apply every fix under ## Revision notes → ### Round {{n+1}} and change nothing else. Set revision: {{n+1}} and status: draft, and write a new LOADED line.` Run QA round n+1 on the result.
6. FAIL in round 1 or 2: add the same block with `QA round {{n}} verdict: FAIL`, the numbered list from qa-report.md, and the line `Redo the whole file from this ticket. Do not patch the old version.` Then send the specialist: `Read 00-START-HERE.md, then your charter, then every file in your job ticket: {{ticket path}}. Round {{n+1}}: redo the file from scratch, following ## Revision notes → ### Round {{n+1}}. Set revision: {{n+1}} and status: draft, and write a new LOADED line.` Run QA round n+1 on the result.
7. Round 3 without PASS (the reply ends with `held-back recommended`): set the file's `status: held-back`. The reason is the list of failing check names in its round-3 section. Add `{{file}} · {{reason}}` under `## Held back` in `00-summary.md`, then follow Held-back outputs.
8. Never run a 4th round. A file without `qa-pass` never reaches the client and never feeds a later step.

## Held-back outputs

1. No ticket goes out for an output that depends on a held-back output, directly or through another output, unless a fallback line below names that held-back output. Record each output that stops under `## Held back` in `00-summary.md` as `{{output file}} · not written: waits on {{held-back file}}`. It goes under `## Held back` in `DELIVERY.md` with the reason "waits on {{held-back output in plain words}}".
2. Outputs that do not depend on the held-back output continue as their steps say.
3. Fallbacks: when a fallback line below names the held-back output, its dependents still get their tickets. Each such ticket writes `none (held back)` for it under `## Depends on` and in `## Must read (in this order)`, and uses the named fallback instead. Outputs with no fallback line follow item 1.
   <!-- FILL: one bullet, indented under item 3, per output that others depend on and that has a named fallback in TEAM-SPEC §12.4 "Held-back rules": "- `<output_file>` held back: its dependents still start; they use <the fallback, for example a line copied from a named brain file section under ## Requirements> instead." When no output has a named fallback, delete this comment and replace item 3 with: "3. Fallbacks: none. Every held-back output stops its dependents (item 1)." Source: TEAM-SPEC §12.4 ("Held-back rules"); team.json specialists[] (depends_on). Length: 0 to 1 line per output that others depend on. Example: kit/The-Almanac/04-agents/workflows/pack-production.md, Step 3, items 8 and 9 (lead magnet held back: the platform tickets use the fallback CTA). -->
4. Stop the <<OUTPUT_UNIT>> when the held-back output is the base (every other output of this <<OUTPUT_UNIT>> depends on it, directly or through another output), or when every output of this <<OUTPUT_UNIT>> is held back or waits on one: set `00-summary.md` → `status: held`, send no other ticket, send the client the template below, and log the session. The held folder stays as it is.
   - Reply a: pick a new focus and start a new <<OUTPUT_UNIT>> at Step 1 with a new `output_id`. Unit from answers: the answer with the next highest score in the same answers file (routine Part 4). Bank unit: the next entry by the routine's Bank <<OUTPUT_UNIT>> procedure. On-demand unit: ask the client for a new focus in 1 message.
   - Reply b: start a bank <<OUTPUT_UNIT>> ([[04-agents/workflows/routine]] → Bank <<OUTPUT_UNIT>> procedure).
   - Bank or on-demand unit: in the template, replace option a with `a) Try a different idea`.

   ```
   The main piece of this <<OUTPUT_UNIT>> didn't pass my quality checks after 3 tries, so I stopped before the rest.
   a) Build it from a different answer you gave me
   b) Build it from {{the source bank, in the client's words}} instead
   Reply a or b.
   ```

## Compile DELIVERY.md

1. Read the second list under Must read (rows R0 + R7).
2. Create `05-outputs/{{output_id}}/DELIVERY.md` from [[04-agents/templates/delivery]]. It has no frontmatter.
3. Title: the template's title line, with `{{delivery_day}}` = this <<OUTPUT_UNIT>>'s date (the first 10 characters of `output_id`) and `{{title}}` = the title noted in Step 2.
4. Next line: `Built from:`, then every brain file as `name vN` with its current `version`, then `QA: all passed`. If any output is held back or not written, end the line with `QA: {{n}} passed, {{n}} held back` instead. Example (fictional): `Built from: company v1 · voice v3 · plan v2 · QA: all passed`.
5. `## This <<OUTPUT_UNIT>> in 30 seconds`: fill every line as the template says.
6. 1 section per `qa-pass` file, in file-number order, with the section names from the template and continuous numbering (1, 2, 3…; skip no number when an output is off or held back; a file from an agent that runs only on demand goes last, without a number). Copy each file's client-facing content exactly, word for word, as the template's "How to compile" says (it lists the internal parts to remove), and move every heading in it 1 level down (`##` becomes `###`).
7. `## Check before using`: every `[BRACKETED CAPS]` marker in the included files, each marker once, with where it appears (Example (fictional): `[BOOKING LINK]: summary, item 2`). Then every item on the `Check before using:` line of each included file's last section in `qa-report.md`. Nothing to list: `Nothing. Ready to use.`
8. `## Held back`: 1 line per held-back or not-written file: `{{output in plain words}}: {{the reason in plain words}}`. Leave the section out when nothing is held back.
9. `## 2-minute feedback`: exactly as the template gives it.
10. Never add a file without `qa-pass`, and never rewrite anything while compiling.
11. `DELIVERY.md` is for the client: never write "ticket", "receipt", "sub-agent", "frontmatter", or "routing table" in it.

## Deliver

1. Read [[01-brain/plan#Delivery]]: `chat` or `chat + google-doc`. `DELIVERY.md` always stays in the <<OUTPUT_UNIT>>'s folder.
2. `chat`: send the intro message (template below, max 80 words), then the content of `DELIVERY.md`. If it does not fit in 1 message, split it into several. Split only between 2 `##` sections or between 2 pieces; never cut a piece or a section in half.
3. `chat + google-doc`: create 1 Google Doc titled with the title line of `DELIVERY.md` (without the `# `), holding the content of `DELIVERY.md`. Put the link in the intro message, then send the `DELIVERY.md` content in chat as in item 2.
4. The Google Doc cannot be created: deliver in chat only, and add this line to the intro message: `The Google Doc didn't work this time, so everything is here in chat.` Note it in the session log.
5. Update `00-summary.md`: `status: delivered`, `delivered: {{today}}`, and fill its `## Delivery` section.

Intro template (leave out the lines that do not apply):

```
Your <<OUTPUT_UNIT>> for {{delivery_day}} is ready: "{{title}}".
Inside: {{counts in plain words}}.
Before using it, check the {{n}} items under "Check before using".
{{n}} piece(s) held back. The reason is at the end.
Google Doc: {{link}}
Edit freely and send back anything you change.
```

## After delivery

1. Bank use: for every bank entry a delivered file used (listed in its ticket's `## Allowed material` and used in the file), add `{{output_id}} ({{output labels}})` at the front of the entry's `Used in` line, separated from older items by `; ` (it replaces `none`). Output label = the output file's name without its number and `.md`. List only delivered files, never held-back ones. List the same uses under `## Material used` in `00-summary.md`.
2. Set each used entry's `Status` where its bank's Rules say so. This includes the source entry of a bank <<OUTPUT_UNIT>> and the entry behind a question that fed the focus.
3. Set `updated` to today in every bank you changed.
4. Write the session-log entry at the top of `06-log/session-log.md`:

   ```
   ## {{YYYY-MM-DD HH:MM}} · Production
   - Did:
     - Built and delivered <<OUTPUT_UNIT>> {{output_id}}: {{n}} files passed QA, {{n}} held back
   - Changed: 05-outputs/{{output_id}}/ (created), {{each bank changed | no bank changed}}
   - State: <<OUTPUT_UNIT>> {{output_id}} delivered
   - Next: feedback-check on {{YYYY-MM-DD}} at {{HH:MM}}
   - Waiting on client: {{brain change approvals | action approvals | nothing}}
   ```

5. Proposed brain changes (this item owns where they go): every brain change proposed while processing the answers ([[04-agents/workflows/routine]] Part 3) or while building this <<OUTPUT_UNIT>> is 1 line in `00-summary.md` → `## Proposed brain changes`: `- {{file}} → {{section}}: "{{before, or (new)}}" → "{{after}}" ({{source}})`. Step 1 starts the list. Right after delivery, send ONE approval message for these items, following [[04-agents/workflows/learning-loop#Approval batching]]: max 5 items; with more than 5, send the first 5 and keep the rest for the next batch. No items: send nothing.
6. Apply each "yes" with [[04-agents/workflows/learning-loop#Brain change procedure]]. "show": send that item's full before and after, then ask yes or no for it. "no": log it and change nothing.
7. Actions: the team acts only as [[01-brain/plan#Authority]] allows (rule 5). For each action listed under With approval that this <<OUTPUT_UNIT>> prepared, ask first: 1 message, 1 numbered line per action naming its exact target (max 5 per message), reply like `1 yes 2 no`. Do exactly that action on "yes"; do nothing on "no" or no reply. Actions listed under Allowed: do them and confirm each in 1 line. Everything else is the client's to do. Log every action taken in the session log.
8. Send nothing else about this <<OUTPUT_UNIT>>. The next contact about it is the `feedback-check` schedule ([[04-agents/workflows/learning-loop]] Part C).

Approval template:

```
{{n}} quick updates to <<VAULT_NAME>> from this <<OUTPUT_UNIT>>:
1. {{Voice file}}: "{{before, or (new)}}" → "{{after}}"
2. {{Plan file}}: "{{before, or (new)}}" → "{{after}}"
Reply like: 1 yes 2 no 3 show
```

## Packet mode

Use packet mode when any of these is true:
1. A sub-agent or the QA Agent replies BLOCKED because it cannot open vault files.
2. A sub-agent's reply starts with a LOADED line, but its file is missing at the Output path.
3. `packet_mode: yes` in `00-START-HERE.md` (the file-access test at install failed; the Install entry in `06-log/session-log.md` says so).

Steps:
1. For each item in the ticket's `## Must read (in this order)` except the ticket itself, paste the text into the ticket's `## Packet` under the heading `### {{path}} · {{version}}`:
   - "(full)": the whole file, frontmatter included.
   - "(sections: …)": the frontmatter, `## TL;DR`, and the named sections.
   - Bank entries named in the ticket: only those entries.
   - Version label: brain files `v{{version}}`; kit files `kit {{kit_version}}`; output files `r{{revision}}`; banks and logs `updated {{updated}}`; source files `{{date}}`.
2. Replace the text of `## Output` with: `Packet mode: you cannot save files. Reply with the LOADED line, then the complete file (frontmatter first, then the LOADED line again, then the content). The <<LEAD_SHORT>> saves it to {{output path}}.`
3. Send the whole ticket text as the message. The sub-agent cannot open the ticket file.
4. Save the returned file (everything after the reply's first line) to the Output path exactly as received. Change nothing.
5. The receipt lists the same files, in the same order, as in normal mode.
6. QA in packet mode: paste every file of routing row R6 (the QA Agent's Must read list: the output file, the specialist's charter, the ticket, and the rest of the row) into the QA request the same way. The QA Agent replies with the section and a `Status to set:` line. Add the section to `qa-report.md` and set the file's `status` yourself.
7. Once packet mode starts, use it for every remaining ticket and QA request in this <<OUTPUT_UNIT>>. If the install test failed, use it for every <<OUTPUT_UNIT>>. Note it in the session log.

## Mode fallback

Use mode fallback when a sub-agent is unavailable (your platform cannot create or reach it) or fails to respond twice (see Timeouts and failures).

1. Read that agent's charter (full), then every item in its ticket's `## Must read (in this order)`, in order.
2. Do the job yourself, following the charter exactly. Save the file at the ticket's Output path.
3. Make the first line after the frontmatter `LOADED (<<LEAD_SHORT>> fallback): ` followed by the same file list a sub-agent would write.
4. QA still runs: send the file to the QA Agent (QA loop). For FIX or FAIL rounds, apply the revision notes yourself under the same rules as the specialist.
5. QA Agent unavailable, or it fails to respond twice: run every check in [[04-agents/qa-agent]] yourself, exactly as written there. Write the section in `qa-report.md` with `QA by <<LEAD_SHORT>> (fallback)` as the first line under the section heading, and set the file's `status`.
6. Note every fallback in the session log (`Did: mode fallback for {{agent}}`). In the next <<OUTPUT_UNIT>>, send that agent its ticket first again.

## Timeouts and failures

1. No reply from a sub-agent or the QA Agent within 30 minutes: send the same message again, 1 time.
2. No reply within 30 minutes after that retry: mode fallback.
3. A reply without a LOADED line that is not a BLOCKED reply: send it back 1 time with `Your reply must start with the LOADED line.` A 2nd bad reply: mode fallback.
4. BLOCKED reply: read the `NEED:` line, then:
   - A ticket error (wrong path, missing ID, missing section): fix the ticket and resend. This does not count as a failure.
   - Cannot open vault files: Packet mode.
   - A brain file missing, empty, or not approved, or a fact only the client knows: ask the client in 1 message (max 80 words, lettered options when possible). Save the reply word for word to `02-sources/routine-answers/{{YYYY-MM-DD}}-{{slug}}.md` (slug: 2–5 words naming what you asked). If the client does not know, log a `Q-###` in `06-log/open-questions.md`. Then resend.
5. The same file BLOCKED 3 times: set its `status: held-back` with the reason and follow Held-back outputs.
6. Never deliver an unchecked file. A file without `qa-pass` goes under `## Held back`, never into the sections of `DELIVERY.md`.

## Checklist

1. The gate passed: `setup_status: complete` and all <<BRAIN_FILE_COUNT>> brain files have `status: approved`.
2. `05-outputs/{{output_id}}/`, `tickets/`, and `00-summary.md` (`status: in-progress` at creation) exist, and `output_id` follows the naming rules in Step 1.
3. Every output of this <<OUTPUT_UNIT>> (Step 1, item 5) got exactly 1 ticket, or is listed under `## Held back` as waiting on a held-back output.
4. Every ticket has every section of the job-ticket template in order, real paths under `## Must read (in this order)`, and only `public-ok` IDs under `## Allowed material`.
5. No ticket went out before every output it depends on reached `qa-pass`.
6. Every output file has 1 qa-report section per round, and no file had more than 3 rounds.
7. `DELIVERY.md` holds only `qa-pass` files in file-number order, plus the `Built from:` line, `## This <<OUTPUT_UNIT>> in 30 seconds`, `## Check before using` (every marker listed), `## Held back` (when needed), and `## 2-minute feedback`.
8. The <<OUTPUT_UNIT>> went out as [[01-brain/plan#Delivery]] says, and `00-summary.md` shows `status: delivered` and the delivery date.
9. Every bank entry used lists this <<OUTPUT_UNIT>> in its `Used in` line, and every `Status` change its bank's Rules ask for is made.
10. The session-log entry exists.
11. At most 1 approval message went out, with max 5 items.
12. Every action taken was allowed by [[01-brain/plan#Authority]], and every With approval action had the client's yes to that exact action.
<!-- FILL: 0 to 3 more lines, numbered from 13, for team-specific checks the production steps add (for example "Every ticket's required line was copied character for character from its source."). Delete this comment when there are none. Source: the production steps above; TEAM-SPEC §12.4 ("This team's order" and "Held-back rules"). Length: 0 to 3 lines. Example: kit/The-Almanac/04-agents/workflows/pack-production.md, Checklist, items 5 to 7. -->
