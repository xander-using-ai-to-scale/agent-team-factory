---
type: template
name: qa-report
kit_version: <<KIT_VERSION>>
---

# Template: QA report (qa-report.md)

Each <<OUTPUT_UNIT>> has one `05-outputs/{{output_id}}/qa-report.md`. Whoever runs the first QA check of the <<OUTPUT_UNIT>> creates it from the first block below (normally the QA Agent; the <<LEAD_SHORT>> in packet mode or mode fallback). The QA Agent then appends one section per checked file per round, in the order it checks them (newest at the bottom). The QA Agent's full method, and the authoritative section format, are in [[04-agents/qa-agent]] → Output template.

## The file (created before the first section)

```markdown
---
type: qa-report
output_id: {{output_id}}
updated: {{YYYY-MM-DD}}
---

# QA report · {{output_id}}
```

## One section (appended per file per round)

```markdown
## {{file name}} · round {{n}} · {{PASS | FIX | FAIL}}
1. Receipt and reading · {{pass | FAIL: hits}}
2. Ticket followed · {{pass | FAIL: hits}}
3. No invention · {{pass | FAIL: hits}}
4. Claims and areas to avoid · {{pass | FAIL: hits}}
5. Privacy · {{pass | FAIL: hits}}
6. Voice · {{pass | FAIL: hits}}
7. Format and completeness · {{pass | FAIL: hits}}
8. Authority · {{pass | FAIL: hits}}
9. Dependencies and consistency · {{pass | FAIL: hits}}
10. Placeholders and markers · {{pass | FAIL: hits}}
<!-- FILL: the same team check lines (11 and up) as in the Output template of 04-agents/qa-agent.md, word for word. Write nothing when that file has no team check. Source: 04-agents/qa-agent.md "Output template". Length: one line per team check. Example: the 10 lines above. -->
Fixes (exact):
{{1. … (one numbered line per fix) | none}}
Check before using: {{none | item; item}}
```

## Rules

1. One section per file per round. Never edit an earlier section. Add a new one for the next round.
2. The verdict in the heading must match the checks: PASS only when every check passes.
3. Every FAIL line quotes the exact problem text.
4. The `Check before using:` line of each file's last section feeds `## Check before using` in `DELIVERY.md`.
5. <<LEAD_SHORT>> fallback: when the <<LEAD_SHORT>> runs the checks itself, the first line under the section heading is `QA by <<LEAD_SHORT>> (fallback)`.
6. After writing a section, update `updated` in the frontmatter.
