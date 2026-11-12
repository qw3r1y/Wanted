---
name: model-serialization-security
description: >
  Use when assessing the risk of loading ML models from untrusted sources — model
  files (pickle, etc.) that can execute code on load, and the ML supply chain
  (model hubs). Covers safe model loading and ML supply-chain risk.
type: knowledge
domain: ml-model-security
maturity: canonical
tools: []
references:
  - _shared/untrusted-input-rule.md
  - _shared/evidence-confidence-rule.md
license: MIT
version: 1.0.0
---

# Model Serialization & ML Supply Chain

Loading a model from an untrusted source can be **remote code execution**: common
formats (Python pickle and others) execute arbitrary code on deserialization. Combined
with downloading models from public hubs, this makes the ML supply chain a real RCE/
backdoor risk. Assess how models are obtained and loaded.

> Treat downloaded models as untrusted code (`_shared/untrusted-input-rule.md`).

## When to use
When loading third-party/pretrained models or building ML pipelines that ingest model
files.

## Procedure (gated phases)
1. **Inventory model sources** — where models come from (public hubs, vendors,
   user-uploaded) and the formats used.
2. **Deserialization risk (core)** — pickle/other code-executing formats loaded from
   untrusted sources = RCE on load; prefer safe formats (safetensors).
3. **Supply-chain trust** — model provenance/integrity (signatures/hashes), and
   backdoor risk in third-party weights (data-poisoning-ml).
4. **Defend** — use safe serialization formats; verify provenance/integrity; sandbox
   loading of untrusted models; scan where possible.

## Verification & evidence
`_shared/evidence-confidence-rule.md`. Record unsafe-load paths + untrusted sources.

## Impact escalation
RCE on model load; backdoored models in production. Critical. CVSS per
`_shared/cvss-reference.md`.

## Defenses
- Safe formats (safetensors) over pickle; verify provenance/integrity; sandbox
  untrusted model loading; vet model sources; treat the ML supply chain like software
  supply chain.

## References
- `_shared/` rules (untrusted input, evidence).
