# Ortak Referans: OWASP Eşlemeleri

> Web/API/LLM skill'leri için hızlı OWASP referansı.

## OWASP Web Top 10 (2021) → ilgili skill'ler
- A01 Broken Access Control → web/idor, api/bola, api/bfla, secure-coding/authz-patterns
- A02 Cryptographic Failures → crypto/*, secure-coding/crypto-usage-review
- A03 Injection → web/sqli, web/xss, web/command-injection, web/ssti, web/nosql-injection
- A04 Insecure Design → appsec/threat-modeling/*
- A05 Security Misconfiguration → cloud-infra/*, secure-coding/framework-hardening
- A06 Vulnerable Components → appsec/sast-dast/dependency-scanning, supply-chain/*
- A07 Identification & Auth Failures → auth-identity/*, api/jwt-attacks, api/oauth-oidc-abuse
- A08 Software & Data Integrity Failures → web/insecure-deserialization, supply-chain/*
- A09 Logging & Monitoring Failures → defensive/detection-engineering, blue-team-ops
- A10 SSRF → web/ssrf, api/webhook-abuse

## OWASP API Top 10 (2023) → ilgili skill'ler
- API1 BOLA → api/bola · API2 Broken Auth → auth-identity/*, api/jwt-attacks
- API3 Broken Object Property (mass assignment) → api/mass-assignment
- API4 Resource Consumption / rate-limit → api/rate-limit-bypass
- API5 BFLA → api/bfla · API6 Sensitive Business Flows → web/business-logic
- API7 SSRF → web/ssrf · API8 Misconfig → cloud/secure-coding
- API9 Inventory Mgmt → api/api-recon, api/swagger-openapi-abuse, easm
- API10 Unsafe 3rd-party API consumption → supply-chain

## OWASP LLM Top 10 → ilgili skill'ler
- LLM01 Prompt Injection → ai-security/llm-security/prompt-injection
- LLM02 Insecure Output Handling → ai-security/llm-security/insecure-output-handling
- LLM03 Training Data Poisoning → ml-model-security/data-poisoning-ml
- LLM04 Model DoS → (usage limits) · LLM05 Supply Chain → ml-model-security/model-serialization-security
- LLM06 Sensitive Info Disclosure → ai-security/llm-security/data-leakage
- LLM07 Insecure Plugin Design → ai-security/agent-security/tool-abuse-defense, mcp-security
- LLM08 Excessive Agency → ai-security/agent-security/excessive-agency-control
- LLM09 Overreliance → (output validation) · LLM10 Model Theft → ml-model-security/model-extraction-defense
