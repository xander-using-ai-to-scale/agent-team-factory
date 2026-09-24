# Bootstrap prompt (Grokbot)

Paste this into a **fresh** Grokbot (no other instructions, no old chats). Either replace `[PASTE REPO LINK HERE]` with this repo's link, or attach `dist/<<TEAM_SLUG>>-kit-v<<KIT_VERSION>>.zip` to the same message. On Hermes, use [BOOTSTRAP-PROMPT-HERMES.md](BOOTSTRAP-PROMPT-HERMES.md) instead.

```
You're about to become my <<LEAD_NAME>>: the head of my <<TEAM_NAME>>.

Install the <<TEAM_NAME>> kit from this GitHub repo: [PASTE REPO LINK HERE]
(If I attached a zip file instead, use the zip.)

1. Get the kit onto your device (download the repo, or unzip the file).
2. Open kit/INSTALL.md and follow every step in order. Don't skip, merge, or improvise steps.
3. When the install is done, start my setup interview.

Don't do any work for me until setup is complete and I've approved my brain files.
```

## What happens next

| Step | Time | You do |
|---|---|---|
| Install | about 10–15 min | Nothing. It messages you when it's ready. |
| Setup interview | about 45–60 min | Answer one question at a time. Voice notes are fine. Say "skip" anytime. |
| First <<OUTPUT_UNIT>> | about 15 min of answering | Answer 5 questions, then review your <<OUTPUT_UNIT>>. |

Everything else: [docs/USER-GUIDE.md](docs/USER-GUIDE.md).
