---
type: question-bank
name: setup-interview
kit_version: <<KIT_VERSION>>
---

# Setup interview question bank

The exact questions for Stage 3 of [[04-agents/workflows/setup]]. The workflow says when to ask; this file says what to ask, in what order, and where each answer goes. Only the <<LEAD_NAME>> (<<LEAD_SHORT>>) uses this file.

## How to use this bank
<!-- Rules for every question in this file. Read all of them before the first question. -->
1. Ask the sections in the order they appear in this file: Section · Company → every domain section after it → Section · Voice (starts with the 60-second voice memo and runs the this-or-that calibration after VO-7) → Section · Plan, always last, because it proposes outputs, rhythm, and authority from everything learned before. The pushback round closes the section it sits in.
2. Send one question per message. Never put 2 questions in one message.
3. Start every question message with the progress label `{{Section}} · {{n}}/{{N}}`, then the question. Example (fictional): `Company · 3/6 · What do you believe about your work so strongly…`
   - Section = the name after "Section · " in the section's heading.
   - N = the core steps written in that section (its pushback round included, if it holds one) minus the ones you will skip, counted when the section starts.
   - n = the position of this question among the N. If a skip is found mid-section, lower N by 1 from the next message on.
4. Ask core questions in the order written. Before each one, check its "Skip if" line. If a drop or an earlier answer already answers it, do not ask it: confirm it in one line instead. Example (fictional): "From your website: you sell {{what}}. Right? (yes / fix)". Put max 3 confirmation lines in one message. Confirmation messages carry no progress label and are not counted in N.
5. Fill every `{{placeholder}}` in an Ask line with the client's own words from earlier answers: `{{industry}}` = their field, from CO-1; `{{city}}` = the city from CO-6; `{{delivery_day}}` and `{{routine_day}}` = as Section · Plan defines them; a domain section defines its own placeholders in its rules. If the value is still unknown, use the plain phrase instead ("your industry", "your city"). Never send a message that contains `{{` or `}}`.
6. Follow-up rule: an answer is vague when it does not meet the question's "Complete when" line, has only adjectives, says "it depends", says "everyone" or "anyone", or has no example. Send 1 follow-up asking for an example, a number, or exact words. Use the question's own "If vague, follow up" line first, then the reusable prompts in rule 7. Max 2 follow-ups per question. After 2 follow-ups, save what you have and move on.
7. Reusable follow-up prompts (use them word for word):
   - F1: "Can you give me one real example? The last time it happened."
   - F2: "What did they actually say? Rough words are fine."
   - F3: "Roughly how many or how much? A range is fine."
   - F4: "Describe one real person. No name needed."
   - F5: "What happened next?"
   - F6: "If you had to pick just one, which would it be?"
