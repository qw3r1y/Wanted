# XSS — Bağlam → Break-out Matrisi (4. seviye varyantlar)

Yetkili test içindir. Amaç: bağlamı tanıyıp **doğru** break-out gereksinimini seçmek;
kör payload denemesi değil. Payload'lar temsilîdir — gerçek testte minimal, zararsız
marker (OOB callback / benign işaret) kullan, kanıtı `OUTPUT_DIR`'a al.

## Bağlam tespiti
Önce canary'nin nereye düştüğünü belirle: HTML metin düğümü mü, attribute mü,
`<script>` içi mi, URL/attribute mü, yoksa yalnız client-side sink mi (sunucu
yansıması yok). Her bağlamın break-out *koşulu* farklıdır.

| # | Bağlam | Break-out koşulu | Tespit ipucu |
|---|---|---|---|
| 1 | HTML text node | Yeni element/handler tanıt | Canary `<div>…CANARY…</div>` içinde ham |
| 2 | Quoted attribute (`value="…"`) | Önce tırnağı/attribute'u kapat | Canary `"…CANARY…"` içinde |
| 3 | Unquoted attribute | Whitespace + event-handler | Canary boşluksuz attribute değerinde |
| 4 | `<script>` / JS string | String/ifadeyi temiz kapat | Canary `var x="…CANARY…"` içinde |
| 5 | URL / `href`/`src` | `javascript:` benzeri şema (filtre yoksa) | Canary link hedefinde |
| 6 | DOM sink | Source→sink'e ulaş (sunucu yansıması gerekmez) | Bundle'da `location`/`referrer`→yazma sink'i |
| 7 | SVG / dosya yükleme | Inline render + gevşek CSP | `image/svg+xml` inline servis |

## DOM-XSS: source → sink
- **Source (kontrol edilen):** `location.hash/search/href`, `document.referrer`,
  `postMessage` verisi, `localStorage`/`sessionStorage`, `document.cookie`.
- **Sink (tehlikeli yazma):** `innerHTML`/`outerHTML`, `document.write`,
  `insertAdjacentHTML`, dinamik `eval`-ailesi, `setAttribute('src'|'href', …)`,
  jQuery `.html()`, framework `dangerouslySetInnerHTML`/`v-html`/`[innerHTML]`/`{@html}`.
- **Yöntem:** bundle'ı indir, source→sink akışını izle; ara filtre/sanitizer var mı
  kontrol et. Akış kırılmıyorsa → exploitable; kırılıyorsa → refuted.

## Filtre/encode gözlemi (refuted sinyalleri)
- `<`/`>` → `&lt;`/`&gt;` dönüşü = doğru encoding.
- Attribute içinde `%22` çözülmez (tarayıcı attribute değerinde URL-decode yapmaz).
- WAF `<` üzerine farklı status/403 = WAF gürültüsü, XSS değil.

## Encoding/bypass düşünme çerçevesi (körlemesine değil, hedefe göre)
Bir filtre gözlemlendiğinde: hangi karakter/anahtar-kelime engelleniyor, hangi
bağlamda? Buna göre meşru-test varyantı seç (büyük/küçük-harf, alternatif
event-handler, alternatif şema, encoding katmanı). Her denemeyi kanıtla; "çalıştı"
demek için tarayıcı yürütmesi veya OOB callback şart.
