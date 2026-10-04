"""The Go Deeper website pages: what a visitor reads, what the purchase click
and the return page send, and what stays unchanged around them."""
import json
import re
import shutil
import subprocess
from html.parser import HTMLParser
from pathlib import Path

import pytest

from engine.api.deeper_ops import load_ops
from engine.m7.turn_readability import score_turn

REPO = Path(__file__).resolve().parents[3]
SITE = REPO / "cic-website"
HARNESS = Path(__file__).with_name("go_deeper_harness.js")
PAGES = ["go-deeper.html", "go-deeper-return.html"]
SUPPORT_LINKS = [
    "https://donate.stripe.com/28E14g3Jp2Vsd1igEl8bS00",
    "https://buy.stripe.com/fZu5kwbbR0NkbXegEl8bS01",
]


class _MainText(HTMLParser):
    def __init__(self):
        super().__init__()
        self.depth = 0
        self.skip = 0
        self.blocks: list[str] = []
        self._buf: list[str] = []

    def handle_starttag(self, tag, attrs):
        if tag == "main":
            self.depth += 1
        if tag in ("script", "style", "noscript"):
            self.skip += 1

    def handle_endtag(self, tag):
        if tag in ("script", "style", "noscript"):
            self.skip -= 1
        if tag == "main":
            self.depth -= 1
        if tag in ("p", "h1", "h2", "li") and self.depth:
            text = " ".join("".join(self._buf).split())
            if text:
                self.blocks.append(text)
            self._buf = []

    def handle_data(self, data):
        if self.depth and not self.skip:
            self._buf.append(data)


def _text_of(html: str) -> list[str]:
    parser = _MainText()
    parser.feed(html)
    return parser.blocks


def _text(page: str) -> list[str]:
    return _text_of((SITE / page).read_text())


def _node(scenario: str):
    node = shutil.which("node")
    assert node, "node is required to run the page script tests"
    out = subprocess.run([node, str(HARNESS), scenario], capture_output=True, text=True, check=True, timeout=60)
    return json.loads(out.stdout)


@pytest.mark.parametrize("page", PAGES)
def test_each_page_reads_at_the_target_level(page):
    text = " ".join(_text(page))
    score = score_turn(text)
    assert score.scored, f"{page} is too short to score"
    assert score.passed, (page, score.failures)


def _without_pack_figures(html: str) -> str:
    return re.sub(r'<li>\$<span data-ops="pack-\d-price">\d+</span>:', "<li>", html)


@pytest.mark.parametrize("page", PAGES)
def test_no_page_shows_a_price_or_money_figure_outside_the_pack_lines(page):
    html = _without_pack_figures((SITE / page).read_text())
    text = " ".join(_text_of(html))
    assert not re.search(r"[$€£]|\b(USD|dollars?|cents?)\b|\d+\s*%", text, re.I), text


def _ops_figures() -> dict:
    ops = load_ops()
    rates = ops.rates
    figures = {"solo-open": rates.solo_open, "solo-round": rates.solo_round, "solo-round-later": rates.solo_round_later}
    for n, pack in enumerate(ops.packs, start=1):
        figures[f"pack-{n}-price"] = pack.price_usd
        figures[f"pack-{n}-tokens"] = pack.tokens
    return figures


NUMBER_WORDS = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten"}


def test_every_figure_on_the_go_deeper_page_is_the_one_in_the_operations_file():
    html = (SITE / "go-deeper.html").read_text()
    found = dict(re.findall(r'data-ops="([a-z0-9-]+)">([\d,]+)<', html))
    expected = {key: f"{value:,}" for key, value in _ops_figures().items()}
    assert found == expected


def test_every_count_of_free_rounds_on_the_page_is_the_operations_files():
    html = (SITE / "go-deeper.html").read_text()
    spoken = re.findall(r'data-ops="free-rounds">([a-z]+)<', html)
    assert len(spoken) == 2
    assert set(spoken) == {NUMBER_WORDS[load_ops().rates.free_rounds]}


