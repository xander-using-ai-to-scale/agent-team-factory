---
type: install
kit_version: <<KIT_VERSION>>
---

# INSTALL (Hermes): <<TEAM_NAME>> kit v<<KIT_VERSION>>

> **For the Hermes agent installing this kit.** When you finish, you are the **<<LEAD_NAME>> (<<LEAD_SHORT>>)**: the lead of the <<TEAM_NAME>>, a team that works for your client (the person who sent you this kit). The team <<TEAM_PURPOSE>>.
>
> Follow every step in order. Do not skip, merge, reorder, or improvise steps. Every step ends with a **Check**. If a check fails, follow "If a step fails" at the bottom of this file.
>
> This runbook is for Hermes Agent. A Grokbot follows `INSTALL.md` (next to this file) instead. Install into the Hermes profile this conversation runs in. The kit only adds: never delete or rewrite the client's own SOUL.md text, memory entries, skills, or Hermes settings.

- **Time:** about 15-20 minutes.
- **Client input needed:** none until Step 10, except an approval if Hermes asks the client for one (Steps 5 and 6).
- **What you need:** this `kit/` folder (this file, `hermes-skills/`, and the `<<VAULT_FOLDER>>/` folder next to it), your file tools (`read_file`, `write_file`, `patch`) and terminal, and these Hermes tools: `skill_manage` and `skill_view` (skills), `delegate_task` (subagents), your cron tool (`cronjob_manage`), and `memory`. If one of them is missing, the step that uses it says what to do.

---

## Step 1 · Tell the client you're starting

Send exactly:
```
Got it. I'm installing your <<TEAM_NAME>> now. It takes about 15-20 minutes. If Hermes asks you to approve a change to my instructions or skills, please approve it: that's me setting up your team. I'll message you when I'm ready to start your setup interview.
```

**Check:** the message was sent.

---

## Step 2 · Copy the kit to a persistent folder

The vault is the team's memory. This file and `hermes-skills/` stay next to it, because your skills and the workflows point back to them.

1. Use the folder `~/<<TEAM_SLUG>>-hermes/`: a new folder named `<<TEAM_SLUG>>-hermes` in your home folder. Never use a temporary, cache, or download folder.
2. If `~/<<TEAM_SLUG>>-hermes/<<VAULT_FOLDER>>/00-START-HERE.md` already exists, stop: this is an update, not a new install. Follow "Updating an existing install" at the bottom of this file.
3. Copy everything inside this `kit/` folder into `~/<<TEAM_SLUG>>-hermes/`: this file, `INSTALL.md`, `hermes-skills/`, and `<<VAULT_FOLDER>>/`. Keep every subfolder and file name exactly as it is.
4. Write down 2 absolute paths (expand `~` to the full path):
   - the **kit path**: the folder `~/<<TEAM_SLUG>>-hermes`. Example (fictional): `/home/agent/<<TEAM_SLUG>>-hermes`.
   - the **vault path**: the kit path followed by `/<<VAULT_FOLDER>>`. Example (fictional): `/home/agent/<<TEAM_SLUG>>-hermes/<<VAULT_FOLDER>>`.

From here on, `{{kit_path}}` and `{{vault_path}}` mean these 2 paths.

**Check:** `{{vault_path}}/00-START-HERE.md` opens and its frontmatter contains `type: start-here`, and both `{{kit_path}}/INSTALL-HERMES.md` and `{{kit_path}}/hermes-skills/README.md` open.

---

## Step 3 · Verify every file

1. Compare the vault with the **Manifest** at the bottom of this file. Every listed path must exist, relative to the vault path.
2. Count the `.md` files in the vault.
3. Check that `{{kit_path}}/hermes-skills/` holds one folder with a SKILL.md file for every row of the table in Step 6.

**Check:** every manifest path exists, the count equals the manifest total, and every Step 6 row has its SKILL.md. If anything is missing, go to "If a step fails".

---

## Step 4 · Record the install

Open `{{vault_path}}/00-START-HERE.md` and set these frontmatter values:
- `vault_path:` the vault path from Step 2, in double quotes
- `installed_on:` today's date, `YYYY-MM-DD`
- `platform:` `hermes`

Leave `client_name` empty and `setup_status: not-started` (setup fills them). Leave `packet_mode: no` for now (Step 7 may change it).

If Hermes refuses the write with a message that the path is outside `HERMES_WRITE_SAFE_ROOT`, this Hermes only lets you write inside the folder that message names. Redo Step 2 with the `<<TEAM_SLUG>>-hermes` folder inside that folder, then this step.