8. A core answer is thin when, after 2 follow-ups, it still does not meet its "Complete when" line, or has no example, no number, and no exact words. When a core answer is thin, ask the deep questions whose "Skip if" line names that core question (max 2 per thin answer) before the next core question.
9. Deep questions: after the last core step of a section, and only if the section is still inside its time budget (rule 14), send once: "Want to go deeper here? a) yes b) no". On "a", ask up to 4 deep questions from that section's group in the Deep-dive bank, in order. Label them `{{Section}} · extra {{n}}/{{M}}` (M = the deep questions you will ask, max 4). On "b", go to Stage 4 of [[04-agents/workflows/setup]].
10. "skip", "don't know", "not sure", or "pass" → log one `Q-###` in `06-log/open-questions.md` (format in rule 18), write `UNKNOWN (Q-###)` in the brain section the question fills, and ask the next question. Never ask the same question twice in setup.
11. Save every answer verbatim to `02-sources/interview/{{date}}-setup-interview.md` the moment it arrives. `{{date}}` = the day setup started; keep using the same file if setup runs over several days. Format:
    ```
    ### {{question ID}} · {{question as sent}}
    {{answer, verbatim}}
    Follow-up: {{follow-up as sent}}
    {{answer, verbatim}}
    ```
    Skipped: write `Skipped → Q-###` under the heading. Answered by a drop: write `Answered by drop: [[02-sources/{{folder}}/{{file name without .md}}]]` and `Confirmed: yes` (or the client's fix, verbatim).
12. Accept voice notes, typos, and rambling. Never ask the client to reformat or to type instead. Transcribe voice notes with your platform's transcription. If transcription fails, send: "I can't play voice notes right now. Could you use your phone's voice-to-text, or type it? Rough is fine."
13. One long voice note can answer several questions. Extract each answer, save each under its own question heading, confirm what you took in one message (max 3 lines), and skip those questions.
14. Time budget per section: Company 6 minutes, Voice 12 minutes, Plan 10 minutes, and each domain section the minutes in its guidance comment. Note the time when each section starts. When a section reaches its budget, finish its core steps but offer no deep questions for it. When the interview reaches 60 minutes in total, send once: "We're at 60 minutes. Keep going or pause? a) keep going b) pause".
15. Every client message follows the house style: max 80 words, plain words, lettered options where they fit. Only these may run longer, because each one is a brain-file review: the calibration rounds (VO-8, VO-9), the voice rules message (VO-10, max 130 words), the Plan proposals (PL-3 and PL-7, max 130 words each), and the file reviews in Stage 4 of [[04-agents/workflows/setup]]. Never say "brain file", "frontmatter", "routing table", "sub-agent", "ticket", or "receipt" to the client; say "your company file", "<<VAULT_NAME>>", "your team".
16. Never answer for the client and never suggest an answer, except in lettered options, in the one-line confirmations of rule 4, and in propose-then-confirm messages (rule 19: VO-10, PL-3, PL-7, and every question marked propose-then-confirm).
17. Exact words: when an answer quotes someone else (a customer, a prospect, a colleague), save the quote word for word in the section the question fills, with a label: `verbatim` (copied from a transcript, review, email, or message the client dropped; add the source file) or `close paraphrase (client memory)` (the client recalled the words in this interview). Never tidy, shorten, or correct a quote; keep slang, grammar, and swearing. Never write a third party's name in a brain file: write the role. Example (fictional): "a practice owner".
18. Open question format for `06-log/open-questions.md` (new entries at the top; take the ID from `next_id`, then increase `next_id` by 1):
    ```
    ### Q-{{###}} · {{brain file}} · {{YYYY-MM-DD}}
    - Question: {{question as sent, with its ID, e.g. "CO-5 · …"}}
    - Why it matters: {{one sentence: what the team's work needs this for}}
    - Status: open
    ```
19. Propose-then-confirm: for anything the client should not have to invent (categories, the output mix, the authority table, focus areas), draft the proposal yourself from earlier answers and the kit defaults, send it as one lettered list, and apply the client's picks, drops, renames, and changes. If fewer items remain than the section needs, propose replacements once, in one message. Never ask the client to write the list from scratch.
20. Pushback round (PB-1 to PB-5): 5 questions asked in character as the toughest person the client's work has to convince, about the riskiest area of the domain. Each question tests one of value, risk, proof, difference, and fit. Example (fictional): a doubtful buyer, a wary new hire, or a strict inspector.
    1. Start the PB-1 message with this line, then the question: "Now I'll push back like {{the skeptic the round names}}. Short answers are fine."
    2. Ask PB-1 to PB-5 in order, one per message, as the last 5 core steps of the section that holds the round.
    3. Stay in character for all 5: ask as that person would, with no explanation and no softening. Never argue with an answer. The follow-up rule still applies.
    4. After PB-5, add one line at the top of your next message: "Done pushing back. That helps a lot."
    5. Save each answer in the section its Fills line names, in the format shown there. If it shows none, write `- Q: "{{question as asked}}"` then `  A: "{{the client's answer, their words, max 60 words}}"`.
    6. Every hedge in an answer ("it depends", "most", "usually", "results vary", "if they do their part") becomes a line that bans the absolute version, under the heading ending in "to avoid" that the Fills line names. Example (fictional): the client says "most clients hear back within 2 days" → "Never say every client hears back within 2 days."
    7. Every new result, client, or number in an answer becomes a bank entry with `Permission: ask` (and unverified, when the bank's Rules have a verification field) until the client confirms it (rule 21).
21. Bank entries found in answers: file them at Stage 4 of each section, in the bank whose README says it holds that kind of material, in that bank's entry format, with the permission defaults in the Drafting rules of [[04-agents/workflows/setup]]. A number or result is usable only after the client confirms it. Numbers the client is unsure of ("about", "I think") → log a `Q-###` and keep them out of every brain file.

Question format used below: `Ask` = the exact message text after the progress label (max 30 words, not counting a list the question inserts). `Fills` = where the answer goes. `Complete when` = what a usable answer contains. `If vague, follow up` = the first follow-up to use. `Skip if` = when not to ask. `Options` = lettered choices, sent on the lines after the question. IDs: a 2-letter prefix per section (CO Company, VO Voice, PL Plan, PB the pushback round, and each domain section's own prefix); core questions are numbered 1 to 20 and deep questions 21 and up, so an added question never takes an existing ID.

## Section · Company
<!-- 6 core questions, about 6 minutes. Fills 01-brain/company.md. Short answers are fine here. -->
Section intro line (first line of the CO-1 message): see Stage 3 in [[04-agents/workflows/setup]].

### CO-1 · core
- Ask: "In 2 sentences, like you'd say it to a friend: what do you sell, and who buys it?"
- Fills: `01-brain/company.md` → What we sell, Who we serve
- Complete when: one line on what they sell and one on who buys it, in their words.
- If vague, follow up: "Who bought from you most recently? Describe them in one line, no name needed."
- Skip if: a drop states both what they sell and who buys it (confirm in one line).

### CO-2 · core
- Ask: "How does money come in right now?"
- Fills: `01-brain/company.md` → How we make money
- Complete when: every way money comes in, with a rough share when they track it.
- If vague, follow up: "Roughly what share comes from each? A guess is fine, like 70/30."
- Skip if: a drop lists every product or service with its price and how it is sold (confirm in one line).
- Options (only if useful): a) one-to-one work b) group work or programs c) products d) retainers or subscriptions e) a mix (tell me the rough split)

### CO-3 · core
- Ask: "What do you believe about your work so strongly that you'd turn down a client over it?"
- Fills: `01-brain/company.md` → What we believe
- Complete when: one belief, the reason behind it, and one real moment it mattered.
- If vague, follow up: "When did that belief last cost you a client, or win you one? What happened?"
- Skip if: never.

### CO-4 · core
- Ask: "What are you against in {{industry}}? The common practice that makes you roll your eyes."
- Fills: `01-brain/company.md` → What we believe
- Complete when: one practice they reject and why it hurts their clients.
- If vague, follow up: "Give me one real example you saw lately. What happened?"
- Skip if: never.

