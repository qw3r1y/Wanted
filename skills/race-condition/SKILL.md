---
name: race-condition
description: >
  Use when testing an authorized target for race conditions / TOCTOU — concurrent
  requests that break an invariant (limit-overrun, double-spend, coupon/vote
  reuse, state confusion). Covers candidate discovery, concurrency proof and
  remediation.
type: knowledge
domain: offensive/web
maturity: canonical
tools: [curl, concurrency-tool]
references:
  - _shared/scope-authorization-rule.md
  - _shared/safe-execution-rules.md
  - _shared/untrusted-input-rule.md
  - _shared/evidence-confidence-rule.md
  - _shared/gated-workflow-rule.md
license: MIT
version: 1.0.0
---

# Race Conditions / TOCTOU (authorized testing)

Find operations whose correctness depends on a check-then-act that is not atomic,
and prove that **concurrent** requests violate the intended limit or state. The
proof is a reproducible invariant break under parallelism (e.g., a one-time action
performed twice).

> Authorized testing only. Use test accounts and **bounded** concurrency; avoid
> financial or destructive effects beyond the minimal proof
> (`safe-execution-rules.md`).

## When to use
Limited actions: coupon/gift-card/credit redemption, "one per account" claims,
balance/withdrawal, vote/like, invite/referral, rate-limited actions, and
multi-step flows with a check-then-update.

## Prerequisites
- Authorization + scope; test accounts; a tool to fire tightly-synchronized
  concurrent requests. `export OUTPUT_DIR="${OUTPUT_DIR:-./output}" && mkdir -p "$OUTPUT_DIR"`.

## Procedure (gated phases)
1. **Identify an invariant** — a limit/uniqueness the server should enforce (once,
   N max, balance ≥ 0).
2. **Baseline sequentially** — confirm the action is normally limited when done one
   at a time.
3. **Concurrency probe (first gate)** — send many copies of the critical request
   **simultaneously** (single-packet/parallel) on a test account; observe whether
   the invariant breaks (action applied more than allowed).
4. **Confirm & bound** — reproduce the break, quantify it (how many succeeded),
   and keep the effect minimal/reversible on test data.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record `verdict`, the invariant, sequential
baseline vs concurrent result, and reproduction. A single success under
concurrency could be chance → reproduce.

## Impact escalation
Financial loss (double-spend, limit bypass), quota/limit bypass, state corruption,
and auth/MFA step bypass. CVSS per `_shared/cvss-reference.md`.

## False positives & pitfalls
- Server serializes/locks correctly → **refuted**.
- Apparent double-effect that is actually idempotent/rolled back → not a race.
- Keep financial effects to the minimum reversible proof on test accounts.

## Remediation
- Make check-then-act **atomic**: DB transactions with appropriate isolation,
  unique constraints, atomic counters/`SELECT ... FOR UPDATE`, idempotency keys.
- Server-side locks/queues for limited actions; never rely on client timing or
  read-then-write without concurrency control.

## References
- `_shared/` rules (authorization, safe execution, untrusted input, evidence, gates).