def test_the_pack_lines_say_how_many_three_round_conversations_each_pack_holds():
    from engine.deeper import tokens

    ops = load_ops()
    words = {10: "ten", 25: "twenty-five", 60: "sixty"}
    html = (SITE / "go-deeper.html").read_text()
    lines = re.findall(r"<li>\$.*?</li>", html)
    assert len(lines) == len(ops.packs)
    per_conversation = tokens.conversation_cost(ops.rates, ops.rates.free_rounds)
    for line, pack in zip(lines, ops.packs):
        assert words[pack.tokens // per_conversation] in line


def test_nothing_on_the_site_links_to_the_go_deeper_pages_yet():
    for path in SITE.rglob("*.html"):
        if path.name in PAGES:
            continue
        text = path.read_text(errors="ignore")
        assert "go-deeper.html" not in text and "go-deeper-return" not in text, path.name


@pytest.mark.parametrize("page", PAGES)
def test_the_pages_are_kept_out_of_search_until_they_are_live(page):
    assert 'name="robots" content="noindex"' in (SITE / page).read_text()


def test_the_two_contribution_links_are_unchanged():
    html = (SITE / "support.html").read_text()
    hrefs = re.findall(r'href="(https://(?:donate|buy)\.stripe\.com/[^"]+)"', html)
    assert hrefs == SUPPORT_LINKS


def test_the_return_page_never_reads_the_reference_from_the_address():
    for name in ("go-deeper-return.html", "assets/go-deeper.js"):
        text = (SITE / name).read_text()
        assert not re.search(r"location\.(search|hash)|URLSearchParams|document\.referrer", text), name


def test_no_script_puts_a_code_or_reference_in_the_console_or_the_page_address():
    for name in ("go-deeper.html", "go-deeper-return.html", "assets/go-deeper.js"):
        assert "console." not in (SITE / name).read_text(), name


def test_the_buy_button_stays_off_until_a_payment_link_is_set():
    html = (SITE / "go-deeper.html").read_text()
    assert 'var PAYMENT_LINK = "";' in html
    assert re.search(r'id="state-open" hidden', html)


def test_a_reference_is_128_bits_unguessable_and_new_for_each_click():
    out = _node("references")
    assert out == {"distinct": 300, "allValid": True}
    purchase = _node("purchase")
    assert len(purchase["went"]) == 2
    assert purchase["first"]["ref"] != purchase["second"]["ref"]
    for url, held in zip(purchase["went"], (purchase["first"], purchase["second"])):
        assert url == f"https://buy.stripe.test/abc?client_reference_id={held['ref']}"
    assert purchase["withQuery"] == "https://buy.stripe.test/abc?prefilled=1&client_reference_id=XYZ"


def test_a_held_reference_lasts_an_hour_and_a_stale_or_broken_one_is_dropped():
    out = _node("expiry")
    assert out == {"fresh": "keepme", "stale": None, "staleRemoved": True, "broken": None}


def test_the_return_page_waits_for_the_code_and_sends_only_the_reference():
    out = _node("claimReady")
    assert out["result"] == {"status": "ready", "codes": ["ABCD 2345 EFGH 6789 JKLM"], "tokens": 40}
    assert len(out["calls"]) == 3 and len(out["sleeps"]) == 2
    for call in out["calls"]:
        assert call["url"] == "https://api.test/api/deeper/claim"
        assert call["init"]["method"] == "POST"
        assert call["init"]["credentials"] == "omit"
        assert json.loads(call["init"]["body"]) == {"reference": "r" * 22}
    assert out["kept"], "the reference stays so a reload within the hour shows the code again"


def test_the_return_page_gives_up_with_a_missing_state_after_a_bounded_wait():
    limits = _node("limits")
    out = _node("claimMissing")
    assert out["result"] == {"status": "missing"}
    assert len(out["calls"]) == limits["tries"] and len(out["sleeps"]) == limits["tries"] - 1
    assert set(out["sleeps"]) == {limits["poll"]}


def test_a_server_fault_is_an_error_at_once_and_a_dropped_connection_is_retried():
    assert _node("claimServerError")["result"] == {"status": "error"}
    assert len(_node("claimServerError")["calls"]) == 1
    offline = _node("claimOffline")
    assert offline["result"] == {"status": "error"} and len(offline["calls"]) == _node("limits")["tries"]


def test_the_code_is_handed_only_to_the_opening_window_and_only_to_the_app_origin():
    out = _node("handOff")
    assert (out["a"], out["b"], out["c"], out["d"]) == (True, False, False, False)
    assert out["sent"] == [[{"type": "cic-deeper-code", "codes": ["ABCD"]}, "https://app.test"]]


def test_one_code_reaches_the_conversation_without_a_paste_and_a_pack_stays_on_the_page():
    out = _node("deliver")
    assert out["pack"] == "shown"
    assert out["answered"] == "closed"
    assert out["silent"] == out["wrongOrigin"] == out["noOpener"] == "redirected"
    ref = "REF" + "r" * 19
    assert out["log"] == [
        "forget", "close",
        "forget", f"redirect https://app.test/#cic-claim={ref}",
        "forget", f"redirect https://app.test/#cic-claim={ref}",
        "forget", f"redirect https://app.test/#cic-claim={ref}",
    ]


def test_the_address_never_carries_a_code_only_the_reference():
    text = (SITE / "assets/go-deeper.js").read_text()
    assert "cic-code" not in text and "#cic-claim=" in text


def test_the_two_addresses_the_return_page_talks_to_are_written_in_one_file():
    for name in ("go-deeper.html", "go-deeper-return.html", "assets/go-deeper.js"):
        assert "onrender.com" not in (SITE / name).read_text(), name
    assert (SITE / "assets/go-deeper-config.js").read_text().count("onrender.com") == 2


def test_the_return_page_names_the_app_origin_and_no_wildcard():
    text = (SITE / "go-deeper-return.html").read_text()
    assert "appOrigin: APP" in text and "window.GoDeeper.deliver(result.codes" in text
    assert not re.search(r"postMessage\([^)]*['\"]\*['\"]", text + (SITE / "assets/go-deeper.js").read_text())


def test_the_door_line_shows_only_what_the_server_sends():
    out = _node("doorLine")
    assert out["shown"] == {"hidden": False, "text": "Free conversations are limited this week."}
    for quiet in ("open", "unreachable", "refused", "malformed"):
        assert out[quiet] == {"hidden": True, "text": ""}, quiet
    assert out["url"] == "https://api.test/api/deeper/door"
    assert out["init"] == {"credentials": "omit", "referrerPolicy": "no-referrer"}


@pytest.mark.parametrize("page", ["index.html", "support.html"])
def test_the_door_line_sits_on_the_home_and_get_involved_pages_hidden(page):
    html = (SITE / page).read_text()
    assert '<p id="door-line" class="door-line" role="status" hidden></p>' in html
    assert html.index("assets/go-deeper-config.js") < html.index("assets/door-line.js")
