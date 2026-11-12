---
name: dast-scanning
description: >
  Use when running dynamic application security testing against an authorized
  running app — configuring the scanner, authenticated scanning, and triaging
  results to real findings. Covers DAST setup and FP-aware triage.
type: knowledge
domain: appsec/sast-dast
maturity: canonical
tools: [zap, nuclei]
references:
  - _shared/scope-authorization-rule.md
  - _shared/safe-execution-rules.md
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# DAST Scanning

Run dynamic scanning against a running (authorized) application to find issues
visible at runtime, with proper **authenticated** coverage and disciplined triage —
because DAST findings are noisy and must be validated before reporting.

> Authorized testing only; scan non-production or with approval, as scanners can be
> intrusive (`_shared/safe-execution-rules.md`).

## When to use
In pre-prod pipelines or authorized assessments, complementing SAST (runtime vs
code view).

## Procedure (gated phases)
1. **Configure & authenticate** — point the scanner at the app; set up
   authenticated scanning (most of the app is behind auth) and scope/exclusions.
2. **Scan safely** — bounded, non-destructive policies; avoid DoS/destructive active
   checks on shared environments.
3. **Triage (core)** — validate each finding manually; DAST has high FP rates —
   confirm before reporting (ties to the specific web/* skill).
4. **Report confirmed issues** with evidence.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Only validated findings → `confirmed`; raw
scanner output is a lead.

## Quality bar / pitfalls
- Unauthenticated scans miss most of the app — authenticate.
- Reporting raw scanner output (FPs) — always validate.

## Deployment
- Integrate into pre-prod CI; combine with SAST; feed confirmed findings to
  remediation.

## References
- `_shared/` rules (authorization, safe execution, evidence).
