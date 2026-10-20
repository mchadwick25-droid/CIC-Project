#!/usr/bin/env python3
"""One-time chrome migration for cic-website/traditions/<census_id>.html.

generate_tradition_pages.py keeps each page's chrome byte for byte and only
replaces the <div class="article"> block. The tradition page is now laid out
around the tradition, not the Representative (Decision-Log, 2026-10-20), so
the chrome changes too: the title block and portrait become an era band, a
hero and a side column (an "At a glance" panel and a small card that ties the
portrait to Talk and Table); the AI line and the seat block go.

This script rewrites that part of each page once. It is idempotent (a page
that already has the era band is left alone) and it never touches the article
block, the head, the header, the door or the footer apart from the door's one
link text. Run it, then run generate_tradition_pages.py.

Usage:
  python3 Build/tools/migrate_tradition_chrome.py
"""
from __future__ import annotations

import html
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT))

TRADITIONS_DIR = REPO_ROOT / "cic-website" / "traditions"
CENSUS_PATH = REPO_ROOT / "cic-website" / "data" / "world-census.json"
FALLBACK_TINT = "#D9B35C"
TIMELINE_END = 2000
TIMELINE_TICKS = (0, 500, 1000, 1500, 2000)

ICON_TALK = '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 5h16v11H10l-5 4v-4H4z"/></svg>'
ICON_TABLE = '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 5v8M8 9h8M6 21v-5h12v5"/></svg>'


def esc(text: str) -> str:
    return html.escape(text, quote=True)


def _one(pattern: str, text: str, label: str, flags: int = re.S) -> re.Match:
    match = re.search(pattern, text, flags)
    if not match:
        raise SystemExit(f"chrome migration: could not find {label}")
    return match


_WORLD_RULES = (
    re.compile(r"\b(This|this|That|that)((?: whole| same)?) world(?P<p>['\u2019]s)?\b"),
    re.compile(r"\bits own world\b"),
)


def tradition_not_world(text: str) -> str:
    """Mark's rule: the first reference to the tradition in a piece of text
    says "Christian tradition", later ones "tradition" (unless the word
    already came earlier in the text)."""
    out, pos = "", 0
    spans = sorted((m.start(), m.end(), m) for rx in _WORLD_RULES for m in rx.finditer(text))
    for start, end, m in spans:
        if start < pos:
            continue
        before = out + text[pos:start]
        noun = "tradition" if re.search(r"\btraditions?\b", before, re.I) else "Christian tradition"
        if m.re is _WORLD_RULES[0]:
            replacement = f"{m.group(1)}{m.group(2)} {noun}{m.group('p') or ''}"
        else:
            replacement = f"its own {noun}"
        out = before + replacement
        pos = end
    return out + text[pos:]


def timeline_svg(start: int, end: int, label: str) -> str:
    left, right = 10, 290
    span = right - left

    def x(year: int) -> float:
        return left + span * min(max(year, 0), TIMELINE_END) / TIMELINE_END

    bar_x = x(start)
    bar_w = max(x(end) - bar_x, 4)
    def tick(t: int) -> str:
        anchor = "start" if t == 0 else ("end" if t == TIMELINE_END else "middle")
        return f'<text x="{x(t):.1f}" y="46" text-anchor="{anchor}">{t}</text>'

    ticks = "".join(tick(t) for t in TIMELINE_TICKS)
    return (
        f'<svg viewBox="0 0 300 54" role="img" aria-label="{esc(label)}">'
        f'<line class="axis" x1="{left}" y1="22" x2="{right}" y2="22"/>'
        f'<rect class="bar" x="{bar_x:.1f}" y="14" width="{bar_w:.1f}" height="16" rx="3"/>'
        f"{ticks}</svg>"
    )


