# HERMES-NOTES: how a team kit runs on Hermes Agent

This file records how every team kit maps onto Hermes Agent (Nous Research), and the verified facts that mapping rests on. [FACTORY-SPEC](FACTORY-SPEC.md) §13 points here. The Hermes templates are `templates/team-repo/kit/INSTALL-HERMES.md`, `templates/team-repo/kit/hermes-skills/README.md`, `templates/team-repo/kit/hermes-skills/_agent-skill/SKILL.md`, and `templates/team-repo/BOOTSTRAP-PROMPT-HERMES.md`.

- **Checked:** 2026-09-25, against the docs at https://hermes-agent.nousresearch.com/docs/ and the `main` branch of https://github.com/NousResearch/hermes-agent (the docs source is its `website/docs/` folder).
- **Rule:** every Hermes command, tool, file path, or config key in a Hermes template appears in section 4 below, tied to a fact in section 1. Anything not listed here stays out of the templates.
- **Where docs and code disagree,** both are recorded (section 5) and the templates handle both.

---

## 1. Verified facts

Doc URLs are relative to https://hermes-agent.nousresearch.com/docs/ (for example `user-guide/features/skills` is https://hermes-agent.nousresearch.com/docs/user-guide/features/skills). Code URLs are relative to https://github.com/NousResearch/hermes-agent/blob/main/.

### Skills

- **F1.** Skills live in the profile's skills folder, `~/.hermes/skills/` (under `$HERMES_HOME` with a custom home or a named profile), laid out as `<category>/<skill-name>/SKILL.md`. Sources: `user-guide/features/skills` (Skill Directory Structure); `user-guide/profiles`.
- **F2.** SKILL.md format: YAML frontmatter with `name`, `description`, `version`, and optional `platforms`, `author`, and `metadata.hermes` (`tags`, `category`, and others), then a `#` title and the sections When to Use, Procedure, Pitfalls, Verification. Sources: `user-guide/features/skills` (SKILL.md Format); `developer-guide/creating-skills`.
- **F3.** The agent writes skills with its `skill_manage` tool: `create` (`name`, `content` = the whole SKILL.md, optional `category`), `patch` (`old_string` and `new_string`, or `content` for a full rewrite), `delete`, `write_file`, `remove_file`. Source: `user-guide/features/skills` (Agent-Managed Skills).
- **F4.** `create` refuses a name that already exists (the fix is `patch` with `content`), a description longer than 60 characters, a name that breaks `^[a-z0-9][a-z0-9._-]*$` or runs past 64 characters, and a category containing a slash. Sources: `user-guide/features/skills` (the /learn section: the 60-character description standard); code: `tools/skill_manager_tool.py`, `agent/skill_utils.py` (`SKILL_PROMPT_DESC_LIMIT = 60`).
- **F5.** `skills_list` returns each skill's name and description; `skill_view(name)` loads one skill. The system prompt carries a skills index and tells the agent to load a skill that matches its task. Sources: `user-guide/features/skills` (Progressive Disclosure); `reference/tools-reference` (skills toolset); `developer-guide/prompt-assembly`.
- **F6.** With `skills.write_approval: true`, every `skill_manage` write is staged instead of saved: the tool result carries `staged: true` and a `pending_id`, and the user approves with `/skills approve <id>` or `/skills approve all`, in the CLI or on any messaging platform. Sources: `user-guide/features/skills` (Gating agent skill writes); `reference/slash-commands`; code: `tools/skill_manager_tool.py`.
- **F7.** Skills the foreground agent creates with `skill_manage` `create` are recorded as `created_by: learn`, and the curator never stales or archives them. Skills named in a cron job are also skipped by the curator's automatic transitions. Source: `user-guide/features/curator`.
- **F8.** `hermes skills install` takes hub identifiers, GitHub paths, and http(s) URLs to a SKILL.md. No install from a local folder is documented. Sources: `reference/cli-commands` (hermes skills); `user-guide/features/skills` (Skills Hub).
- **F9.** Hermes loads project skills only from `<repo>/.hermes/skills/` or `<repo>/.agents/skills/` in a trusted repo, so a kit's `kit/hermes-skills/` folder never loads by itself. Source: `user-guide/features/skills` (Project-Local Skills).
- **F10.** When a skill loads, Hermes substitutes `${HERMES_SKILL_DIR}` and `${HERMES_SESSION_ID}` in its body, and runs inline shell snippets when `skills.inline_shell` is on. Kit skills use neither form. Source: `developer-guide/creating-skills`.

