---
name: wallet-security
description: >
  Use when assessing wallet/key-management security in a web3 context — approval
  risks, signing UX (blind signing), key storage, and smart-contract-wallet logic —
  to reduce user fund-loss risk. Covers wallet and approval security.
type: knowledge
domain: blockchain-web3/defi-infra
maturity: canonical
tools: []
references:
  - _shared/scope-authorization-rule.md
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Wallet & Approval Security

Many user losses come not from protocol bugs but from wallet-level risks — unlimited
token approvals to malicious contracts, blind-signing opaque transactions, phishing
dApps, and key mismanagement. Assess these risks and the security of
smart-contract-wallet logic.

> Authorized review (`_shared/scope-authorization-rule.md`).

## When to use
Reviewing a dApp's signing/approval UX, a smart-contract wallet, or user key
practices.

## Procedure (gated phases)
1. **Approval risk** — does the dApp request unlimited/broad token approvals? Can
   users scope/revoke them? Malicious-approval phishing exposure.
2. **Signing UX** — are users blind-signing opaque payloads? Is transaction intent
   clearly presented (what is being authorized)?
3. **Key management** — storage of keys/seeds; hardware vs hot; recovery; for
   contract wallets, the account logic (owners, recovery, modules).
4. **Smart-contract-wallet logic** — audit multisig/recovery/module logic for
   access-control flaws.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record risks (broad approvals, blind signing,
weak key handling) + impact.

## Impact escalation
User fund loss via malicious approvals/signatures or key compromise. CVSS/impact per
`_shared/cvss-reference.md`.

## Remediation
- Scoped/revocable approvals (and prompt users); clear transaction intent (no blind
  signing); hardware keys; audited contract-wallet logic; phishing awareness.

## References
- `_shared/` rules (authorization, evidence).
