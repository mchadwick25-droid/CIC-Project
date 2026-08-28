"""The admission gate (stage-10 enforcement; 2026-08-28). The 2026-08-26
audit's headline finding: the running engine never checked registry state -
create_session served any `built` world. The gate exists now, off by
default (today's informed-tester practice as an explicit, declared
deferral), and CIC_ENFORCE_ADMISSION=1 is Mark's doors-open flip. Both
directions are pinned here: enforcement refuses everything in today's
registry (all worlds sit at `built`), refuses nothing once a world's state
is admitted/open, and the default leaves current behavior byte-identical
(every other test in this suite runs with the default and would scream
otherwise)."""
import copy

from engine.api.tests.conftest import FakeBedrockClient, reader_response, safety_response
from engine.api.tests.test_table_api import _http, _table_client
from engine.api.app import create_app
from fastapi.testclient import TestClient


def _enforcing_client(*, store, usage_store, world_loader, registry):
    client = FakeBedrockClient(safety_response=safety_response("NO_SIGNAL"), reader_response=reader_response())
    app = create_app(
        voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m",
        store=store, usage_store=usage_store, world_loader=world_loader, registry=registry,
        default_world_key="fix", enforce_admission=True,
    )
    return TestClient(app)


def test_enforcement_refuses_built_worlds(store, usage_store, world_loader, registry):
    http = _enforcing_client(store=store, usage_store=usage_store, world_loader=world_loader, registry=registry)
    # Interview: every world in today's registry is `built` - refused,
    # including the fixture (which never advances past built by design).
    resp = http.post("/api/session", json={"world_key": "alx"})
    assert resp.status_code == 403
    assert "admission" in resp.json()["detail"]
    assert http.post("/api/session", json={"world_key": "fix"}).status_code == 403
    # Table: one unadmitted seat refuses the whole table.
    assert http.post("/api/session", json={"world_keys": ["alx", "desert"]}).status_code == 403
    # The doorway offers nothing it would refuse at the door.
    assert http.get("/api/worlds").json()["worlds"] == []
    # And nothing was written for any refused create.
    assert store.read_events("") == []


def test_enforcement_admits_admitted_worlds(store, usage_store, world_loader, registry):
    # The same registry with alx and desert advanced to the states the
    # lifecycle defines - the gate opens for exactly them.
    admitted = copy.deepcopy(registry)
    admitted["alx"]["state"] = "admitted"
    admitted["desert"]["state"] = "open"
    http = _enforcing_client(store=store, usage_store=usage_store, world_loader=world_loader, registry=admitted)
    assert http.post("/api/session", json={"world_key": "alx"}).status_code == 201
    assert http.post("/api/session", json={"world_keys": ["alx", "desert"]}).status_code == 201
    # A table seating one admitted and one merely-built world still refuses.
    assert http.post("/api/session", json={"world_keys": ["alx", "pahc"]}).status_code == 403
    listed = {w["world_key"] for w in http.get("/api/worlds").json()["worlds"]}
    assert listed == {"alx", "desert"}


def test_default_leaves_current_practice(store, usage_store, world_loader, registry):
    # enforcement off (the default): built worlds serve, exactly as today -
    # the declared deferral, not a silent gap.
    http = _http(store=store, usage_store=usage_store, world_loader=world_loader, registry=registry,
                 client=_table_client(selector_script=[], stream_scripts=[]))
    assert http.post("/api/session", json={"world_key": "alx"}).status_code == 201
