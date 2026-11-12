# Command Injection — Shell Bağlamı & Kör Oracle'lar (4. seviye)

Yetkili test içindir. Yalnız **zararsız, sınırlı** komut (bounded delay / OOB ping). Yıkıcı/exfil/persistence komutu yok.

## Girdi bağlamı → break-out gereği
| Bağlam | Koşul |
|---|---|
| Unquoted argument | Komut ayracı ile yeni komut (ör. `;`, `&&`, `|`, `` ` ``, `$()`) |
| Quoted argument | Önce tırnağı kapat, sonra ayraç |
| Argument-only (ayraç filtreli) | Flag/opsiyon enjeksiyonu (daha düşük etki) |
| Windows cmd/powershell | `&`, `|`, `;` davranışı Unix'ten farklı |

> Doğru break-out, girdinin komuta **nasıl gömüldüğüne** bağlıdır; körlemesine
> ayraç denemek yerine bağlamı gözlemle.

## OS tespiti (zararsız prob)
Benign bir komutun çıktısı/gecikmesiyle Linux mu Windows mu olduğunu çıkar
(ör. yol ayracı, temel komut farkları). Ayrıcalık bağlamını minimal gözle.

## Kör oracle'lar
| Oracle | Kanıt |
|---|---|
| Time-blind | Sınırlı, tekrarlanabilir gecikme (2–3x; jitter/rate-limit ele) |
| OOB (DNS/HTTP) | Sunucu unique host'u çözer/ister → token'lı callback |
| In-band | Zararsız komut çıktısının yansıması (ör. mevcut kullanıcı/dizin) |

## Doğrulama
Yan etki (gecikme/callback) attributable ve tekrarlanabilir olmalı. Girdiyi anan
hata metni = yürütme değil → **inconclusive**. Non-repeatable timing = latency.

## Remediation hatırlatması
Shell'den kaçın (parametreli process API, arg dizisi); katı allow-list; shell
metakarakterlerini reddet; native kütüphane tercih et; least-privilege + sandbox;
anomali komut loglama/alarm.
