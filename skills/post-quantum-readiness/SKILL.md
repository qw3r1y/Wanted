---
name: post-quantum-readiness
description: >
  Use when assessing an organization's post-quantum cryptography readiness —
  inventorying quantum-vulnerable crypto, prioritizing by data longevity, and
  planning migration to PQC. Covers crypto-agility and PQC planning.
type: knowledge
domain: crypto
maturity: canonical
tools: []
references:
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Post-Quantum Readiness

Quantum computers will break today's public-key crypto (RSA/ECC), and "harvest-now,
decrypt-later" means long-lived data is already at risk. Assess where
quantum-vulnerable crypto is used, prioritize by how long the data must stay
confidential, and plan migration to post-quantum algorithms with crypto-agility.

## When to use
For strategic crypto planning, especially for long-lived sensitive data.

## Procedure (gated phases)
1. **Inventory crypto** — where public-key crypto (RSA/ECC/DH) is used (TLS, signing,
   key exchange, data-at-rest key wrapping).
2. **Prioritize by data longevity** — data that must stay secret for years is most
   exposed to harvest-now-decrypt-later.
3. **Assess crypto-agility** — how hard is it to swap algorithms? (hardcoded vs
   abstracted crypto).
4. **Plan migration** — toward NIST PQC standards (hybrid during transition);
   improve crypto-agility first.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Deliverable: a crypto inventory + prioritized
PQC migration/agility plan.

## Quality bar / pitfalls
- Treating PQC as urgent for all data vs prioritizing long-lived secrets.
- No crypto-agility → painful future migration.

## Remediation
- Build crypto-agility; adopt hybrid/PQC for long-lived data; track NIST PQC
  standardization; inventory and plan.

## References
- `_shared/` rules (evidence).
