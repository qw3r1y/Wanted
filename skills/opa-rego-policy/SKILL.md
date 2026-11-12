---
name: opa-rego-policy
description: >
  Use when writing OPA/Rego policies for policy-as-code — admission control (K8s),
  IaC/plan evaluation, or authorization — encoding security guardrails as testable
  policy. Covers Rego policy authoring and enforcement.
type: knowledge
domain: cloud-infra/iac
maturity: canonical
tools: [opa, conftest]
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Policy-as-Code (OPA / Rego)

Express security guardrails as testable Rego policy enforced by OPA — Kubernetes
admission (reject non-compliant pods), IaC/plan evaluation (conftest), or service
authorization — so rules are consistent, versioned, and automatically enforced.

## When to use
For admission control, IaC gating, or centralized authorization policy.

## Procedure (gated phases)
1. **Define the rule** — the allow/deny condition (e.g., deny privileged pods,
   require encryption, enforce authz).
2. **Write Rego** — the policy with clear deny/allow logic over the input document
   (pod spec, Terraform plan, request).
3. **Test** — `opa test` against compliant + violating inputs; cover edge cases.
4. **Enforce** — deploy at the enforcement point (admission webhook, CI conftest,
   service); fail-closed on violations.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. "Done" = policy correctly allows/denies test
inputs and is enforced at the right point.

## Quality bar / pitfalls
- Untested policies (logic bugs → bypass or outage); fail-open mistakes.
- Over-complex policies — keep readable + tested.

## Deployment
- K8s admission / CI conftest; version; align to pod-security + iac scanning.

## References
- `_shared/` rules (evidence).
