---
name: ransomware-response
description: >
  Use when responding to a ransomware incident — rapid containment, scoping of
  encryption/exfiltration, identifying entry/strain, and recovery decisioning —
  with a structured, time-critical playbook. Covers the IR lifecycle for
  ransomware specifically.
type: knowledge
domain: defensive/dfir
maturity: canonical
tools: []
references:
  - _shared/evidence-confidence-rule.md
  - _shared/gated-workflow-rule.md
license: MIT
version: 1.0.0
---

# Ransomware Incident Response

Respond to active/recent ransomware with speed and structure: contain spread,
scope what is encrypted and whether data was exfiltrated (double-extortion),
identify the strain and entry vector, and support recovery decisions — all while
preserving evidence.

## When to use
On suspected/confirmed ransomware. Time-critical; coordinate with leadership/legal.

## Procedure (gated phases)
1. **Contain (gated)** — isolate affected hosts/segments to stop spread; disable
   compromised accounts; preserve evidence while containing.
2. **Scope** — which hosts/data are encrypted; identify exfiltration signs (large
   outbound transfers) for double-extortion assessment.
3. **Identify** — strain (ransom note/extensions/TTPs), entry vector (phish/RDP/
   vuln), and persistence — to prevent re-entry.
4. **Recover & harden** — support recovery from clean backups; close the entry
   vector; feed detections; coordinate reporting/notification.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record scope, exfiltration assessment, entry
vector, and evidence; mark confidence.

## Impact / output
Contained incident, scoped impact, identified root cause, and recovery/hardening
plan.

## Pitfalls
- Powering off hosts destroys memory evidence — capture before where feasible.
- Restoring before closing the entry vector → re-infection.
- Missing exfiltration (notification obligations) — check.

## Remediation / hardening
- Immutable/offline backups, MFA, patch entry vectors, segmentation, EDR, and
  tested recovery plans.

## References
- `_shared/` rules (evidence, gated workflow).
