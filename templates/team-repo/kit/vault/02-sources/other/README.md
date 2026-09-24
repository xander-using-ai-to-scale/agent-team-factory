---
type: readme
folder: 02-sources/other
kit_version: <<KIT_VERSION>>
---

# other

## Purpose
Every other document the client gives you, word for word: website text, bios, brand docs, and anything that fits no other subfolder.

## What goes here
Website pages, bios and about pages, brand docs and style guides, and any drop that fits no other subfolder of [[02-sources/README]]. 1 document or web page per file.

## What never goes here
- Interview answers or answers to the <<ROUTINE_NAME>> questions: [[02-sources/interview/README]], [[02-sources/routine-answers/README]]. Transcripts: [[02-sources/transcripts/README]]. Docs, SOPs, templates, past work, and samples the client loves or hates: [[02-sources/documents/README]].
- Confirmed facts about the business: [[01-brain/company]] and the other brain files in [[01-brain/README]].

## File naming
`YYYY-MM-DD-{{slug}}.md`. Date = the day you save it. Slug = 2 to 5 lowercase words naming the document, max 40 characters.
Example (fictional): `2026-10-06-website-services-page.md`

## Frontmatter for files here
```
---
type: source
kind: other
date: {{YYYY-MM-DD}}
permission: {{public-ok | ask | private}}
---
```

## Who writes
The <<LEAD_NAME>> (<<LEAD_SHORT>>) only.

## Who reads
The <<LEAD_SHORT>> only: during setup (to pre-fill brain drafts) and when a document changes a brain file fact.

## Rules
1. Line 1 after the frontmatter: `What it is: {{website page | bio | brand doc | other}} · From: {{link, file name, or "pasted in chat"}}`.
2. Below line 1, save the text verbatim. For a web page, save the page's main text and leave out menus, footers, and cookie notices.
3. Permission: published by the client (website, public bio) `public-ok`; unpublished (brand docs, internal docs) `ask`; confidential or under NDA `private`.
4. A link you cannot open: tell the client in 1 line and offer 2 options: paste the text, or skip. Never ask twice.
5. A newer version of a document: save it as a new file with the new date. The newest file wins; never edit the old one.
