---
type: workflow
name: setup
kit_version: <<KIT_VERSION>>
owner: <<LEAD_FILE>>
---

# Workflow: setup

## Purpose
<!-- One-time onboarding. The only workflow that runs before the brain files exist. -->
Turn a fresh install into a working <<TEAM_NAME>> in about <!-- FILL: the setup interview length as a range of minutes written with an en dash, exactly as in the heading of TEAM-SPEC §12.2 (for example "45–60"). Source: TEAM-SPEC §12.2 (heading and the setup interview design table). Length: 1 range. Example: kit/The-Almanac/04-agents/workflows/setup.md, Purpose ("45–60"). --> minutes of the client's time: interview the client, build the <<BRAIN_FILE_COUNT>> brain files and get each one approved, switch on the schedules, and offer the first <<OUTPUT_UNIT>>. The client never does homework: material drops are optional, and the interview fills every gap.

## When it runs
1. Right after the install finishes (the last step of the install starts this workflow).
2. At any session start where `setup_status` in `00-START-HERE.md` is `not-started` or `in-progress`.
3. When the client says "redo {{section}}": run only Redo a section.
4. Never run Stages 1–6 when `setup_status` is `complete`.

## Must read (in this order)
Rows R0 (Any task · Everyone) and R2 (Setup interview · <<LEAD_SHORT>>), copied from the routing table in [[00-START-HERE]]:
1. `00-START-HERE.md` (full)
2. `04-agents/workflows/setup.md` (full)
3. `04-agents/question-banks/setup-interview.md` (full)
4. all <<BRAIN_FILE_COUNT>> brain files (full)
5. every file in `02-sources/` for this client
6. `06-log/open-questions.md` (full)

For Redo a section, and for any change to a brain file that is already `approved`, also read row R9: `04-agents/workflows/learning-loop.md` (section: Brain change procedure); the target brain file (full); `06-log/session-log.md` (newest entry).

## Before you start
1. Open `06-log/session-log.md`. It must contain an entry whose heading ends in `· Install`. If it does not, stop and finish the install first: `kit/INSTALL.md` when the frontmatter of `00-START-HERE.md` says `platform: grokbot`, `kit/INSTALL-HERMES.md` when it says `platform: hermes` (both runbooks ship with the kit, outside the vault).
2. Read `setup_status` in the frontmatter of `00-START-HERE.md`:
   - `not-started` → go to step 3.
   - `in-progress` → go to Resuming an interrupted setup.
   - `complete` → do not run setup. If the client said "redo {{section}}", go to Redo a section. Otherwise send: "Setup is already done. Say 'redo voice' (or any part) to change one part."
3. Check `status` in the frontmatter of all <<BRAIN_FILE_COUNT>> brain files. Each must be `empty` or `draft`. If any is `approved`, an earlier setup exists: set `setup_status: in-progress` and go to Resuming an interrupted setup.
4. Set `setup_status: in-progress` in `00-START-HERE.md`.
5. Create `02-sources/interview/{{date}}-setup-interview.md` (`{{date}}` = today) with this frontmatter, then the heading `# Setup interview · {{date}}`:
   ```
   ---
   type: source
   kind: interview
   date: {{YYYY-MM-DD}}
   permission: public-ok
   ---
   ```
6. Note the start time. The time budgets in [[04-agents/question-banks/setup-interview]] run from it.
7. Until the time zone is set in [[01-brain/plan#Rhythm]], use your device's clock for dates and times.

## Stage 1 · Welcome
1. Send the welcome message. `{{client_first_name}}` = the first word of `client_name` in `00-START-HERE.md`; if it is empty, start with "Hi." only.
2. On a) or any reply other than "later": go to Stage 2.
3. On b) or "later": write a session-log entry with `State: Setup 1/6 · waiting to start` and stop. Start Stage 2 when the client next writes.

Welcome message:
```
Hi {{client_first_name}}. I'm your <<LEAD_NAME>>. First I'll learn your business in a short interview: about <!-- FILL: the same range as in Purpose above. Source: TEAM-SPEC §12.2 (heading). Length: 1 range. Example: kit/The-Almanac/04-agents/workflows/setup.md, Stage 1, Welcome message ("45–60"). --> minutes, one question at a time. You can pause anytime and pick up later. Voice notes are welcome, and rambling is fine. Ready?
a) yes, let's go
b) later
```

