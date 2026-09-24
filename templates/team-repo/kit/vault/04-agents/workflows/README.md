---
type: readme
folder: 04-agents/workflows
kit_version: <<KIT_VERSION>>
---

# Workflows

## Purpose

This folder holds the 6 procedures the <<LEAD_NAME>> (<<LEAD_SHORT>>) runs. Each workflow has its own Must read list, numbered steps, and a checklist. Open the workflow that matches the trigger, read its Must read list in order, then follow its steps in order.

## The workflows

| Workflow | Trigger | Link |
|---|---|---|
| setup | Right after install; the client says `redo {{section}}` | [[04-agents/workflows/setup]] |
| routine | The `routine-send` schedule fires, or the client says `questions now` | [[04-agents/workflows/routine]] |
| production | The <<ROUTINE_NAME>> answers are processed, or the client says `bank` / `bank <<OUTPUT_UNIT>>` | [[04-agents/workflows/production]] |
| learning-loop | The client sends back an edit, says `this isn't me` or `winner`; the `feedback-check` schedule fires; any brain file change | [[04-agents/workflows/learning-loop]] |
| monthly-review | The `monthly-review` schedule fires (first delivery day of each month, after the delivery) | [[04-agents/workflows/monthly-review]] |
| on-demand | The client asks for a single piece of work, a rewrite, or a full <<OUTPUT_UNIT>> on a topic | [[04-agents/workflows/on-demand]] |

The client knows the routine as the <<ROUTINE_NAME>>. The file names and schedule names say "routine".

## A normal cycle

1. At the question time in [[01-brain/plan#Rhythm]] (by default the day before delivery day, 10:00): `routine-send` fires and the <<LEAD_SHORT>> sends the <<ROUTINE_NAME>> questions ([[04-agents/workflows/routine]]).
2. The client answers by voice note or text. No answers by the `routine-reminder` time on delivery day (by default 09:00): 1 reminder with the "bank" option.
3. The <<LEAD_SHORT>> builds the <<OUTPUT_UNIT>>: <!-- FILL: the production order in one line: the outputs in plain words in dependency order (outputs that run in parallel joined with "and"), separated by commas, then ", QA on every file". Source: team.json specialists[] (output_file, depends_on, on_demand_only false); TEAM-SPEC §12.4 ("This team's order"). Length: max 25 words. Example: kit/The-Almanac/04-agents/workflows/README.md, "A normal week", item 3 ("pillar, lead magnet, platform content, QA on every file"). --> ([[04-agents/workflows/production]]).
4. By delivery day: the <<LEAD_SHORT>> delivers the <<OUTPUT_UNIT>> in chat (plus a Google Doc when [[01-brain/plan#Delivery]] says so), then sends 1 approval message if brain changes are waiting.
5. At the `feedback-check` time (by default 3 days after delivery day, 10:00): the <<LEAD_SHORT>> asks once for edits and winners ([[04-agents/workflows/learning-loop]]).
6. The first delivery day of each month, after the delivery: the monthly review ([[04-agents/workflows/monthly-review]]).

Items 1, 2, and 5 repeat at the cadence in [[01-brain/plan#Rhythm]]: every week for `weekly`, every 2 weeks for `every-2-weeks`. All times use the client's timezone from that section. The schedule names and default times are in the schedules table of [[00-START-HERE]]; setup creates them ([[04-agents/workflows/setup]], Stage 5).

## Who runs them

1. Only the <<LEAD_SHORT>> runs workflows, as [[04-agents/<<LEAD_FILE>>]] describes.
2. Sub-agents never run a workflow. They receive job tickets (the QA Agent receives QA requests) and follow their own charters in `04-agents/`.
3. Only the <<LEAD_SHORT>> talks to the client.

## Editing rules

1. These files are kit-owned: a kit update replaces every file in this folder.
2. Never write client facts here. Client facts live in `01-brain/`, `02-sources/`, `03-banks/`, `05-outputs/`, and `06-log/`.
3. To change how a workflow behaves, update the kit (a new kit version), never the copy in the vault.
