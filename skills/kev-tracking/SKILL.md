---
name: kev-tracking
description: >
  Use when tracking known-exploited vulnerabilities (e.g., CISA KEV) against the
  environment — rapidly identifying and prioritizing vulns under active exploitation
  that affect owned assets. Covers KEV-driven urgent remediation.
type: knowledge
domain: vulnerability-management
maturity: canonical
tools: []
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Known-Exploited Vulnerability (KEV) Tracking

Vulnerabilities under **active exploitation** are the highest-urgency category.
Continuously match KEV catalogs (CISA KEV and threat-intel) against your asset/
software inventory to find and drive emergency remediation of what attackers are
exploiting right now.

## When to use
Continuously, as an urgent lane in vulnerability management.

## Procedure (gated phases)
1. **Ingest KEV sources** — CISA KEV + threat-intel on actively-exploited CVEs.
2. **Match to inventory (core)** — cross-reference against your software/asset
   inventory (SBOM, asset DB, EASM) to find affected assets fast.
3. **Confirm exposure** — is the affected component present and reachable? (validate,
   don't assume from version alone).
4. **Emergency remediate** — expedite patch/mitigation on confirmed-affected,
   especially internet-facing assets; hunt for prior exploitation (threat-hunting).

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record affected assets + remediation status;
confirm exposure before escalating.

## Impact / output
Rapid closure of actively-exploited exposure and detection of prior compromise.

## Pitfalls
- Slow inventory matching (the bottleneck) — keep SBOM/inventory current.
- Patching without checking for prior exploitation — hunt too.

## Linkage
- Consumes SBOM/EASM inventory; feeds patch-verification + threat-hunting.

## References
- `_shared/` rules (evidence).
