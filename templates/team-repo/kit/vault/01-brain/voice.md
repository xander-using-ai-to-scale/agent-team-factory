---
type: brain
file: voice
version: 0
status: empty
updated: ""
approved_on: ""
kit_version: <<KIT_VERSION>>
---

# Voice

Holds how the client sounds in writing and out loud: testable rules with examples, banned words, formatting habits, spoken and written samples, and rules learned from edits. The <<LEAD_NAME>> (<<LEAD_SHORT>>) fills it during setup from the interview, the 60-second voice memo, the this-or-that calibration, and any optional drops.
Read in full by every specialist and the QA Agent (routing table in [[00-START-HERE]]). Read-only: sub-agents never edit it, and after approval the <<LEAD_SHORT>> changes it only through [[04-agents/workflows/learning-loop#Brain change procedure]].

<!-- Fill rules (<<LEAD_SHORT>>): write only facts the client confirmed. Unknown → log a Q-### in [[06-log/open-questions]], write UNKNOWN (Q-###) in the field, add its pointer under ## Open questions; a section below its minimum count gets a Q-### too. Never guess.
Replace every {{placeholder}}. A placeholder holding a value, like {{no}} or {{1}}, is the default: confirm it with the client, then drop the braces. Delete unused template rows and blocks. Empty list → "- none"; empty table → one row with none in the first cell. Never edit guidance comments; {{ }} inside them are format examples.
Set status: draft when you start filling; status: approved needs the client's OK and zero {{ }} outside comments. Agents: UNKNOWN is not a fact; never fill it in; if your job needs it, reply BLOCKED. -->

## TL;DR
<!-- The 10 voice rules that matter most, 1 testable line each, taken from the sections below. Agents read this first. The <<LEAD_SHORT>> writes it last and updates it in the same edit as any change to this file; a new top rule replaces the weakest line, which stays in its own section.
Exactly 10 lines (this comment not counted); no {{ }} once approved.
Example (fictional). Good: "3. Max 2 sentences per paragraph." Bad: "3. Sound natural." -->
1. {{top_rule_1}}
2. {{top_rule_2}}
3. {{top_rule_3}}
4. {{top_rule_4}}
5. {{top_rule_5}}
6. {{top_rule_6}}
7. {{top_rule_7}}
8. {{top_rule_8}}
9. {{top_rule_9}}
10. {{top_rule_10}}

## How we sound
<!-- 5–10 rules, each one the QA Agent can check in a draft, each with a short example in the client's voice (their own words or a line they approved). Adjectives alone are never rules: "friendly" or "confident" tells an agent nothing.
Example (fictional). Good: "Rule: Put the conclusion in the first sentence · Example: "Raise your prices. Here's the math."" Bad: "Rule: Be confident." -->
- Rule: {{testable_rule}} · Example: "{{short_example_in_client_voice}}"
- Rule: {{testable_rule}} · Example: "{{short_example_in_client_voice}}"
- Rule: {{testable_rule}} · Example: "{{short_example_in_client_voice}}"
- Rule: {{testable_rule}} · Example: "{{short_example_in_client_voice}}"
- Rule: {{testable_rule}} · Example: "{{short_example_in_client_voice}}"

## How we never sound
<!-- 3–8 rules in the same format, each with a counter-example of the wrong sound: text the client rejected, or a line written to show the error.
Example (fictional). Good: "Rule: Never stack slogan fragments · Counter-example: "Dream big. Start small. Never quit."" Bad: "Rule: Don't be cringe." -->
- Rule: {{testable_rule}} · Counter-example: "{{short_counter_example}}"
- Rule: {{testable_rule}} · Counter-example: "{{short_counter_example}}"
- Rule: {{testable_rule}} · Counter-example: "{{short_counter_example}}"

## Phrases we use
<!-- 0–10 signature phrases, sayings, and recurring metaphors, verbatim from the client, each with when they use it and its source. The Limit line caps how often one piece may use them.
Example (fictional). Good: ""Boring beats clever." · when: closing a point about systems · source: voice memo 60s". Bad: "Some folksy sayings." -->
- "{{phrase_verbatim}}" · when: {{when_they_use_it}} · source: {{source}}
- "{{phrase_verbatim}}" · when: {{when_they_use_it}} · source: {{source}}

Limit: max {{1}} signature phrase per piece.

## Banned words and phrases
<!-- Every item in both lists is banned in every draft (the QA Agent's banned-words check). The QA Agent scans for each item case-insensitively and in every form (plural, -s, -ed, -ing, -ise/-ize spellings); items marked (figurative) or (as a verb) are banned only in that use.
A piece = 1 unit of work as the specialist's charter defines it (for example 1 email, 1 letter, 1 script, or 1 report).
Example (fictional). Good: QA flags "unlocking" as a form of "unlock". Bad: QA lets "Delving" pass because of the capital D. -->

### Client's banned list
<!-- Words and phrases the client hates, 1 per line, each with the reason and where it came from (setup or E-###).
Example (fictional). Good: ""hustle" · reason: sounds like hype · from: setup". Bad: "cringe stuff". -->
- "{{word_or_phrase}}" · reason: {{reason}} · from: {{setup / E-###}}

### Default anti-AI list
<!-- Active by default. The client can add or remove items through the brain change procedure. If the client says they genuinely use an item, move it to ## Phrases we use and note it in ## Changelog. If an item conflicts with a rule the client gave above, ask the client which wins before approval.
Example (fictional). Good: the client says "I really do say 'at the end of the day'" → item moved, changelog line added. Bad: an agent deciding an item "sounds fine here". -->

**Words**
- delve
- tapestry
- testament
- realm
- landscape (figurative)
- leverage (as a verb)
- unlock (figurative)
- unleash
- elevate
- empower
- supercharge
- game-changer (also game-changing)
- cutting-edge
- seamless
- robust
- synergy
- holistic
- paradigm
- journey (figurative)
- navigate (figurative)
- foster
- harness
- bespoke
- pivotal
- embark
- resonate
- transformative
- revolutionize (also revolutionise)
- myriad
- plethora
- meticulous
- underscore (as a verb)
- utilize (also utilise)
- moreover (also furthermore)

**Phrases**
- "In today's fast-paced world" (and any "In today's ... world / age / landscape")
- "Let's dive in" (also "dive into", "deep dive")
- "Let that sink in"
- "Buckle up"
- "Here's the thing"
- "At the end of the day"
- "The best part?"
- "Here's the kicker"
- "Without further ado"
- "I hope this helps"
- "Imagine a world where"
- "Picture this"
- "Take it to the next level" (also "next-level")
- "It's important to note" (also "It's worth noting")
- "Needless to say"
- "In conclusion" (also "In summary", "To sum up")
- "When it comes to"
- "What if I told you"

**Patterns**
- "It's not X, it's Y" reframes (also "This isn't about X. It's about Y.")
- "Not X. Not Y. Just Z." triplets
- Question or colon reveals: "The result? ...", "The catch? ...", "The secret: ..."
- Opening a piece with a generic rhetorical question ("Ever wondered why...?", "Are you tired of...?", "Want to know the secret...?"). A specific question with a concrete detail from the client's world is allowed ("How many invoices went out late last month?").
- 3 adjectives in a row describing one thing ("X, Y, and Z")
- Starting 3 or more lines of one piece with an emoji
- More than 1 exclamation mark per piece
- ALL-CAPS emphasis more than once per piece (acronyms and `[BRACKETED CAPS]` client-fill markers do not count)
- Hashtags in the middle of a sentence
- Ending a piece with "Thoughts?" or "Agree?"
- "Whether you're X or Y" openers
- "Say goodbye to X" (and "hello to Y") promises
- Double hedges: "may potentially", "could possibly", "might perhaps"

**Punctuation**
- Em dash (the long dash, Unicode U+2014): none by default; use a period or a comma.
- En dash with spaces (`word – word`) or double hyphen (`word -- word`) used as a dash: same rule.

## Formatting habits
<!-- One line per habit, each a number or a fixed choice the QA Agent can check. When a habit conflicts with a length or format rule in the specialist's charter, the charter wins.
Example (fictional). Good: "Paragraph length: max 3 sentences." Bad: "Paragraphs: short-ish." -->
- Language and spelling: {{language}}, {{US / UK / other}} spelling
- Point of view: {{I / we / I for stories and we for the business}}
- Sentence length: average {{number}} words; max {{number}} words
- Paragraph length: max {{number}} sentences
- Line breaks: {{where_they_break_lines}}
- Emoji use: {{none / few / many}} · allowed: {{emojis, or none}} · max {{number}} per piece
- Capitalization: {{sentence case / all lowercase / Title Case headlines}}
- Profanity: {{none / mild / strong}} · allowed words: {{words, or none}}
- Numbers: {{digits always / one to nine in words, 10 and up in digits}}
- Lists vs prose: {{prose only / lists for steps only / lists often}}
- Contractions: {{always / mostly / never}}

## Spoken voice
<!-- Rules for spoken work: anything said out loud in the client's name, such as calls, videos, audio, voicemails, and scripts. Samples come only from speech: the 60-second voice memo, interview voice notes, <<ROUTINE_NAME>> answers sent as voice notes, and transcripts; never from written text. Target: at least 3 samples after setup; fewer than 3 → log a Q-###.
Example (fictional). Good: "How they open: straight into the claim, no greeting." Bad: "Energy: good vibes." -->

**Rules**
- Pace: {{pace_rule_as_sentence_length_and_pauses}}
- Filler words they genuinely use: {{"word", "word", or none}} · max {{number}} per minute of speech
- How they open: {{opening_rule}} · Example: "{{opening_line_verbatim}}"
- How they close: {{closing_rule}} · Example: "{{closing_line_verbatim}}"
- Energy: {{energy_rule_as_checkable_traits}}

**Samples**

| # | Verbatim excerpt (1–4 sentences) | Source (voice memo 60s / interview voice note YYYY-MM-DD / <<ROUTINE_NAME>> YYYY-MM-DD / transcript YYYY-MM-DD) |
|---|---|---|
| 1 | "{{excerpt}}" | {{source}} |
| 2 | "{{excerpt}}" | {{source}} |
| 3 | "{{excerpt}}" | {{source}} |

## Written voice
<!-- 3–8 rules for written work: everything people read, such as emails, letters, documents, messages, and posts, in the How we sound format. Samples come only from the client's own documents in 02-sources/documents/, the this-or-that pick, or delivered work the client approved. Target: at least 1 sample after setup, 5 after 4 <<OUTPUT_UNIT_PLURAL>>; none → log a Q-###.
Example (fictional). Good: "Rule: Line 1 is a number or a blunt claim." Bad: "Rule: Catchy openings." -->

**Rules**
- Rule: {{testable_rule}} · Example: "{{short_example_in_client_voice}}"
- Rule: {{testable_rule}} · Example: "{{short_example_in_client_voice}}"
- Rule: {{testable_rule}} · Example: "{{short_example_in_client_voice}}"

**Samples**

| # | Verbatim excerpt (1–4 sentences) | Source (document YYYY-MM-DD / this-or-that pick YYYY-MM-DD / approved output: output id) |
|---|---|---|
| 1 | "{{excerpt}}" | {{source}} |
| 2 | "{{excerpt}}" | {{source}} |
| 3 | "{{excerpt}}" | {{source}} |

## Good examples
<!-- Pieces or passages that sound exactly like the client, each with why it works as traits an agent can copy. At least 1 after setup (the this-or-that pick). Sources: document, this-or-that pick, approved output, W-### winner.
Example (fictional). Good why: "Opens with a number, 2-sentence paragraphs, ends on a question answerable in 1 word." Bad why: "Feels authentic." -->

| # | Example (verbatim) | Why it works | Source |
|---|---|---|---|
| 1 | "{{example_verbatim}}" | {{checkable_traits}} | {{source}} |
| 2 | "{{example_verbatim}}" | {{checkable_traits}} | {{source}} |

## Bad examples
<!-- Text the client rejected or hates, each with what is wrong as traits an agent can avoid. At least 2 after setup (the rejected this-or-that versions). Sources: rejected in this-or-that, client-hated document, E-### edit.
Example (fictional). Good what's wrong: "3 rhetorical questions in a row, no concrete detail." Bad: "Not me." -->

| # | Example | What's wrong | Source |
|---|---|---|---|
| 1 | "{{example}}" | {{checkable_traits}} | {{source}} |
| 2 | "{{example}}" | {{checkable_traits}} | {{source}} |

## Rules learned from edits
<!-- Added only through the learning loop, with the client's approval ([[04-agents/workflows/learning-loop]]); newest first. A rule that belongs in the top 10 also goes into ## TL;DR. "- none" until the first approved rule.
Example (fictional). Good: "- Never open with a question (E-002, added v3)". Bad: "- Be more direct". -->
- {{rule}} (E-###, added vN)

## Open questions
<!-- Pointers only: each question lives in [[06-log/open-questions]], which is always the full list. Update pointers only while drafting in setup or inside an approved brain change. "- none" when empty.
Example (fictional). Good: "- Q-009 · Do you swear when you talk to customers, and which words? (see [[06-log/open-questions]])". Bad: "- tone?". -->
- Q-### · {{question}} (see [[06-log/open-questions]])

## Changelog
<!-- Newest first, one line per version; never edit old lines. Format: - vN · YYYY-MM-DD · {{change}} ({{E-### | client request | setup}}); client request = any other change the client approved (monthly review, post-delivery proposals, answered questions).
Every approved version: version +1, updated and approved_on = that date, one line here.
Example (fictional). Good: "- v3 · 2026-10-02 · Added banned phrase "hustle harder" (E-004)". Bad: "- voice tweaks". -->
- v0 · template · installed from kit <<KIT_VERSION>>
