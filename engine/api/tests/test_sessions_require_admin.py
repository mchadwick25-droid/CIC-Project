"""sessions_require_admin: with it on, only the operator can open a
conversation; with it off, opening one is unchanged."""
import pytest
from fastapi.testclient import TestClient

from engine.api import admin_auth
from engine.api.app import MissingAdminTokenForSessions, create_app
from engine.api.tests.test_table_api import _table_client

ADMIN_TOKEN = "the-real-token-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
GOOD_PASSWORD = "MyPassword123!"


def _http(store, usage_store, world_loader, registry, tmp_path, *, require_admin, admin_token=ADMIN_TOKEN):
    client = _table_client(selector_script=[], stream_scripts=[])
    app = create_app(
        voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m",
        store=store, usage_store=usage_store, world_loader=world_loader, registry=registry,
        default_world_key="fix", admin_token=admin_token, sessions_require_admin=require_admin,
        admin_auth_store=admin_auth.AdminAuthStore(tmp_path / "admin_auth.json") if admin_token else None,
    )
    return TestClient(app, base_url="https://testserver")


def test_a_visitor_without_the_login_cannot_open_a_conversation(store, usage_store, world_loader, registry, tmp_path):
    http = _http(store, usage_store, world_loader, registry, tmp_path, require_admin=True)
    for headers in ({}, {"Authorization": "Bearer wrong"}):
        resp = http.post("/api/session", json={"world_key": "fix"}, headers=headers)
        assert resp.status_code == 403
        assert "Log in" in resp.json()["detail"]
    assert http.post("/api/session", json={"world_keys": ["fix", "fix2"]}).status_code == 403


def test_the_admin_token_opens_a_conversation(store, usage_store, world_loader, registry, tmp_path):
    http = _http(store, usage_store, world_loader, registry, tmp_path, require_admin=True)
    resp = http.post("/api/session", json={"world_key": "fix"}, headers={"Authorization": f"Bearer {ADMIN_TOKEN}"})
    assert resp.status_code == 201


def test_the_dashboard_login_cookie_opens_a_conversation(store, usage_store, world_loader, registry, tmp_path):
    http = _http(store, usage_store, world_loader, registry, tmp_path, require_admin=True)
    http.post("/api/admin/set-password", json={"password": GOOD_PASSWORD}, headers={"Authorization": f"Bearer {ADMIN_TOKEN}"})
    assert http.post("/api/admin/login", json={"password": GOOD_PASSWORD}).status_code == 200
    assert http.post("/api/session", json={"world_key": "fix"}).status_code == 201


def test_after_logout_the_cookie_no_longer_opens_a_conversation(store, usage_store, world_loader, registry, tmp_path):
    http = _http(store, usage_store, world_loader, registry, tmp_path, require_admin=True)
    http.post("/api/admin/set-password", json={"password": GOOD_PASSWORD}, headers={"Authorization": f"Bearer {ADMIN_TOKEN}"})
    http.post("/api/admin/login", json={"password": GOOD_PASSWORD})
    http.post("/api/admin/logout")
    assert http.post("/api/session", json={"world_key": "fix"}).status_code == 403


def test_the_login_cookie_is_scoped_to_the_api(store, usage_store, world_loader, registry, tmp_path):
    http = _http(store, usage_store, world_loader, registry, tmp_path, require_admin=True)
    http.post("/api/admin/set-password", json={"password": GOOD_PASSWORD}, headers={"Authorization": f"Bearer {ADMIN_TOKEN}"})
    login = http.post("/api/admin/login", json={"password": GOOD_PASSWORD})
    assert "Path=/api;" in login.headers["set-cookie"] or login.headers["set-cookie"].endswith("Path=/api")


def test_logout_clears_a_cookie_issued_under_the_former_path(store, usage_store, world_loader, registry, tmp_path):
    http = _http(store, usage_store, world_loader, registry, tmp_path, require_admin=True)
    cleared = http.post("/api/admin/logout").headers.get_list("set-cookie")
    paths = {part.strip() for header in cleared for part in header.split(";") if part.strip().startswith("Path=")}
    assert paths == {f"Path={admin_auth.SESSION_COOKIE_PATH}", f"Path={admin_auth.FORMER_SESSION_COOKIE_PATH}"}


def test_without_the_setting_anyone_can_open_a_conversation(store, usage_store, world_loader, registry, tmp_path):
    http = _http(store, usage_store, world_loader, registry, tmp_path, require_admin=False)
    assert http.post("/api/session", json={"world_key": "fix"}).status_code == 201


def test_the_setting_without_an_admin_token_is_refused_at_construction(store, usage_store, world_loader, registry, tmp_path):
    with pytest.raises(MissingAdminTokenForSessions):
        _http(store, usage_store, world_loader, registry, tmp_path, require_admin=True, admin_token=None)
