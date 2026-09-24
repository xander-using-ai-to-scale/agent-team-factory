---
type: workflow
name: learning-loop
kit_version: <<KIT_VERSION>>
owner: <<LEAD_FILE>>
---

# Learning loop

> Client edits become rules the QA Agent can test, winners become saved patterns, and every brain file change goes through 1 approved procedure.

## Purpose

1. Turn every edit the client makes into a voice rule the QA Agent can test, or into a fact fix in the brain file that holds the fact, with the client's approval.
2. Turn every winner into a saved pattern the specialists reuse.
3. Ask for feedback once per <<OUTPUT_UNIT>>, without nagging.
4. Hold the only procedure for changing a brain file: `## Brain change procedure` below.

## Triggers

| The client says or the scheduler does | Run |
|---|---|
| The client sends back an edited version of a delivered piece | Part A |
| The client says `this isn't me: {{your version}}` | Part A |
| The client says `winner: {{which piece}} {{result}}` | Part B |
| The `feedback-check` schedule fires | Part C |
| Any change to a file in `01-brain/`: an approved rule, `update my {{file}}: {{change}}`, `change delivery day to {{day}}`, `change question time to {{time}}`, `add {{output}}`, `remove {{output}}`, `pause questions for {{N}} weeks`, `resume questions`, a monthly review answer, a fact fix | Brain change procedure |

## Must read (in this order)

Client edits, "this isn't me", winners, and the feedback check (rows R0 + R8):

1. `00-START-HERE.md` (full)
2. `04-agents/workflows/learning-loop.md` (full)
3. `06-log/edits-log.md` (full)
4. `01-brain/voice.md` (full)
5. the original draft
6. the client's version

Any brain file change (rows R0 + R9):

1. `00-START-HERE.md` (full)
2. `04-agents/workflows/learning-loop.md` (section: Brain change procedure)
3. the target brain file (full)
4. `06-log/session-log.md` (newest entry)

Winners and the feedback check have no client version: skip item 6 of the first list.

## Part A · Client edits

1. Save the client's version, word for word, to `02-sources/documents/{{YYYY-MM-DD}}-edit-{{output label}}.md` (output label = the edited output file's name without its number and `.md`), with frontmatter `type: source`, `kind: document`, `date: {{YYYY-MM-DD}}`, and `permission` as rule 3 of [[02-sources/documents/README]] says (a third-party name makes it at least `ask`). Lines 1 and 2 follow that README: `What it is: edit · Written by: client · From: {{link, file name, or "pasted in chat"}}`, then `Client's reason: "{{their words}}"` or `Client's reason: not given`.
2. Find the original. Search the 8 newest folders in `05-outputs/`, newest first, for a piece of the same output that shares at least 1 full sentence, the opening line, or the same bank entry with the client's version.
   - Exactly 1 match: that piece is the original.
   - 0 matches or 2 or more: send the "Which piece" template below and wait.
   - The client says it is new writing: stop Part A. The saved document stays in `02-sources/documents/`.
