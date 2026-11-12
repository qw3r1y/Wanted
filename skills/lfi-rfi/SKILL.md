---
name: lfi-rfi
description: >
  Use when testing an authorized web target for Local/Remote File Inclusion —
  input that controls a file path or include/require target, enabling local file
  read, log/wrapper-based code execution, or remote inclusion. Covers detection,
  wrapper/filter analysis, controlled proof and remediation. Related to
  path-traversal (file read) but focused on inclusion/execution sinks.
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

# LFI / RFI — File Inclusion (authorized testing)

Find input that reaches a file-include/read sink (template loader, `include`/
`require`, language-file selector, path parameter) and prove it reads or executes
an unintended file. LFI escalates (log poisoning, wrappers, session files) toward
code execution; RFI pulls a remote file where the config allows it.

> Authorized testing only. Read the **minimum** to prove the class; benign
> markers only, no real web shells (`_shared/safe-execution-rules.md`).

## When to use
Parameters like `?page=`, `?file=`, `?lang=`, `?template=`, `?include=`, theme/
skin selectors, and any path that feeds an include/read. Often paired with path
traversal.

## Prerequisites
- Authorization + scope recorded; `export OUTPUT_DIR="${OUTPUT_DIR:-./output}" && mkdir -p "$OUTPUT_DIR"`.

## Procedure (gated phases)
1. **Identify the sink** — does the parameter select a file to include/read?
   Observe behaviour with a known-valid value first.
2. **Traversal/read probe (first gate)** — attempt to read a benign known file
   outside the intended directory; confirm its content appears. Reflection of a
   non-sensitive system file = read confirmation.
3. **Wrapper/filter analysis** — test language wrappers/filters and encoding where
   relevant; identify whether inclusion evaluates content (execution path) vs pure
   read.
4. **Controlled escalation** — only with scope approval, demonstrate execution via
   a benign marker (log/session/wrapper) — a unique token echo, never a shell.
   RFI: confirm remote fetch via OOB to your host.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record `verdict`, LFI vs RFI, read vs
execution, and the proof path. Error mentioning a path ≠ inclusion.

## Impact escalation
Local file disclosure (configs/secrets/source), code execution via
log/wrapper/session poisoning, SSRF/RFI remote inclusion, and info leakage. CVSS
per `_shared/cvss-reference.md`.

## False positives & pitfalls
- Allow-list of page names / no traversal → **refuted**.
- Read of your own intended file in a different form → not inclusion.
- Never deploy functional shells; benign token markers only.

## Remediation
- Never build include/read paths from user input; use a **fixed allow-list** of
  identifiers mapped to server-side paths.
- Disable remote inclusion (`allow_url_include` off); restrict wrappers; confine
  reads with a safe base dir + canonicalization; least-privilege FS.

## References
- `_shared/` rules (authorization, safe execution, untrusted input, evidence, gates).
