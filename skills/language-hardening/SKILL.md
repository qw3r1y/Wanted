---
name: language-hardening
description: >
  Use when applying language-specific secure-coding guidance — the common pitfalls
  and safe patterns per language (Python, JS/TS, Java, Go, Rust, C#, PHP, C/C++) —
  to prevent language-idiomatic vulnerabilities. Covers per-language hardening.
type: knowledge
domain: appsec/secure-coding
maturity: canonical
tools: []
references:
  - _shared/evidence-confidence-rule.md
  - references/per-language.md
license: MIT
version: 1.0.0
---

# Language-Specific Hardening

Each language has idiomatic footguns. Apply the per-language safe patterns and avoid
the common pitfalls — deserialization in Java/Python, prototype pollution in JS,
memory safety in C/C++, unsafe reflection, SSRF-prone HTTP clients — so code is
secure in that language's idioms.

## When to use
Writing/reviewing code in a specific language; onboarding a stack's secure-coding
standard.

## Procedure (gated phases)
1. **Identify the language/runtime** and its risk profile.
2. **Apply the pitfalls checklist** — language-specific dangerous APIs and the safe
   alternatives (`references/per-language.md`).
3. **Use safe defaults** — memory-safe constructs, safe (de)serialization, parameter-
   ized APIs, and vetted libraries.
4. **Enforce** — language-aware linters/SAST (semgrep) encoding these rules.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. "Correct" = code avoids the language's known
pitfalls; verified by review + language-aware SAST.

## Quality bar / pitfalls
- Applying generic advice that misses language idioms (e.g., prototype pollution).
- Unsafe deserialization / dynamic eval in any language.

## Linkage
- Pairs with sast-dast (semgrep/codeql), input-validation, framework-hardening.

## References
- `_shared/` rules; `references/per-language.md` — per-language pitfalls (4th level).
