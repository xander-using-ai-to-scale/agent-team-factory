# Factory prompt

Paste the message below into a new Claude Code chat. Attach your context (call transcripts, notes, documents) or paste it under the message.

```
You're going to build a new agent team kit with the Agent Team Factory.

Factory repo: https://github.com/xander-using-ai-to-scale/agent-team-factory
Team to build: [ONE LINE, for example "an HR team for small service businesses"]
Context: attached (or pasted below)

1. Clone the factory repo and the reference kit it names into this folder.
2. Open process/00-builder-charter.md and follow it, then every stage in process/ in order. Don't skip, merge, or improvise stages.
3. Use only the parts of my context that are about this team. Ask me only what the process says to ask.
4. Don't build anything until I approve the blueprint.
5. When the kit passes every check, publish it and send me the repo link and both start prompts (Grokbot and Hermes).
```

What happens next:

1. **Intake:** it reads your context and asks up to 5 short questions about gaps, each with a recommended answer.
2. **Blueprint:** it proposes the team (roles, brain files, routine, outputs, what the team may do). You reply "approve" or send changes.
3. **Questions, build, check, ship:** it writes the interview questions, builds the kit, tests it, and publishes it. You answer two quick questions at the end: the repo name and public or private.