### CO-5 · core
- Ask: "Why do clients pick you over their other options? If a client ever told you why, use their words."
- Fills: `01-brain/company.md` → What makes us different
- Complete when: 1-3 reasons, at least one in a client's own words.
- If vague, follow up: "What did your last happy client say when they signed? Rough words are fine."
- Skip if: never. What makes the business different must come from the client, not from a drop.

### CO-6 · core
- Ask: "Three quick facts: your business name exactly as you spell it, the name I should use for you, and the city you work from."
- Fills: `01-brain/company.md` → Key facts; `01-brain/plan.md` → Rhythm (time zone, from the city)
- Complete when: the exact business name, the name to use for them, and a city.
- If vague, follow up: "Which name do people use for you: first name, full name, or a nickname?"
- Skip if: drops give all 3 facts (confirm in one line). If drops give 1 or 2, ask only for the missing ones.

<!-- FILL: core questions for any domain sections appended to company.md in team.json (its sections after "Key facts"), IDs CO-7 and up, each as "### CO-<n> · core" with the fields Ask, Fills, Complete when, If vague, follow up, Skip if, and Options only when useful. Write nothing when company.md has only its core sections. Source: team.json brain_files (company.md sections); TEAM-SPEC §20 (brain file sections). Length: 1-2 questions per appended section. Example: CO-1 to CO-6 above. -->

<!-- FILL: one section per domain brain file (team.json brain_files with core: false), in team.json order, written with process/03-question-design.md. Each section is headed "## Section · <File title>" and holds, in this order:
(1) a guidance comment: "<n> core questions, about <minutes> minutes. Fills 01-brain/<file>." (about 1.5 minutes per core question);
(2) the line "Section intro line (first line of the <first ID> message): see Stage 3 in [[04-agents/workflows/setup]].";
(3) "Rules for this section:" (numbered, only when needed): the placeholders the section defines, how quoted words are labeled (How to use rule 17), and what to ask when the client has no data yet (never invent it);
(4) the core questions, IDs <XX>-1 and up with a 2-letter prefix unique in this file (never CO, VO, PL, or PB), each as "### <ID> · core" with the fields Ask (max 30 words), Fills (file → section), Complete when, If vague, follow up, Skip if, and Options only when useful, ordered from easy to hard inside the section; add "· propose-then-confirm" to the heading of a question that proposes a list (How to use rule 19) and give its message template;
(5) in the section that covers the riskiest area of the domain, after its core questions: a "### Pushback round" block with a guidance comment naming the skeptic, then PB-1 to PB-5, each as "### PB-<n> · core" testing one of value, risk, proof, difference, and fit (adapted to the domain), with Ask, a Fills line naming that file's question-and-answer section and its section whose heading ends in "to avoid", Complete when, If vague, follow up, and "Skip if: never."
With no domain brain file, write only the pushback round, right here at the end of Section · Company, with Fills lines naming 01-brain/company.md → What makes us different and 01-brain/plan.md → Areas to avoid.
Techniques: exact words from memory; the last time it happened (a recent, specific event); propose-then-confirm for anything the client should not invent. Every question passes the quality check in process/03-question-design.md: fills a named section; answerable in under 2 minutes without looking anything up; one idea; plain words; not leading; not a duplicate; has an example when abstract.
Size: the whole interview has 30-45 core questions. This file fixes 25 (Company 6, Voice 10, Plan 9), the pushback round adds 5, and questions for sections appended to core files count too, so write 0-10 domain core questions in total, at least 2 per domain brain file, and give every domain section at least 1 question or a drafting rule in the Coverage map.
Source: TEAM-SPEC §20 (each file's sections and what they hold); team.json brain_files; TEAM-BRIEF → 6 Knowledge, 10 Quality bar, and 11 Constraints. Length: 3-15 questions per section, pushback round included. Example: kit/The-Almanac/04-agents/question-banks/setup-interview.md, "Section B · Customer" (exact words from memory) and "Section C · Offer" with its "Skeptical-buyer round" (the pushback round). -->

## Section · Voice
<!-- 1 voice memo + 6 core questions + 3 calibration steps, about 12 minutes. Fills 01-brain/voice.md. -->
Section intro line (first line of the VO-1 message): see Stage 3 in [[04-agents/workflows/setup]].

Order: VO-1 (the memo) first, then VO-2 to VO-7, then the calibration (VO-8, VO-9, VO-10).

### 60-second voice memo
<!-- Captures how the client really talks before any question can shape it. Source for Spoken voice and Phrases we use. -->
1. Ask VO-1 as the first question of Section · Voice, word for word.
2. If the client says they can't or won't record, send the typed fallback: "No problem. Type 5 sentences exactly the way you'd say them out loud." Never ask for the recording again.
3. Transcribe the memo with your platform's transcription. If transcription fails, use How to use rule 12.
4. Save the transcript verbatim to `02-sources/interview/{{date}}-voice-memo-60s.md` with this frontmatter: `type: source`, `kind: interview`, `date: {{YYYY-MM-DD}}`, `permission: public-ok`. Under the VO-1 heading in the interview file, write `Saved to [[02-sources/interview/{{date}}-voice-memo-60s]]`.
5. If the transcript is under 80 words, send 1 follow-up: "Thanks. Can you send 30 more seconds about the last client you helped?"
6. Extract these 6 things from the transcript (or the typed fallback) and write them into `01-brain/voice.md` at Stage 4:
   - Repeated phrases: every group of 2-5 words the client used 2 or more times (ignore groups like "and the", "of the") → Phrases we use.
   - Sentence rhythm: average words per sentence, labeled short (under 10), medium (10-20), or long (over 20) → Spoken voice.
   - How they open: their first 10 words, verbatim → Spoken voice.
   - Filler words they really use, each with its count (Example (fictional): "honestly 3 times, look 2 times") → Spoken voice. Spoken text the team writes never contains "um", "uh", or "er".
   - Energy: calm, steady, or high, plus the one sentence that shows it → Spoken voice.
   - 3 samples: 3 verbatim excerpts of 1-3 sentences each → Spoken voice.

### VO-1 · core
- Ask: "Record 60 seconds explaining what you do and who you help, like you're telling a friend."
- Fills: `01-brain/voice.md` → Spoken voice, Phrases we use; the memo transcript file (step 4 above)
- Complete when: a recording or typed text of at least 80 words.
- If vague, follow up: "Thanks. Can you send 30 more seconds about the last client you helped?"
- Skip if: never. If the client refuses, use the typed fallback (step 2 above).

### VO-2 · core
- Ask: "What phrases do you say a lot? The ones your clients or team would tease you about."
- Fills: `01-brain/voice.md` → Phrases we use
- Complete when: 1-5 phrases, word for word.
- If vague, follow up: "What do you say when a client finally gets something right?"
- Skip if: never.

### VO-3 · core
- Ask: "Which words or phrases make you cringe when you see them in writing?"
- Fills: `01-brain/voice.md` → Banned words and phrases (added to the default list, never replacing it)
- Complete when: at least 1 word or phrase, or "none".
- If vague, follow up: "What's a word you'd never use to describe your own work?"
- Skip if: never.

### VO-4 · core
- Ask: "Fill in the blanks: 'I want to sound ___, never ___.'"
- Fills: `01-brain/voice.md` → How we sound, How we never sound
- Complete when: both blanks filled, plus one sentence that sounds like them or one that doesn't.
- If vague, follow up: "Give me one sentence that sounds like you, and one that doesn't."
- Skip if: never.

### VO-5 · core
- Ask: "How much swearing is OK in the work we write for you?"
- Fills: `01-brain/voice.md` → How we sound (one rule: none, mild, or strong), Formatting habits (profanity)
- Complete when: a, b, or c.
- If vague, follow up: "Pick the closest one: a, b, or c."
- Skip if: never.
- Options (only if useful): a) none b) mild c) strong

