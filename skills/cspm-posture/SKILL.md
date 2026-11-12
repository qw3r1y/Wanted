---
name: cspm-posture
description: >
  Use when establishing continuous cloud security posture management — benchmarking
  against CIS/best practice, continuous misconfiguration detection, drift, and
  prioritized remediation across accounts. Covers CSPM program setup.
type: knowledge
domain: cloud-infra/cloud
maturity: canonical
tools: [prowler]
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Cloud Security Posture Management (CSPM)

Move from point-in-time audits to continuous posture: benchmark the environment
against CIS/best practice, continuously detect misconfigurations and drift across
all accounts, and drive prioritized remediation — so new exposures are caught fast,
not at the next audit.

## When to use
When operationalizing cloud security across multiple accounts/clouds.

## Procedure (gated phases)
1. **Baseline** — benchmark accounts against CIS/best-practice; record the posture.
2. **Continuous detection** — automated, ongoing checks for misconfigurations and
   drift from baseline across accounts.
3. **Prioritize** — by exploitability + data exposure (not raw check count);
   deduplicate across accounts.
4. **Remediate & track** — route to owners; track closure; prevent recurrence via
   guardrails (SCP/org-policy, IaC).

## Verification & evidence
`_shared/evidence-confidence-rule.md`. "Done" = continuous detection + prioritized,
tracked remediation. Record posture trend.

## Quality bar / pitfalls
- Alert floods without prioritization — rank by real risk.
- Detecting but not preventing recurrence — add guardrails + IaC policy.

## Linkage
- Consumes cloud audits; feeds iac policy + easm; preventive guardrails.

## References
- `_shared/` rules (evidence).
