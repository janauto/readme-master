#!/usr/bin/env python3
"""capture_web.py — screenshot a URL or local HTML file for README assets.

Tries shot-scraper first (if on PATH), falls back to Playwright's Python API.

Usage:
    python3 capture_web.py URL_OR_PATH -o docs/assets/shot.png [--width 1280] [--height 800] [--wait 2000] [--selector "#main"] [--js "document.querySelector('.cookie-banner')?.remove()"]

Requires one of:
    pip install shot-scraper && shot-scraper install
    pip install playwright && playwright install chromium
"""
import argparse
import shutil
import subprocess
import sys


def via_shot_scraper(a) -> bool:
    if not shutil.which("shot-scraper"):
        return False
    cmd = ["shot-scraper", a.target, "-o", a.output,
           "--width", str(a.width), "--height", str(a.height), "--wait", str(a.wait)]
    if a.selector:
        cmd += ["-s", a.selector]
    if a.js:
        cmd += ["--javascript", a.js]
    return subprocess.run(cmd).returncode == 0


def via_playwright(a) -> bool:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        return False
    url = a.target
    if "://" not in url:
        import pathlib
        url = pathlib.Path(url).resolve().as_uri()
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": a.width, "height": a.height})
        page.goto(url, wait_until="networkidle")
        page.wait_for_timeout(a.wait)
        if a.js:
            page.evaluate(a.js)
        if a.selector:
            page.locator(a.selector).screenshot(path=a.output)
        else:
            page.screenshot(path=a.output)
        browser.close()
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("target", help="URL or local HTML file path")
    ap.add_argument("-o", "--output", required=True)
    ap.add_argument("--width", type=int, default=1280)
    ap.add_argument("--height", type=int, default=800)
    ap.add_argument("--wait", type=int, default=2000, help="ms to wait before shooting")
    ap.add_argument("--selector", default=None, help="CSS selector to shoot instead of full page")
    ap.add_argument("--js", default=None, help="JS to run before shooting (e.g. hide banners)")
    a = ap.parse_args()

    if via_shot_scraper(a) or via_playwright(a):
        print(f"saved: {a.output}")
    else:
        sys.exit("No capture backend. Install: pip install shot-scraper && shot-scraper install")


if __name__ == "__main__":
    main()
