#!/usr/bin/env python3
"""Deterministically route a project questionnaire to a baseline architecture.

Input is JSON from a file or stdin. This is an advisory classifier: it never
calls a provider or changes infrastructure.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def choose(data: dict) -> dict:
    public = bool(data.get("public", True))
    commercial = bool(data.get("commercial", False))
    secrets = bool(data.get("secrets", False))
    durable = bool(data.get("durable_shared_data", False))
    auth = bool(data.get("auth", False))
    ssr = bool(data.get("ssr", False))
    python_native = bool(data.get("python_or_native", False))
    persistent = bool(data.get("persistent_process", False))
    periodic = bool(data.get("periodic_job", False))
    media = bool(data.get("large_media", False))
    realtime = bool(data.get("realtime", False))
    private_only = bool(data.get("private_only", not public))

    components: list[str] = ["GitHub repository"]
    warnings: list[str] = []
    upgrade: list[str] = []

    if private_only and (python_native or persistent):
        project_type = "local/private service"
        components += ["Mac Mini service", "Tailscale private access"]
        warnings.append("No public exposure without a separate approval and security gate.")
        upgrade.append("Move to Railway when users require cloud availability.")
    elif periodic and not persistent:
        project_type = "batch or scheduled workflow"
        components.append("GitHub Actions or Mac Mini scheduled job")
        if media:
            components.append("Cloudflare R2")
        upgrade.append("Use a Railway job for heavy native work, long runtime, or private networking.")
    elif python_native or persistent or realtime:
        project_type = "container-backed application"
        components += ["Cloudflare or Vercel frontend", "Railway API/container"]
        if durable:
            components.append("Postgres/Supabase")
        if media:
            components.append("Cloudflare R2")
        upgrade.append("Add a separate worker only after sustained queue demand is measured.")
    elif ssr:
        project_type = "full-stack serverless web application"
        components.append("Vercel Pro/Cloudflare" if commercial else "Vercel Free/Cloudflare")
        if durable or auth:
            components.append("Supabase")
        if media:
            components.append("Cloudflare R2")
    elif secrets:
        project_type = "static application with API gateway"
        components += ["Cloudflare static hosting", "Cloudflare Worker"]
        if durable or auth:
            components.append("Supabase or D1")
    else:
        project_type = "static/client application"
        components.append("Cloudflare static hosting")
        if durable or auth:
            components.append("Supabase or D1")
        if media:
            components.append("Cloudflare R2")

    if commercial:
        warnings.append("Do not use Vercel Hobby for a commercial workload.")
    if auth or durable:
        warnings.append("Define backups, migrations, authorization, and data retention.")
    if secrets:
        warnings.append("Keep privileged credentials out of browser bundles.")

    return {
        "project_type": project_type,
        "recommended_components": components,
        "warnings": warnings,
        "upgrade_triggers": upgrade,
        "deployment_approval_status": "NOT REQUESTED",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", nargs="?", help="JSON file; reads stdin when omitted")
    args = parser.parse_args()
    raw = Path(args.input).read_text() if args.input else sys.stdin.read()
    data = json.loads(raw)
    print(json.dumps(choose(data), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
