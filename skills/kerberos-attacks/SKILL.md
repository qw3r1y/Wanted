---
name: kerberos-attacks
description: >
  Use when testing an authorized AD for Kerberos-based attacks — Kerberoasting
  (SPN service tickets), AS-REP roasting (no-preauth accounts), and ticket abuse —
  focused on identifying crackable/abusable accounts and the detection/remediation
  that closes them.
type: knowledge
domain: offensive/active-directory
maturity: canonical
tools: [impacket, hashcat]
references:
  - _shared/scope-authorization-rule.md
  - _shared/safe-execution-rules.md
  - _shared/untrusted-input-rule.md
  - _shared/evidence-confidence-rule.md
  - _shared/gated-workflow-rule.md
license: MIT
version: 1.0.0
---

# Kerberos Attacks (authorized)

Identify AD accounts exposed to Kerberos credential attacks — service accounts
with SPNs (Kerberoasting) and accounts without pre-authentication (AS-REP
roasting) — and demonstrate the risk (offline-crackable ticket) to drive
remediation. Cracking is done offline on retrieved tickets, bounded.

> Authorized testing only. Offline cracking stays bounded; do not use recovered
> credentials beyond proving the risk (`_shared/safe-execution-rules.md`).

## Prerequisites
- Authorization + scope; a domain context; SPN/no-preauth targets (from ad-recon).
  `export OUTPUT_DIR="${OUTPUT_DIR:-./output}" && mkdir -p "$OUTPUT_DIR"`.

## Procedure (gated phases)
1. **Enumerate targets** — accounts with SPNs (Kerberoast) and accounts flagged
   "do not require pre-auth" (AS-REP).
2. **Request tickets** — obtain the relevant service/AS-REP tickets for those
   accounts.
3. **Offline crack (bounded)** — attempt to crack weak account passwords offline;
   success proves the exposure. Keep wordlists/time bounded.
4. **Assess reach** — a cracked privileged/service account's access (what it
   unlocks) — enough to show impact, not to exploit broadly.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record `verdict`, the account(s), and the
crack proof (or that strong passwords resisted → **refuted** for those).

## Impact escalation
Service/account compromise, privilege escalation, and lateral movement from
cracked credentials. CVSS per `_shared/cvss-reference.md`.

## False positives & pitfalls
- Strong passwords resist cracking → risk is lower; report the exposure anyway.
- Don't reuse cracked creds beyond the minimal proof.

## Remediation
- Strong, long passwords / gMSAs for service accounts; remove unnecessary SPNs;
  require pre-authentication; monitor for roasting (ticket request patterns);
  tier/limit service-account privileges.

## References
- `_shared/` rules (authorization, safe execution, untrusted input, evidence, gates).
