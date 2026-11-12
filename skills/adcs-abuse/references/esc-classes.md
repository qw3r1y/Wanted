# ADCS ESC Sınıfları — Özet (4. seviye)

Yetkili test içindir. Her sınıf bir yanlış-yapılandırma kategorisidir; minimal kanıt
(issuance), issued cert'i kötüye kullanma yok.

| ESC | Özet (kavramsal) | Kök neden |
|---|---|---|
| ESC1 | Enrollee-supplied SAN + client-auth EKU + düşük-yetki enroll | Template SAN'a izin veriyor |
| ESC2 | Any-purpose/SubCA EKU ile geniş kullanım | Aşırı geniş EKU |
| ESC3 | Enrollment Agent template kötüye kullanımı | Agent hakları gevşek |
| ESC4 | Template üzerinde zayıf ACL (yazma) | ACL misconfig → template'i düzenle |
| ESC6 | CA'da EDITF_ATTRIBUTESUBJECTALTNAME2 | CA SAN'ı request'ten alıyor |
| ESC7 | CA üzerinde zayıf ACL (ManageCA/Certificates) | CA yönetim hakları |
| ESC8 | HTTP(S) web enrollment'a NTLM relay | Enrollment'ta EPA/HTTPS yok |
| ESC9/10 | No-security-extension / zayıf eşleme | Sertifika↔hesap eşleme zayıf |
| ESC11 | RPC enrollment relay | IF_ENFORCEENCRYPTICERTREQUEST yok |

## Tespit/doğrulama
Template ve CA ayarlarını enumerate et; bir sınıfı doğrula; minimal issuance ile
kanıtla. Hardened template/approval/EPA → ilgili sınıf refuted.

## Remediation hatırlatması
Enrollee-SAN kapat, EKU daralt, manager-approval, enroll haklarını kısıtla, web
enrollment'ta HTTPS+EPA, CA/template ACL denetimi, issuance monitoring,
strong certificate mapping.
