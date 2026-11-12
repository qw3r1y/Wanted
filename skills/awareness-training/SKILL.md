---
name: awareness-training
description: >
  Use when building security-awareness content/program from engagement findings —
  translating real phishing/social-engineering results into targeted, effective
  training and measuring behaviour change. Program-design and enablement focus.
type: knowledge
domain: offensive/social-engineering
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

# Security Awareness Program (enablement)

Turn simulation/engagement findings into targeted, effective awareness training and
a measurable behaviour-change program — addressing the specific lures and segments
that struggled, and tracking improvement over time. The deliverable is a training
program and metrics, not a one-off slideshow.

> Use real engagement data responsibly and in aggregate
> (`_shared/scope-authorization-rule.md`).

## Prerequisites
- Findings from phishing-campaign / phishing-initial-access; stakeholder buy-in.
  `export OUTPUT_DIR="${OUTPUT_DIR:-./output}" && mkdir -p "$OUTPUT_DIR"`.

## Procedure (gated phases)
1. **Analyze findings** — which lures/segments failed; the behaviours to change.
2. **Targeted content** — build role/segment-specific, concise, actionable training
   tied to real examples; focus on "what to do" (report) over fear.
3. **Reinforcement** — just-in-time training on interaction, repeated short
   touchpoints, and a strong report-phish workflow.
4. **Measure** — track report rate, click rate, and time-to-report over successive
   simulations; iterate.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Deliverable: the program + a metrics plan;
success = measurable behaviour change.

## Impact escalation
Reduces human attack-surface risk; improves detection via faster user reporting.

## False positives & pitfalls
- One-off training doesn't change behaviour — make it continuous and measured.
- Keep it non-punitive and privacy-respecting.

## Remediation / program hygiene
- Continuous, role-based training; positive reporting culture; metrics-driven
  iteration; integrate with technical controls (email defense, MFA).

## References
- `_shared/` rules (authorization, safe execution, untrusted input, evidence, gates).
