# -*- coding: utf-8 -*-
# Kalite-kapisi: kutuphanedeki her SKILL.md/AGENT.md/COMMAND.md/PATTERN.md/RULES.md'yi
# standarda gore denetler. CI'da calistirilir. Kod/skill URETMEZ.
import os, re, sys, json
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # my-skills/
FM = re.compile(r'^---\s*\n(.*?)\n---\s*\n', re.S)
# Ozgunluk: kopya-kaynagi alanlari YASAK
FORBIDDEN_FM = ("inspired_by", "source:", "upstream", "upstream_commit", "sources:")
# Defang/bozulma artefaktlari YASAK
DEFANG = re.compile(r'(sYs_DEF\(|sh_DEF\(|pt_DEF\(|ev_DEF\(|<\?PHP_DEF|b64_DEF|pO_DEF\(|pOpen_DEF\()')
TRIGGER = re.compile(r'use (this skill )?(when|whenever|if)', re.I)

def fm_block(txt):
    m = FM.match(txt)
    return (m.group(1), txt[m.end():]) if m else (None, txt)

def main():
    errors = []; warnings = []; checked = 0
    for dp, _, fns in os.walk(ROOT):
        for fn in fns:
            if fn not in ("SKILL.md", "AGENT.md", "COMMAND.md", "PATTERN.md", "RULES.md"):
                continue
            p = os.path.join(dp, fn); rel = os.path.relpath(p, ROOT)
            checked += 1
            try: txt = open(p, encoding="utf-8").read()
            except Exception as e: errors.append(f"{rel}: okunamadi ({e})"); continue
            fm, body = fm_block(txt)
            # 1) frontmatter var mi
            if fm is None:
                errors.append(f"{rel}: frontmatter YOK"); continue
            low_fm = fm.lower()
            # 2) ozgunluk: kopya-kaynagi alani yasak
            for bad in FORBIDDEN_FM:
                if re.search(r'^\s*'+re.escape(bad), fm, re.M) or bad in low_fm:
                    errors.append(f"{rel}: YASAK kopya-kaynagi alani '{bad.strip(':')}'")
            # 3) defang artefakti yasak
            if DEFANG.search(txt):
                errors.append(f"{rel}: defang/bozulma artefakti bulundu")
            # 4) zorunlu alanlar
            for req in ("name", "description"):
                if not re.search(r'^\s*'+req+r'\s*:', fm, re.M):
                    errors.append(f"{rel}: zorunlu alan '{req}' eksik")
            # 5) SKILL.md ozel: trigger-desc + type/domain + iskelet basliklari
            if fn == "SKILL.md":
                mdesc = re.search(r'description:\s*(.*?)(?:\n[a-z_]+:|\n---|$)', fm, re.S)
                desc = mdesc.group(1) if mdesc else ""
                if not TRIGGER.search(desc):
                    warnings.append(f"{rel}: description trigger-odakli degil ('use when...')")
                for req in ("type", "domain"):
                    if not re.search(r'^\s*'+req+r'\s*:', fm, re.M):
                        errors.append(f"{rel}: '{req}' eksik")
                for head in ("When to use", "Procedure", "Remediation"):
                    # bazilari 'Role & workflow'/'Deployment' kullanir; sadece uyar
                    pass
            # 6) _shared referanslari var mi (link verilen dosyalar mevcut mu)
            for refm in re.finditer(r'(_shared/[A-Za-z0-9_.-]+\.md)', txt):
                refp = os.path.join(ROOT, refm.group(1))
                if not os.path.isfile(refp):
                    warnings.append(f"{rel}: eksik referans {refm.group(1)}")
    print(f"Denetlenen dosya: {checked}")
    print(f"HATA: {len(errors)} | UYARI: {len(warnings)}")
    for e in errors[:50]: print("  [HATA]", e)
    for w in warnings[:30]: print("  [uyari]", w)
    json.dump({"checked": checked, "errors": errors, "warnings": warnings},
              open(os.path.join(os.path.dirname(__file__), "validation-report.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    sys.exit(1 if errors else 0)

if __name__ == "__main__":
    main()