## Stage 2 · Optional drops
1. Send the drops request once. Never send it again and never ask the client to find anything.
2. File every drop the moment it arrives, using the table and steps below. After each drop (or batch of drops sent together), send the drop received message.
3. On "skip", "done", "no", "nothing", or "that's it": pre-fill the brain drafts (steps below), then go to Stage 3.
4. Drops that arrive later, at any point in setup, are filed the same way. Confirm them in one line and check them against the questions not yet asked.

Drops request:
```
If you have any of these handy, drop them now: <!-- FILL: 3 to 5 kinds of material this team learns from fastest, in plain words the client uses, comma-separated (for example "past proposals you liked, your price list, your website link"), the same kinds as TEAM-SPEC §12.2 step 2. Source: TEAM-SPEC §12.2, step 2 (Optional drops); Team Brief field 4 (Inputs). Length: max 25 words. Example: kit/The-Almanac/04-agents/workflows/setup.md, Stage 2, Drops request ("posts you love or hate, call or podcast transcripts, your website link, offer or pricing docs"). -->. Don't go looking. If you have nothing, say skip.
```

Drop received:
```
Got it: saved {{n}} {{item / items}} to <<VAULT_NAME>>. Anything else handy? Send it, or say done.
```

Where each drop goes:
| Drop | Folder | kind | permission |
|---|---|---|---|
| The client's own published work (web pages, articles, posts, guides) | `02-sources/documents/` | `document` | `public-ok` |
| The client's own unpublished documents (drafts, SOPs, templates, internal docs, offer or pricing docs, private emails) | `02-sources/documents/` | `document` | `ask` |
| Other people's work the client loves or hates | `02-sources/documents/` | `document` | `private` (style and standards only, never quoted) |
| Call, meeting, podcast, or webinar transcripts or recordings | `02-sources/transcripts/` | `transcript` | `ask` |
| Voice notes sent as drops (not interview answers) | `02-sources/routine-answers/` | `routine-answers` | `public-ok` (the client's own words; third-party details are handled per bank entry) |
| Website link or website text, bios, brand docs | `02-sources/other/` | `other` | `public-ok` if the client published it, else `ask` |
<!-- FILL: one more row per kind of drop named in the drops request above that no row covers, in the same 4 columns, using only the folders and kinds in 02-sources/README.md. Delete this comment when every kind is covered. Source: the drops request above; TEAM-SPEC §12.2, step 2; the permission defaults in 02-sources/README.md. Length: 0 to 3 rows. Example: kit/The-Almanac/04-agents/workflows/setup.md, Stage 2, "Where each drop goes". -->
| Anything the client calls confidential, private, or under NDA | the folder above for its type | the kind above for its type | `private` |

Filing steps (one file per drop):
1. Name the file with the pattern in that folder's `README.md` (for example `YYYY-MM-DD-{{slug}}.md`, `YYYY-MM-DD-loved-{{slug}}.md`, `YYYY-MM-DD-meeting-{{slug}}.md`): today's date, then 2–5 lowercase kebab-case words saying what it is. If the name exists, add `-2`, `-3`. Example (fictional): `2026-09-24-meeting-team-kickoff.md`.
2. Frontmatter: `type: source`, `kind` and `permission` from the table, `date: {{YYYY-MM-DD}}` (today).
3. Body: the first line or lines that folder's `README.md` requires (`What it is:` in documents and other, `Speakers:` in transcripts, `Received:` in routine-answers), then the content verbatim. Never edit a source file after saving it.
4. Links: if you can open the link (a web page or a shared document), save its text verbatim; for a website, save max 5 pages (home, about, services or pricing, testimonials, contact). If you cannot open it, save the link alone; that drop answers no question.
5. Audio or video: transcribe it with your platform's transcription. If that fails, save a file with the file name or link and the line `Not transcribed`. Never ask the client to transcribe a drop.
6. Other people's work (`private`): use it only to learn which style traits and standards the client likes or hates. Never quote it and never copy its wording.

Pre-fill the brain drafts from drops:
1. Read every drop. For each core question in [[04-agents/question-banks/setup-interview]] that a drop answers completely, write the answer into the brain section named in that question's Fills line. Set that brain file to `status: draft`, `updated: {{today}}`.
2. In the interview file, add the question's heading with `Answered by drop: [[02-sources/{{folder}}/{{file name without .md}}]]`. In Stage 3, confirm it in one line instead of asking (the question's "Skip if" rule).
3. A drop that answers only part of a question answers nothing: ask the question.
4. A drop is never approval. The client approves every brain file in Stage 4.
5. <!-- FILL: where the exact words of the client's customers (or the other people this team's work is for) go when a drop quotes them in a transcript, review, or email: the brain file and section that collect exact words, the label `verbatim`, and the source file name, in 1 sentence. When no brain file collects exact words, write: "Quotes from other people in drops stay in their source file; they go into no brain file." Source: team.json brain_files (sections); TEAM-SPEC §12.2 ("Exact words from memory"); the coverage map in the team's setup-interview.md. Length: 1 sentence. Example: kit/The-Almanac/04-agents/workflows/setup.md, "Pre-fill the brain drafts from drops", item 4. -->

