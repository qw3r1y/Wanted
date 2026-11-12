---
name: ntlm-relay-coercion
description: >
  Use when testing an authorized AD for NTLM relay and authentication coercion —
  poisoning/coercion to capture authentication and relay it to vulnerable services
  (LDAP/SMB/ADCS). Focused on identifying missing signing/mitigations and the
  remediation that closes relay paths.
type: knowledge
domain: offensive/active-directory
maturity: canonical
tools: [impacket, responder]
references:
  - _shared/scope-authorization-rule.md
  - _shared/safe-execution-rules.md
  - _shared/untrusted-input-rule.md
  - _shared/evidence-confidence-rule.md
  - _shared/gated-workflow-rule.md
license: MIT
version: 1.0.0
---

# NTLM Relay & Coercion (authorized)

Assess whether AD authentication can be captured (via name-resolution poisoning or
coercion) and **relayed** to services that lack signing/channel-binding (LDAP,
SMB, ADCS HTTP enrollment) — a common path to privilege escalation. The objective
is to prove the missing mitigation, bounded and coordinated.

> Authorized testing only, with care: poisoning/coercion affects the network.
> Coordinate scope/timing; keep it bounded and avoid disrupting production
> (`_shared/safe-execution-rules.md`).

## Prerequisites
- Authorization + scope + **explicit approval for network poisoning/coercion**; a
  network position. `export OUTPUT_DIR="${OUTPUT_DIR:-./output}" && mkdir -p "$OUTPUT_DIR"`.

## Procedure (gated phases)
1. **Identify relay targets (first gate)** — services without required signing/
   channel binding (SMB signing off, LDAP(S) without binding, ADCS web enrollment).
2. **Capture authentication** — via name-resolution poisoning or an approved
   coercion technique, obtain authentication from a host/account — bounded.
3. **Relay** — relay the captured auth to a vulnerable service to demonstrate the
   escalation (e.g., to ADCS for a certificate) — minimal proof.
4. **Assess impact** — what the relayed context grants.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record `verdict`, the missing mitigation,
and the relay proof. Signing/binding enforced everywhere → **refuted**.

## Impact escalation
Privilege escalation to domain-level (e.g., relay-to-ADCS → certificate →
authentication as a privileged principal). CVSS per `_shared/cvss-reference.md`.

## False positives & pitfalls
- SMB signing + LDAP channel binding + EPA enforced → relay **refuted**.
- Poisoning is disruptive/detectable — only within approved windows.

## Remediation
- Enforce SMB signing, LDAP channel binding + signing, and ADCS HTTPS/EPA; disable
  LLMNR/NBT-NS/mDNS; restrict coercion surfaces; monitor relay indicators.

## References
- `_shared/` rules (authorization, safe execution, untrusted input, evidence, gates).
