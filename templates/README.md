# templates/

`team-repo/` mirrors the repo of every team kit: 55 files, listed in FACTORY-SPEC §17. The scaffold script copies them into a new team folder.

## Markers inside the templates

| Marker | Meaning |
|---|---|
| `<<TOKEN>>` | A build-time value from team.json. `scripts/scaffold_team.py` replaces every one. |
| `<!-- FILL: ... -->` | Team-specific text the builder writes in stage 3 or 4. Each FILL names its Source and an Example in the reference kit. |
| `{{like_this}}` | A runtime placeholder. It stays in the kit; the team's lead fills it while working. |
| `[LIKE THIS]` | A client-fill marker. It stays; only the client can supply it. |

## Files the scaffold renames

| Template | Becomes |
|---|---|
| `kit/vault/` | `kit/<vault_folder>/` |
| `gitignore.txt` | `.gitignore` |
| `kit/vault/01-brain/_brain-file.md` | one file per domain brain file |
| `kit/vault/03-banks/_bank.md` | one file per bank |
| `kit/vault/04-agents/_lead-agent.md` | the lead's charter |
| `kit/vault/04-agents/_specialist-agent.md` | one charter per specialist |
| `kit/hermes-skills/_agent-skill/SKILL.md` | one Hermes skill per agent |

## Editing rules

1. Every template must match FACTORY-SPEC: names, headings, tokens, markers.
2. Keep universal text universal: nothing domain-specific outside a FILL.
3. Every FILL states what to write, its Source, its Length, and an Example in the reference kit.
4. Run `python scripts/check_factory.py` after every change.
