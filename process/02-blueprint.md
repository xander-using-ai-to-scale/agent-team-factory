# Stage 2 · Blueprint

Design the team, get the requester's written approval, then lock the design into `team.json` and `docs/TEAM-SPEC.md` and scaffold the repo.

- **Input:** the finished `docs/TEAM-BRIEF.md`.
- **Output:** the approved blueprint, `team.json`, `docs/TEAM-SPEC.md`, and a scaffolded repo.
- **Gate:** the requester approved the blueprint in writing, team.json follows FACTORY-SPEC §7, and the scaffold ran without errors.
- **Time:** 15-30 minutes, plus approval.

---

## Step 1 · Name things

| Item | Rule | Content kit |
|---|---|---|
| Team name | "<Domain> Team", plain | Content Team |
| Team slug | lowercase, hyphens | content-team |
| Lead | A job title a client would recognize in this domain, 1-3 words, plus a short form | Editor-in-Chief (EIC) |
| Vault | "The <Noun>": a book-like noun that fits the domain | The Almanac |
| Output unit | The noun for one delivery of work | pack |
| Routine | What the recurring question cycle is called | ritual |

Names never reuse fixed names ("QA Agent" is taken). The lead's short form appears in hundreds of places: keep it 2-4 characters or one short word.

---

## Step 2 · Design the roster

1. List every distinct kind of output in the brief's Outputs field.
2. Give each kind one specialist. Merge two kinds into one specialist when the same skill and the same inputs produce both (the content kit merged Reels, Shorts, and TikTok into one Short-Form Agent). Split one kind into two only when they need different knowledge or run on different schedules.
3. Mark work the client asks for only occasionally as `on_demand_only: true` (content kit: the VSL Agent).
4. Set `depends_on`: which outputs must pass QA before this one starts. Put a "core piece" first when other outputs are cut from it (content kit: the pillar first, the lead magnet next, then the platform pieces).
5. Keep 1 to 8 specialists. More than 8 means two teams.
6. For each specialist, write: name ("<Thing> Agent"), file (`<thing>-agent.md`), job (one sentence), `output_file` (`NN-<thing>.md` in production order), `depends_on`, and what it must never do beyond the team's authority.
7. The lead and the QA Agent are always there. The lead never produces client work itself except in mode fallback.

Roster tests (all must pass):
1. Every specialist produces something the client uses.
2. No two specialists produce the same thing.
3. Every output in the brief has exactly one owner.
4. The dependency order has no loops.

---

## Step 3 · Design the brain files

1. The 3 core files are always there: `company.md`, `voice.md`, `plan.md`, with their fixed sections (FACTORY-SPEC §9).
2. Add 0 to 3 domain files for knowledge from the brief's Knowledge field that fits none of the core files. Content kit: `customer.md` and `offer.md`. HR example (fictional): `roles.md`, `policies.md`.
3. Give each domain file 5 to 12 sections. Each section answers one question the team needs answered to do good work ("Pains", "Objections", "Pay bands", "Interview stages").
4. Append domain sections to a core file only when they clearly belong there (for example "Service area" on `company.md`).
5. Include a section ending in "to avoid" wherever the domain has banned territory (content kit: "Claims to avoid"). Rule 7 bans everything under those headings.

Brain-file tests:
1. Every section is read by at least one agent (you will prove it in the routing rows).
2. Every section can be filled from the client's interview answers alone.
3. No fact is stored in two files.

---

## Step 4 · Design the banks

1. Banks hold reusable material collected from the client's routine answers, each entry with an ID. Content kit: stories (S), proof (P), hooks (H), ideas (I).
2. Pick 1 to 5 banks. Each bank must be written by the routine or the learning loop and read by at least one specialist.
3. Give each bank a unique one-letter prefix. E, W, and Q are taken by the logs.
4. List each entry's fields (always id, date, source, permission, status, plus the domain fields).

---

## Step 5 · Design the routine, outputs, and authority

