import pytest
from fastapi.testclient import TestClient

from access_ledger.main import ConfigError, build_app
from access_ledger.packs import PACKS, PRODUCT_NAMES, price_per_conversation_cents

ENV = {
    "STRIPE_SECRET_KEY": "sk_test_x", "STRIPE_WEBHOOK_SECRET": "whsec_x", "ACCESS_DB": "", "ACCESS_INTERNAL_TOKEN": "t",
    "ACCESS_SUCCESS_URL": "https://x/ok", "ACCESS_CANCEL_URL": "https://x/cancel",
}


def test_launch_ladder_is_7_15_30_and_each_rung_lowers_the_price_per_conversation():
    assert [(s.units, s.amount_cents) for s in PACKS.values()] == [(5, 700), (13, 1500), (30, 3000)]
    rates = [price_per_conversation_cents(s) for s in PACKS.values()]
    assert rates == sorted(rates, reverse=True) and len(set(rates)) == 3
    assert [round(r) for r in rates] == [140, 115, 100]


def test_every_pack_has_a_product_name():
    assert set(PACKS) == set(PRODUCT_NAMES)


def test_build_app_serves_the_packs(tmp_path):
    client = TestClient(build_app({**ENV, "ACCESS_DB": str(tmp_path / "a.db")}))
    assert [p["sku"] for p in client.get("/access/packs").json()] == ["pack_5", "pack_13", "pack_30"]


def test_missing_settings_are_named(tmp_path):
    with pytest.raises(ConfigError, match="ACCESS_INTERNAL_TOKEN"):
        build_app({k: v for k, v in ENV.items() if k != "ACCESS_INTERNAL_TOKEN"})


def test_a_live_key_is_refused_without_the_explicit_flag(tmp_path):
    env = {**ENV, "ACCESS_DB": str(tmp_path / "a.db"), "STRIPE_SECRET_KEY": "sk_live_x"}
    with pytest.raises(ConfigError, match="ACCESS_ALLOW_LIVE"):
        build_app(env)
    assert build_app({**env, "ACCESS_ALLOW_LIVE": "1"}) is not None
