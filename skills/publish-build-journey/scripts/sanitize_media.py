#!/usr/bin/env python3
"""Create metadata-stripped raster-image derivatives without overwriting sources."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

try:
    from PIL import Image, ImageOps
except ImportError as exc:  # fail closed
    raise SystemExit("Pillow is required. Install it in the active Python environment before sanitizing media.") from exc


SUPPORTED = {".jpeg", ".jpg", ".png", ".tif", ".tiff", ".webp"}


def digest(path: Path) -> str:
    hasher = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def sanitize(source: Path, output_dir: Path) -> dict[str, object]:
    if source.suffix.lower() not in SUPPORTED:
        raise ValueError(f"Unsupported raster format: {source.suffix}")
    output_dir.mkdir(parents=True, exist_ok=True)
    suffix = ".jpg" if source.suffix.lower() == ".jpeg" else source.suffix.lower()
    target = output_dir / f"{source.stem}-sanitized{suffix}"
    if target.resolve() == source.resolve():
        raise ValueError("Refusing to overwrite the source image.")

    with Image.open(source) as opened:
        image = ImageOps.exif_transpose(opened)
        image.load()
        save_kwargs: dict[str, object] = {}
        if suffix in {".jpg", ".jpeg"}:
            if image.mode not in {"RGB", "L"}:
                background = Image.new("RGB", image.size, "white")
                if "A" in image.getbands():
                    background.paste(image, mask=image.getchannel("A"))
                else:
                    background.paste(image.convert("RGB"))
                image = background
            save_kwargs = {"quality": 90, "optimize": True, "progressive": True}
        elif suffix == ".png":
            save_kwargs = {"optimize": True}
        elif suffix == ".webp":
            save_kwargs = {"quality": 90, "method": 6}
        image.save(target, **save_kwargs)

    return {
        "source": str(source),
        "output": str(target),
        "sha256": digest(target),
        "metadata_stripped": True,
        "visible_frame_reviewed": False,
        "publication_approved": False,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("images", nargs="+", type=Path)
    parser.add_argument("--output-dir", required=True, type=Path)
    args = parser.parse_args()
    try:
        results = [sanitize(path, args.output_dir) for path in args.images]
    except (FileNotFoundError, OSError, ValueError) as exc:
        print(json.dumps({"status": "error", "message": str(exc)}))
        return 2
    print(json.dumps({"status": "sanitized", "assets": results}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
