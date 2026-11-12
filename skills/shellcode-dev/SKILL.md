---
name: shellcode-dev
description: >
  Use when, for authorized research, understanding and analyzing shellcode/payload
  mechanics — position-independence, encoding, bad-char avoidance, and detection
  surfaces — primarily to inform detection/remediation. Analysis and defensive
  understanding focus.
type: knowledge
domain: offensive/exploit-dev
maturity: canonical
tools: [nasm, gdb]
references:
  - _shared/scope-authorization-rule.md
  - _shared/safe-execution-rules.md
  - _shared/untrusted-input-rule.md
  - _shared/evidence-confidence-rule.md
  - _shared/gated-workflow-rule.md
license: MIT
version: 1.0.0
---

# Shellcode / Payload Mechanics (authorized research)

For authorized research, understand how position-independent payloads are
constructed and constrained (bad characters, size, encoding) and — importantly —
what detection surfaces they create, so defenders can detect them and developers
can understand exploit requirements. Analysis/defensive framing, in a controlled
lab.

> Authorized research only, in a controlled lab (`_shared/scope-authorization-rule.md`).
> The aim is understanding and detection, not producing operational malware.

## Prerequisites
- Authorization + scope; a lab environment. `export OUTPUT_DIR="${OUTPUT_DIR:-./output}" && mkdir -p "$OUTPUT_DIR"`.

## Procedure (gated phases)
1. **Constraints** — for a given exploit, enumerate constraints (bad chars, size,
   architecture, position-independence) that a payload must satisfy.
2. **Mechanics** — study how payloads achieve position-independence and encoding to
   meet constraints (conceptually), in a lab.
3. **Detection surface (core)** — identify the static/behavioural signatures such
   payloads create (syscall patterns, encoder stubs, memory artifacts) that EDR/AV
   can detect.
4. **Feed detection** — translate mechanics into detection/remediation guidance
   (feeds defensive/detection-engineering).

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Deliverable: constraint/detection analysis,
lab-contained.

## Impact escalation
Understanding payload constraints informs exploit severity; detection surfaces
inform defense.

## False positives & pitfalls
- Keep all work lab-contained; the deliverable is understanding/detection, not
  deployable payloads.

## Remediation
- Exploit mitigations (DEP/CFI/ASLR), EDR behavioural detection, memory-safety,
  and attack-surface reduction.

## References
- `_shared/` rules (authorization, safe execution, untrusted input, evidence, gates).
