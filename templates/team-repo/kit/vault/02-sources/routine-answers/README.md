---
type: readme
folder: 02-sources/routine-answers
kit_version: <<KIT_VERSION>>
---

# routine-answers

## Purpose
The client's answers to the questions of each <<ROUTINE_NAME>>, word for word. Every <<OUTPUT_UNIT>> built from new answers starts from 1 of these files.

## What goes here
1 answers file per <<ROUTINE_NAME>> (every piece, voice or text, as it arrives), voice memos the client sends outside the <<ROUTINE_NAME>> that carry something the team can use (a story, a result, a fact, an idea), other answers a workflow asks for, and their audio if your platform stores it.

## What never goes here
Setup interview answers and the 60-second voice memo: [[02-sources/interview/README]]. Call or meeting recordings: [[02-sources/transcripts/README]]. The questions as sent: [[06-log/questions-asked]]. Bank entries found in the answers: [[03-banks/README]].

## File naming
- Answers: `YYYY-MM-DD-routine-answers.md`, date = the day the questions were sent (by the `routine-send` schedule or after `questions now`), even if answers arrive later.
- Voice memo outside the <<ROUTINE_NAME>>: `YYYY-MM-DD-voice-memo-{{slug}}.md`, date = the day it arrived.
- Monthly review answers: `YYYY-MM-DD-monthly-review.md` ([[04-agents/workflows/monthly-review]]).
- The client's notes for an on-demand <<OUTPUT_UNIT>>: `YYYY-MM-DD-od-{{slug}}.md` ([[04-agents/workflows/on-demand]]).
- Any other answer a workflow asks for (for example a missing fact while briefing the <<OUTPUT_UNIT>>): `YYYY-MM-DD-{{slug}}.md`, with the slug the workflow gives ([[04-agents/workflows/production]]).
- Audio: the text file's base name plus `-{{nn}}` (2-digit arrival order: `01`, `02`) and the original extension.
Example (fictional): `2026-10-11-routine-answers.md`

## Frontmatter for files here
```
---
type: source
kind: routine-answers
date: {{YYYY-MM-DD}}
permission: public-ok
---
```

## Who writes
The <<LEAD_NAME>> (<<LEAD_SHORT>>) only, following [[04-agents/workflows/routine]].

## Who reads
The <<LEAD_SHORT>> (processing answers, briefing each <<OUTPUT_UNIT>>)<!-- FILL: append ", and " plus each specialist whose routing row lists the answers file, with "(the file named in its job ticket)", for example ", and the Article Agent (the file named in its job ticket)"; delete this comment when no specialist reads it. Source: 00-START-HERE §4 rows R12 and up. Example: kit/The-Almanac/02-sources/voice-memos/README.md ## Who reads. -->.

## Rules
1. Create the answers file when the first piece arrives. Append every later piece at the end; never insert above existing text.
2. Each piece is 1 block: heading `### Q{{n}} · {{question exactly as sent}}`, then `Received: {{YYYY-MM-DD HH:MM}} · {{voice memo | text}}`, then the answer verbatim. A memo outside the <<ROUTINE_NAME>> has no heading: the `Received:` line, then the transcript.
3. Optional lines directly under `Received:`: `Also answers: Q{{n}}` (1 piece covers several questions; file it under the first); `Audio: {{file name}}`; `Private: {{what, 10 words or fewer}}` (a part the client says is off the record; never used in any output).
4. Anything in the reply that answers none of the questions (an edited draft, a result, a new idea): a block headed `### Extra · {{what it is, 5 words or fewer}}` with the same `Received:` line.
5. Transcribe audio with your platform's transcription; if that fails, ask the client to use their phone's voice-to-text or to type. Times use the client's timezone from [[01-brain/plan#Rhythm]].
