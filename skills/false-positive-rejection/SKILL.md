---
name: false-positive-rejection
description: >
  Use when filtering out assets wrongly attributed to the organization — shared
  infrastructure, third-party/CDN/cloud assets, and defunct assets — so the EASM
  inventory stays accurate and avoids testing others' systems. The guardrail of
  EASM quality.
type: knowledge
domain: easm
maturity: canonical
tools: []
references:
  - _shared/scope-authorization-rule.md
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# False-Positive Rejection (EASM)

The flip side of attribution: actively reject candidates that look related but are
**not** the organization's — shared CDN/cloud IPs, SaaS/third-party assets,
parked/defunct domains, and coincidental matches — because a false asset in the
inventory wastes effort and, worse, risks testing someone else's systems.

> Rejecting wrong assets protects both accuracy and the boundary against
> unauthorized testing (`_shared/scope-authorization-rule.md`).

## When to use
Continuously, as a gate on attribution/discovery output.

## Procedure (gated phases)
1. **Shared-infra filters** — detect CDN/cloud/shared-hosting IP ranges and shared
   certificates where IP/cert ≠ ownership; don't attribute these on infra alone.
2. **Third-party/SaaS detection** — assets hosted/owned by vendors (the org uses but
   doesn't own) → not in-scope for testing.
3. **Defunct/parked** — expired/parked/sinkholed assets → flag/remove.
4. **Human review for ambiguous** — medium-confidence candidates get reviewed, not
   auto-included.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Each rejection is justified; measure
false-inclusion rate.

## Impact / output
A clean inventory free of misattributed/third-party assets — and a safer testing
boundary.

## Pitfalls
- Auto-including shared-infra assets → testing others' systems (serious).
- Over-rejecting real assets (false negatives) — balance with confidence-scoring.

## Linkage
- Works with confidence-scoring + asset-attribution; protects scope boundaries.

## References
- `_shared/` rules (authorization, evidence).
