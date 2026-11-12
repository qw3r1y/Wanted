# Skill Yazım Standardı (zorunlu)

Bu kütüphanedeki her skill bu standarda uyar. CI (`_meta/validate.py`) denetler.

## 1. Özgünlük (kesin)
- Skill %100 kendi yazımımızdır. Eski korpus **yalnız incelenir** (kapsam/teknik anlamak için); metin kopyalanmaz.
- Frontmatter'da veya gövdede **asla** `inspired_by` / `source` / `upstream` / kopya-kaynağı bulunmaz.
- Defang/bozulma artefaktı (`sYs_DEF(`, `ev_DEF(`, `<?PHP_DEF` vb.) **yasak**.

## 2. Frontmatter (zorunlu şema)
```yaml
---
name: kebab-case-ad          # benzersiz, dizinle uyumlu
description: >               # trigger-odaklı, 3. şahıs, "Use when…"; "Do NOT use for…" ile sınır
type: knowledge|executable|agent|command|mcp|rule
domain: offensive/web        # taksonomi yolu
maturity: canonical|draft
tools: []                    # opsiyonel
references: []               # _shared/ bağlantıları
license: MIT
version: 1.0.0
---
```

## 3. Gövde iskeleti (SKILL.md)
Sıra: `## When to use` → `## Prerequisites` (yetki/kapsam/araç) → `## Procedure` (kapılı fazlar) → `## Verification` (presence≠exploitation, kanıt) → `## Evidence & reporting` → `## False positives / pitfalls` → `## Remediation` → `## References` (_shared + references/).

## 4. Derinlik ölçütü
- Somut, aksiyon-alınabilir; jenerik "güvenli ol" cümleleri değil.
- Tablolar (framework/sink, bypass, önem) tercih edilir.
- 4. seviye varyantlar `references/` içinde tablo olarak (ayrı skill değil).
- Her aktif-test skill'i: yetki kapısı + kanıt kapısı + false-positive reddi içerir.

## 5. Güvenlik çerçevesi
- Tüm offensive içerik **yetkili test** çerçevesinde; `_shared/scope-authorization-rule.md` ve `safe-execution-rules.md` link'lenir.
- Odak: metodoloji, doğrulama, tespit ve **remediation** — ham silahlandırılmış yük dökümü değil.
