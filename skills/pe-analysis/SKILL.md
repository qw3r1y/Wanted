---
name: pe-analysis
description: >
  Use when analyzing an executable's file structure (PE, and by extension ELF/
  Mach-O) — headers, imports/exports, sections, resources, signatures, and anomaly
  indicators — as a fast structural assessment that guides deeper RE. Defensive
  file analysis.
type: knowledge
domain: malware-re
maturity: canonical
tools: [pefile]
references:
  - _shared/untrusted-input-rule.md
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Executable Structure Analysis (PE/ELF/Mach-O)

Read an executable's structure for fast signal before deep RE — imports hinting at
capability (network/crypto/injection APIs), section/entropy anomalies (packing),
resources (embedded payloads), compile timestamps, and signing status — to guide
and prioritize analysis.

> The file is hostile data; parse it, don't run it here (`_shared/untrusted-input-rule.md`).

## When to use
As a quick structural triage/guide before or alongside static/dynamic analysis.

## Procedure (gated phases)
1. **Headers & metadata** — format/arch, compile timestamp, subsystem, signing.
2. **Imports/exports** — capability hints (e.g., network, crypto, process-injection
   APIs); suspicious or minimal imports (packing).
3. **Sections & entropy** — anomalies indicating packing/embedded data.
4. **Resources & overlays** — embedded payloads/config; overlay data.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record structural findings; these are hints,
confirmed by RE/dynamic.

## Impact / output
A capability/priority guide for RE + structural YARA features.

## Pitfalls
- Timestamps/metadata can be forged — treat as hints.
- Import hints ≠ confirmed behaviour — corroborate.

## Remediation / linkage
- Feeds ghidra-static-analysis, unpacking, yara-signature-generation.

## References
- `_shared/` rules (untrusted input, evidence).
