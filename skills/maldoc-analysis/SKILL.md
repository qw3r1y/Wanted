---
name: maldoc-analysis
description: >
  Use when analyzing a malicious document (Office/PDF/OneNote/LNK) — extracting and
  analyzing embedded macros, scripts, and payloads safely to understand the
  infection chain and extract IOCs. Defensive document malware analysis.
type: knowledge
domain: malware-re
maturity: canonical
tools: [oletools, pdfid]
references:
  - _shared/untrusted-input-rule.md
  - _shared/safe-execution-rules.md
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Malicious Document Analysis

Analyze a weaponized document to understand its infection chain — extract and read
embedded macros/scripts/objects (Office VBA, PDF JS, OneNote/LNK droppers), follow
the staging to the next payload, and extract IOCs — without executing the document.

> Analyze statically / in isolation; never open the document in a normal
> application (`_shared/safe-execution-rules.md`, `untrusted-input-rule.md`).

## When to use
On a suspicious document from phishing/IR, to map the chain and extract IOCs.

## Procedure (gated phases)
1. **Identify structure** — document type and embedded active content (macros,
   scripts, objects, embedded files, external links/templates).
2. **Extract active content** — pull VBA/JS/scripts and embedded objects with
   analysis tooling (not the host app).
3. **Analyze the chain** — read/deobfuscate the script (script-deobfuscation) to
   understand staging → next payload (URL/dropper).
4. **Extract IOCs** — URLs, dropped files/hashes, C2, and technique for detection/
   hunting.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record the chain + IOCs + evidence.

## Impact / output
Mapped infection chain + IOCs (feeds hunting, detection, phishing-detection).

## Pitfalls
- Opening in the real app detonates it — use analysis tools only.
- Heavy obfuscation — pair with deobfuscation.

## Remediation / linkage
- Block IOCs; detections for the technique; user awareness.

## References
- `_shared/` rules (untrusted input, safe execution, evidence).
