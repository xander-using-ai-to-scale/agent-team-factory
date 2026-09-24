---
type: readme
folder: 02-sources
kit_version: <<KIT_VERSION>>
---

# 02-sources

## Purpose
Raw evidence: everything the client gives you, saved word for word. Brain files and banks are built from these files, so every original stays exactly as received.

## What goes here
Only files inside these 5 subfolders. Never save a file directly in `02-sources/`.
- [[02-sources/interview/README]]: setup interview answers and the 60-second voice memo.
- [[02-sources/routine-answers/README]]: answers to the <<ROUTINE_NAME>> questions (1 file per <<ROUTINE_NAME>>) and voice memos sent outside the <<ROUTINE_NAME>>.
- [[02-sources/transcripts/README]]: call, meeting, podcast, and webinar transcripts the client drops.
- [[02-sources/documents/README]]: docs, samples, SOPs, templates, and past work the client drops in, including pieces they love or hate.
- [[02-sources/other/README]]: website text, bios, brand docs, anything else.

## What never goes here
- Facts, summaries, or analysis drawn from a source: [[01-brain/README]] or [[03-banks/README]].
- Drafts, tickets, and deliverables: [[05-outputs/README]].
- Records of what you did: [[06-log/session-log]]. Client edits to drafts, as patterns: [[06-log/edits-log]].

## File naming
`YYYY-MM-DD-{{what}}.md`, lowercase kebab-case. Each subfolder README gives the exact pattern. The date is the day you save the file unless that README says otherwise. A `{{slug}}` is 2 to 5 lowercase words, kebab-case, max 40 characters. If the name already exists, add `-2` (then `-3`) before `.md`.
Example (fictional): `2026-10-06-client-onboarding-checklist.md`

## Frontmatter for files here
```
---
type: source
kind: {{interview | routine-answers | transcript | document | other}}
date: {{YYYY-MM-DD}}
permission: {{public-ok | ask | private}}
---
```
`kind` always matches the subfolder. `date` always matches the date in the file name.

Permission meanings:
- `public-ok`: may be quoted or used in outputs.
- `ask`: the <<LEAD_NAME>> (<<LEAD_SHORT>>) must get the client's yes before any use in outputs.
- `private`: never used in outputs. It may still inform voice and understanding.

Permission defaults (when 2 match, the stricter wins: `private`, then `ask`, then `public-ok`):
- Anything the client calls confidential, off the record, or under NDA: `private`.
- Other people's work the client loves or hates: `private` (style reference only, never quoted).
- Call, meeting, podcast, or webinar transcripts with other people: `ask`.
- The client's own published work, pages, and recordings: `public-ok`.
- Setup interview answers, <<ROUTINE_NAME>> answers, and the client's voice memos: `public-ok`, except parts marked with a `Private:` line. Other people named in them are handled per bank entry, where any third-party name starts as `ask`.
- Everything else (unpublished docs, SOPs, templates, drafts, private emails): `ask`.

## Who writes
The <<LEAD_NAME>> only. Sub-agents never write here.

## Who reads
- <<LEAD_NAME>>: every file, during setup, when processing <<ROUTINE_NAME>> answers, and when briefing each <<OUTPUT_UNIT>>.
<!-- FILL: one bullet per specialist whose routing row lists a file in this folder, naming the file it reads, for example "- Article Agent: the answers file named in its job ticket.", then the bullet "- No other agent reads this folder." When no specialist reads this folder, write only "- No sub-agent reads this folder." Source: 00-START-HERE §4 rows R12 and up; team.json specialists. Length: 1 bullet per specialist. Example: kit/The-Almanac/02-sources/README.md ## Who reads (Newsletter Agent bullet). -->

## Rules
1. Save every file verbatim: no spelling fixes, no summaries, no reordering, no removed filler words.
2. Never edit a saved file. Only 2 changes are allowed: appending new answers to a setup interview or <<ROUTINE_NAME>> answers file, and changing `permission` when the client tells you to (log it in [[06-log/session-log]]).
3. Never delete or rename a file here.
4. Audio, image, or PDF originals are optional: save them next to their `.md` file, named with the same base name (plus any suffix the subfolder README sets) and their original extension. The `.md` text file is always required.
5. Never use a part marked `Private:` in any output.
6. A bank entry is never more open than its source: a `private` file or part gives only `private` entries; an `ask` file gives `ask` entries until the client says yes to that entry.
7. Drops are optional. Never ask the client to go looking for material.
