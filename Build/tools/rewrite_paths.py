#!/usr/bin/env python3
"""Rewrite citations of moved paths across the repo, driven by a move manifest.

Manifest: TSV with columns from, to, kind. Rules apply longest-source-first so a
nested path (Syriac-Build/L4-Templates/) is rewritten by its outer move before
the inner name could match. A source matches only when not preceded by a path
character, so "Build/reference/L4-Templates/" is never rewritten twice.

Never touched: .git, node_modules, cic/texts (vendored), packages (derived),
Archive (history describes the tree as it was), binaries (.docx .xlsx .pdf .png
.jpg .gif .zip .skill .ico .sqlite). Binaries that contain an old path string are
listed so the ledger can record them as not rewritten.

Usage: rewrite_paths.py MANIFEST [--apply] [--repo DIR]
Without --apply it is a dry run: counts per rule and per file, nothing written.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

TEXT_EXT = {".md", ".txt", ".yaml", ".yml", ".py", ".mjs", ".js", ".ts", ".tsx", ".html", ".css", ".json", ".jsonc", ".toml", ".cfg", ".ini", ".csv", ".svg", ".gan", ""}
BIN_EXT = {".docx", ".xlsx", ".pdf", ".png", ".jpg", ".jpeg", ".gif", ".zip", ".skill", ".ico", ".sqlite", ".db", ".pptx", ".mp4", ".woff", ".woff2", ".ttf"}
SKIP = ("/.git/", "/node_modules/", "/cic/texts/", "/packages/", "/Archive/", "/.claude/",
        # Dated history describes the tree as it was; the move ledger maps old to new.
        "/Build/Ministry/Operations/Audits/", "/Build/Ministry/Operations/Standing/Launch-Prompts/",
        "/Build/Ministry/Operations/Markup-Queue/",
        # Hashed or sealed content: a record is copied byte-for-byte into its package and
        # hashed by the manifest, so one changed byte fails the in-image restore; canon/ is
        # seal-checked. Their citations are baselined for the owning threads.
        "/records/", "/canon/", "/fixtures/")
DATED = re.compile(r"(_|-)20\d\d-\d\d-\d\d|Decision[_-]Log|Change_Log|Thread_Launch|Handoff|_Tracking\.md|Task_Board|Move_Ledger")


def load_manifest(path: Path) -> list[tuple[str, str]]:
    rules = []
    for line in path.read_text(encoding="utf-8").splitlines()[1:]:
        if not line.strip():
            continue
        src, dst, kind = line.split("\t")
        if dst == "DELETE":
            continue
        rules.append((src, dst))
    rules.sort(key=lambda r: -len(r[0]))
    return rules


def compile_rules(rules):
    out = []
    for src, dst in rules:
        pat = re.compile(r"(?<![\w/.\-])" + re.escape(src) + r"(?=$|[/\s\)\]\"'`,.;:*_>])")
        out.append((src, dst, pat))
    return out


def main(argv):
    if not argv:
        print(__doc__)
        return 2
    manifest = Path(argv[0])
    apply = "--apply" in argv
    repo = Path(argv[argv.index("--repo") + 1]) if "--repo" in argv else Path.cwd()
    rules = compile_rules(load_manifest(manifest))
    per_rule = {src: 0 for src, _, _ in rules}
    per_file = {}
    binaries = []
    for p in repo.rglob("*"):
        if not p.is_file():
            continue
        sp = "/" + p.relative_to(repo).as_posix()
        if any(s in sp + "/" for s in SKIP):
            continue
        if sp.startswith("/Build/Ministry/") and DATED.search(p.name):
            continue
        ext = p.suffix.lower()
        if ext in BIN_EXT:
            try:
                raw = p.read_bytes()
            except OSError:
                continue
            hits = [src for src, _, _ in rules if src.encode() in raw]
            if hits:
                binaries.append((sp.lstrip("/"), hits))
            continue
        if ext not in TEXT_EXT:
            continue
        try:
            text = p.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        new = text
        n_file = 0
        for src, dst, pat in rules:
            new, n = pat.subn(dst, new)
            if n:
                per_rule[src] += n
                n_file += n
        if n_file:
            per_file[sp.lstrip("/")] = n_file
            if apply:
                p.write_text(new, encoding="utf-8")
    print("== replacements per rule ==")
    for src, _, _ in rules:
        if per_rule[src]:
            print(f"{per_rule[src]:5d}  {src}")
    print(f"\n== files touched: {len(per_file)}  total replacements: {sum(per_file.values())}  ({'APPLIED' if apply else 'dry run'}) ==")
    by_tree = {}
    for f, n in per_file.items():
        by_tree[f.split('/')[0]] = by_tree.get(f.split('/')[0], 0) + 1
    for t, n in sorted(by_tree.items(), key=lambda x: -x[1]):
        print(f"{n:5d}  {t}")
    if binaries:
        print(f"\n== binaries containing an old path (NOT rewritten; record in ledger): {len(binaries)} ==")
        for f, hits in binaries:
            print(f"  {f}: {', '.join(hits)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
