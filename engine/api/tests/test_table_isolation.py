"""THE ISOLATION PROPERTY (Artifact-7 SS3; Constitution V2.2 Art. 3;
Table Design V2.3 SS6): no voice at a table may ground a claim in another
world's records - the only cross-world channel is what was SAID at the
Table. This suite is the CI gate Artifact-7 SS8 item 1 names:

  (a) an assertion sweep over a multi-turn table round - every surviving
      citation of every turn resolves within the speaker's own repository;
  (b) the seeded leak - a record id from seated world B planted in world
      A's raw output must be withheld by A's net as an unresolvable tag,
      visible in the turn's own grounding result;
  (c) the runtime scope check - every voice turn is constructed from
      exactly one LoadedWorld, the selected speaker's, and its generation
      call carries that world's own compiled prompt as its system prefix.

Plus the per-world session-memory boundary (SS3) and the viewer-
parameterized transcript projection (SS4) at the unit level.
"""
from types import SimpleNamespace

import pytest

from engine.api import table_wiring
from engine.api.app import create_app
from engine.api.tests.conftest import reader_response, safety_response
from engine.api.tests.test_table_api import (
    TableFakeClient,
    _create_table,
    _http,
    _table_client,
    grounded_sentence,
)
from engine.api.wiring import _load_world
from engine.m4 import evidence


@pytest.fixture
def alx_world(world_loader, registry):
    return _load_world(world_loader, registry, "alx")


@pytest.fixture
def desert_world(world_loader, registry):
    return _load_world(world_loader, registry, "desert")


def test_seeded_cross_world_leak_is_withheld_then_dropped(store, usage_store, world_loader, registry, alx_world, desert_world):
    """(b) - alx's voice 'cites' a real desert record. desert's id resolves
    in desert's repository, so the ONLY thing keeping it out of alx's
    citations is that alx's net never sees desert's repository at all."""
    good_sentence, good_rid = grounded_sentence(alx_world)
    _, desert_rid = grounded_sentence(desert_world)
    assert desert_rid in evidence.repository_records_by_id(desert_world.repository)
    leak_sentence = f"The desert elders taught silence above all things [[{desert_rid}]]."
    client = _table_client(
        selector_script=[{"next": "alx", "reason": "r"}],
        stream_scripts=[[good_sentence, " ", leak_sentence], [good_sentence, " ", leak_sentence]],
    )
    http = _http(store=store, usage_store=usage_store, world_loader=world_loader, registry=registry, client=client)
    session_id, auth = _create_table(http)
    result = http.post(f"/api/session/{session_id}/message", json={"text": "what of the desert?"}, headers=auth).json()

    voice = result["voice"]
    assert voice["speaker"] == "alx"
    # The genuine citation survives; the cross-world one is gone.
    cited = {rid for c in voice["citations"] for rid in c["record_ids"]}
    assert good_rid in cited
    assert desert_rid not in cited
    # The net withheld the sentence (an id alx's world does not carry), the
    # one regeneration repeated it, and it was dropped from the reply.
    assert voice["sentence_enforcement"]["flagged"] == [leak_sentence.replace(f" [[{desert_rid}]]", "")]
    assert voice["sentence_enforcement"]["sentences_dropped"] == voice["sentence_enforcement"]["flagged"]
    assert "silence above all things" not in voice["text"]
    assert desert_rid not in voice["text"]