### Standing instructions: SOUL.md, memory, context files

- **F11.** SOUL.md sits in the Hermes home: `~/.hermes/SOUL.md`, or `$HERMES_HOME/SOUL.md` with a custom home or a named profile. Hermes seeds a starter file and never overwrites an existing one. Sources: `user-guide/features/personality`; `user-guide/features/context-files`.
- **F12.** SOUL.md is slot 1 of the system prompt in every session. The docs name it the surface for the agent's "persona and standing behavior" (`developer-guide/prompt-assembly`), "the Bot's persona and standing instructions" (`user-guide/bot-mode`), and "personality and instructions" (`user-guide/profiles`).
- **F13.** Subagents never get SOUL.md (`skip_context_files`). Scheduled (cron) runs do, and memory loads in cron runs too. Sources: `developer-guide/prompt-assembly`; `developer-guide/cron-internals` (Fresh Session Isolation); code: `cron/scheduler.py` (`load_soul_identity=True`).
- **F14.** Hermes builds the system prompt at session start and again after context compression, so an edit to SOUL.md or memory reaches the next session, not the running one. Gateway chats never reset on their own; `/new` (alias `/reset`) starts a fresh conversation. Sources: `user-guide/which-file-does-what`; `user-guide/profiles`; `developer-guide/prompt-assembly` (Memory snapshots); `user-guide/messaging/` (Session continuity); `reference/slash-commands`.
- **F15.** The docs say agent writes to SOUL.md always need the user's approval. On messaging platforms Hermes asks in the chat, and the user approves there (for example by replying yes or approve). Sources: `guides/use-soul-with-hermes`; `user-guide/features/context-files` (Security); `user-guide/security` (Approval Flow (Gateway/Messaging)). See U1.
- **F16.** SOUL.md is scanned for prompt-injection patterns; for the user's own SOUL.md a hit only warns. An HTML comment that contains ignore, override, system, secret, or hidden is one of the patterns. Sources: `user-guide/features/context-files` (Security); code: `tools/threat_patterns.py`.
- **F17.** The SOUL.md guide keeps file paths and project workflow out of SOUL.md and in AGENTS.md, but AGENTS.md loads only from the session's working directory (a cron job loads it only with `workdir`). Sources: `guides/use-soul-with-hermes`; `user-guide/features/context-files`; `user-guide/features/cron` (Running a job inside a project directory).
- **F18.** The `memory` tool has the actions `add`, `replace`, and `remove` (`old_text` is a unique substring of the entry) and the targets `memory` and `user`. MEMORY.md holds 2,200 characters, and a write that would overflow is refused. Entries are scanned and threat-pattern hits are blocked. The snapshot is frozen at session start. Source: `user-guide/features/memory`.
- **F19.** The memory page recommends a skill, not a memory entry, for a location that a recurring task needs. Source: `user-guide/features/memory` (Troubleshooting).

### Subagents