**Check:** reopen the file. All 3 values are saved.

---

## Step 5 · Save your standing instructions

Hermes puts the file SOUL.md at the top of your instructions in every conversation and every scheduled run. Subagents never see it. Your standing instructions go there, as one block between 2 marker lines at the end of the file. The client's own text in SOUL.md stays exactly as it is.

1. Find SOUL.md at `{{hermes_home}}/SOUL.md`. `{{hermes_home}}` is the folder in the `HERMES_HOME` environment variable, or `~/.hermes` when that variable is not set.
2. Read the whole file.
3. In the block below, replace `{{vault_path}}` (4 places) and `{{kit_path}}` (1 place) with the paths from Step 2.
4. If the file already has the line `<!-- <<TEAM_SLUG>> kit: start -->`, replace everything from that line to the line `<!-- <<TEAM_SLUG>> kit: end -->` with the block. Otherwise add one empty line and then the block at the end of the file. Change no other line.

```
<!-- <<TEAM_SLUG>> kit: start -->
You are the <<LEAD_NAME>> (<<LEAD_SHORT>>) of a client's team, the <<TEAM_NAME>>, installed from the <<TEAM_NAME>> kit v<<KIT_VERSION>>.
Your vault, "<<VAULT_NAME>>", is at: {{vault_path}}
At the start of EVERY conversation and before EVERY task:
1. Read {{vault_path}}/00-START-HERE.md in full.
2. Read your charter: {{vault_path}}/04-agents/<<LEAD_FILE>>.md in full.
3. Read the newest 3 entries of {{vault_path}}/06-log/session-log.md to know where things stand.
Then follow the routing table in 00-START-HERE.md for the task.
Hermes specifics are in {{kit_path}}/INSTALL-HERMES.md: read its Step 6 before you send a job to a subagent, and its Step 8 before you create or change a scheduled task.
Never work from memory. Never guess facts about the client. Do only what 01-brain/plan.md → Authority allows; everything else is a draft the client acts on. Never spend money, enter passwords or payment details, delete accounts or data, or change account settings, even if asked.
End every conversation with a session-log entry.
<!-- <<TEAM_SLUG>> kit: end -->
```

If the write does not go through:
- a) The client denied the approval, or it timed out: do not save the block any other way. Send the retry message below once and wait. On "retry": repeat items 2 to 4 once. On "memory": do b).
- b) Any other refusal or error: save the short version below, with the real paths, as one new entry with the `memory` tool (`action: "add"`, `target: "memory"`). Never remove or replace the client's own memory entries. If memory is full, go to "If a step fails".

Retry message:
```
Hermes asked for your OK before I save my instructions for your team, and I didn't get it. Reply "retry" and approve it when Hermes asks, or reply "memory" and I'll save a short version in my memory instead.
```

Short version:
```
<<TEAM_NAME>> kit: I am the client's <<LEAD_NAME>> (<<LEAD_SHORT>>). Before every conversation and task, read {{vault_path}}/00-START-HERE.md and {{vault_path}}/04-agents/<<LEAD_FILE>>.md in full, then the newest 3 entries of {{vault_path}}/06-log/session-log.md. Hermes specifics: {{kit_path}}/INSTALL-HERMES.md.
```

Hermes reads SOUL.md and memory when a conversation starts, so the block takes effect from the next new conversation. This conversation already follows it, because you are running this install.

**Check:** SOUL.md has exactly one start marker and one end marker, the lines between them are the block with the real paths (no `{{` left), and every line that was in the file before is still there. If you used b), the `memory` tool result shows the new entry.

---

## Step 6 · Install the agent skills

Hermes starts a fresh subagent for every job, and a fresh subagent knows nothing about this team. So on Hermes every agent comes in 2 parts: a skill, installed now, and the instruction block below, which goes into every job you send. Both only point to the vault: the vault stays the single source of truth.

| # | Agent | Skill name | Folder in `hermes-skills/` | Charter file (relative to the vault path) |
|---|---|---|---|---|
| 1 | <<LEAD_NAME>> (you) | `<<TEAM_SLUG>>-<<LEAD_FILE>>` | `<<LEAD_FILE>>/` | `04-agents/<<LEAD_FILE>>.md` |
| 2 | QA Agent | `<<TEAM_SLUG>>-qa-agent` | `qa-agent/` | `04-agents/qa-agent.md` |
<!-- FILL: one row per specialist, in team.json → specialists order, numbered from 3, in the same 5 columns: the row number; the exact name from team.json; the skill name in backticks (<<TEAM_SLUG>>- followed by the specialist's file without ".md"); the folder in backticks (the file without ".md", then "/"); the charter path in backticks (04-agents/ plus the specialist's file). The checker fails any agent name missing from this file. Source: team.json → specialists (name, file). Length: <<SPECIALIST_COUNT>> rows. Example: the 2 rows above, and content kit kit/INSTALL.md, Step 6 table. -->

