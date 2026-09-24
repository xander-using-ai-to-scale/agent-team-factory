# Stage 1 · Intake

Turn the requester's context into a complete **Team Brief**, asking only about the gaps that change the design.

- **Input:** the requester's context (transcripts, notes, documents, messages).
- **Output:** `<team_slug>/docs/TEAM-BRIEF.md`.
- **Gate:** all 12 fields have an answer (confirmed, inferred, or default), and no open gap would change the blueprint.
- **Time:** 10-20 minutes, plus the requester's answers.

---

## Step 1 · Create the team folder

1. Pick a working team name and slug from the context (for example "HR Team", `hr-team`). Both can change in stage 2.
2. Create `<team_slug>/` next to the factory folder, then `<team_slug>/docs/`.
3. Copy `templates/team-repo/docs/TEAM-BRIEF.md` to `<team_slug>/docs/TEAM-BRIEF.md`. Leave its `<<TOKEN>>` values as they are: the scaffold script fills them in at the end of stage 2, when the final names are set.

---

## Step 2 · Read and sort the context

1. Read every context file in full, start to finish. Transcripts often mention the team only once, deep in the call.
2. Mark each passage as **about this team** (what it does, for whom, outputs, inputs, tools, limits, quality, rhythm) or **not about this team** (other projects, other clients, small talk, unrelated tools).
3. Use only the first kind. A passage about another project stays out even when it sounds useful. When unsure, leave it out and turn it into a gap question.
4. List every ignored topic in "Context not used", one line each ("Affiliate program setup: a separate project").

---

## Step 3 · Fill the 12 fields

The fields are fixed in FACTORY-SPEC §18. For each one write:

1. **Answer**: specific and short. Numbers, names of outputs, cadences.
2. **Source**: the context file plus a short quote (15 words or fewer), or "requester answer, {{date}}", or "default".
3. **Confidence**: `confirmed` (stated plainly), `inferred` (you concluded it from the context), or `default` (from the table below).

Rules:
1. Never turn a guess into `confirmed`. An inference is `inferred`.
2. Knowledge (field 6) lists what the team must know, not the facts themselves. "The client's hiring stages" is a knowledge item; "Stage 1 is a phone screen" is a client fact and belongs in the vault at runtime.
3. Client-specific facts found in the context (names, prices, policies) go under "Material for setup drops" at the end of the brief, not into any field. They reach the kit only through the client's setup interview.

---

## Step 4 · Apply the safe defaults

Use a default when the context is silent and the default fits. Mark it `default`.

| Field | Default |
|---|---|
| Platforms | Grokbot and Hermes (every v1 kit builds both) |
| Authority | Draft-only for everything; the client acts |
| Rhythm | Weekly, one delivery day the client picks in setup; questions the day before at 10:00; client's timezone |
| Inputs | The recurring routine questions answered by voice memo or text, plus optional drops in setup |
| Delivery | Chat and the vault; Google Doc optional, tested in setup |
| Quality bar | The reference kit's QA checks and the default anti-AI list in `voice.md` |
| Client | A small-business owner who approves everything the team produces |
| Constraints | Never invent facts; names need permission; nothing outside the authority table |

No default exists for Purpose, Outputs, Roles, or Knowledge. If the context does not answer them, they are gaps.

---

## Step 5 · Find the gaps

A gap is a field that is empty, or `inferred` with an answer that would change the blueprint if wrong. Test each field: "If this answer were different, would the roster, brain files, routine, outputs, or authority change?" Yes = gap. No = keep the inference or default and move on.

Typical design-changing gaps:
1. What exactly the team delivers each cycle (outputs and quantities).
2. Whether the team must act in outside tools (send, book, update records) or only draft.
3. Which roles the requester already has in mind.
4. What recurring input the client can give each cycle.
5. Domain limits (legal, compliance, privacy) that need their own QA check.

---

## Step 6 · Ask the requester

Write the gap questions with the intake rules in [03-question-design.md](03-question-design.md) (section "Intake questions"):

1. At most 5 questions per message, numbered, one decision each.
2. Each question offers a recommended default first, marked "(recommended)", plus 1 to 3 alternatives, so the requester can reply "go" or "2: B".
3. Plain words. No jargon from this factory ("FILL", "token", "routing row").
4. Start the message with the state line: `Stage 1/6 · Intake · 3 questions`.

Record every answer in "Gaps and answers" with its date. Update the field, its source ("requester answer"), and its confidence (`confirmed`).

Ask at most 2 rounds. After round 2, use the recommended defaults for anything still open, mark them `default`, and say so in one line.

---

## Step 7 · Close the brief

1. Reread the brief top to bottom. Every field has an answer, a source, and a confidence.
2. "Context not used" lists every ignored topic.
3. "Material for setup drops" lists client-specific facts and files the client can drop in during setup.
4. Send the requester one line: `Stage 1/6 done · brief complete · designing the blueprint now`.

---

## Checklist

- [ ] `<team_slug>/docs/TEAM-BRIEF.md` exists and all 12 fields are filled.
- [ ] Every field has a source and a confidence; no guess is marked `confirmed`.
- [ ] No passage about another project was used.
- [ ] Gap questions: 5 or fewer per message, each with a recommended default; at most 2 rounds.
- [ ] Client-specific facts are under "Material for setup drops", not in the fields.
