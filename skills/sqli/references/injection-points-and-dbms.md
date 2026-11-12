# SQLi — Enjeksiyon Noktaları & DBMS Varyantları (4. seviye)

Yetkili test içindir. Amaç: bağlamı/motoru tanıyıp doğru oracle'ı seçmek.
Yıkıcı SQL yok; kanıt = tekrarlanabilir differential.

## Enjeksiyon noktaları (sık atlananlar dahil)
URL/body parametreleri · JSON alanları · `ORDER BY`/kolon adı · `LIMIT`/offset ·
arama/filtre · cookie · header'lar (`X-Forwarded-For`, `User-Agent`, `Referer`
→ DB'ye loglanıyorsa) · ikinci-mertebe (stored değer sonradan sorguda kullanılır).

## Bağlam tipi → yaklaşım
| Bağlam | Balans gereği |
|---|---|
| String literal (`'…'`) | Tırnağı dengele/kapat |
| Numeric | Tırnak yok; aritmetik/mantık ile |
| Identifier (`ORDER BY col`) | Parametrelenemez → allow-list beklenir; test et |
| LIKE/arama | `%`/`_` ve escape davranışı |

## DBMS parmak izi (hata/fonksiyon/sözdizimi)
| İpucu | Olası motor |
|---|---|
| `You have an error in your SQL syntax` | MySQL/MariaDB |
| `unterminated quoted string` / `pg_` | PostgreSQL |
| `Unclosed quotation mark` / `CONVERT` | MSSQL |
| `ORA-00933` / `ORA-` | Oracle |
| Dosya-tabanlı, `SQLITE_` | SQLite |

## Oracle varyantları (temsilî, motor-özel sözdizimi referansla)
- **Boolean-blind:** doğru/yanlış mantık ifadesi ile stabil içerik farkı.
- **Time-blind:** motor-özel bekletme (MySQL `SLEEP`, PostgreSQL `pg_sleep`,
  MSSQL `WAITFOR DELAY`, Oracle `DBMS_LOCK.SLEEP`) — 2–3x tekrar, jitter ele.
- **Error-based:** parser/convert hatasıyla çıktı sızdırma.
- **UNION:** kolon sayısı/tip hizalaması sonrası marker satır.
- **OOB:** motorun dış-bağlantı yeteneğiyle unique host'a callback (tam kör).

## sqlmap (yetkiliyse) sınırları
Onaylanan oracle'a `--technique` sabitle; `--level`/`--risk` muhafazakâr; hassas
tablolarda `--dump` yalnız açık onayla; hız/eşzamanlılık kapsamdaki limite uyar.
