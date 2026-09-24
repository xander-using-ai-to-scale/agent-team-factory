# Agent Team Factory

A reusable process for building agent teams. Give it context (a call transcript, notes, a client's documents) and it builds a complete **team kit**: a GitHub repo that turns a Grokbot or a Hermes agent into the lead of a team of specialist agents, with an Obsidian vault as the team's memory.

Same structure every time, different context: a content team, an HR team, an SEO team, a podcast-booking team.

---

## What every team kit contains

| Part | What it is |
|---|---|
| GitHub repo | The source of truth for the team |
| Grokbot template | `kit/INSTALL.md` + a start prompt |
| Hermes template | `kit/INSTALL-HERMES.md` + Hermes skills + a start prompt |
| Obsidian vault | Brain files, sources, banks, charters, workflows, question banks, templates, outputs, logs; a README in every folder; a routing table; the read-first rule |
| The team | A lead (the only agent the client talks to), 1-8 specialists, and a QA Agent |
| User guide | How the client uses the team (ready to turn into a Google Doc) |
| Checker + zip | `scripts/check_kit.py` and a zip in `dist/` |

The reference build is the Content Grokbot kit: https://github.com/xander-using-ai-to-scale/content-grokbot

---

## Use it in 3 steps

1. Open a new Claude Code chat in an empty folder.
2. Paste the message from [FACTORY-PROMPT.md](FACTORY-PROMPT.md), with your one-line team description, and attach your context.
3. Answer its few questions and approve the blueprint. It builds, checks, and publishes the kit, then sends you the repo link and the start prompts.

---

## How it works

```
Context ──► 1 Intake ──► 2 Blueprint ──► 3 Questions ──► 4 Build ──► 5 Check ──► 6 Ship
            Team Brief    you approve     interview +     every       checker,    repo, zip,
            + gap         roster, brain   routine         FILL        review,     start
            questions     files, routine  questions       written     dry run     prompts
```

| Stage | Process file | Output |
|---|---|---|
| 1. Intake | [process/01-intake.md](process/01-intake.md) | `docs/TEAM-BRIEF.md` |
| 2. Blueprint | [process/02-blueprint.md](process/02-blueprint.md) | Approved blueprint, `team.json`, scaffolded repo |
| 3. Questions | [process/03-question-design.md](process/03-question-design.md) | The setup interview and routine questions |
| 4. Build | [process/04-build.md](process/04-build.md) | A complete kit |
| 5. Check | [process/05-check.md](process/05-check.md) | Checker at 0 errors, 0 warnings; dry run passed |
| 6. Ship | [process/06-ship.md](process/06-ship.md) | Published repo, zip, handoff message |

The builder's rules are in [process/00-builder-charter.md](process/00-builder-charter.md). The contract every stage follows is [docs/FACTORY-SPEC.md](docs/FACTORY-SPEC.md).

---

## Repo map

```
agent-team-factory/
├── README.md               this file
├── FACTORY-PROMPT.md       the message you paste into Claude Code
├── CHANGELOG.md
├── process/                the 6 stages + the builder charter
├── docs/
│   ├── FACTORY-SPEC.md     the contract: layout, markers, tokens, team.json, rules, checks
│   └── HERMES-NOTES.md     verified Hermes facts the Hermes install relies on
├── templates/team-repo/    the 55 template files every team kit is built from
├── scripts/
│   ├── scaffold_team.py    copies the templates and fills every token from team.json
│   └── check_factory.py    validates the factory itself
└── examples/               the content team (the reference build) mapped onto the factory
```

---

## Changing the factory

1. Change [docs/FACTORY-SPEC.md](docs/FACTORY-SPEC.md) first.
2. Update the templates, process files, and scripts to match.
3. Run `python scripts/check_factory.py` until it prints 0 errors.
4. Add a line to [CHANGELOG.md](CHANGELOG.md) and bump the factory version.

Kits already built keep their own version; rebuild or update them on purpose, never automatically.
