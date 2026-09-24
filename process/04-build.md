# Stage 4 · Build

Write every remaining FILL so the scaffolded repo becomes a complete, working team kit.

- **Input:** the scaffolded repo, `team.json`, `docs/TEAM-BRIEF.md`, `docs/TEAM-SPEC.md` (approved blueprint), the finished question banks, and the reference kit (`content-grokbot/`).
- **Output:** a repo with zero `<!-- FILL` markers and zero `<<` tokens.
- **Gate:** `grep -r "<!-- FILL" <team_slug>` finds nothing outside `scripts/`, and `python scripts/check_kit.py --write-manifest` has run.
- **Time:** 45-120 minutes (less with helper agents).

---

## Step 1 · Know what you are filling

1. Count the FILLs: `grep -rc "<!-- FILL" <team_slug> --include=*.md --include=*.json`.
2. Each FILL says what to write, its Source, its Length, and the reference-kit Example to imitate. Everything outside FILLs is fixed text: keep it word for word.
3. Per-item files (each domain brain file, bank, specialist charter, and Hermes skill) were created from one template each. Write each one for its own item from team.json.

---

## Step 2 · Fill in this order

Later files quote earlier ones, so the order matters.

| Order | Files | Main sources |
|---|---|---|
| 1 | `docs/TEAM-SPEC.md` (every section after the approved blueprint) | Blueprint, team.json, brief |
| 2 | `01-brain/`: README, extra sections on core files, each domain brain file | TEAM-SPEC brain-file design |
| 3 | `03-banks/`: README, each bank | TEAM-SPEC banks |
| 4 | `04-agents/`: each specialist charter, then `qa-agent.md` (team checks), then the lead charter | TEAM-SPEC agents, commands, QA |
| 5 | `04-agents/templates/`: delivery.md sections, the job-ticket example | TEAM-SPEC delivery layout |
| 6 | `04-agents/workflows/`: setup order, routine filing and focus, production steps, learning-loop bank, monthly domain question, on-demand triggers | TEAM-SPEC routine and production order |
| 7 | `00-START-HERE.md`: who works here, routing rows R12 and up, bank IDs, the production line, extra schedules | Everything above |
| 8 | `02-sources/`, `05-outputs/`, `06-log/` READMEs | team.json |
| 9 | `kit/INSTALL.md`, `kit/INSTALL-HERMES.md`, each `kit/hermes-skills/<agent>/SKILL.md` | team.json |
| 10 | `docs/USER-GUIDE.md`, `README.md`, `CHANGELOG.md` | Everything above |

Then run from the team folder:

```
python scripts/check_kit.py --write-manifest
```

The first run lists what is still wrong. Stage 5 takes it to zero.

---

## Step 3 · How to write one FILL

1. Read the whole FILL comment.
2. Read its Source (the TEAM-SPEC section, team.json key, or brief field).
3. Open the Example in the reference kit and read the whole section it points to, not just its first lines.
4. Write your text at the same depth: the same kind of structure, a similar number of steps or rows, the same precision.
5. Delete the FILL comment. Keep any non-FILL guidance comment that explains a runtime format.
6. Reread the paragraph around it: it must read as one file, not a patch.

Content rules for every FILL:
1. Generic for the domain: no client names, prices, or facts. Client facts arrive at runtime.
2. Fictional examples only, labeled "(fictional)", with no em dashes and no real people or companies.
3. Every link points to a file that exists in this kit; every routing row cited exists.
4. Instructions are imperative, numbered, and specific: no "try to", "consider", "ideally", "maybe", "as appropriate".
5. Client-facing messages stay within 80 words unless FACTORY-SPEC §14 allows longer.

---

## Step 4 · Keep one source of truth

The reference kit needed three alignment passes because the same fact drifted between files. Each fact below has one owner; every other file copies it exactly or links to it.

| Fact | Owner | Must match in |
|---|---|---|
| Agent names, files, jobs | team.json | START-HERE §2, lead charter "Your team", both INSTALL files, Hermes skills, README, USER-GUIDE §2 |
| What each agent reads | START-HERE §4 routing table | Each charter's "Must read" (copy the row exactly), job tickets |
| Which outputs are on | `plan.md` "Outputs and quantities" | Nowhere else holds a switch; production.md and delivery.md say "active outputs only" |
| Output file names | team.json `output_file` | production.md, delivery.md, 05-outputs README, QA |
| Schedule names and default times | START-HERE §7 table | setup.md Stage 5, lead charter, USER-GUIDE rhythm table, TEAM-SPEC |
| Client commands | Lead charter "Client commands" | TEAM-SPEC commands, USER-GUIDE "Things you can say" |
| Bank prefixes and fields | team.json + each bank file | START-HERE IDs, banks README, routine.md filing step |
| Authority | `plan.md` "Authority" | Each charter's "What you never" section, QA check 8, USER-GUIDE rules |
| Production order | team.json `depends_on` | production.md steps, START-HERE §7, delivery.md order |
| Delivery layout | `templates/delivery.md` | production.md compile step, USER-GUIDE §6 |
| Pause semantics | `plan.md` "Rhythm" | routine.md, lead charter, USER-GUIDE |
| Where proposed brain changes go | production.md "After delivery" | routine.md, learning-loop.md, output-summary.md |

---

## Step 5 · Using helper agents (optional, faster)

Split the FILLs into groups that do not share files, for example: (A) brain files and banks, (B) specialist and QA charters, (C) workflows and templates, (D) START-HERE and READMEs, (E) installs, skills, and docs. Group D and E read the others' output, so run them last or give them the final team.json and TEAM-SPEC as their source.

Give every helper this brief, filled in:

```
You are a helper building the <Team name> kit with the Agent Team Factory.
Read first, in full: agent-team-factory/docs/FACTORY-SPEC.md,
agent-team-factory/process/04-build.md, <team_slug>/team.json,
<team_slug>/docs/TEAM-SPEC.md, <team_slug>/docs/TEAM-BRIEF.md.
Your files (write only these): <list>.
In each file, replace every <!-- FILL ... --> comment with finished text,
following Step 3 of 04-build.md. Each FILL names its Source and an Example in
content-grokbot/ (the reference kit, read-only): read the example section in
full and match its depth. Keep all text outside FILLs unchanged.
Rules: plain markdown; no client facts; fictional examples only, no em dashes;
imperative, specific instructions; no weasel words; links only to files that
exist in this kit; the one-source-of-truth table in 04-build.md Step 4.
Before you report: grep your files for "<!-- FILL" and "<<" (must be zero),
reread each file start to finish, and check it against team.json.
Report: files finished, decisions made, anything you could not fill and why.
```

Then review every file yourself before you accept it:
1. Read it start to finish.
2. Check it against team.json, TEAM-SPEC, and the Step 4 table.
3. Grep it for leftovers and residue from the reference kit (for example "pillar", "pack", "EIC" in a non-content team).
4. Fix what is wrong, or send it back with the exact change. Never accept work you have not read.

---

## Checklist

- [ ] Every FILL written in the Step 2 order; zero `<!-- FILL` and zero `<<` left outside `scripts/`.
- [ ] Every per-item file written for its own item.
- [ ] The Step 4 facts match everywhere.
- [ ] Every helper file read and checked by you.
- [ ] `python scripts/check_kit.py --write-manifest` has run.
