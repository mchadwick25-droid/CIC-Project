"""The no-spend dev server mounts Go Deeper only when the flag is on, and
keeps the real server's refusals to start."""
import pytest
from fastapi.testclient import TestClient

from engine.api import dev_server
from engine.api.app import MissingAnonCapSecret
from engine.api.deeper_routes import DeeperConfigError

SECRET = "whsec_test_secret"
FREE_KEY = "k" * 40
VISITOR_SECRET = "v" * 40

ENV = {
    "CIC_DEEPER_ENABLED": "1",
    "CIC_DEEPER_WEBHOOK_SECRET": SECRET,
    "CIC_DEEPER_FREE_KEY": FREE_KEY,
    "CIC_API_ANON_CAP_ENABLED": "1",
    "CIC_API_ANON_VISITOR_SECRET": VISITOR_SECRET,
}


@pytest.fixture
def dev_env(monkeypatch, tmp_path):
    monkeypatch.setattr(dev_server, "REPO_ROOT", tmp_path)
    for name in (*ENV, "CIC_DEEPER_METER_DB", "CIC_DEEPER_CLAIMS_DB", "CIC_DEEPER_PRODUCTS", "CIC_DEEPER_OPS_FILE"):
        monkeypatch.delenv(name, raising=False)
    return monkeypatch


def deeper_paths(app):
    return [p for p in (getattr(r, "path", "") for r in app.routes) if p.startswith(("/api/deeper", "/api/admin/deeper"))]


def test_the_module_level_app_builds_with_the_flag_off():
    assert callable(dev_server.app)
    assert dev_server.app.state.deeper is None


def test_flag_off_mounts_no_deeper_route_and_writes_nothing(dev_env, tmp_path):
    app = dev_server.build_dev_app()
    assert app.state.deeper is None
    assert not deeper_paths(app)
    http = TestClient(app)
    assert http.post("/api/deeper/webhook", content=b"{}").status_code == 404
    assert http.get("/api/deeper/balance").status_code == 404
    assert not (tmp_path / dev_server._DEV_DEEPER_DIR).exists()


def test_flag_on_mounts_the_webhook_and_admin_routes(dev_env, tmp_path):
    for name, value in ENV.items():
        dev_env.setenv(name, value)
    app = dev_server.build_dev_app()
    try:
        paths = set(deeper_paths(app))
        assert {
            "/api/deeper/webhook", "/api/deeper/claim", "/api/deeper/balance", "/api/deeper/door",
            "/api/admin/deeper/pause", "/api/admin/deeper/reconciliation", "/api/admin/deeper/funds",
        } <= paths
        assert app.state.deeper.webhook_secret == SECRET
        assert (tmp_path / dev_server._DEV_DEEPER_DIR / "cic_deeper_meter.db").exists()
        assert TestClient(app).post("/api/deeper/webhook", content=b"{}").status_code == 400
    finally:
        app.state.deeper.meter.close()
        app.state.deeper.claims.close()


def test_flag_on_honours_a_named_meter_database(dev_env, tmp_path):
    for name, value in ENV.items():
        dev_env.setenv(name, value)
    dev_env.setenv("CIC_DEEPER_METER_DB", str(tmp_path / "named_meter.db"))
    dev_env.setenv("CIC_DEEPER_CLAIMS_DB", str(tmp_path / "named_claims.db"))
    app = dev_server.build_dev_app()
    try:
        assert (tmp_path / "named_meter.db").exists()
    finally:
        app.state.deeper.meter.close()
        app.state.deeper.claims.close()


@pytest.mark.parametrize("missing", ["CIC_DEEPER_WEBHOOK_SECRET", "CIC_DEEPER_FREE_KEY", "CIC_API_ANON_CAP_ENABLED"])
def test_flag_on_refuses_to_start_without_its_required_settings(dev_env, missing):
    for name, value in ENV.items():
        if name != missing:
            dev_env.setenv(name, value)
    with pytest.raises(DeeperConfigError):
        dev_server.build_dev_app()


def test_flag_on_refuses_to_start_without_the_visitor_secret(dev_env):
    for name, value in ENV.items():
        if name != "CIC_API_ANON_VISITOR_SECRET":
            dev_env.setenv(name, value)
    with pytest.raises(MissingAnonCapSecret):
        dev_server.build_dev_app()