### VO-6 · core
- Ask: "How many emojis do you like in the work we write for you?"
- Fills: `01-brain/voice.md` → Formatting habits
- Complete when: a, b, or c.
- If vague, follow up: "Pick the closest one: a, b, or c."
- Skip if: the client's own dropped writing shows a clear pattern. Confirm in one line: "Your writing uses {{no / a few / lots of}} emojis. Keep that? (yes / fix)".
- Options (only if useful): a) none b) a few c) lots

### VO-7 · core
- Ask: "Name 1 to 3 people or businesses whose style you like. What exactly do you like about each one?"
- Fills: `01-brain/voice.md` → How we sound (traits only; Example (fictional): "opens with a story", "sentences under 10 words"). Never write their names in `01-brain/voice.md`. Never imitate them; use only the traits.
- Complete when: at least 1 concrete trait per name, or "none".
- If vague, follow up: "What do they do in the first 5 seconds that keeps your attention?"
- Skip if: never. If the answer is "none", write nothing and move on.

### This-or-that calibration
<!-- The client reacts to drafts instead of describing their voice. Every reaction becomes a testable rule. -->
1. Pick 1 topic from the client's answers, in this order: CO-4, then CO-3, then CO-5. Take the first one whose answer contains a real moment, a number, or a quote; if none does, take CO-4.
2. Write 3 versions of one short piece that make the same point, each 60-90 words, in this form: <!-- FILL: the kind of short text this team's work is most often read as, in plain words (for example "a short email to a customer", "the opening of a job post", "a short update to the team"). Source: TEAM-SPEC §15 (output specs); team.json specialists (the first specialist's job). Length: max 8 words. Example: kit/The-Almanac/04-agents/question-banks/setup-interview.md, "This-or-that calibration", step 2 ("one post"). -->.
   - A · short and blunt: every sentence max 12 words; the opinion in sentence 1; no story; no list.
   - B · story-led and warm: opens with one specific moment (a person plus a time or place); the point arrives in the last 2 sentences; speaks to the reader as "you".
   - C · punchy and structured: a 1-line opener, then 3-5 short lines or a list, then a 1-line takeaway.
3. All 3 versions: use only facts the client gave; no number or result they did not state; 1-2 of their own phrases (from VO-1 or VO-2); zero words from VO-3 or from the default anti-AI list in `01-brain/voice.md`; follow VO-5 and VO-6; no link and no request for the reader to act.
4. Send VO-8 as one message (template below). This message may exceed 80 words; the text outside the 3 versions must be max 30 words.
5. Round 2 (VO-9): write 2 variants of the winner. Choose the difference from the client's round-1 comment:
   - Comment about length → a) 40-60 words b) 90-120 words.
   - Comment about tone (formal, casual, soft, harsh, salesy) → a) more of that quality b) less of it, both 60-90 words.
   - No comment, or any other comment → a) 40-60 words b) 90-120 words.
   Apply every round-1 fix to both variants.
