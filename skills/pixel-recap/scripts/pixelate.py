#!/usr/bin/env python3
"""Convert event photos to 8-bit pixel-art stills.

Usage: python3 pixelate.py SRC_DIR [OUT_DIR] [--grid 160] [--colors 40] [--width 1280]
Defaults: OUT_DIR = SRC_DIR/pixel
"""
from PIL import Image, ImageEnhance, ImageOps
import os, sys, glob

def arg(flag, default, cast=int):
    return cast(sys.argv[sys.argv.index(flag) + 1]) if flag in sys.argv else default

EXTS = (".jpg", ".jpeg", ".png", ".webp", ".heic")

def main():
    positional = [a for a in sys.argv[1:] if not a.startswith("--")
                  and (sys.argv.index(a) == 1 or not sys.argv[sys.argv.index(a) - 1].startswith("--"))]
    if not positional:
        sys.exit(__doc__)
    src = os.path.expanduser(positional[0])
    out = os.path.expanduser(positional[1]) if len(positional) > 1 else os.path.join(src, "pixel")
    os.makedirs(out, exist_ok=True)

    PIX_W = arg("--grid", 160)          # pixel grid width (8-bit feel)
    COLORS = arg("--colors", 40)        # palette size
    UPSCALE_W = arg("--width", 1280)    # final output width

    paths = sorted(p for p in glob.glob(os.path.join(src, "*")) if p.lower().endswith(EXTS))
    if not paths:
        sys.exit(f"no images in {src}")

    for path in paths:
        name = os.path.splitext(os.path.basename(path))[0]
        img = Image.open(path)
        # phone photos are often stored rotated — honour EXIF before anything else
        img = ImageOps.exif_transpose(img).convert("RGB")
        w, h = img.size
        # boost saturation + contrast for that punchy 8-bit palette
        img = ImageEnhance.Color(img).enhance(1.45)
        img = ImageEnhance.Contrast(img).enhance(1.15)
        # downscale to pixel grid
        ph = max(1, round(PIX_W * h / w))
        small = img.resize((PIX_W, ph), Image.LANCZOS)
        # quantize to limited palette (median cut)
        small = small.quantize(colors=COLORS, method=Image.MEDIANCUT, dither=Image.Dither.NONE).convert("RGB")
        # upscale nearest-neighbor for crisp pixels
        uh = round(UPSCALE_W * ph / PIX_W)
        big = small.resize((UPSCALE_W, uh), Image.NEAREST)
        dest = os.path.join(out, f"{name}_8bit.png")
        big.save(dest)
        print(f"{name}: {w}x{h} -> {big.size[0]}x{big.size[1]}")
    print(f"done -> {out}")

if __name__ == "__main__":
    main()
