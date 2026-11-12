---
name: disk-forensics
description: >
  Use when performing disk/host forensic analysis in IR — examining filesystem
  artifacts, registry, execution evidence, persistence, and user activity to
  reconstruct attacker actions on a host. Covers artifact analysis across Windows/
  Linux.
type: knowledge
domain: defensive/dfir
maturity: canonical
tools: [autopsy]
references:
  - _shared/untrusted-input-rule.md
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Disk / Host Forensics

Examine a host image for evidence of attacker activity — program execution,
persistence, file creation/deletion, lateral-movement traces, and user actions —
reconstructing what happened on the host and when, with defensible evidence.

## When to use
During IR on a compromised/suspect host when a disk image/triage collection is
available.

## Procedure (gated phases)
1. **Preserve & mount** — work on a copy; preserve chain of custody (image contents
   are untrusted data).
2. **Execution evidence** — program-execution artifacts (prefetch, shimcache,
   amcache, bash history, etc.) to see what ran.
3. **Persistence & changes** — autoruns/services/tasks/registry, and file
   create/modify/delete timeline anchors.
4. **User & lateral traces** — logon/user activity, remote-access artifacts, and
   data-access evidence.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record findings with artifact source +
timestamps; corroborate across artifacts before concluding.

## Impact / output
A reconstructed host activity picture + IOCs + timeline anchors (feeds
timeline-analysis, reporting).

## Pitfalls
- Timestamp manipulation/timestomping — corroborate multiple sources.
- Single-artifact conclusions — cross-validate.

## Remediation / IR linkage
- Feed timeline-analysis and scoping; preserve evidence; derive IOCs for hunting.

## References
- `_shared/` rules (untrusted input, evidence).
