#!/usr/bin/env python3
"""Submit a pixel-recap generation to fal.ai reference-to-video.

Usage:
  FAL_KEY=... python3 generate_fal.py REFS_DIR PROMPT_FILE [options]

Options:
  --model h3|seedance|seedance-fast   default: h3
  --res   768P|2K|4K (h3) | 1080p|720p (seedance)   default: model-appropriate
  --ar    16:9 | 9:16 | ...           default: 16:9
  --duration N seconds                default: 15

Cost at time of writing (15s): h3 768P $1.20, h3 2K $1.95,
seedance-fast ~$3+, seedance ~$10 (token-billed, scales with frames).
h3 bills flat per second; first 5 reference images free, extras $0.08 each.
"""
import os, sys, json

MODELS = {
    "h3":            ("minimax/h3/reference-to-video", "2K"),
    "seedance":      ("bytedance/seedance-2.0/reference-to-video", "1080p"),
    "seedance-fast": ("bytedance/seedance-2.0/fast/reference-to-video", "720p"),
}

def opt(flag, default):
    return sys.argv[sys.argv.index(flag) + 1] if flag in sys.argv else default

def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    refs_dir, prompt_file = sys.argv[1], sys.argv[2]
    key = opt("--model", "h3")
    if key not in MODELS:
        sys.exit(f"--model must be one of: {', '.join(MODELS)}")
    endpoint, default_res = MODELS[key]
    res = opt("--res", default_res)
    ar = opt("--ar", "16:9")
    duration = int(opt("--duration", "15"))
    prompt = open(prompt_file).read()

    try:
        import fal_client
    except ImportError:
        sys.exit("fal_client not installed — run: pip install fal-client")
    if not os.environ.get("FAL_KEY"):
        sys.exit("FAL_KEY not set in the environment")

    files = sorted(f for f in os.listdir(refs_dir) if f.lower().endswith((".png", ".jpg", ".jpeg", ".webp")))
    if not files:
        sys.exit(f"no reference images in {refs_dir}")
    if len(files) > 9:
        sys.exit(f"{len(files)} refs — max is 9")
    urls = [fal_client.upload_file(os.path.join(refs_dir, f)) for f in files]

    # Reference order is upload order — it must match the Image N citations in the prompt.
    print(f"{len(urls)} refs -> {endpoint} @ {res}, {duration}s")
    for i, f in enumerate(files, 1):
        print(f"  Image {i}: {f}")
    if key == "h3" and len(urls) > 5:
        print(f"  note: {len(urls) - 5} ref(s) beyond the free 5 -> +${(len(urls) - 5) * 0.08:.2f}")

    if key == "h3":
        args = {
            "prompt": prompt,
            "reference_image_urls": urls,
            "resolution": res,          # 768P | 2K | 4K
            "aspect_ratio": ar,
            "duration": duration,
        }                                # audio is native and always on
    else:
        args = {
            "prompt": prompt,
            "image_urls": urls,
            "resolution": res,
            "aspect_ratio": ar,
            "duration": duration,
            "generate_audio": True,
            "bitrate_mode": "high",
        }

    handler = fal_client.submit(endpoint, arguments=args)
    print("request_id:", handler.request_id)
    result = handler.get()
    print(json.dumps(result, indent=2))
    url = (result.get("video") or {}).get("url")
    if url:
        print("\nvideo:", url)

if __name__ == "__main__":
    main()
