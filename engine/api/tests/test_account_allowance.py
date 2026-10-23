"""A2: the account's monthly allowance and the codes it holds, at the admission seam."""
from datetime import date, timedelta

import pytest
from fastapi.testclient import TestClient

from engine.accounts.keys import KeyRing
from engine.accounts.service import AccountsService
from engine.accounts.store import AccountStore
from engine.accounts.tests.conftest import ADDRESS_KEY, SESSION_KEY, Clock, FakeMailer
from engine.api.accounts_routes import AccountsRuntime
from engine.api.app import create_app
from engine.api.deeper_ops import load_ops
from engine.api.deeper_routes import DeeperRuntime
from engine.api.tests.test_deeper_seam import ACUTE, FREE_CAP, RecordingClient, code_with, open_session, say, solo_charge
from engine.deeper import codes
from engine.deeper.claims import ClaimStore
from engine.deeper.meter import Meter

H = {"x-cic-accounts": "1"}
ADDR = "ada@example.org"


@pytest.fixture(autouse=True)
def small_free_cap(monkeypatch):
    monkeypatch.setattr("engine.m4.turn.SESSION_TURN_CAP", FREE_CAP)
    monkeypatch.setattr("engine.m4.round.TABLE_SESSION_ROUND_CAP", 1)


@pytest.fixture
def runtime(tmp_path):
    rt = DeeperRuntime(
        meter=Meter(str(tmp_path / "m.db"), clock=lambda: date(2026, 10, 5)),
        claims=ClaimStore(str(tmp_path / "c.db")),
        webhook_secret="whsec_x", products={}, miss_delay_seconds=0.0, ops=load_ops(),
    )
    yield rt
    rt.meter.close()
    rt.claims.close()


@pytest.fixture
def mailer():
    return FakeMailer()


@pytest.fixture
def accounts(tmp_path, mailer):
    store = AccountStore(str(tmp_path / "d.db"), str(tmp_path / "e.db"))
    service = AccountsService(store, KeyRing(ADDRESS_KEY, SESSION_KEY), mailer, clock=Clock())
    yield AccountsRuntime(service=service, miss_delay_seconds=0.0, start_floor_seconds=0.0)
    store.close()


def app_for(store, usage_store, world_loader, registry, runtime, accounts, client):
    app = create_app(
        voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m",
        store=store, usage_store=usage_store, world_loader=world_loader, registry=registry,
        default_world_key="fix", deeper=runtime, accounts=accounts, rate_limit=False,
        anon_cap_enabled=True, anon_visitor_secret="s" * 32,
    )
    return TestClient(app, base_url="https://testserver")


def sign_in(http, mailer, address=ADDR):
    started = http.post("/api/accounts/sign-in/start", json={"address": address}, headers=H)
    done = http.post(
        "/api/accounts/sign-in/finish",
        json={"challenge": started.json()["challenge"], "address": address, "code": mailer.last_code(address), "over_18": True},
        headers=H,
    )
    assert done.status_code == 200 and done.json()["status"] == "ok", done.text
    return done


def me_account(accounts, http):
    return accounts.service.admission_context(http.cookies.get(accounts.cookie_name))


@pytest.fixture
def setup(store, usage_store, world_loader, registry, runtime, accounts, mailer):
    client = RecordingClient()
    http = app_for(store, usage_store, world_loader, registry, runtime, accounts, client)
    return http, client


def test_a_signed_in_person_draws_the_account_window_and_leaves_the_browser_window_alone(setup, runtime, accounts, mailer):
    http, client = setup
    sign_in(http, mailer)
    context = me_account(accounts, http)
    session_id, auth = open_session(http)
    reply = say(http, session_id, auth, "hello")
    assert reply.json()["voice"] is not None
    spent = solo_charge(runtime, 1)
    assert runtime.free.account_left(context["account_id"], context["refill_day"]) == runtime.free.window_amount - spent
    assert reply.headers["x-cic-free-left"] == str(runtime.free.window_amount - spent)
    assert runtime.meter.free_window_spent(runtime.meter.free_key("ip:testclient")) == 0


def test_a_new_account_starts_with_what_is_left_of_its_browser_window(setup, runtime, accounts, mailer):
    http, client = setup
    say(http, *open_session(http), "hello")
    drawn = solo_charge(runtime, 1)
    visitor = http.cookies.get("cic_visitor").split(".")[0]
    assert runtime.meter.free_window_spent(runtime.meter.free_key(visitor)) == drawn
    sign_in(http, mailer)
    context = me_account(accounts, http)
    assert runtime.free.account_left(context["account_id"], context["refill_day"]) == runtime.free.window_amount - drawn
    other = TestClient(http.app, base_url="https://testserver")  # a browser that never drew: a full window
    sign_in(other, mailer, "bob@example.org")
    fresh = me_account(accounts, other)
    assert runtime.free.account_left(fresh["account_id"], fresh["refill_day"]) == runtime.free.window_amount


