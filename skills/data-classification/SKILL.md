---
name: data-classification
description: >
  Use when designing/applying a data classification scheme — defining sensitivity
  levels and labeling data so controls (access, encryption, retention, DLP) can be
  applied consistently. Covers classification program design.
type: knowledge
domain: data-privacy
maturity: canonical
tools: []
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Data Classification

Define a practical classification scheme (e.g., Public / Internal / Confidential /
Restricted) and apply it so that security controls follow the data's sensitivity
automatically — the organizing principle behind access control, encryption,
retention, and DLP.

## When to use
When building a data-protection program or standardizing how data is handled.

## Procedure (gated phases)
1. **Define levels** — a small, clear set of sensitivity levels with concrete
   examples and handling rules per level.
2. **Map controls to levels** — required access, encryption, retention, sharing, and
   DLP per classification.
3. **Apply labels** — classify data (from pii-discovery); automate labeling where
   possible.
4. **Operationalize** — enforce control differences by level; train staff.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. "Done" = data is labeled and controls follow
the labels consistently.

## Quality bar / pitfalls
- Too many levels (unusable) or purely theoretical (unapplied).
- Labels without enforced control differences.

## Linkage
- Consumes pii-discovery; drives dlp-policy, access control, encryption, retention.

## References
- `_shared/` rules (evidence).
