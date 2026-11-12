---
name: poc-crafting
description: >
  Use when crafting a safe, convincing proof-of-concept for a finding — demonstrating
  impact clearly without causing harm or crossing ethical lines. Covers PoC design
  for reports.
type: knowledge
domain: bug-bounty
maturity: canonical
tools: []
references:
  - _shared/scope-authorization-rule.md
  - _shared/safe-execution-rules.md
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# PoC Crafting (safe & convincing)

A good PoC proves impact unmistakably while staying safe and ethical — enough to
leave no doubt the bug is real and serious, but without accessing real users' data,
causing damage, or exceeding what's needed. The PoC is what turns "I think" into
"here's proof".

> Demonstrate the minimum needed; use test accounts/benign markers; never harm real
> users or exfiltrate real data (`_shared/safe-execution-rules.md`).

## When to use
When preparing evidence for any finding, especially higher-severity ones.

## Procedure (gated phases)
1. **Define what proves it** — the minimal demonstration that establishes the class +
   impact (e.g., a benign OOB callback, a test-account cross-access, a controlled
   marker).
2. **Craft safely (core)** — use test accounts, benign payloads/markers, and bounded
   actions; never access real PII, move funds, or disrupt service.
3. **Capture evidence** — record the PoC working (screenshot/HAR/OOB log) clearly.
4. **Keep it minimal** — enough to convince, not to maximize damage; respect the
   program's rules.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. The PoC unambiguously demonstrates the impact,
safely and reproducibly.

## Impact / output
Convincing, ethical proof that accelerates validation.

## Pitfalls
- Over-aggressive PoCs (real data/damage) — unethical, against rules, and risky.
- Weak PoCs that don't actually prove impact.

## Linkage
- Uses the offensive skills' impact-demonstration discipline; feeds report-writing.

## References
- `_shared/` rules (authorization, safe execution, evidence).
