# Dile Özel Güvenli Kodlama — Pitfalls (4. seviye)

Her dilde idiyomatik tuzaklar + güvenli alternatif. (Kavramsal; kodda enforce için
semgrep/codeql kuralları yaz.)

| Dil | Yaygın tuzak | Güvenli pattern |
|---|---|---|
| Python | pickle/yaml.load deserialization, `subprocess(shell=True)`, `eval/exec` | safe loaders, arg-list subprocess, ast.literal_eval |
| JS/TS | prototype pollution, `eval`, insecure `child_process`, proto-merge | null-proto objects, no eval, safe merge libs |
| Java | native deserialization (gadget chains), XXE, reflection | no untrusted deserialization, XXE-hardened parsers, allow-list |
| Go | SSRF-prone http clients, path traversal, template injection | validate URLs, filepath.Clean+confine, html/template |
| Rust | `unsafe` misuse, integer overflow (release), FFI | minimize `unsafe`, checked arithmetic, audit FFI |
| C# / .NET | BinaryFormatter, ViewState, LDAP/SQL injection | avoid BinaryFormatter, parameterized queries |
| PHP | `include` LFI, `unserialize`, type juggling (`==`) | allow-list includes, no untrusted unserialize, `===` |
| C/C++ | buffer overflow, UAF, format string, integer overflow | bounds checks, smart pointers, `-fsanitize`, no `%n` |

## Ortak
Untrusted deserialization, dynamic eval, shell'e string geçme, XXE, SSRF-prone
client'lar — tüm dillerde tehlikeli. Memory-safe dil + vetted kütüphane + SAST
ile enforce.
