# XXE — XML-Backed Formatlar & Teknikler (4. seviye)

Yetkili test içindir. Minimal okuma; billion-laughs/entity-expansion DoS'u canlı hedefte tetikleme. Kör XXE'de OOB zorunlu.

## XML'in saklandığı formatlar (gözden kaçanlar)
| Format | Not |
|---|---|
| Ham `application/xml` / `text/xml` | Doğrudan intake |
| SOAP | XML gövde; eski servisler |
| SAML assertion | İmza+XML; SAML-XXE authn-bypass riski |
| SVG upload | XML tabanlı; inline render → XXE + stored-XSS |
| DOCX/XLSX/PPTX | Zip içinde XML; parser hardening gerek |
| RSS/Atom/sitemap importer | Dış XML çekme |

## Teknik sınıfları
| Sınıf | Koşul | Kanıt |
|---|---|---|
| In-band | Entity değeri yanıtta görünür | Tanımlı entity'nin değeri döndü |
| Blind/OOB | Yansıma yok | Dış entity → unique host'a parser callback'i |
| Parameter-entity (blind extraction) | DTD işleniyor | OOB DTD ile dolaylı veri çıkarımı |
| SSRF-via-XXE | `http:` izinli | İç/metadata endpoint'e erişim |
| File-read | `file:` izinli | Zararsız yerel dosya okuma (minimal) |

## Parser quirk'leri
Encoding hileleri (UTF-16/7), platforma göre `file:`/`http:` izinleri, parametre-
entity desteği, DOCTYPE reddi davranışı. Hangi motor (libxml2, Java JAXP, .NET)
olduğunu hata/davranıştan çıkar.

## Doğrulama
Entity *expansion* veya OOB callback şart; entity'yi anan hata mesajı tek başına
kanıt değildir → **refuted/inconclusive**.

## Remediation hatırlatması
DTD ve external entity'yi kapat (tek en etkili önlem); platforma özel hardening
flag'leri; mümkünse JSON; XML-backed upload'ları da aynı hardening'le parse et.
