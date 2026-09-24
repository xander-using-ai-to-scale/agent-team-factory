# Bootstrap prompt (Hermes)

Paste this into the client's existing Hermes chat as one message. Send `/new` first, so the install starts in a fresh conversation. Either replace `[PASTE REPO LINK HERE]` with this repo's link, or attach `dist/<<TEAM_SLUG>>-kit-v<<KIT_VERSION>>.zip` to the same message. On Grokbot, use [BOOTSTRAP-PROMPT.md](BOOTSTRAP-PROMPT.md) instead.

```
You're about to become my <<LEAD_NAME>>: the head of my <<TEAM_NAME>>.

Install the <<TEAM_NAME>> kit from this GitHub repo: [PASTE REPO LINK HERE]
(If I attached a zip file instead, use the zip.)

1. Get the kit onto your machine (clone or download the repo, or unzip the file).
2. Open kit/INSTALL-HERMES.md and follow every step in order. Don't skip, merge, or improvise steps.
3. When the install is done, start my setup interview.

Don't do any work for me until setup is complete and I've approved my brain files.
```

## What happens next

| Step | Time | You do |
|---|---|---|
| Install | about 15–20 min | Approve a change if Hermes asks you to. Otherwise nothing: it messages you when it's ready. |
| Setup interview | about <!-- FILL: the setup interview length as a range of minutes, for example 45-60, the same range as BOOTSTRAP-PROMPT.md. Source: TEAM-SPEC §12.2 (Setup). Length: 1 range. Example: content kit BOOTSTRAP-PROMPT.md, "What happens next" row 2. --> min | Answer one question at a time. Voice notes are fine. Say "skip" anytime. |
| First <<OUTPUT_UNIT>> | about <!-- FILL: the minutes the client spends answering one <<ROUTINE_NAME>>, as one number or a range, the same as BOOTSTRAP-PROMPT.md. Source: TEAM-SPEC §12.3 (the <<ROUTINE_NAME>>: questions per cycle, 1 to 5 minutes each). Length: 1 number or range. Example: content kit BOOTSTRAP-PROMPT.md, "What happens next" row 3 ("about 15 min of answering"). --> min of answering | Answer your <<ROUTINE_NAME>> questions, then review your <<OUTPUT_UNIT>>. |

Everything else: [docs/USER-GUIDE.md](docs/USER-GUIDE.md).
