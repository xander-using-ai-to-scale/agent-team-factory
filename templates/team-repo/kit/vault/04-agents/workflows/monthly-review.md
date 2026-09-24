---
type: workflow
name: monthly-review
kit_version: <<KIT_VERSION>>
owner: <<LEAD_FILE>>
---

# Monthly review

> Once a month: count what happened, ask the client a few questions in 1 message, update the brain files with approval, and send a 5-line summary.

## Purpose

1. Keep the brain files true. What the client sells, prices, results, what customers ask, and things to avoid change over time.
2. Close open questions from `06-log/open-questions.md`.
3. Show the client the month in 5 lines.

## When it runs

1. The `monthly-review` schedule fires on the first delivery day of each month.
2. If that day's <<OUTPUT_UNIT>> is not delivered yet, wait. Start this workflow right after [[04-agents/workflows/production#After delivery]] ends for that <<OUTPUT_UNIT>>.
3. If no <<OUTPUT_UNIT>> is planned that day (questions paused), start when the schedule fires.
4. Run it at most once per calendar month. If `06-log/session-log.md` already has a `Monthly review` entry dated this month, stop.

## Must read (in this order)

Rows R0 and R10 of the routing table:

1. `00-START-HERE.md` (full)
2. `04-agents/workflows/monthly-review.md` (full)
3. all <<BRAIN_FILE_COUNT>> brain files (full)
4. `06-log/open-questions.md` (full)
5. `06-log/winners.md` (full)
6. `06-log/edits-log.md` (full)

The brain files are every file in `01-brain/` except `README.md`. Step 1 also opens `00-summary.md` and the tickets in the month's <<OUTPUT_UNIT>> folders.

## Step 1 · Gather the month

The month is the last calendar month, from its first day to its last day. Example (fictional): a review on 2026-11-02 covers 2026-10-01 to 2026-10-31.

1. Delivered: count the folders in `05-outputs/` whose `00-summary.md` shows `status: delivered` and a `delivered` date in the month. Count on-demand ones (`kind: on-demand`) separately as well.
2. Pieces produced: in those folders, add up the `## Task` quantity of every ticket whose output file has `status: qa-pass`. Each item the `## Task` line names counts as 1 piece, however many parts it has. Example (fictional): `Write 3 job posts` = 3 pieces.
3. Rules learned: count the E-### entries in `06-log/edits-log.md` with `Client decision: approved` and an `Applied:` date in the month.
4. Winners: count the W-### entries in `06-log/winners.md` dated in the month.
5. Open questions: count every Q-### entry in `06-log/open-questions.md` with `Status: open`, from any month.
6. Stale facts: for each section in the table below, find its last confirmed date. That is the date of the newest `## Changelog` line in the same file that names the section; if no line names it, the file's first approval date (its `v1` changelog line, or `approved_on` when there is no `v1` line). A section is stale when that date is 90 or more days before today.

| File | Sections to check |
|---|---|
| `01-brain/company.md` | What we sell, How we make money, Key facts |
<!-- FILL: one row per brain file that holds facts that change over time, in team.json brain_files order after company.md: the file as a backticked path, then its sections that go stale (prices, offers, people, dates, numbers, lists the client updates), comma-separated. Include plan.md domain sections of that kind; leave out voice.md. Source: team.json brain_files (sections); TEAM-SPEC §12.6 (stale facts) and §20 (brain file sections). Length: 1 to 4 rows, max 5 sections each. Example: kit/The-Almanac/04-agents/workflows/monthly-review.md, Step 1, the offer.md, customer.md, and strategy.md rows. -->

7. For each stale section, pick 1 line to confirm: the first line in it that holds a number, a price, or a name; otherwise its first line.
8. Keep the 5 counts for Step 4.

## Step 2 · Ask

1. Pick up to 3 extra items: open Q-### entries first (oldest first), then stale lines (oldest confirmed date first). Write each extra item in 10 words or fewer.
2. Send ONE message with the template below. Keep it at 80 words or fewer: shorten the extra items first, then send fewer of them; never shorten the questions.
3. Never send a reminder.
4. No answer before the next `routine-send`: skip Step 3, send the Step 4 summary with the current counts, and stop. Do not ask these questions again until next month. Unanswered Q-### entries stay open.

```
Monthly check-in (about 5 minutes, voice note is fine):
1. What changed in your business, offers, or prices?
2. Any new wins or results we can use?
3. What are your customers asking lately?
4. Anything the team should stop doing or saying?
<!-- FILL: 0 or 1 domain question on the fact this team's work depends on most that can change month to month, as the line "5. <question>", max 12 words, plain words, one idea, answerable from memory. Delete this comment when the team needs none. Source: TEAM-SPEC §12.6 (the monthly questions) and §20 (brain file sections); process/03-question-design.md §2 rules. Length: 1 line. Example: kit/The-Almanac/04-agents/workflows/monthly-review.md, Step 2 template, questions 1 to 4 (the form to imitate). -->
{{n}}. {{open question, or: Still true: "{{stale line}}"?}}
{{n}}. {{same, if any}}
{{n}}. {{same, if any}}
Skip any you like.
```

`{{n}}` continues the numbering after the last question.

## Step 3 · Apply

