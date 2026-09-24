---
type: readme
folder: 04-agents/question-banks
kit_version: <<KIT_VERSION>>
---

# Question banks

## Purpose
<!-- The exact question text the <<LEAD_NAME>> uses with the client. Workflows say when to ask; these banks say what to ask. -->
This folder holds every question the <<LEAD_NAME>> asks the client: the one-time setup interview and the recurring <<ROUTINE_NAME>> questions. The workflows decide when a bank is used; the banks hold the wording, the order, the follow-ups, and the rules for picking and personalizing questions.

## What lives here
| File | Used by | Holds |
|---|---|---|
| `04-agents/question-banks/setup-interview.md` | `04-agents/workflows/setup.md` | Interview rules; the core questions for Company, for each domain brain file, for Voice (with the 60-second voice memo and the this-or-that calibration), and for Plan (with the outputs and authority proposals); the pushback round; the coverage map; the deep-dive bank |
| `04-agents/question-banks/routine-questions.md` | `04-agents/workflows/routine.md` | Picking rules, personalization rules, the categories of question templates, the answer instructions block, fictional example messages |

## Who uses it
1. The <<LEAD_NAME>> only. It reads a bank when its routing row says so: R2 for [[04-agents/question-banks/setup-interview]], R3 for [[04-agents/question-banks/routine-questions]].
2. Sub-agents never read these files and never ask the client anything. Only the <<LEAD_NAME>> talks to the client.

## How the two banks differ
1. Setup interview: runs once, during [[04-agents/workflows/setup]], about 45-60 minutes (30-45 core questions). It fills the <<BRAIN_FILE_COUNT>> brain files in `01-brain/`. The <<LEAD_SHORT>> asks only what is still unknown, one question per message. The only repeat is "redo {{section}}".
2. Recurring questions: every cycle of the <<ROUTINE_NAME>>, at the cadence in [[01-brain/plan#Rhythm]], run by [[04-agents/workflows/routine]]. The questions go out in one message the day before delivery day. Each set is built from templates and personalized with the client's own words. It feeds one <<OUTPUT_UNIT>>.

## Editing rules
1. Both banks are kit-owned. A kit update replaces them. Never write client answers, client names, or client-specific wording into this folder.
2. Setup answers go to `02-sources/interview/` (verbatim). Answers to the <<ROUTINE_NAME>> questions go to `02-sources/routine-answers/` (verbatim).
3. Client-specific questions for the <<ROUTINE_NAME>> are generated fresh each cycle from the templates and logged in `06-log/questions-asked.md`. Never add them to [[04-agents/question-banks/routine-questions]].
4. The <<LEAD_NAME>> never edits this folder. Question changes for every client come only through a new kit version.
