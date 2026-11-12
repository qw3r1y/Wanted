---
name: dependency-audit
description: >
  Use when auditing the health and trust of third-party dependencies beyond CVEs —
  maintenance status, provenance, permissions/behaviour, and risk of each package —
  to reduce supply-chain exposure. Covers holistic dependency risk review.
type: knowledge
domain: appsec/supply-chain
maturity: canonical
tools: []
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Dependency Trust Audit

Go beyond "does it have a CVE": assess each (especially new/critical) dependency's
**trustworthiness** — maintenance, popularity, provenance, maintainer practices,
and whether it does more than it should (postinstall scripts, network access) — to
reduce the risk of a compromised or malicious package.

## When to use
When adding dependencies and periodically auditing critical ones.

## Procedure (gated phases)
1. **Inventory & prioritize** — focus on direct/critical and recently-added
   dependencies.
2. **Trust signals** — maintenance activity, maintainer count/reputation, download
   trends, and known incidents; prefer well-maintained libs.
3. **Behaviour check** — install/build scripts, network/filesystem access, and
   permissions disproportionate to purpose (feeds malicious-dependency-detection).
4. **Decide** — approve, pin + monitor, or replace; document the decision.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record per-dependency risk + decision.

## Quality bar / pitfalls
- Judging only by CVEs (misses abandonment/malice).
- Deep transitive chains hiding risky packages — consider the tree.

## Linkage
- Pairs with dependency-scanning, sbom-generation, malicious-dependency-detection.

## References
- `_shared/` rules (evidence).
