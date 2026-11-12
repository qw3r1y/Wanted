---
name: alert-triage-automation
description: >
  Use when automating alert triage/enrichment — auto-enriching alerts with context
  (asset, user, threat-intel), scoring/deduplicating, and auto-closing clear false
  positives — to cut analyst load while keeping a human gate on consequential
  actions. Covers enrichment and automation design.
type: knowledge
domain: defensive/blue-team-ops
maturity: canonical
tools: []
references:
  - _shared/evidence-confidence-rule.md
  - _shared/gated-workflow-rule.md
license: MIT
version: 1.0.0
---

# Alert Triage & Enrichment Automation

Automate the repetitive front of triage — enrich each alert with asset/user/intel
context, score and deduplicate, and auto-dismiss unambiguous false positives — so
analysts focus on real decisions. Keep consequential actions (containment) behind a
human gate.

## When to use
When alert volume outpaces analysts, or triage context-gathering is manual/slow.

## Procedure (gated phases)
1. **Enrichment** — on each alert, automatically add asset criticality, user
   context, threat-intel reputation (cti), and related alerts.
2. **Scoring & dedup** — score by severity + context; group/deduplicate related
   alerts into incidents.
3. **Safe auto-actions (gated)** — auto-close only clearly benign patterns; never
   auto-contain without a human gate for consequential actions.
4. **Handoff** — present enriched, scored incidents to analysts with the playbook.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. "Done" = enrichment is reliable and
auto-close only fires on well-validated benign cases. Measure precision.

## Quality bar / pitfalls
- Auto-closing real alerts (dangerous) — be conservative; audit auto-closures.
- Over-automation of containment — keep a human gate (`gated-workflow-rule.md`).

## Governance
- Audit auto-actions; measure false auto-close rate; iterate enrichment sources.

## References
- `_shared/` rules (evidence, gated workflow).
