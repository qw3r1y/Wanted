---
name: crypto-usage-rules
type: rule
description: >
  Rules for correct cryptography usage in generated code — safe defaults, no misuse.
references: [skills/appsec/secure-coding/crypto-usage-review, skills/crypto/*]
license: MIT
version: 1.0.0
---

# Crypto Usage Rules (assistant)

- **Never hand-roll crypto** — use vetted library defaults.
- **Encryption**: authenticated encryption (AES-GCM / encrypt-then-MAC); never ECB;
  unique random IV/nonce per message; protect + rotate keys (secret manager).
- **Hashing**: SHA-256+ for integrity; for passwords use a **slow salted KDF**
  (argon2/bcrypt/scrypt), never fast/unsalted hashes.
- **Randomness**: CSPRNG for all security values (tokens/keys/IV/salt), ≥128-bit; never
  `Math.random`/`rand()`/time-seeded.
- **TLS**: validate certificates + hostnames (never disable/trust-all); TLS 1.2+.
- No hardcoded keys; separate keys per purpose; consider crypto-agility.