3. Compare the original and the client's version sentence by sentence. List every change as `"{{original excerpt}}" → "{{client excerpt}}"`.
4. Classify each change as exactly 1 of: removed words, added words, shortened, tone, structure, facts. A change that only corrects a misspelled word is a typo: ignore it.
5. Facts (a price, a name, a number, a date, a claim, a detail of what the client sells), and bans (the client says never to use a topic, claim, or name again): make no voice rule. Run the Brain change procedure on the brain file section that holds it: the section that states the fact, or [[01-brain/plan#Areas to avoid]] for a ban. If the fact lives in a bank entry, correct that entry's field and add the line `- Corrected: {{YYYY-MM-DD}}, was "{{old value}}"` at the end of the entry.
6. Every other change: name the pattern in 1 sentence. Example (fictional): "The client deletes every opening question and starts with the answer."
7. If `01-brain/voice.md` already has a rule (not archived) that says the same thing, write no new rule. Add `QA missed rule: "{{rule}}" ({{output_id}}/{{file}})` to the `Did:` line of this session's log entry, and stop Part A for this pattern.
8. Write 1 proposed rule the QA Agent can test: 1 sentence that names a word, a count, a position, or a structure.
   - Example (fictional), bad: `Be more casual.`
   - Example (fictional), good: `Never open with a question; open with the answer in 12 words or fewer.`
9. Log it at the top of the entries in `06-log/edits-log.md`, using the ID in `next_id`. Then raise `next_id` by 1 and set `updated` to today. Several changes with the same pattern share 1 entry.

   ```
   ### E-{{###}} · {{YYYY-MM-DD}} · {{output label}}
   - Draft: [[05-outputs/{{output_id}}/{{output file name without .md}}]] ({{unit}})
   - What the client changed: {{short description}}
   - Before: "{{excerpt}}"
   - After: "{{excerpt}}"
   - Pattern: {{one sentence}}
   - Proposed rule: {{one sentence, testable}}
   - Client decision: pending
   - Applied: not applied
   ```

10. Add the E-### to the approval batch (see Approval batching).
11. On "yes": run the Brain change procedure on `01-brain/voice.md` → `## Rules learned from edits`. The change adds the line `- {{rule}} (E-###, added v{{N}})`, where N is the new version number, and replaces `- none` when it is the first rule. The "yes" in the batch is the approval: do not ask again.
12. If the new rule conflicts with an existing rule: add ` (archived {{YYYY-MM-DD}}, replaced by E-###)` to the end of the old rule's line, and end the changelog line with `; replaced rule "{{old rule}}"`.
13. Top-10 rule: a rule is top-10 when its pattern appears in 2 or more E-### entries, or when the client said "never", "always", or "hate" about it. Add a top-10 rule to `## TL;DR` of `01-brain/voice.md` when the TL;DR has fewer than 10 lines. When it has 10 lines, replace the TL;DR line on the same topic; when no line has the same topic, leave the TL;DR unchanged.
14. In the E-### entry, set `Client decision: approved` and `Applied: voice v{{N}} on {{YYYY-MM-DD}}`.
15. On "no": set `Client decision: rejected` and keep `Applied: not applied`. Change nothing else.
16. Log the session with the format in Part C, step 6.

"Which piece" template:

```
Which piece is this?
a) {{date}} · {{output in plain words}} · "{{first 6 words}}…"
b) {{date}} · {{output in plain words}} · "{{first 6 words}}…"
c) None of these (send the original, or say "new")
```

## Part B · Winners

1. Find the piece the client means, as in Part A, step 2. Unsure: send the "Which piece" template.
2. Log it at the top of the entries in `06-log/winners.md`, using the ID in `next_id`. Then raise `next_id` by 1 and set `updated` to today.

   ```
   ### W-{{###}} · {{YYYY-MM-DD}} · {{output label}}
   - Piece: [[05-outputs/{{output_id}}/{{output file name without .md}}]] ({{unit}})
   - Result (client's words or numbers): "{{the client's words, word for word}}"
   - Why it likely worked: {{one sentence naming 1 pattern: the opening, a story, the format, the topic, or the timing}}
   - Saved as: {{bank entry ID | none}}
   ```

3. Save the winner's reusable part: <!-- FILL: the bank that stores winning patterns (as `03-banks/<file>`), the part of the piece to save (for example its opening line), the entry fields to fill with `Source: W-###`, and the duplicate rule: when the same text is already saved, add nothing and write that entry's ID in `Saved as`. It must say the same as rule 6 of 06-log/winners.md. When no bank stores winning patterns, write "Write `Saved as: none`; this team keeps winner patterns in [[06-log/winners]] only." Source: team.json banks[]; the team's 06-log/winners.md rule 6; TEAM-SPEC §12.5 (Winner). Length: 2 to 4 sentences. Example: kit/The-Almanac/04-agents/workflows/learning-loop.md, Part B, step 3 (the opening line saved to 03-banks/hooks.md as H-###). -->
4. If the client's message names a follow-up request (Example (fictional): "people asked for part 2"), file it as a new entry in the source bank named in [[04-agents/workflows/routine]] → Bank <<OUTPUT_UNIT>> procedure, with `Source: client said in chat {{YYYY-MM-DD}}` and the status that makes it usable there.
5. Reply with 1 line:

   ```
   Logged as a winner. Your team will reuse what worked.
   ```

6. Log the session with the format in Part C, step 6.

## Part C · Feedback check

1. The `feedback-check` schedule fires (setup Stage 5 sets its time; default: 3 days after delivery day, 10:00, in the client's timezone).
2. If Paused until in [[01-brain/plan#Rhythm]] holds a date later than today, log "skipped: paused until {{date}}" and end. If no <<OUTPUT_UNIT>> was delivered within one cadence period before today (7 days for `weekly`, 14 days for `every-2-weeks`), send nothing and end.
3. Send exactly this message, once per <<OUTPUT_UNIT>>:

   ```
   Quick one: did you use anything from your last <<OUTPUT_UNIT>>? Send back any piece you changed, or say 'winner: …'. 'Nothing' is fine too.
   ```

4. An edited piece: Part A. `winner: …`: Part B. "nothing", "no", "not yet", or "didn't use it": log the session and stop.
5. No reply: do nothing. Never send a 2nd feedback message for the same <<OUTPUT_UNIT>>, and never bring it up again.
6. Log the session at the top of `06-log/session-log.md`:

   ```
   ## {{YYYY-MM-DD HH:MM}} · Feedback
   - Did:
     - {{feedback check sent | 2 edits logged (E-004, E-005) | winner logged (W-002) | client said nothing}}
   - Changed: {{files created or changed | nothing}}
   - State: Feedback for {{output_id}} {{done | sent}}
   - Next: {{next action + when}}
   - Waiting on client: {{approval of E-004, E-005 | nothing}}
   ```

## Brain change procedure

Use this procedure for every change to a file in `01-brain/`, for any reason. Only you, the <<LEAD_SHORT>>, run it. Sub-agents never run it and never edit brain files.

1. Identify the file (`01-brain/{{file}}.md`) and the exact section (`## {{section}}`).
2. Write the change as Before → After. Before = the exact current text (`(new)` when you add something). After = the exact new text.
3. Ask the client with the template below, or as 1 item of an approval batch (see Approval batching). Skip this step only when the client already said yes to this exact Before → After in a batch, or when the change is the one a `pause questions for {{N}} weeks` or `resume questions` command names (that command is the approval, as [[01-brain/plan#Rhythm]] says).
4. On "yes":
   1. Apply the After text exactly.
   2. In the frontmatter: raise `version` by 1, set `updated: {{today}}` and `approved_on: {{today}}`.
   3. Add a line at the top of `## Changelog`: `- v{{N}} · {{YYYY-MM-DD}} · {{change}} ({{source}})`. The source is the E-### or W-### ID, `monthly review {{YYYY-MM}}`, `client request {{YYYY-MM-DD}}`, or `routine {{YYYY-MM-DD}}`. Example (fictional): `- v4 · 2026-10-08 · Added rule "Never open with a question" (E-006)`.
   4. If the change touches a fact or rule stated in `## TL;DR`, update that TL;DR line. The TL;DR stays at 10 lines or fewer.
   5. If the file is `01-brain/plan.md` and the change touches `## Rhythm` → Cadence, Delivery day, Question time, or Timezone, update the schedules as described below this list. A change to `## Delivery` or to Paused until needs no schedule change.
   6. Record the change in this session's log entry: `Changed: 01-brain/{{file}}.md v{{N}} ({{section}})`.
   7. Confirm to the client in 1 line: `Saved to your {{file}} file.`
5. On "no": add `Declined: {{file}} · {{section}} · {{short change}}` to the `Did:` line of this session's log entry. For an E-###, set `Client decision: rejected`. Change nothing in the brain file.
6. Never edit a brain file without a yes.
7. Never delete. An outdated line or entry stays in the file; add `(archived {{YYYY-MM-DD}})` to its end.

After a `## Rhythm` change, use your platform's scheduler (your install runbook says how):
1. Delete every schedule in the schedules table of [[00-START-HERE]]: `routine-send`, `routine-reminder`, `feedback-check`, `monthly-review`, and any extra one listed there.
2. Recreate all of them from the new `## Rhythm`, exactly as [[04-agents/workflows/setup#Stage 5 · Activate]] step 3 says. All times are in the timezone stored in `## Rhythm`.
3. Paused until never deletes or pauses a schedule ([[04-agents/workflows/routine#Pauses and skipped cycles]]).

Template (1 change):

```
Update your {{file}} file?
Before: "{{before}}"
After: "{{after}}"
Reply yes or no.
```

## Approval batching

1. Pending items are: E-### entries with `Client decision: pending`, the lines under `## Proposed brain changes` in the current <<OUTPUT_UNIT>>'s `00-summary.md`, and the proposals from a monthly review.
2. Send pending items in 1 message: max 5 items, numbered 1–5, oldest first. Items 6 and up wait for the next batch.
3. Each item is 1 line of max 30 words: `{{n}}. {{file in plain words}}: "{{before, or (new)}}" → "{{after}}"`. Shorten a long Before or After with "…"; the client can say "show".
4. Reply format: `1 yes 2 no 3 show`. Accept any clear equivalent: "all yes", "yes to 1 and 3", a voice note.
5. "show": send the full Before and After for that item (template below), then wait for yes or no on it.
6. Send at most 1 batch per session: at the end of the exchange that produced the items; for a <<OUTPUT_UNIT>>, right after delivery ([[04-agents/workflows/production#After delivery]]); for a monthly review, after the answers ([[04-agents/workflows/monthly-review]], Step 3).
7. An item with no answer stays pending and goes into the next batch. After 2 batches with no answer, treat it as "no": for an E-###, set `Client decision: rejected`; for a line in `00-summary.md`, add `(declined: no reply)` to its end. Note it in the session log.
8. An approval batch counts as a brain-file review, so the 80-word message limit does not apply. Every other client message rule does.

Batch template:

```
{{n}} quick updates to <<VAULT_NAME>>:
1. {{Voice file}}: "{{before}}" → "{{after}}"
2. {{Company file}}: "{{before, or (new)}}" → "{{after}}"
Reply like: 1 yes 2 no 3 show
```

"show" template:

```
Item {{n}}, in full.
Before: "{{full before}}"
After: "{{full after}}"
Yes or no?
```

## Checklist

1. Every client edit either has an E-### with a testable proposed rule, went through the Brain change procedure as a fact fix or a ban, or was a typo.
2. Every edited version is saved in `02-sources/documents/`.
3. No brain file changed without the client's yes (or the pause or resume command that named the change).
4. Every approved change raised `version` by 1, set `updated` and `approved_on`, and added a changelog line with its source.
5. Approved rules sit under `## Rules learned from edits` as `- {{rule}} (E-###, added vN)`; replaced rules end with `(archived …, replaced by E-###)`.
6. Every winner has a W-### in `06-log/winners.md`, and its reusable part is saved as Part B step 3 says.
7. The feedback message went out at most once per <<OUTPUT_UNIT>>.
8. Every approval batch had max 5 items.
9. Every `## Rhythm` change deleted and recreated every schedule.
10. This session has a session-log entry.
