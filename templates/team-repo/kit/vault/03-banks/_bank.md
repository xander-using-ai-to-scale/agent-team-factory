---
type: bank
name: "<!-- FILL: replace the quotes and this comment with this bank's file name without .md, from team.json banks[].file, for example proof. Source: team.json banks[].file. Example: kit/The-Almanac/03-banks/proof.md frontmatter (name: proof). -->"
next_id: X-001
updated: ""
---
<!-- FILL: replace every "X-" in this file (next_id above, How to add an entry step 5, and the entry format) with this bank's id_prefix from team.json followed by a hyphen, for example "P-", then delete this comment. Source: team.json banks[].id_prefix. Example: kit/The-Almanac/03-banks/proof.md frontmatter (next_id: P-001). -->

# <!-- FILL: this bank's title from team.json banks[].title, for example Proof. Source: team.json banks[].title. Example: kit/The-Almanac/03-banks/proof.md line 8 (# Proof). -->

<!-- FILL: 2 lines. Line 1: what one entry is and what makes an item qualify, in one sentence, for example "Verifiable evidence behind the client's claims: results, testimonials, numbers, credentials.". Line 2: which outputs draw from this bank and the one rule that matters most when using it. Source: team.json banks[].title; TEAM-SPEC banks. Length: max 40 words. Example: kit/The-Almanac/03-banks/proof.md lines 10 to 11. -->

## How to add an entry
1. Read `next_id` in the frontmatter. That is the new entry's ID.
2. Copy the entry format below.
3. Fill every field. Write `none` for an empty field; never leave a `{{...}}` placeholder.
4. Put the entry at the top of `## Entries`, directly under the comment line.
5. Increase `next_id` by 1, keeping 3 digits: `X-009` becomes `X-010`.
6. Set `updated` to today's date (YYYY-MM-DD).

## Entry format
```
### X-001 · {{short title}}
- Date: {{YYYY-MM-DD, the day you filed it}}
<!-- FILL: the bank-specific fields, 2 to 6 lines, each "- <Field>: {{allowed values or what to write}}", for example "- Type: {{testimonial | result | metric | credential}}" and "- Exact wording or number: "{{verbatim}}"". Include a field for the client's own words, copied verbatim, when this bank holds them. Source: TEAM-SPEC banks; team.json banks. Length: 2 to 6 lines. Example: kit/The-Almanac/03-banks/stories.md and kit/The-Almanac/03-banks/proof.md ## Entry format. -->
- Source: {{wikilink to the source file | client said in chat YYYY-MM-DD}}
- Permission: {{public-ok | ask | private}}
- Names: {{none | every person, client, or company named or identifiable}}
- Status: {{active | archived YYYY-MM-DD}}
- Used in: {{none | output_id (output labels)}}
```

## Rules
1. `Source`: a wikilink to the source file (full vault path, no `.md`), or `client said in chat YYYY-MM-DD` for a typed chat message.
2. A field that quotes the client or a source holds the words verbatim: never fix, trim, or paraphrase them.
3. Permission defaults: the client's own experience with no third-party names and no confidential numbers `public-ok`; any third-party name, client result, or confidential detail `ask`; anything the client says is off the record `private`. Never more open than the source file's `permission`.
4. `Names`: every person, client, and company named or identifiable; `none` if none. After the client answers the permission message ([[03-banks/README]]), add `(names: OK)` or `(names: leave out)` at the end: "yes" = `(names: leave out)` (use the entry, never the names); "yes names ok" = `(names: OK)`.
5. Only `public-ok` entries go into outputs. `ask` entries wait for the client's yes in the batched message; `private` entries never go into outputs.
6. `Used in`: after each delivery, add `{{output_id}} ({{output labels}})` at the front, separated by `; `. Use the output labels in [[03-banks/README]]. List only delivered work, never held-back files.
   Example (fictional): `2026-10-26-bank-referral-habits (article); 2026-10-12-spring-price-update (article, email)`
7. Before adding, search the entries for the same item. If it exists, keep the first entry and add nothing.
8. To retire an entry, set its `Status` to `archived YYYY-MM-DD`. Never delete an entry. Never use an archived entry.
<!-- FILL: the bank-specific rules, numbered from 9: (a) what qualifies for this bank, with 1 fictional example and 1 fictional non-example; (b) any extra condition before use, for example "Verified by client: yes"; (c) this bank's own Status values when it needs more than active and archived (for example new, used, parked), with when each applies, after replacing "active" in the Status line of the entry format; (d) the reuse rule: how many days must pass before an entry goes into another <<OUTPUT_UNIT>>, with the "(repeat ok)" exception, or "Entries may be reused in any <<OUTPUT_UNIT>>."; (e) permission defaults per entry type that differ from rule 3. Source: TEAM-SPEC banks; team.json banks. Length: 2 to 6 rules. Example: kit/The-Almanac/03-banks/stories.md ## Rules 1, 7, 9 and kit/The-Almanac/03-banks/proof.md ## Rules 4 to 8. -->

## Entries
<!-- Newest first. No entries yet. -->
