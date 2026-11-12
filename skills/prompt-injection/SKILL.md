---
name: prompt-injection
description: >
  Use when testing or defending an authorized LLM application against prompt
  injection — direct (user) and indirect (via retrieved/tool content) attempts to
  override instructions, exfiltrate data, or misuse tools. Covers testing
  methodology and defenses (OWASP LLM01).
type: knowledge
domain: ai-security/llm-security
maturity: canonical
tools: []
references:
  - _shared/scope-authorization-rule.md
  - _shared/untrusted-input-rule.md
  - _shared/evidence-confidence-rule.md
  - _shared/gated-workflow-rule.md
license: MIT
version: 1.0.0
---

# Prompt Injection (test & defend)

The core LLM vulnerability (OWASP LLM01): untrusted content — from the user
(**direct**) or from retrieved documents/tool outputs/web pages (**indirect**) —
overrides the app's intended instructions, leaks data, or triggers tool misuse.
Test for it and design defenses; the trust boundary is "any content the model reads
is untrusted".

> Authorized testing only, on an in-scope app (`_shared/scope-authorization-rule.md`).
> Treat all model-visible content as untrusted (`untrusted-input-rule.md`).

## When to use
Testing any LLM feature that mixes instructions with untrusted content, or that has
tools/data access; and when designing its defenses.

## Procedure (gated phases)
1. **Map the trust surface** — where untrusted content reaches the model (user
   input, RAG sources, tool outputs, web/files) and what the model can do (tools,
   data, actions).
2. **Direct injection tests** — attempts to override the system prompt, extract it,
   or change behaviour via crafted user input.
3. **Indirect injection tests (core)** — plant instructions in content the app will
   retrieve/ingest (a document, page, tool result) and see if the model obeys them —
   the highest-impact, most-missed class.
4. **Assess impact** — data exfiltration, unauthorized tool/action use, or output
   manipulation resulting from a successful injection.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record `verdict`, injection class (direct/
indirect), the vector, and the impact (data/action). Model resisting across vectors
→ **refuted** for those.

## Impact escalation
Data leakage, unauthorized actions via tools, output manipulation, and (in agents)
chained compromise. CVSS/impact per `_shared/cvss-reference.md`.

## Defenses (design)
- Treat all model-visible content as untrusted; **separate instructions from data**
  (structured prompts, delimiting, spotlighting).
- Constrain capability: least-privilege tools, human-in-the-loop gates for
  consequential actions, and output filtering.
- Don't rely on prompt-level "ignore injections" instructions alone; defense-in-depth
  (input/output checks, allow-lists, sandboxing). Test continuously (ai-red-team).

## References
- `_shared/` rules (authorization, untrusted input, evidence, gated workflow).
