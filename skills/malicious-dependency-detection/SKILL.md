---
name: malicious-dependency-detection
description: >
  Use when detecting malicious packages — typosquats, dependency confusion,
  compromised updates, and install-time malicious behaviour — to stop supply-chain
  attacks via the dependency channel. Covers detection signals and prevention.
type: knowledge
domain: appsec/supply-chain
maturity: canonical
tools: []
references:
  - _shared/untrusted-input-rule.md
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Malicious Dependency Detection

Catch packages that are malicious by design or compromised in an update —
typosquatting, dependency confusion (internal name resolved from public registry),
and malicious install/postinstall behaviour — before they execute in your build or
runtime.

## When to use
When adding/updating dependencies and as a pipeline control.

## Procedure (gated phases)
1. **Name/confusion checks** — detect typosquats of popular packages and
   dependency-confusion risk (internal names claimable publicly).
2. **Behaviour signals** — install/postinstall scripts, obfuscated code, network/
   filesystem access at install, and sudden maintainer/behaviour changes in updates.
3. **Pin & verify** — pin versions + integrity hashes; scope registries; prefer
   signed/provenance-backed packages.
4. **Triage suspicious packages** — analyze (treat as untrusted) before allowing.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record suspicious indicators + decision;
confirmed-malicious → block + report.

## Quality bar / pitfalls
- Legitimate build scripts vs malicious ones — assess behaviour/context.
- Dependency confusion via unscoped internal names — prevent by config.

## Linkage
- Pairs with dependency-audit, ci-cd-pipeline-security; registry/namespace controls.

## References
- `_shared/` rules (untrusted input, evidence).
