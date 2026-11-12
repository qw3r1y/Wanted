---
name: windows-privesc
description: >
  Use when, from an authorized low-privilege Windows foothold, assessing privilege-
  escalation exposure — service/registry/path misconfigurations, token/privilege
  abuse, unquoted paths, AlwaysInstallElevated, and credential exposure.
  Enumeration + detection + remediation focus.
type: knowledge
domain: offensive/post-exploitation
maturity: canonical
tools: [winpeas]
references:
  - _shared/scope-authorization-rule.md
  - _shared/safe-execution-rules.md
  - _shared/untrusted-input-rule.md
  - _shared/evidence-confidence-rule.md
  - _shared/gated-workflow-rule.md
license: MIT
version: 1.0.0
---

# Windows Privilege Escalation Assessment (authorized)

From an authorized low-priv Windows foothold, enumerate the misconfigurations and
exposures enabling escalation — insecure service permissions/paths, registry
autoruns, dangerous privileges/tokens, unquoted service paths,
AlwaysInstallElevated, and stored credentials — and demonstrate one path minimally.

> Authorized testing only, on an in-scope host. Escalate minimally; avoid host
> instability (`_shared/safe-execution-rules.md`).

## Prerequisites
- Authorization + scope; a low-priv session. `export OUTPUT_DIR="${OUTPUT_DIR:-./output}" && mkdir -p "$OUTPUT_DIR"`.

## Procedure (gated phases)
1. **Enumerate** — service permissions/binary paths, unquoted paths, registry
   autoruns, scheduled tasks, held privileges/tokens (SeImpersonate etc.),
   AlwaysInstallElevated, writable privileged locations, and stored creds.
2. **Identify a path (core gate)** — map a misconfig to a concrete escalation
   (service/path/token/registry abuse).
3. **Demonstrate minimally** — prove escalation to a higher privilege on the test
   host.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record `verdict`, the misconfig, and proof.
Hardened host → **refuted**.

## Impact escalation
SYSTEM/admin control, credential access, and lateral movement. CVSS per
`_shared/cvss-reference.md`.

## False positives & pitfalls
- Escalation requiring privileges you lack isn't a finding — verify start point.
- Avoid destabilizing changes.

## Remediation
- Secure service/registry permissions and quote paths; remove AlwaysInstallElevated;
  restrict dangerous privileges; patch; no stored creds (LAPS); EDR + audit
  monitoring.

## References
- `_shared/` rules (authorization, safe execution, untrusted input, evidence, gates).
