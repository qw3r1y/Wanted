---
name: risk-based-scoring
description: >
  Use when building a risk-based vulnerability-management program — combining
  threat, exposure, and business-impact into a consistent risk score and SLAs, and
  measuring the program. Covers VM program design and metrics.
type: knowledge
domain: vulnerability-management
maturity: canonical
tools: []
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Risk-Based Vulnerability Management

Turn vulnerability handling into a measurable, risk-based program: a consistent
scoring model (threat × exposure × business impact), SLAs by risk tier, clear
ownership, and metrics that show risk going down over time — rather than chasing raw
counts.

## When to use
When maturing vulnerability management from ad-hoc scanning to a program.

## Procedure (gated phases)
1. **Scoring model** — define how threat (EPSS/KEV), exposure (reachability), and
   business impact (asset criticality/data) combine into a risk score.
2. **SLAs & ownership** — remediation timelines per risk tier; clear owners and
   escalation.
3. **Workflow** — intake → dedupe → prioritize (vuln-prioritization) → remediate →
   verify (patch-verification) → close.
4. **Metrics** — mean-time-to-remediate by tier, SLA adherence, risk reduction, and
   backlog trend; report to leadership.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. "Done" = consistent scoring, met SLAs, and
metrics showing risk reduction.

## Quality bar / pitfalls
- Measuring raw counts instead of risk/SLA — count isn't risk.
- No ownership/SLAs → stale backlog.

## Linkage
- Orchestrates prioritization/KEV/patch-verification; feeds reporting + grc.

## References
- `_shared/` rules (evidence).
