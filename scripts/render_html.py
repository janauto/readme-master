#!/usr/bin/env python3
"""render_html.py — render a local, self-contained HTML file to a fixed-size PNG.

Used for composited hero banners and other generated visuals (see
references/visual-capture.md -> "Web UI -- composited hero banner"): author a
small HTML+CSS file that lays out brand copy plus a real screenshot embedded
via <img>, then shoot it at an exact pixel size for a crisp README hero.

Usage:
    python3 render_html.py INPUT.html OUTPUT.png [--width 1600] [--height 760] [--scale 2] [--wait 400]

Requires: pip install playwright && playwright install chromium
"""
import argparse
import pathlib
import sys

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    sys.exit("playwright not found. Install: pip install playwright && playwright install chromium")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input", help="local HTML file (relative asset paths resolve from its folder)")
    ap.add_argument("output", help="PNG path to write")
    ap.add_argument("--width", type=int, default=1600)
    ap.add_argument("--height", type=int, default=760)
    ap.add_argument("--scale", type=float, default=2, help="device scale factor (2 = retina)")
    ap.add_argument("--wait", type=int, default=400, help="ms to wait for fonts/layout before shooting")
    a = ap.parse_args()

    src = pathlib.Path(a.input).resolve()
    if not src.exists():
        sys.exit(f"not found: {src}")
    url = src.as_uri()

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": a.width, "height": a.height}, device_scale_factor=a.scale)
        page.goto(url)
        page.wait_for_timeout(a.wait)
        page.screenshot(path=a.output, clip={"x": 0, "y": 0, "width": a.width, "height": a.height})
        browser.close()

    print(f"rendered: {a.output} ({a.width}x{a.height} @{a.scale}x)")


if __name__ == "__main__":
    main()
