#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
Usage: verify_video.sh --video FILE [--source-root DIR] [--destination FILE] [--allow-claims]

Verifies video metadata, complete decode, source secrets/unsupported claims, and optional delivery integrity.
USAGE
}

video=""
source_root=""
destination=""
allow_claims=0

while [[ $# -gt 0 ]]; do
  case "$1" in
    --video) video="${2:-}"; shift 2 ;;
    --source-root) source_root="${2:-}"; shift 2 ;;
    --destination) destination="${2:-}"; shift 2 ;;
    --allow-claims) allow_claims=1; shift ;;
    -h|--help) usage; exit 0 ;;
    *) echo "Unknown argument: $1" >&2; usage >&2; exit 2 ;;
  esac
done

[[ -n "$video" ]] || { echo "--video is required" >&2; exit 2; }
[[ -f "$video" ]] || { echo "Video not found: $video" >&2; exit 1; }

for command_name in ffprobe ffmpeg; do
  command -v "$command_name" >/dev/null || { echo "Missing required command: $command_name" >&2; exit 1; }
done

codec=$(ffprobe -v error -select_streams v:0 -show_entries stream=codec_name -of csv=p=0 "$video")
width=$(ffprobe -v error -select_streams v:0 -show_entries stream=width -of csv=p=0 "$video")
height=$(ffprobe -v error -select_streams v:0 -show_entries stream=height -of csv=p=0 "$video")
fps=$(ffprobe -v error -select_streams v:0 -show_entries stream=r_frame_rate -of csv=p=0 "$video")
audio_codec=$(ffprobe -v error -select_streams a:0 -show_entries stream=codec_name -of csv=p=0 "$video" || true)
duration=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$video")

case "$codec" in h264|hevc|vp9|av1) ;; *) echo "Unsupported or missing video codec: $codec" >&2; exit 1 ;; esac
awk -v n="$width" 'BEGIN { exit !(n > 0) }' || { echo "Invalid width: $width" >&2; exit 1; }
awk -v n="$height" 'BEGIN { exit !(n > 0) }' || { echo "Invalid height: $height" >&2; exit 1; }
awk -v n="$duration" 'BEGIN { exit !(n > 0) }' || { echo "Invalid duration: $duration" >&2; exit 1; }

ffmpeg -hide_banner -v error -i "$video" -f null -

if [[ -n "$source_root" ]]; then
  [[ -d "$source_root" ]] || { echo "Source root not found: $source_root" >&2; exit 1; }
  command -v rg >/dev/null || { echo "Missing required command for source scans: rg" >&2; exit 1; }
  rg_args=(--hidden -l -i --glob '!.git/**' --glob '!node_modules/**' --glob '!.next/**' --glob '!dist/**' --glob '!build/**' --glob '!renders/**' --glob '!snapshots/**')
  secret_pattern='(api[_-]?key|access[_-]?token|bearer[_-]?token|password|client[_-]?secret)[[:space:]]*[:=][[:space:]]*[^$<{[:space:]]+'
  if matches=$(rg "${rg_args[@]}" "$secret_pattern" "$source_root" 2>/dev/null); then
    echo "Potential secrets found in files (values suppressed):" >&2
    printf '%s\n' "$matches" >&2
    exit 1
  fi
  if [[ "$allow_claims" -eq 0 ]]; then
    claim_pattern='download (the )?app|app store|google play|order now|trusted by|endorsed by|official partner'
    if matches=$(rg "${rg_args[@]}" "$claim_pattern" "$source_root" 2>/dev/null); then
      echo "Potential unsupported ad claims found in files:" >&2
      printf '%s\n' "$matches" >&2
      echo "Verify evidence, then rerun with --allow-claims only if intentional." >&2
      exit 1
    fi
  fi
fi

if [[ -n "$destination" ]]; then
  [[ -f "$destination" ]] || { echo "Destination not found: $destination" >&2; exit 1; }
  cmp "$video" "$destination"
  if command -v shasum >/dev/null; then
    source_hash=$(shasum -a 256 "$video" | awk '{print $1}')
    destination_hash=$(shasum -a 256 "$destination" | awk '{print $1}')
  else
    source_hash=$(sha256sum "$video" | awk '{print $1}')
    destination_hash=$(sha256sum "$destination" | awk '{print $1}')
  fi
  [[ "$source_hash" == "$destination_hash" ]] || { echo "SHA-256 mismatch" >&2; exit 1; }
  echo "sha256=$source_hash"
fi

printf 'verified video=%s duration=%s resolution=%sx%s fps=%s video_codec=%s audio_codec=%s\n' \
  "$video" "$duration" "$width" "$height" "$fps" "$codec" "${audio_codec:-none}"
