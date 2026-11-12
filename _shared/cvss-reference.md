# Ortak Referans: CVSS & Önem Derecelendirme

> Bulgu üreten her skill bu referansa link verir. Amaç: tutarlı, savunulabilir severity.

## İlke
Severity, **gösterilen** etkiye dayanır — teorik en-kötü senaryoya değil. Her metrik,
kanıtla gerekçelendirilir (bkz. `evidence-confidence-rule.md`).

## CVSS v3.1 Base metrikleri (özet)
| Metrik | Değerler | Not |
|---|---|---|
| Attack Vector (AV) | Network/Adjacent/Local/Physical | Uzaktan sömürülebilirlik |
| Attack Complexity (AC) | Low/High | Koşul/hazırlık gereği |
| Privileges Required (PR) | None/Low/High | Saldırganın başlangıç yetkisi |
| User Interaction (UI) | None/Required | Kurban etkileşimi gerekli mi |
| Scope (S) | Unchanged/Changed | Güvenlik-sınırı/yetki aşıldı mı (büyük etki) |
| Confidentiality/Integrity/Availability (C/I/A) | None/Low/High | **Gösterilen** etki |

## Severity bantları (Base score)
- 9.0–10.0 **Critical** · 7.0–8.9 **High** · 4.0–6.9 **Medium** · 0.1–3.9 **Low** · 0.0 None

## Puanlama disiplini
- C/I/A'yı yalnız **kanıtladığın** etkiye göre seç; abartma → triage düşürür, güven kaybı.
- **Scope**: etki başka bir güvenlik otoritesine/bileşene taştıysa Changed (ör. SSRF→iç
  sistem, sandbox escape) — skoru belirgin yükseltir.
- PR/UI'yi gerçekçi değerlendir (auth gerekiyorsa PR:Low/High; kurban tıklaması
  gerekiyorsa UI:Required).

## Bağlam (EPSS/KEV/çevresel)
Base skor sabit kalsa da gerçek risk için: **EPSS** (sömürü olasılığı), **KEV** (aktif
sömürü), erişilebilirlik (internet-facing mi), ve varlık kritikliği dikkate alınır
(bkz. vulnerability-management). Raporda base + bağlamı birlikte sun.

## Tipik örnekler (kavramsal)
- Stored XSS (admin panelinde) ≫ self-XSS. · RCE/command-injection → genellikle Critical.
- IDOR (PII okuma) → Medium/High (veri hassasiyetine göre). · Missing security header
  (tek başına) → genelde Low/Info.