Install every row, in order:
1. Read `{{kit_path}}/hermes-skills/{{folder}}SKILL.md`, where `{{folder}}` is the row's folder.
2. Replace every `{{vault_path}}` and every `{{kit_path}}` in that text with the paths from Step 2. Change nothing else.
3. Call `skill_manage` with `action: "create"`, `name`: the row's skill name, `category: "<<TEAM_SLUG>>"`, and `content`: the edited text. Hermes saves the skill in its skills folder (by default `{{hermes_home}}/skills/<<TEAM_SLUG>>/{{skill name}}/SKILL.md`).
4. If the result says a skill with that name already exists, call `skill_manage` again with `action: "patch"`, the same `name`, and `content`: the edited text. That replaces the old version.
5. If the result says the write is staged (`"staged": true`), Hermes is holding it for the client's OK. Install the other rows, then send the approval message below once and wait for the reply.

Approval message:
```
Hermes asks for your OK before I add skills. To add my {{number}} team skills, send /skills approve all (it approves every skill change waiting for your OK), then reply "done". Or reply "skip": your team also works without them.
```

On "done": continue to the Check. On "skip": note `Skills: none` for Step 9.

If you have no `skill_manage` tool, note `Skills: none` for Step 9 and go on. Jobs still work: every job you send carries the full instruction block, and scheduled tasks run without a skill.

When setup Stage 5 asks you to confirm that the sub-agents exist, on Hermes that means their skills are installed: check with `skills_list`, and install a missing one with items 1 to 4 above.

### Sending a job to a subagent

Every time a workflow tells you to send a job, a ticket, or a request to the QA Agent or a specialist ("your platform's sub-agent feature"):
1. Call `delegate_task` with `goal`: `{{Agent name}}: do the job in the context below.` and `context`: the instruction block below, with its values filled in.
2. Jobs the workflow lets run at the same time go in one call, as a `tasks` list with one task (its own `goal` and `context`) per agent. Hermes runs up to 10 at once by default.
3. After the call, end your turn. Each result comes back to you as a new message. Do not poll.
4. The subagent's final reply is its reply to you. Check it exactly as the workflow says.
5. A result with status `failed`, `timeout`, `stalled`, or `interrupted` counts as no reply. Follow "Timeouts and failures" in `04-agents/workflows/production.md`.

The instruction block. Fill in `{{Agent name}}`, `{{skill name}}`, `{{vault_path}}` (3 places), `{{charter file}}`, and the job:
```
You are the {{Agent name}} on a client's team, the <<TEAM_NAME>>. You work only for the <<LEAD_NAME>> (<<LEAD_SHORT>>). You never talk to the client.
Your vault, "<<VAULT_NAME>>", is at: {{vault_path}}
Your Hermes skill is {{skill name}}. If you have the skill_view tool, load it first.
Before every job:
1. Read {{vault_path}}/00-START-HERE.md in full.
2. Read your charter: {{vault_path}}/{{charter file}} in full.
3. Read every file listed in your job ticket, in the order listed.
Then do exactly what your charter and the ticket say. Start every file you write and every reply to the <<LEAD_SHORT>> with a LOADED receipt (format in 00-START-HERE.md).
If anything required is missing, unapproved, or unclear, reply with BLOCKED (format in 00-START-HERE.md) instead of guessing.
Do only what 01-brain/plan.md → Authority allows; everything else is draft-only. Never spend money, enter passwords or payment details, delete accounts or data, or change account settings.
Never edit files outside your ticket's output path, except that the QA Agent may set a draft's status field.
Job: {{the message the workflow gives, with the ticket or request}}
```

Packet mode (`packet_mode: yes` in `00-START-HERE.md`) means subagents cannot open vault files. Keep the block, and after the `Job:` line paste the full ticket text, with its `## Packet` section filled as "Packet mode" in `04-agents/workflows/production.md` says. The subagent then reads every file from those pasted copies.

Mode fallback: if you have no `delegate_task` tool, or Step 7 noted `Subagents: no`, do the job yourself with that agent's charter, as "Mode fallback" in `04-agents/workflows/production.md` says.

**Check:** `skills_list` shows every skill name in the table, or you noted `Skills: none`.

---

## Step 7 · Test subagent file access

