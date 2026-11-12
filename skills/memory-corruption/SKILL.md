---
name: memory-corruption
description: >
  Use when analyzing an authorized memory-safety vulnerability (overflow, UAF,
  type confusion) to understand root cause, reachability, and exploitability —
  for research and remediation. Analysis/triage focus, not weaponization.
type: knowledge
domain: offensive/exploit-dev
maturity: canonical
tools: [gdb, asan]
references:
  - _shared/scope-authorization-rule.md
  - _shared/safe-execution-rules.md
  - _shared/untrusted-input-rule.md
  - _shared/evidence-confidence-rule.md
  - _shared/gated-workflow-rule.md
license: MIT
version: 1.0.0
---

# Memory-Corruption Analysis (authorized research)

Analyze a memory-safety bug (stack/heap overflow, use-after-free, type confusion,
out-of-bounds) in authorized software to determine **root cause, attacker
reachability, and exploitability tier** — the information a developer needs to fix
it and a researcher needs to assess severity. Focus on understanding, not building
weaponized exploits.

> Authorized research/testing only (`_shared/scope-authorization-rule.md`). Keep
> analysis in a controlled environment; handle PoCs responsibly.

## Prerequisites
- Authorization + scope; the crashing input/target (e.g., from fuzzing) + a debug
  build. `export OUTPUT_DIR="${OUTPUT_DIR:-./output}" && mkdir -p "$OUTPUT_DIR"`.

## Procedure (gated phases)
1. **Root cause** — reproduce under a debugger/sanitizer; identify the exact
   faulting operation and the bug class.
2. **Reachability** — trace how attacker-controlled input reaches the bug; assess
   whether it is remotely/locally triggerable and the control over corrupted data.
3. **Exploitability tier** — assess, conceptually, whether it is DoS-only or
   potentially code-execution given mitigations (ASLR/DEP/CFI/stack cookies) —
   enough to score severity, not to produce a working exploit.
4. **Document** — root cause, reach, tier, and a minimal reproducer.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record the root cause, reproducer, and
exploitability assessment with sanitizer evidence.

## Impact escalation
DoS vs potential code execution; severity per reachability and mitigations. CVSS
per `_shared/cvss-reference.md`.

## False positives & pitfalls
- Sanitizer artifacts vs real bugs; harness-only crashes — verify in the real
  target.
- Mitigations may reduce exploitability — reflect that in severity.

## Remediation
- Fix the unsafe operation; bounds/lifetime checks; memory-safe languages; enable
  all mitigations (ASLR/DEP/CFI/cookies); add regression tests + fuzzing.

## References
- `_shared/` rules (authorization, safe execution, untrusted input, evidence, gates).
