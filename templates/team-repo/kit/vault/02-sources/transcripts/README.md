---
type: readme
folder: 02-sources/transcripts
kit_version: <<KIT_VERSION>>
---

# transcripts

## Purpose
Transcripts of real conversations the client drops, word for word. They show the client's spoken voice and the exact words of the people the client works with.

## What goes here
Sales call, client call, meeting, podcast, and webinar transcripts, 1 conversation per file, plus the recording if your platform stores it.

## What never goes here
- Setup interview answers: [[02-sources/interview/README]]. Answers to the <<ROUTINE_NAME>> questions: [[02-sources/routine-answers/README]]. Written documents, emails, or samples: [[02-sources/documents/README]].
- Facts or phrases taken from a transcript: the brain file that holds them ([[01-brain/README]]), during setup in that file's draft, and after setup through the brain change procedure in [[04-agents/workflows/learning-loop]].

## File naming
`YYYY-MM-DD-{{kind}}-{{slug}}.md`. kind = `call`, `meeting`, `podcast`, or `webinar`. Date = the day you save it. Slug = 2 to 5 lowercase words, max 40 characters. Recording: same base name, original extension.
Example (fictional): `2026-10-08-meeting-new-hire-onboarding.md`

## Frontmatter for files here
```
---
type: source
kind: transcript
date: {{YYYY-MM-DD}}
permission: ask
---
```

## Who writes
The <<LEAD_NAME>> (<<LEAD_SHORT>>) only.

## Who reads
The <<LEAD_SHORT>> only: during setup, and when filing bank entries and proposing brain changes.

## Rules
1. Line 1 after the frontmatter: `Speakers: {{name or role of each speaker}} · Recorded: {{YYYY-MM-DD | unknown}} · Confidentiality: {{none | NDA | client says confidential}}`.
2. Below line 1, paste the transcript verbatim. Never clean it up, shorten it, or reorder it.
3. Permission: `ask` when anyone besides the client speaks; `public-ok` only when the client alone speaks and the recording is already public; `private` when line 1 says NDA or confidential.
4. Never quote another speaker in any output unless the client said yes to that exact quote and it sits in a bank entry with `Permission: public-ok`.
5. A dropped recording you cannot transcribe: tell the client in 1 line and skip it. Never ask the client to transcribe a drop.
