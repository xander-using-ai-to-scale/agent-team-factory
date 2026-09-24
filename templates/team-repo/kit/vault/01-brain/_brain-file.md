---
type: brain
file: "<!-- FILL: replace the quotes and this comment with this file's name without .md, from team.json brain_files[].file, for example site. Source: team.json brain_files[].file. Example: kit/The-Almanac/01-brain/customer.md frontmatter (file: customer). -->"
version: 0
status: empty
updated: ""
approved_on: ""
kit_version: <<KIT_VERSION>>
---

# <!-- FILL: this file's title from team.json brain_files[].title, for example Site. Source: team.json brain_files[].title. Example: kit/The-Almanac/01-brain/customer.md line 11 (# Customer). -->

Holds <!-- FILL: what this file holds in one phrase that names every section in plain words, in order, for example "the pages that matter, the keywords we target, and our competitors". Source: team.json brain_files[].sections; TEAM-SPEC brain files. Length: max 40 words. Example: kit/The-Almanac/01-brain/customer.md line 13. -->. The <<LEAD_NAME>> (<<LEAD_SHORT>>) fills it during setup from the interview and any optional drops.
Read by <!-- FILL: every agent whose routing row lists this file, in plain words, for example "the <<LEAD_SHORT>>, the Article Agent, and the QA Agent". Source: 00-START-HERE §4 rows that list this file. Example: kit/The-Almanac/01-brain/customer.md line 14. --> (which sections: routing table in [[00-START-HERE]]). Read-only: sub-agents never edit it, and after approval the <<LEAD_SHORT>> changes it only through [[04-agents/workflows/learning-loop#Brain change procedure]].

<!-- Fill rules (<<LEAD_SHORT>>): write only facts the client confirmed. Unknown → log a Q-### in [[06-log/open-questions]], write UNKNOWN (Q-###) in the field, add its pointer under ## Open questions; a section below its minimum count gets a Q-### too. Never guess.
Replace every {{placeholder}}. A placeholder holding a value, like {{no}} or {{1}}, is the default: confirm it with the client, then drop the braces. Delete unused template rows and blocks. Empty list → "- none"; empty table → one row with none in the first cell. Never edit guidance comments; {{ }} inside them are format examples.
Set status: draft when you start filling; status: approved needs the client's OK and zero {{ }} outside comments. Agents: UNKNOWN is not a fact; never fill it in; if your job needs it, reply BLOCKED. -->

## TL;DR
<!-- Agents read this first. The <<LEAD_SHORT>> writes it last, from the sections below, and updates it in the same edit as any change to this file. Max 10 lines (this comment not counted); no {{ }} once approved. -->
<!-- FILL: two parts. (1) Insert a second line into the guidance comment above, before its closing marker: Example (fictional). Good: "<one specific TL;DR line for this file>". Bad: "<the same line written vaguely>". (2) Replace this comment with 4 to 9 TL;DR lines, one per fact most jobs need from this file, each "- <Label>: {{placeholder_in_snake_case}}", drawn from the sections below. Source: team.json brain_files[].sections; TEAM-SPEC brain files and reading lists. Length: max 10 lines, max 75 words. Example: kit/The-Almanac/01-brain/customer.md ## TL;DR. -->

<!-- FILL: one section per entry in this file's team.json sections, in team.json order. For each: (1) "## <Section>" exactly as written in team.json. (2) On the next line, a guidance comment: what goes here and from which interview answers or drops, a count range (for example 3–7 items), what makes an item testable, and a last line "Example (fictional). Good: "<a specific item>" Bad: "<a vague item>"", with no em dashes and no real people or companies. (3) A placeholder body of bullets, a numbered list, or a table, with {{snake_case}} placeholders and 2 to 5 placeholder rows. Source: team.json brain_files[].sections; TEAM-SPEC brain files; Team Brief field 6 (Knowledge). Length: 3 to 12 body lines per section. Example: kit/The-Almanac/01-brain/customer.md ## Pains, ## Objections, and ## Exact language. -->

## Open questions
<!-- Pointers only: each question lives in [[06-log/open-questions]], which is always the full list. Update pointers only while drafting in setup or inside an approved brain change. "- none" when empty.
Example (fictional). Good: "- Q-007 · Who approves work when the owner is away? (see [[06-log/open-questions]])". Bad: "- approver??". -->
- Q-### · {{question}} (see [[06-log/open-questions]])

## Changelog
<!-- Newest first, one line per version; never edit old lines. Format: - vN · YYYY-MM-DD · {{change}} ({{E-### | client request | setup}}); client request = any other change the client approved (monthly review, post-delivery proposals, answered questions).
Every approved version: version +1, updated and approved_on = that date, one line here.
Example (fictional). Good: "- v2 · 2026-10-20 · Added 2 rows to the first section (client request)". Bad: "- updated stuff". -->
- v0 · template · installed from kit <<KIT_VERSION>>
