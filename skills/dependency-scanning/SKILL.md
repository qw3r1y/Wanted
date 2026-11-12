---
name: dependency-scanning
description: >
  Use when scanning dependencies for known-vulnerable components (SCA) —
  identifying vulnerable packages, assessing reachability/exploitability, and
  prioritizing upgrades. Covers SCA triage beyond raw CVE lists.
type: knowledge
domain: appsec/sast-dast
maturity: canonical
tools: [trivy, osv-scanner]
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Dependency Scanning (SCA)

Find known-vulnerable dependencies and — the hard part — prioritize them by real
risk, not raw CVE count: whether the vulnerable code is reachable, whether a fix
exists, and the component's exposure. Avoid drowning teams in unreachable
"criticals".

## When to use
Continuously in CI and as periodic audits of the dependency tree.

## Procedure (gated phases)
1. **Inventory & scan** — full (transitive) dependency tree vs vulnerability DBs
   (OSV/advisories).
2. **Assess reachability (first gate)** — is the vulnerable function actually used/
   reachable? Many SCA "criticals" are unreachable.
3. **Prioritize** — by reachability + exploitability (EPSS/KEV) + exposure + fix
   availability.
4. **Remediate** — upgrade/patch; where no fix, mitigate/accept with justification.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record findings with reachability +
priority; distinguish reachable from theoretical.

## Quality bar / pitfalls
- Treating every CVE as urgent (fatigue) — prioritize by reachability/exploitability.
- Ignoring transitive deps — scan the full tree.

## Deployment
- CI gate on high-priority reachable vulns; SBOM (sbom-generation); feed
  vulnerability-management.

## References
- `_shared/` rules (evidence).