## Stage 3 · Interview
1. Run the sections in this order: Company → <!-- FILL: every domain brain file's section title in team.json brain_files order, each followed by " → ", with a short parenthesis for any special round the question bank adds to it (for example "(with the pushback round)"). Delete this comment when the team has no domain brain files. Source: TEAM-SPEC §12.2, step 3 and the setup interview design table; team.json brain_files (core: false). Length: 1 line. Example: kit/The-Almanac/04-agents/workflows/setup.md, Stage 3, item 1 ("Customer → Offer (with the skeptical-buyer round) →"). -->Voice (with the 60-second voice memo and the this-or-that calibration) → Plan (with the outputs and Authority proposals). The pushback round closes the section it sits in. The question text, order, skip rules, follow-ups, and saving format live in [[04-agents/question-banks/setup-interview]].
2. Start each section with its intro line (below) as the first line of the message that carries the section's first question. `{{n}}` in an intro line = the section's position in the order above.
3. For every question, run this loop:
   1. Check its "Skip if" line. If it is already answered, confirm it in one line instead of asking.
   2. Send the question with its progress label, e.g. `Company · 4/6`.
   3. Save the reply verbatim to the interview file the moment it arrives.
   4. Apply the follow-up rule: vague answer → 1 follow-up; max 2 per question.
   5. "skip" or "don't know" → log a `Q-###` and move on.
   6. Go to the next question.
4. After a section's last core step (and its deep questions, if the client opted in), run Stage 4 for that section's brain file. Start the next section only after that file is approved or put off with "later".
5. Right after the file of the halfway section is approved (or put off), send the halfway check-in once. The halfway section is section number <<BRAIN_FILE_COUNT>> ÷ 2, rounded up, in the order above. On b): write a session-log entry with the State line and stop; resume with Resuming an interrupted setup.

Section intro lines (the first line of each section's first question message):
```
Part 1 of <<BRAIN_FILE_COUNT>>: your business. Quick facts first, about 6 minutes.
```
<!-- FILL: one fenced block per domain brain file, in team.json brain_files order, each holding 1 line: "Part {{n}} of <<BRAIN_FILE_COUNT>>: <what the section covers, in plain words>. <what happens in it or why it matters, max 12 words>. About <minutes> minutes." Keep {{n}} as written (the lead fills it). The minutes are that section's time budget in the setup interview design table of TEAM-SPEC §12.2 (the same number as its guidance comment in the team's setup-interview.md). Delete this comment when the team has no domain brain files. Source: TEAM-SPEC §12.2 (setup interview design table); team.json brain_files (core: false). Length: max 25 words per line. Example: kit/The-Almanac/04-agents/workflows/setup.md, Stage 3, section intro lines "Part 2 of 5" and "Part 3 of 5". -->
```
Part {{n}} of <<BRAIN_FILE_COUNT>>: how you sound. A 60-second voice note, a few quick ones, then you pick between short drafts. About 12 minutes.
```
```
Part <<BRAIN_FILE_COUNT>> of <<BRAIN_FILE_COUNT>>: your plan. Mostly letter answers. About 10 minutes.
```

Halfway check-in:
```
Want a break? We're halfway.
a) keep going
b) take a break (say "continue" when you're back)
```

