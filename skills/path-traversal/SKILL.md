---
name: path-traversal
description: >
  Use when testing an authorized web target for path/directory traversal — input
  that controls a filesystem path for read/write/download, allowing access
  outside the intended directory. Covers detection, encoding/normalization
  bypass, controlled proof and remediation. For include/execution sinks see
  offensive/web/lfi-rfi.
type: knowledge
domain: offensive/web
maturity: canonical
tools: [curl]
references:
  - _shared/scope-authorization-rule.md
  - _shared/safe-execution-rules.md
  - _shared/untrusted-input-rule.md
  - _shared/evidence-confidence-rule.md
  - _shared/gated-workflow-rule.md
license: MIT
version: 1.0.0
---

# Path Traversal (authorized testing)

Find input that maps to a filesystem path and prove you can reach a file outside
the intended directory — read a benign out-of-scope file, or (with approval)
write/overwrite in a bounded location. Proof is content of an unintended file,
not a mere error.

> Authorized testing only. Read the minimum; benign targets only
> (`_shared/safe-execution-rules.md`).

## When to use
Download/export endpoints, file viewers, `?file=`/`?path=`/`?name=` params,
avatar/attachment fetchers, static-file handlers, and archive-extraction features
(zip-slip).

## Prerequisites
- Authorization + scope recorded; `export OUTPUT_DIR="${OUTPUT_DIR:-./output}" && mkdir -p "$OUTPUT_DIR"`.

## Procedure (gated phases)
1. **Identify the path sink** — confirm the parameter selects a file; baseline a
   valid request.
2. **Traversal probe (first gate)** — attempt to reach a benign known file above
   the base dir; confirm its content returns.
3. **Normalization/encoding analysis** — test encoding layers, mixed separators,
   and absolute-path acceptance where the filter is naive; identify what the
   canonicalizer misses.
4. **Write/zip-slip (approval)** — where the feature writes/extracts, test bounded
   traversal in archive entry names; prove with a benign file in a safe location.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record `verdict`, read vs write, the
reached path and its content proof. 403/empty for out-of-dir targets → **refuted**.

## Impact escalation
Source/config/secret disclosure, arbitrary file read, file overwrite (via
write/extract), and chaining to code execution. CVSS per `_shared/cvss-reference.md`.

## False positives & pitfalls
- Canonicalization + base-dir confinement defeats traversal → **refuted**.
- Reflected path in an error ≠ file read.
- Keep reads benign and bounded; no sensitive bulk reads.

## Remediation
- **Canonicalize and confine**: resolve the final real path and verify it stays
  within an allowed base directory; reject traversal sequences after decoding.
- Prefer indirect identifiers mapped server-side over raw paths; validate archive
  entry names (prevent zip-slip); least-privilege filesystem access.

## References
- `_shared/` rules (authorization, safe execution, untrusted input, evidence, gates).
