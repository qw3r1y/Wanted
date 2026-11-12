---
name: data-leakage
description: >
  Use when testing/defending an LLM app against sensitive-data leakage — system-
  prompt extraction, training/context data disclosure, PII in outputs, and
  cross-user/session leakage. Covers leakage testing and controls (OWASP LLM02/06).
type: knowledge
domain: ai-security/llm-security
maturity: canonical
tools: []
references:
  - _shared/scope-authorization-rule.md
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# LLM Sensitive Data Leakage (test & defend)

Test whether an authorized LLM app leaks what it shouldn't — the system prompt/
instructions, data from its context/RAG (other users' or sensitive documents),
training-data memorization, or PII — and design controls. Cross-session/tenant
leakage is especially high-impact.

> Authorized testing only, with test data (`_shared/scope-authorization-rule.md`).

## When to use
On any LLM app handling sensitive data, multi-tenant context, or RAG.

## Procedure (gated phases)
1. **Map sensitive data** — what's in the system prompt, context/RAG, tools, and
   memory that must not leak; and tenant boundaries.
2. **Extraction tests** — attempts to reveal the system prompt, enumerate/extract
   context or RAG documents, and surface memorized data.
3. **Cross-boundary tests (core)** — whether one user/tenant can obtain another's
   data via shared context/memory/cache.
4. **PII handling** — whether PII appears in outputs/logs inappropriately.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record `verdict`, the leaked data class, and
the vector. Proper isolation/redaction → **refuted**.

## Impact escalation
Disclosure of prompts/secrets/other-users' data, privacy violations, and IP leakage.
CVSS/impact per `_shared/cvss-reference.md`.

## Defenses
- Don't put secrets in prompts; enforce per-tenant isolation of context/memory/
  cache; retrieval authorization (users see only permitted RAG docs); output/PII
  filtering; and log hygiene.

## References
- `_shared/` rules (authorization, evidence).
