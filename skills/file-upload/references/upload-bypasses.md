# File Upload — Doğrulama Bypass Matrisi (4. seviye)

Yetkili test içindir. Yalnız **zararsız marker** dosya; gerçek web shell/malware yok. Amaç: tehlikeli disposition'a ulaşılabilir mi — shell düşürmek değil.

## Kontrol → bypass sınıfı
| Doğrulama | Test yaklaşımı |
|---|---|
| Client-side only | İsteği doğrudan gönder (sunucu kontrolü yok) |
| Uzantı deny-list | Alternatif/çift uzantı, büyük-küçük harf, trailing nokta/boşluk/null gözlemi |
| Uzantı allow-list | İzinli uzantı + içerik uyuşmazlığı (polyglot) |
| `Content-Type` header | Header spoof (izinli MIME ver, içerik farklı) |
| Magic-byte sniffing | İzinli magic-byte prefix + zararlı gövde (polyglot) |
| Image re-encode | Re-encode'a dayanıklı vektör yoksa → muhtemel refuted |
| Boyut/isim | Path-traversal filename (`../`), aşırı uzun ad |

## Disposition → sonuç
| Depolama/servis | Olası sonuç |
|---|---|
| Executable path + sunucu interprete ediyor | RCE (zararsız token-echo ile kanıt) |
| Aynı origin'de inline servis (SVG/HTML) | Stored XSS (OOB ile kanıt) |
| Parse edilen format (SVG/Office) | SSRF/XXE (ilgili skill) |
| Traversal ile hedef-dışı yazma | Overwrite/DoS (bounded, zararsız) |
| Sandbox/non-exec origin + doğru MIME | Yüksek-etki refuted/low |

## Polyglot & traversal notu
Polyglot = hem geçerli izinli format hem de tehlikeli içerik (ör. geçerli resim +
ek yorum/uç). Traversal = filename'de yol bileşeni. Her ikisi de yalnız zararsız
marker ile, kanıt amaçlı.

## Doğrulama
"Yüklendi" ≠ "çalışır/render olur". Stored path/URL'yi al, disposition'ı (echo/
OOB/overwrite) kanıtla. Artefaktları mümkünse temizle, yollarını kaydet.

## Remediation hatırlatması
İçerik-tabanlı doğrulama + resim re-encode, katı allow-list, sunucu-üretimi rastgele
isim, web-root dışı/non-exec origin, doğru Content-Type + attachment + nosniff,
inline SVG/HTML render etme, XXE-hardened parse.
