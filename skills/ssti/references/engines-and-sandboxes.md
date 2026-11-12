# SSTI — Motorlar, Delimiter'lar & Sandbox Notları (4. seviye)

Yetkili test içindir. Önce *evaluation* kanıtla (aritmetik sonuç döndü mü), sonra motoru belirle. Minimal kanıt; RCE-tarzı komuta scope onayı olmadan geçme.

## Motor parmak izi (delimiter/davranış)
| Motor | Delimiter | Ayırt edici ipucu |
|---|---|---|
| Jinja2 (Python) | `{{ }}` / `{% %}` | Python obje modeli; config/attr erişimi |
| Twig (PHP) | `{{ }}` / `{% %}` | Filtre sözdizimi; Symfony bağlamı |
| Freemarker (Java) | `${ }` / `<#...>` | Java tipleri; `?` builtin'ler |
| Velocity (Java) | `#set($x=...)` / `$x` | `#`-direktif, `$`-referans |
| ERB (Ruby) | `<%= %>` | Ruby ifadesi |
| Thymeleaf (Java) | `[[${...}]]` / `th:` | Spring EL |
| Handlebars/Mustache | `{{ }}` | Logic-less (daha sınırlı) |
| Razor (.NET) | `@{ } / @(...)` | C# ifadesi |

> Aynı `{{ }}` deliminitörünü Jinja2/Twig/Handlebars paylaşır → ayırt etmek için
> motor-özel ifade davranışı (filtre, obje erişimi, hata metni) kullan.

## Reach katmanları
1. **Expression-only:** aritmetik/dizgi; veri yok.
2. **Object/data access:** bağlamdaki değişken/attribute/builtin traversal.
3. **Code/command surface:** motor+versiyon+sandbox izin veriyorsa (kritik).

## Sandbox notu
Jinja2 SandboxedEnvironment, Twig sandbox, Freemarker `?api`/new-builtin
kısıtları versiyon-özeldir; sandbox escape'ler yamayla kapanır. "Sandbox var"
demek "güvenli" demek değildir — versiyonu ve bilinen escape durumunu değerlendir,
ama canlı hedefte yalnız minimal kanıt al.

## Remediation hatırlatması
Template'i kullanıcı girdisinden derleme; veriyi **bound context** olarak geçir;
logic-less/sandboxed motor; tehlikeli builtin/reflection kapat; motoru güncel tut.
