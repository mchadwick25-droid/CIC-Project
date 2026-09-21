#!/usr/bin/env python3
"""Regenerate cic-website/traditions/<slug>.html for every built world from
its Part-1-compiled cic-website/data/worlds/<census_id>.json (Website V2
world_front design, site cutover stage - CLAUDE.md's "keep the live/
canonical surfaces clean" and the project owner's own ruling: the rebuilt
pages render the world_front's FULL content, not the old 3-section page).

Chrome (everything from <head> through the "seat" CTA block: title, meta
description, breadcrumb, title block, portrait, ai-line, "begin a
conversation" seat, and everything after the article - the door, footer,
script) is preserved BYTE-IDENTICAL from each world's existing hand-built
page. This script never re-derives it from world-census.json (which it
does not touch) - it only surgically replaces the <div class="article">
block's own inner <section> elements. Two of that chrome's own fields -
the portrait's alt text/figcaption, and the ai-line prose - exist nowhere
as structured data (not in world-census.json, not in any record), and a
Representative's own identity/voice is a decision this project always
asks about, never derives from a formula (CLAUDE.md's own escalation
table) - so byte-preserving the existing page, rather than re-deriving
chrome from a template + census fields, is the only fabrication-free way
to do this.

The actual per-world content comes from cic-website/templates/tradition.html
(a real template - see that file's own header comment for its two marker
conventions), filled in per world by this script and then spliced into
that world's own preserved chrome. Content itself is never generated
directly by this script - it shells out to Node against
cic-website/assets/orientation-render.mjs (tools/render_orientation_cli.mjs),
the exact same render functions the Atlas panel imports in the browser
(Part 3), so the two surfaces render identical HTML from identical data
by construction.

Usage:
  python3 tools/generate_tradition_pages.py            regenerate all 8 built worlds
  python3 tools/generate_tradition_pages.py desert alx  regenerate only these world keys
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from engine.m1.registry import load_registry  # noqa: E402

SITE_DATA_DIR = REPO_ROOT / "cic-website" / "data" / "worlds"
TRADITIONS_DIR = REPO_ROOT / "cic-website" / "traditions"
CENSUS_PATH = REPO_ROOT / "cic-website" / "data" / "world-census.json"
RENDER_CLI = REPO_ROOT / "tools" / "render_orientation_cli.mjs"
TEMPLATE_PATH = REPO_ROOT / "cic-website" / "templates" / "tradition.html"

# The 10 built worlds this cutover covers (registry code -> nothing else
# hardcoded; census_id, representative name and the existing page all
# come from the registry / world-census.json / the file already on disk).
# don and rzg were built after the original 8-world cutover and are added
# here for the 2026-09-21 card redesign regen.
BUILT_WORLD_KEYS = ["alx", "cappadocian", "desert", "don", "gallic", "hal", "ijc", "pahc", "rzg", "syr"]

ARTICLE_OPEN = '<div class="article">'
# The literal boilerplate that follows the article's own closing </div> in
# every hand-built page today (verified against desert-monasticism.html
# and syriac-edessa-nisibis.html) - used as the anchor for the article
# block's own end, so nothing after it (the door, footer, script) is ever
# touched.
ARTICLE_CLOSE_ANCHOR = "\n    </div>\n  </div>\n</main>"

# Maps each template {{TOKEN}} to the section key its content comes from
# (cic-website/assets/orientation-render.mjs's own RENDERERS keys, plus
# "questions"). "voices" and friends whose section wrapper the template
# itself doesn't add a <div class="reading"> around get their raw
# (non-"reading"-wrapped) HTML - the template's own markup decides that,
# not this script.
TOKEN_TO_SECTION = {
    "STORY": "story",
    "VOICES": "voices",
    "DOCUMENTED_STORIES": "documented_stories",
    "LEGACY": "legacy",
    "RELATIONS_SUMMARY": "relations_summary",
    "SOURCING": "sourcing",
    "PULL_QUOTES": "pull_quotes",
    "GLOSSARY": "glossary",
    "QUESTIONS": "questions",
}

# Which {{TOKEN}}(s) gate each <!--SECTION:key--> block: the block is
# dropped whole for a world whose compiled JSON has nothing there (e.g. a
# world_front that deliberately leaves orientation.relations_summary
# absent, per its own body notes - desert's pilot report explains why).
SECTION_GATE_TOKENS = {
    "story": ["STORY"],
    "voices": ["VOICES"],
    "documented_stories": ["DOCUMENTED_STORIES"],
    "legacy": ["LEGACY"],
    "relations_summary": ["RELATIONS_SUMMARY"],
    "sourcing": ["SOURCING"],
    "glossary_and_quotes": ["PULL_QUOTES", "GLOSSARY"],
    "questions": ["QUESTIONS"],
}

_SECTION_BLOCK_RE = re.compile(r"<!--SECTION:(\w+)-->(.*?)<!--/SECTION:\1-->", re.DOTALL)
_STYLE_BLOCK_RE = re.compile(r'<style id="tradition-content-css">(.*?)</style>', re.DOTALL)


def render_sections(compiled_path: Path, slug: str, representative_name: str) -> dict[str, str]:
    result = subprocess.run(
        ["node", str(RENDER_CLI), str(compiled_path), slug, representative_name],
        capture_output=True,
        text=True,
        check=True,
        cwd=REPO_ROOT,
    )
    return json.loads(result.stdout)


def load_template() -> tuple[str, str]:
    """(content_css, article_template) - the shared CSS block and the raw
    template text with its <!--SECTION--> markers still in place, read
    fresh every run (never cached) so an edit to the template file always
    takes effect on the next generate."""
    raw = TEMPLATE_PATH.read_text(encoding="utf-8")
    css_match = _STYLE_BLOCK_RE.search(raw)
    if not css_match:
        raise SystemExit(f"{TEMPLATE_PATH}: no <style id=\"tradition-content-css\"> block found")
    content_css = css_match.group(1).strip("\n")
    article_template = raw[css_match.end():]
    return content_css, article_template


def fill_article(article_template: str, sections: dict[str, str]) -> str:
    def replace_block(match: re.Match) -> str:
        key = match.group(1)
        block = match.group(2)
        gate_tokens = SECTION_GATE_TOKENS.get(key, [])
        if not any(sections.get(TOKEN_TO_SECTION[t], "") for t in gate_tokens):
            return ""  # nothing to show for this world - drop the whole section
        for token in gate_tokens:
            block = block.replace("{{" + token + "}}", sections.get(TOKEN_TO_SECTION[token], ""))
        return block

    filled = _SECTION_BLOCK_RE.sub(replace_block, article_template)
    # Tidy only the blank-line runs a dropped section leaves behind. The
    # existing hand-built pages this replaces are themselves pretty-printed,
    # multi-line HTML (verified against the pre-cutover desert/syriac pages
    # - only their <style> blocks are dense), and this generator's own
    # design doc gives committing generated output as the reason a
    # reviewer's diff shows the exact prose change - collapsing every
    # section to one line would erase that property, so the template's and
    # the renderer's own line breaks are kept, not flattened.
    lines = [line.rstrip() for line in filled.strip("\n").split("\n")]
    cleaned: list[str] = []
    for line in lines:
        if line == "" and (not cleaned or cleaned[-1] == ""):
            continue
        cleaned.append(line)
    indented = "\n".join(("      " + line if line else "") for line in cleaned)
    return "\n" + indented + "\n"


def regenerate(world_key: str, registry: dict, census_by_id: dict, content_css: str, article_template: str) -> None:
    entry = registry[world_key]
    census_id = entry["census_id"]
    compiled_path = SITE_DATA_DIR / f"{census_id}.json"
    html_path = TRADITIONS_DIR / f"{census_id}.html"
    if not compiled_path.is_file():
        raise SystemExit(f"{world_key}: no compiled JSON at {compiled_path} - run engine.m2.site_cli build first")
    if not html_path.is_file():
        raise SystemExit(f"{world_key}: no existing page at {html_path} to preserve chrome from")

    census_entry = census_by_id.get(census_id)
    if not census_entry or not census_entry.get("entry", {}).get("representativeName"):
        raise SystemExit(f"{world_key}: world-census.json has no entry.representativeName for {census_id!r}")
    representative_name = census_entry["entry"]["representativeName"]

    sections = render_sections(compiled_path, census_id, representative_name)
    article_inner = fill_article(article_template, sections)

    original = html_path.read_text(encoding="utf-8")

    # The template's own CSS is inserted between two markers so a later
    # edit to the template's CSS (e.g. this session's own docstory-entry
    # fix) replaces what's there rather than accumulating a second, stale
    # copy alongside it - re-running this generator is always idempotent.
    css_begin, css_end = "/* BEGIN orientation-content-css */", "/* END orientation-content-css */"
    css_block = f"{css_begin}\n{content_css}\n{css_end}"
    css_block_re = re.compile(re.escape(css_begin) + r".*?" + re.escape(css_end), re.DOTALL)
    if css_block_re.search(original):
        original = css_block_re.sub(lambda _m: css_block, original, count=1)
    else:
        style_close = "</style>"
        if style_close not in original:
            raise SystemExit(f"{world_key}: {html_path} has no </style> to append new CSS before")
        original = original.replace(style_close, css_block + "\n" + style_close, 1)

    article_start = original.find(ARTICLE_OPEN)
    if article_start == -1:
        raise SystemExit(f"{world_key}: {html_path} has no {ARTICLE_OPEN!r} to replace")
    content_start = article_start + len(ARTICLE_OPEN)
    close_idx = original.find(ARTICLE_CLOSE_ANCHOR, content_start)
    if close_idx == -1:
        raise SystemExit(f"{world_key}: {html_path} has no recognizable article-closing anchor after the article opens")

    new_html = original[:content_start] + article_inner + original[close_idx:]
    html_path.write_text(new_html, encoding="utf-8")
    print(f"{world_key}: regenerated {html_path.relative_to(REPO_ROOT)}")


def main(argv: list[str]) -> int:
    registry = load_registry()
    census = json.loads(CENSUS_PATH.read_text(encoding="utf-8"))
    census_by_id = {m["id"]: m for m in census["movements"]}
    content_css, article_template = load_template()

    world_keys = argv or BUILT_WORLD_KEYS
    for world_key in world_keys:
        if world_key not in registry:
            raise SystemExit(f"{world_key!r} is not in the registry")
        regenerate(world_key, registry, census_by_id, content_css, article_template)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
