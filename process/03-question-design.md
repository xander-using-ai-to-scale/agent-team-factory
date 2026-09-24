# Stage 3 · Question design

The factory never ships prepared questions. Nobody can know in advance what an HR, SEO, or podcast-booking team needs to ask. This file is the **method** for writing the questions for each new team, so every team asks questions as good as the reference kit's.

- **Input:** the approved blueprint, `team.json`, `docs/TEAM-SPEC.md`, and the scaffolded repo.
- **Output:** the FILLs in `04-agents/question-banks/setup-interview.md` and `routine-questions.md`, written and checked.
- **Gate:** every brain-file section is covered by at least one question, and every question passes the checklist in §7.
- **Time:** 20-40 minutes.

The same rules also shape the intake questions you ask the requester in stage 1 (§6).

---

## 1. The kinds of questions

| Kind | Who asks whom | When | Fills | Where it lives |
|---|---|---|---|---|
| Intake questions | Builder → requester | Stage 1 | The Team Brief | Your messages |
| Setup interview | Lead → client | Once, at setup | The brain files | `question-banks/setup-interview.md` |
| Routine questions | Lead → client | Every cycle | The banks and each output unit | `question-banks/routine-questions.md` |
| Monthly review | Lead → client | Monthly | Brain-file updates | `workflows/monthly-review.md` (4 fixed + 0-1 domain question) |
| Deep-dive bank | Lead → client | Only if answers were thin or the client wants more | Brain-file depth | End of `setup-interview.md` |

---

## 2. The rules (every question, every kind)

