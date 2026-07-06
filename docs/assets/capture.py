#!/usr/bin/env python3
"""Regenerate docs/assets/readme-before-after.png from before-after.html.

Screenshots-as-code: the hero image is not hand-drawn — it is a rendered HTML
page captured with Playwright, so it can be regenerated verbatim after the
README template or the source screenshots change.

Usage:
    pip install playwright pillow && playwright install chromium
    python docs/assets/capture.py

Inputs  (all in this directory): before-after.html, crop-pg-default.png,
        crop-pg-random.png  — the two panel screenshots are the real UI shots
        produced by the palette-gen benchmark run (evals/).
Output: readme-before-after.png  (2400px wide, downscaled from a 2x capture)
"""
import asyncio
import pathlib

from playwright.async_api import async_playwright

HERE = pathlib.Path(__file__).resolve().parent
SRC = (HERE / "before-after.html").as_uri()
RAW = HERE / "_hero-raw.png"
OUT = HERE / "readme-before-after.png"
TARGET_WIDTH = 2400


async def main() -> None:
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(
            device_scale_factor=2, viewport={"width": 1740, "height": 1000}
        )
        await page.goto(SRC)
        await page.wait_for_timeout(400)
        await page.screenshot(path=str(RAW), full_page=True)
        await browser.close()

    try:
        from PIL import Image

        img = Image.open(RAW)
        w, h = img.size
        nh = round(h * TARGET_WIDTH / w)
        img.resize((TARGET_WIDTH, nh), Image.LANCZOS).save(OUT, optimize=True)
        RAW.unlink(missing_ok=True)
    except ImportError:
        RAW.rename(OUT)  # Pillow absent: keep the 2x capture as-is

    print(f"wrote {OUT}")


if __name__ == "__main__":
    asyncio.run(main())
