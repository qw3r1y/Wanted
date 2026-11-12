---
name: script-deobfuscation
description: >
  Use when deobfuscating malicious scripts (PowerShell, JS, VBScript, batch) —
  decoding layers, resolving encoding/string tricks, and recovering intent safely
  without executing. Defensive analysis of scripted malware stages.
type: knowledge
domain: malware-re
maturity: canonical
tools: []
references:
  - _shared/untrusted-input-rule.md
  - _shared/safe-execution-rules.md
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Script Deobfuscation

Recover the intent of an obfuscated malicious script (PowerShell/JS/VBScript/batch)
by peeling its layers — decoding base64/encoding, resolving string-construction and
compression tricks, and reconstructing the logic — **statically**, never by running
it, to extract the next stage and IOCs.

> Deobfuscate by analysis, not execution; if any evaluation is needed, do it
> isolated/sandboxed, never live (`_shared/safe-execution-rules.md`).

## When to use
On scripted stages from maldocs, phishing, or incident artifacts.

## Procedure (gated phases)
1. **Map the obfuscation** — identify techniques (encoding, concatenation,
   compression, char-code, environment-based).
2. **Decode layers** — reverse each layer statically (decode/transform) to reveal
   the next; iterate through nested layers.
3. **Reconstruct intent** — read the deobfuscated logic: what it downloads/executes/
   persists.
4. **Extract IOCs** — URLs, payloads, C2, and technique.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record the recovered logic + IOCs; keep
transformations documented.

## Impact / output
Recovered script intent + IOCs (feeds detection, hunting).

## Pitfalls
- Environment/anti-analysis-dependent decoding — reason statically; sandbox only if
  needed.
- Many layers — iterate patiently.

## Remediation / linkage
- Detections (script-block logging/AMSI), block IOCs, awareness.

## References
- `_shared/` rules (untrusted input, safe execution, evidence).