1. **Routine.** What the client answers each cycle (the recurring input), how many questions (default 5), cadence (default weekly), and the question time (default the day before delivery day, 10:00). Name the 8-15 question categories you will write in stage 3.
2. **Schedules.** The 4 fixed schedules (`routine-send`, `routine-reminder`, `feedback-check`, `monthly-review`) with default times. Add an extra schedule only when the brief needs it.
3. **Outputs and quantities.** One row per specialist: output, active by default (yes or on demand), quantity per unit.
4. **Delivery.** The DELIVERY.md sections in production order, and what goes in "Check before using".
5. **Authority.** Propose the table from FACTORY-SPEC §12. Default: everything draft-only; "Allowed" and "With approval" empty. Add an action only when the brief confirms it, and prefer "With approval" over "Allowed".
6. **On-demand requests.** The commands the client uses for single pieces ("write a job post for {{role}}"), one per specialist that can work on demand.
7. **QA.** The 10 universal checks always apply. Add 0-5 team-specific checks for domain risks (content kit: CTA rules per platform; HR example: no discriminatory wording).

---

## Step 6 · Send the blueprint for approval

Send one message the requester can read in 2 minutes. Use this layout:

```
Stage 2/6 · Blueprint · waiting for approval

<Team name>: <purpose, one sentence>

1. Team (<N> agents)
| Agent | Job | Output |
|---|---|---|
| <Lead> | Talks to the client, runs everything | Deliveries |
| <Specialist> | ... | ... |
| QA Agent | Checks everything before the client sees it | QA report |

2. What it knows (brain files): company, voice, plan, <domain files with one-line purpose>
3. Each <routine name>: <N> questions on <day/time>, <cadence>; the client answers by voice memo
4. Each <output unit>: <list of outputs and quantities>, in this order: <production order>
5. What it may do: <authority summary; default "drafts only, the client acts">

Names: lead "<Lead name>", vault "<Vault name>", repo "<slug>".
Reply "approve", or send changes (for example "2: add a policies file").
```

Rules:
1. Every row states a choice and, where not obvious, a one-line reason.
2. Iterate until the requester replies with approval. Two change rounds are normal.
3. Record the approval: the date and the requester's words.

---

## Step 7 · Lock the design

1. Write `<team_slug>/team.json` exactly per FACTORY-SPEC §7 (keys, order, formats). Validate it: `python -c "import json; json.load(open('team.json', encoding='utf-8'))"` from the team folder.
2. Copy `templates/team-repo/docs/TEAM-SPEC.md` to `<team_slug>/docs/TEAM-SPEC.md` and write its "Approved blueprint" section: the approved message, the approval date, and the requester's words. Fill the rest of TEAM-SPEC in stage 4.
3. Run the scaffold from the working directory:
   ```
   python agent-team-factory/scripts/scaffold_team.py <team_slug>
   ```
   It copies every template, replaces every token, creates the per-item files (brain files, banks, charters, Hermes skills), and keeps the files you already wrote.
4. Confirm the output: "created" is about 55 plus the per-item files, "kept" lists team.json, TEAM-BRIEF.md, and TEAM-SPEC.md, and there are no unknown tokens.
5. Send the requester one line: `Stage 2/6 done · blueprint approved and scaffolded · writing the interview questions now`.

---

## Checklist

- [ ] Names follow Step 1; no fixed name reused.
- [ ] Roster passes the 4 roster tests; 1-8 specialists; the dependency order has no loops.
- [ ] Brain files: the 3 core files plus 0-3 domain files, 5-12 sections each, passing the 3 brain-file tests.
- [ ] Banks: 1-5, unique prefixes, not E, W, or Q.
- [ ] Routine, schedules, outputs, delivery, authority, on-demand commands, and QA additions designed.
- [ ] Written approval recorded in TEAM-SPEC with its date.
- [ ] team.json valid; the scaffold reported no unknown tokens.
