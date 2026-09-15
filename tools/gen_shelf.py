#!/usr/bin/env python3
"""Generate each world's SHELF.md — the works, loci and roles it may draw from.

The shelf is the world's projection of the library: its tradition's corpus-map bucket
(`cic/corpus-map/<census_id>.yaml`, itself generated from `_staging/`), joined through
`records/worlds.yaml → census_id`, or through an explicit mapping for candidate worlds
that have no registry entry yet. Generated, never hand-edited; carries no notes. Step 2
(Source Ecology) narrows it; WO-4's gate enforces it.

Usage: gen_shelf.py [--worlds DIR] [--only CODE] [--stdout]
"""
from __future__ import annotations

import re
import sys
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent if HERE.name == "tools" else Path.cwd()

# Candidate worlds: no registry entry yet, so the join is stated here until they have one.
CANDIDATES = {
    "gallic": "gallic-monastic-ascetic-christianity",
    "lpc": "latin-pastoral-congregational-christianity",
    "latap": "latin-apologists",
    "grkap": "greek-apologists-second-century",
}


def registry_map() -> dict[str, str]:
    """code -> census_id from records/worlds.yaml (no YAML dependency; the file is regular)."""
    out, code = {}, None
    for line in (REPO / "records" / "worlds.yaml").read_text(encoding="utf-8").splitlines():
        m = re.match(r"^  ([a-z]+):\s*$", line)
        if m:
            code = m.group(1)
            continue
        m = re.match(r'^    census_id:\s*"?([a-z0-9-]+)"?\s*$', line)
        if m and code and m.group(1) != "null":
            out[code] = m.group(1)
    return out


def parse_bucket(path: Path) -> tuple[str, list[dict]]:
    """Minimal reader for the generated bucket: atlas_id + a list of work entries."""
    atlas_id, works, cur = "", [], None
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("atlas_id:"):
            atlas_id = line.split(":", 1)[1].strip()
        elif line.startswith("- work:"):
            cur = {"work": line.split(":", 1)[1].strip().strip("'\"")}
            works.append(cur)
        elif cur is not None and re.match(r"^  [a-z_]+:", line):
            k, v = line.strip().split(":", 1)
            if k != "note":
                cur[k] = v.strip().strip("'\"")
    return atlas_id, works


def render(code: str, census: str, works: list[dict]) -> str:
    roles = {}
    for w in works:
        roles[w.get("role", "?")] = roles.get(w.get("role", "?"), 0) + 1
    lines = [
        f"# Shelf — `{code}`",
        "",
        f"Tradition: `{census}` · {len(works)} works · "
        + " · ".join(f"{r}: {n}" for r, n in sorted(roles.items())),
        "",
        f"Generated {date.today().isoformat()} by `tools/gen_shelf.py` from "
        f"`cic/corpus-map/{census}.yaml`. Do not edit; regenerate. Roles: `tradition` is this "
        "world's own voice and may be voiced; `context`, `antecedent` and `transmission` may be "
        "cited as evidence, never voiced as the world's own.",
        "",
        "| work | author | file | locus | role | confidence |",
        "|---|---|---|---|---|---|",
    ]
    for w in sorted(works, key=lambda x: (x.get("role", ""), x.get("author", ""), x["work"])):
        lines.append(
            f"| {w['work']} | `{w.get('author', '')}` | `{w.get('source_file', '')}` | "
            f"{w.get('locus', '')} | {w.get('role', '')} | {w.get('confidence', '')} |"
        )
    return "\n".join(lines) + "\n"


def main(argv: list[str]) -> int:
    worlds_dir = Path(argv[argv.index("--worlds") + 1]) if "--worlds" in argv else REPO / "worlds"
    only = argv[argv.index("--only") + 1] if "--only" in argv else None
    mapping = {**registry_map(), **CANDIDATES}
    written = 0
    for code, census in sorted(mapping.items()):
        if only and code != only:
            continue
        bucket = REPO / "cic" / "corpus-map" / f"{census}.yaml"
        if not bucket.exists():
            print(f"{code}: no bucket {bucket.name} — skipped", file=sys.stderr)
            continue
        atlas_id, works = parse_bucket(bucket)
        text = render(code, atlas_id or census, works)
        if "--stdout" in argv:
            print(text)
            continue
        target = worlds_dir / code
        if not target.is_dir():
            print(f"{code}: no world directory {target} — skipped", file=sys.stderr)
            continue
        (target / "SHELF.md").write_text(text, encoding="utf-8")
        written += 1
        print(f"{code}: SHELF.md — {len(works)} works")
    print(f"{written} shelves written", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