def build_chrome(page: str, movement: dict, eras: dict) -> str:
    entry = movement["entry"]
    era = eras[movement["era"]]
    tint = era.get("chooserTint") or FALLBACK_TINT

    h1 = _one(r"<h1>(.*?)</h1>", page, "the h1").group(1)
    formal = _one(r'<p class="formal">(.*?)</p>', page, "the formal name").group(1)
    # The hero's description is the page's own existing short description,
    # word for word (not the census tile, which has moved on for some
    # traditions): the text on these pages is not being rewritten. The one
    # change is Mark's rule of 2026-10-20, "tradition" in place of "world".
    tile = tradition_not_world(html.unescape(_one(r'<p class="tile">(.*?)</p>', page, "the tile text").group(1)))
    img = _one(r'<aside class="plate".*?<img ([^>]*)>', page, "the portrait image").group(1)
    src = _one(r'src="([^"]*)"', img, "the portrait src").group(1)
    alt = _one(r'alt="([^"]*)"', img, "the portrait alt").group(1)
    tree_href = _one(r'<p class="tree-link"><a href="([^"]*)"', page, "the tree link").group(1)
    talk_href = _one(r'id="seat-begin" href="([^"]*)"', page, "the Talk link").group(1)
    held = _one(r'(    <div class="held" id="held" hidden>.*?</div>\n)', page, "the held-question block").group(1)

    name = entry["representativeName"]
    census_id = movement["id"]
    era_label = f'{era["no"]}. {era["title"].replace(" Era", "")}'
    facts = [("Period", movement["dates"]), ("Place", movement["region"]), ("Era", era_label)]
    aliases = [a["name"] for a in entry.get("aliases", [])]
    if aliases:
        facts.append(("Also known as", "; ".join(aliases)))
    shaped = entry.get("shaped") or []
    if shaped:
        facts.append(("Shaped by", ", ".join(shaped)))
    dl = "\n".join(f"          <div><dt>{esc(k)}</dt><dd>{esc(v)}</dd></div>" for k, v in facts)
    timeline = timeline_svg(
        movement["start"], movement["end"], f'{movement["dates"]} on a line from 0 to {TIMELINE_END} CE'
    )

    table_href = f"../table.html?worlds={census_id}"
    return f'''    <div class="era-band" style="--era:{tint}"><span>{esc(era_label)}</span><span>{esc(era["dates"])}</span></div>
    <div class="hero">
      <div class="hero-main">
        <p class="ident">{esc(movement["dates"])} &middot; {esc(movement["region"])}</p>
        <h1>{h1}</h1>
        <p class="formal">{formal}</p>
        <p class="tile">{esc(tile)}</p>
        <p class="to-story"><a href="#story">Listen to the story</a></p>
      </div>
      <div class="side">
        <aside class="facts" aria-labelledby="facts-title">
          <h2 id="facts-title">At a glance</h2>
          <div class="span">{timeline}</div>
          <dl>
{dl}
          </dl>
          <a class="tree" href="{tree_href}">See it on the Church Family Tree &rarr;</a>
        </aside>
        <div class="meet" role="group" aria-label="Meet {esc(name)}">
          <img src="{src}" alt="{alt}" width="573" height="573">
          <p class="meet-name">{esc(name)}</p>
          <div class="acts">
            <a class="act primary" id="seat-begin" href="{talk_href}" data-ask aria-label="Talk with {esc(name)}"><span class="disc">{ICON_TALK}</span>Talk</a>
            <a class="act" href="{table_href}" aria-label="Add {esc(name)} to a table"><span class="disc">{ICON_TABLE}</span>Table</a>
          </div>
        </div>
      </div>
    </div>

{held}'''


def migrate(path: Path, movement: dict, eras: dict) -> bool:
    page = path.read_text(encoding="utf-8")
    if 'class="era-band"' in page:
        return False
    start = _one(r'    <div class="titleblock">', page, "the title block").start()
    seat = _one(r'    <div class="seat" role="region".*?</div>\n', page, "the seat block")
    end = seat.end()
    # Everything between the title block and the end of the seat block (the
    # portrait, the tree link, the AI line, the held block, the seat) is
    # rebuilt from the page's own fields and the census.
    chrome = build_chrome(page, movement, eras)
    new_page = page[:start] + chrome + page[end:]
    door_old = "The other voices →"
    if door_old in new_page:
        new_page = new_page.replace(door_old, "The other traditions →", 1)
    path.write_text(new_page, encoding="utf-8")
    return True


def main() -> int:
    census = json.loads(CENSUS_PATH.read_text(encoding="utf-8"))
    by_id = {m["id"]: m for m in census["movements"]}
    eras = {e["num"]: e for e in census["eras"]}
    changed = 0
    for path in sorted(TRADITIONS_DIR.glob("*.html")):
        movement = by_id.get(path.stem)
        if not movement or not movement.get("entry", {}).get("representativeName"):
            continue
        if migrate(path, movement, eras):
            changed += 1
            print(f"migrated {path.relative_to(REPO_ROOT)}")
    print(f"{changed} page(s) migrated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
