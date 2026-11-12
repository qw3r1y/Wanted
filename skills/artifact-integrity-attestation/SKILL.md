---
name: artifact-integrity-attestation
description: >
  Use when ensuring build-artifact integrity in CI/CD — generating and verifying
  attestations/signatures so only trusted, unmodified artifacts are deployed. Covers
  the pipeline side of artifact integrity.
type: knowledge
domain: ci-cd-devsecops
maturity: canonical
tools: [cosign]
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Artifact Integrity & Attestation (CI/CD)

Ensure that what gets deployed is exactly what the trusted pipeline built: sign
artifacts and generate provenance attestations in the pipeline, and **verify** them
at deploy/admission — so a tampered or out-of-band artifact is rejected. The pipeline
side of supply-chain integrity.

## When to use
When hardening the build→deploy integrity chain.

## Procedure (gated phases)
1. **Sign in-pipeline** — sign artifacts/images and emit provenance (what/how built)
   (supply-chain/artifact-signing + slsa-provenance).
2. **Attest** — record build provenance attestations tied to the artifact.
3. **Verify at deploy (core)** — admission/deploy verifies signature + provenance +
   policy (from the trusted pipeline); reject otherwise.
4. **Protect signing identity** — keyless/ephemeral or well-guarded keys; scope trust.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. "Done" = deploy fails for unsigned/untrusted/
tampered artifacts; verified end-to-end.

## Quality bar / pitfalls
- Signing without enforcing verification (no protection).
- Verifying signature but not provenance/policy (any signed artifact passes).

## Linkage
- Implements supply-chain/artifact-signing + slsa-provenance at the pipeline;
  pairs with container-k8s admission.

## References
- `_shared/` rules (evidence).
