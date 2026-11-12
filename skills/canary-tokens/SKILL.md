---
name: canary-tokens
description: >
  Use when deploying canary tokens — specific trackable triggers (URLs, documents,
  DNS, cloud keys) that alert when accessed — for targeted tripwires on sensitive
  assets and exfiltration detection. Covers canary-token use.
type: knowledge
domain: deception
maturity: canonical
tools: []
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Canary Tokens

Canary tokens are individual tripwires — a unique URL, a tracked document, a DNS
callback, or a decoy cloud key — that phone home when triggered, pinpointing
unauthorized access or exfiltration. A focused, easy form of deception for specific
sensitive assets.

## When to use
To place targeted tripwires on sensitive files/systems and detect exfiltration.

## Procedure (gated phases)
1. **Select token types** — tracked documents (alert on open), unique URLs/DNS tokens,
   decoy cloud keys (alert on use), and folder/share tokens.
2. **Place on sensitive assets (core)** — in sensitive document stores, "important"-
   looking files, and places exfiltrated data would be opened; each uniquely
   identifiable.
3. **Alert** — trigger → immediate alert with context (which token, source);
   investigate as potential compromise/exfil.
4. **Maintain** — track token locations; refresh.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. "Done" = tokens alert reliably on trigger with
identifying context.

## Quality bar / pitfalls
- Tokens triggered by legitimate processes (FPs) — place where only an intruder goes.
- Losing track of where tokens are placed.

## Linkage
- The lightweight end of honeypot/honeytoken deception; feeds SOC/IR.

## References
- `_shared/` rules (evidence).
