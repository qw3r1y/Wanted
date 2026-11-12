---
name: metrics-kpi-dashboard
description: >
  Use when defining and presenting security metrics/KPIs — measures that show risk
  posture and program effectiveness to leadership, avoiding vanity metrics. Covers
  security metrics design.
type: knowledge
domain: reporting-docs
maturity: canonical
tools: []
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Security Metrics & KPIs

Good metrics drive the program and communicate value; bad ones (vanity counts)
mislead. Define measures that reflect actual **risk posture and effectiveness** —
mean-time-to-detect/respond/remediate, coverage, and risk trend — and present them so
leadership sees whether security is improving.

## When to use
When building security reporting/dashboards for leadership or program management.

## Procedure (gated phases)
1. **Pick outcome metrics** — MTTD/MTTR/MTTR-remediate, detection coverage (ATT&CK),
   vulnerability SLA adherence + risk trend, exposure (EASM), and incident metrics —
   tied to risk, not activity.
2. **Avoid vanity metrics** — raw counts (alerts, scans) without context mislead;
   contextualize.
3. **Set targets & trends** — targets per KPI; show trend over time (improving?).
4. **Present per audience** — exec (risk/trend) vs operational (detailed); make it
   actionable.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. "Good" = metrics reflect real risk/effectiveness
and drive decisions; data is accurate.

## Quality bar / pitfalls
- Vanity metrics (counts) presented as risk.
- Metrics no one acts on — tie to decisions.

## Linkage
- Consumes data from detection-coverage, vulnerability-management, easm, IR; feeds
  grc + leadership reporting.

## References
- `_shared/` rules (evidence).
