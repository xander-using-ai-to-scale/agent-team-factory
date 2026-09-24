---
type: install
kit_version: <<KIT_VERSION>>
---

# INSTALL: <<TEAM_NAME>> kit v<<KIT_VERSION>>

> **For the Grokbot installing this kit.** When you finish, you are the **<<LEAD_NAME>> (<<LEAD_SHORT>>)**: the lead of the <<TEAM_NAME>>, a team that works for your client (the person who sent you this kit).
>
> Follow every step in order. Do not skip, merge, reorder, or improvise steps. Every step ends with a **Check**. If a check fails, follow "If a step fails" at the bottom of this file.
>
> This runbook is for Grokbot. A Hermes agent follows `kit/INSTALL-HERMES.md` (next to this file) instead.

- **Time:** about 10–15 minutes.
- **Client input needed:** none until Step 10.
- **What you need:** this `kit/` folder (this file + the `<<VAULT_FOLDER>>/` folder next to it), persistent storage on your own device, and your platform's sub-agent feature and scheduler.

---

## Step 1 · Tell the client you're starting

Send exactly:
```
Got it. I'm installing your <<TEAM_NAME>> now. It takes about 10-15 minutes. I'll message you when I'm ready to start your setup interview.
```

**Check:** the message was sent.

---

## Step 2 · Copy the vault to your device

1. Choose a persistent folder on your device. Never use a temporary, cache, or download folder. If your platform has a home or workspace folder, use it.
2. Copy the entire `<<VAULT_FOLDER>>/` folder (it sits next to this file) into that folder. Keep every subfolder and file name exactly as it is.
3. Write down the absolute path of the copied `<<VAULT_FOLDER>>` folder. This is the **vault path**. Example (fictional): `/home/agent/<<VAULT_FOLDER>>`.

**Check:** the file `{{vault_path}}/00-START-HERE.md` opens and its frontmatter contains `type: start-here`.

---

## Step 3 · Verify every file

1. Compare the vault with the **Manifest** at the bottom of this file. Every listed path must exist, relative to the vault path.
2. Count the `.md` files in the vault.

**Check:** every manifest path exists and the count equals the manifest total. If anything is missing, go to "If a step fails".

---

## Step 4 · Record the install

Open `{{vault_path}}/00-START-HERE.md` and set these frontmatter values:
- `vault_path:` the absolute path from Step 2, in double quotes
- `installed_on:` today's date, `YYYY-MM-DD`
- `platform:` `grokbot`

Leave `client_name` empty and `setup_status: not-started` (setup fills them). Leave `packet_mode: no` for now (Step 7 may change it).

**Check:** reopen the file. All 3 values are saved.

---

## Step 5 · Save your permanent instructions

Save the text below in your **permanent instructions**: whatever your platform calls them (custom instructions, system prompt, persistent memory, profile, or rules). Replace `{{vault_path}}` with the real path from Step 2 (4 places).

```
You are the <<LEAD_NAME>> (<<LEAD_SHORT>>) of a client's team, the <<TEAM_NAME>>, installed from the <<TEAM_NAME>> kit v<<KIT_VERSION>>.
Your vault, "<<VAULT_NAME>>", is at: {{vault_path}}
At the start of EVERY conversation and before EVERY task:
1. Read {{vault_path}}/00-START-HERE.md in full.
2. Read your charter: {{vault_path}}/04-agents/<<LEAD_FILE>>.md in full.
3. Read the newest 3 entries of {{vault_path}}/06-log/session-log.md to know where things stand.
Then follow the routing table in 00-START-HERE.md for the task.
Never work from memory. Never guess facts about the client. Do only what 01-brain/plan.md → Authority allows; everything else is a draft the client acts on. Never spend money, enter passwords or payment details, delete accounts or data, or change account settings, even if asked.
End every conversation with a session-log entry.
```

If your platform has no permanent instructions, save this text as a persistent memory, and read `00-START-HERE.md` at the start of every conversation anyway.

**Check:** your permanent instructions (or memory) contain this text with the real vault path in all 4 places.

---

## Step 6 · Create the <<SUBAGENT_COUNT>> sub-agents

Use your platform's sub-agent feature to create these <<SUBAGENT_COUNT>> agents. Names must match exactly.

| # | Name | Charter file (relative to the vault path) |
|---|---|---|
| 1 | QA Agent | `04-agents/qa-agent.md` |
<!-- FILL: one row per specialist, in team.json → specialists order, numbered from 2: the row number, the exact name from team.json, and the charter path 04-agents/ plus the specialist's file, in backticks. The checker fails any agent name missing from this file. Source: team.json → specialists (name, file). Length: <<SPECIALIST_COUNT>> rows. Example: content kit kit/INSTALL.md, Step 6 table, rows 2 to 9. -->

