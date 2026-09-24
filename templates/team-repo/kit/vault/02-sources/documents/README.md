---
type: readme
folder: 02-sources/documents
kit_version: <<KIT_VERSION>>
---

# documents

## Purpose
Documents the client drops in, word for word: docs, samples, SOPs, templates, and past work, written by the client or by others. They show how the client's work is done, the style the client wants, and the style to avoid.

## What goes here
Docs, SOPs, checklists, templates, offer and pricing docs, past work, and samples (emails, letters, reports, posts, proposals), including pieces the client says they love or hate, and the client's own edited versions of delivered work. 1 document per file.

## What never goes here
- Spoken material: [[02-sources/transcripts/README]]. Website text, bios, brand docs: [[02-sources/other/README]].
- Voice rules drawn from documents: [[01-brain/voice]]. Client edits to our drafts, as patterns: [[06-log/edits-log]].

## File naming
- Docs, SOPs, templates, and past work: `YYYY-MM-DD-{{slug}}.md`.
- Pieces the client loves or hates: `YYYY-MM-DD-loved-{{slug}}.md` or `YYYY-MM-DD-hated-{{slug}}.md`.
- The client's edited version of a delivered piece: `YYYY-MM-DD-edit-{{output_label}}.md` ([[04-agents/workflows/learning-loop]]). The output label is the output file's name without its number and `.md`.
- Date = the day you save it. Slug = 2 to 5 lowercase words naming the document, max 40 characters.
Example (fictional): `2026-10-06-hated-cold-intro-email.md`

## Frontmatter for files here
```
---
type: source
kind: document
date: {{YYYY-MM-DD}}
permission: {{public-ok | ask | private}}
---
```

## Who writes
The <<LEAD_NAME>> (<<LEAD_SHORT>>) only.

## Who reads
The <<LEAD_SHORT>>: during setup (the voice section, the this-or-that calibration, and pre-filling brain drafts), when proposing voice rules, and when briefing work that follows a client document.<!-- FILL: when a specialist's routing row lists a file in this folder (for example a template the client wants reused), append " The <specialist name> reads the document named in its job ticket." for each one; delete this comment when none does. Source: 00-START-HERE §4 rows R12 and up. Example: kit/The-Almanac/02-sources/README.md ## Who reads (Newsletter Agent bullet). -->

## Rules
1. Line 1 after the frontmatter: `What it is: {{doc | SOP | template | past work | sample | loved | hated | edit}} · Written by: {{client | someone else}} · From: {{link, file name, or "pasted in chat"}}`.
2. Line 2: `Client's reason: "{{their words, verbatim}}"` or `Client's reason: not given`. Then the document, verbatim.
3. Permission: the client's own published piece `public-ok`; the client's own unpublished document (drafts, SOPs, templates, internal docs) `ask`; anything written by someone else `private`.
4. Never quote or copy sentences from a piece written by someone else. Use it only to learn what the client likes or dislikes, or how the work is done.
5. Samples with no loved or hated label: file the client's own pieces as `loved`; for someone else's piece, ask 1 question: "Love it or hate it? a) love b) hate".
6. A screenshot or file you cannot read: tell the client in 1 line and skip it.
7. A newer version of a document: save it as a new file with the new date. The newest file wins; never edit the old one.
