---
name: detection-as-code
description: >
  Use when operationalizing detections as code — version control, CI testing,
  automated deployment, and lifecycle management of detection rules across SIEM/
  EDR. Covers the pipeline and governance that keep detections reliable at scale.
type: knowledge
domain: defensive/detection-engineering
maturity: canonical
tools: [git]
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Detection-as-Code

Manage detections like software: versioned in git, validated by CI (syntax, test
data, FP checks), deployed automatically, and lifecycle-managed — so a growing rule
set stays consistent, tested, and auditable across platforms.

## When to use
When the detection library grows beyond ad-hoc rules and needs repeatable quality/
deployment.

## Procedure (gated phases)
1. **Repository structure** — rules (Sigma/platform), tests, and metadata in git;
   a clear schema and ownership.
2. **CI validation** — on each change: syntax/schema checks, unit tests against
   known-malicious and known-benign samples, and FP-rate gates.
3. **Automated deployment** — convert/deploy to target SIEM/EDR on merge; staged
   rollout (audit → enforce).
4. **Lifecycle** — track coverage, review/retire stale rules, and measure
   effectiveness.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. "Done" = rules only ship when tests/FP gates
pass; deployments are auditable.

## Quality bar / pitfalls
- Deploying untested rules (alert storms); no rollback; drift between repo and
  live SIEM — enforce via the pipeline.

## Governance
- Ownership, review, coverage metrics (ATT&CK), and a feedback loop from incidents/
  purple-team into new detections.

## References
- `_shared/` rules (evidence).
