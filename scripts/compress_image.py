#!/usr/bin/env python3
"""compress_image.py — shrink a generated PNG for README hero use.

Composited hero banners (see visual-capture.md) render at full resolution
(often 2-3 MB) for crispness while authoring, but a README hero should stay
well under ~300 KB so the page loads fast. This resizes to a max edge and,
for PNGs, quantizes to a palette -- a big win on flat-color/gradient
illustrations, typically with no visible banding at 256 colors, but always
eyeball the result before committing.

Usage:
    python3 compress_image.py INPUT.png OUTPUT.png [--max-edge 1920] [--colors 256]

Falls back to pngquant/oxipng on PATH if Pillow isn't installed; if neither
is available, copies the file unchanged and warns.
"""
import argparse
import os
import shutil
import subprocess
import sys


def via_pillow(a) -> bool:
    try:
        from PIL import Image
    except ImportError:
        return False
    im = Image.open(a.input).convert("RGB")
    w, h = im.size
    scale = min(1.0, a.max_edge / max(w, h))
    if scale < 1.0:
        im = im.resize((round(w * scale), round(h * scale)), Image.LANCZOS)
    if a.colors:
        im = im.quantize(colors=a.colors, method=Image.FASTOCTREE, dither=Image.Dither.FLOYDSTEINBERG)
    im.save(a.output, optimize=True)
    return True


def via_cli_tool(a) -> bool:
    shutil.copy(a.input, a.output)
    if shutil.which("pngquant"):
        return subprocess.run(["pngquant", "--quality=75-95", "--force",
                                "--output", a.output, a.output]).returncode == 0
    if shutil.which("oxipng"):
        return subprocess.run(["oxipng", "-o", "4", a.output]).returncode == 0
    return False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input")
    ap.add_argument("output")
    ap.add_argument("--max-edge", type=int, default=1920, help="resize so the longest edge is at most this many px")
    ap.add_argument("--colors", type=int, default=256, help="palette size for quantization (0 = skip, keep full color)")
    a = ap.parse_args()

    if via_pillow(a) or via_cli_tool(a):
        size_kb = os.path.getsize(a.output) // 1024
        print(f"compressed: {a.output} ({size_kb} KB)")
        if size_kb > 300:
            print("warning: still over ~300 KB -- consider a smaller --max-edge or fewer --colors", file=sys.stderr)
    else:
        shutil.copy(a.input, a.output)
        print("warning: no Pillow/pngquant/oxipng found -- copied uncompressed. "
              "pip install pillow for best results.", file=sys.stderr)


if __name__ == "__main__":
    main()
