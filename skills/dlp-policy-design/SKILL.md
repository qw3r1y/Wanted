---
name: dlp-policy-design
description: >
  Use when designing Data Loss Prevention policies — detecting and controlling
  sensitive-data movement across endpoints, email, and cloud, balancing protection
  with false positives. Covers DLP policy design and tuning.
type: knowledge
domain: data-privacy
maturity: canonical
tools: []
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# DLP Policy Design

Design Data Loss Prevention policies that detect and control sensitive-data egress —
via email, endpoints, web uploads, and cloud — accurately enough to stop real
leakage without drowning the business in false positives. DLP lives or dies on
tuning.

## When to use
When implementing/maturing DLP for classified sensitive data.

## Procedure (gated phases)
1. **Target data** — which classified data (from data-classification) to protect and
   on which channels (email/endpoint/web/cloud).
2. **Detection** — patterns + context + classification labels (not pattern-only);
   exact-data-match for high-value sets.
3. **Response per risk** — monitor/alert vs block; start in monitor mode to tune
   before enforcing.
4. **Tune** — reduce false positives with context/exceptions; measure precision.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. "Done" = catches real exfiltration with
acceptable FPs; tested in monitor mode first.

## Quality bar / pitfalls
- Pattern-only DLP → high FPs / business friction.
- Blocking before tuning → disruption.

## Linkage
- Consumes data-classification/pii-discovery; pairs with email-security, cloud DLP.

## References
- `_shared/` rules (evidence).
