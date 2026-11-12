---
name: access-control-flaws
description: >
  Use when auditing smart-contract access control — missing/incorrect permission
  checks, unprotected critical functions, flawed ownership/role logic, and
  initialization issues — that let anyone perform privileged actions. Covers authz
  review for contracts.
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

# Smart Contract Access Control

Privileged functions (mint, withdraw, upgrade, pause, parameter changes) must be
properly restricted. Audit for missing/incorrect access checks, unprotected
initializers, flawed role/ownership logic, and `delegatecall`/proxy-admin issues
that let an attacker seize control or funds.

> Authorized review; PoCs on fork/testnet (`_shared/scope-authorization-rule.md`).

## When to use
Auditing contracts with privileged operations, upgradeability, or roles.

## Procedure (gated phases)
1. **Enumerate privileged functions** — state/fund/upgrade/parameter-changing
   functions and who should call them.
2. **Check protection (core gate)** — each has a correct modifier/check; test
   calling as a non-privileged account. Include **initializer** protection (can it
   be re-initialized / was it left open?).
3. **Role/ownership logic** — correct role assignment/transfer; no way to self-grant.
4. **PoC** — demonstrate an unauthorized privileged action on a fork.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record the unprotected function + PoC. Proper
checks → **refuted**.

## Impact escalation
Unauthorized mint/withdraw, protocol takeover (ownership/upgrade), fund loss.
Critical. CVSS per `_shared/cvss-reference.md`.

## Remediation
- Enforce access control on every privileged function (OZ AccessControl/Ownable);
  protect initializers (initializer modifier); secure upgrade/proxy admin; test authz.

## References
- `_shared/` rules (authorization, evidence).
