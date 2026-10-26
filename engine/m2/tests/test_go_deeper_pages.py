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


def _node(scenario: str, *args: str):
    node = shutil.which("node")
    assert node, "node is required to run the page script tests"
    out = subprocess.run([node, str(HARNESS), scenario, *args], capture_output=True, text=True, check=True, timeout=60)
    return json.loads(out.stdout)


@pytest.mark.parametrize("page", PAGES)
def test_each_page_reads_at_the_target_level(page):
    text = " ".join(_text(page))
    score = score_turn(text)
    assert score.scored, f"{page} is too short to score"
    assert score.passed, (page, score.failures)


def _without_pack_figures(html: str) -> str:
    return re.sub(r'\$<span data-ops="pack-\d-price">[\d.]+</span>', "<span>", html)


@pytest.mark.parametrize("page", PAGES)
def test_no_page_shows_a_price_or_money_figure_outside_the_pack_lines(page):
    html = _without_pack_figures((SITE / page).read_text())
    text = " ".join(_text_of(html))
    assert not re.search(r"[$€£]|\b(USD|dollars?|cents?)\b|\d+\s*%", text, re.I), text


def _ops_figures() -> dict:
    ops = load_ops()
    rates = ops.rates
    figures = {
        "solo-open": rates.solo_open, "solo-round": rates.solo_round, "solo-round-later": rates.solo_round_later,
        "free-tokens": rates.free_window,
    }
    for n, pack in enumerate(ops.packs, start=1):
        figures[f"pack-{n}-price"] = f"{pack.price_usd}.00"
        figures[f"pack-{n}-tokens"] = pack.tokens
    return figures


NUMBER_WORDS = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten"}


def test_every_figure_on_the_go_deeper_page_is_the_one_in_the_operations_file():
    html = (SITE / "go-deeper.html").read_text()
    found = dict(re.findall(r'data-ops="([a-z0-9-]+)">([\d,.]+)<', html))
    expected = {key: value if isinstance(value, str) else f"{value:,}" for key, value in _ops_figures().items()}
    assert found == expected






def test_the_page_names_no_count_of_conversations_or_rounds_a_free_allowance_buys():
    text = " ".join(_text("go-deeper.html"))
    assert not re.search(r"\babout\b|free conversation lasts|conversations of", text, re.I)
    assert "free-rounds" not in (SITE / "go-deeper.html").read_text()


def test_each_pack_card_shows_its_price_and_tokens_and_a_choose_button():
    ops = load_ops()
    html = (SITE / "go-deeper.html").read_text()
    for n, pack in enumerate(ops.packs, start=1):
        figures = re.search(rf'id="pack-{n}-figures">(.*?)</div>', html, re.S).group(1)
        assert re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", figures)).strip() == f"${pack.price_usd}.00 More conversations: {pack.tokens:,} tokens"
        assert re.search(rf'<button[^>]*id="buy-pack-{n}"[^>]*aria-labelledby="buy-pack-{n} pack-{n}-figures"[^>]*hidden>Choose</button>', html)


def test_the_expiry_and_refund_draft_is_left_off_the_page_until_the_lawyer_clears_it():
    text = " ".join(_text("go-deeper.html"))
    assert not re.search(r"\bexpire|\blapse|\brefund", text, re.I)




def test_only_the_landing_page_links_to_the_go_deeper_pages():
    for path in SITE.rglob("*.html"):
        if path.name in PAGES or path.name == "index.html":
            continue
        text = path.read_text(errors="ignore")
        assert not re.search(r"""href=["'][^"']*go-deeper(?!-config)""", text), path.name


@pytest.mark.parametrize("page", PAGES)
def test_the_pages_are_kept_out_of_search_until_they_are_live(page):
    assert 'name="robots" content="noindex"' in (SITE / page).read_text()


def test_the_two_contribution_links_are_unchanged():
    html = (SITE / "support.html").read_text()
    hrefs = re.findall(r'href="(https://(?:donate|buy)\.stripe\.com/[^"]+)"', html)
    assert hrefs == SUPPORT_LINKS


def test_the_go_deeper_page_offers_the_same_two_gift_links_as_the_support_page():
    html = (SITE / "go-deeper.html").read_text()
    hrefs = re.findall(r'href="(https://(?:donate|buy)\.stripe\.com/[^"]+)"', html)
    assert hrefs == SUPPORT_LINKS


def test_the_return_page_never_reads_the_reference_from_the_address():
    for name in ("go-deeper-return.html", "assets/go-deeper.js"):
        text = (SITE / name).read_text()
        assert not re.search(r"location\.(search|hash)|URLSearchParams|document\.referrer", text), name


