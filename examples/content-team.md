# Example: the content team

The Content Grokbot kit (https://github.com/xander-using-ai-to-scale/content-grokbot) was built by hand before the factory existed. Every factory template is a generic version of one of its files, so it is the best worked example of a finished kit. This page maps it onto the factory's concepts.

---

## The blueprint, in factory terms

| Factory concept | Content kit |
|---|---|
| Team name / slug | Content Grokbot / content-grokbot |
| Purpose | Turns the owner's weekly voice-memo answers into a pack of content drafts |
| Lead | Editor-in-Chief (EIC), `editor-in-chief.md` |
| Vault | The Almanac (`The-Almanac/`) |
| Output unit | pack (`05-packs/`, compiled into `PACK.md`) |
| Routine | the ritual: 5 questions the day before content day |
| Specialists (8) | Newsletter, Lead Magnet, YouTube, Short-Form, LinkedIn, X, Instagram, VSL (on demand) |
| Production order | Pillar (newsletter) first → lead magnet → platform pieces in parallel → QA → PACK.md |
| Core brain files | company.md, voice.md, strategy.md (the factory calls it plan.md) |
| Domain brain files | customer.md, offer.md |
| Banks | stories (S), proof (P), hooks (H), ideas (I) |
| Pushback round | The skeptical-buyer round after the offer questions |
| Team-specific QA | Call-to-action rules per platform, link rules, KEYWORD rules |
| Authority | Drafts only: the client posts everything |
| On-demand commands | `write a {{platform}} post about {{topic}}`, `make a VSL for {{offer}}`, `lead magnet about {{topic}}` |

---

## team.json, if the content kit were built by the factory (fictional reconstruction)

```json
{
  "factory_version": "1.0.0",
  "kit_version": "1.0.0",
  "release_date": "2026-09-24",
  "team_name": "Content Team",
  "team_slug": "content-team",
  "team_purpose": "turns the owner's weekly voice-memo answers into a pack of content drafts",
  "vault_name": "The Almanac",
  "vault_folder": "The-Almanac",
  "output_unit": "pack",
  "output_unit_plural": "packs",
  "routine_name": "ritual",
  "platforms": ["grokbot", "hermes"],
  "lead": {"name": "Editor-in-Chief", "short": "EIC", "file": "editor-in-chief.md"},
  "qa": {"name": "QA Agent", "file": "qa-agent.md"},
  "specialists": [
    {"name": "Newsletter Agent", "file": "newsletter-agent.md", "job": "Writes the pillar.", "row": "R12", "output_file": "01-pillar.md", "depends_on": [], "on_demand_only": false},
    {"name": "Lead Magnet Agent", "file": "lead-magnet-agent.md", "job": "Writes the playbook, its KEYWORD, and the CTA lines.", "row": "R13", "output_file": "02-lead-magnet.md", "depends_on": ["newsletter-agent.md"], "on_demand_only": false},
    {"name": "YouTube Agent", "file": "youtube-agent.md", "job": "Writes the long-form video package.", "row": "R14", "output_file": "03-youtube.md", "depends_on": ["newsletter-agent.md", "lead-magnet-agent.md"], "on_demand_only": false},
    {"name": "VSL Agent", "file": "vsl-agent.md", "job": "Writes video sales letter scripts.", "row": "R15", "output_file": "04-vsl.md", "depends_on": [], "on_demand_only": true}
  ],
  "brain_files": [
    {"file": "company.md", "title": "Company", "core": true, "sections": ["What we sell", "Who we serve", "How we make money", "What we believe", "What makes us different", "Key facts"]},
    {"file": "voice.md", "title": "Voice", "core": true, "sections": ["How we sound", "How we never sound", "Phrases we use", "Banned words and phrases", "Formatting habits", "Spoken voice", "Written voice", "Good examples", "Bad examples", "Rules learned from edits"]},
    {"file": "plan.md", "title": "Plan", "core": true, "sections": ["Goal", "Outputs and quantities", "Rhythm", "Delivery", "Authority", "Team and handoff", "Areas to avoid", "Content pillars", "Calls to action", "Lead magnets", "Script style"]},
    {"file": "customer.md", "title": "Customer", "core": false, "sections": ["Ideal customer", "Not a fit", "Pains", "Desired outcomes", "Objections", "Buying triggers", "Questions they ask", "Exact language", "Fears", "Decision criteria", "Where they spend time"]},
    {"file": "offer.md", "title": "Offer", "core": false, "sections": ["Offers", "Pricing logic", "Promises we make", "Proof", "Claims to avoid", "Good-fit customer", "Skeptical buyer Q&A"]}
  ],
  "banks": [
    {"file": "stories.md", "title": "Stories", "id_prefix": "S"},
    {"file": "proof.md", "title": "Proof", "id_prefix": "P"},
    {"file": "hooks.md", "title": "Hooks", "id_prefix": "H"},
    {"file": "ideas.md", "title": "Ideas", "id_prefix": "I"}
  ],
  "schedules": [
    {"name": "routine-send", "default_time": "Day before delivery day, 10:00", "does": "Sends the 5 ritual questions"},
    {"name": "routine-reminder", "default_time": "Delivery day, 09:00", "does": "Only if no answers yet: 1 reminder + the bank option"},
    {"name": "feedback-check", "default_time": "3 days after delivery day, 10:00", "does": "Asks for edits and winners"},
    {"name": "monthly-review", "default_time": "First delivery day of each month, after the delivery", "does": "Runs the monthly review"}
  ]
}
```

Four specialists are shown to keep the example short; the real kit has eight. Content-specific strategy sections (pillars, calls to action, lead magnets, script style) sit on `plan.md` as domain sections after the 7 core ones.

---

## Names that changed when the kit became the factory

| Content kit | Factory (every team) |
|---|---|
| `strategy.md` | `plan.md` |
| `05-packs/`, `PACK.md` | `05-outputs/`, `DELIVERY.md` |
| `02-sources/voice-memos/` | `02-sources/routine-answers/` |
| `02-sources/writing-samples/` | `02-sources/documents/` |
| Workflows `ritual.md`, `pack-production.md` | Workflows `routine.md`, `production.md` |
| Output templates `pack-summary.md`, `pack.md` | Output templates `output-summary.md`, `delivery.md` |
| `ritual-send`, `ritual-reminder` | `routine-send`, `routine-reminder` |
| Content day | Delivery day |
| "Check before posting" | "Check before using" |
| Rule 5 "Drafts only" | Rule 5 "Authority" (drafts only unless `plan.md` allows more) |
| Rule 10 "Pillar first" | Rule 10 "Dependencies first" |
| Routing rows R0-R15 (writers in the middle) | R0-R11 fixed, specialists from R12 |

The content kit itself stays as it is: it predates these names and works as installed.
