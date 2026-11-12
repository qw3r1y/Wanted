---
name: executive-summary-writing
description: >
  Use when writing the executive summary of a security report — conveying risk,
  business impact, and priorities to leadership concisely, without jargon. Covers
  exec-level security communication.
type: knowledge
domain: reporting-docs
maturity: canonical
tools: []
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Executive Summary Writing

The executive summary is what leadership actually reads — and where security work
translates into decisions. Convey the overall risk, business impact, and top
priorities clearly and concisely, in business terms (not CVE lists or jargon), so
executives can prioritize and fund remediation.

## When to use
For the leadership-facing section of any assessment/pentest/audit report.

## Procedure (gated phases)
1. **Lead with the bottom line** — overall risk posture and the few things that matter
   most, up front.
2. **Business impact, not tech detail** — frame findings as business risk (data,
   money, operations, compliance), avoiding jargon.
3. **Prioritized recommendations** — the top actions, their impact, and rough effort —
   decision-ready.
4. **Concise & honest** — short; state what was/ wasn't tested and residual risk.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. "Good" = an executive can understand the risk
and decide priorities without the technical sections.

## Quality bar / pitfalls
- Jargon/CVE dumps execs can't action.
- Burying the key risk; overstating/understating severity.

## Linkage
- Tops the technical-finding-report; feeds remediation-roadmap decisions.

## References
- `_shared/` rules (evidence).