def test_no_script_puts_a_code_or_reference_in_the_console_or_the_page_address():
    for name in ("go-deeper.html", "go-deeper-return.html", "assets/go-deeper.js"):
        assert "console." not in (SITE / name).read_text(), name


def test_the_buy_buttons_start_hidden_and_the_page_script_opens_them_for_the_set_links():
    html = (SITE / "go-deeper.html").read_text()
    assert re.search(r'id="state-open" hidden', html)
    for pack in ("1", "2", "3"):
        assert re.search(rf'<button[^>]*id="buy-pack-{pack}"[^>]*hidden>', html), pack


def test_sales_are_suspended_until_accounts_exist_so_no_pack_has_a_link():
    html = (SITE / "go-deeper.html").read_text()
    block = html.split("var PAYMENT_LINKS = ")[1].split("};")[0]
    assert dict(re.findall(r'"(\d)": "([^"]*)"', block)) == {"1": "", "2": "", "3": ""}


def test_the_page_makes_no_promise_about_accounts_until_accounts_exist():
    text = " ".join(_text("go-deeper.html"))
    assert not re.search(r"your home|with an account", text, re.I)


def test_the_page_stays_closed_with_no_link_set():
    out = _node("buyPage", "{}")
    assert out == {"open": False, "closed": True, "shown": [], "went": []}


def test_a_pack_with_an_empty_link_shows_no_button_and_the_page_opens_for_the_others():
    out = _node("buyPage", json.dumps({"2": "https://buy.stripe.test/b", "3": ""}))
    assert out["open"] and not out["closed"]
    assert out["shown"] == ["buy-pack-2"]
    assert out["went"] == ["https://buy.stripe.test/b"]


def test_with_all_three_links_set_three_buttons_show_and_each_opens_its_own_link():
    links = {"1": "https://buy.stripe.test/a", "2": "https://buy.stripe.test/b", "3": "https://buy.stripe.test/c"}
    out = _node("buyPage", json.dumps(links))
    assert out["shown"] == ["buy-pack-1", "buy-pack-2", "buy-pack-3"]
    assert out["went"] == [links["1"], links["2"], links["3"]]


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
        assert "app.churchinconversation.com" not in (SITE / name).read_text(), name
    assert (SITE / "assets/go-deeper-config.js").read_text().count("app.churchinconversation.com") == 2


def test_the_return_page_names_the_app_origin_and_no_wildcard():
    text = (SITE / "go-deeper-return.html").read_text()
    assert "appOrigin: APP" in text and "window.GoDeeper.deliver(result.codes" in text
    assert not re.search(r"postMessage\([^)]*['\"]\*['\"]", text + (SITE / "assets/go-deeper.js").read_text())


def test_the_no_link_rule_catches_a_link_without_the_extension():
    caught = re.compile(r"""href=["'][^"']*go-deeper(?!-config)""")
    for link in ('<a href="/go-deeper">', '<a href="go-deeper.html">', "<a href='go-deeper-return.html'>"):
        assert caught.search(link), link
    assert not caught.search('<script src="assets/go-deeper-config.js"></script>')


def test_the_privacy_page_shows_the_go_deeper_parts_only_when_go_deeper_is_on():
    out = _node("privacy")
    assert out["off"] == {"applied": False, "section": True, "one": False, "two": True}
    assert out["absent"]["applied"] is False and out["notStrictlyTrue"]["applied"] is False
    assert out["on"] == {"applied": True, "section": False, "one": True, "two": False}
    assert out["pageWithoutTheParts"] is False


def test_the_privacy_page_ships_with_the_go_deeper_parts_hidden_and_the_current_text_showing():
    html = (SITE / "privacy.html").read_text()
    assert '<section class="page-section" id="go-deeper" hidden>' in html
    assert '<p id="cookie-two-jobs" hidden>' in html
    assert '<p id="cookie-one-job">' in html
    assert html.index("assets/go-deeper-config.js") < html.index("assets/privacy-go-deeper.js")


def test_the_privacy_page_go_deeper_words_read_at_the_target_level_and_name_no_money_figure():
    html = (SITE / "privacy.html").read_text()
    section = html[html.index('id="go-deeper"'):html.index('id="retention"')]
    text = " ".join(_text_of("<main>" + section + "</main>"))
    assert text, "the section's words were not found"
    assert score_turn(text).passed, score_turn(text).failures
    assert not re.search(r"[$€£]|\d+\s*%", text)
    assert "30 days" in text and "14 more days" in text and "90 days" in text
    assert "we never see your card details" in text and "nothing here is for sale" not in text
    assert "only a count of each answer" in text and "not linked to you or to your code" in text
    assert "network address" in text and "scrambled" in text


