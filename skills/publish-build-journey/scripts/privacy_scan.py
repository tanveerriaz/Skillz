#!/usr/bin/env python3
"""Fail-closed text/privacy scanner for proposed public build-journey artifacts."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path


MAX_BYTES = 5 * 1024 * 1024
TEXT_SUFFIXES = {
    ".css", ".csv", ".html", ".ini", ".js", ".json", ".jsx", ".md",
    ".mdx", ".py", ".rst", ".svg", ".toml", ".ts", ".tsx", ".txt",
    ".xml", ".yaml", ".yml",
}
MEDIA_SUFFIXES = {".gif", ".heic", ".jpeg", ".jpg", ".mov", ".mp4", ".png", ".tif", ".tiff", ".webp"}
SENSITIVE_NAMES = re.compile(r"(^|[._-])(\.env|credentials?|secrets?|private[-_]?key|id_rsa|id_ed25519|cookies?|session)([._-]|$)", re.I)


@dataclass(frozen=True)
class Finding:
    severity: str
    category: str
    path: str
    line: int | None
    message: str


PATTERNS: tuple[tuple[str, str, re.Pattern[str]], ...] = (
    ("high", "private-key", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |PGP )?PRIVATE KEY-----")),
    ("high", "bearer-token", re.compile(r"(?i)\bBearer\s+[A-Za-z0-9._~+/=-]{12,}")),
    ("high", "jwt", re.compile(r"\beyJ[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}\b")),
    ("high", "openai-key", re.compile(r"\bsk-(?:proj-)?[A-Za-z0-9_-]{16,}\b")),
    ("high", "github-token", re.compile(r"\b(?:ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9]{20,}\b")),
    ("high", "google-api-key", re.compile(r"\bAIza[A-Za-z0-9_-]{25,}\b")),
    ("high", "aws-access-key", re.compile(r"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b")),
    ("high", "assigned-secret", re.compile(r"(?i)\b(?:api[_-]?key|secret|password|passwd|token|client[_-]?secret)\s*[:=]\s*[\"']?[A-Za-z0-9_./+~=-]{8,}")),
    ("medium", "absolute-user-path", re.compile(r"(?:/Users/[^/\s]+|/home/[^/\s]+|[A-Za-z]:\\Users\\[^\\\s]+)(?:[/\\][^\s\"'<>]*)?")),
    ("medium", "localhost-or-private-network", re.compile(r"(?i)(?:https?://)?(?:localhost|127\.0\.0\.1|0\.0\.0\.0|10\.\d{1,3}\.\d{1,3}\.\d{1,3}|192\.168\.\d{1,3}\.\d{1,3})(?::\d+)?")),
    ("medium", "email-address", re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.I)),
    ("medium", "phone-number", re.compile(r"(?<!\w)(?:\+?\d[\s().-]*){8,15}(?!\w)")),
    ("medium", "precise-coordinates", re.compile(r"(?<!\d)[-+]?(?:[1-8]?\d(?:\.\d{4,})?|90(?:\.0+)?)[,\s]+[-+]?(?:1[0-7]\d(?:\.\d{4,})?|\d?\d(?:\.\d{4,})?|180(?:\.0+)?)(?!\d)")),
)


def redact_message(category: str) -> str:
    return {
        "private-key": "Private key material detected; value suppressed.",
        "bearer-token": "Bearer token detected; value suppressed.",
        "jwt": "JWT-like token detected; value suppressed.",
        "openai-key": "OpenAI-style key detected; value suppressed.",
        "github-token": "GitHub-style token detected; value suppressed.",
        "google-api-key": "Google-style API key detected; value suppressed.",
        "aws-access-key": "AWS-style access key detected; value suppressed.",
        "assigned-secret": "Assigned credential-like value detected; value suppressed.",
        "absolute-user-path": "Absolute local user path detected.",
        "localhost-or-private-network": "Localhost or private-network address detected.",
        "email-address": "Email address detected; confirm it is intentionally public.",
        "phone-number": "Phone-number-like sequence detected.",
        "precise-coordinates": "Precise coordinate-like value detected.",
    }[category]


def iter_files(inputs: list[Path]) -> list[Path]:
    files: set[Path] = set()
    for item in inputs:
        if item.is_file():
            files.add(item)
        elif item.is_dir():
            for child in item.rglob("*"):
                if child.is_file() and ".git" not in child.parts:
                    files.add(child)
    return sorted(files)


def scan_file(path: Path) -> list[Finding]:
    findings: list[Finding] = []
    display = str(path)
    if SENSITIVE_NAMES.search(path.name):
        findings.append(Finding("high", "sensitive-filename", display, None, "Sensitive filename detected; file contents were not read."))
        return findings
    if path.suffix.lower() in MEDIA_SUFFIXES:
        findings.append(Finding("medium", "media-review", display, None, "Media requires metadata sanitization and visible-frame review."))
        return findings
    if path.suffix.lower() not in TEXT_SUFFIXES or path.stat().st_size > MAX_BYTES:
        return findings
    raw = path.read_bytes()
    if b"\x00" in raw:
        return findings
    text = raw.decode("utf-8", errors="replace")
    for line_number, line in enumerate(text.splitlines(), 1):
        for severity, category, pattern in PATTERNS:
            if pattern.search(line):
                findings.append(Finding(severity, category, display, line_number, redact_message(category)))
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="+", type=Path)
    parser.add_argument("--json", action="store_true", dest="as_json")
    args = parser.parse_args()

    missing = [str(path) for path in args.paths if not path.exists()]
    if missing:
        payload = {"status": "error", "missing": missing, "findings": []}
        print(json.dumps(payload, indent=2) if args.as_json else f"Missing paths: {', '.join(missing)}")
        return 2

    findings = [finding for path in iter_files(args.paths) for finding in scan_file(path)]
    high = sum(item.severity == "high" for item in findings)
    medium = sum(item.severity == "medium" for item in findings)
    status = "blocked" if high else ("review" if medium else "clean")
    payload = {
        "status": status,
        "summary": {"high": high, "medium": medium, "files_scanned": len(iter_files(args.paths))},
        "findings": [asdict(item) for item in findings],
        "publication_approved": False,
        "note": "A clean scan does not authorize publication.",
    }
    if args.as_json:
        print(json.dumps(payload, indent=2))
    else:
        print(f"Privacy scan: {status} ({high} high, {medium} medium)")
        for item in findings:
            location = f"{item.path}:{item.line}" if item.line else item.path
            print(f"[{item.severity.upper()}] {item.category} — {location} — {item.message}")
        print(payload["note"])
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
