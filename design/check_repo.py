import io, os, re, glob, pathlib
from playwright.sync_api import sync_playwright
ROOT = r"C:\Users\pkashyap\OneDrive - Warner Bros. Discovery\Personal\Ad-hoc\AI Project\Databricks learning\databricks-at-scale"
os.chdir(ROOT)
issues = []

# 1. posters: overflow + empty band
with sync_playwright() as pw:
    b = pw.chromium.launch(channel="chrome", headless=True)
    for f in sorted(glob.glob("episodes/*/*poster.html")):
        pg = b.new_page(viewport={"width": 1080, "height": 1350})
        pg.goto(pathlib.Path(f).resolve().as_uri())
        pg.wait_for_load_state("networkidle")
        r = pg.evaluate("""(()=>{const p=document.querySelector('.p')||document.querySelector('.poster');
          const t=document.querySelector('.take'), s=document.querySelector('.strip');
          return {over:p.scrollHeight-1350,
                  gap:(t&&s)?Math.round(t.getBoundingClientRect().top-s.getBoundingClientRect().bottom):-1}})()""")
        pg.close()
        flag = ""
        if r["over"] > 0:
            issues.append("%s overflows by %dpx" % (f, r["over"])); flag = "  <-- OVERFLOW"
        if r["gap"] > 90:
            issues.append("%s has a %dpx empty band" % (f, r["gap"])); flag += "  <-- EMPTY BAND"
        print("poster %-46s over=%-4s gap=%s%s" % (f.replace(chr(92),"/").split("/")[1], r["over"], r["gap"], flag))
    b.close()

# 2. markdown links resolve
print()
for md in glob.glob("**/*.md", recursive=True):
    if md.startswith("docs\\private") or md.startswith("docs/private"):
        continue
    base = os.path.dirname(md)
    for link in re.findall(r"\]\(([^)#:]+?)\)", io.open(md, encoding="utf-8").read()):
        if link.startswith(("http", "mailto")):
            continue
        if not os.path.exists(os.path.normpath(os.path.join(base, link))):
            issues.append("broken link in %s -> %s" % (md, link))
# html <img src>
for html in glob.glob("episodes/*/README.md"):
    base = os.path.dirname(html)
    for src in re.findall(r'<img src="([^"]+)"', io.open(html, encoding="utf-8").read()):
        if not os.path.exists(os.path.normpath(os.path.join(base, src))):
            issues.append("broken image in %s -> %s" % (html, src))
print("link check done")

# 3. post bodies: no emoji, length sane
print()
for pm in sorted(glob.glob("episodes/*/*post.md")):
    parts = io.open(pm, encoding="utf-8").read().split("```")
    if len(parts) < 2:
        issues.append("no fenced post body in " + pm); continue
    body = parts[1]
    emo = [c for c in body if ord(c) > 0x1F000]
    n = len(body.encode("utf-16-le")) // 2
    if emo:
        issues.append("%s has %d emoji in the body" % (pm, len(emo)))
    if n > 3000:
        issues.append("%s is %d chars (LinkedIn limit 3000)" % (pm, n))
    print("post %-46s chars=%-6d emoji=%d" % (pm.replace(chr(92),"/").split("/")[1], n, len(emo)))

# 4. employer / brand scan over tracked text
print()
pat = re.compile(r"\bhbo\b|hbo ?max|warner|\bwbd\b|\bjapac\b|discovery\+|cinemax", re.I)
hits = 0
for f in glob.glob("**/*.*", recursive=True):
    nf = f.replace("\\", "/")
    if "/private/" in nf or nf.endswith(("check_repo.py", ".png", ".jpg", ".svg")):
        continue
    try:
        if pat.search(io.open(f, encoding="utf-8", errors="ignore").read()):
            issues.append("brand/employer term in " + f); hits += 1
    except Exception:
        pass
print("brand scan: %d files with hits" % hits)

# 5. each built episode has its five files
print()
for d in sorted(glob.glob("episodes/0[1-9]-*")):
    num = os.path.basename(d)[:2]
    have = [os.path.basename(x) for x in glob.glob(d + "/*") if os.path.isfile(x)]
    need = ["ep%s-learn.md" % num, "ep%s-post.md" % num, "ep%s-poster.html" % num,
            "ep%s-poster.png" % num, "ep%s-cert-prep.md" % num, "README.md"]
    missing = [x for x in need if x not in have]
    state = "complete" if not missing else "placeholder only" if have == ["README.md"] else "MISSING " + ", ".join(missing)
    if missing and have != ["README.md"]:
        issues.append("%s is incomplete: missing %s" % (d, ", ".join(missing)))
    print("%-42s %s" % (os.path.basename(d), state))

# 6. LinkedIn folder mirrors built episodes
print()
for d in sorted(glob.glob("../LinkedIn/0[1-9]-*")):
    print("%-42s %s" % (os.path.basename(d), sorted(os.path.basename(x) for x in glob.glob(d + "/*.*"))))

print("\n" + "=" * 70)
if issues:
    print("ISSUES FOUND (%d):" % len(issues))
    for i in issues:
        print("  -", i)
else:
    print("NO ISSUES FOUND")
