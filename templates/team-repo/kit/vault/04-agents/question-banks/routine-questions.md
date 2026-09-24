---
type: question-bank
name: routine-questions
kit_version: <<KIT_VERSION>>
---

# Question bank: the <<ROUTINE_NAME>>

The question templates for Part 1 of [[04-agents/workflows/routine]]. Every cycle, the <<LEAD_NAME>> (<<LEAD_SHORT>>) picks 5 templates, fills them with the client's own words, and sends them in one message. Only the <<LEAD_SHORT>> uses this file.

## How to pick this cycle's questions
<!-- Run these rules in order. Every rule must hold for the final 5. -->
1. Read the files in routing row R3 first (listed in [[04-agents/workflows/routine]] → Must read).
2. Build the eligible list: every template in this file, minus every template whose ID appears in `06-log/questions-asked.md` with a date in the last 56 days (8 weeks) before today. The ID is the tag in parentheses at the end of each logged question. Example (fictional): `(RQ-WIN-03)`.
3. Pick 5 eligible templates from at least 3 different categories. Max 2 from one category.
4. Tag each question with 1 area from <!-- FILL: the list of areas the team's work rotates through, as a link to its brain section (for example a focus-area section in a domain brain file, or a section appended to 01-brain/plan.md); when the team has no such list, write "the rows of [[01-brain/plan#Outputs and quantities]] marked Active = yes" (the outputs the answers feed). Source: team.json brain_files (sections); TEAM-SPEC §12.3 (the routine design). Length: 1 line. Example: kit/The-Almanac/04-agents/question-banks/ritual-questions.md, "How to pick this week's 5", rule 5 (content pillars). -->: the area you put into `{{area}}`, or, if the template has no `{{area}}`, the area its topic fits best. The 5 questions must cover at least 2 different areas.
5. Tie-break when more templates fit than you need: pick the category whose newest row in `06-log/questions-asked.md` is oldest (categories never asked come first). Inside a category, pick the template asked longest ago; never-asked templates come first, then the lowest number.
6. Order the 5 in the message: <!-- FILL: the order rule, by category, that makes the message easy to answer: for example the category that feeds a required brain section first, questions about a recent event before opinions, and method questions last. Source: the categories below; TEAM-SPEC §12.3 (the routine design). Length: 1-2 sentences. Example: kit/The-Almanac/04-agents/question-banks/ritual-questions.md, "How to pick this week's 5", rule 9. -->
<!-- FILL: 0-3 team pick rules, numbered from 7, for example: a category that must appear at least every 2nd cycle because it feeds a brain section (and which section); at least 1 question from a group of categories (for example 1 story category and 1 opinion category, naming them); max 1 question built from a bank entry with Status: new (name the bank) when that entry fits an area the other questions do not cover (How to personalize, rule 8). Write nothing when the team needs none. Source: TEAM-SPEC §12.3 (the routine design); team.json banks. Length: 1-3 lines each. Example: kit/The-Almanac/04-agents/question-banks/ritual-questions.md, "How to pick this week's 5", rules 4, 6, and 7. -->

Before sending, check the 5 against every rule in this section and in How to personalize. Replace any question that fails.

## How to personalize
<!-- Every sent question must read like it was written for this client this cycle. -->
1. Replace each placeholder with the client's own words:
   - `{{area}}` = one area from the list in pick rule 4, in the client's words.
   - `{{industry}}` = the client's own field, from the company TL;DR read at session start. Example (fictional): "bookkeeping".
   - `{{customer}}` = what the client calls the people they serve, from `01-brain/company.md` → Who we serve. Example (fictional): "practice owner".
   <!-- FILL: 0-4 more placeholder lines that the templates below use, each "- `{{name}}` = what it stands for, from <brain file> → <section>. Example (fictional): "<value>"." Write nothing when the templates use only the 3 placeholders above. Source: the templates written below; team.json brain_files. Length: one line each. Example: kit/The-Almanac/04-agents/question-banks/ritual-questions.md, "How to personalize", rule 1. -->
