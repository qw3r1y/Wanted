---
name: ghidra-static-analysis
description: >
  Use when statically reverse-engineering a malware/binary sample with Ghidra —
  disassembly, decompilation, identifying key functions (crypto, network, config),
  and understanding behaviour without executing. Defensive RE for detection/IOCs.
type: knowledge
domain: malware-re
maturity: canonical
tools: [ghidra]
references:
  - _shared/untrusted-input-rule.md
  - _shared/safe-execution-rules.md
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Static Malware RE with Ghidra

Understand a sample's behaviour by reading its code — disassembly/decompilation to
locate the functions that matter (C2/network, crypto, config, persistence) — so you
can characterize capability and extract detection logic/IOCs without running it.

> Never execute the sample during static analysis; treat it and all its data as
> hostile (`_shared/safe-execution-rules.md`, `untrusted-input-rule.md`).

## When to use
Deep analysis after triage (dfir/malware-triage), or when dynamic analysis is
evaded/insufficient.

## Procedure (gated phases)
1. **Load & auto-analyze** — import into Ghidra; let analysis run; note format/arch
   (feeds pe-analysis).
2. **Locate key functions** — entry/main, imports, strings → find network, crypto,
   config-decode, and persistence routines.
3. **Understand logic** — decompile the key functions; trace config/C2 derivation
   and behaviour.
4. **Extract detection value** — durable strings/constants/structure for YARA
   (yara-signature-generation) and config/C2 (c2-config-extraction).

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record identified capabilities + evidence
(function offsets); mark inferred vs confirmed.

## Impact / output
Capability assessment, detection signatures, and config/C2 — feeds hunting/CTI.

## Pitfalls
- Obfuscation/packing blocks static analysis → unpack first (unpacking skill).
- Misreading decompiler artifacts — corroborate with dynamic where needed.

## Remediation / linkage
- Produce YARA + IOCs + behavioural detection guidance (detection-engineering).

## References
- `_shared/` rules (untrusted input, safe execution, evidence).
