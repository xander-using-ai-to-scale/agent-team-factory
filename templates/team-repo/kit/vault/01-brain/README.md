---
type: readme
folder: 01-brain
kit_version: <<KIT_VERSION>>
---

# 01-brain: What we know

## Purpose
The <<BRAIN_FILE_COUNT>> brain files hold the stable, client-approved facts every piece of work is built from. Agents work only from these files, the banks in `03-banks/`, and the sources in `02-sources/`. A fact that is in none of them must never appear in a draft.

## What lives here
- [[01-brain/company]]: what the business sells, who it serves, how it makes money, what it believes, what makes it different, key facts.
- [[01-brain/voice]]: how the client sounds and never sounds, banned words, formatting habits, spoken and written samples, learned rules.
- [[01-brain/plan]]: goal, outputs and quantities, rhythm, delivery, authority, team and handoff, areas to avoid.
<!-- FILL: one bullet per domain brain file, in team.json order: "- [[01-brain/<file stem>]]: <its sections in plain words, lowercase, comma-separated>." When team.json appends domain sections to company.md, voice.md, or plan.md, add them in plain words to the end of that file's bullet above. Delete this comment when there is nothing to add. Source: team.json brain_files (file, sections, core). Length: 1 line per file. Example: kit/The-Almanac/01-brain/README.md ## What lives here (the customer and offer bullets). -->

## What never goes here
- Raw material (interview answers, <<ROUTINE_NAME>> answers, transcripts, documents, website text) → `02-sources/`, saved verbatim.
- Bank entries → `03-banks/`. Brain files point to them by ID and never copy their text.
- Drafts, job tickets, and <<OUTPUT_UNIT_PLURAL>> → `05-outputs/`.
- Edits, winners, open questions, and session history → `06-log/`.

## Who writes
- Only the <<LEAD_NAME>> (<<LEAD_SHORT>>), and only with the client's approval: the whole file at the end of its setup section, then every exact change after that.
- Every fact comes from the client. Unknown → log a Q-### in [[06-log/open-questions]] and write UNKNOWN (Q-###) in the field. Never guess.
- Sub-agents never edit brain files. A sub-agent that finds a gap or an error says so in its reply to the <<LEAD_SHORT>>.

## Who reads
- Everyone, following their row in the routing table in [[00-START-HERE]]: "(full)" = the whole file; "(sections: …)" = `## TL;DR` plus the named sections only.
- [[01-brain/company]]: every specialist reads at least its TL;DR (business name, founder, what it sells, core belief); the QA Agent reads Key facts to check names and credentials. The routing rows R12 and up name the specialists that read more.
- [[01-brain/voice]]: every specialist and the QA Agent read it in full.

## Statuses

| Status | Meaning | Agents may use it |
|---|---|---|
| `empty` | Kit template, nothing filled | No |
| `draft` | Filled by the <<LEAD_SHORT>>, not yet approved by the client | No |
| `approved` | The client approved the current version | Yes |

Production gate: no <<OUTPUT_UNIT>> is produced until all <<BRAIN_FILE_COUNT>> brain files are `approved` and `setup_status` is `complete` in `00-START-HERE.md`. A sub-agent handed a brain file that is not `approved` replies BLOCKED.

## Versions and changelog
- `version`: 0 = template, 1 = first client approval, +1 for every approved change after that.
- `updated`: the date of the last change. `approved_on`: the date the client approved the current version.
- Each file ends with `## Open questions` (pointers to [[06-log/open-questions]]), then `## Changelog`, newest first: `- vN · YYYY-MM-DD · what changed (E-### | client request | setup)`.
- In this folder a kit update replaces only this README; it never overwrites the <<BRAIN_FILE_COUNT>> brain files.

## How to change a brain file
Follow [[04-agents/workflows/learning-loop#Brain change procedure]] for every change, whatever the reason: propose the exact change (before → after), get the client's approval, apply it, add 1 to `version`, add the changelog line, log the session. Never edit a brain file without approval.

## The TL;DR rule
- Every brain file starts with `## TL;DR`: max 10 lines, written last, and updated in the same edit as any change to the file.
- Session start reads only the TL;DRs, and every "(sections: …)" read includes the TL;DR, so it must carry the facts most jobs need.
- An approved file has zero `{{placeholders}}` outside guidance comments, the TL;DR included.