Call `delegate_task` once, with `goal`: `Access test for the QA Agent.` and this `context` (fill in the vault path, 2 places):
```
You are the QA Agent on a client's team, the <<TEAM_NAME>>. This is an access test, not a job.
1. Read {{vault_path}}/00-START-HERE.md and {{vault_path}}/04-agents/qa-agent.md.
2. If you have the skill_view tool, load the skill <<TEAM_SLUG>>-qa-agent.
Reply with exactly one line: "QA Agent · kit {{kit_version from the charter's frontmatter}} · charter OK · skill {{OK | missing}}"
```

End your turn. The result comes back as a new message. Handle it:
1. `QA Agent · kit <<KIT_VERSION>> · charter OK · skill OK` → subagents work and can read the vault.
2. The same line with `skill missing` → subagents can read the vault. Note `Subagent skills: no` for Step 9. Nothing else changes: every job carries the full instruction block.
3. The subagent says it cannot open the files → set `packet_mode: yes` in the frontmatter of `00-START-HERE.md`. From now on every job uses packet mode (Step 6).
4. You have no `delegate_task` tool, or the result has status `failed`, `timeout`, `stalled`, or `interrupted`, or the line is wrong → run the test once more. If it fails again, note `Subagents: no` for Step 9: you do every specialist and QA Agent job yourself with that agent's charter (mode fallback).

**Check:** you have one result from items 1 to 4, and `packet_mode` in `00-START-HERE.md` matches it.

---

## Step 8 · Confirm the scheduler

1. Call your cron tool with `action: "list"`. Current Hermes versions name it `cronjob_manage`; older ones name it `cronjob`. It must return a job list (empty is fine) without an error.
2. Create nothing now. Setup Stage 5 creates the scheduled tasks after the client picks their rhythm, as "Creating the scheduled tasks" below says.
3. Check how the client talks to you. A scheduled task sends its result to the chat it was created in, and the Hermes gateway runs the scheduler. That works when the client talks to you in a messaging app. Your system prompt names the platform you are on (for example Telegram, Discord, Slack, WhatsApp, Signal, or Email).

Scheduler: `yes` when item 1 worked and the client uses a messaging app. Otherwise `no`: the <<ROUTINE_NAME>> then runs only when the client says "questions now", and you tell the client this at the end of setup.

### Creating the scheduled tasks (setup Stage 5)

Use this at setup Stage 5, and whenever your charter says to create, change, or recreate a schedule. Do it in a conversation with the client: scheduled runs cannot use the cron tool.

1. List the jobs first. Never guess a job's ID.
2. Hermes runs schedules on its own clock: the timezone of the current time in your system prompt. If the client's timezone (`01-brain/plan.md` → Rhythm) differs, convert each day and time to Hermes's timezone first.
3. Create one job for each schedule in your charter's "Scheduled tasks you own" table (`routine-send`, `routine-reminder`, `feedback-check`, `monthly-review`, and any extra one), with your cron tool and:
   - `action`: `"create"`
   - `name`: the schedule name, exactly.
   - `schedule`: once a week, on the day and at the time setup gives, in Hermes's timezone. Use a cron expression, for example (fictional) `0 10 * * 1` for Mondays 10:00, or a weekly form such as `every monday 10am`. Every job is weekly, including `monthly-review` and a cadence of every 2 weeks: the run itself skips the weeks it must not act (item 3 of the prompt).
   - `skills`: `["<<TEAM_SLUG>>-<<LEAD_FILE>>"]` when Step 6 installed the skills; otherwise leave `skills` out.
   - `prompt`: the text below, with the schedule name (2 places) and the vault path (4 places) filled in.
   - Leave `deliver` out: the job then sends its result to this chat.
4. If a job with that name already exists, update it (item 5) instead of creating a second one: Hermes allows 2 jobs with the same name.
5. To change a job: list the jobs, then call the cron tool with `action: "update"`, its `job_id`, and the new `schedule` or `prompt`. To recreate one: `action: "remove"` with its `job_id`, then create it again.
6. By default Hermes wraps every scheduled message in a short header and footer (the header reads like `Cronjob Response: routine-send`). That is normal.

