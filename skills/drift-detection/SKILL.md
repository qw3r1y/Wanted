---
name: drift-detection
description: >
  Use when detecting and responding to infrastructure drift — differences between
  IaC-defined state and the actual cloud, which can introduce or hide security
  misconfigurations. Covers drift monitoring and reconciliation.
type: knowledge
domain: cloud-infra/iac
maturity: canonical
tools: [terraform]
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Infrastructure Drift Detection

Detect when the running cloud no longer matches its IaC — manual "fixes", console
changes, or attacker modifications — because drift both reintroduces
misconfigurations and hides unauthorized changes. Detect, assess, and reconcile.

## When to use
Continuously, for IaC-managed environments.

## Procedure (gated phases)
1. **Compare state** — periodically diff actual cloud vs IaC-defined state.
2. **Assess drift (core)** — classify each difference: benign, security-relevant
   (e.g., a security group opened), or **suspicious** (unauthorized change →
   possible incident, feeds cloud-IR).
3. **Reconcile** — re-apply IaC to remove benign/misconfig drift; investigate
   suspicious drift before reverting (preserve evidence).
4. **Prevent** — restrict console changes; require changes via IaC/pipeline.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. "Done" = drift is detected and triaged;
security-relevant drift is reconciled or investigated.

## Quality bar / pitfalls
- Auto-reverting suspicious drift destroys incident evidence — triage first.
- No drift detection → silent misconfigurations.

## Linkage
- Pairs with cspm-posture, cloud-incident-response; enforce IaC-only changes.

## References
- `_shared/` rules (evidence).
