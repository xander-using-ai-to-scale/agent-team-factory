---
type: workflow
name: routine
kit_version: <<KIT_VERSION>>
owner: <<LEAD_FILE>>
---

# Workflow: routine

## Purpose
<!-- The recurring engine: questions in, one focus out, then production. -->
Every cycle (the cadence in [[01-brain/plan#Rhythm]]), send the client the <<ROUTINE_NAME>> questions in one message, save the answers verbatim, file what they contain into the banks, pick the strongest focus, and hand it to production. The answers are the raw material for every <<OUTPUT_UNIT>>. The client knows this routine as the <<ROUTINE_NAME>>; the schedules and files call it "routine".

## Triggers
1. The `routine-send` schedule fires → Part 1.
2. The client says "questions now" → Part 1.
3. The client answers a <<ROUTINE_NAME>> question (voice note or text) → Part 2.
4. The `routine-reminder` schedule fires → No answers.
5. The client says "bank" or "bank <<OUTPUT_UNIT>>", or replies "bank" to the reminder → Bank <<OUTPUT_UNIT>> procedure.
6. The client says "pause questions for {{N}} weeks" or "resume questions", or asks in plain words to skip this cycle's questions → Pauses and skipped cycles.

## Must read (in this order)
Copied from the routing table in [[00-START-HERE]].

R0 · Any task (every trigger above):
1. `00-START-HERE.md` (full)

R3 · Write <<ROUTINE_NAME>> questions (Part 1):
1. `04-agents/workflows/routine.md` (full)
2. `04-agents/question-banks/routine-questions.md` (full)
3. `01-brain/plan.md` (full)
4. `06-log/questions-asked.md` (full)
<!-- FILL: items 5 and up, one numbered line each: the domain brain files and the banks used to personalize the questions, as "`01-brain/<file>.md` (full)" or "(sections: ...)" and "`03-banks/<file>.md` (full)". The whole list must equal row R3 in 00-START-HERE.md §4: same files, same order, same markers. Delete this comment when row R3 has no more items. Source: 00-START-HERE §4 row R3; TEAM-SPEC §10 (routing table); team.json brain_files and banks. Length: 0 to 5 lines. Example: kit/The-Almanac/04-agents/workflows/ritual.md, Must read, R3 items 3 and 6 (customer.md (full), ideas.md (full)). -->

R4 · Process <<ROUTINE_NAME>> answers (Parts 2–4, No answers, Bank <<OUTPUT_UNIT>> procedure):
1. `04-agents/workflows/routine.md` (full)
2. the answers file in `02-sources/routine-answers/`
3. `01-brain/plan.md` (sections: Goal, Areas to avoid)
<!-- FILL: items 4 and up, one numbered line each: the domain brain file sections used to tag new entries and spot proposed brain changes, then every bank the answers are filed into, as "`03-banks/<file>.md` (full)". Add any plan.md domain section row R4 names inside the brackets of item 3. The whole list must equal row R4 in 00-START-HERE.md §4: same files, same order, same markers. Source: 00-START-HERE §4 row R4; TEAM-SPEC §10 (routing table); team.json brain_files and banks. Length: 1 to 8 lines. Example: kit/The-Almanac/04-agents/workflows/ritual.md, Must read, R4 items 3 to 5. -->

Part 5 continues with row R5 inside [[04-agents/workflows/production]]. Pauses use row R9 (the brain change procedure in [[04-agents/workflows/learning-loop#Brain change procedure]]).

## Part 1 · Send the questions
1. Gate check. All 4 must be true:
   1. `setup_status: complete` in `00-START-HERE.md`.
   2. All <<BRAIN_FILE_COUNT>> brain files have `status: approved`.
   3. [[01-brain/plan#Rhythm]] → Paused until is `no`, or a date on or before today (then run Pauses and skipped cycles, step 2, first).
   4. No <<ROUTINE_NAME>> was sent in the last 3 days (the newest date in `06-log/questions-asked.md` is 3 or more days ago).
2. If check 1 or 2 fails, send once: "Your questions are on hold until you approve your {{file}} file. Review it now? a) yes b) later". On a): run Stage 4 of [[04-agents/workflows/setup]] for that file. Log the skip and stop.
3. If check 3 fails: on a scheduled run, send nothing, log "Routine skipped: paused until {{date}}", and stop. On "questions now", send "Questions are paused until {{date}}. Send them now anyway? a) yes b) no"; on a) continue (the pause stays).
4. If check 4 fails: on a scheduled run, send nothing, log "Routine skipped: questions sent {{date}}", and stop. On "questions now", continue.
5. Pick the questions with the picking rules in [[04-agents/question-banks/routine-questions]]. Those rules set how many (5 by default).
6. Personalize them with the personalization rules in the same file.
7. Send ONE message with the template below. It may exceed 80 words because it carries every question and the answer instructions; keep it max 30 words per question plus 80 words (5 questions: max 230 words).
   - Greeting (1 line): scheduled run → "Hi {{client_first_name}}. Your questions for {{delivery_day}}'s <<OUTPUT_UNIT>>:"; "questions now" → "Here are your questions:". The first scheduled run after a pause ends adds a second line: "Your questions are back on."
   - The answer instructions: the answer instructions block in [[04-agents/question-banks/routine-questions]], word for word.
   - The last line ("Also: …") goes on every <<ROUTINE_NAME>> except the first one after setup.
8. Log the questions at the top of the table in `06-log/questions-asked.md`, in the order sent, one row each (row format below). Answered starts as `no`.
9. Write a session-log entry (type Routine) with `State: Routine sent {{date}} · waiting on answers`.

Routine message:
```
{{greeting, 1 line}}

1. {{question 1}}
2. {{question 2}}
{{one numbered line per further question}}

{{the answer instructions block, word for word}}

Also: send back anything you changed from the last <<OUTPUT_UNIT>>, or tell me what worked.
```

Row format for `06-log/questions-asked.md` (Answered = `no`, `yes`, or `skipped`):
```
| {{YYYY-MM-DD}} | {{the category's "Log as" value}} | {{question as sent}} ({{template ID}}) | no |
```

## Part 2 · Receive and save answers
1. Answers can arrive over hours or days, in pieces, in any order, as voice notes or text. A message is an answer piece when it responds to one of the questions (by number or by content). Client commands (like "status" or "help") and unrelated requests are not answer pieces.
2. On the first piece, create `02-sources/routine-answers/{{date}}-routine-answers.md` (`{{date}}` = the day the questions were sent) with the frontmatter below and the heading `# Routine answers · {{date}}`.
3. Transcribe voice notes with your platform's transcription. If transcription fails, send the fallback message once per <<ROUTINE_NAME>>.
4. Append each piece at the end of the file as 1 block: `### Q{{n}} · {{question exactly as sent}}`, then `Received: {{YYYY-MM-DD HH:MM}} · {{voice memo | text}}`, then the piece verbatim. Never edit, trim, or reorder saved text, and never insert above existing text.
5. Match pieces to questions: use the number the client says; else match by content. A piece that moves from one question to the next becomes 1 block per question, split at the point the client moves on. A piece whose answers are mixed together stays 1 block under the first question it answers, with the line `Also answers: Q{{n}}` directly under `Received:`. A piece that answers none of the questions becomes a block headed `### Extra · {{what it is, 5 words or fewer}}` with the same `Received:` line.
6. "skip" for a question → a block for that question whose text is `Skipped`.
7. After each piece, confirm in one line: "Saved your answer to {{n}}. {{k}} to go." ({{k}} = questions neither answered nor skipped).
8. Close Part 2 when the first of these happens: every question is answered or skipped; the client says "done", "that's all", or "finished"; or the `routine-reminder` time on delivery day has passed and at least 1 question is answered.
9. On close: set Answered to `yes` or `skipped` in this <<ROUTINE_NAME>>'s rows of `06-log/questions-asked.md` (unanswered rows stay `no`), send "Thanks, that's what I need. Your <<OUTPUT_UNIT>> is on its way.", and go to Part 3.
10. Pieces that arrive after close: append them to the same file. If the first ticket of the <<OUTPUT_UNIT>> is not sent yet, include them in Parts 3–4; otherwise file them in Part 3 only, for future <<OUTPUT_UNIT_PLURAL>>.
11. An edited piece or a "this worked" note (the "Also:" line) is not an answer. Save it as an `### Extra` block, then run [[04-agents/workflows/learning-loop]] Part A (an edit) or Part B (a winner) on it. Never file it under a question.

Answers file frontmatter:
```
---
type: source
kind: routine-answers
date: {{YYYY-MM-DD}}
permission: public-ok
---
```

Transcription fallback:
```
I can't play voice notes right now. Could you use your phone's voice-to-text, or type it? Rough is fine.
```

## Part 3 · File into the banks
<!-- Turn raw answers into reusable entries. Banks change freely; brain files change only with the client's approval. -->
Definitions (use them exactly):
<!-- FILL: one line per bank in team.json banks[], in order: "- <Title> (`<prefix>-###`, `03-banks/<file>`): <what counts as an entry, with the test that decides it; a missing part means it is not an entry>. <which field gets which value when you file it, for example the category or type taken from the question's category>." Then 1 line for material that becomes a proposed brain change instead of a bank entry, naming the brain file section (for example the exact words of the client's customers, when a brain file collects them). Source: team.json banks[] (file, title, id_prefix); the entry format and Rules of each bank file; TEAM-SPEC §21 (banks) and §11.8 (bank entry formats). Length: max 45 words per line. Example: kit/The-Almanac/04-agents/workflows/ritual.md, Part 3, Definitions (Story, Proof, Hook, Idea, Customer phrase) and step 4 (Story Type and Pillar). -->

Steps:
1. Read the whole answers file, including every `### Extra` block.
2. For each answer, list every item that fits a definition above, and every fact that belongs in a brain file.
3. File each item in its bank, in the entry format written in that bank file, with `Source: [[02-sources/routine-answers/{{date}}-routine-answers]] (Q{{n}})`. Take the ID from the bank's `next_id`, add the entry at the top of `## Entries`, increase `next_id` by 1, and set the bank's `updated` to today. Never reuse or renumber an ID. If the same item is already in the bank, add nothing.
4. Permission defaults: the client's own experience with no third-party names and no confidential numbers → `public-ok`; any third-party name, any result of one of the client's customers, or any confidential detail → `ask`; anything the client calls off the record → `private`. A result of one of the client's customers is always `ask`. An entry is never more open than its source.
5. Facts that belong in a brain file (a new or changed fact for any section of any file in `01-brain/`, including a new banned word or a new area to avoid) are PROPOSED brain changes. Never edit a brain file here. Skip any fact the brain file already states in the same words. Keep the list for this session, 1 line each in the format below; production copies it into the <<OUTPUT_UNIT>>'s `00-summary.md` ([[04-agents/workflows/production#After delivery]] owns where proposals go and when they are asked). If the session has to end before production Step 1, copy the list into the session-log entry under `Did:` so the next session can carry it over.
6. Send ONE permission message for all `ask` items from this <<ROUTINE_NAME>> (template below): max 6 items, each max 8 words, in question order. Items beyond 6 stay `ask` and join the next <<ROUTINE_NAME>>'s message.
7. Reply meanings: "yes" → `public-ok`, and add `(names: leave out)` at the end of the entry's `Names` line; "yes names ok" → `public-ok` and `(names: OK)`; "no" → `private`. When the entry has a `Verified by client` line, "yes" also sets it to `yes`.
8. Production never waits for this reply. Tickets list only `public-ok` items. If a "yes" arrives before the first ticket is sent, add that item to the ticket's `## Allowed material`.

Proposed brain change (1 line each):
```
- {{file}} → {{section}}: "{{before, or (new)}}" → "{{exact text}}" (routine {{date}}, Q{{n}})
```

Permission message:
```
Before I use these, a quick check. Reply like "1 yes 2 no" (add "names ok" if I can use names):
1. {{item, max 8 words}}
2. {{item, max 8 words}}
```

## Part 4 · Pick the focus
1. Score every answered question (not skipped, not unanswered) on each row of the scoring rubric below, 0–3 per row.
2. The highest total wins. Tie → the higher score on the rubric's first row. Still tied → the answer with more words.
3. Write the focus: 1 sentence (the <<OUTPUT_UNIT>>'s core idea) and 3–6 key points, each 1 sentence, taken from the winning answer first, then from other answers that support it. Never add a fact the client did not say.
4. Apply the minimum material rule below.
5. Save the focus block in the session-log entry and pass it to Part 5. Production copies the focus sentence and the key points into the `## Brief` of the first ticket.

Scoring rubric:
<!-- FILL: a table with columns "Criterion | 0 | 1 | 2 | 3" and 3 or 4 rows, one per quality that makes an answer a good base for this team's <<OUTPUT_UNIT>>, each cell a testable description (what the answer contains at that score). Order the rows by importance: the first row breaks ties. One row must tie the answer to something a brain file states (a need, a goal, or an area in [[01-brain/plan#Goal]] or a domain file). Source: TEAM-SPEC §12.3 ("Angle rule": the criteria and the tie-break); team.json specialists[] (what the first output needs). Length: 3 to 4 rows. Example: kit/The-Almanac/04-agents/workflows/ritual.md, Part 4, Scoring rubric (Specific story, Clear opinion, Tied to a pain, Leads to an offer). -->

Minimum material rule: <!-- FILL: the smallest amount of real material the first output needs from the answers or the banks (for example "at least 1 story in the client's own words"), where to take it when the winning answer lacks it (other answers first, then the newest public-ok bank entry that meets its bank's reuse rule), and the one-time request to the client when nothing fits: the message (max 80 words, 1 question), a max 3-hour wait, then continue without it; the reply is saved word for word to `02-sources/routine-answers/{{YYYY-MM-DD}}-{{slug}}.md` and filed in Part 3. When the team has no minimum, write "none: any answered question can be the focus." Source: TEAM-SPEC §12.3 ("Angle rule"); the first specialist's charter (what it needs). Length: 2 to 5 sentences. Example: kit/The-Almanac/04-agents/workflows/ritual.md, Part 4, step 4. -->

Focus block:
```
Focus: {{one sentence}}
From: Q{{n}} · {{score}}/{{max score}} · [[02-sources/routine-answers/{{date}}-routine-answers]]
Key points:
- {{point 1}}
- {{point 2}}
- {{point 3}}
Bank entries: {{public-ok entry IDs, or "none"}}
```
`{{max score}}` = 3 × the number of rubric rows.

## Part 5 · Hand off to production
1. Follow [[04-agents/workflows/production]] from The gate, with: the answers file path, the focus block, the allowed bank entry IDs, and the proposed brain changes from Part 3. Production Step 1 builds the `output_id` (a unit from answers: `YYYY-MM-DD-{slug}`).
2. If the winning answer came from a question built on a bank entry, that entry counts as used: [[04-agents/workflows/production#After delivery]] records it.
3. Write a session-log entry (type Routine): `State: Routine {{send date}} processed · <<OUTPUT_UNIT>> {{output_id}} in production`, with the focus line ("Focus: Q{{n}}, {{score}}/{{max score}}") under `Did:`.

## No answers
1. Trigger: `routine-reminder` fires on delivery day.
2. Send nothing if any of these is true: no <<ROUTINE_NAME>> was sent for this delivery day; the answers file for this <<ROUTINE_NAME>> has at least 1 piece; the client asked to skip this cycle's questions; a reminder was already sent for this <<ROUTINE_NAME>>; Paused until in [[01-brain/plan#Rhythm]] holds a date later than today.
3. Otherwise send the reminder once. Max 1 reminder per <<ROUTINE_NAME>>.
4. Answers arrive → Part 2. Reply "bank" → Bank <<OUTPUT_UNIT>> procedure.
5. If nothing arrives by 23:59 on delivery day (client time): send no more messages, keep this <<ROUTINE_NAME>>'s rows at `no`, write a session-log entry "Routine {{date}}: no answers, no <<OUTPUT_UNIT>>", and let the next <<ROUTINE_NAME>> run as scheduled.
6. Answers that arrive after delivery day: run Parts 2–3, then send "Got your answers. Want a <<OUTPUT_UNIT>> from them now? a) yes, now b) save them for later". On a): run Parts 4–5 with today as the <<OUTPUT_UNIT>> date. On b): stop; the entries stay in the banks for future <<OUTPUT_UNIT_PLURAL>>.

Reminder:
```
Hi {{client_first_name}}. Your questions from {{routine_day}} are still open. Answer any 2 in a quick voice note and I'll build today's <<OUTPUT_UNIT>>. Or reply bank and I'll build it from {{the source bank, in the client's words}}.
```

## Bank <<OUTPUT_UNIT>> procedure
<!-- FILL: 2 lines. Line 1: "Source bank: `03-banks/<file>` (full). Usable entries: <the test, for example the Status value that marks an entry as unused, plus `Permission: public-ok`>." Line 2: "In the client's words: "<plain words for that bank, for example your saved ideas>"." Source: TEAM-SPEC §12.3 ("Bank option": the banks and the selection rule); team.json banks[]; the bank file's Status values and Rules. Length: 2 lines. Example: kit/The-Almanac/04-agents/workflows/ritual.md, Bank pack procedure, steps 3 to 5 (03-banks/ideas.md, entries with Status: new; "your idea bank"). -->

1. Triggers: the client says "bank" or "bank <<OUTPUT_UNIT>>", or replies "bank" to the reminder.
2. Run the gate checks 1 and 2 from Part 1. If one fails, follow Part 1 step 2.
3. Read the source bank (full) and the rest of row R4. A bank <<OUTPUT_UNIT>> has no answers file.
4. If the source bank has no usable entry, send "Nothing is left in {{the source bank, in the client's words}} right now. Want quick questions instead? Reply questions now." and stop.
5. Score every usable entry with the Part 4 rubric, using the entry's text. The highest total wins. Tie → the older entry (lower ID).
6. Supporting material: <!-- FILL: which other bank entries to attach to the winning entry (how many, from which banks, with `Permission: public-ok` and each bank's reuse rule), what to do when none fits the winner (take the next-best entry that has support; else keep the winner and attach the newest free entry from any area), and the message and stop when nothing is free (max 30 words, options "a) yes, questions now b) skip this time"). When the team attaches nothing, write "none: the source entry alone is the focus." Source: TEAM-SPEC §12.3 ("Bank option"); team.json banks[]; each bank's Rules (reuse). Length: 2 to 5 sentences. Example: kit/The-Almanac/04-agents/workflows/ritual.md, Bank pack procedure, step 6 (1 to 2 public-ok stories unused for 28 days). -->
7. Write the focus block (Part 4 format) with `From: {{entry ID}} · {{score}}/{{max score}}` and the attached public-ok IDs under Bank entries.
8. Follow [[04-agents/workflows/production]] from The gate with these rules: Step 1 builds a bank `output_id` (`YYYY-MM-DD-bank-{slug}`); every ticket's `## Must read (in this order)` lists `the answers file: none (bank <<OUTPUT_UNIT>>; use the entries named in this ticket)`, so every receipt shows it; the first ticket's `## Brief` names the source entry ID.
9. After delivery, the source entry counts as used: [[04-agents/workflows/production#After delivery]] records it, so it no longer passes the usable-entry test.
10. Write a session-log entry (type Routine): `State: Bank <<OUTPUT_UNIT>> {{output_id}} in production`.

## Pauses and skipped cycles
[[01-brain/plan#Rhythm]] owns the pause rules; this section carries them out.
1. "pause questions for {{N}} weeks":
   1. Resume date = today + N × 7 days.
   2. Change [[01-brain/plan#Rhythm]] → Paused until from `no` to the resume date with the brain change procedure ([[04-agents/workflows/learning-loop#Brain change procedure]]). The client's request is the approval of this exact change. `version` +1, changelog line, session log.
   3. Never pause or delete a schedule for this. The schedules keep running: while Paused until holds a date later than today, `routine-send`, `routine-reminder`, and `feedback-check` still fire and do nothing except log "skipped: paused until {{date}}". `monthly-review` runs normally.
   4. Send: "Done. No questions until {{resume date}}. Say resume questions anytime to restart sooner."
2. "resume questions", or the first `routine-send` on or after the resume date:
   1. Change Paused until back to `no` with the brain change procedure. The pause request already approved this change, so do not ask again. "resume questions" clears it at once.
   2. On "resume questions", send: "Questions are back on. Next ones: {{next routine date}}." On a `routine-send` run, continue with Part 1 (its greeting adds "Your questions are back on.").
3. Part 1 gate check 3 finds an arrived resume date on the first `routine-send` on or after it and runs step 2 first.
4. The client asks to skip this cycle's questions: log it in the session log, send "OK, no questions this time. Next ones: {{next routine date}}.", and send nothing else for that <<ROUTINE_NAME>>.
5. Missed cycles are never made up: never send 2 rounds of questions to catch up.

## Checklist
A <<ROUTINE_NAME>> is done when every line is true:
1. The gate check ran; any skip is in the session log with its reason.
2. The questions pass every picking and personalization rule in [[04-agents/question-banks/routine-questions]], and no template repeats within the window those rules set.
3. One message went out with every question, the answer instructions block, and the "Also:" line (except on the first <<ROUTINE_NAME>> after setup), within its word limit.
4. New rows sit at the top of `06-log/questions-asked.md`, one per question sent, each ending with its template ID tag.
5. The answers file exists with the right name and frontmatter, and every piece is saved verbatim as its own block.
6. Every row in `06-log/questions-asked.md` for this <<ROUTINE_NAME>> shows `yes`, `skipped`, or `no`.
7. Every item that fits a bank definition is filed with a new ID, and each changed bank has a new `next_id` and `updated`.
8. Brain facts are listed as proposed changes for the <<OUTPUT_UNIT>>'s `00-summary.md`; no brain file was edited outside the brain change procedure.
9. One permission message went out if any `ask` item exists (max 6 items).
10. Every answered question has a score; the focus block has 1 sentence and 3–6 key points, and the minimum material rule holds (or its one-time request was sent).
11. Production started with the focus block, and its Step 1 built the `output_id`.
12. Max 1 reminder went out for this <<ROUTINE_NAME>>.
13. A session-log entry records the <<ROUTINE_NAME>>.
