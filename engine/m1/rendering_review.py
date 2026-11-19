"""The rendering-review check: a record's `modern_rendering` cannot pass
without a named Opus review file that lists it.

Each world keeps its reviews in `Build/worlds/<world>/Review-Artifacts/`. A
rendering review log there (`Rendering_Review_Log*.md`) is a table with one row per record:

    | Record | Review file(s) | Verdict on the rendering |

The record cell is the record id with or without its `<world>.<type>.` prefix.
A record passes when a log row names it and at least one review file that row
names exists in that folder, mentions Opus, and itself mentions the record. The
gate asks that a named review exists; it does not read the verdict.
"""
import re
from functools import lru_cache
from pathlib import Path

from .loader import REPO_ROOT

_ROW = re.compile(r"^\|\s*(?P<record>[^|]+?)\s*\|\s*(?P<files>[^|]+?)\s*\|\s*(?P<verdict>[^|]+?)\s*\|\s*$")
_FILE = re.compile(r"[\w.\-]+\.md")


def review_dir(world_key: str) -> Path:
    return REPO_ROOT / "Build" / "worlds" / world_key / "Review-Artifacts"


@lru_cache(maxsize=32)
def _text(path: str) -> str:
    return Path(path).read_text(encoding="utf-8", errors="replace")


def log_rows(world_key: str) -> dict[str, list[str]]:
    """record cell -> the review files its row names, over every rendering review log in the world's folder."""
    rows: dict[str, list[str]] = {}
    folder = review_dir(world_key)
    if not folder.is_dir():
        return rows
    for log in sorted(folder.glob("Rendering_Review_Log*.md")):
        for line in _text(str(log)).splitlines():
            match = _ROW.match(line)
            if not match or match["record"].lower() == "record" or set(match["record"]) <= {"-", " ", ":"}:
                continue
            if match["verdict"].strip():
                rows.setdefault(match["record"].strip(), []).extend(_FILE.findall(match["files"]))
    return rows


def _short(rid: str) -> str:
    return rid.split(".", 2)[-1]


def _lists(rid: str, text: str) -> bool:
    """The review text names the record id, full or short, not as the start of a longer id."""
    return any(re.search(rf"(?<![\w.-]){re.escape(name)}(?![\w-])", text) for name in (rid, _short(rid)))


def gate_rendering_review(records, fleet, registry) -> list[str]:
    rendered = {rid: r for rid, r in records.items() if isinstance(r.get("modern_rendering"), str) and r["modern_rendering"].strip()}
    if not rendered:
        return []
    world_key = next(iter(rendered)).split(".")[0]
    rows = log_rows(world_key)
    folder = review_dir(world_key)
    findings = []
    for rid in sorted(rendered):
        files = rows.get(rid) or rows.get(_short(rid))
        if not files:
            findings.append(f"{rid}: no rendering review log row names this record")
            continue
        named = [folder / name for name in dict.fromkeys(files)]
        existing = [p for p in named if p.is_file()]
        if not existing:
            findings.append(f"{rid}: its log row names review files that do not exist: {', '.join(p.name for p in named)}")
            continue
        if not any("Opus" in _text(str(p)) and _lists(rid, _text(str(p))) for p in existing):
            findings.append(f"{rid}: none of its named review files mentions Opus and this record: {', '.join(p.name for p in existing)}")
    return findings
