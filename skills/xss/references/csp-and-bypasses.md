# XSS — CSP Okuma ve Yaygın Zayıflık Sınıfları

Amaç: bir enjeksiyon bulununca, hedefin **Content-Security-Policy**'si yürütmeyi
engelliyor mu yoksa zayıf mı — bunu değerlendirmek. Yetkili test içindir.

## 1. CSP'yi oku
```bash
curl --max-time 30 -skI "https://target/" | grep -i "content-security-policy"
```
`script-src`, `default-src`, `object-src`, `base-uri` direktiflerine bak. Yürütme
kararını belirleyen `script-src`'tir.

## 2. Zayıflık sınıfları (sinyal → sonuç)
| Gözlem | Anlam |
|---|---|
| CSP yok / `X-XSS-Protection: 0` ve CSP yok | İnline script serbest → yürütme muhtemel |
| `script-src 'unsafe-inline'` | İnline handler/script çalışır → CSP koruması etkisiz |
| `script-src *` veya geniş whitelist | Güvenilir host'tan script yüklenebilir |
| İzin verilen CDN'de açık JSONP/eval endpoint | Whitelist üzerinden yürütme |
| `base-uri` serbest | `<base>` ile relatif script yollarını yönlendirme |
| `object-src` kısıtsız | Eski plugin tabanlı vektörler |
| Nonce tekrar kullanılıyor/sabit | Nonce öngörülebilir → inline enjekte edilebilir |

## 3. Güçlü CSP (refuted sinyali)
`script-src 'nonce-…' 'strict-dynamic'`, `unsafe-inline` yok, dar whitelist,
`object-src 'none'`, `base-uri 'none'` → enjeksiyon olsa bile yürütme büyük olasılıkla
**engellenir**. Bu durumda bulguyu "injection present, execution blocked by CSP
(inconclusive/low)" olarak işaretle; kesin iddia için gerçek yürütme kanıtı iste.

## 4. Doğrulama disiplini
CSP'yi "bypass ettim" demek için: canlı hedefte gerçek yürütme (tarayıcı/OOB) kanıtı
şart. Teorik bypass, kanıt değildir. Tüm denemeleri `OUTPUT_DIR` altında belgele.

## 5. Remediation bağlantısı
Zayıf CSP bulgusu raporlanırken önerilen düzeltme: nonce/hash tabanlı katı CSP,
`unsafe-inline` kaldırma, whitelist daraltma, `object-src 'none'`, `base-uri 'none'`.
