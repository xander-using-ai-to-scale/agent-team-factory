---
type: readme
kit_version: <<KIT_VERSION>>
---

# hermes-skills: one Hermes skill per agent

This folder is for installing the <<TEAM_NAME>> kit on Hermes Agent. A Grokbot install never uses it. `kit/INSTALL-HERMES.md` is the only file that reads it.

## What is here

1. This README.
2. One folder per agent, named after the agent's charter file without `.md`: `<<LEAD_FILE>>/` for the <<LEAD_NAME>>, `qa-agent/` for the QA Agent, and one folder per specialist.
3. One SKILL.md file in each folder. Nothing else.

The table in `kit/INSTALL-HERMES.md` → Step 6 lists every agent with its skill name and folder. That table is the list; this README does not repeat it.

## What each SKILL.md does

A Hermes skill is a short procedure that Hermes loads by name. Each SKILL.md in this folder:
1. Names one agent. Its frontmatter `name` is `<<TEAM_SLUG>>-` followed by the folder name, and its `description` starts with "Use when" (60 characters or less).
2. Tells that agent where the vault is and what to read before any work: `00-START-HERE.md`, then its charter, then every file in its job ticket, in order (the <<LEAD_NAME>>: the newest 3 session-log entries and the routing-table row for the task instead of a ticket).
3. Repeats the hard limits: the LOADED receipt first, BLOCKED instead of guessing, only the <<LEAD_SHORT>> talks to the client, and nothing beyond `01-brain/plan.md` → Authority.

The <<LEAD_NAME>>'s skill also points to `kit/INSTALL-HERMES.md` Step 6 (sending jobs to subagents) and Step 8 (scheduled tasks).

## How INSTALL-HERMES.md uses this folder

1. Step 2 copies this folder, with the rest of `kit/`, into a persistent folder on the client's machine.
2. Step 6 reads each SKILL.md, replaces `{{vault_path}}` and `{{kit_path}}` with the real paths, and creates the skill with Hermes's `skill_manage` tool, in the `<<TEAM_SLUG>>` category.
3. Step 6 also defines the instruction block that goes into every job sent to a subagent. The block names the agent's skill, and it works even when a subagent cannot load skills.
4. Step 7 tests whether a subagent can load the QA Agent's skill.
5. Step 8 attaches the <<LEAD_NAME>>'s skill to every scheduled task, when the skills are installed.
6. "Updating an existing install" re-creates every skill from the new version of this folder.

## The vault stays the single source of truth

The skills add no team rules of their own: they repeat a few hard limits and point to the vault (`<<VAULT_FOLDER>>/`). The rules live in `00-START-HERE.md`, each agent's job lives in its charter in `04-agents/`, and the client's facts live in the brain files. To change how an agent works, change its charter in the vault, never its SKILL.md. If a skill and a vault file ever disagree, the vault file wins.

## Rules for this folder

1. One folder per agent in `team.json`: the <<LEAD_NAME>>, the QA Agent, and every specialist. No other folders. The kit checker fails a missing SKILL.md.
2. Keep `{{vault_path}}` and `{{kit_path}}` in every SKILL.md exactly as written. The install fills them in on the client's machine.
3. Never edit a SKILL.md for one client. Kit updates replace this whole folder.
4. Every Hermes tool, command, and path these files use comes from the factory's verified Hermes notes. Add no other Hermes feature.
