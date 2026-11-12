---
name: runner-hardening
description: >
  Use when hardening CI/CD build runners/agents — isolation, ephemerality, least
  privilege, and protecting them from untrusted workloads (fork PRs, third-party
  actions). Covers runner security.
type: knowledge
domain: ci-cd-devsecops
maturity: canonical
tools: []
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# CI/CD Runner Hardening

Build runners execute code — including potentially untrusted code (fork PRs,
third-party actions) — with access to secrets and deploy credentials. Harden them:
ephemeral + isolated runners, least privilege, and strict handling of untrusted
workloads, so a malicious build can't steal secrets or persist.

## When to use
When securing self-hosted or managed CI runners/agents.

## Procedure (gated phases)
1. **Ephemeral + isolated** — fresh, isolated runner per job (no shared mutable
   state/persistence between jobs); clean teardown.
2. **Least privilege** — minimal runner identity/permissions; no broad standing
   credentials on the runner.
3. **Untrusted workloads (core)** — restrict what fork-PR/third-party code can access
   (no secrets, limited permissions); require approval for privileged workflows.
4. **Pin & verify** — pin third-party actions/images by digest; monitor runner
   activity.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. "Done" = ephemeral, isolated, least-privilege
runners that don't expose secrets to untrusted code.

## Quality bar / pitfalls
- Persistent shared self-hosted runners (poisoning/persistence risk).
- Fork PRs / untrusted actions reaching secrets or privileged runners.

## Linkage
- Core to pipeline-threat-model + supply-chain/ci-cd-pipeline-security.

## References
- `_shared/` rules (evidence).
