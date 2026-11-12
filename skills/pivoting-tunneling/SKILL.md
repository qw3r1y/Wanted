---
name: pivoting-tunneling
description: >
  Use when, in an authorized engagement, assessing how far a foothold allows
  pivoting into segmented networks — port forwarding, SOCKS proxying, and tunneling
  through a compromised host — to demonstrate segmentation gaps. Scope-bounded;
  segmentation/remediation emphasis.
type: knowledge
domain: offensive/network
maturity: canonical
tools: [ssh, proxychains]
references:
  - _shared/scope-authorization-rule.md
  - _shared/safe-execution-rules.md
  - _shared/untrusted-input-rule.md
  - _shared/evidence-confidence-rule.md
  - _shared/gated-workflow-rule.md
license: MIT
version: 1.0.0
---

# Pivoting & Tunneling — Segmentation Assessment (authorized)

From an authorized foothold, determine what otherwise-unreachable networks/services
become accessible via pivoting (port forwarding, SOCKS, tunneling) — demonstrating
segmentation gaps that would let an attacker reach sensitive zones. The value is
proving reachability to drive segmentation.

> Authorized testing only. Stay within the approved network scope; reaching a new
> segment is itself a scope boundary — confirm it's in scope before pivoting
> further (`_shared/scope-authorization-rule.md`).

## Prerequisites
- Authorization + scope (which segments are in scope); an authorized foothold.
  `export OUTPUT_DIR="${OUTPUT_DIR:-./output}" && mkdir -p "$OUTPUT_DIR"`.

## Procedure (gated phases)
1. **Map adjacency** — from the foothold, discover reachable networks/hosts not
   reachable from the start position.
2. **Establish a pivot (bounded)** — set up port forwarding/SOCKS through the
   foothold to reach an in-scope internal service.
3. **Demonstrate reach** — access one in-scope internal service via the pivot to
   prove the segmentation gap; do not expand beyond scope.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record `verdict`, the segmentation gap, and
the reach proof. Proper segmentation (no cross-segment reach) → **refuted**.

## Impact escalation
Access to sensitive internal zones (databases, management, OT) that should be
isolated. CVSS per `_shared/cvss-reference.md`.

## False positives & pitfalls
- Reaching a new segment may be out of scope — verify before continuing.
- Keep tunnels minimal and documented.

## Remediation
- Enforce network segmentation and least-privilege east-west rules; restrict
  outbound from sensitive hosts; monitor for tunneling/proxy patterns; zero-trust
  segmentation (see cloud-infra/iac, zero-trust).

## References
- `_shared/` rules (authorization, safe execution, untrusted input, evidence, gates).
