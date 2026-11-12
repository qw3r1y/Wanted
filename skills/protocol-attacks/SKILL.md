---
name: protocol-attacks
description: >
  Use when testing authorized network services/protocols for weaknesses — SMB,
  SNMP, RDP, DNS, SMTP, and similar — covering misconfiguration, weak auth,
  information disclosure, and known-CVE exposure. Service-protocol-focused testing
  and remediation.
type: knowledge
domain: offensive/network
maturity: canonical
tools: [nmap]
references:
  - _shared/scope-authorization-rule.md
  - _shared/safe-execution-rules.md
  - _shared/untrusted-input-rule.md
  - _shared/evidence-confidence-rule.md
  - _shared/gated-workflow-rule.md
license: MIT
version: 1.0.0
---

# Network Protocol / Service Attacks (authorized)

Test exposed network services for protocol-level weaknesses — anonymous/weak
authentication, information disclosure, dangerous defaults, and known-CVE exposure
(SMB, SNMP, RDP, DNS, SMTP, LDAP, databases). The proof is unauthorized access or
disclosure via the service.

> Authorized testing only. Read-only posture; no destructive operations
> (`_shared/safe-execution-rules.md`).

## Prerequisites
- Authorization + scope; the service inventory (from network-scanning). `export OUTPUT_DIR="${OUTPUT_DIR:-./output}" && mkdir -p "$OUTPUT_DIR"`.

## Procedure (gated phases)
1. **Per-service enumeration** — for each exposed service, enumerate shares/
   objects/info reachable anonymously or with weak creds.
2. **Weakness tests (core)** — anonymous access, default/weak credentials, info
   disclosure (SNMP public, zone transfer, SMTP user enum), and known-CVE exposure
   based on version.
3. **Confirm access/disclosure** — demonstrate the unauthorized access/info
   minimally.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record `verdict`, the service, the
weakness, and proof. Hardened/authenticated service → **refuted**.

## Impact escalation
Data disclosure, unauthorized access, and footholds for lateral movement; known-CVE
exposure → exploitation (exploit-dev/post-exploitation). CVSS per `_shared/cvss-reference.md`.

## False positives & pitfalls
- Version-based CVE guess ≠ confirmed exploitable — validate carefully/non-
  destructively.
- Avoid destructive service operations.

## Remediation
- Disable anonymous access; strong auth; patch services; restrict SNMP/zone
  transfer; segment; monitor.

## References
- `_shared/` rules (authorization, safe execution, untrusted input, evidence, gates).
