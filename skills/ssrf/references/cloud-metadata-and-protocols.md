# SSRF — Cloud Metadata, Filtre-Bypass & Protokol (4. seviye)

Yetkili test içindir. İç/metadata erişimi yalnız tanımlı ağ kapsamında; sınırda dur.
Kör SSRF'de OOB callback zorunlu.

## Cloud metadata hedefleri (kavramsal)
| Sağlayıcı | Not |
|---|---|
| AWS IMDS (169.254.169.254) | IMDSv2 (session-token) zorunluysa basit GET engellenir; kanıt = kimlik bilgisi *ifşası*, kullanma yok |
| GCP metadata | `Metadata-Flavor: Google` header gereği |
| Azure IMDS | `Metadata: true` header gereği |
| Link-local / internal | 169.254.0.0/16, 127.0.0.0/8, RFC1918, fd00::/8, IPv6 link-local |

## Filtre-bypass sınıfları (sinyal → dene)
| Filtre gözlemi | Yaklaşım |
|---|---|
| Hostname kara listesi | DNS rebinding (kayıt TTL=0, iç IP'ye dönen isim) |
| Düz IP engeli | Alternatif IP kodlaması (decimal/octal/hex/IPv6-mapped) |
| Scheme kısıtı | İzinli scheme + redirect zinciri (dış→iç yönlendirme) |
| İlk-host doğrulaması | Redirect sonrası iç host (son hedef doğrulanmıyorsa) |

> Her bypass iddiası canlı OOB/iç-erişim kanıtı ister; teorik değil.

## Protokol smuggling (motor/parser izinliyse)
`gopher://` → ham TCP (ör. Redis/HTTP iç servis komutu), `dict://`, `file://`
(yerel dosya okuma), `ftp://`. Bunlar yüksek-etki; yalnız kapsam izniyle, minimal
kanıtla (servis banner'ı) göster.

## Full-response vs blind
- Full-response: iç yanıt doğrudan görünür → minimal host/port haritası.
- Blind: OOB zamanlama/DNS ile erişilebilirlik çıkarımı.

## Remediation hatırlatması
Allow-list (scheme+host), link-local/metadata bloku (app+ağ), redirect-sonrası
son-hedef doğrulama, DNS pinning, gereksiz scheme kapatma, IMDSv2.
