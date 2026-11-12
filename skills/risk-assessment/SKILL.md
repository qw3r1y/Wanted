---
name: risk-assessment
description: >
  Use when conducting a security risk assessment — identifying assets/threats/
  vulnerabilities, estimating likelihood and impact, and prioritizing treatment.
  The foundation of risk-based security and most frameworks. Covers risk-assessment
  methodology.
type: knowledge
domain: grc
maturity: canonical
tools: []
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Security Risk Assessment

Risk assessment underpins risk-based security and nearly every framework: identify
what matters (assets), what threatens it, and the vulnerabilities, then estimate
likelihood × impact to prioritize treatment — so effort and spend go where risk is
highest.

## When to use
As the basis for a security program, framework compliance, or a specific decision.

## Procedure (gated phases)
1. **Identify assets & value** — the information/systems that matter and their value/
   sensitivity.
2. **Threats & vulnerabilities** — relevant threats (from CTI) and the vulnerabilities/
   weaknesses that expose each asset.
3. **Estimate risk** — likelihood × impact per risk, using a consistent scale
   (qualitative or quantitative); account for existing controls.
4. **Treat & prioritize** — mitigate / accept / transfer / avoid, prioritized by risk;
   document the risk register.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Deliverable: a prioritized risk register with
justified ratings + treatment decisions.

## Quality bar / pitfalls
- Inconsistent/gut-feel ratings — use a defined, consistent method.
- A register that's written once and ignored — maintain it.

## Linkage
- Foundation for iso27001/soc2/nist-csf, vulnerability-management, and policy.

## References
- `_shared/` rules (evidence).