1. **Real examples and exact words, not opinions.** Ask for the last time something happened and what was actually said. Opinions come out of stories anyway.
2. **One question at a time.** One message, one question, one idea. A progress label on every setup question: `Company · 3/7`.
3. **No homework.** Every answer comes from memory in under 2 minutes. Never ask the client to look something up, count, or prepare. `skip` or "don't know" is always allowed: it logs an open question (Q-###) and moves on.
4. **Propose, then confirm,** whenever the client should not have to invent the answer: categories, output mix, focus areas, the authority table. Show a draft with 3-5 items and ask "Right? What would you change?"
5. **Every question fills a named brain-file section** (or a named bank for routine questions). A question that fills nothing gets cut.
6. **Follow-ups: 2 at most,** and each asks for exactly one of: an example, a number, or the exact words. Never re-ask the same question in new words.
7. **Plain words.** No jargon from the domain unless the client used it first; none from this factory ever.

---

## 3. The techniques

Pick the technique by the kind of information the section needs.

| Technique | Use it for | Pattern | Content kit example | HR example (fictional) |
|---|---|---|---|---|
| Exact words from memory | How customers, candidates, or staff talk | "Think of your last {{event}}. What did they say about {{topic}}, as close to their exact words as you remember?" | Customer · Exact language | "Think of your last exit interview. What did the person say about why they left, word for word if you can?" |
| The last time it happened | Beliefs, processes, standards | "Walk me through the last time {{event}}. What happened first?" | Company · What we believe | "Walk me through the last time you hired someone. What happened first?" |
| Propose, then confirm | Things the client should not invent | "Here's what I'd suggest: {{3-5 items}}. Right? What would you change?" | Strategy · Content pillars | "Here are 4 interview stages I'd suggest for most roles: ... Right? What would you change?" |
| Pushback round | The domain's riskiest area | "Now I'll push back like a {{skeptic}}." Then 5 tough questions, one per message | Offer · Skeptical buyer Q&A | "Now I'll push back like an employment lawyer." Then questions on fairness, consistency, records, pay, and dismissal |
| 60-second voice memo | How the client sounds | "Record 60 seconds explaining {{topic}}, like you're telling a friend." | Voice | "Record 60 seconds explaining what it's like to work at your company, like you're telling a friend." |
| This-or-that calibration | Voice and style choices | Write 3 short versions (A blunt, B warm and story-led, C structured). "Which sounds most like you? What's off?" Then 2 variations of the pick. | Voice | The same, with a short job-post intro as the sample |
| Scale or number | Sizes, frequencies, limits | "Roughly how many {{thing}} per {{period}}? A range is fine." | Strategy · Platforms and quantities | "Roughly how many people do you hire per quarter? A range is fine." |

Every technique keeps rule 3: the answer comes from memory.

---

## 4. Method: the setup interview

Work in `kit/<vault_folder>/04-agents/question-banks/setup-interview.md`. The template already holds the universal mechanics and the Company, Voice, and Plan sections. You write the domain sections, the coverage map, and the deep-dive bank, and you adjust Company, Voice, and Plan only where the domain needs it.

1. **List every section** of every brain file from team.json, in file order.
2. **Write the need for each section** in one line, for yourself: what the team must know, which agent uses it (its routing row), and the answer shape (a story, a list, a number, exact words, a table, yes/no).
3. **Choose the technique** per section with the table in §3. Default by answer shape: story → the last time it happened; how people talk → exact words; list the client knows → direct question; list the client should not invent → propose, then confirm; risky claims or limits → pushback round.
4. **Write 1-3 questions per section.** For each question write:
   - `ID`: the file's 2-letter prefix plus a number (`CO-1`, `VO-2`, `PL-4`, and domain prefixes you define, such as `RO-1` for roles.md).
   - The question: 30 words or fewer, plain, one idea.
   - `Fills:` the file and section (`roles.md · Interview stages`).
   - `Follow-ups:` up to 2 (an example, a number, or the exact words).
   - `Complete when:` what a usable answer contains ("at least one real example with what happened").
5. **Order** sections: Company, then the domain files in team.json order, then Voice, then Plan (Plan comes last because it proposes outputs, rhythm, and authority from everything learned before). Inside a section, go from easy to hard.
6. **Add one pushback round** of 5 questions on the domain's riskiest area, placed right after the section it protects. Name the skeptic ("a skeptical buyer", "an employment lawyer", "a picky editor", "a search engine reviewer"). Each question tests one of: value, risk, proof, difference, fit (adapt the five to the domain). The answers fill a "Q&A" or "to avoid" section.
7. **Write the coverage map**: a table with one row per brain-file section and the question IDs that fill it. Every section needs at least one question; every question appears in the map.
8. **Count.** Aim for 30-45 core questions in total. The template's fixed Company, Voice, and Plan questions are about 25 of them, so domain sections get 1-2 core questions each, plus the pushback round. Over 45: move the weakest to the deep-dive bank (the ones a drop or another answer already covers). Under 30: check coverage again.
9. **Write the deep-dive bank**: 20-30 optional questions that add depth to the thinnest sections. The lead uses them only if answers were thin or the client asks for more.
10. **Run the question checklist** (§7) on every question.

---

## 5. Method: the routine questions

Work in `kit/<vault_folder>/04-agents/question-banks/routine-questions.md`. The template holds the pick rules, personalization rules, and answer instructions. You write the categories and the examples.

1. **List the recurring inputs** the team needs each cycle, from the blueprint's routine design. Content kit: stories, opinions, lessons, customer words, wins, mistakes. HR example (fictional): open roles, new starters, people issues, policy questions, wins, culture moments.
2. **Turn each input into a category.** Write 8-15 categories. Each gets a `## Category: <Name>` heading, one line on what it collects and which bank or output it feeds, and 4-8 question templates.
3. **Write templates with placeholders** filled from the brain files at send time: `{{customer}}`, `{{service}}`, `{{role}}`, `{{pillar}}`. Every placeholder must name something the brain files hold.
4. **Favor stories.** Stories beat opinions, and opinions beat facts: at least half of each category's templates ask for a specific recent event.
5. **Keep the pick rules** from the template: 5 questions per cycle by default, at least 3 categories, at least 2 plan areas covered, no repeat of the same template within 8 weeks, and every question sent logged in `06-log/questions-asked.md`.
6. **Write 2 fictional example cycle messages**: the full message the lead would send, with 5 personalized questions and the answer instructions, within the routine message's word limit.
7. **Run the question checklist** (§7) on every template.

---

## 6. Intake questions (builder → requester, stage 1)

1. Ask only about gaps that change the design (stage 1, Step 5).
2. At most 5 per message, numbered, one decision each.
3. Recommended default first, marked "(recommended)", then 1-3 alternatives, so a reply can be "go" or "2: B".
4. Say in one line why it matters when that is not obvious.
5. Plain words; no factory jargon.

Example (fictional):

```
Stage 1/6 · Intake · 3 questions

1. Should the team send outreach emails itself?
   A. No, it drafts them and you send them (recommended)
   B. Yes, after you approve each one
2. How often should the owner get questions?
   A. Weekly (recommended)
   B. Every 2 weeks
3. Who approves the team's work on the client side?
   A. The owner (recommended)
   B. An office manager

Reply "go" for the recommended answers, or send changes like "1: B".
```

---

## 7. The question checklist (run it on every question)

A question passes only if all 8 are true:

1. It fills a named brain-file section or bank.
2. The client can answer from memory in under 2 minutes.
3. It asks one thing.
4. It uses plain words the client would use.
5. It does not lead ("Don't you think...?", "Wouldn't you agree...?").
6. It duplicates no other question.
7. Abstract questions carry an example or a "for example".
8. The follow-ups ask only for an example, a number, or exact words.

---

## 8. Bad and better

| Bad | Why | Better |
|---|---|---|
| "What is your brand voice?" | Abstract; nobody can answer it | The 60-second voice memo, then this-or-that calibration |
| "Describe your ideal customer and their pain points and goals." | Three questions in one; homework-like | "Think of your favorite customer. What was going on for them right before they called you?" |
| "Can you send your hiring policy document?" | Homework | Optional drops in setup; then "Walk me through the last time you hired someone." |
| "Don't you think fast replies matter most?" | Leading | "What makes a customer happy with you, in their words?" |
| "What KPIs matter for the E-E-A-T of your content?" | Jargon | "How would you know this month's articles worked?" |
| "What are your content pillars?" | The client should not invent strategy | Propose 3-5 pillars from the answers so far, then confirm |

---

## 9. Where to look in the reference kit

- `content-grokbot/kit/The-Almanac/04-agents/question-banks/setup-interview.md`: the full interview (sections A-E, coverage map, deep-dive bank). Read it before writing your first domain section.
- `content-grokbot/kit/The-Almanac/04-agents/question-banks/ritual-questions.md`: 14 categories, 114 templates, pick rules, and answer instructions.
- `content-grokbot/kit/The-Almanac/04-agents/workflows/setup.md`: how the interview runs (drops, drafting, approval).

---

## Checklist

- [ ] Every brain-file section in team.json has at least one question in the coverage map.
- [ ] 30-45 core setup questions, in the order Company, domain files, Voice, Plan.
- [ ] One pushback round of 5 questions on the domain's riskiest area.
- [ ] Propose-then-confirm used for outputs, authority, and anything the client should not invent.
- [ ] Deep-dive bank: 20-30 optional questions.
- [ ] Routine questions: 8-15 categories, 4-8 templates each, at least half story-based; 2 example cycle messages.
- [ ] Every question passes the 8-point checklist.
- [ ] Zero `<!-- FILL` markers left in both question-bank files.
