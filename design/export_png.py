"""Export an HTML poster to PNG for LinkedIn (LinkedIn cannot display HTML).

Usage (from the repo root):
    python design/export_png.py <poster.html>                  # 1080x1350 poster -> 2160x2700 PNG
    python design/export_png.py <page.html> --full --scale 1.5 # whole long page, for reference

Writes <name>.png next to the HTML. Uses Playwright with the installed Chrome
(falls back to Edge, then Playwright's bundled Chromium). Warns if poster content
overflows the frame, so nothing gets clipped silently.
"""
import argparse, pathlib, struct
from playwright.sync_api import sync_playwright

ap = argparse.ArgumentParser()
ap.add_argument("html")
ap.add_argument("--full", action="store_true", help="capture the whole page instead of a 1080x1350 frame")
ap.add_argument("--width", type=int)
ap.add_argument("--height", type=int, default=1350)
ap.add_argument("--scale", type=float, default=2)
ap.add_argument("--out")
a = ap.parse_args()

src = pathlib.Path(a.html).resolve()
out = pathlib.Path(a.out).resolve() if a.out else src.with_suffix(".png")
width = a.width or (1320 if a.full else 1080)

with sync_playwright() as p:
    browser = None
    for channel in ("chrome", "msedge", None):
        try:
            browser = p.chromium.launch(channel=channel, headless=True) if channel else p.chromium.launch(headless=True)
            break
        except Exception:
            pass
    if browser is None:
        raise SystemExit("No browser available (tried Chrome, Edge, bundled Chromium)")
    page = browser.new_page(viewport={"width": width, "height": a.height}, device_scale_factor=a.scale)
    page.goto(src.as_uri())
    page.wait_for_load_state("networkidle")
    if a.full:
        page.screenshot(path=str(out), full_page=True)
    else:
        overflow = page.evaluate(
            f"(() => {{ const e = document.querySelector('.p') || document.body; return e.scrollHeight - {a.height}; }})()")
        if overflow > 0:
            print(f"WARNING: content overflows the poster by {overflow}px - trim spacing before posting")
        page.screenshot(path=str(out), clip={"x": 0, "y": 0, "width": width, "height": a.height})
    browser.close()

with open(out, "rb") as f:
    f.read(16)
    w, h = struct.unpack(">II", f.read(8))
print(f"{out.name}: {w}x{h}, {out.stat().st_size // 1024} KB")
