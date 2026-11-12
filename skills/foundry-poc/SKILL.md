---
name: foundry-poc
description: >
  Use when writing proof-of-concept exploits/tests for smart-contract findings with
  Foundry — fork testing, attacker contracts, and impact quantification on a local
  fork/testnet. Covers PoC construction for audits.
type: knowledge
domain: blockchain-web3/tooling
maturity: canonical
tools: [foundry]
references:
  - _shared/scope-authorization-rule.md
  - _shared/safe-execution-rules.md
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Foundry PoC Development

Prove a smart-contract finding with a concrete, reproducible PoC — using Foundry to
fork mainnet state, write an attacker contract/test, and quantify the impact (funds
drained, invariant broken) — so severity is demonstrated, not asserted. All on a
local fork/testnet, never against live funds.

> Authorized review; PoCs on local fork/testnet ONLY (`_shared/safe-execution-rules.md`).

## When to use
To demonstrate impact for any confirmed contract vulnerability.

## Procedure (gated phases)
1. **Set up the fork** — fork the relevant chain state at a block; configure the
   test environment.
2. **Write the attack** — an attacker contract/test reproducing the vulnerability
   (reentrancy, flash loan, oracle move, etc.).
3. **Quantify impact** — assert the concrete outcome (balance drained, state broken)
   with before/after.
4. **Document** — a minimal, reproducible PoC + the impact for the report.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. The PoC reproduces the exploit on the fork
with measured impact.

## Quality bar / pitfalls
- "Theoretical" findings without PoC — demonstrate real impact.
- Never run against mainnet with real funds.

## Linkage
- Used by all smart-contract/* audit skills to confirm severity.

## References
- `_shared/` rules (authorization, safe execution, evidence).
