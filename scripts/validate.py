#!/usr/bin/env python3
"""
Skillz marketplace validator.

Checks every skill's SKILL.md frontmatter and body, the naming convention,
duplicate names, marketplace.json structure and path resolution, and runs a
lightweight secret / private-data scan. Exits non-zero on any failure so it
can gate CI.

Usage: python3 scripts/validate.py
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS_DIR = os.path.join(ROOT, "skills")
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
REQUIRED_SECTIONS = [
    "# Purpose", "# When to Use", "# Inputs", "# Outputs", "# Procedure",
    "# Quality Checklist", "# Edge Cases", "# Safety Rules", "# Examples",
]
REQUIRED_MK_KEYS = [
    "name", "description", "path", "category", "source_projects",
    "tags", "compatibility", "status", "public_safe", "last_updated",
]
# Live-secret patterns (NOT the documented detection patterns, which use placeholders).
SECRET_PATTERNS = [
    (re.compile(r"eyJ[A-Za-z0-9_-]{30,}\.[A-Za-z0-9_-]{20,}"), "JWT token"),
    (re.compile(r"sk_live_[A-Za-z0-9]{16,}"), "live secret key"),
    (re.compile(r"sk-or-v1-[A-Za-z0-9]{20,}"), "OpenRouter key"),
    (re.compile(r"whsec_[A-Za-z0-9]{16,}"), "webhook secret"),
    (re.compile(r"(postgres|postgresql|mysql|mongodb)://[A-Za-z0-9_]+:[^@/\s]+@[A-Za-z0-9.]"), "db credentials"),
]
SECRET_ALLOW = ("USER:PASSWORD", "YOUR-", "user:password")


def main() -> int:
    issues = []
    folders = sorted(
        d for d in os.listdir(SKILLS_DIR)
        if os.path.isdir(os.path.join(SKILLS_DIR, d))
    )
    names = []

    for d in folders:
        p = os.path.join(SKILLS_DIR, d, "SKILL.md")
        if not os.path.isfile(p):
            issues.append(f"[frontmatter] {d}: missing SKILL.md")
            continue
        txt = open(p, encoding="utf-8").read()
        m = re.match(r"^---\n(.*?)\n---\n", txt, re.S)
        if not m:
            issues.append(f"[frontmatter] {d}: no frontmatter block")
            continue
        fm = m.group(1)
        nm = re.search(r"^name:\s*(.+)$", fm, re.M)
        ds = re.search(r"^description:\s*(.+)$", fm, re.M)
        if not nm:
            issues.append(f"[frontmatter] {d}: no name")
            continue
        name = nm.group(1).strip()
        names.append(name)
        if name != d:
            issues.append(f"[name-match] {d}: frontmatter name '{name}' != folder")
        if not NAME_RE.match(name):
            issues.append(f"[naming] {name}: bad pattern")
        if len(name) > 64:
            issues.append(f"[naming] {name}: exceeds 64 chars")
        if not ds or len(ds.group(1).strip()) < 20:
            issues.append(f"[description] {d}: missing/short description")
        for section in REQUIRED_SECTIONS:
            if section not in txt:
                issues.append(f"[body] {d}: missing section {section}")

    dups = sorted({n for n in names if names.count(n) > 1})
    if dups:
        issues.append(f"[duplicate] names: {dups}")

    # marketplace.json
    try:
        mk = json.load(open(os.path.join(ROOT, "marketplace.json"), encoding="utf-8"))
        mnames = [s["name"] for s in mk["skills"]]
        for missing in set(folders) - set(mnames):
            issues.append(f"[marketplace] folder missing entry: {missing}")
        for extra in set(mnames) - set(folders):
            issues.append(f"[marketplace] entry without folder: {extra}")
        for s in mk["skills"]:
            for k in REQUIRED_MK_KEYS:
                if k not in s:
                    issues.append(f"[marketplace] {s.get('name','?')}: missing key {k}")
            if not os.path.isdir(os.path.join(ROOT, s.get("path", ""))):
                issues.append(f"[marketplace] {s['name']}: path not found {s.get('path')}")
            if s.get("public_safe") is not True:
                issues.append(f"[marketplace] {s['name']}: public_safe not true")
        used = {s["category"] for s in mk["skills"]}
        undeclared = used - set(mk.get("categories", []))
        if undeclared:
            issues.append(f"[category] used but not declared: {undeclared}")
    except Exception as e:  # noqa: BLE001
        issues.append(f"[marketplace] error: {e}")

    # secret / sensitive-file scan
    for dirpath, dirnames, filenames in os.walk(ROOT):
        if ".git" in dirpath:
            continue
        for fn in filenames:
            if fn in (".env",) or fn.endswith((".pem", ".key", ".p12", ".pfx")) or fn in ("id_rsa", "id_ed25519"):
                if fn != ".env.example":
                    issues.append(f"[secret-file] {os.path.relpath(os.path.join(dirpath, fn), ROOT)}")
            if fn.endswith((".md", ".json", ".txt", ".yml", ".yaml")):
                fp = os.path.join(dirpath, fn)
                try:
                    content = open(fp, encoding="utf-8").read()
                except Exception:
                    continue
                for pat, label in SECRET_PATTERNS:
                    for match in pat.finditer(content):
                        if any(a in match.group(0) for a in SECRET_ALLOW):
                            continue
                        issues.append(f"[secret] {os.path.relpath(fp, ROOT)}: possible {label}")

    print(f"Skills: {len(folders)} | named: {len(names)}")
    if issues:
        print("\nVALIDATION FAILED:")
        for i in issues:
            print("  -", i)
        return 1
    print("All checks passed ✅")
    return 0


if __name__ == "__main__":
    sys.exit(main())
