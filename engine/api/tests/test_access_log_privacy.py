"""No log line joins a client IP to a session (System Hub decisions 19 and 26)."""
import logging
import re
from pathlib import Path

from engine.api.tests.test_app import _client

DOCKERFILE = Path(__file__).resolve().parents[2] / "Dockerfile"
IP = re.compile(r"\b\d{1,3}(?:\.\d{1,3}){3}\b")


def test_the_container_runs_uvicorn_without_its_access_log():
    cmd = next(line for line in DOCKERFILE.read_text().splitlines() if line.startswith("CMD"))
    assert "uvicorn" in cmd and "--no-access-log" in cmd


def test_the_apps_own_request_logs_carry_no_client_ip(store, usage_store, world_loader, registry, caplog):
    http = _client(store=store, usage_store=usage_store, world_loader=world_loader, registry=registry)
    with caplog.at_level(logging.INFO, logger="cic.api"):
        created = http.post("/api/session", json={"world_key": "fix"}, headers={"X-Forwarded-For": "203.0.113.7"}).json()
        http.post(f"/api/session/{created['session_id']}/message", headers={
            "Authorization": f"Session {created['session_code']}", "X-Forwarded-For": "203.0.113.7"}, json={"text": "who was Jesus"})
    lines = [r.getMessage() for r in caplog.records]
    assert any(created["session_id"] in line for line in lines)
    assert not any(IP.search(line) for line in lines if created["session_id"] in line)