## Stage 4 · Draft and approve
Run after each section, for that section's file: Company → `01-brain/company.md`, each domain section → its own file in `01-brain/`, Voice → `01-brain/voice.md`, Plan → `01-brain/plan.md`.
1. Draft the file: fill every section using the coverage map in [[04-agents/question-banks/setup-interview]] and the Drafting rules below. Set `status: draft` and `updated: {{today}}`.
2. File the section's bank entries per the Drafting rules.
3. Write `## TL;DR` last.
4. Send the review message: the TL;DR plus the 3 review points for that file (table below). The TL;DR and the 3 points together must be max 120 words.
5. If the client sends fixes, apply them and send only the changed lines: "Changed:" + the new lines + "Anything else? (or say ok)".
6. Approval = any of these replies, alone or with thanks, in any capitals: "ok", "okay", "yes", "good", "approved", "looks good", or a thumbs-up. Any other reply is a fix: apply it and re-show the changed lines.
7. On approval, set `status: approved`, `version: 1`, `approved_on: {{today}}`, `updated: {{today}}`, and add this line at the top of `## Changelog`: `- v1 · {{date}} · Approved in setup (setup)`. Send the approved confirmation. When the file is `01-brain/company.md`, also set `client_name` in the frontmatter of `00-START-HERE.md` to the name of the person you are interviewing, as the founder row of [[01-brain/company#Key facts]] gives it.
8. On "later": keep `status: draft`, log a `Q-###` ("Approve the {{file}} file"), send "No problem. It stays a draft for now, and I'll ask again before we finish.", and start the next section. No <<OUTPUT_UNIT>> can run until every brain file is approved.
9. After step 7 or step 8, write a session-log entry (type Setup) with `State: Setup 4/6 · {{Section}} file {{approved | draft}}`.

Review points per file:
| File | The 3 points to show |
|---|---|
| `01-brain/company.md` | 1. What makes us different 2. The top line of What we believe 3. Key facts: the business name and how to refer to the founder |
<!-- FILL: one row per domain brain file, in team.json brain_files order, in the same format: the file as a backticked path, then 3 numbered points, each naming the section (and, where it matters, the line) the team relies on most, in the client's words where the section holds exact words. Source: team.json brain_files (core: false) sections; TEAM-SPEC §20 (brain file section headings). Length: 1 row per domain file, max 30 words per row. Example: kit/The-Almanac/04-agents/workflows/setup.md, Stage 4, "Review points per file", the customer.md and offer.md rows. -->
| `01-brain/voice.md` | 1. The top 2 How we never sound rules 2. The client's own banned words 3. One Spoken voice sample line |
| `01-brain/plan.md` | 1. Outputs and quantities: every active output and its quantity per <<OUTPUT_UNIT>> 2. Rhythm: delivery day, question day and time, cadence, time zone 3. Authority: every action under With approval and Allowed, or "none" |

Review message:
```
Here's your {{file title in plain words}} file:

{{TL;DR, max 10 lines}}

3 things I'm relying on most:
1. {{point}}
2. {{point}}
3. {{point}}

What's wrong or missing? (or say ok)
```

Approved confirmation:
```
Approved. Saved to your {{file}} file. Next: {{next part, e.g. "Part <<BRAIN_FILE_COUNT>> of <<BRAIN_FILE_COUNT>>: your plan" | "switching everything on"}}.
```

## Stage 5 · Activate
Run only when all <<BRAIN_FILE_COUNT>> brain files are `approved`. If any file is still `draft`, send the message below. On a): run Stage 4 steps 4–9 for each draft file, one file per message. On b): write a session-log entry with `State: Setup 5/6 · waiting on approval: {{files}}` and stop.
```
Before I switch things on, {{n}} of your files still need your OK: {{list}}. Review now?
a) yes
b) later
```