- **F20.** `delegate_task` spawns subagents: `goal` plus `context` for one, a `tasks` list for a batch. Up to 10 run at once by default (`delegation.max_concurrent_children`). Source: `user-guide/features/delegation`.
- **F21.** A subagent starts with a fresh conversation. Its only context is the `goal` and `context` it receives (plus the workspace's project context files, never SOUL.md). Source: `user-guide/features/delegation` (How Subagent Context Works).
- **F22.** Subagents inherit the parent's toolsets. Leaf subagents cannot call `delegate_task`, `clarify`, `memory`, `send_message`, or the cron tool. The `skills` toolset is not on that list. Sources: `user-guide/features/delegation` (Inherited Tool Access); code: `tools/delegate_tool_toolsets.py`.
- **F23.** Top-level delegations run in the background: Hermes returns a handle, the result re-enters the conversation as a new message, and the parent ends its turn instead of polling. Source: `user-guide/features/delegation` (Batch Mode Details).
- **F24.** A failed child returns status `failed` with an `error`; a child that stops making progress returns status `timeout` (a background run gets a `stalled` completion); a stopped child returns status `interrupted`. There is no wall-clock timeout by default. Source: `user-guide/features/delegation`.
- **F25.** Each subagent gets its own terminal session, so delegations pass absolute paths. Sources: `user-guide/features/delegation` (Key Properties); `guides/delegation-patterns` (Tips).

### Scheduled tasks (cron)

- **F26.** One tool manages cron: `cronjob_manage` (toolset `cronjob`), with the actions `create`, `list`, `update`, `pause`, `resume`, `run`, and `remove`. A job name works in place of its ID, but names are not unique. Older docs and the code examples call it `cronjob(...)`. Sources: `user-guide/features/cron`; `reference/tools-reference`; code: `tools/cronjob_tools.py`.
- **F27.** `create` needs `schedule` and `prompt`. Optional fields include `name`, `skills` (a list, loaded before the prompt), `deliver`, and `workdir`. Schedules accept cron expressions (`0 9 * * 1`), weekly forms (`every monday 9am`), intervals, and ISO one-shots. Sources: `user-guide/features/cron` (Skill-backed cron jobs, Schedule formats); code: `tools/cronjob_tools.py` (tool schema).
- **F28.** Leaving `deliver` out sends the result to the chat the job was created in (`origin`). In the CLI the default is `local` (saved to a file). Sources: `user-guide/features/cron` (Delivery options); code: `tools/cronjob_tools.py`.
- **F29.** Every run is a fresh session: no chat history, a self-contained prompt, attached skills loaded first, and the final response delivered. Cron tools are disabled inside cron runs. Sources: `user-guide/features/cron`; `developer-guide/cron-internals`.
- **F30.** A final response that contains `[SILENT]` is not delivered (the output stays in a local file). Source: `user-guide/features/cron` (Silent suppression).
- **F31.** By default the delivered output is wrapped in a header (`Cronjob Response: <name>`) and a footer (`cron.wrap_response`). Sources: `user-guide/features/cron` (Response wrapping); code: `cron/scheduler_delivery.py`.
- **F32.** The gateway connects Telegram, Discord, Slack, WhatsApp, Signal, Email, and other platforms, and ticks the scheduler every 60 seconds. A plain CLI chat does not fire jobs. Sources: `user-guide/messaging/`; `user-guide/features/cron` (How it works); `guides/cron-troubleshooting` (Check 3).
- **F33.** Schedules run on Hermes's clock: the `timezone` setting (or `HERMES_TIMEZONE`), else server-local time. The same setting drives the current time in the system prompt. Sources: `user-guide/configuration#timezone`; `guides/cron-troubleshooting` (Check 4).
- **F34.** Before a run, Hermes checks that attached skills are ready; a job whose skill is missing is marked `blocked_config` and makes no model call. Source: `user-guide/features/cron` (Pre-dispatch configuration validation).

### Profiles, files, and surfaces

- **F35.** `hermes profile create <name>` makes a separate Hermes home with its own SOUL.md, memory, skills, and cron jobs, and each profile runs its own gateway with its own bot token. Sources: `user-guide/profiles`; `reference/profile-commands`.
- **F36.** `write_file` and `patch` refuse paths outside `HERMES_WRITE_SAFE_ROOT` when it is set (the official Docker image sets `/opt/data`), with a "Write denied ... is outside HERMES_WRITE_SAFE_ROOT" message. Source: `user-guide/security` (File Write Safety).
- **F37.** In the official Docker image, tool calls see `HOME` as `/opt/data/home`, inside the persisted `/opt/data` volume. Source: `user-guide/docker`.
- **F38.** The file tools are `read_file`, `write_file`, `patch`, and `search_files`; `write_file` needs a full `read_file` of an existing file first. Source: `reference/tools-reference` (file toolset).
- **F39.** The toolsets of the chat platforms (Telegram, Slack, WhatsApp, Signal, Email, and others) match `hermes-cli`: file, terminal, memory, skills, delegation, cronjob, and more; Discord adds its own tools, and only the webhook surface is cut down. Core tools are always loaded; some cold built-ins sit behind `tool_search`. Sources: `reference/toolsets-reference`; `user-guide/features/tool-search`.
- **F40.** The system prompt carries a platform hint that names the surface (Telegram, WhatsApp, Slack, CLI, and others) and the current time. Source: `developer-guide/prompt-assembly`.
- **F41.** Telegram voice notes are transcribed automatically. Source: `user-guide/messaging/telegram`.

---

## 2. The mapping

The vault, charters, workflows, and rules are the same on both platforms (FACTORY-SPEC §13). Only these mechanics change.

| Concept | Grokbot (`kit/INSTALL.md`) | Hermes (`kit/INSTALL-HERMES.md`) | Facts | Step |
|---|---|---|---|---|
| Where the kit lives | The vault is copied to a persistent folder | The whole `kit/` folder is copied to `~/<team_slug>-hermes/`: the vault inside it (`{{vault_path}}`), the runbook and skills next to it (`{{kit_path}}`), because workflows and skills point back to the runbook | F37 | 2 |
| Platform flag | `platform: grokbot` | `platform: hermes` in `00-START-HERE.md` | | 4 |
| Lead's standing instructions | The platform's permanent instructions | One block between `<!-- <team_slug> kit: start -->` and `<!-- <team_slug> kit: end -->`, added at the end of SOUL.md in the Hermes home. Fallback: one short `memory` entry, only after a technical refusal or the client's "memory" reply | F11-F16, F18 | 5 |
| Lead's procedure | (none) | The lead skill `<team_slug>-<lead file stem>`, also attached to every scheduled task | F5, F27 | 6, 8 |
| Specialists and QA Agent | Named sub-agents, created at install | One skill per agent, created with `skill_manage` in the `<team_slug>` category, plus a fresh subagent per job | F3, F4, F20, F21 | 6 |
| Sending a job | A message to a named sub-agent | `delegate_task` with `goal` and `context`; `context` carries the Grokbot Step 6 instruction block, the skill name, and a `Job:` line; parallel jobs go in one `tasks` call; the lead ends its turn and the result arrives as a message | F20-F25 | 6 |
| No reply | 30-minute timeouts | Status `failed`, `timeout`, `stalled`, or `interrupted` counts as no reply, then production's "Timeouts and failures" | F24 | 6 |
| Helper cannot read the vault | Packet mode | Packet mode: the full ticket, with `## Packet` filled, after the `Job:` line | F21 | 6, 7 |
| Helper unavailable | Mode fallback | Mode fallback: no `delegate_task`, or the Step 7 test fails twice | F22 | 6, 7 |
| Skill approval gate | (none) | The client sends `/skills approve all` or replies "skip"; the kit also works without skills | F6 | 6 |
| Schedules | The platform scheduler | Cron jobs made with `cronjob_manage` at setup Stage 5, from the client's chat: fixed names, weekly schedules on Hermes's clock, the lead skill attached, a self-contained prompt, `deliver` left out; the run replies `[SILENT]` in off weeks | F26-F34 | 8 |
| No scheduler | "questions now" | `Scheduler: no` when the cron tool fails or the client is not on a messaging app; then "questions now" | F28, F32 | 8 |
| Kit updates | Replace kit-owned files | The same, plus `patch` every skill, rewrite only the SOUL.md block between the markers, and `update` job prompts when the version notes say so | F3, F18, F26 | Updating |
| Profile | (none) | The profile the conversation runs in. A dedicated profile needs its own bot token and gateway, so it stays an operator option outside the runbook | F35 | Intro |

Why SOUL.md for the standing instructions: it is the only documented surface that loads in every chat and every scheduled run, whatever the working directory (F12, F13). AGENTS.md depends on the working directory (F17), a memory entry competes for 2,200 characters and a skill loads only when the model picks it (F18, F19). The block stays short (identity, vault path, read-first lines, runbook pointer) to respect the SOUL.md guide (F17); everything else lives in the vault.

Why skills are an extra, not a dependency: the instruction block in every delegation is complete without them, cron prompts are self-contained, and Step 7 tests whether subagents can load skills at all (F22, U4). A client who declines the skill approval still gets a working team.

---

## 3. Which runbook step relies on which fact

| Step in `kit/INSTALL-HERMES.md` | Facts |
|---|---|
| Intro and "What you need" | F3, F5, F18, F20, F26, F35, F38, F39 |
| Step 1 · Tell the client | F15 |
| Step 2 · Copy the kit | F9, F37 |
| Step 3 · Verify every file | (none: plain file checks) |
| Step 4 · Record the install | F36, F38 |
| Step 5 · Standing instructions | F11-F16, F18, F38 |
| Step 6 · Agent skills and sending jobs | F1-F7, F10, F20-F25, F39 |
| Step 7 · Test subagent file access | F20-F24 |
| Step 8 · Scheduler and creating the scheduled tasks | F26-F34, F40 |
| Step 9 · Log the install | (none) |
| Step 10 · Start setup | F14 |
| If a step fails | F15, F16, F36 |
| Updating an existing install | F3, F4, F18, F26 |
| `BOOTSTRAP-PROMPT-HERMES.md` | F14 (`/new`), F41 (voice notes) |
| `kit/hermes-skills/_agent-skill/SKILL.md` | F2, F4, F5, F10, F25 |

---

## 4. Hermes names used in the templates

Every Hermes-specific name in the 4 Hermes templates, with the fact that verifies it.

| Name | Kind | Used in | Fact |
|---|---|---|---|
| SOUL.md, `~/.hermes`, `HERMES_HOME`, `{{hermes_home}}` | file, folder, environment variable | INSTALL-HERMES Steps 5, 6; Updating | F11 |
| `<!-- <team_slug> kit: start -->` / `end` markers | text in SOUL.md | Step 5 | F16 |
| `memory` with `action: "add"`, `target: "memory"`, `action: "replace"`, `old_text` | tool | Step 5; Updating | F18 |
| `skill_manage` with `action: "create"` / `"patch"`, `name`, `category`, `content` | tool | Step 6; Updating; hermes-skills README | F3, F4 |
| `"staged": true`, `/skills approve all` | tool result, slash command | Step 6 | F6 |
| `skills_list`, `skill_view` | tools | Steps 6, 7; instruction block | F5 |
| `{{hermes_home}}/skills/<team_slug>/<skill name>/SKILL.md` | path | Step 6 | F1 |
| `name`, `description` (60 characters or less), `version`, `metadata.hermes.tags`, `metadata.hermes.category` | SKILL.md frontmatter | `_agent-skill/SKILL.md` | F2, F4 |
| `delegate_task` with `goal`, `context`, `tasks`; up to 10 at once | tool | Steps 6, 7 | F20 |
| Statuses `failed`, `timeout`, `stalled`, `interrupted` | tool results | Steps 6, 7 | F24 |
| `cronjob_manage` (older: `cronjob`) with `action: "list"` / `"create"` / `"update"` / `"remove"`, `name`, `schedule`, `prompt`, `skills`, `deliver`, `job_id` | tool | Step 8; Updating | F26-F28 |
| `0 10 * * 1`, `every monday 10am` | schedule forms | Step 8 | F27 |
| `[SILENT]` | reply token | Step 8 (job prompt) | F30 |
| `Cronjob Response:` header | delivery wrapper | Step 8 | F31 |
| Hermes's clock (the time in the system prompt) | behavior | Step 8 | F33, F40 |
| Platform hint (Telegram, Discord, Slack, WhatsApp, Signal, Email) | system prompt | Step 8 | F32, F40 |
| `HERMES_WRITE_SAFE_ROOT` | environment variable | Step 4 | F36 |
| `read_file`, `write_file`, `patch`, terminal | tools | "What you need"; Step 5 | F38, F39 |
| `~/<team_slug>-hermes/` | folder | Step 2 | F37 |
| `/new` | slash command | `BOOTSTRAP-PROMPT-HERMES.md` | F14 |
| Approval by replying yes or approve | gateway behavior | Steps 1, 5 | F15 |

---

## 5. Open uncertainties and how the templates handle them

- **U1 · SOUL.md write approval.** The docs (F15) say every agent write to SOUL.md needs the user's approval. The `main` code (`tools/file_tools_write_guards.py`) exempts files inside the active Hermes home from the protected-instruction approval gate, so no prompt may appear. Handled: Step 1 tells the client an approval may come; Step 5 handles a denial or a timeout with a retry message and a memory fallback that needs the client's "memory" reply.
- **U2 · Non-local terminal backends** (Docker, SSH, Modal, Daytona as the terminal backend). File tools act inside the backend, and the code has a "sandbox mirror" warning guard, so a SOUL.md write can land in a copy instead of the real Hermes home. Not handled in the runbook beyond the Step 5 check. An operator can confirm with `/context`, which lists SOUL.md and whether it loaded (`reference/slash-commands`).
- **U3 · Cron tool name.** `cronjob_manage` in current docs and code; `cronjob` in older docs, the code examples, and the delegation page's blocked-tool list. Handled: Step 8 names both.
- **U4 · Skills inside subagents.** Subagents inherit the `skills` toolset (F22), so `skill_view` works for them, but no doc page says so directly. Handled: Step 7 tests it; the instruction block works without it.
- **U5 · Size of a delegation's context.** No limit is documented for `delegate_task` (the plugin lifecycle API caps goal and context sizes). Packet-mode jobs can be large. Handled: a failed call counts as no reply; after 2, mode fallback.
- **U6 · Cadence.** No single cron schedule means "every 2 weeks on Monday" or "the first Monday of the month". Handled: every job is weekly; the job prompt skips off weeks (dates in `06-log/questions-asked.md`) and skips `monthly-review` outside days 1 to 7, replying `[SILENT]`.
- **U7 · Timezones and daylight saving time.** Jobs follow Hermes's clock (F33), and the lead converts the client's times when it creates them. When only one of the 2 zones switches to or from daylight saving time, the jobs move by an hour. Not handled by the kit; an operator can set Hermes's `timezone` to the client's zone (a config change the kit never makes itself).
- **U8 · Surfaces without chat delivery.** In the CLI, results go to a local file (F28), and the Desktop app's delivery target for `origin` is not documented. Handled: `Scheduler: no` unless the client uses a messaging app.
- **U9 · `/skills approve all` scope.** It approves every staged skill write, including writes that are not the kit's. Handled: the approval message says so, and the client can reply "skip".
- **U10 · Injection scanner and kit text.** A `team_slug` containing ignore, override, system, secret, or hidden turns the SOUL.md markers into a flagged HTML comment (a warning in SOUL.md). Memory entries are blocked on any hit, including phrases such as "check in with" or "pull tasks". Handled: the runbook texts avoid these patterns; the factory must keep those words out of `team_slug` (a FACTORY-SPEC §7 gap).
- **U11 · Docs and code drift seen on 2026-09-25.** The cron footer text differs between the cron page and `cron/scheduler_delivery.py`; the security page says the agent may write `config.yaml`, while the code refuses it. The kit relies on neither.
- **U12 · Persistence of `~` on remote sandbox backends** (Modal, Daytona) depends on the backend. Not handled; the Step 2 check and Step 7 catch missing files during the install, not a later loss.

---

## 6. Re-verify when Hermes updates

Run this list before shipping a kit when Hermes has released a new version since the "Checked" date above. Read the doc pages named in section 1 (or the same files in `website/docs/` of the repo), then:

- [ ] Skills: the folder layout, the SKILL.md frontmatter keys, and the `skill_manage` actions and fields (`create`, `patch` with `content`, `category`) (F1-F3).
- [ ] Code: the 60-character description limit and the name rule in `tools/skill_manager_tool.py` and `agent/skill_utils.py` (F4).
- [ ] The `skills_list` and `skill_view` names, the `/skills approve` syntax, and the `staged` result (F5, F6).
- [ ] Curator: foreground-created skills still stay unmanaged (F7).
- [ ] SOUL.md: location, slot 1, loaded in cron runs, not loaded in subagents, and the write-approval behavior (F11-F15, U1).
- [ ] Threat patterns in `tools/threat_patterns.py`: the HTML comment rule and the phrases in U10 (F16).
- [ ] `memory`: actions, targets, and the 2,200-character limit (F18).
- [ ] `delegate_task`: `goal`, `context`, `tasks`, default concurrency, blocked tools, background completion, and result statuses (F20-F24).
- [ ] Cron: the tool name, its actions, the `create` fields (`name`, `schedule`, `prompt`, `skills`, `deliver`), the `deliver` default, `[SILENT]`, the wrapper, the timezone, the gateway requirement, and the skill readiness check (F26-F34, U3).
- [ ] `/new` and gateway session continuity (F14).
- [ ] `HERMES_WRITE_SAFE_ROOT` and the Docker `HOME` (F36, F37).
- [ ] Profiles, only if the runbook starts using them (F35).
- [ ] After any change: update section 1, the names table in section 4, and every template line that uses the changed name; grep the 4 Hermes templates for each name in section 4; run `python scripts/check_factory.py`; record the change in the factory's CHANGELOG (FACTORY-SPEC §16).
