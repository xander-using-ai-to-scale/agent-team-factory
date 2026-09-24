# Your <<TEAM_NAME>>: User Guide

Your <<TEAM_NAME>> <<TEAM_PURPOSE>>. It lives inside your agent (a Grokbot or a Hermes agent): <!-- FILL: one sentence, second person, max 25 words: what you do each cycle (answer 5 questions by voice memo) and what you get back. Source: TEAM-SPEC §2 (What we are building) and §12.3 (Routine). Length: max 25 words, ending with a period. Example: content kit docs/USER-GUIDE.md, line 3, after the colon ("you answer 5 questions by voice memo, and it sends back a pack of drafts in your voice"). -->

Sections 1 to 13 are for you, the business owner. Section 14 is for whoever installs and maintains it.

## 1. What it does

- **It interviews you once:** about 45–60 minutes, no homework. From your answers it writes <<BRAIN_FILE_COUNT>> "brain files" about your company, your voice, and your plan<!-- FILL: ", " plus what each domain brain file covers in 1 to 3 plain words, in team.json order, with "and" before the last item; no domain files: delete this comment. Source: team.json → brain_files (core: false); TEAM-SPEC §20 (Brain files). Length: max 12 words. Example: content kit docs/USER-GUIDE.md §1, bullet 1 ("your company, customer, offer, voice, and strategy"). -->.
- **It sends you 5 questions** the day before your delivery day, every week (or every 2 weeks).
- **You answer by voice memo or text,** 15–25 minutes in total. A walk works great.
- **Your team turns your answers into a <<OUTPUT_UNIT>>:** <!-- FILL: what one <<OUTPUT_UNIT>> holds by default, in plain words, as a list joined with commas and "and", ending with a period. Source: TEAM-SPEC §15 (Outputs); team.json → specialists. Length: max 35 words. Example: content kit docs/USER-GUIDE.md §1, bullet 4. -->
- **A QA Agent checks every piece** before you see it.
- **Everything is a draft unless you allowed it in your plan.** Your plan lists what your team may do on its own and what needs your yes each time; everything else, you do.
- **It learns your voice from your edits,** and only adds a rule when you say yes.

## 2. Meet your team

Your agent becomes your <<LEAD_NAME>>. It's the only one you talk to, and it runs a team of <<SUBAGENT_COUNT>> agents behind the scenes: a QA Agent and <<SPECIALIST_COUNT>> specialists.

| Who | What they do |
|---|---|
| **<<LEAD_NAME>>** (the only one you talk to) | Interviews you, sends your questions, and runs your monthly check-in. Briefs the team and delivers your <<OUTPUT_UNIT>>. Turns your edits into voice rules and keeps your brain files current, only with your OK. |
| **QA Agent** | Runs 10 checks on every piece before you see it, including your voice, banned words, facts and claims, privacy, format, and what your plan allows<!-- FILL: ", plus " and this team's own checks in plain words (max 12 words); no team checks: delete this comment. Source: TEAM-SPEC §11.6 (This team's checks). Length: max 12 words. Example: content kit docs/USER-GUIDE.md §2, QA Agent row. -->. Sends anything that fails back to be fixed or redone. |
<!-- FILL: one row per specialist, in team.json → specialists order: the exact name in bold, then what it makes in 1 to 2 plain sentences (max 40 words) with the default amount; say "only when you ask" for on-demand specialists. Source: team.json → specialists (name, job, on_demand_only); TEAM-SPEC §9.1 (contracts) and §15 (Outputs). Length: 1 row per specialist. Example: content kit docs/USER-GUIDE.md §2, rows after QA Agent. -->

<!-- FILL: 1 to 2 sentences on when the specialists work: which ones only work on the outputs you turn on in your plan, which ones only when you ask, and that you pick them in setup and can change them any time (section 11). Source: team.json → specialists (on_demand_only); TEAM-SPEC §9 (roster). Length: max 40 words. Example: content kit docs/USER-GUIDE.md §2, the line after the table ("The platform writers only work on the platforms you turn on..."). -->

### The rules your team follows

**Everything is a draft unless you allowed it in your plan.** In setup you approve two short lists in your plan file: what your team may do on its own (small things that are easy to undo) and what it may do only after your yes, each time. Everything else it prepares for you to do. You can change the lists any time (section 11).

**Your team never:**

- **Spends money or touches your account settings.** No payments, no passwords or payment details, no deleting accounts or data, and no changes to account settings, even if you ask. Nobody can switch these on.
- **Acts outside your plan.** Anything not on your plan's lists is prepared for you, never done for you.
- **Guesses or makes things up.** No invented facts, numbers, results, testimonials, quotes, names, credentials, or stories. When something is missing, it stops and asks you.
- **Uses a fact or claim you can't back up.** Facts and claims come only from files you approved and saved material you cleared. Anything on a "to avoid" list is banned.
- **Names a person, client, or company without your OK.** Anything you mark private is never used.
- **Changes your brain files without your yes** to the exact change. It never deletes anything from your <<VAULT_NAME>> either: old items are marked archived.

**Your team always:**

