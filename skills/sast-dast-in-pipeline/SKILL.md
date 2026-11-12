---
name: sast-dast-in-pipeline
description: >
  Use when integrating security scanning into CI/CD — SAST, SCA, secret, IaC, and
  DAST scans as pipeline gates with sensible fail criteria and developer-friendly
  feedback. Covers shift-left scanning integration.
type: knowledge
domain: ci-cd-devsecops
maturity: canonical
tools: [semgrep, trivy]
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Security Scanning in CI/CD

Integrate security scanning (SAST, SCA, secrets, IaC, DAST) into the pipeline so
issues are caught at commit/PR — but do it so it helps rather than blocks developers:
gate on real high-confidence issues, give fast actionable feedback, and avoid noise
that trains people to ignore it.

## When to use
When shifting security scanning left into the development workflow.

## Procedure (gated phases)
1. **Select scans by stage** — SAST/secrets/SCA on PR (fast); IaC on infra changes;
   DAST in pre-prod; SBOM at build.
2. **Gate criteria (core)** — fail on high-confidence, high-severity, reachable
   issues (and any secret); warn on the rest — avoid blocking on noise.
3. **Developer feedback** — results in the PR with fix guidance; fast runs; dedupe
   (sarif-triage).
4. **Tune continuously** — reduce FPs; track findings to resolution.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. "Done" = scans run per stage, gate on real
issues, and developers get actionable feedback.

## Quality bar / pitfalls
- Blocking builds on noisy/low-confidence findings → developers bypass security.
- Slow scans that stall the pipeline — optimize/parallelize.

## Linkage
- Operationalizes sast-dast/* + secret-scanning + iac + sbom as pipeline gates.

## References
- `_shared/` rules (evidence).
