---
name: slither-echidna-analysis
description: >
  Use when running automated smart-contract analysis — static analysis (Slither) and
  property-based fuzzing (Echidna) to surface vulnerabilities and invariant
  violations, and interpreting results. Covers automated contract analysis.
type: knowledge
domain: blockchain-web3/tooling
maturity: canonical
tools: [slither, echidna]
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Automated Contract Analysis (Slither + Echidna)

Use static analysis (Slither) to surface known bug patterns and property-based
fuzzing (Echidna) to find inputs that violate your protocol invariants — the
automated backbone of an audit — then validate and prioritize the results manually.

## When to use
Early and continuously in a smart-contract audit/development.

## Procedure (gated phases)
1. **Static analysis** — run Slither; triage detectors (reentrancy, access,
   arithmetic, etc.); filter FPs.
2. **Define invariants** — the properties that must always hold (e.g., total supply
   conservation, no insolvency).
3. **Fuzz (Echidna)** — write the invariants as properties; fuzz to find violating
   sequences.
4. **Validate & prioritize** — confirm real issues manually; feed to Foundry PoC +
   the specific audit skill.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record detector hits + invariant violations;
validate before treating as confirmed.

## Quality bar / pitfalls
- Trusting raw detector output (FPs) — triage.
- Weak/incomplete invariants — fuzzing is only as good as the properties.

## Linkage
- Feeds solidity-audit + specific class skills; pairs with foundry-poc.

## References
- `_shared/` rules (evidence).
