---
name: fuzzing
description: >
  Use when fuzzing an authorized target (software, parser, API, protocol) to
  discover crashes/vulnerabilities — harness design, coverage-guided fuzzing
  (AFL++/libFuzzer/cargo-fuzz), corpus and triage. Research/testing focus with
  responsible handling of findings.
type: knowledge
domain: offensive/exploit-dev
maturity: canonical
tools: [afl++, libfuzzer, cargo-fuzz]
references:
  - _shared/scope-authorization-rule.md
  - _shared/safe-execution-rules.md
  - _shared/untrusted-input-rule.md
  - _shared/evidence-confidence-rule.md
  - _shared/gated-workflow-rule.md
license: MIT
version: 1.0.0
---

# Fuzzing (authorized research/testing)

Build an effective fuzzing campaign against authorized software to surface
crashes/memory-safety issues: design a harness around the target's input, use
coverage-guided fuzzing with sanitizers, grow a good corpus, and triage findings
to unique, actionable bugs. Emphasis on methodology and responsible disclosure.

> Authorized testing/research only, on software you may test (your own, in-scope,
> or open-source). Handle crashing inputs responsibly (`_shared/scope-authorization-rule.md`).

## Prerequisites
- Authorization + scope; buildable target/harness. `export OUTPUT_DIR="${OUTPUT_DIR:-./output}" && mkdir -p "$OUTPUT_DIR"`.

## Procedure (gated phases)
1. **Identify the attack surface** — the parsing/processing entry points worth
   fuzzing (file formats, protocol messages, APIs).
2. **Harness + sanitizers** — write a harness exercising the target; build with
   ASan/UBSan/MSan for crash visibility; add a seed corpus + dictionary.
3. **Run coverage-guided** — AFL++/libFuzzer/cargo-fuzz; monitor coverage and
   crashes; grow corpus.
4. **Triage** — deduplicate crashes, minimize inputs, classify exploitability
   signal; document reproducible cases.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record reproducible crashing inputs with
sanitizer output; distinguish unique bugs from duplicates.

## Impact escalation
Memory-safety bugs feeding memory-corruption/exploit-development; DoS; logic bugs.
Severity depends on reachability/exploitability. CVSS per `_shared/cvss-reference.md`.

## False positives & pitfalls
- Crashes in the harness vs the target; sanitizer false positives — verify.
- Non-reproducible crashes — minimize and confirm.

## Remediation
- Fix memory-safety bugs; adopt memory-safe languages/APIs; integrate fuzzing +
  sanitizers into CI; input validation; keep dependencies patched.

## References
- `_shared/` rules (authorization, safe execution, untrusted input, evidence, gates).
