---
name: dockerfile-hardening
description: >
  Use when hardening Dockerfiles/container builds — minimal base, non-root user,
  no secrets in layers, least privilege, and reduced attack surface. Covers secure
  image construction.
type: knowledge
domain: cloud-infra/container-k8s
maturity: canonical
tools: [hadolint]
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Dockerfile / Image Hardening

Build images that are small, least-privileged, and free of secrets — minimal base,
non-root user, no secrets baked into layers, pinned dependencies, and a reduced
surface — so a compromised container has little to work with.

## When to use
When authoring/reviewing Dockerfiles and build pipelines.

## Procedure (gated phases)
1. **Minimal base** — distroless/minimal, pinned by digest; only needed packages.
2. **Non-root & least privilege** — run as non-root; drop capabilities; read-only
   filesystem where possible.
3. **No secrets in layers** — use build secrets/mounts, not COPY/ENV secrets (they
   persist in history); multi-stage builds to drop build tooling.
4. **Surface reduction** — remove package managers/shells where feasible; pin deps.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. "Correct" = minimal, non-root, no layer
secrets; verify with a linter + image inspection.

## Quality bar / pitfalls
- Running as root; secrets in ENV/layers; `latest` unpinned bases.
- Bloated images (large surface).

## Deployment
- Lint in CI (hadolint); enforce non-root via pod-security; scan (image-vulnerability-scan).

## References
- `_shared/` rules (evidence).
