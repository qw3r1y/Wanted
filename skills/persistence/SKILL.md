---
name: persistence
description: >
  Use when, in an authorized engagement, assessing persistence exposure — the
  mechanisms by which an attacker could maintain access (autoruns, services,
  scheduled tasks, accounts, cloud/identity) — to validate detection and drive
  hardening. Detection/remediation framing; no lasting persistence on production.
type: knowledge
domain: offensive/post-exploitation
maturity: canonical
tools: []
references:
  - _shared/scope-authorization-rule.md
  - _shared/safe-execution-rules.md
  - _shared/untrusted-input-rule.md
  - _shared/evidence-confidence-rule.md
  - _shared/gated-workflow-rule.md
license: MIT
version: 1.0.0
---

# Persistence Exposure Assessment (authorized)

Assess how an attacker could persist in the environment and whether such mechanisms
would be detected — autoruns/services/scheduled tasks/accounts on hosts, and
identity/cloud persistence — to validate monitoring and drive hardening. Any
demonstration is minimal, reversible, and cleaned up; no lasting persistence on
production.

> Authorized testing only, coordinated with defenders. Demonstrate minimally and
> **remove** any test persistence; do not leave backdoors
> (`_shared/safe-execution-rules.md`).

## Prerequisites
- Authorization + scope + blue-team coordination; a foothold/lab. `export OUTPUT_DIR="${OUTPUT_DIR:-./output}" && mkdir -p "$OUTPUT_DIR"`.

## Procedure (gated phases)
1. **Enumerate mechanisms** — host (autoruns, services, scheduled tasks, startup
   items), account-based, and identity/cloud (OAuth app, access key, federation)
   persistence relevant to the environment.
2. **Detection validation (core)** — for a representative mechanism, test (in lab
   or with a benign, logged marker) whether creation/use is detected.
3. **Document & clean up** — record which mechanisms would be detected vs missed;
   remove any test artifacts immediately.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Deliverable: persistence detection-coverage
findings; confirm cleanup.

## Impact escalation
Undetected persistence = durable attacker access; closing detection gaps limits
dwell time.

## False positives & pitfalls
- Never leave real persistence on production; always clean up.
- Coordinate with defenders to avoid confusion/IR.

## Remediation
- Monitor autoruns/services/tasks/account and identity changes; alert on new OAuth
  apps/keys/federation; baseline + anomaly detection; least privilege; regular
  credential/app review.

## References
- `_shared/` rules (authorization, safe execution, untrusted input, evidence, gates).