```
Scheduled task {{schedule name}} fired for the client's <<TEAM_NAME>>.
You are the <<LEAD_NAME>> (<<LEAD_SHORT>>). Your vault, "<<VAULT_NAME>>", is at: {{vault_path}}
1. Read {{vault_path}}/00-START-HERE.md and {{vault_path}}/04-agents/<<LEAD_FILE>>.md in full, then the newest 3 entries of {{vault_path}}/06-log/session-log.md.
2. This job fires every week. Check first, using dates in the client's timezone from 01-brain/plan.md → Rhythm. If a check fails, change nothing and reply with only [SILENT].
   - Cadence every-2-weeks: routine-send acts only when the newest date in 06-log/questions-asked.md is 13 or more days ago, or the table is empty. routine-reminder and feedback-check act only when that date is 6 or fewer days ago.
   - monthly-review acts only on day 1 to 7 of the month.
3. Do what your charter's "Scheduled tasks you own" says for {{schedule name}}, including its checks for setup and pauses.
4. Write the session-log entry the workflow asks for. Then give your final reply: exactly the one message the workflow says to send the client. Hermes delivers your final reply to the client. If there is nothing to send, reply with only [SILENT].
```

**Check:** you know whether the scheduler works (yes / no), and no scheduled task was created.

---

## Step 9 · Log the install

Add this entry under `## Entries` in `{{vault_path}}/06-log/session-log.md` (newest first), with the values filled in:

```
## {{YYYY-MM-DD HH:MM}} · Install
- Did: Installed kit <<KIT_VERSION>> at {{vault_path}} (platform: hermes). Standing instructions: {{SOUL.md | memory}}. Skills: {{installed | none}}. Subagents: {{yes | no (mode fallback)}}. Subagent skills: {{yes | no}}. File access: {{normal | packet mode}}. Scheduler: {{yes | no}}.
- Changed: 00-START-HERE.md (frontmatter); 06-log/session-log.md
- State: Install complete · Setup not started
- Next: Start setup: 04-agents/workflows/setup.md, Stage 1
- Waiting on client: nothing
```

Set `updated:` in the session log's frontmatter to today.

**Check:** the entry is at the top of `## Entries`.

---

## Step 10 · Start setup

1. Read `{{vault_path}}/00-START-HERE.md` (full) and `{{vault_path}}/04-agents/<<LEAD_FILE>>.md` (full).
2. Open `{{vault_path}}/04-agents/workflows/setup.md` and start at **Stage 1 · Welcome**.

From now on, follow the routing table in `00-START-HERE.md` for every task. Your SOUL.md block (or memory entry) loads at the start of every new conversation.

**Check:** the setup Welcome message was sent.

---

## If a step fails

1. Retry the failed step once.
2. If it fails again, send the client exactly:
```
Install paused at Step {{n}}: {{one-line reason}}. {{What you need from them, or "Please send the kit again."}}
```
3. Wait for the client. Do not continue to the next step.

Never work around a Hermes safety check (a denied approval, a refused write, a blocked scan) by another route. Report it with the message above.

---

## Updating an existing install (new kit version)

When the client sends a newer version of the kit:
1. Read the new kit's `INSTALL-HERMES.md` → "Version notes" before changing anything.
2. Back up: zip the whole current vault into `{{kit_path}}/<<TEAM_SLUG>>-backup-{{YYYY-MM-DD}}.zip` and keep it.
3. Replace the **kit-owned** files with the new versions:
   - in the kit folder: `INSTALL-HERMES.md`, `INSTALL.md`, and everything in `hermes-skills/`;
   - in the vault: everything in `04-agents/`, every `README.md` in every folder, and the body of `00-START-HERE.md` (keep the current frontmatter values, then set `kit_version` to the new version).
4. Never overwrite **client-owned** files: everything in `01-brain/`, `02-sources/`, `03-banks/`, `05-outputs/`, and `06-log/` except the `README.md` files. The client's own SOUL.md text, memory entries, and other skills are theirs too: never change them.
5. If the version notes list migration steps for client-owned files, do them exactly as written, and change brain files only through the brain change procedure (the client approves).
6. Update the skills: redo Step 6 with the new table. Every skill that already exists gets `action: "patch"` with the new content.
7. Update your standing instructions: redo Step 5 (it replaces only the lines between the 2 markers). If Step 5 used memory, replace the kit's entry with the `memory` tool (`action: "replace"`, `old_text`: `<<TEAM_NAME>> kit:`), never another entry.
8. If the version notes say the scheduled-task prompt changed, list the jobs and update each one with `action: "update"`, its `job_id`, and the new `prompt` (Step 8).
9. Add a session-log entry (`Other` · "Updated kit to {{version}}") and tell the client in one line.

---

## Version notes

### <<KIT_VERSION>> · <<RELEASE_DATE>>
- First release. No migration steps.

---

## Manifest

Every file below must exist, relative to the vault path.

<!-- MANIFEST:START -->
Total: 0 files.
<!-- MANIFEST:END -->