def test_the_allowance_refills_on_the_account_s_own_day_and_never_accumulates(setup, runtime, accounts, mailer):
    http, client = setup
    sign_in(http, mailer)
    context = me_account(accounts, http)
    day, who, full = context["refill_day"], context["account_id"], runtime.free.window_amount
    start = runtime.meter.account_window_start(day)
    following = (start.replace(day=1) + timedelta(days=32)).replace(day=day)
    runtime.free.settle(runtime.free.account_reserve(who, day, 100), True)
    assert runtime.free.account_left(who, day) == full - 100
    runtime.meter._clock = lambda: following - timedelta(days=1)
    assert runtime.free.account_left(who, day) == full - 100  # the day has not come
    runtime.meter._clock = lambda: following
    assert runtime.free.account_left(who, day) == full  # refilled to the same 550, nothing carried
    runtime.free.settle(runtime.free.account_reserve(who, day, 50), True)
    runtime.meter._clock = lambda: (following.replace(day=1) + timedelta(days=32)).replace(day=day)
    assert runtime.free.account_left(who, day) == full


@pytest.mark.parametrize("today, day, start", [
    (date(2026, 3, 31), 28, date(2026, 3, 28)), (date(2026, 3, 5), 28, date(2026, 2, 28)),
    (date(2026, 1, 1), 15, date(2025, 12, 15)), (date(2026, 2, 28), 28, date(2026, 2, 28)),
])
def test_the_window_starts_on_the_most_recent_refill_day_across_month_ends(runtime, today, day, start):
    runtime.meter._clock = lambda: today
    assert runtime.meter.account_window_start(day) == start


def test_many_accounts_behind_one_network_share_the_network_window(runtime):
    free = runtime.free
    network = "net-1"
    drawn = 0
    for i in range(40):
        held = free.account_reserve(f"acct-{i}", 5, 100, 1.0, network)
        if held is None:
            break
        free.settle(held, True)
        drawn += 100
    assert drawn == free.network_window_amount - free.network_window_amount % 100
    assert free.account_reserve("acct-fresh", 5, 100, 1.0, network) is None
    assert free.account_reserve("acct-fresh", 5, 100, 1.0, "other-net") is not None


def test_the_allowance_row_and_the_meter_file_hold_no_raw_account_id(setup, runtime, accounts, mailer, tmp_path):
    http, client = setup
    sign_in(http, mailer)
    context = me_account(accounts, http)
    say(http, *open_session(http), "hello")
    runtime.meter._conn.execute("PRAGMA wal_checkpoint(TRUNCATE)")
    path = tmp_path / "m.db"
    data = path.read_bytes() + (tmp_path / "m.db-wal").read_bytes() if (tmp_path / "m.db-wal").exists() else path.read_bytes()
    assert context["account_id"].encode() not in data
    assert runtime.free.account_key(context["account_id"]).encode() in data


def attach(http, code):
    return http.post("/api/accounts/codes/attach", json={"code": codes.display(code)}, headers=H)


def test_a_code_the_account_holds_pays_past_the_free_window_and_is_summed_in_the_balance(setup, runtime, accounts, mailer):
    http, client = setup
    sign_in(http, mailer)
    context = me_account(accounts, http)
    code = code_with(runtime, 5000)
    assert attach(http, code).status_code == 200
    runtime.free.settle(runtime.free.account_reserve(context["account_id"], context["refill_day"],
                                                     runtime.free.account_left(context["account_id"], context["refill_day"])), True)
    balance = http.get("/api/accounts/balance").json()
    assert balance["free_left"] == 0 and balance["code_tokens"] == 5000 and balance["codes_held"] == 1
    session_id, auth = open_session(http)
    replies = [say(http, session_id, auth, f"q{i}") for i in range(FREE_CAP + 1)]
    assert replies[0].json()["voice"] is not None
    assert replies[0].headers["x-cic-remaining"] == str(5000 - solo_charge(runtime, 1))
    assert http.get("/api/accounts/balance").json()["code_tokens"] < 5000


def test_free_is_drawn_before_any_code(setup, runtime, accounts, mailer):
    http, client = setup
    sign_in(http, mailer)
    code = code_with(runtime, 5000)
    attach(http, code)
    session_id, auth = open_session(http)
    say(http, session_id, auth, "hello")
    assert runtime.meter.status(code).remaining == 5000


def test_the_same_code_attached_twice_counts_once_and_another_account_is_refused(setup, runtime, accounts, mailer, tmp_path):
    http, client = setup
    sign_in(http, mailer)
    code = code_with(runtime, 100)
    assert attach(http, code).status_code == 200 and attach(http, code).status_code == 200
    assert http.get("/api/accounts/balance").json()["codes_held"] == 1
    other = TestClient(http.app, base_url="https://testserver")
    sign_in(other, mailer, "bob@example.org")
    refused = attach(other, code)
    assert refused.status_code == 400 and "another account" in refused.json()["detail"]
    assert other.get("/api/accounts/balance").json()["codes_held"] == 0


