---
name: sbom-generation
description: >
  Use when generating and using a Software Bill of Materials — producing accurate
  SBOMs (CycloneDX/SPDX), keeping them current, and using them for vulnerability and
  supply-chain response. Covers SBOM creation and operational use.
type: knowledge
domain: appsec/sast-dast
maturity: canonical
tools: [syft, cyclonedx]
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# SBOM Generation & Use

Produce an accurate, machine-readable inventory of everything in a build
(dependencies, versions, licenses) and operationalize it — so when the next
widely-used component has a critical vuln, you can answer "are we affected?" in
minutes, not days.

## When to use
In the build pipeline (per release) and to enable fast supply-chain response.

## Procedure (gated phases)
1. **Generate** — produce an SBOM (CycloneDX/SPDX) from the build, capturing direct
   + transitive components with versions.
2. **Verify completeness** — ensure it reflects what actually ships (not just
   manifests); include OS/base-image components for containers.
3. **Store & version** — attach the SBOM to the artifact; keep it queryable.
4. **Operationalize** — query SBOMs against new vulnerabilities for instant impact
   analysis (feeds vulnerability-management, supply-chain).

## Verification & evidence
`_shared/evidence-confidence-rule.md`. "Done" = SBOM accurately reflects shipped
components and is queryable.

## Quality bar / pitfalls
- Incomplete SBOMs (missing transitive/OS components) → false "not affected".
- Stale SBOMs — regenerate per build.

## Deployment
- Automate in CI; sign/attest the SBOM (slsa-provenance); query on new CVEs.

## References
- `_shared/` rules (evidence).
