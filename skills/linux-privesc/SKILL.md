---
name: linux-privesc
description: >
  Use when, from an authorized low-privilege Linux foothold, assessing privilege-
  escalation exposure — misconfigurations (sudo, SUID, capabilities, cron, writable
  paths), kernel/service exposure, and credential reuse. Enumeration + detection +
  remediation focus.
type: knowledge
domain: offensive/post-exploitation
maturity: canonical
tools: [linpeas]
references:
  - _shared/scope-authorization-rule.md
  - _shared/safe-execution-rules.md
  - _shared/untrusted-input-rule.md
  - _shared/evidence-confidence-rule.md
  - _shared/gated-workflow-rule.md
license: MIT
version: 1.0.0
---

# Linux Privilege Escalation Assessment (authorized)

From an authorized low-priv foothold, enumerate the misconfigurations and exposures
that would let an attacker escalate — permissive sudo, dangerous SUID/capabilities,
writable service/cron paths, exposed secrets, and credential reuse — and
demonstrate one path minimally to prove the risk.

> Authorized testing only, on an in-scope host (`_shared/scope-authorization-rule.md`).
> Escalate minimally to prove the path; avoid destabilizing the host
> (`safe-execution-rules.md`).

## Prerequisites
- Authorization + scope; a low-priv shell. `export OUTPUT_DIR="${OUTPUT_DIR:-./output}" && mkdir -p "$OUTPUT_DIR"`.

## Procedure (gated phases)
1. **Enumerate** — sudo rights, SUID/SGID binaries, capabilities, cron jobs,
   writable files/paths in privileged contexts, services, kernel version, and
   stored credentials.
2. **Identify a path (core gate)** — map an enumerated misconfig to a concrete
   escalation (e.g., a sudo/SUID/cron/writable-path abuse).
3. **Demonstrate minimally** — prove the escalation to a higher privilege on the
   test host; stop at proof.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record `verdict`, the misconfig, and the
escalation proof. Hardened host (no path) → **refuted**.

## Impact escalation
Root/privileged control of the host, enabling credential access and lateral
movement. CVSS per `_shared/cvss-reference.md`.

## False positives & pitfalls
- A "finding" needing privileges you don't have isn't escalation — check the start
  point.
- Avoid changes that destabilize the host.

## Remediation
- Least-privilege sudo; remove unnecessary SUID/capabilities; secure cron/service
  paths (no writable privileged paths); patch kernel/services; no stored secrets;
  EDR/auditd monitoring.

## References
- `_shared/` rules (authorization, safe execution, untrusted input, evidence, gates).
