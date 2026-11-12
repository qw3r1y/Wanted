---
name: solidity-audit
description: >
  Use when auditing a Solidity/EVM smart contract — systematic review across the
  common vulnerability classes (reentrancy, access control, arithmetic, oracle,
  logic) plus tooling, to find and prioritize on-chain risk. Umbrella audit skill
  for smart contracts.
type: knowledge
domain: blockchain-web3/smart-contract
maturity: canonical
tools: [foundry, slither]
references:
  - _shared/scope-authorization-rule.md
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Smart Contract Audit (Solidity/EVM)

Review a smart contract for the classes of bugs that cause fund loss — reentrancy,
broken access control, arithmetic/logic errors, oracle manipulation, and
upgradeability flaws — combining manual review with tooling, and demonstrating
impact via test PoCs (Foundry) on a fork/testnet, never on mainnet funds.

> Authorized review; PoCs on local fork/testnet only (`_shared/scope-authorization-rule.md`).

## When to use
Auditing a contract/protocol, or reviewing changes before deployment.

## Procedure (gated phases)
1. **Understand the system** — the contracts, their roles, value flows, trust
   assumptions, and external dependencies (oracles, tokens).
2. **Automated pass** — static analysis (Slither) + fuzzing (Echidna/Foundry) to
   surface candidates.
3. **Manual review by class** — reentrancy, access control, arithmetic, oracle
   dependence, front-running/MEV, upgrade/delegatecall, signature handling
   (each has a dedicated skill).
4. **PoC & prioritize** — prove impactful findings with a Foundry PoC on a fork;
   prioritize by fund-loss potential.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Each finding: class, affected code, and a PoC/
impact. No exploitable path → **refuted**.

## Impact / output
Prioritized findings (fund loss, DoS, privilege) + fixes.

## Pitfalls
- Tool output without manual logic review (misses business-logic/economic bugs).
- Testing on mainnet — use forks/testnets.

## Remediation
- Checks-effects-interactions, access-control modifiers, safe math, robust oracles,
  reentrancy guards, and thorough testing + audits before deploy.

## References
- `_shared/` rules (authorization, evidence).
