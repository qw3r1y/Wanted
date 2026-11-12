---
name: unpacking
description: >
  Use when a malware sample is packed/obfuscated and must be unpacked before
  analysis — identifying the packer and recovering the original code via static or
  controlled dynamic unpacking. Defensive RE preparation step.
type: knowledge
domain: malware-re
maturity: canonical
tools: [x64dbg, unicorn]
references:
  - _shared/untrusted-input-rule.md
  - _shared/safe-execution-rules.md
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Malware Unpacking

Recover a sample's real code from a packer/obfuscator so the rest of analysis can
proceed — identify the packing, then unpack statically or via controlled,
isolated dynamic execution to a dumped, reconstructed payload.

> Any dynamic unpacking happens only in an isolated sandbox/VM; the sample is
> hostile (`_shared/safe-execution-rules.md`).

## When to use
When static analysis shows high entropy / few strings / packer signatures, before
deeper RE.

## Procedure (gated phases)
1. **Identify packing** — entropy, section anomalies, known packer signatures, few
   imports/strings.
2. **Choose approach** — known packer → known static unpacker; unknown → controlled
   dynamic unpack (run to OEP in an isolated debugger/emulator) and dump.
3. **Reconstruct** — fix the dumped image (imports/IAT) into an analyzable file.
4. **Validate** — confirm the unpacked payload reveals real code/strings for
   analysis.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. "Done" = an analyzable unpacked payload;
record packer + method.

## Impact / output
An unpacked sample enabling static/dynamic analysis and signature generation.

## Pitfalls
- Anti-analysis/anti-debug tricks — note and handle; keep isolated.
- Multiple packing layers — iterate.

## Remediation / linkage
- Feed unpacked payload to ghidra-static-analysis, yara-signature-generation.

## References
- `_shared/` rules (untrusted input, safe execution, evidence).