6. Turn every client comment from both rounds into a testable voice rule: a reviewer can point at a line and say pass or fail. Adjectives alone are not rules. Example (fictional):

   | Client comment | Testable voice rule |
   |---|---|
   | "Too salesy." | Max 1 request to act per piece; never use urgency words ("now", "hurry", "last chance"). |
   | "I'd never say 'folks'." | Add "folks" to Banned words and phrases. |
   | "Too long-winded." | Sentences max 15 words. |
   | "B, but it takes too long to get going." | Open with the point or the moment in line 1; never open with a warm-up line. |
   | "I like the list in C." | Use a list of 3-5 items when a piece explains steps. |

7. For each rejected version, write 1 "How we never sound" candidate: the feature the client criticized, or, if they gave no reason, that version's defining feature from step 2 (A: short sentences with no story; B: opening with a story; C: a list structure). Example (fictional): "Never open with a list."
8. Send VO-10: 5-8 rules, each max 12 words, built in this order: calibration comments first, then VO-4, VO-5, VO-6, the VO-7 traits, then the memo's rhythm. This message counts as a voice file review: it may exceed 80 words, max 130 words.
9. On "ok" (or after the client's fixes are applied): rules starting with "Never" go to `## How we never sound`; all others go to `## How we sound`. The winning round-2 variant, with every fix applied, goes to `## Good examples` labeled "Calibration winner, approved in setup {{date}}", and into `## Written voice` as a sample. The other versions go to `## Bad examples` with the client's reason, verbatim, or "not picked".
10. Save every version sent and every reply verbatim in the interview file under VO-8, VO-9, and VO-10.

Round 1 message (VO-8):
```
Voice · {{n}}/{{N}} · Same point, written 3 ways.

A)
{{version A, 60-90 words}}

B)
{{version B, 60-90 words}}

C)
{{version C, 60-90 words}}

Which sounds most like you, and what's off in it? (reply a / b / c + anything)
```

Round 2 message (VO-9):
```
Voice · {{n}}/{{N}} · Two takes on {{winning letter}}, with your fixes.

a)
{{variant a}}

b)
{{variant b}}

Which is closer? (reply a / b + anything)
```

Rules message (VO-10):
```
Voice · {{n}}/{{N}} · Here's how I'll write for you:
1. {{rule, max 12 words}}
2. {{rule}}
3. {{rule}}
4. {{rule}}
5. {{rule}}
Reply ok, or tell me what to change.
```

### VO-8 · core
- Ask: "Same point, written 3 ways. Which sounds most like you, and what's off in it? (reply a / b / c + anything)"
- Fills: `01-brain/voice.md` → How we sound, How we never sound, Written voice, Bad examples
- Complete when: a letter, plus what is off in it, or "nothing".
- If vague, follow up: "What's one line in it you'd never say?"
- Skip if: never.

### VO-9 · core
- Ask: "Two takes on {{winning letter}}, with your fixes. Which is closer? (reply a / b + anything)"
- Fills: `01-brain/voice.md` → How we sound, Formatting habits, Written voice, Good examples, Bad examples
- Complete when: a letter, plus any fix.
- If vague, follow up: "What would you change in it before using it?"
- Skip if: never.

### VO-10 · core · propose-then-confirm
- Ask: "Here's how I'll write for you: {{5-8 numbered rules}}. Reply ok, or tell me what to change."
- Fills: `01-brain/voice.md` → How we sound, How we never sound
- Complete when: "ok", or the number of every rule to change with the change.
- If vague, follow up: "Which rule feels off? Give me the number."
- Skip if: never.

<!-- FILL: core questions for any domain sections appended to voice.md in team.json (its sections after "Rules learned from edits"), IDs VO-11 and up, in the same field format. Write nothing when voice.md has only its core sections. Source: team.json brain_files (voice.md sections); TEAM-SPEC §20 (brain file sections). Length: 1-2 questions per appended section. Example: VO-2 to VO-7 above. -->

## Section · Plan
<!-- 9 core questions, about 10 minutes. Mostly letter answers and 2 proposals. Fills 01-brain/plan.md. Always the last section: it proposes outputs, rhythm, and authority from everything learned before. -->
Section intro line (first line of the PL-1 message): see Stage 3 in [[04-agents/workflows/setup]].

Rules for this section:
1. Before PL-4, turn the CO-6 city into an IANA time zone (Example (fictional): Denver → America/Denver). If the city is unknown, first send, with no label: "What city are you in? I'll set your times to your local clock." If the city has more than 1 time zone, ask: "Which time zone? a) {{zone 1}} b) {{zone 2}}".
2. `{{delivery_day}}` = the day picked in PL-4. `{{routine_day}}` = the day before it. The default question time is 10:00.
3. PL-3 and PL-7 are propose-then-confirm (How to use rule 19). Both start from the kit defaults already written in `01-brain/plan.md`: the rows of `## Outputs and quantities` and the lists in `## Authority`. Never ask the client to list outputs or permissions from scratch.
4. Drafting: Rhythm → Paused until = `no`. Delivery = `chat` unless PL-6 picked b and the Google Doc test in Stage 5 of [[04-agents/workflows/setup]] worked.

### PL-1 · core
- Ask: "What should your team do for you first?"
- Fills: `01-brain/plan.md` → Goal
- Complete when: one goal, in their words.
- If vague, follow up: "If your team did one thing for you in the next 90 days, what would make you happy?"
- Skip if: never.
- Options (only if useful): <!-- FILL: 3-5 lettered goals this kind of client picks most, in the client's words, then "other (tell me)", written "a) ... b) ...". Source: TEAM-BRIEF → 1 Purpose and 3 Outputs; TEAM-SPEC §1 (approved blueprint). Length: max 8 words per option. Example: kit/The-Almanac/04-agents/question-banks/setup-interview.md, ST-01, "Options". -->

### PL-2 · core
- Ask: "How will you know it's working? Name one number or sign you'd check each month."
- Fills: `01-brain/plan.md` → Goal (the measure)
- Complete when: one number or sign they could check each month.
- If vague, follow up: "What would you see in 90 days that tells you this was worth it?"
- Skip if: never.

### PL-3 · core · propose-then-confirm
- Ask: "Here's what your team would make each <<OUTPUT_UNIT>>: {{lettered list}}. Keep it, or change anything?"
- Fills: `01-brain/plan.md` → Outputs and quantities (Active and quantity per <<OUTPUT_UNIT>>)
- Complete when: "keep", or every change to the list.
- If vague, follow up: "Which one matters most to you right now?"
- Skip if: never.

Build the proposal:
1. Take every row of `01-brain/plan.md` → `## Outputs and quantities` with its kit default for Active and for the quantity per <<OUTPUT_UNIT>>.
2. Change a default only when an earlier answer shows the client needs that output or does not. Example (fictional): a client who said "nobody here reads long reports" gets the long-report row switched off. Write each change and the answer behind it in the interview file under PL-3, never in the client message.
3. Send the active rows as lettered lines in plain words, each with its quantity. Outputs that run only on request go on one last line. Max 130 words.
4. Apply the client's picks, drops, and quantity changes: a dropped row gets Active = `no`; a new quantity replaces the default.

Outputs message (PL-3):
```
Plan · {{n}}/{{N}} · Each <<OUTPUT_UNIT>>, your team would make:
a) {{quantity}} {{output in plain words}}
b) {{quantity}} {{output in plain words}}
Only when you ask: {{outputs in plain words | nothing}}
Keep this? (reply "keep", or e.g. "drop b, make a 2")
```

### PL-4 · core
- Ask: "Which day do you want each <<OUTPUT_UNIT>> ready?"
- Fills: `01-brain/plan.md` → Rhythm (delivery day)
- Complete when: one weekday.
- If vague, follow up: "Which day do you usually plan your week?"
- Skip if: never.
- Options (only if useful): a) Mon b) Tue c) Wed d) Thu e) Fri f) Sat g) Sun

