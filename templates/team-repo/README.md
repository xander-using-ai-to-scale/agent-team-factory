# <<TEAM_NAME>> kit

<<TEAM_NAME>>: <<TEAM_PURPOSE>>.

A drop-in kit that turns a fresh Grokbot or Hermes agent into the <<LEAD_NAME>>: the lead of a team of <<SUBAGENT_COUNT>> agents that works for one business, with an Obsidian-style vault, <<VAULT_NAME>>, as the team's memory.

<!-- FILL: 2 to 3 sentences on what the client experiences: one setup interview, then **5 questions** before every delivery day, answered by voice memo or text, then what one <<OUTPUT_UNIT>> holds, in plain words with the default quantities. Source: TEAM-SPEC §2 (What we are building), §12.3 (Routine), and §15 (Outputs); team.json → specialists. Length: max 70 words; bold "5 questions" and the name of the delivery. Example: content kit README.md, paragraph 2 ("It interviews the business owner once..."). -->

Every piece is checked by the QA Agent before the client sees it. Everything is a draft unless the client allowed it in their plan, and the team never spends money, enters passwords or payment details, deletes accounts or data, or changes account settings.

**Version <<KIT_VERSION>>** · <<RELEASE_DATE>>

---

## Install in 3 steps

**On Grokbot**

1. Open a **fresh** Grokbot.
2. Paste the prompt from [BOOTSTRAP-PROMPT.md](BOOTSTRAP-PROMPT.md) with this repo's link, or attach [`dist/<<TEAM_SLUG>>-kit-v<<KIT_VERSION>>.zip`](dist/<<TEAM_SLUG>>-kit-v<<KIT_VERSION>>.zip).
3. Answer the setup interview (about 45–60 minutes, no homework).

**On Hermes**

1. Open a **fresh** Hermes agent.
2. Paste the prompt from [BOOTSTRAP-PROMPT-HERMES.md](BOOTSTRAP-PROMPT-HERMES.md) with this repo's link, or attach the same zip.
3. Answer the same setup interview.

## How it works

```
setup interview (once)
  → <<BRAIN_FILE_COUNT>> brain files (you approve each one)
  → <<ROUTINE_NAME>>: questions the day before delivery day → your answers
  → production: <!-- FILL: the specialists' outputs in production order, joined with " → " (outputs that run side by side joined with " + "), in plain words. Source: team.json → specialists (depends_on); TEAM-SPEC §12.4 (Production order). Length: 1 line, max 90 characters. Example: content kit README.md, How it works ("pillar (newsletter) → lead magnet → platform drafts"). -->
  → QA: every piece checked before you see it
  → delivery: your <<OUTPUT_UNIT>>, in chat (and a Google Doc if you want one)
  → learning loop: your edits and winners → new rules, only with your yes
  → the next <<ROUTINE_NAME>>
```

| Role | What it does |
|---|---|
| **<<LEAD_NAME>>** | The only agent you talk to. Interviews you, keeps your <<VAULT_NAME>>, briefs the team, and delivers each <<OUTPUT_UNIT>>. |
| **QA Agent** | Checks every piece before you see it: voice, banned words, facts and claims, privacy, format, and what your plan allows. |
<!-- FILL: one row per specialist, in team.json → specialists order: the exact name in bold, then what it does in max 15 words, in plain words for a business owner. Specialists that do the same kind of work may share one row (list their names together, as the content kit does). Source: team.json → specialists (name, job). Length: 1 row per specialist or group. Example: content kit README.md, roles table rows after QA Agent. -->

## What's inside

```
<<TEAM_SLUG>>/
├── README.md                     You are here
├── BOOTSTRAP-PROMPT.md           Start message for a fresh Grokbot
├── BOOTSTRAP-PROMPT-HERMES.md    Start message for a fresh Hermes agent
├── CHANGELOG.md                  Versions
├── team.json                     The approved blueprint, machine-readable
├── .gitignore
├── docs/
│   ├── TEAM-BRIEF.md             The brief the team was designed from
│   ├── TEAM-SPEC.md              The approved blueprint and build contract: edit this first
│   └── USER-GUIDE.md             How to use it (also shared as a Google Doc)
├── kit/
│   ├── INSTALL.md                Install runbook for Grokbot (with the manifest)
│   ├── INSTALL-HERMES.md         Install runbook for Hermes (with the manifest)
│   ├── hermes-skills/            One skill per agent, for Hermes
│   └── <<VAULT_FOLDER>>/         The vault, installed on the agent's device
│       ├── 00-START-HERE.md      Rules, routing table, folder map
│       ├── 01-brain/             company, voice, plan<!-- FILL: ", " plus each domain brain file name without .md, in team.json order; no domain files: delete this comment. Source: team.json → brain_files (core: false). Length: 1 line. Example: content kit README.md tree ("01-brain/ company, customer, offer, voice, strategy"). -->
│       ├── 02-sources/           interview answers, <<ROUTINE_NAME>> answers, transcripts, documents, other
│       ├── 03-banks/             <!-- FILL: every bank title in lowercase, comma-separated, in team.json order. Source: team.json → banks (title). Length: 1 line. Example: content kit README.md tree ("03-banks/ stories, proof, hooks, ideas"). -->
│       ├── 04-agents/            charters, workflows, question banks, templates
│       ├── 05-outputs/           one folder per <<OUTPUT_UNIT>>
│       └── 06-log/               session log, edits, winners, open questions, questions asked
├── scripts/
│   ├── check_kit.py              Checks team.json, links, frontmatter, headings, agent names, and both manifests
│   └── build_zip.py              Rebuilds the zip from kit/
└── dist/
    └── <<TEAM_SLUG>>-kit-v<<KIT_VERSION>>.zip
```

Open `kit/<<VAULT_FOLDER>>` in [Obsidian](https://obsidian.md) ("Open folder as vault") to browse it.

## Docs

- [docs/USER-GUIDE.md](docs/USER-GUIDE.md): how to use it, day to day.
- [kit/INSTALL.md](kit/INSTALL.md): what a Grokbot does during install.
- [kit/INSTALL-HERMES.md](kit/INSTALL-HERMES.md): what a Hermes agent does during install.
- [docs/TEAM-SPEC.md](docs/TEAM-SPEC.md): the approved blueprint, and every rule, format, and decision behind the kit.
- [docs/TEAM-BRIEF.md](docs/TEAM-BRIEF.md): the brief the team was designed from.

## Changing the kit

1. Edit [docs/TEAM-SPEC.md](docs/TEAM-SPEC.md) first. If agents, brain files, banks, or schedules change, edit `team.json` too.
2. Edit the kit files to match.
3. Run `python scripts/check_kit.py` (must report 0 errors and 0 warnings; `--write-manifest` regenerates both manifests).
4. Bump the version in `CHANGELOG.md`, `team.json`, `kit/INSTALL.md`, `kit/INSTALL-HERMES.md`, and every `kit_version` field; add upgrade steps to "Version notes" in both install runbooks.
5. Run `python scripts/build_zip.py`.

Built with the Agent Team Factory v1.0.0.
