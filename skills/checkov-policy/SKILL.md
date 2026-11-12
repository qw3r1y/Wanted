---
name: checkov-policy
description: >
  Use when authoring custom IaC security policies (e.g., Checkov custom checks) —
  encoding organization-specific guardrails for cloud resources into automated,
  testable policy. Covers custom policy authoring for IaC.
type: knowledge
domain: cloud-infra/iac
maturity: canonical
tools: [checkov]
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Custom IaC Policy (Checkov)

Encode your organization's cloud guardrails as custom IaC checks so they're enforced
automatically on every change — beyond the built-in rules, matching your specific
standards (required tags, approved regions, encryption settings, naming/network
rules).

## When to use
When built-in IaC checks don't cover org-specific requirements.

## Procedure (gated phases)
1. **Define the guardrail** — the specific requirement (e.g., all storage encrypted
   with CMK, no 0.0.0.0/0 on sensitive ports).
2. **Write the check** — a custom policy (Python/YAML) matching the resource +
   condition.
3. **Test** — against compliant + non-compliant IaC fixtures; control FPs.
4. **Enforce** — add to the CI IaC scan as a gate.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. "Done" = flags non-compliant IaC, passes
compliant; tested.

## Quality bar / pitfalls
- Over-broad checks → FPs; too-narrow → gaps.
- Not testing the policy against fixtures.

## Deployment
- Ship with the IaC scan (terraform-security-scan); version; align to grc controls.

## References
- `_shared/` rules (evidence).
