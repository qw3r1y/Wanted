---
name: oracle-manipulation
description: >
  Use when auditing a DeFi contract's price-oracle dependence — spot-price/AMM
  reliance manipulable via flash loans, stale/weak oracles — that enables
  under-collateralized borrowing or mispriced actions. Covers oracle-risk review.
type: knowledge
domain: blockchain-web3/smart-contract
maturity: canonical
tools: [foundry]
references:
  - _shared/scope-authorization-rule.md
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Oracle Manipulation

DeFi protocols that read a manipulable price (e.g., an AMM spot price) can be
attacked by moving that price within a transaction (often with a flash loan) to
borrow under-collateralized, liquidate unfairly, or mint mispriced assets. Audit how
prices are sourced and whether they can be moved.

> Authorized review; PoCs on fork/testnet (`_shared/scope-authorization-rule.md`).

## When to use
Auditing lending/AMM/derivatives contracts that depend on price feeds.

## Procedure (gated phases)
1. **Identify price sources** — where/how the contract gets prices (AMM spot, TWAP,
   external oracle) and what decisions depend on them.
2. **Assess manipulability (core)** — can the source be moved cheaply within a tx
   (spot price via a swap/flash loan)? Is it a single source, stale, or unguarded?
3. **PoC** — demonstrate a flash-loan-driven price move leading to profit/insolvency
   on a fork.
4. **Impact** — under-collateralized borrow, unfair liquidation, mispricing.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record the manipulable source + PoC. Robust
oracle (TWAP/decentralized, sanity checks) → **refuted**.

## Impact escalation
Protocol drain/insolvency via mispricing. Critical. CVSS per `_shared/cvss-reference.md`.

## Remediation
- Use robust oracles (decentralized feeds, TWAP) not spot prices; multiple sources +
  sanity/deviation checks; account for flash-loan-scale manipulation.

## References
- `_shared/` rules (authorization, evidence).
