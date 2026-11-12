---
name: honeytoken-design
description: >
  Use when designing honeytokens — fake credentials, files, API keys, or DB records
  planted so that their use reveals an intruder. High-fidelity, low-cost detection
  spread through the environment. Covers honeytoken strategy.
type: knowledge
domain: deception
maturity: canonical
tools: []
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Honeytoken Design

Honeytokens are planted lures — fake credentials, API keys, documents, or database
rows — that no legitimate process should ever use, so any use is a high-fidelity
intrusion signal. Cheap to spread everywhere (code, configs, databases, file shares),
they catch attackers who've already gotten in.

## When to use
To detect credential theft, data access, and lateral movement cheaply and broadly.

## Procedure (gated phases)
1. **Choose token types** — fake AWS/API keys, decoy credentials, lure documents,
   honey DB records, fake admin accounts.
2. **Make them believable & monitored (core)** — realistic enough to be used; wire
   each to an alert that fires on **any** use/access.
3. **Place widely** — in code/configs (fake keys), databases (honey rows), file shares
   (lure docs), and AD (decoy accounts) — where an attacker would find them.
4. **Operationalize** — alert → high-priority investigation; the token's location tells
   you where the attacker is.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. "Done" = tokens are placed and any use triggers
a reliable alert; near-zero FPs.

## Quality bar / pitfalls
- Tokens that look fake/are never found — make them believable + well-placed.
- Unmonitored tokens (no alert) — the whole point is the alert.

## Linkage
- Pairs with honeypot/canary-tokens; integrates with detection/SOC.

## References
- `_shared/` rules (evidence).
