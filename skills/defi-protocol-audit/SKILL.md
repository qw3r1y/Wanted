---
name: defi-protocol-audit
description: >
  Use when auditing a DeFi protocol holistically — economic/invariant design,
  composability risk, oracle and flash-loan exposure, and governance — beyond
  single-contract bugs. Covers protocol-level economic security.
type: knowledge
domain: blockchain-web3/defi-infra
maturity: canonical
tools: [foundry]
references:
  - _shared/scope-authorization-rule.md
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# DeFi Protocol Audit (economic/system)

DeFi exploits are often economic, not just code bugs: broken invariants,
composability with other protocols, oracle/flash-loan exposure, and governance
capture. Audit the protocol as a system — its money flows, invariants, and external
dependencies — not just individual contracts.

> Authorized review; PoCs on fork/testnet (`_shared/scope-authorization-rule.md`).

## When to use
Auditing lending, AMM, vault, staking, or other DeFi protocols.

## Procedure (gated phases)
1. **Model the economics** — value flows, collateralization, incentives, and the
   invariants that keep it solvent.
2. **Stress the invariants** — can flash-loans/oracle moves/extreme inputs break
   solvency or extract value? (flash-loan-attacks, oracle-manipulation).
3. **Composability & external deps** — interactions with other protocols/tokens
   (fee-on-transfer, rebasing, callbacks) and their failure modes.
4. **Governance & admin** — parameter/upgrade powers and capture risk.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Each finding: the broken invariant/economic
flaw + PoC. Robust economics → **refuted**.

## Impact escalation
Insolvency, value extraction, governance capture. Critical. CVSS per
`_shared/cvss-reference.md`.

## Remediation
- Design flash-resistant invariants; robust oracles; careful composability
  assumptions; timelocked/decentralized governance; economic stress testing.

## References
- `_shared/` rules (authorization, evidence).