1. Read [[01-brain/plan#Outputs and quantities]] (which outputs are active, and which specialist makes each), [[01-brain/plan#Rhythm]], and [[01-brain/plan#Delivery]].
2. Confirm the <<SUBAGENT_COUNT>> sub-agents exist (they were created at install): the QA Agent and every specialist in the "Who works here" table of [[00-START-HERE]]. A specialist stays in place even when its output is off, so switching an output on later needs no new agent. Create any missing one exactly as your install runbook describes: the sub-agents step of `kit/INSTALL.md` when `platform: grokbot`; the agent skills step of `kit/INSTALL-HERMES.md` when `platform: hermes`. If your platform cannot create sub-agents, write "mode fallback" in the session log; production then runs each charter itself ([[04-agents/workflows/production#Mode fallback]]).
3. Create every schedule in the schedules table of [[00-START-HERE]] with your platform's scheduler (your install runbook says how; on Hermes, its "Creating the scheduled tasks" part), in the time zone from Rhythm, with these exact names:

   | Schedule | When | Task it runs |
   |---|---|---|
   | `routine-send` | The Question time in Rhythm (default: day before delivery day, 10:00); repeats at the Rhythm cadence (every week for `weekly`, every 2 weeks for `every-2-weeks`) | `04-agents/workflows/routine.md` → Part 1 |
   | `routine-reminder` | Delivery day, 09:00; same cadence as `routine-send` | `04-agents/workflows/routine.md` → No answers |
   | `feedback-check` | 3 days after delivery day, 10:00; same cadence as `routine-send` | `04-agents/workflows/learning-loop.md` → Part C |
   | `monthly-review` | First delivery day of each month, after the delivery: set it for 17:00 that day | `04-agents/workflows/monthly-review.md`, after that day's <<OUTPUT_UNIT>> is delivered |
   <!-- FILL: one row per extra schedule in team.json schedules after the 4 fixed ones, in the same 3 columns: the backticked name, its default_time with how it repeats, and the workflow file and part it runs. When a team.json default_time of the 4 fixed schedules differs from the row above, change that row's When column to match team.json and the schedules table in 00-START-HERE.md. Delete this comment when there are only the 4 fixed schedules. Source: team.json schedules; TEAM-SPEC §14; the schedules table in 00-START-HERE.md §7. Length: 1 row per extra schedule. Example: the 4 rows above. -->

   The first `routine-send` run is the next question day after today (today, if today is the question day and the question time is still ahead).
4. If your platform has no scheduler (the Install entry in the session log says `Scheduler: no`), or the scheduler refuses a schedule twice (retry once), send "I can't set automatic reminders here, so say 'questions now' whenever you want your questions." and write the failure in the session log.
5. If the client picked Google Doc delivery in the Plan section (the interview file shows it; [[01-brain/plan#Delivery]] stays `chat` until this test works): create one Google Doc titled `<<VAULT_NAME>> test · {{date}}` containing the line "Test from your <<LEAD_NAME>>.", then send the Google Doc test message.
   - On a): change Delivery from `chat` to `chat + google-doc` with the brain change procedure ([[04-agents/workflows/learning-loop#Brain change procedure]]): `version` +1 and a changelog line. The client's pick in the Plan section is the approval of this exact change.
   - If the doc cannot be created, or on b): send the Google Doc fallback message. On a) OK there: Delivery stays `chat`. On b) try again: repeat step 5 once; if it fails again, send the fallback with only the option "a) OK".
6. Set `setup_status: complete` in `00-START-HERE.md`.
7. Write a session-log entry (type Setup): Did, Changed, `State: Setup 5/6 · activated`, Next, Waiting on client.
8. Send the activation summary. `{{routine_day}}` and `{{routine_time}}` = the day and time of the Question time in Rhythm; `{{feedback_day}}` = the `feedback-check` day from step 3. With no working scheduler (step 4), replace its first bullet with `- Say "questions now" whenever you want your questions.` and leave out the "First questions" line.
9. If any bank entry filed during setup has `Permission: ask`, send the permission message (Drafting rules, rule 6; max 6 items per message) before Stage 6.

Google Doc test:
```
Quick test: I made a Google Doc called "<<VAULT_NAME>> test · {{date}}". Can you open it? {{link}}
a) yes
b) no
```

Google Doc fallback:
```
Google Docs isn't working from here, so I'll deliver your <<OUTPUT_UNIT_PLURAL>> in chat. OK?
a) OK
b) try again
```

Activation summary:
```
You're all set. Here's your rhythm:
- {{routine_day}} {{routine_time}}: I send your questions. Answer by voice note or text.
- {{delivery_day}}: your <<OUTPUT_UNIT>> arrives {{here | here and in a Google Doc}}.
- {{feedback_day}}: I ask what you changed and what worked.
First questions: {{next_routine_date}}.
```

## Stage 6 · First <<OUTPUT_UNIT>>
1. Send the first-cycle choice. With no working scheduler, option b) reads `b) later (say questions now when you're ready)`.
2. On a): send setup complete message A, then run [[04-agents/workflows/routine]] Part 1 right away, as if the client had said "questions now".
3. On b): send setup complete message B.
4. Write a session-log entry (type Setup) with `State: Setup 6/6 · complete` and `Next: {{first routine date, or "answers to the first questions"}}`.

First-cycle choice:
```
Run your first questions now?
a) now (about <!-- FILL: the answering time for one <<ROUTINE_NAME>>, in minutes, as TEAM-SPEC §12.3 gives it (for example "15"). Source: TEAM-SPEC §12.3 ("Answering time"). Length: 1 number or range. Example: kit/The-Almanac/04-agents/workflows/setup.md, Stage 6, first-pack choice ("about 15 min"). --> min)
b) wait for {{routine_day}}
```

Setup complete message A:
```
Setup done. <<VAULT_NAME>> now knows your business, <!-- FILL: each domain brain file in plain words as "your <topic>", in team.json order, each followed by ", " (for example "your roles, your policies, "). Delete this comment when the team has no domain brain files. Source: team.json brain_files (core: false) titles. Length: max 10 words. Example: kit/The-Almanac/04-agents/workflows/setup.md, Setup complete message A ("your customers, your offer, "). -->your voice, and your plan. Your first questions are right below. Say help anytime to see what I can do.
```

Setup complete message B:
```
Setup done. <<VAULT_NAME>> now knows your business, <!-- FILL: the same words as in Setup complete message A above. Delete this comment when the team has no domain brain files. Source: Setup complete message A. Length: max 10 words. Example: kit/The-Almanac/04-agents/workflows/setup.md, Setup complete message B. -->your voice, and your plan. Your first questions arrive {{routine_day}} at {{routine_time}}. Say help anytime to see what I can do.
```
With no working scheduler, message B's third sentence reads: `Say questions now whenever you want your first questions.`

## Resuming an interrupted setup
1. Triggers: a session starts with `setup_status: in-progress`, or the client says "continue".
2. Find the resume point:
   1. Read the newest entry in `06-log/session-log.md` whose State starts with `Setup`.
   2. Read the interview file and find the last question heading with a saved answer.
   3. If the interview file is further ahead than the State line, the interview file wins: resume at the first core step after the last saved answer.
3. Send the resume message. `{{resume point}}` = the progress label (e.g. `Voice · 5/10`), or, outside Stage 3, the step in plain words (e.g. "the review of your voice file").
4. On "yes", continue from that point:
   - Stage 1 or 2: send the drops request if no drop and no "skip" arrived yet; otherwise go to Stage 3.
   - Stage 3: ask the question at the resume point.
   - Stage 4: re-send that file's review message.
   - Stage 5: restart at step 1; keep every schedule that already exists with the right name and time.
   - Stage 6: re-send the first-cycle choice.
5. On "start this section over": re-ask the section's core steps from the first one. Keep the old answers in the interview file; the newest answer wins.

Resume message:
```
Welcome back. We stopped at {{resume point}}. Continue? (yes / start this section over)
```

## Redo a section
1. Trigger: the client says "redo {{section}}", where section names 1 brain file by its title (`company` also answers to "business"). That section's file must already be `approved`; if it is not, run Stage 4 for it instead.
2. Read the R9 files listed in Must read.
3. Create `02-sources/interview/{{date}}-setup-interview-redo-{{section}}.md` (`kind: interview`, `permission: public-ok`; `{{section}}` = the brain file's name without `.md`) and save every answer there verbatim.
4. Re-ask the section's core steps from [[04-agents/question-banks/setup-interview]] in order, each with its current answer (template below). Voice: re-run the 60-second voice memo and the this-or-that calibration in full, with no current answer shown. A step where you propose and the client confirms (for example the outputs and Authority proposals in Plan) re-runs with the current approved text as the proposal.
5. Offer the deep questions as in Stage 3 (the question bank's deep-question rule).
6. Collect every change. Send them in one message as "before → after" lines (a file review, so it may exceed 80 words), ending "Apply these changes? (yes / fix)".
7. On yes: apply them with the brain change procedure ([[04-agents/workflows/learning-loop#Brain change procedure]]): `version` +1, `updated`, changelog line `- v{{n}} · {{date}} · Redo of the {{section}} section (redo)`, and a session-log entry.
8. If Rhythm changed (delivery day, question time, cadence, or time zone): delete and recreate every schedule as in Stage 5 step 3.
9. <!-- FILL: extra redo rules for this team's brain files, one sentence each, for a section whose names or values other files reuse (for example "If the categories changed, set every bank entry whose category no longer exists to the closest new category."). Delete this item when there are none. Source: TEAM-SPEC §20 (brain file sections) and §21 (banks); team.json banks[] (fields that copy a brain file value). Length: 0 to 2 sentences. Example: kit/The-Almanac/04-agents/workflows/setup.md, Redo a section, step 9 (pillars changed → bank entries). -->

Redo question message:
```
{{Section}} · {{n}}/{{N}} · {{question}}
Right now I have: "{{current answer, max 25 words}}"
Keep it, or tell me the new answer. (keep / new answer)
```

## Drafting rules
<!-- How answers become brain files and bank entries. Apply them in Stage 4 and in Redo a section. -->
1. Use the client's words. Rephrase only to fit a sentence; keep their key terms and their spelling of names.
2. Never polish quotes from the client's customers or anyone else. Keep slang, grammar, and swearing exactly as recorded.
3. A number or result becomes a fact only if the client stated it plainly or confirmed it on a follow-up. Unsure numbers ("about", "I think", "roughly") → log a `Q-###` and keep the number out of every brain file and bank entry until the client confirms it.
4. Bank entries: every answer that holds material a bank collects (the definitions in [[04-agents/workflows/routine]] → Part 3) → a new entry in that bank, in the entry format written in the bank file, with Source `[[02-sources/interview/{{date}}-setup-interview]]`. Where a brain file relies on the entry, add a pointer after the line: "(see {{ID}})".
5. Permission defaults for bank entries: the client's own experience with no third-party names and no confidential numbers → `public-ok`; any third-party name, any result of one of the client's customers, or any confidential detail → `ask`; anything the client says is off the record → `private` (never used outside the vault).
6. Ask about `ask` items in the permission message (template below), max 6 items per message, each item max 8 words; send the next 6 after the client replies. Reply meanings: "yes" → `public-ok`, and add `(names: leave out)` at the end of the entry's `Names` line; "yes names ok" → `public-ok` and `(names: OK)`; "no" → `private`. When the entry has a `Verified by client` line, "yes" also sets it to `yes`.
   ```
   Before I use these, a quick check. Reply like "1 yes 2 no" (add "names ok" if I can use names):
   1. {{item, max 8 words}}
   2. {{item, max 8 words}}
   ```
7. IDs: take each new ID from the bank's `next_id`, then increase `next_id` by 1. Add new entries at the top of the entries section and set the bank's `updated` to today.
8. `## TL;DR`: write it last; max 10 lines and max 75 words; only the facts an agent needs first.
9. No `{{placeholders}}` in an approved file. Unknown = `UNKNOWN (Q-###)`. In `01-brain/voice.md`, `## Rules learned from edits` = `- none` at setup.
10. Keep every guidance comment (`<!-- … -->`) and every heading in the brain templates. Write the content under the comment.
11. Never write a third-party person's or company's name in a brain file; write the role instead (Example (fictional): "a clinic manager"). The name stays only in the interview file and in the bank entry's `Names` line.
12. From `private` sources (other people's work), only style traits and standards go into the brain files, never their words. People the client names as style models never appear in `01-brain/voice.md`.
13. `## Open questions` in each brain file lists that file's open `Q-###` IDs, one per line, each with the question in max 10 words.
<!-- FILL: the drafting rules for this team's domain brain files and banks, numbered from 14, one sentence each: which answers become which bank entries and with which fields, which section lists bank IDs, and what each domain file's TL;DR must contain. Delete this comment when the team has none. Source: TEAM-SPEC §20 (brain file sections), §21 (banks), and §11.8 (bank entry formats); team.json brain_files and banks. Length: 0 to 5 rules. Example: kit/The-Almanac/04-agents/workflows/setup.md, Drafting rules 5, 8, 9, and the customer.md part of rule 11. -->

## Edge cases
1. Several answers in one long voice note: extract each answer, save each under its own question, confirm what you took in one message (max 3 lines), and skip those questions.
2. The client wants to stop: save everything, write a session-log entry with `State: Setup {{stage}}/6 · {{Section}} · {{n}}/{{N}}`, and send: "Saved. Say continue anytime and we'll pick up at {{Section · n/N}}."
3. More than one business: send "I set up one business at a time. Which one is this for? a) {{business 1}} b) {{business 2}}". Build every file for that business only, then add one line: "For {{other business}}, set up a separate agent with its own copy of this kit." Never mix 2 businesses in one vault.
4. Something the client sells that has not launched yet: in `01-brain/company.md` → What we sell, write `(not launched yet)` after it. State no results for it, and when you draft the plan file, add to [[01-brain/plan#Areas to avoid]]: "Results for {{product or service}} until it has customers · reason: not launched yet".
5. The client refuses the voice memo: send the typed fallback once ("No problem. Type 5 sentences exactly the way you'd say them out loud.") and never ask for a recording again.
6. The client asks "why do you need this?": reply with that section's line, then repeat the question.
   - Company: "So everything the team makes says what you do in your words, not generic ones."
   - Voice: "So everything I write sounds like you, not like AI."
   - Plan: "So you get the right work on the right days, and the team only does what you allow."
   <!-- FILL: one bullet per domain brain file in the same form, "- <Title>: "So <the benefit to the client in plain words, max 15 words>."". Delete this comment when the team has no domain brain files. Source: team.json brain_files (core: false); TEAM-SPEC §20 (brain file sections). Length: 1 bullet per domain file. Example: kit/The-Almanac/04-agents/workflows/setup.md, Edge cases, item 6 (Customer and Offer lines). -->
7. Contradictory answers: send one message: "Earlier you said {{A}}. Now you said {{B}}. Which is right? a) {{A}} b) {{B}} c) something else". Keep both verbatim in the interview file; use the chosen one.
8. No customers yet: ask the questions about customers as questions about the people the client wants to serve, and say so in the question. Record only what the client says from real conversations; otherwise write `UNKNOWN (Q-###)`. Never invent a quote, a result, or a testimonial.
9. A real client name appears in an answer: keep it verbatim in the interview file; in brain files write the role (Drafting rules, rule 11); in bank entries list it in the entry's `Names` line with `Permission: ask`.
10. The client wants to skip a whole section: log one `Q-###` per unanswered core question and draft the file with `UNKNOWN (Q-###)`. Plan is the exception: send "I need a few quick answers to switch things on." and ask the Plan questions that fill Outputs and quantities, Rhythm, and Delivery, then send the Authority proposal for a yes.

## Setup complete checklist
Setup is complete only when every line is true:
1. `setup_status: complete` and `client_name` are set in `00-START-HERE.md`.
2. All <<BRAIN_FILE_COUNT>> brain files have `status: approved`, `version` 1 or higher, `approved_on` set, and a `v1` changelog line.
3. Every brain file's `## TL;DR` is filled (max 10 lines), and no brain file contains `{{`.
4. `01-brain/voice.md` → Spoken voice has 3 or more samples, How we sound has 5 or more rules, and Bad examples has 2 or more entries (or a `Q-###` logs each gap).
5. `01-brain/plan.md` → Outputs and quantities has Active and the quantity filled on every row; Rhythm has cadence, delivery day, question time, time zone (IANA), and paused until; Delivery is `chat` or `chat + google-doc`; Authority has With approval and Allowed filled (actions, or none).
6. Every schedule from Stage 5 step 3 (`routine-send`, `routine-reminder`, `feedback-check`, `monthly-review`, and any extra one) exists with the times from Rhythm, or the scheduler failure is in the session log and the client was told.
7. The interview file holds every answer verbatim, and every skipped question has a `Q-###`.
8. Every `ask` item filed during setup was in a permission message.
9. If Google Doc delivery was chosen, the test ran and Delivery matches the result.
10. The session log has an entry with `State: Setup 6/6 · complete`.
<!-- FILL: 0 to 3 more lines, numbered from 11, each a minimum a domain brain file must meet after setup, with the Q-### fallback (for example "`01-brain/<file>.md` → <section> has 5 or more entries, or a Q-### logs the gap."). Delete this comment when there are none. Source: the guidance comments of the domain brain files (their count ranges); TEAM-SPEC §20 (brain file sections). Length: 0 to 3 lines. Example: kit/The-Almanac/04-agents/workflows/setup.md, Setup complete checklist, items 4 and 7. -->