### PL-5 · core
- Ask: "Your questions will arrive {{routine_day}} at 10:00, {{city}} time, so your <<OUTPUT_UNIT>> is ready {{delivery_day}}. How often?"
- Fills: `01-brain/plan.md` → Rhythm (cadence: a = `weekly`, b = `every-2-weeks`; question day and time; time zone)
- Complete when: a or b, after any change from c.
- If vague, follow up: "Pick a or b. You can change it anytime."
- Skip if: never. On c, take the new day, time, or city, then send PL-5 again with the new values (this counts as a follow-up).
- Options (only if useful): a) weekly b) every 2 weeks c) change the day, time, or city first

### PL-6 · core
- Ask: "How do you want each <<OUTPUT_UNIT>> delivered?"
- Fills: `01-brain/plan.md` → Delivery (a = `chat`, b = `chat + google-doc`); b is tested in Stage 5 of [[04-agents/workflows/setup]]
- Complete when: a or b.
- If vague, follow up: "Pick a or b. You can switch anytime."
- Skip if: never.
- Options (only if useful): a) here in chat b) chat + Google Doc

### PL-7 · core · propose-then-confirm
- Ask: "Here's what your team may do without asking, only after your yes, and never: {{the 3 lists}}. Keep it, or change anything?"
- Fills: `01-brain/plan.md` → Authority
- Complete when: "keep", or every change to the lists.
- If vague, follow up: "Is there one thing on the list you'd rather do yourself?"
- Skip if: never.

Build the proposal:
1. Take the kit's proposed lists in `01-brain/plan.md` → `## Authority`: Allowed, With approval, and Never.
2. Write each action in plain words, max 12 words, the way the client would say it.
3. The Never line is fixed: spending money, entering passwords or payment details, deleting accounts or data, changing account settings. If the client asks to allow one, reply once: "That one stays off to keep your accounts safe. I'll prepare it and you do it." Keep it in Never.
4. A new action the client wants the team to take goes under With approval, unless it is low-risk and reversible (it costs nothing and can be undone) and the client asks for no check each time: then Allowed.
5. An action the client removes leaves both lists and becomes draft-only again.
6. Everything not listed stays draft-only: the team prepares it, the client does it. The message says so.

Authority message (PL-7):
```
Plan · {{n}}/{{N}} · Here's what your team may do:
Without asking: {{Allowed actions in plain words | nothing yet}}
Only after your yes, each time: {{With approval actions in plain words | nothing yet}}
Never: spend money, enter passwords or payment details, delete accounts or data, or change account settings.
Everything else, I prepare and you do.
Keep this? (reply "keep", or tell me what to change)
```

