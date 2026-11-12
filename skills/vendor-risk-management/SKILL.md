---
name: vendor-risk-management
description: >
  Use when assessing and managing third-party/vendor security risk — due diligence,
  tiering by risk, contractual controls, and ongoing monitoring — since vendors are
  a major breach vector. Covers third-party risk management.
type: knowledge
domain: grc
maturity: canonical
tools: []
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Third-Party / Vendor Risk Management

Your security is only as strong as your vendors' — supply-chain and third-party
breaches are a leading cause of incidents. Assess vendors by the risk they pose
(access/data), apply proportional due diligence and contractual controls, and monitor
them over time, not just at onboarding.

## When to use
When onboarding vendors or building a third-party risk program.

## Procedure (gated phases)
1. **Tier by risk (core)** — classify vendors by data access + criticality; focus
   effort on high-risk ones (not equal scrutiny for all).
2. **Due diligence** — proportional assessment (questionnaires, SOC 2/certifications,
   security review) for the tier.
3. **Contractual controls** — security requirements, breach notification, right-to-
   audit, and data-handling terms (DPAs).
4. **Ongoing monitoring** — reassess periodically; monitor for vendor breaches +
   changes; offboard securely.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. "Done" = vendors tiered, assessed per risk,
contractually controlled, and monitored.

## Quality bar / pitfalls
- One-time onboarding assessment with no ongoing monitoring.
- Equal scrutiny for all vendors (wastes effort / misses high-risk).

## Linkage
- Pairs with supply-chain, data-privacy (processor terms); feeds risk-assessment.

## References
- `_shared/` rules (evidence).