1. Save the answers word for word to `02-sources/routine-answers/{{YYYY-MM-DD}}-monthly-review.md` with frontmatter `type: source`, `kind: routine-answers`, `date: {{YYYY-MM-DD}}`, `permission: public-ok` (`ask` if the answers name a third party). Audio: transcribe it with your platform's transcription. If that fails, ask the client to use their phone's voice-to-text or to type.
2. Turn each answer into proposals:
   - Question 1 (business, offers, prices): write each change as a proposed Before → After for the brain file section that states it: `01-brain/company.md` → `## What we sell` or `## How we make money`, or the section of another brain file that holds it.
   - Question 2 (wins and results): <!-- FILL: where each win or result goes: the bank that holds results (as `03-banks/<file>`), in that bank's entry format with Source `monthly review {{YYYY-MM-DD}}`, and its permission: `public-ok` for the client's own results with no third-party name and no confidential number, `ask` for any third-party name, customer result, or confidential detail; plus any second bank a win told as a story also goes into. When no bank holds results, write: "each result → a proposed addition to [[01-brain/company#Key facts]] when it is a fact about the business; otherwise note it in the session log only." Source: team.json banks[]; each bank's Rules; TEAM-SPEC §12.6 and §21 (banks). Length: 2 to 4 sentences. Example: kit/The-Almanac/04-agents/workflows/monthly-review.md, Step 3, item 3 (a P-### in 03-banks/proof.md; a win told as a story also becomes an S-###). -->
   - Question 3 (what customers ask): <!-- FILL: where each question the client reports goes: a proposed addition to the domain brain file section that holds what customers ask or say (Before `(new)`, After `"{{their words}}" (close paraphrase, client memory)`), and a new entry in the bank that holds topics for future work, with Source `monthly review {{YYYY-MM-DD}}`. When the team has neither, write: "each question → a new entry in the source bank named in the routine's Bank procedure." Source: team.json brain_files and banks[]; TEAM-SPEC §12.6, §20 (brain file sections), and §21 (banks). Length: 2 to 3 sentences. Example: kit/The-Almanac/04-agents/workflows/monthly-review.md, Step 3, item 4 (customer.md Exact language, plus an I-### in ideas.md). -->
   - Question 4 (stop doing or saying): a word or phrase → a proposed addition to the client's list in [[01-brain/voice#Banned words and phrases]]. A style request (Example (fictional): "less formal") → a proposed rule for `## How we never sound`, written so the QA Agent can test it (a word, a count, a position, or a structure). An action, topic, or kind of work to stop → a proposed addition to [[01-brain/plan#Areas to avoid]], with the client's reason.
   <!-- FILL: when the check-in has a question 5, one more bullet in the same form: "- Question 5 (<topic>): <the brain file section or bank its answers go to, as a proposed Before → After or a new entry>." Delete this comment when there is no question 5. Source: the Step 2 template above; TEAM-SPEC §12.6 (the monthly questions). Length: 1 sentence. Example: the Question 1 bullet above. -->
3. Permission items: each new bank entry with `Permission: ask` becomes 1 approval item: `OK to use publicly? "{{exact wording}}"`.
4. Open questions: for each answered Q-###, set `Status: answered {{YYYY-MM-DD}}` and turn the answer into a proposed change to the brain file named in the entry's heading. "Don't know" or "skip": leave it open.
5. Stale lines: "still true" → add a line at the top of that file's `## Changelog`: `- v{{current version}} · {{YYYY-MM-DD}} · Confirmed {{section}} unchanged (monthly review {{YYYY-MM}})`. The `version` stays the same because the section did not change; the client's "still true" is the approval. "Changed" → a proposed Before → After.
6. Send 1 approval message with every proposed change and every permission item, following [[04-agents/workflows/learning-loop#Approval batching]]: max 5 items; the rest wait for the next batch.
7. Apply each "yes" with [[04-agents/workflows/learning-loop#Brain change procedure]]. A "yes" to a permission item sets `Permission: public-ok` in that entry (and `Verified by client: yes` when the entry has that line). A "no" changes nothing, except that a "no" to a permission item sets `Permission: private`.

## Step 4 · Month summary

1. Count the open questions again after Step 3, item 4.
2. Send the summary in the same session as the Step 3 approval message (or, with no answers, as Step 2, item 4 says).

   ```
   Your {{month name}} in 5 lines:
   1. Delivered: {{n}} <<OUTPUT_UNIT_PLURAL>> ({{n}} on request)
   2. Pieces produced: {{n}}
   3. Rules learned from your edits: {{n}}
   4. Winners logged: {{n}}
   5. Open questions left: {{n}}
   ```

3. Log the session at the top of `06-log/session-log.md`:

   ```
   ## {{YYYY-MM-DD HH:MM}} · Monthly review
   - Did:
     - Monthly review for {{YYYY-MM}}: {{n}} answers processed, {{n}} changes proposed
   - Changed: {{files created or changed | nothing}}
   - State: Monthly review {{YYYY-MM}} done
   - Next: next monthly review on {{first delivery day of next month}}
   - Waiting on client: {{approval of items 1–5 | nothing}}
   ```

## Checklist

1. The review ran once this calendar month, after that day's <<OUTPUT_UNIT>>.
2. The 5 counts come from the files named in Step 1.
3. The client got 1 message with the 4 questions (plus question 5, when the template has one) and at most 3 extra items, 80 words or fewer, and no reminder.
4. The answers are saved word for word in `02-sources/routine-answers/`.
5. Every brain change went through the Brain change procedure with the client's yes.
6. Every new win or result is filed as Step 3 says, with its permission set by the defaults, and every `ask` entry was in the approval message.
7. Every answered Q-### shows `Status: answered {{date}}`.
8. The 5-line summary went out.
9. The session-log entry exists.
