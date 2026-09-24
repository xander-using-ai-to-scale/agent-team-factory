---
type: brain
file: company
version: 0
status: empty
updated: ""
approved_on: ""
kit_version: <<KIT_VERSION>>
---

# Company

Holds the stable facts about the business: what it sells, who it serves, how it makes money, what it believes, and what makes it different. The <<LEAD_NAME>> (<<LEAD_SHORT>>) fills it during setup from the interview and any optional drops.
Read by the <<LEAD_SHORT>> (full), by every specialist (at least the TL;DR; each specialist's routing row names any other sections), and by the QA Agent (Key facts), per the routing table in [[00-START-HERE]]. So the TL;DR must always carry the business name, the founder's name, and how to refer to them. Read-only: sub-agents never edit it, and after approval the <<LEAD_SHORT>> changes it only through [[04-agents/workflows/learning-loop#Brain change procedure]].

<!-- Fill rules (<<LEAD_SHORT>>): write only facts the client confirmed. Unknown → log a Q-### in [[06-log/open-questions]], write UNKNOWN (Q-###) in the field, add its pointer under ## Open questions; a section below its minimum count gets a Q-### too. Never guess.
Replace every {{placeholder}}. A placeholder holding a value, like {{no}} or {{1}}, is the default: confirm it with the client, then drop the braces. Delete unused template rows and blocks. Empty list → "- none"; empty table → one row with none in the first cell. Never edit guidance comments; {{ }} inside them are format examples.
Set status: draft when you start filling; status: approved needs the client's OK and zero {{ }} outside comments. Agents: UNKNOWN is not a fact; never fill it in; if your job needs it, reply BLOCKED. -->

## TL;DR
<!-- Agents read this first. The <<LEAD_SHORT>> writes it last, from the sections below, and updates it in the same edit as any change to this file. Max 10 lines (this comment not counted); no {{ }} once approved.
Example (fictional). Good: "- Serves: solo physiotherapists in their first 3 years who get patients only through referrals." Bad: "- Serves: people who want to feel better." -->
- Business: {{business_name}}: {{what_it_does_in_one_line}}
- Founder: {{founder_names}}, referred to as {{how_to_refer_to_them}}
- Sells: {{product_and_service_lines_in_one_line}}
- Serves: {{ideal_customer_in_one_line}}
- Main revenue driver: {{offer_name}}
- Core belief: {{top_belief_in_one_line}}
- Against: {{top_practice_or_myth_we_reject}}
- Different: {{top_differentiator}} ({{backing entry ID or needs proof}})

## What we sell
<!-- One bullet per product or service line: its name + what the customer gets, 1 line each. Add a price only when the client gives it and wants the team to use it; a price is a claim the QA Agent checks.
Example (fictional). Good: "Quarterly tax filing for freelancers: we prepare it, you sign it." Bad: "Financial services." -->
- {{product_or_service_line}}: {{what_the_customer_gets_in_one_line}}
- {{product_or_service_line}}: {{what_the_customer_gets_in_one_line}}

## Who we serve
<!-- One paragraph of 2–4 sentences: who they are, the situation they are in, what they want. Concrete enough to picture one real person; never "anyone" or "everyone".
Example (fictional). Good: "Solo physiotherapists in their first 3 years who fill their diary only through referrals and want 5 new patients a week." Bad: "Anyone who wants to be healthier." -->
{{who_we_serve_in_2_to_4_sentences}}

## How we make money
<!-- Internal context for the <<LEAD_SHORT>> only: never put revenue figures or the mix into any output. List the revenue models, the rough mix if the client tracks it, and the offer that brings in the most revenue.
Example (fictional). Good: "Rough mix: retainers about 70%, one-off audits about 30%." Bad: "Rough mix: various streams." -->
- Revenue models: {{revenue_models: retainers / projects / products / courses / memberships / other}}
- Rough mix: {{percent_per_model, or not tracked}}
- Main revenue driver: {{offer_name}}

## What we believe
<!-- 3–7 beliefs, each "We believe X because Y", in the client's own reasoning. They guide every judgment call and every opinion an output states, so each must be specific enough that a reasonable person could disagree.
Example (fictional). Good: "We believe clients must own their data because switching providers must never cost a year of history." Bad: "We believe in quality." -->
1. We believe {{belief}} because {{reason}}.
2. We believe {{belief}} because {{reason}}.
3. We believe {{belief}} because {{reason}}.

### What we're against
<!-- 3–7 bad practices or industry myths the client rejects, each with why it hurts the customer; no output ever recommends them. Name practices, never companies or people.
Example (fictional). Good: "We're against 12-month lock-in contracts because they protect the agency, not the client." Bad: "We're against bad agencies." -->
- We're against {{practice_or_myth}} because {{why_it_hurts_the_customer}}.
- We're against {{practice_or_myth}} because {{why_it_hurts_the_customer}}.
- We're against {{practice_or_myth}} because {{why_it_hurts_the_customer}}.

## What makes us different
<!-- 3–5 differentiators, each a fact a buyer could check, each ending with its backing: the ID of an approved bank entry that proves it, or "needs proof". The <<LEAD_SHORT>> never puts a "needs proof" line into a ticket as a claim.
Example (fictional). Good: "Work starts within 5 business days, with no onboarding fee". Bad: "We care more than others". -->
1. {{differentiator}} · {{backing entry ID or needs proof}}
2. {{differentiator}} · {{backing entry ID or needs proof}}
3. {{differentiator}} · {{backing entry ID or needs proof}}

## Key facts
<!-- Client-confirmed facts only. Numbers and credentials are claims (rule 7 in [[00-START-HERE]]): an output states one only when its row says yes, and names the backing entry when one exists. Confirmed by client: yes, or no (Q-###); nobody uses a no row. The timezone must match [[01-brain/plan#Rhythm]].
Example (fictional). Good: "Founded | 2019 | yes". Bad: "Founded | a while ago | yes". -->

| Fact | Value | Confirmed by client (yes/no) |
|---|---|---|
| Business name (exact spelling) | {{business_name}} | {{yes/no}} |
| Founder name(s) and how to refer to them | {{founder_names}} · refer to as {{first_name / full_name / title_and_surname}} | {{yes/no}} |
| Location and timezone | {{city_and_country}} · {{iana_timezone}} | {{yes/no}} |
| Founded | {{year}} | {{yes/no}} |
| Team size | {{number_of_people}} | {{yes/no}} |
| Website | {{website_url}} | {{yes/no}} |
| Social handles | {{platform}}: {{handle}}; {{platform}}: {{handle}} | {{yes/no}} |
| Key numbers (only confirmed ones) | {{number_and_what_it_counts}} (backing: {{entry ID, or none}}) | {{yes/no}} |
| Certifications / credentials | {{credential}} (backing: {{entry ID, or none}}) | {{yes/no}} |
| Origin (1–2 sentences) | {{origin_in_1_to_2_sentences}} Full story: {{entry ID, or none}} | {{yes/no}} |

<!-- FILL: only if team.json lists extra sections for company.md after "Key facts": for each one, in order, write "## <Section>" exactly as in team.json, then a guidance comment in the style of the sections above (what goes here, a count range, who reads it, and a last line "Example (fictional). Good: "..." Bad: "..."" with no em dashes), then a placeholder body of 2 to 5 lines with {{snake_case}} placeholders. Otherwise delete this comment. Source: team.json brain_files[company.md].sections after the 6 core sections; TEAM-SPEC brain files. Length: 3 to 12 body lines per section. Example: kit/The-Almanac/01-brain/company.md ## What makes us different. -->

## Open questions
<!-- Pointers only: each question lives in [[06-log/open-questions]], which is always the full list. Update pointers only while drafting in setup or inside an approved brain change. "- none" when empty.
Example (fictional). Good: "- Q-004 · What year did the business start? (see [[06-log/open-questions]])". Bad: "- founding year??". -->
- Q-### · {{question}} (see [[06-log/open-questions]])

## Changelog
<!-- Newest first, one line per version; never edit old lines. Format: - vN · YYYY-MM-DD · {{change}} ({{E-### | client request | setup}}); client request = any other change the client approved (monthly review, post-delivery proposals, answered questions).
Every approved version: version +1, updated and approved_on = that date, one line here.
Example (fictional). Good: "- v1 · 2026-09-25 · First approved version (setup)". Bad: "- updated stuff". -->
- v0 · template · installed from kit <<KIT_VERSION>>
