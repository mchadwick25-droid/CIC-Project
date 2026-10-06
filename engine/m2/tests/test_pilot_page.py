"""The pilot page on the website: the words Mark approved, the figures from the
operations file, and the audience link that carries into the app."""
import json
import re
import shutil
import subprocess
from pathlib import Path

from engine.api.deeper_ops import load_ops
from engine.deeper import tokens
from engine.m2.tests.test_go_deeper_pages import NUMBER_WORDS, _text_of
from engine.m7.turn_readability import score_turn

REPO = Path(__file__).resolve().parents[3]
SITE = REPO / "cic-website"
PAGE = SITE / "pilot.html"
SCRIPT = SITE / "assets" / "pilot.js"


def _node(code: str):
    node = shutil.which("node")
    assert node, "node is required to run the page script tests"
    out = subprocess.run([node, "-e", code], capture_output=True, text=True, check=True, timeout=60)
    return json.loads(out.stdout)


def _long_date(day) -> str:
    return f"{day.day} {day.strftime('%B %Y')}"


def test_the_offer_is_the_words_mark_approved():
    blocks = _text_of(PAGE.read_text())
    assert "Join the pilot" in blocks
    assert any(
        b.startswith("Go Deeper lets you keep talking after a free conversation ends. Join the pilot and we give you one free pack:")
        and b.endswith("conversations.")
        for b in blocks
    )
    assert any(b.startswith("In return, we ask you to answer a short questionnaire after") and b.endswith("You do not need to give your name or email.") for b in blocks)
    assert "Places are limited." in blocks
    assert 'id="pilot-button"' in PAGE.read_text() and ">Get my free pack<" in PAGE.read_text()


def test_the_figures_are_the_pilot_packs_in_the_operations_file():
    ops = load_ops()
    pack = next(p for p in ops.packs if p.price_usd == ops.pilot_pack_usd)
    html = PAGE.read_text()
    assert re.search(r'data-ops="pilot-tokens">' + f"{pack.tokens:,}" + "<", html)
    words = re.search(r'data-ops="pilot-conversations">([a-z-]+)<', html).group(1)
    assert words == NUMBER_WORDS[pack.tokens // tokens.conversation_cost(ops.rates, ops.rates.free_rounds)]


def test_the_pilots_one_end_date_on_the_page_is_the_operations_files():
    ops = load_ops()
    found = re.findall(r"<span data-pilot-end>([^<]+)</span>", PAGE.read_text())
    assert found == [_long_date(ops.pilot_end_date)]


def test_the_page_names_no_price_and_reads_at_the_target_level():
    text = " ".join(_text_of(PAGE.read_text()))
    assert not re.search(r"[$€£]|\b(USD|dollars?|cents?)\b|\d+\s*%", text, re.I), text
    score = score_turn(text)
    assert score.scored and score.passed, score.failures


def test_the_page_is_unlisted_unlinked_and_empty_until_the_site_config_opens_the_pilot():
    html = PAGE.read_text()
    assert 'name="robots" content="noindex"' in html
    assert '<section class="hero" id="pilot-offer" hidden' in html
    assert re.search(r"pilot:\s*false", (SITE / "assets" / "go-deeper-config.js").read_text())
    for path in SITE.rglob("*"):
        if path.suffix in (".html", ".xml", ".txt", ".js") and path != PAGE and path != SCRIPT:
            assert "pilot.html" not in path.read_text(errors="ignore"), path.name


def test_the_link_comes_from_the_query_and_only_a_well_formed_one_goes_into_the_app_link():
    out = _node(
        f"""const p = require({json.dumps(str(SCRIPT))});
        console.log(JSON.stringify([
          p.linkOf(''), p.linkOf('?for=pastors-link-key-0123456789'), p.linkOf('?for='), p.linkOf('?for=a%20b'),
          p.linkOf('?for=historians-key-0123456789&fbclid=1'), p.linkOf('?for=../x'), p.linkOf('?utm=1'), p.linkOf('?for=' + 'x'.repeat(65)),
          p.joinUrl('https://app.example/', 'pastors-link-key-0123456789'), p.joinUrl('https://app.example', 'general')
        ]))"""
    )
    assert out == [
        "general", "pastors-link-key-0123456789", None, None, "historians-key-0123456789", None, "general", None,
        "https://app.example/#cic-pilot=pastors-link-key-0123456789", "https://app.example/#cic-pilot=general",
    ]


def test_the_link_travels_in_the_fragment_never_the_query_to_the_app():
    text = SCRIPT.read_text()
    assert "#cic-pilot=" in text
    assert not re.search(r"""\?cic-pilot|[?&]for=["']\s*\+""", text)


def test_the_key_is_taken_out_of_the_address_sent_no_referrer_and_met_by_no_analytics():
    script = SCRIPT.read_text()
    assert "history.replaceState(null, \"\", root.location.pathname)" in script
    assert script.index("replaceState") < script.index("config.pilot") < script.index("pilot-offer")
    html = PAGE.read_text()
    assert '<meta name="referrer" content="no-referrer">' in html
    assert not re.search(r"gtag|analytics|plausible|fathom|googletagmanager|<img[^>]+src=\"https?://", html + script, re.I)
