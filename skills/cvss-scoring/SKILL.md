---
name: cvss-scoring
description: >
  Use when scoring a vulnerability's severity with CVSS — selecting metrics correctly
  and justifying the vector, for consistent, defensible severity in reports. Covers
  CVSS application (shared reference for all reporting).
type: knowledge
domain: bug-bounty
maturity: canonical
tools: []
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# CVSS Scoring

Score severity consistently and defensibly with CVSS: choose each metric based on the
**demonstrated** impact and attack conditions, and justify the vector — so severity
reflects reality, not optimism, and holds up to triage/review.

## When to use
When assigning severity to any finding (bounty or assessment).

## Procedure (gated phases)
1. **Base metrics from reality** — attack vector/complexity, privileges/interaction
   required, and the actual confidentiality/integrity/availability impact you
   **demonstrated** (not the theoretical worst case).
2. **Scope** — did the impact cross a security scope/authority boundary? (affects the
   score significantly).
3. **Justify the vector** — document why each metric value, tied to evidence.
4. **Context** — note environmental/business context that adjusts real risk (even if
   base CVSS stays fixed).

## Verification & evidence
`_shared/evidence-confidence-rule.md`. The score is backed by the demonstrated impact;
each metric is justified.

## Impact / output
Consistent, defensible severity that triage accepts.

## Pitfalls
- Inflating metrics beyond what was demonstrated (triage downgrades → lost trust).
- Mis-setting Scope / privileges-required.

## Linkage
- Used by finding-triage, technical-finding-report, and all reporting; the shared
  severity method.

## References
- `_shared/` rules (evidence).
