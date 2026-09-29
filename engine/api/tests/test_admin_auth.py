"""engine.api.admin_auth: the dashboard's password login (Mark,
2026-09-28 - "every website no matter how sensitive is just password
protected"). Two layers tested separately: the pure hashing/policy/
session-token functions here, and the wired-up endpoints (set-password,
login, logout, auth-status, and the dual token-or-session auth on
pilot-summary/usage-summary) in test_admin.py-style fashion below."""
import time
import uuid

import pytest
from fastapi.testclient import TestClient

from engine.api import admin_auth
from engine.api.app import create_app
from engine.api.tests.test_table_api import _table_client

GOOD_PASSWORD = "MyPassword123!"  # 14 chars, upper+digit+symbol - clears the policy


def test_valid_password_passes_policy():
    admin_auth.validate_password_policy(GOOD_PASSWORD)  # does not raise


@pytest.mark.parametrize("password,missing", [
    ("Short1!", "12-20 characters"),
    ("thisisaverylongpassword12345!", "12-20 characters"),
    ("nocapitalhere123!", "uppercase"),
    ("NoDigitHere!!!!", "number"),
    ("NoSymbolHere1234", "symbol"),
])
def test_password_policy_rejects_each_missing_requirement(password, missing):
    with pytest.raises(admin_auth.PasswordPolicyError, match=missing):
        admin_auth.validate_password_policy(password)


def test_hash_then_verify_round_trips():
    hashed = admin_auth.hash_password(GOOD_PASSWORD)
    assert admin_auth.verify_password(GOOD_PASSWORD, hashed)


def test_wrong_password_fails_verification():
    hashed = admin_auth.hash_password(GOOD_PASSWORD)
    assert not admin_auth.verify_password("WrongPassword1!", hashed)


def test_two_hashes_of_the_same_password_differ():
    """Random salt per hash_password call - two operators choosing the
    same password must not produce identical stored hashes."""
    assert admin_auth.hash_password(GOOD_PASSWORD) != admin_auth.hash_password(GOOD_PASSWORD)


def test_malformed_stored_hash_fails_closed_not_raises():
    assert admin_auth.verify_password(GOOD_PASSWORD, "not-a-real-hash") is False
    assert admin_auth.verify_password(GOOD_PASSWORD, "") is False


def test_session_token_round_trips_with_the_right_secret():
    token = admin_auth.issue_session_token("s3cret")
    assert admin_auth.verify_session_token(token, "s3cret")


def test_session_token_rejected_with_wrong_secret():
    token = admin_auth.issue_session_token("s3cret")
    assert not admin_auth.verify_session_token(token, "different")


def test_session_token_rejected_once_expired():
    token = admin_auth.issue_session_token("s3cret", ttl_seconds=-1)
    assert not admin_auth.verify_session_token(token, "s3cret")


def test_malformed_or_missing_session_token_fails_closed():
    assert admin_auth.verify_session_token(None, "s3cret") is False
    assert admin_auth.verify_session_token("", "s3cret") is False
    assert admin_auth.verify_session_token("garbage", "s3cret") is False


def test_auth_store_round_trips_through_disk(tmp_path):
    store = admin_auth.AdminAuthStore(tmp_path / "admin_auth.json")
    assert store.read_password_hash() is None
    store.write_password_hash("pbkdf2_sha256$1$aa$bb")
    assert store.read_password_hash() == "pbkdf2_sha256$1$aa$bb"


def test_auth_store_missing_file_reads_as_none(tmp_path):
    store = admin_auth.AdminAuthStore(tmp_path / "does-not-exist" / "admin_auth.json")
    assert store.read_password_hash() is None


ADMIN_TOKEN = "the-real-token-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"


def _app_with_auth(store, usage_store, world_loader, registry, tmp_path, client=None):
    client = client or _table_client(selector_script=[], stream_scripts=[])
    auth_store = admin_auth.AdminAuthStore(tmp_path / "admin_auth.json")
    app = create_app(
        voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m",
        store=store, usage_store=usage_store, world_loader=world_loader, registry=registry,
        default_world_key="fix", admin_token=ADMIN_TOKEN, admin_auth_store=auth_store,
    )
    return TestClient(app, base_url="https://testserver")


def test_auth_status_before_and_after_setup(store, usage_store, world_loader, registry, tmp_path):
    http = _app_with_auth(store, usage_store, world_loader, registry, tmp_path)
    assert http.get("/api/admin/auth-status").json() == {"password_set": False}
    http.post("/api/admin/set-password", json={"password": GOOD_PASSWORD}, headers={"Authorization": f"Bearer {ADMIN_TOKEN}"})
    assert http.get("/api/admin/auth-status").json() == {"password_set": True}


def test_auth_status_404s_when_admin_token_unconfigured(store, usage_store, world_loader, registry):
    client = _table_client(selector_script=[], stream_scripts=[])
    app = create_app(
        voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m",
        store=store, usage_store=usage_store, world_loader=world_loader, registry=registry, default_world_key="fix",
    )
    assert TestClient(app).get("/api/admin/auth-status").status_code == 404


