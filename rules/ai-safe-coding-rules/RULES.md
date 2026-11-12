---
name: ai-safe-coding-rules
type: rule
description: >
  Rules for building LLM/agent features safely — encodes ai-security directives for the
  assistant when writing AI-integrated code.
references: [skills/ai-security/llm-security/*, skills/ai-security/agent-security/*]
license: MIT
version: 1.0.0
---

# AI-Safe Coding Rules (assistant)

When building LLM/agent features:
- **Treat all model-visible content as untrusted** — user input, retrieved/RAG docs,
  tool outputs, web content. Separate instructions from data; don't rely on
  prompt-level "ignore injections".
- **Treat model output as untrusted** at every sink — encode for HTML, don't execute
  generated code/commands unsandboxed, validate URLs (SSRF), parameterize queries.
- **Least agency** — give agents only needed tools, least-privilege; **gate
  consequential/irreversible actions** with a human-in-the-loop.
- **RAG authorization** — users retrieve only documents they're allowed to.
- Don't put secrets in prompts; isolate per-user context/memory; add usage limits
  (denial-of-wallet).
- Validate tools' inputs (model-supplied, possibly injected); sandbox tool execution.