### PL-8 · core
- Ask: "After I deliver, who uses the work?"
- Fills: `01-brain/plan.md` → Team and handoff
- Complete when: who gets which part and when, or "just me".
- If vague, follow up: "Who gets which part, and when?"
- Skip if: never.
- Options (only if useful): a) just me b) someone on my team (tell me who gets what) c) a mix (tell me who gets what)

### PL-9 · core
- Ask: "Anything your team must never touch? Pick all that fit."
- Fills: `01-brain/plan.md` → Areas to avoid
- Complete when: the picked letters, with any "other" area in their words, or "none".
- If vague, follow up: "Anything that got you in trouble before, or that you'd hate a client to see?"
- Skip if: never.
- Options (only if useful): a) politics b) religion c) naming competitors d) my personal life e) client names or details f) other (tell me) g) none

<!-- FILL: core questions for any domain sections appended to plan.md in team.json (its sections after "Areas to avoid"), IDs PL-10 and up, in the same field format; use propose-then-confirm for any list the client should not invent (for example focus areas). Write nothing when plan.md has only its core sections. Source: team.json brain_files (plan.md sections); TEAM-SPEC §20 (sections appended to plan.md). Length: 1-2 questions per appended section. Example: PL-3 and PL-7 above (proposals); kit/The-Almanac/04-agents/question-banks/setup-interview.md, "Propose content pillars". -->