def test_set_password_requires_the_real_admin_token(store, usage_store, world_loader, registry, tmp_path):
    http = _app_with_auth(store, usage_store, world_loader, registry, tmp_path)
    resp = http.post("/api/admin/set-password", json={"password": GOOD_PASSWORD}, headers={"Authorization": "Bearer wrong"})
    assert resp.status_code == 404
    assert http.get("/api/admin/auth-status").json() == {"password_set": False}


def test_set_password_rejects_a_policy_violating_password(store, usage_store, world_loader, registry, tmp_path):
    http = _app_with_auth(store, usage_store, world_loader, registry, tmp_path)
    resp = http.post("/api/admin/set-password", json={"password": "short1!"}, headers={"Authorization": f"Bearer {ADMIN_TOKEN}"})
    assert resp.status_code == 400
    assert "12-20" in resp.json()["detail"]


def test_login_then_reach_usage_summary_via_session_cookie(store, usage_store, world_loader, registry, tmp_path):
    http = _app_with_auth(store, usage_store, world_loader, registry, tmp_path)
    http.post("/api/admin/set-password", json={"password": GOOD_PASSWORD}, headers={"Authorization": f"Bearer {ADMIN_TOKEN}"})
    login = http.post("/api/admin/login", json={"password": GOOD_PASSWORD})
    assert login.status_code == 200
    assert admin_auth.SESSION_COOKIE_NAME in login.cookies
    # No Authorization header at all - the session cookie alone must carry it.
    assert http.get("/api/admin/usage-summary").status_code == 200
    assert http.get("/api/admin/pilot-summary").status_code == 200


def test_login_with_wrong_password_is_401_and_sets_no_cookie(store, usage_store, world_loader, registry, tmp_path):
    http = _app_with_auth(store, usage_store, world_loader, registry, tmp_path)
    http.post("/api/admin/set-password", json={"password": GOOD_PASSWORD}, headers={"Authorization": f"Bearer {ADMIN_TOKEN}"})
    resp = http.post("/api/admin/login", json={"password": "WrongPassword1!"})
    assert resp.status_code == 401
    assert admin_auth.SESSION_COOKIE_NAME not in resp.cookies


def test_login_before_any_password_is_set_is_401_not_500(store, usage_store, world_loader, registry, tmp_path):
    http = _app_with_auth(store, usage_store, world_loader, registry, tmp_path)
    assert http.post("/api/admin/login", json={"password": GOOD_PASSWORD}).status_code == 401


def test_logout_invalidates_the_session(store, usage_store, world_loader, registry, tmp_path):
    http = _app_with_auth(store, usage_store, world_loader, registry, tmp_path)
    http.post("/api/admin/set-password", json={"password": GOOD_PASSWORD}, headers={"Authorization": f"Bearer {ADMIN_TOKEN}"})
    http.post("/api/admin/login", json={"password": GOOD_PASSWORD})
    assert http.get("/api/admin/usage-summary").status_code == 200
    http.post("/api/admin/logout")
    assert http.get("/api/admin/usage-summary").status_code == 404


def test_original_bearer_token_still_works_after_a_password_is_set(store, usage_store, world_loader, registry, tmp_path):
    """Backward compatibility: a script calling pilot-summary directly
    with the raw admin token must be unaffected by the password feature
    existing at all."""
    http = _app_with_auth(store, usage_store, world_loader, registry, tmp_path)
    http.post("/api/admin/set-password", json={"password": GOOD_PASSWORD}, headers={"Authorization": f"Bearer {ADMIN_TOKEN}"})
    resp = http.get("/api/admin/usage-summary", headers={"Authorization": f"Bearer {ADMIN_TOKEN}"})
    assert resp.status_code == 200


def test_forged_session_cookie_is_rejected(store, usage_store, world_loader, registry, tmp_path):
    http = _app_with_auth(store, usage_store, world_loader, registry, tmp_path)
    http.cookies.set(admin_auth.SESSION_COOKIE_NAME, "9999999999.deadbeef")
    assert http.get("/api/admin/usage-summary").status_code == 404


def test_login_attempts_are_locked_out_after_five_per_15_minutes(store, usage_store, world_loader, registry, tmp_path):
    client = _table_client(selector_script=[], stream_scripts=[])
    auth_store = admin_auth.AdminAuthStore(tmp_path / "admin_auth.json")
    app = create_app(
        voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m",
        store=store, usage_store=usage_store, world_loader=world_loader, registry=registry,
        default_world_key="fix", admin_token=ADMIN_TOKEN, admin_auth_store=auth_store, rate_limit=True,
    )
    http = TestClient(app, base_url="https://testserver")
    codes = [http.post("/api/admin/login", json={"password": "WrongPassword1!"}).status_code for _ in range(7)]
    assert codes[:5] == [401] * 5
    assert codes[5:] == [429, 429]