def test_the_privacy_page_tells_what_a_purchase_keeps_and_how_long():
    html = (SITE / "privacy.html").read_text()
    section = html[html.index('id="go-deeper"'):html.index('id="retention"')]
    text = " ".join(_text_of("<main>" + section + "</main>"))
    assert "You pay on Stripe's own page" in text
    assert "We keep only the payment's ID and its amount" in text and "never your name or email" in text
    assert "deleted after 90 days" in text
    from engine.deeper.meter import FUNDS_RETENTION_DAYS

    assert FUNDS_RETENTION_DAYS == 90



ACCOUNT_PARTS = ["accounts-optional", "accounts-holds", "accounts-signin", "accounts-back", "accounts-delete",
                 "accounts-review", "accounts-services"]


def test_the_privacy_page_shows_the_account_parts_only_when_accounts_are_on():
    out = _node("privacyAccounts")
    count = len(ACCOUNT_PARTS)
    for name in ("off", "absent", "notStrictlyTrue", "goDeeperAloneDoesNotShowThem"):
        assert out[name] == {"applied": False, "hidden": count}, name
    assert out["on"] == {"applied": True, "hidden": 0}
    assert out["onWithGoDeeperOff"] == {"applied": True, "hidden": 0}
    assert out["pageWithoutTheParts"] is False


def test_the_privacy_page_ships_with_every_account_part_hidden_and_the_switch_off():
    html = (SITE / "privacy.html").read_text()
    for part in ACCOUNT_PARTS:
        assert re.search(rf'<(section|p)[^>]*id="{part}"[^>]*\bhidden\b', html), part
    assert "accounts: false" in (SITE / "assets" / "go-deeper-config.js").read_text()


def test_the_privacy_page_account_words_read_at_the_target_level_and_say_what_was_approved():
    html = (SITE / "privacy.html").read_text()
    section = html[html.index('id="accounts-optional"'):html.index('id="retention"')]
    text = " ".join(_text_of("<main>" + section.replace(" hidden", "") + "</main>"))
    assert text
    assert score_turn(text).passed, score_turn(text).failures
    for sentence in (
        "We keep no name.",
        "Stripe knows who paid. What you say in a conversation is never stored with your payment.",
        "Nothing about you is carried from one conversation to the next.",
        "If you lose both your email and your recovery code, we cannot get your account back.",
        "Backups drop deleted data within 14 days.",
        "If someone gives us an email address, we can check whether it has an account.",
    ):
        assert sentence in text, sentence
    assert "can't be traced back" not in html and "cannot be linked" not in html


def test_the_privacy_page_numbers_match_the_meters_own_retention():
    from engine.api import db_backup
    from engine.deeper import meter

    html = (SITE / "privacy.html").read_text()
    section = html[html.index('id="go-deeper"'):html.index('id="retention"')]
    assert f"We delete this record {load_ops().rates.free_window_days} days after that first day." in section
    assert f"we delete it {meter.RETENTION_DAYS} days after the end of the week it was last used." in section
    assert f"We delete it {meter.PILOT_RETENTION_DAYS} days after that day." in section
    assert f"{db_backup._DEFAULT_RETENTION_DAYS} more days" in section


def test_the_landing_page_offers_get_more_conversations_in_the_top_row_and_loads_nothing_until_it_is_pressed():
    html = (SITE / "index.html").read_text()
    button = re.search(r'<button[^>]*id="more-toggle"[^>]*>(.*?)</button>', html, re.S)
    assert button and "hidden" in button.group(0) and button.group(1).strip() == "Get more conversations"
    frame = re.search(r'<iframe[^>]*id="more-frame"[^>]*>', html).group(0)
    assert "src=" not in frame
    assert html.index("assets/go-deeper-config.js") < html.index("assets/more-conversations.js")


def test_the_slide_out_hears_only_the_app_frame_at_the_app_origin():
    js = (SITE / "assets" / "more-conversations.js").read_text()
    assert "ev.origin !== appOrigin" in js and "ev.source !== frame.contentWindow" in js
    assert 'postMessage({ type: "cic:panel-open" }, appOrigin)' in js


def test_the_landing_page_drawer_is_on_and_its_script_obeys_the_switch():
    config = (SITE / "assets" / "go-deeper-config.js").read_text()
    assert re.search(r"\bdrawer:\s*true\b", config)
    assert "cfg.drawer" in (SITE / "assets" / "more-conversations.js").read_text()


def test_the_app_panel_offers_the_same_two_gift_links_as_the_support_page():
    ts = (REPO / "cic-poc" / "frontend" / "src" / "lib" / "giftLinks.ts").read_text()
    assert re.findall(r"'(https://(?:donate|buy)\.stripe\.com/[^']+)'", ts) == SUPPORT_LINKS
