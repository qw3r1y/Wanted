---
name: artifact-signing
description: >
  Use when implementing artifact signing and verification — signing builds/images/
  packages (e.g., Sigstore/cosign) and enforcing verification at deploy — to ensure
  integrity and provenance. Covers signing setup and enforcement.
type: knowledge
domain: appsec/supply-chain
maturity: canonical
tools: [cosign, sigstore]
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Artifact Signing & Verification

Ensure that what you deploy is what you built: sign build artifacts/images/packages
and **enforce signature verification** at admission/deploy, so tampered or
unauthorized artifacts are rejected — a core defense against supply-chain tampering.

## When to use
In the build/release pipeline and at deployment admission (container/package).

## Procedure (gated phases)
1. **Sign in the pipeline** — sign artifacts/images at build (keyless/Sigstore or
   managed keys); attach attestations.
2. **Store provenance** — signatures + attestations (what/how it was built) with the
   artifact (ties to slsa-provenance).
3. **Enforce verification (core)** — at deploy/admission, verify signatures + policy
   (e.g., only from the trusted pipeline); **reject** unsigned/untrusted.
4. **Key/trust management** — protect signing identity; rotate; scope trust.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. "Done" = deploy fails for unsigned/untrusted
artifacts; signing + verification demonstrated.

## Quality bar / pitfalls
- Signing without **enforcing** verification (no protection).
- Weakly-protected signing keys/identity — guard them.

## Linkage
- Pairs with slsa-provenance, ci-cd-pipeline-security, container-k8s admission.

## References
- `_shared/` rules (evidence).
