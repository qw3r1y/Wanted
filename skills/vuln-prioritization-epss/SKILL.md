---
name: vuln-prioritization-epss
description: >
  Use when prioritizing vulnerabilities for remediation using EPSS and context —
  moving beyond CVSS-only to exploit-probability and environmental factors so teams
  fix what's actually likely to be exploited. Covers risk-based prioritization.
type: knowledge
domain: vulnerability-management
maturity: canonical
tools: []
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Vulnerability Prioritization (EPSS + context)

Most organizations can't patch everything; CVSS alone over-flags. Prioritize using
**EPSS** (probability of exploitation), **KEV** (known exploited), reachability, and
asset exposure/criticality — so remediation effort targets the small set of vulns
actually likely to be exploited in your environment.

## When to use
When triaging a large vulnerability backlog from scanners/SCA/pentests.

## Procedure (gated phases)
1. **Aggregate findings** — from scanners, SCA (dependency-scanning), cloud, and
   pentests; deduplicate.
2. **Enrich** — CVSS (severity), EPSS (exploit likelihood), KEV (actively exploited),
   and whether a public exploit exists.
3. **Add environmental context (core)** — reachability (internet-facing vs internal),
   asset criticality, and compensating controls.
4. **Rank & SLA** — prioritize KEV + high-EPSS + exposed-critical first; assign
   remediation SLAs by tier.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Prioritization is explainable per finding;
measure that high-priority = high-real-risk.

## Impact / output
A focused, defensible remediation queue instead of an unactionable CVSS dump.

## Pitfalls
- CVSS-only prioritization (patch everything "critical") → wasted effort.
- Ignoring reachability/exposure context.

## Linkage
- Consumes dependency-scanning, cve-weaponization, easm exposure; feeds patch-
  verification + reporting.

## References
- `_shared/` rules (evidence).