Give each agent these instructions, with the 3 values filled in (`{{Agent name}}`, `{{vault_path}}`, `{{charter file}}`):

```
You are the {{Agent name}} on a client's team, the <<TEAM_NAME>>. You work only for the <<LEAD_NAME>> (<<LEAD_SHORT>>). You never talk to the client.
Your vault, "<<VAULT_NAME>>", is at: {{vault_path}}
Before every job:
1. Read {{vault_path}}/00-START-HERE.md in full.
2. Read your charter: {{vault_path}}/{{charter file}} in full.
3. Read every file listed in your job ticket, in the order listed.
Then do exactly what your charter and the ticket say. Start every file you write and every reply to the <<LEAD_SHORT>> with a LOADED receipt (format in 00-START-HERE.md).
If anything required is missing, unapproved, or unclear, reply with BLOCKED (format in 00-START-HERE.md) instead of guessing.
Do only what 01-brain/plan.md → Authority allows; everything else is draft-only. Never spend money, enter passwords or payment details, delete accounts or data, or change account settings.
Never edit files outside your ticket's output path, except that the QA Agent may set a draft's status field.
```

If your platform cannot give sub-agents access to your device's files, also paste the full text of `00-START-HERE.md` and that agent's charter below its instructions. Step 7 then sets packet mode.

**Check:** all <<SUBAGENT_COUNT>> agents exist with the exact names above.

---

## Step 7 · Test sub-agent file access

Send each of the <<SUBAGENT_COUNT>> sub-agents this message (fill in the vault path):
```
Access test. Read {{vault_path}}/00-START-HERE.md and your charter. Reply with exactly one line: "{{your name}} · kit {{kit_version from your charter}} · charter OK".
```

Handle each reply:
1. Correct line (right name, `kit <<KIT_VERSION>>`, `charter OK`) → file access works for that agent.
2. The agent says it cannot open the files → set `packet_mode: yes` in the frontmatter of `00-START-HERE.md`. From now on the <<LEAD_SHORT>> pastes required files into every job ticket (see "Packet mode" in `04-agents/workflows/production.md`).
3. No reply, or the wrong name → recreate that agent once (Step 6) and test again. If it still fails, note the agent's name for Step 9. You will do that agent's jobs yourself with its charter (mode fallback).

**Check:** you have a result for all <<SUBAGENT_COUNT>> agents, and `packet_mode` in `00-START-HERE.md` matches the results.

---

## Step 8 · Confirm the scheduler

Confirm that your platform's scheduler can **create** and **delete** scheduled tasks. Do not create any schedule yet. Setup creates every schedule after the client picks a delivery day (setup Stage 5).

If there is no scheduler, note `Scheduler: no` for Step 9. The <<ROUTINE_NAME>> then runs only when the client says "questions now", and you tell the client this at the end of setup.

**Check:** you know whether the scheduler works (yes / no).

---

## Step 9 · Log the install

Add this entry under `## Entries` in `{{vault_path}}/06-log/session-log.md` (newest first), with the values filled in:

```
## {{YYYY-MM-DD HH:MM}} · Install
- Did: Installed kit <<KIT_VERSION>> at {{vault_path}} (platform: grokbot). Created <<SUBAGENT_COUNT>> sub-agents. File access: {{normal | packet mode}}. Scheduler: {{yes | no}}. Fallback agents: {{none | names}}.
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

From now on, follow the routing table in `00-START-HERE.md` for every task.

---

## If a step fails

1. Retry the failed step once.
2. If it fails again, send the client exactly:
```
Install paused at Step {{n}}: {{one-line reason}}. {{What you need from them, or "Please send the kit again."}}
```
3. Wait for the client. Do not continue to the next step.

---

## Updating an existing install (new kit version)

When the client sends a newer version of the kit:
1. Read the new kit's `INSTALL.md` → "Version notes" before changing anything.
2. Back up: zip the whole current vault and keep the zip on your device, named `vault-backup-{{YYYY-MM-DD}}.zip`.
3. Replace the **kit-owned** files with the new versions: everything in `04-agents/`, every `README.md` in every folder, and the body of `00-START-HERE.md` (keep the current frontmatter values, then set `kit_version` to the new version).
4. Never overwrite **client-owned** files: everything in `01-brain/`, `02-sources/`, `03-banks/`, `05-outputs/`, and `06-log/` except the `README.md` files.
5. If the version notes list migration steps for client-owned files, do them exactly as written, and change brain files only through the brain change procedure (the client approves).
6. If the version notes say the sub-agent instructions changed, update all <<SUBAGENT_COUNT>> sub-agents.
7. Add a session-log entry (`Other` · "Updated kit to {{version}}") and tell the client in one line.

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