2. After filling, fix only grammar: singular or plural, "a" or "an", capital letters. You may change max 5 other words so the question reads naturally. Never change its intent or its category.
3. Every question must be timely: it contains "this week", "this month", "lately", "right now", or "this year". Every template below already does; keep it when you edit.
4. Every question must be specific: it points at one person type, one moment, or one topic. Never "anything", "in general", or "any thoughts".
5. Max 30 words per question after filling.
6. Never 2 questions in one: max 1 question mark per question. A second sentence may only be an instruction. Example (fictional): "Their words, not yours."
7. Never a yes/no question: never start a question with Do, Did, Is, Are, Have, Has, Can, Could, Would, Will, or Should.
8. Bank-based question (only when a pick rule allows one): take any eligible template, replace its topic with the words of the bank entry, and keep the category's intent. Log it with both IDs. Example (fictional): `(RQ-HOW-04 · I-014)`.
9. Never put a client's customer name, a third-party name, or a confidential number in a question.
10. Log each question in `06-log/questions-asked.md` exactly as sent, followed by its ID tag in parentheses (see [[04-agents/workflows/routine]] → Part 1).

Each category below has: `Log as` (the exact value for the Category column of `06-log/questions-asked.md`), `Feeds` (the banks and brain sections its answers usually fill, with the entry Type to use when a bank has one), Purpose, Best for (the outputs and areas it serves), the question templates, and what a good answer contains.

<!-- FILL: 8-15 category sections, one per kind of recurring input this team needs from the client each cycle, derived from the TEAM-BRIEF → 4 Inputs and TEAM-SPEC §12.3 (the routine design) and written with process/03-question-design.md. Each section is headed "## Category: <Name>" and holds, in this order: a guidance comment (what the category asks for, 1 line); "- Log as: `<kebab-case value>`"; "- Feeds: <bank or brain section, with the entry Type>"; "- Purpose: <what the answers are for>"; "- Best for: <outputs and areas>"; "- Question templates:" followed by 4-8 lines "  - RQ-<3 capital letters>-<01, 02, ...> · "<question>"" using only the placeholders in How to personalize, with at least half of each category's templates asking for a specific recent event (stories beat opinions, opinions beat facts); "- What a good answer contains: <the 3-5 parts of a strong answer>". Every template passes How to personalize rules 3-7 as written (a timely phrase, specific, max 30 words when filled, 1 question mark, not yes/no) and the quality check in process/03-question-design.md (one idea; plain words; not leading; not a duplicate; answerable in 1-5 minutes by talking, without looking anything up). The 3-letter codes are unique; no 2 templates in the file ask for the same thing. Source: TEAM-BRIEF → 4 Inputs; TEAM-SPEC §12.3 (the routine design); team.json banks and brain_files. Length: 8-15 categories, 4-8 templates each. Example: kit/The-Almanac/04-agents/question-banks/ritual-questions.md, "Category: Contrarian" to "Category: Values and origin". -->

## Answer instructions
<!-- Append this block, word for word, after the 5 questions in every message of the <<ROUTINE_NAME>>. -->
```
How to answer:
- Talk, don't write: a voice memo is best, text works too. Say the question number first.
- 1-5 minutes per question. Rambling is fine.
- Stories beat opinions. Opinions beat facts.
<!-- FILL: 0-2 more tip lines, each "- <tip, max 10 words>", for the answer tips in TEAM-SPEC §12.3 that this block does not already say. Write nothing when there are none. Source: TEAM-SPEC §12.3 (the routine design, "Answer tips"). Length: 0-2 lines. Example: the line "- Stories beat opinions. Opinions beat facts." above. -->
- Answer in any order, all at once or over the day.
- Say "skip" to skip one.
```

## Examples (fictional)
<!-- Complete messages for fictional clients. They show the picking rules and the personalization. Never send these as written. -->

<!-- FILL: 2 complete example messages for 2 fictional clients of the kind this team serves (different industries), each with: 1 line naming the client, every placeholder value, the areas, the delivery day, and which pick rules apply this cycle; a fenced block with the whole message exactly as the routine message template in 04-agents/workflows/routine.md builds it (greeting line, 5 numbered questions, the Answer instructions block word for word, and the closing line); then "Picked (logged in `06-log/questions-asked.md`, never sent to the client):" with 5 numbered lines "<template ID> · <Log as value> · area: <area>"; then "Rule check:" in 1 line counting categories, areas, bank-based questions, and the team pick rules. No real people or companies, no em dashes. Source: the categories and rules above; 04-agents/workflows/routine.md (message template). Length: 20-30 lines per example. Example: kit/The-Almanac/04-agents/question-banks/ritual-questions.md, "Examples (fictional)". -->
