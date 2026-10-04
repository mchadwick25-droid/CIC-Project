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


def test_each_audience_has_its_end_date_on_the_page_from_the_operations_file():
    ops = load_ops()
    found = dict(re.findall(r'data-pilot-end="([a-z0-9-]+)" hidden>([^<]+)<', PAGE.read_text()))
    assert found == {name: _long_date(a.pilot_end_date) for name, a in ops.pilot_audiences.items()}


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


def test_the_audience_comes_from_the_query_and_only_a_well_formed_name_goes_into_the_app_link():
    out = _node(
        f"""const p = require({json.dumps(str(SCRIPT))});
        console.log(JSON.stringify([
          p.audienceOf(''), p.audienceOf('?for=pastors'), p.audienceOf('?for=Pastors'), p.audienceOf('?for='),
          p.audienceOf('?for=historians&fbclid=1'), p.audienceOf('?for=../x'), p.audienceOf('?utm=1'),
          p.joinUrl('https://app.example/', 'pastors'), p.joinUrl('https://app.example', 'general')
        ]))"""
    )
    assert out == [
        "general", "pastors", None, None, "historians", None, "general",
        "https://app.example/#cic-pilot=pastors", "https://app.example/#cic-pilot=general",
    ]


def test_the_audience_travels_in_the_fragment_never_the_query_to_the_app():
    text = SCRIPT.read_text()
    assert "#cic-pilot=" in text
    assert not re.search(r"""\?cic-pilot|[?&]for=["']\s*\+""", text)
