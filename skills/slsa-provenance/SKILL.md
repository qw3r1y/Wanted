---
name: slsa-provenance
description: >
  Use when establishing build provenance and SLSA levels — generating tamper-
  evident provenance attestations about how artifacts were built and raising the
  build's integrity level. Covers provenance generation and SLSA maturity.
type: knowledge
domain: appsec/supply-chain
maturity: canonical
tools: []
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Build Provenance (SLSA)

Produce tamper-evident evidence of **how** an artifact was built — source, builder,
inputs — as signed provenance, and raise the build's SLSA level by hardening the
pipeline (isolated, reproducible, non-falsifiable provenance). This lets consumers
trust the artifact's origin.

## When to use
When maturing supply-chain integrity and meeting provenance requirements.

## Procedure (gated phases)
1. **Generate provenance** — the build emits signed provenance (source commit,
   builder identity, build parameters, inputs).
2. **Assess current SLSA level** — scripted vs hosted-isolated builder, provenance
   existence/authenticity, and tamper resistance.
3. **Harden to raise level** — isolated/ephemeral builders, non-falsifiable
   provenance, and verified inputs.
4. **Consume** — verify provenance at deploy (with artifact-signing) to enforce
   origin/policy.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. "Done" = signed provenance generated and
verifiable; SLSA level documented.

## Quality bar / pitfalls
- Provenance that the build itself could forge (low assurance) — isolate the
  builder.
- Generating but not verifying provenance.

## Linkage
- Pairs with artifact-signing, ci-cd-pipeline-security, sbom-generation.

## References
- `_shared/` rules (evidence).
