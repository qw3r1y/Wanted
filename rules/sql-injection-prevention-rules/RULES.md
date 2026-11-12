---
name: sql-injection-prevention-rules
type: rule
description: >
  Focused rules preventing SQL/NoSQL injection in generated data-access code.
references: [skills/offensive/web/sqli, skills/appsec/secure-coding/input-validation]
license: MIT
version: 1.0.0
---

# SQL/NoSQL Injection Prevention Rules (assistant)

- **Always use parameterized queries / prepared statements**; never build SQL by
  string concatenation or interpolation of user input.
- Use an ORM/query-builder with **bound parameters**; for identifiers (table/column/
  sort) that can't be parameterized, use a strict **allow-list**.
- For NoSQL: **validate types** (reject objects/arrays where scalars are expected) to
  prevent operator injection; don't pass raw user objects into query operators.
- Least-privilege DB accounts (no DDL/file privileges for app users).
- Generic error handling — never return raw DB errors to clients.
