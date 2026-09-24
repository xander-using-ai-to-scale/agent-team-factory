---
type: readme
folder: 03-banks
kit_version: <<KIT_VERSION>>
---

# 03-banks

## Purpose
Reusable material taken from the client's sources: <!-- FILL: the bank titles in team.json order, lowercase, joined with commas and a final "and", for example "ideas and proof". Source: team.json banks[].title. Example: kit/The-Almanac/03-banks/README.md ## Purpose ("stories, proof, hooks, and ideas"). -->. The banks grow with every <<ROUTINE_NAME>>, and every <<OUTPUT_UNIT>> draws from them.

## What goes here
Exactly these <!-- FILL: the number of banks in team.json, as a digit. Source: team.json banks. Example: kit/The-Almanac/03-banks/README.md ("Exactly these 4 files"). --> files. Never create another file here.
<!-- FILL: one bullet per bank, in team.json order: "- [[03-banks/<file stem>]]: <what one entry is, in one line> (<id_prefix>-###)." Source: team.json banks[].file, .title, .id_prefix; TEAM-SPEC banks. Length: 1 line per bank. Example: kit/The-Almanac/03-banks/README.md ## What goes here. -->

## What never goes here
- Whole answers, transcripts, or documents: [[02-sources/README]]. Banks hold short excerpts and a `Source` pointer.
- Stable facts about the business, the voice, or the plan: [[01-brain/README]].
- Client edits, winners, and open questions: [[06-log/README]].

## File naming
Fixed names: <!-- FILL: every bank file name in backticks, in team.json order, comma-separated, ending with a period, for example "`ideas.md`, `proof.md`.". Source: team.json banks[].file. Example: kit/The-Almanac/03-banks/README.md ## File naming. --> Never rename them.

## Frontmatter for files here
```
---
type: bank
name: {{the file name without .md}}
next_id: {{the bank's ID prefix}}-{{3 digits}}
updated: {{YYYY-MM-DD}}
---
```

## Who writes
The <<LEAD_NAME>> (<<LEAD_SHORT>>) only: after each setup section, after <<ROUTINE_NAME>> answers arrive, when logging a winner, in the monthly review, and after every delivery. Sub-agents never write here.

## Who reads
- <<LEAD_SHORT>>: every bank, in full.
<!-- FILL: one bullet per specialist, or per group of specialists with the same reading, naming the banks they read in full and the banks they read only as the entries named in their ticket, exactly as their routing rows say; then one bullet for the QA Agent naming the banks it reads in full (row R6). Source: 00-START-HERE §4 rows R6 and R12 and up. Length: 1 line per bullet. Example: kit/The-Almanac/03-banks/README.md ## Who reads. -->

## Rules
1. IDs: prefix + 3 digits, zero-padded: the first entry of a bank with prefix `X` is `X-001`. Take the new ID from `next_id`, then increase `next_id` by 1. Never reuse, renumber, or delete an ID.
2. New entries go at the top of `## Entries` (newest first). Set `updated` to today's date whenever the file changes.
3. Only entries with `Permission: public-ok` may be used in outputs. `ask` entries wait for the client's yes. `private` entries are never used in outputs. A bank's own Rules can add a condition, for example a verification field that must say yes.
4. Set each new entry's permission with its bank's defaults. An entry is never more open than its source file, and a source part marked `Private:` gives only `private` entries.
5. After each filing round, batch every new `ask` entry into 1 yes/no message, never 1 message per item. Yes: `public-ok`. No: `private`. No reply: nothing changes.
   Example (fictional): "Can I use these? 1) The warehouse move story (names a client). 2) "Orders ship in 2 days": is that exact? Reply like: 1 yes, 2 no (add "names ok" if I can use names)." A "yes" without "names ok" means the entry is used without its names: add `(names: leave out)` to its `Names` line.
6. A sub-agent uses a bank entry only if its job ticket lists that ID as allowed.
7. `Used in`: after every delivery, the <<LEAD_SHORT>> adds the `output_id` and the output labels to every entry the delivered work used, and updates `Status` where the bank's Rules say so.
8. Reuse: each bank's Rules say how soon an entry may be used again. A ticket that lists an ID followed by `(repeat ok)` overrides that wait.
9. Never delete an entry. To retire one, set its `Status` to `archived YYYY-MM-DD`. Never use an archived entry.
10. Output labels, used in `Used in` lines: the output file's name without its number and `.md` (for example article, from 01-article.md).
