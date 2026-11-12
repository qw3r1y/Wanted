---
name: file-upload
description: >
  Use when testing an authorized web target with a file-upload feature for unsafe
  upload handling — content-type/extension bypass, dangerous file types, path
  traversal in filenames, SVG/polyglot and image-parsing issues, and the path
  from upload to execution or XSS. Covers validation analysis, controlled proof
  and remediation. Do NOT use for pure storage without any retrieval/rendering.
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
  - references/upload-bypasses.md
license: MIT
version: 1.0.0
---

# Unsafe File Upload (authorized testing)

Find upload features whose validation can be bypassed to store a dangerous file,
and prove a real outcome — code execution, stored XSS (SVG/HTML), SSRF/XXE via
parsed formats, overwrite via path traversal, or client-side impact on download.
The value is **what the stored file does when retrieved/processed**, not merely
that an upload succeeded.

> Authorized testing only (`_shared/scope-authorization-rule.md`). Upload only
> benign proof files; never deploy real web shells or malware
> (`safe-execution-rules.md`).

## When to use
Any feature accepting files: avatars/images, documents, attachments, import,
resume/CV, profile media, SVG, archives. Especially where uploaded files are
later **served, rendered, parsed, or executed**.

## Prerequisites
- Authorization + scope recorded (`OUTPUT_DIR/scope.md`).
- `export OUTPUT_DIR="${OUTPUT_DIR:-./output}" && mkdir -p "$OUTPUT_DIR"`.
- Benign marker files only (e.g., an image carrying a harmless comment, or an SVG
  with a non-malicious OOB beacon for stored-XSS verification).

## Procedure (gated phases)

### Phase 1 — Characterize the validation
Determine how the server validates: client-side only, extension allow/deny list,
`Content-Type` header, magic-byte/content sniffing, image re-encoding, size, or a
combination. Note where files are stored and how they are served (same origin?
executable path? CDN?).

### Phase 2 — Bypass analysis (first gate)
Test each control precisely (full matrix in `references/upload-bypasses.md`):
double/alternate extensions, case/trailing tricks, `Content-Type` spoofing,
magic-byte prefixing, polyglots, archive/path-traversal filenames. The goal is to
determine *whether a dangerous disposition is reachable*, not to drop a shell.

### Phase 3 — Reach & outcome
Map the stored file to an outcome:
- **Execution:** file lands in an executable path and server interprets it →
  prove with a benign, non-destructive marker (e.g., a script that only echoes a
  unique token), never a real shell.
- **Stored XSS:** SVG/HTML served inline on the app origin → confirm execution
  (OOB), see offensive/web/xss.
- **SSRF/XXE:** parsed formats (SVG/Office) → see ssrf/xxe skills.
- **Overwrite/traversal:** filename path traversal writes outside the intended
  dir → prove with a benign file in a bounded location.

### Phase 4 — Controlled proof
Demonstrate the minimal outcome that proves severity (token echo / OOB callback /
benign overwrite). Clean up uploaded artifacts where possible and record paths.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record `verdict`, the bypassed control,
the stored path/URL, and the outcome proof. A successful upload with no dangerous
disposition → **low/refuted**.

## Impact escalation
Remote code execution, stored XSS, SSRF/XXE, file overwrite/DoS, and malware
distribution via trusted origin. State the proven outcome. CVSS per
`_shared/cvss-reference.md`.

## False positives & pitfalls
- Upload accepted but re-encoded/stripped, served from a sandboxed non-exec
  origin with safe content-type → likely **refuted** for high impact.
- "It uploaded" ≠ "it executes/renders" — always prove the disposition.
- Never upload functional web shells or live malware; benign markers only.

## Remediation
- Validate by **content** (magic bytes + re-encode images) and enforce a strict
  **allow-list** of types/extensions; generate server-side random filenames;
  strip path components.
- Store outside the web root / on a **sandboxed, non-executable** origin; serve
  with correct `Content-Type` + `Content-Disposition: attachment` +
  `X-Content-Type-Options: nosniff`.
- Never render untrusted SVG/HTML inline; parse Office/SVG with XXE-hardened
  parsers; scan and size-limit uploads.

## References
- `_shared/` rules (authorization, safe execution, untrusted input, evidence, gates).
- `references/upload-bypasses.md` — validation-control bypass matrix, polyglots, traversal (4th level).
