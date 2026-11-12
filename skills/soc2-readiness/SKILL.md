---
name: soc2-readiness
description: >
  Use when preparing for a SOC 2 audit — mapping the Trust Services Criteria to
  controls, finding gaps, and building the evidence/process needed to pass. Covers
  SOC 2 readiness (implementation, not legal/audit opinion).
type: knowledge
domain: grc
maturity: canonical
tools: []
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# SOC 2 Readiness

Prepare for a SOC 2 audit by implementing and evidencing the controls behind the
Trust Services Criteria (security, and as scoped: availability, confidentiality,
processing integrity, privacy). Focus on real controls + repeatable evidence, not
just policy documents.

> Implementation guidance; the audit opinion comes from a licensed auditor.

## When to use
When pursuing SOC 2 (Type I/II) for the organization.

## Procedure (gated phases)
1. **Scope** — which Trust Services Criteria and systems are in scope.
2. **Map criteria → controls** — the actual controls (access control, change
   management, monitoring, IR, vendor management) that satisfy each criterion.
3. **Gap assessment** — where controls are missing/weak or lack evidence; remediate.
4. **Evidence & operation (core for Type II)** — controls must operate over time with
   collectable evidence (logs, tickets, reviews); automate evidence where possible.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. "Ready" = controls implemented + operating +
evidenced; gaps closed.

## Quality bar / pitfalls
- Policies without operating controls/evidence (Type II tests operation over time).
- Over-scoping; manual evidence that doesn't scale.

## Linkage
- Consumes many technical controls (identity, detection, VM); feeds risk-assessment +
  metrics.

## References
- `_shared/` rules (evidence).
