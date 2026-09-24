---
type: readme
folder: 02-sources/interview
kit_version: <<KIT_VERSION>>
---

# interview

## Purpose
The client's setup interview answers and 60-second voice memo, word for word. Setup resumes from these files, and the <<BRAIN_FILE_COUNT>> brain files are drafted from them.

## What goes here
The setup interview file (1 per setup, appended answer by answer), redo files after `redo {{section}}`, and the 60-second voice memo transcript.

## What never goes here
Answers to the <<ROUTINE_NAME>> questions: [[02-sources/routine-answers/README]]. Material the client drops during setup: its subfolder in [[02-sources/README]]. Brain file drafts: [[01-brain/README]]. Skipped or unknown answers, as questions: [[06-log/open-questions]].

## File naming
- Setup interview: `YYYY-MM-DD-setup-interview.md`, date = the day the interview started. Later sessions append to this same file.
- Redo: `YYYY-MM-DD-setup-interview-redo-{{section}}.md`, section = the brain file's name without `.md` (for example `company`, `voice`, or `plan`). Where it repeats a question, the redo file wins.
- Voice memo: `YYYY-MM-DD-voice-memo-60s.md`. Stored audio: same base name, original extension.
Example (fictional): `2026-10-06-setup-interview.md`

## Frontmatter for files here
```
---
type: source
kind: interview
date: {{YYYY-MM-DD}}
permission: public-ok
---
```
Set `permission: private` only if the client calls the whole interview confidential.

## Who writes
The <<LEAD_NAME>> (<<LEAD_SHORT>>) only, following [[04-agents/workflows/setup]].

## Who reads
The <<LEAD_SHORT>> only: to resume setup, to draft the brain files, and to file bank entries.

## Rules
1. Save each answer the moment it arrives, before you send the next question.
2. 1 heading per question, in the order asked: `### {{question ID}} · {{question}}`, with the ID and wording exactly as in [[04-agents/question-banks/setup-interview]]. The answer goes below it, verbatim.
3. Extra lines under an answer, 1 per line: `Follow-up: {{your question}}` then the answer verbatim (max 2 per question); `From: {{source file path}}` when a drop answered it and the client confirmed; `Logged: Q-###` after "skip" or "don't know"; `Private: {{what, 10 words or fewer}}` for a part the client says is off the record.
4. Voice memo file: line 1 is `Received: {{YYYY-MM-DD HH:MM}}`, then the transcript verbatim. If you cannot transcribe the audio, ask the client to use their phone's voice-to-text or to type.
