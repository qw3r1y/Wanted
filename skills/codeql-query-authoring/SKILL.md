---
name: codeql-query-authoring
description: >
  Use when writing CodeQL queries for deep semantic/dataflow vulnerability
  detection and variant analysis — modeling sources/sinks, taint tracking, and
  finding all instances of a bug class. Covers query design and variant hunting.
type: knowledge
domain: appsec/sast-dast
maturity: canonical
tools: [codeql]
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# CodeQL Query Authoring

Use CodeQL's semantic model to find vulnerabilities and, crucially, **variant
analysis** — after one bug is found, write a query that finds every instance of
that pattern across the codebase. Model sources/sinks and taint flow for precise,
deep detection.

## When to use
For deep dataflow analysis, variant hunting after a finding, or codifying a
security property.

## Procedure (gated phases)
1. **Model the bug class** — define sources (untrusted input), sinks (dangerous
   operations), and sanitizers in the CodeQL dataflow framework.
2. **Write the query** — taint-tracking configuration from sources to sinks for the
   language.
3. **Variant analysis** — run across the codebase to find all instances; refine to
   reduce FPs.
4. **Validate** — confirm true positives; tune sanitizer modeling for precision.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. "Done" = finds the known instance + variants
with acceptable precision. Record results.

## Quality bar / pitfalls
- Incomplete sanitizer modeling → FPs; missing sources/sinks → FNs.
- Expensive queries — scope sensibly.

## Deployment
- CI/code-scanning integration; reuse for variant analysis on new findings.

## References
- `_shared/` rules (evidence).