def test_a_made_up_or_void_code_cannot_be_attached(setup, runtime, accounts, mailer):
    http, client = setup
    sign_in(http, mailer)
    assert attach(http, codes.generate()).status_code == 400
    code = code_with(runtime, 100)
    runtime.meter.void(runtime.meter._conn.execute("SELECT payment_id FROM meter").fetchone()[0])
    assert attach(http, code).status_code == 400
    assert http.post("/api/accounts/codes/attach", json={"code": "nonsense"}, headers=H).status_code == 400


def test_the_account_file_holds_a_scramble_of_the_code_hash_never_the_hash(setup, runtime, accounts, mailer, tmp_path):
    http, client = setup
    sign_in(http, mailer)
    code = code_with(runtime, 100)
    attach(http, code)
    for name in ("d.db", "e.db"):
        assert codes.hash_code(code).encode() not in (tmp_path / name).read_bytes()
        assert code.encode() not in (tmp_path / name).read_bytes()
    stored = accounts.service.store._d.execute("SELECT scramble FROM account_codes").fetchone()[0]
    assert stored == accounts.service.keys.secret_hash("code", codes.hash_code(code))


def test_signed_out_a_code_on_the_request_still_pays_as_before(setup, runtime):
    http, client = setup
    code = code_with(runtime, solo_charge(runtime, FREE_CAP + 1))
    session_id, auth = open_session(http, **{"X-Cic-Code": code})
    replies = [say(http, session_id, auth, f"q{i}") for i in range(FREE_CAP + 1)]
    assert replies[-1].json()["voice"] is not None


def test_a_signed_in_sitting_builds_the_same_voice_request_as_an_anonymous_one(store, usage_store, world_loader, registry, runtime, accounts, mailer):
    anon_client, signed_client = RecordingClient(), RecordingClient()
    anon = app_for(store, usage_store, world_loader, registry, runtime, accounts, anon_client)
    say(anon, *open_session(anon), "same words")
    signed = app_for(store, usage_store, world_loader, registry, runtime, accounts, signed_client)
    sign_in(signed, mailer)
    say(signed, *open_session(signed), "same words")
    assert anon_client.voice_requests and anon_client.voice_requests == signed_client.voice_requests


def test_a_safety_turn_is_answered_for_a_signed_in_person_and_draws_nothing(store, usage_store, world_loader, registry, runtime, accounts, mailer):
    client = RecordingClient(safety=ACUTE)
    http = app_for(store, usage_store, world_loader, registry, runtime, accounts, client)
    sign_in(http, mailer)
    context = me_account(accounts, http)
    reply = say(http, *open_session(http), "I do not know how to say this")
    body = reply.json()
    assert body["routing_action"] == "safety_turn" and body["voice"] is None and body["facilitator"]["resources_appended"]
    assert runtime.free.account_left(context["account_id"], context["refill_day"]) == runtime.free.window_amount


def test_a_signed_in_person_with_nothing_left_gets_the_pause_and_the_safety_check(setup, runtime, accounts, mailer):
    http, client = setup
    sign_in(http, mailer)
    context = me_account(accounts, http)
    runtime.free.settle(runtime.free.account_reserve(
        context["account_id"], context["refill_day"], runtime.free.account_left(context["account_id"], context["refill_day"])), True)
    before = len(client.voice_requests)
    reply = say(http, *open_session(http), "hello")
    assert reply.json()["routing_action"] == "session_cap_turn" and len(client.voice_requests) == before


def test_deleting_the_account_removes_its_code_links_and_leaves_the_code_in_the_meter(setup, runtime, accounts, mailer):
    http, client = setup
    sign_in(http, mailer)
    code = code_with(runtime, 100)
    attach(http, code)
    session = accounts.service.session(http.cookies.get(accounts.cookie_name))
    accounts.service.store.step_up_session(session.token_hash, accounts.service.now() + 600)
    assert http.post("/api/accounts/delete", json={}, headers=H).status_code == 200
    assert accounts.service.store._d.execute("SELECT COUNT(*) FROM account_codes").fetchone()[0] == 0
    assert runtime.meter.status(code).remaining == 100


def test_an_account_fault_at_admission_leaves_the_free_grant(setup, runtime, accounts, mailer, monkeypatch):
    http, client = setup
    sign_in(http, mailer)

    def broken(*a, **k):
        raise RuntimeError("accounts unavailable")

    monkeypatch.setattr(accounts.service, "admission_context", broken)
    reply = say(http, *open_session(http), "hello")
    assert reply.json()["voice"] is not None


def test_signing_in_reads_the_visitor_cookie_and_mints_none(setup, mailer):
    http, client = setup
    done = sign_in(http, mailer)
    assert "cic_visitor" not in done.headers.get("set-cookie", "") and http.cookies.get("cic_visitor") is None