## Coverage map
<!-- Every brain file section (except TL;DR, Open questions, and Changelog) and what fills it. A section with no answer after setup gets UNKNOWN (Q-###). -->
| Brain file | Section | Filled by (question IDs or a drafting rule) |
|---|---|---|
| `01-brain/company.md` | What we sell | CO-1; drops (website, product or price documents) |
| `01-brain/company.md` | Who we serve | CO-1 |
| `01-brain/company.md` | How we make money | CO-2 |
| `01-brain/company.md` | What we believe | CO-3, CO-4; CO-22, CO-23 (deep) |
| `01-brain/company.md` | What makes us different | CO-5; CO-23, CO-25 (deep); PB-1 to PB-5 when the pushback round closes Section · Company |
| `01-brain/company.md` | Key facts | CO-6 (business name spelling, the name to use for the client, city); CO-21, CO-24 (deep) |
<!-- FILL: one row per section of every domain brain file, in team.json order ("| `01-brain/<file>` | <Section> | <question IDs, or "Drafting rule: ..."> |"), including the pushback round's IDs on the rows it fills, then one row per domain section appended to company.md, voice.md, or plan.md. Every section except TL;DR, Open questions, and Changelog has at least 1 question ID or a drafting rule. Source: team.json brain_files (every section); the domain sections written above. Length: one row per section. Example: kit/The-Almanac/04-agents/question-banks/setup-interview.md, "Coverage map". -->
| `01-brain/voice.md` | How we sound | VO-4, VO-5, VO-7 (traits only), VO-10 (approved rules) |
| `01-brain/voice.md` | How we never sound | VO-4, VO-10; VO-22 (deep). Drafting rule: 1 candidate per rejected calibration version (VO-8, VO-9) |
| `01-brain/voice.md` | Phrases we use | VO-2; VO-1 (repeated phrases from the memo); VO-24, VO-25 (deep) |
| `01-brain/voice.md` | Banned words and phrases | VO-3, added to the default list already in the file |
| `01-brain/voice.md` | Formatting habits | VO-5 (profanity), VO-6 (emojis). Drafting rule: sentence length, list use, and paragraph size of the calibration winner (VO-9); the client's own dropped writing |
| `01-brain/voice.md` | Spoken voice | VO-1 (samples, rhythm, opening, fillers, energy); VO-23 (deep); voice-note answers from the whole interview |
| `01-brain/voice.md` | Written voice | Drafting rule: the calibration winner (VO-9), typed answers, and the client's own dropped writing; VO-21, VO-25 (deep) |
| `01-brain/voice.md` | Good examples | Drafting rule: the calibration winner with fixes applied (VO-9); VO-21 (deep) |
| `01-brain/voice.md` | Bad examples | Drafting rule: the rejected calibration versions with the client's reason (VO-8, VO-9); VO-22 (deep) |
| `01-brain/voice.md` | Rules learned from edits | Drafting rule: `- none` at setup; the learning loop fills it |
| `01-brain/plan.md` | Goal | PL-1, PL-2; PL-21, PL-22 (deep) |
| `01-brain/plan.md` | Outputs and quantities | PL-3 (propose-then-confirm from the kit defaults); PL-22 (deep) |
| `01-brain/plan.md` | Rhythm | PL-4 (delivery day), PL-5 (cadence, question day and time, time zone from the CO-6 city). Drafting rule: Paused until = `no` |
| `01-brain/plan.md` | Delivery | PL-6 (tested in Stage 5 of the setup workflow) |
| `01-brain/plan.md` | Authority | PL-7 (propose-then-confirm from the kit defaults). Drafting rule: the Never line never changes |
| `01-brain/plan.md` | Team and handoff | PL-8; PL-23 (deep) |
| `01-brain/plan.md` | Areas to avoid | PL-9; every hedge from the pushback round when its Fills line names this section |

## Deep-dive bank
<!-- Optional. Asked only when the client opts in ("Want to go deeper here?") or when the core question named in "Skip if" got a thin answer (How to use rules 8 and 9). -->

### Company deep-dive

### CO-21 · deep
- Ask: "Tell me the moment you decided to start. Where were you, and what had just happened?"
- Fills: `01-brain/company.md` → Key facts (origin line, max 2 sentences); the bank that holds stories, if the team has one (How to use rule 21)
- Complete when: one moment with a place or a time, and what had just happened.
- If vague, follow up: "What did you do the next day?"
- Skip if: the client did not opt in.

### CO-22 · deep
- Ask: "What's the biggest mistake you've made in the business so far?"
- Fills: `01-brain/company.md` → What we believe; the bank that holds stories, if the team has one
- Complete when: one mistake and what it cost (money, time, or a client).
- If vague, follow up: "What did it cost you, in money, time, or a client?"
- Skip if: the client did not opt in.

### CO-23 · deep
- Ask: "What do you refuse to do for clients, even if they'd pay you more?"
- Fills: `01-brain/company.md` → What we believe, What makes us different
- Complete when: one thing they refuse and the last time it came up.
- If vague, follow up: "When did someone last ask you to do it? What happened?"
- Skip if: the client did not opt in, unless CO-3 was thin.

### CO-24 · deep
- Ask: "What milestones can I mention? Years in business, clients served, awards, qualifications."
- Fills: `01-brain/company.md` → Key facts; the bank that holds proof, if the team has one (1 entry per milestone)
- Complete when: each milestone with its number or name.
- If vague, follow up: "How many years have you done this work, roughly?"
- Skip if: the client did not opt in.

### CO-25 · deep
- Ask: "What kind of business in {{industry}} would you hate to be confused with?"
- Fills: `01-brain/company.md` → What makes us different
- Complete when: one kind of business and what it does that they never would.
- If vague, follow up: "What do they do that you never would?"
- Skip if: the client did not opt in, unless CO-5 was thin.

<!-- FILL: one group per domain section, in the same order as the domain sections above, each headed "### <File title> deep-dive" and holding 3-8 questions "### <XX>-21 · deep" and up, in the core field format; every Skip if line reads "the client did not opt in." or "the client did not opt in, unless <core ID> was thin." (How to use rule 8). Add 1-2 pushback deep questions (PB-21 and up) to the group of the section that holds the pushback round. The Deep-dive bank has 20-30 questions in total and 13 are fixed here (CO-21 to CO-25, VO-21 to VO-25, PL-21 to PL-23), so write 7-17; with no domain brain file, write them as more Company deep questions (CO-26 and up) right here, with the pushback deep questions last. Source: TEAM-SPEC §20 (brain file sections); TEAM-BRIEF → 6 Knowledge. Length: 7-17 questions. Example: kit/The-Almanac/04-agents/question-banks/setup-interview.md, "Customer deep-dive" and "Offer deep-dive". -->

### Voice deep-dive

### VO-21 · deep
- Ask: "Paste or describe something you wrote that you were proud of: an email, a page, a post."
- Fills: `01-brain/voice.md` → Good examples, Written voice; `02-sources/documents/` (saved as a drop)
- Complete when: the text itself, or a description with at least one line they remember.
- If vague, follow up: "What did people say about it?"
- Skip if: the client did not opt in, or already dropped their own writing in Stage 2.

### VO-22 · deep
- Ask: "What's a sentence you'd never say to a client?"
- Fills: `01-brain/voice.md` → Bad examples, How we never sound
- Complete when: one sentence, word for word.
- If vague, follow up: "What's a line you've heard others say that made you cringe?"
- Skip if: the client did not opt in, unless VO-4 was thin.

### VO-23 · deep
- Ask: "How do you give a client bad news? Say it the way you'd really say it."
- Fills: `01-brain/voice.md` → Spoken voice
- Complete when: 2-4 sentences, said the way they say them.
- If vague, follow up: "What was the last hard thing you had to tell a client?"
- Skip if: the client did not opt in.

### VO-24 · deep
- Ask: "What sayings or comparisons do clients repeat back to you?"
- Fills: `01-brain/voice.md` → Phrases we use
- Complete when: 1-3 sayings or comparisons, word for word.
- If vague, follow up: "How do you usually explain your work to someone new?"
- Skip if: the client did not opt in, unless VO-2 was thin.

### VO-25 · deep
- Ask: "When you write to a client, how do you start and end the message? Your exact words."
- Fills: `01-brain/voice.md` → Written voice, Phrases we use
- Complete when: their usual opening and closing, word for word.
- If vague, follow up: "How did you sign off the last message you sent a client?"
- Skip if: the client did not opt in.

### Plan deep-dive

### PL-21 · deep
- Ask: "Is anything coming up in the next 90 days that your team's work should build toward?"
- Fills: `01-brain/plan.md` → Goal
- Complete when: a date and what happens then, or "nothing".
- If vague, follow up: "What's the date, and what happens then?"
- Skip if: the client did not opt in.

### PL-22 · deep
- Ask: "If your team could take only one job off your plate first, which one would it be?"
- Fills: `01-brain/plan.md` → Goal, Outputs and quantities (which output comes first)
- Complete when: one job.
- If vague, follow up: "If you had to pick just one, which would it be?"
- Skip if: the client did not opt in, unless PL-1 was thin.

### PL-23 · deep
- Ask: "Does anyone else need to see or approve the work before it's used?"
- Fills: `01-brain/plan.md` → Team and handoff
- Complete when: who checks, which part, and when, or "nobody".
- If vague, follow up: "Who was the last person who checked something before it went out?"
- Skip if: the client did not opt in, unless PL-8 was thin.
