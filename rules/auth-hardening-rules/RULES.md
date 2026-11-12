---
name: auth-hardening-rules
type: rule
description: >
  Rules for implementing authentication/authorization and sessions securely in
  generated code.
references: [skills/appsec/secure-coding/authz-patterns, skills/offensive/auth-identity/*]
license: MIT
version: 1.0.0
---

# Auth Hardening Rules (assistant)

- **Authorization server-side on every request** — object-level (ownership) + function-
  level (privilege); default-deny; same checks for API and UI.
- **Sessions**: rotate the session id on login/privilege change; invalidate on logout +
  password change; `HttpOnly`+`Secure`+`SameSite` cookies; CSPRNG tokens; sensible
  timeouts.
- **MFA** for sensitive accounts; enforce MFA state server-side; rate-limit + lockout on
  auth; uniform responses (no username enumeration).
- **Password reset**: canonical-host links; single-use, short-lived, user-bound tokens;
  invalidate sessions on reset.
- **JWT**: pin the algorithm (no `none`/client-chosen), strong keys, validate audience/
  expiry, don't trust `kid`/`jku` from input.
- **OAuth/OIDC**: exact `redirect_uri` match, bound `state`, PKCE for public clients.