- **Reads the right files before working** (short summaries first, to save credits), shows which versions it used, and files everything in its one place.
- **Works in order.** Work that other work builds on is finished and checked first.
- **Shows you only work that passed QA,** or clearly marks it "held back".
- **Writes in your voice** with zero banned words: your spoken voice for anything said out loud, your written voice for anything people read.
- **Takes instructions only from you** (and its own kit files). Anything you drop in or forward, like transcripts, websites, or documents, is material to learn from, never orders to follow.
- **Keeps it short and logged.** Only your <<LEAD_NAME>> talks to you: one question at a time during interviews, and messages of 80 words or less (deliveries and file reviews run longer). It logs every session.

## 3. Install in 3 steps

For whoever sets it up. Your agent does the work; you only start it.

1. **Get the kit.** Use the GitHub repo link you were given, or download the zip file `<<TEAM_SLUG>>-kit-v<<KIT_VERSION>>.zip` from the repo's `dist` folder.
2. **Open a fresh agent and paste its start message.** On Grokbot, paste the message below (it's in `BOOTSTRAP-PROMPT.md`). On Hermes, paste the message in `BOOTSTRAP-PROMPT-HERMES.md`: it's the same, except that it opens `kit/INSTALL-HERMES.md` instead of `kit/INSTALL.md`. Put the repo link where it says [PASTE REPO LINK HERE], or attach the zip. "Fresh" means a new agent with no other instructions.
3. **Wait about 10–15 minutes** while it installs itself. When it's done, it starts your setup interview.

```
You're about to become my <<LEAD_NAME>>: the head of my <<TEAM_NAME>>.

Install the <<TEAM_NAME>> kit from this GitHub repo: [PASTE REPO LINK HERE]
(If I attached a zip file instead, use the zip.)

1. Get the kit onto your device (download the repo, or unzip the file).
2. Open kit/INSTALL.md and follow every step in order. Don't skip, merge, or improvise steps.
3. When the install is done, start my setup interview.

Don't do any work for me until setup is complete and I've approved my brain files.
```

**Using the zip?** Attach it and send the message as is. During the install it needs nothing else from you, and it messages you when it's ready.

## 4. Your setup interview (about 45–60 minutes)

No homework and nothing to prepare. You talk (or type); your <<LEAD_NAME>> asks, listens, and writes.

### How it goes

1. **Read the welcome.** One short message: what happens, how long it takes, and that you can pause any time.
2. **Drop anything handy (optional).** If you have <!-- FILL: the optional drops from the drops table, in the client's words, joined with commas and "or". Source: TEAM-SPEC §12.8 (Inputs, "Optional drops for this team"). Length: max 30 words. Example: content kit docs/USER-GUIDE.md §4, step 2 ("old posts you love or hate, call or podcast transcripts, your website link, or offer or pricing docs"). --> handy, drop them in. Don't go looking. Nothing handy? Say `skip`.
3. **Answer the sections in order:** Company, <!-- FILL: each domain section name in interview order, each followed by ", " (for example "Customers, Offer, "); no domain sections: delete this comment. Source: TEAM-SPEC §12.2 (setup interview design). Length: max 6 words. Example: content kit docs/USER-GUIDE.md §4, step 3. -->Voice, and Plan. Anything your drops already answered, it confirms in one line instead of asking.
4. **Approve each file.** After each section it drafts that brain file, shows you a short summary and the 3 most important points, and asks "What's wrong or missing?" Fix anything, or just say `ok`.
5. **Let it finish setting up.** It prepares the team for the outputs you chose, sets up your timed tasks (your questions, one reminder, a feedback question, and a monthly check-in<!-- FILL: ", " plus each extra schedule from team.json in plain words; none: delete this comment. Source: team.json → schedules; TEAM-SPEC §14. Length: max 12 words. Example: content kit docs/USER-GUIDE.md §4, step 5. -->), and tests Google Doc delivery if you want it.
6. **Choose your first run.** It asks whether to run your first 5 questions now (about 15 minutes) or wait for your usual day.

It won't start any work until all <<BRAIN_FILE_COUNT>> brain files are approved.

### The sections

| Section | What it covers | Special moment |
|---|---|---|
| Company | What you sell, who you serve, how you make money, what you believe, what makes you different | The basics, in your words |
<!-- FILL: one row per domain section, in interview order: the section name, what it covers in plain words (max 25 words), and its special moment (the exact-words questions, the pushback round, a list it proposes for your OK, or "none"). With no domain brain file, the pushback round closes Company: change the Company row's special moment to "The basics, then the pushback round". Source: TEAM-SPEC §12.2 (setup interview design) and §20 (Brain files). Length: 1 row per domain section. Example: content kit docs/USER-GUIDE.md §4, the Customer and Offer rows. -->
| Voice | How you sound, how you never sound, phrases you use, words you'd never use, and how you talk and write | The 60-second voice memo and "pick the version that sounds like you" |
| Plan | Your goal, what you get and how much, your delivery day and timing, how you get your <<OUTPUT_UNIT_PLURAL>>, what your team may do on its own, who on your team does what, and areas to avoid | You approve what you get and what your team may do |

### The special moments

- **Exact words from memory.** For example: "<!-- FILL: one exact-words question from the setup interview, word for word. Source: TEAM-SPEC §12.2 (Exact words from memory). Length: max 35 words. Example: content kit docs/USER-GUIDE.md §4 ("Think of your last sales call..."). -->" Your answers teach your team the words the people you serve really use.
- **The pushback round.** <!-- FILL: 2 sentences: after which section it comes, the exact line your <<LEAD_NAME>> opens it with ("Now I'll push back like" plus the skeptic), that it asks 5 tough questions and what they cover, and what your answers tell your team to say and never to claim. Source: TEAM-SPEC §12.2 (Pushback round). Length: max 50 words. Example: content kit docs/USER-GUIDE.md §4, "The skeptical-buyer round". -->
- **The 60-second voice memo.** "Record 60 seconds explaining what you do and who you help, like you're telling a friend." This teaches your team how you talk.
- **Pick the version that sounds like you.** It writes 3 versions of the same short piece (60–90 words): A is short and blunt, B is story-led and warm, C is punchy and structured. Pick one and say what's off, then choose between 2 variations of your pick. Your comments become voice rules.
- **Approve your plan and authority.** It proposes what you get and how much, and exactly what your team may do on its own, what needs your yes each time, and what stays a draft for you. You approve or edit both lists. You're never asked to invent a plan from scratch.

### While you answer

- **Answer one question at a time.** Each shows where you are, like `Company · 3/6`.
- **Send voice notes.** Typos and rambling are fine. When it offers options (a / b / c), reply with one letter.
- **Say `skip` any time** (or "don't know"). It saves the question for later and moves on.
- **Give an example when asked.** If an answer is vague, it asks for one example, number, or exact words, with no more than 2 follow-ups per question.
- **Pause whenever you need to.** Every answer is saved as it arrives. When you're back, say `status` to see where you left off.

Expect about 30–40 questions in total, fewer if your drops covered some. Optional deep-dive questions (up to 4 more per section) come only if you want them or if some answers were thin.

## 5. Your rhythm

These are the default times, in your timezone. You can change them (section 11).

| When | What happens | What you do | Time it takes |
|---|---|---|---|
| The day before delivery day, 10:00 | Your 5 questions arrive in one message | Read them | 1 minute |
| Whenever you're ready | Nothing, until you answer | Answer by voice memo or text. A walk works great. | 15–25 minutes |
| Delivery day | Your <<OUTPUT_UNIT>> arrives (it's built as soon as your answers are in). No answers by 09:00? One reminder comes, with the "bank" option. | Open your <<OUTPUT_UNIT>> (or reply `bank`) | Under 1 minute |
| When it suits you | Nothing is done for you outside your plan | Review, fill in the "Check before using" items, and use it | <!-- FILL: the review time for a full <<OUTPUT_UNIT>> as a range of minutes, plus anything that takes extra time, in max 8 words. Source: TEAM-SPEC §15 (Outputs). Length: max 14 words. Example: content kit docs/USER-GUIDE.md §5, row 4 ("About 30–45 minutes for a full pack (filming and posting are extra)"). --> |
| 3 days after delivery day, 10:00 | One quick feedback question | Paste anything you edited, or say what worked | 2 minutes |
| First delivery day of each month | A short check-in, after that day's <<OUTPUT_UNIT>> | Answer in one voice memo | About 5 minutes |
<!-- FILL: one row per extra schedule from team.json in the same 4-column form, in plain words; none: delete this comment. Source: team.json → schedules; TEAM-SPEC §14. Length: 1 row per extra schedule. Example: the rows above. -->

- **Prefer every 2 weeks?** Say `update my plan: every 2 weeks`. Your questions, the reminder, and the feedback question then come every 2 weeks; the monthly check-in stays monthly.
- **Reply `bank` if you skip the questions.** Your team builds the <<OUTPUT_UNIT>> from your saved material instead. You get one reminder, never more.
- **Look for your <<OUTPUT_UNIT>> in chat.** It's also saved in your <<VAULT_NAME>>, and if you chose Google Doc delivery in setup, you get a Google Doc link too.

### Answering your 5 questions

- **Talk, don't write.** A voice memo is best; text works too. Say the question number first, then take 1–5 minutes per question. Rambling is fine.
- **Tell stories.** Stories beat opinions, and opinions beat facts. Your most specific answer becomes the focus of your <<OUTPUT_UNIT>>.
<!-- FILL: 0 to 2 bullets with the extra answer tips from this team's routine design, in the same "**Bold label.** detail" format. No extra tips: delete this comment. Source: TEAM-SPEC §12.3 (Answer tips). Length: max 25 words each. Example: content kit docs/USER-GUIDE.md §5, "Tell stories." bullet. -->
- **Expect variety.** Your 5 questions come from at least 3 kinds of question, in your own words, and none repeats within 8 weeks.
- **Add feedback if you like.** The message ends with: "Also: send back anything you changed from the last <<OUTPUT_UNIT>>, or tell me what worked."
- **Answer one yes/no message about names.** If your answers mention another person, a client result, or anything confidential, it asks you in one yes/no message before anyone uses it.

### Your monthly check-in

On the first delivery day of each month, after that day's <<OUTPUT_UNIT>>, you get these questions in one message:

1. What changed in your business, offers, or prices?
2. Any new wins or results we can use?
3. What are your customers asking lately?
4. Anything the team should stop doing or saying?
<!-- FILL: the domain question as item 5, word for word, when TEAM-SPEC has one; none: delete this comment. Source: TEAM-SPEC §12.6 (Monthly review, domain question). Length: 1 line, max 12 words. Example: the 4 questions above. -->

It may add up to 3 questions still open from earlier (like ones you skipped), and it shows you any change to your brain files before making it. Then you get a 5-line month summary: <<OUTPUT_UNIT_PLURAL>> delivered, pieces produced, rules learned, winners, and open questions left.

## 6. What's in a <<OUTPUT_UNIT>>

These are the defaults. You only get sections for the outputs you turned on, and you can change amounts and outputs any time (section 11).

| Section | What you get | How to use it |
|---|---|---|
<!-- FILL: one row per specialist output, in file-number order: the section name as it appears in DELIVERY.md, what you get with the default quantity and the key limits in numbers (max 45 words), and how the client uses it (max 25 words). Mark on-demand outputs "(only when you ask)" in the first column. Source: TEAM-SPEC §15 (Outputs: client-facing names and output specs). Length: 1 row per output. Example: content kit docs/USER-GUIDE.md §6, table rows. -->

<!-- FILL: 0 to 2 sentences on how outputs relate to each other (which ones are built from which), in plain words. No dependencies: delete this comment. Source: team.json → specialists (depends_on); TEAM-SPEC §12.4 (Production order). Length: max 40 words. Example: content kit docs/USER-GUIDE.md §6, the line after the table ("The pillar's call to action..."). -->

### How a <<OUTPUT_UNIT>> is laid out

Every <<OUTPUT_UNIT>> opens with a "Built from" line: which versions of your brain files it used, and the QA result. Then:

1. **This <<OUTPUT_UNIT>> in 30 seconds:** the core idea, what's inside, and a suggested order<!-- FILL: ", plus " and the extra summary lines in plain words; none: delete this comment. Source: TEAM-SPEC §11.5 (DELIVERY.md layout, item 3). Length: max 15 words. Example: content kit docs/USER-GUIDE.md §6, "How a pack is laid out", item 1. -->.
2. **The pieces,** in the order of the table above.
3. **Check before using:** anything only you can fill in or confirm.
4. **Held back** (only if needed): pieces that didn't pass QA, with the reason.
5. **2-minute feedback:** paste any piece you edited, or say "winner" when something performs.

<!-- FILL: 0 to 2 short subsections (### heading + 2 to 5 lines each) for settings the client picks in setup that change how outputs look, in plain words. None: delete this comment. Source: TEAM-SPEC §15 (Outputs) and §20 (sections appended to plan.md and domain brain files). Length: max 80 words per subsection. Example: content kit docs/USER-GUIDE.md §6, "Scripts: word-for-word or beats". -->

### One piece, any time

Need something between <<OUTPUT_UNIT_PLURAL>>? Ask for it: <!-- FILL: the on-demand commands from section 9, in backticks, comma-separated, then ", or" plus one plain-language example in quotes. Source: TEAM-SPEC §17 (Client commands) and §12.7 (On-demand). Length: max 40 words. Example: content kit docs/USER-GUIDE.md §6, "One piece, any time". -->. Your <<LEAD_NAME>> checks the scope with you only if the request is unclear, and QA checks the result like everything else.

## 7. Review and use

Your <<OUTPUT_UNIT>> is a set of drafts. Your team only does what your plan allows (section 2); everything else is for you (or your staff) to do.

1. **Read "This <<OUTPUT_UNIT>> in 30 seconds" first.** It gives you the core idea and a suggested order.
2. **Fill in everything under "Check before using".** These are things only you can supply, marked in square brackets like [BOOKING LINK] or [START DATE], plus any fact to confirm. If it says "Nothing", you're clear.
<!-- FILL: 0 to 2 numbered steps (numbered 3 and 4, in the same "**Bold action.** detail" format) for anything the client sets up before using this team's work. Renumber the steps below to follow them. None: delete this comment. Source: TEAM-SPEC §15 (Outputs) and §13 (Authority: the draft-only actions the client does). Length: max 30 words each. Example: content kit docs/USER-GUIDE.md §7, step 3 ("Set up your lead magnet delivery"). -->
3. **Edit freely.** It's your work, so change anything.
4. **Use it, then paste your edits back** so your team learns from them (section 8).

<!-- FILL: 0 to 1 subsection (### heading + 3 bullets) on a part of the work that needs the client's own setup or tools, in plain words. None: delete this comment. Source: TEAM-SPEC §13 (Authority) and §15 (Outputs). Length: max 90 words. Example: content kit docs/USER-GUIDE.md §7, "How the lead magnet keyword works". -->

## 8. Teach it your voice

Your team learns from your edits, but it only adds a rule when you say yes.

- **Paste your edited version back.** It finds the original, compares the two, and names the pattern in one sentence.
- **Or say `this isn't me:` followed by your version.** Same result.
- **Approve with yes or no.** It proposes a rule with a before and after, then asks "Make this a rule? yes / no", up to 5 at a time. Only a yes changes your voice file.
- **Say `winner:` when something performs.** It logs the win and notes why it likely worked, so your team can repeat it.
- **Answer the feedback question.** 3 days after delivery day it asks once for edits and winners. It takes about 2 minutes.

**Example (fictional)**

- **Draft:** "In today's fast-paced world, business owners are busier than ever."
- **Your edit:** "Most owners I talk to haven't taken a day off since March."
- **Proposed rule:** "Open with a specific detail, never a general statement about the world."

Each rule you approve goes into your voice file and applies to every draft after that. That's how the drafts get closer to your voice, <<OUTPUT_UNIT>> by <<OUTPUT_UNIT>>.

- **Reply yes, no, or "show me"** when, right after a <<OUTPUT_UNIT>>, it suggests up to 5 changes to your brain files in one message.
- **Say `show my voice full`** to see every rule and when it was added.

## 9. Things you can say

Plain language always works; these are shortcuts. Swap anything in {{double curly brackets}} for your own words.

| You say | What happens |
|---|---|
| `help` | Lists these commands in one short message |
| `status` | Shows your setup progress, or: your next questions date, your last <<OUTPUT_UNIT>>, anything waiting on you, and how many open questions are left |
| `questions now` | Sends your 5 questions right away |
| `bank` / `bank <<OUTPUT_UNIT>>` | Builds your next <<OUTPUT_UNIT>> from your saved material (no new answers needed) |
<!-- FILL: one row per on-demand command, with the command in backticks exactly as in TEAM-SPEC §17 and the lead charter's Client commands, and what happens in plain words (max 25 words). Source: TEAM-SPEC §17 (Client commands). Length: 1 row per command. Example: content kit docs/USER-GUIDE.md §9, rows "write a {{platform}} post about {{topic}}", "make a VSL for {{offer}}", and "lead magnet about {{topic}}". -->
| `this isn't me: {{your version}}` (or just paste an edited piece) | Compares your version (after the colon) with the draft, then proposes a voice rule for you to approve |
| `winner: {{which piece}} {{result}}` | Logs the win and notes why it likely worked, so your team can repeat it |
| `show my {{file}}` | Shows that file's short summary. Add `full` at the end to see the whole file. Your files: company, voice, plan<!-- FILL: ", " plus each domain brain file name without .md, in team.json order; no domain files: delete this comment. Source: team.json → brain_files. Length: max 6 words. Example: content kit docs/USER-GUIDE.md §9, the "show my" row. -->. |
| `update my {{file}}: {{change}}` | Shows you the exact change (before and after), then applies it when you say yes |
| `change delivery day to {{day}}` / `change question time to {{time}}` | Updates your plan file and resets your timed tasks to match |
| `add {{output}}` / `remove {{output}}` | Turns that output on or off in your plan file |
| `pause questions for {{N}} weeks` / `resume questions` | Pauses or restarts your questions |
| `redo {{section}}` | Re-runs that section of your setup interview |
| `export my vault` | Zips your <<VAULT_NAME>> and sends it to you (so you can open it in Obsidian or keep a backup) |

Examples: <!-- FILL: 1 on-demand command filled in with a fictional topic, in backticks, then a comma. Source: TEAM-SPEC §17 (Client commands). Length: max 12 words. Example: content kit docs/USER-GUIDE.md §9, the Examples line ("write a LinkedIn post about raising your prices"). --> `show my voice full`, `pause questions for 2 weeks`.

Can't remember any of these? Say `help`.

## 10. Your <<VAULT_NAME>>

Your <<VAULT_NAME>> is your <<LEAD_NAME>>'s memory: a folder of plain text files on the device your agent runs on.

| Part | What's inside | How it changes |
|---|---|---|
| 00-START-HERE | The front page: what your <<VAULT_NAME>> is, the rules, and a map of the folders | Updated with new kit versions |
| 01-brain | Your <<BRAIN_FILE_COUNT>> brain files: company, voice, plan<!-- FILL: ", " plus each domain brain file name without .md, in team.json order; no domain files: delete this comment. Source: team.json → brain_files. Length: max 6 words. Example: content kit docs/USER-GUIDE.md §10, 01-brain row. --> | Only with your OK |
| 02-sources | Your raw words: interview and <<ROUTINE_NAME>> answers, voice memo transcripts, and anything you dropped in | Saved word for word, never edited |
| 03-banks | <!-- FILL: "Your " plus every bank title in plain words, joined with commas and "and". Source: team.json → banks (title). Length: max 15 words. Example: content kit docs/USER-GUIDE.md §10, 03-banks row ("Your stories, proof (results and testimonials), hooks, and ideas"). --> | Grows every time you answer |
| 04-agents | How your team works: job descriptions, step-by-step workflows, question lists, and templates | Replaced when the kit is updated |
| 05-outputs | Every <<OUTPUT_UNIT>>, one folder each | A new folder per <<OUTPUT_UNIT>> |
| 06-log | History: session notes, your edits, winners, open questions, and questions already asked | Added to after every session |

### Privacy

- **It lives on your agent's device.** Nothing in your <<VAULT_NAME>> is published anywhere.
- **Names need your OK.** Anything with another person's name, a client result, or a confidential detail stays "ask first" until you say yes.
- **Say "off the record"** and it's marked private: never used in your team's work.
- **Google Docs are optional.** If you turned on Google Doc delivery, each <<OUTPUT_UNIT>> is also saved as a Google Doc.
- **Your platform's terms still apply.** Your Grokbot or Hermes platform's own privacy terms cover what you send it.

### Get a copy

Say `export my vault`. Your <<LEAD_NAME>> zips your <<VAULT_NAME>> and sends it to you. Keep it as a backup, or open it in Obsidian, a free notes app:

1. **Install Obsidian** from obsidian.md.
2. **Unzip** the file you received.
3. **Open Obsidian, choose "Open folder as vault",** and pick the unzipped folder.

Your copy is a snapshot: edits you make in it don't reach your <<LEAD_NAME>>. To change something, tell it: `update my {{file}}: {{change}}`.

## 11. Changing things

Just say it. Plain language works; these phrases are the shortcuts.

| To change | Say |
|---|---|
| Your delivery day | `change delivery day to {{day}}` |
| The time your questions arrive | `change question time to {{time}}` |
| Weekly or every 2 weeks | `update my plan: every 2 weeks` (or `weekly`) |
| Your timezone | `update my plan: my timezone is now {{city}}` |
| Which outputs you get | `add {{output}}` / `remove {{output}}` |
| How many pieces you get | `update my plan: {{change}}`, e.g. <!-- FILL: 1 filled-in example in backticks with a real output name from plan.md → Outputs and quantities and a fictional number. Source: TEAM-SPEC §15 (Outputs). Length: max 12 words. Example: content kit docs/USER-GUIDE.md §11 ("update my strategy: 2 LinkedIn posts per pack"). --> |
| What your team may do on its own | `update my plan: {{change}}`. It shows you the change first. Spending money, passwords or payment details, deleting accounts or data, and account settings can't be switched on. |
| Areas to stay away from | `update my plan: never touch {{topic}}` |
| A break from questions | `pause questions for {{N}} weeks`, then `resume questions` |
<!-- FILL: one row per domain brain file the client changes often: what it holds in plain words, and `update my` plus the file name without .md, plus ": {{change}}" in backticks. None: delete this comment. Source: team.json → brain_files (core: false); TEAM-SPEC §20 (Brain files). Length: 1 row per file. Example: content kit docs/USER-GUIDE.md §11, "Your offers or prices" row. -->
| Anything else in a brain file | `update my {{file}}: {{change}}` |
| A whole setup section | `redo {{section}}` (<!-- FILL: every setup section name in lowercase, in interview order, joined with commas and "or". Source: TEAM-SPEC §12.2 (setup interview design). Length: 1 line. Example: content kit docs/USER-GUIDE.md §11, last row ("company, customer, offer, voice, or strategy"). -->) |

What happens next:

- **Approve the change.** Every change to a brain file, including outputs, timing, and what your team may do, is shown to you first (before and after). It's applied when you say yes and noted in that file's changelog.
- **Expect a reset after timing changes.** A new delivery day, question time, pace, or timezone resets all your timed tasks to match.
- **Know what a pause stops:** your questions, the reminder, and the feedback question. The restart date is noted in your plan file, and your questions come back on their own on that date. Say `resume questions` to restart sooner.

## 12. Troubleshooting

| Problem | What to do |
|---|---|
| It doesn't sound like me | Paste your edited version back, or say `this isn't me:` plus your version, and approve the rules it proposes. Still far off? Say `redo voice`. |
| I missed my questions | Reply `bank` for a <<OUTPUT_UNIT>> built from your saved material, or answer when you can: your <<OUTPUT_UNIT>> is built once your answers arrive. For a fresh set, say `questions now`. |
| No <<OUTPUT_UNIT>> arrived | Say `status` to see your last <<OUTPUT_UNIT>> and anything waiting on you. A <<OUTPUT_UNIT>> needs your answers (or `bank`) and all <<BRAIN_FILE_COUNT>> brain files approved. If you paused, say `resume questions`. |
| A fact or claim is wrong | Don't use that line. Send the correct fact, or say `update my {{file}}: {{change}}`. Your team only uses facts from files you approved, so fixing the file fixes every future <<OUTPUT_UNIT>>. |
| I want fewer or more pieces | Say `update my plan: {{change}}`, e.g. <!-- FILL: 1 filled-in example in backticks with a real output name and a fictional number. Source: TEAM-SPEC §15 (Outputs). Length: max 12 words. Example: content kit docs/USER-GUIDE.md §12 ("update my strategy: 3 short-form scripts per pack"). -->. |
| I want to add an output | Say `add {{output}}`. Your team covers <!-- FILL: every output in plain words, joined with commas and "and", marking on-demand ones "(on request)". Source: team.json → specialists; TEAM-SPEC §15 (Outputs). Length: max 40 words. Example: content kit docs/USER-GUIDE.md §12, "I want to add a platform" row. -->. |
| It won't do something I asked | Your team only does what your plan allows. To allow it, say `update my plan: {{change}}` and approve the change. Spending money, passwords or payment details, deleting accounts or data, and account settings always stay with you. |
| It asked for a password or a payment | It never should. Don't send it. Do that step yourself, and tell whoever set up your agent. |
| The Google Doc isn't working | Nothing is lost: your <<OUTPUT_UNIT>> still arrives in chat and is saved in your <<VAULT_NAME>>, and your <<LEAD_NAME>> tells you in one line when it switches to chat. To get Google Docs back, ask whoever set up your agent to check its Google access. |
| It asked something I already answered | Reply "already answered" and say where (for example, "in setup"). Your questions never repeat within 8 weeks, and setup skips anything your drops already covered. |
| I want to redo part of setup | Say `redo {{section}}`, e.g. `redo voice`. It re-runs that section, and you approve the updated file. |
| I want to stop for a while | Say `pause questions for {{N}} weeks`, then `resume questions` when you're back. You can still ask for single pieces while paused. |
| It says something is "held back" | That piece didn't pass QA after 3 rounds, so it was left out. Read the reason; if it needs something from you (a fact, a number, a permission), reply with it and ask for a new version. If other pieces are built from it, they wait too. |
| My voice memo didn't go through | Use your phone's voice-to-text, or type your answer. |
| I shared something private | Say "that's off the record". It's marked private and never used. |
| An area came up that I want to avoid | Say `update my plan: never touch {{topic}}`. QA checks every draft against that list. |
<!-- FILL: 0 to 4 rows for problems specific to this team's outputs, each with what to do in 1 to 3 sentences, using commands from section 9. None: delete this comment. Source: TEAM-SPEC §9.1 (contracts), §12.4 (Production order), and §15 (Outputs). Length: max 50 words per answer. Example: content kit docs/USER-GUIDE.md §12, "I want to add a platform" and "It says something is held back" rows. -->

## 13. FAQ

### Does it act for me?

Only where your plan allows it. Everything else is a draft: your team prepares it, and you (or your staff) do it. It never spends money, enters passwords or payment details, deletes accounts or data, or changes account settings.

### Do I need to prepare anything?

No. The setup interview fills every gap. If you have documents, transcripts, or your website handy, drop them in during setup, but don't go looking.

### How much time does it take per week?

About 15–25 minutes to answer your questions, plus <!-- FILL: the review time for a full <<OUTPUT_UNIT>> as a range of minutes, the same range as section 5. Source: TEAM-SPEC §15 (Outputs). Length: 1 range. Example: content kit docs/USER-GUIDE.md §13, "How much time does it take per week?" ("about 30–45 minutes to review a full pack"). --> minutes to review a full <<OUTPUT_UNIT>>. Add 2 minutes for the feedback question and, once a month, about 5 minutes for the check-in.<!-- FILL: " " plus 1 sentence on what takes extra time outside the team's work (for example recording or sending); none: delete this comment. Source: TEAM-SPEC §13 (Authority) and §15 (Outputs). Length: max 15 words. Example: content kit docs/USER-GUIDE.md §13 ("Filming and posting are extra."). -->

### Can my staff use the work?

Yes. Forward the <<OUTPUT_UNIT>> from chat, or share the Google Doc if you use them. Send your staff's edits back through your chat so your <<LEAD_NAME>> learns from them too.

### Is my information private?

Your <<VAULT_NAME>> lives on your agent's device, and nothing in it is published. Your team never names a person, client, or company without your OK, and anything off the record is never used. Your platform's own privacy terms cover what you send it.

### What if I run two businesses?

Use a separate agent for each business, each with its own install and setup interview. Each <<VAULT_NAME>> is built around one business, so this keeps voices, plans, and facts from mixing.

### Can I use it with Claude or another AI?

It's designed to: the kit is plain text files, with install steps for Grokbot and Hermes, so another agent platform such as Claude can follow it too. Some features depend on the platform. Timed questions need a scheduler (you can always say `questions now`), and if separate team members aren't available, your <<LEAD_NAME>> does each job itself and QA still checks it.

### What happens when the kit gets updated?

Only the files that describe how your team works are replaced. Your brain files, sources, banks, <<OUTPUT_UNIT_PLURAL>>, and history are never overwritten.

<!-- FILL: 1 to 3 questions specific to this team, each as a ### question heading and a 1 to 3 sentence answer that points to a command or section. Source: TEAM-SPEC §1 (Approved blueprint), §13 (Authority), and §15 (Outputs); TEAM-BRIEF → 11 Constraints. Length: max 60 words per answer. Example: content kit docs/USER-GUIDE.md §13, the last 3 questions. -->

## 14. For operators (installing, updating, maintaining)

This section is for whoever installs and maintains the kit. Light technical terms ahead.

### Repo layout

| Path | What it is |
|---|---|
| `README.md` | Human overview and 3-step install |
| `BOOTSTRAP-PROMPT.md` | The exact start message for a fresh Grokbot (same as section 3) |
| `BOOTSTRAP-PROMPT-HERMES.md` | The exact start message for a fresh Hermes agent |
| `CHANGELOG.md` | Kit version history |
| `team.json` | The approved blueprint, machine-readable. The checker and the zip builder read it. |
| `.gitignore` | Files git ignores (Obsidian settings, Python caches, OS files) |
| `docs/TEAM-BRIEF.md` | The brief the team was designed from |
| `docs/TEAM-SPEC.md` | The approved blueprint and build contract. If a kit file and the spec disagree, the spec wins. |
| `docs/USER-GUIDE.md` | This guide (the source for the Google Doc) |
| `kit/INSTALL.md` | The step-by-step install runbook a Grokbot follows, with the manifest |
| `kit/INSTALL-HERMES.md` | The step-by-step install runbook a Hermes agent follows, with the manifest |
| `kit/hermes-skills/` | One skill per agent for Hermes, plus a README |
| `kit/<<VAULT_FOLDER>>/` | The vault template, copied onto the agent's device |
| `scripts/check_kit.py` | Checks team.json, links, frontmatter, headings, agent names, schedules, and both manifests |
| `scripts/build_zip.py` | Rebuilds the zip from `kit/` |
| `dist/<<TEAM_SLUG>>-kit-v<<KIT_VERSION>>.zip` | Zip of the `kit/` folder. Rebuild it after any edit. |

### Install flow on Grokbot (under 15 minutes, no client input beyond the start message)

1. **Copies the vault** (`<<VAULT_FOLDER>>/`) onto its own device and verifies the manifest.
2. **Records the install facts** (including `platform: grokbot`) and saves its permanent <<LEAD_NAME>> instructions.
3. **Creates all <<SUBAGENT_COUNT>> sub-agents:** the QA Agent and <<SPECIALIST_COUNT>> specialists. Inactive ones simply never get tickets.
4. **Tests sub-agent file access.** No vault access: packet mode (`packet_mode: yes` in `00-START-HERE.md`; the <<LEAD_SHORT>> pastes the needed files into each job ticket). An unavailable sub-agent: mode fallback (the <<LEAD_SHORT>> does that job with the agent's charter; QA still runs).
5. **Confirms the scheduler works.**
6. **Logs the session** and starts the setup interview.

### Install flow on Hermes

Same vault, same rules, and the same outcomes in the same order. `kit/INSTALL-HERMES.md` holds the Hermes mechanics: how the <<LEAD_NAME>>'s standing instructions are saved, how the QA Agent and the specialists run (one skill per agent from `kit/hermes-skills/`, run as a subagent per job), and how the schedules are created. It records `platform: hermes` in `00-START-HERE.md`. Packet mode and mode fallback work the same way.

### Updating an existing install

1. **Replace kit-owned files only:** everything in `04-agents/`, every `README.md` (including those inside client-owned folders), and the body of `00-START-HERE.md`, keeping its frontmatter values (only `kit_version` changes to the new version).
2. **Never touch client-owned folders:** `01-brain/`, `02-sources/`, `03-banks/`, `05-outputs/`, `06-log/`.

The agent does this itself when you send it the new kit: it follows "Updating an existing install" at the end of `kit/INSTALL.md` (Grokbot) or `kit/INSTALL-HERMES.md` (Hermes).

### Changing the kit

1. **Change `docs/TEAM-SPEC.md` first** (and `team.json` when agents, brain files, banks, or schedules change), then the kit files, then `CHANGELOG.md` (bump the kit version).
2. **Validate:** run `python scripts/check_kit.py`. It must report 0 errors and 0 warnings. `python scripts/check_kit.py --write-manifest` regenerates the manifests in both install runbooks.
3. **Rebuild the zip:** run `python scripts/build_zip.py` (rebuilds the zip in `dist/` from `kit/`).

- **Keep kit files generic.** No client details, and no invented platform commands, menu names, or buttons.
- **Keep the commands in sync.** The <<LEAD_NAME>> charter's "Client commands" section owns the set; TEAM-SPEC §17 and section 9 of this guide must list the same commands.

### Schedules and fallbacks

| Name | When (default, client's timezone) | Does |
|---|---|---|
| `routine-send` | Day before delivery day, 10:00 | Sends the <<ROUTINE_NAME>> questions |
| `routine-reminder` | Delivery day, 09:00 | Only if no answers yet: 1 reminder + the "bank" option |
| `feedback-check` | 3 days after delivery day, 10:00 | Asks for edits and winners |
| `monthly-review` | First delivery day of each month, after the delivery | Runs the monthly review |
<!-- FILL: one row per extra schedule after the 4 fixed ones, in team.json → schedules order, with the name in backticks, default time, and what it does; no extra schedules: delete this comment. Source: team.json → schedules; TEAM-SPEC §14. Length: 1 row per extra schedule. Example: content kit docs/USER-GUIDE.md §14, "Schedules and fallbacks" table. -->

- **Every 2 weeks:** `routine-send`, `routine-reminder`, and `feedback-check` run every 2 weeks.
- **Timing changes:** a new delivery day, time, cadence, or timezone goes through the brain change procedure on `plan.md`; then every schedule is deleted and recreated.
- **Pauses:** `pause questions for {{N}} weeks` sets "Paused until" in the Rhythm section of `plan.md`. The schedules keep running but skip while paused; the first `routine-send` on or after that date clears the pause and runs normally. `resume questions` clears it immediately.
- **No scheduler:** the <<ROUTINE_NAME>> runs only when the client says `questions now`.
- **Other fallbacks:** audio that can't be transcribed means the client uses phone voice-to-text or types; a Google Doc that can't be created means delivery in chat and the vault only.
