"""Hermetic tests for the E1 layouts, answerers and runner - fake clients
only, no network and no billed call."""
import re
from pathlib import Path
from types import SimpleNamespace

import pytest

import engine.m3.e1_run as e1_run
from engine.m1.loader import load_world_records
from engine.m1.registry import formation_world_keys, load_registry
from engine.m3 import e1_layout as layout
from engine.m3.e1_answerers import DossierAnswerer, NativeCitationAnswerer, read_response
from engine.m4.world_loader import LoadedWorld

REPO_ROOT = Path(__file__).resolve().parents[3]
REGISTRY = load_registry()
WORLDS = sorted(formation_world_keys(REGISTRY))
CELLS = ["F1-I", "F4-T"]


def _prompt(world_key: str) -> str:
    location = REPO_ROOT / REGISTRY[world_key]["package"]["location"]
    return (location / "compiled" / "prompt.txt").read_text(encoding="utf-8")


def test_the_eleven_formation_worlds_are_covered():
    assert WORLDS == sorted("alx cappadocian desert don gallic hal ijc pahc rzg syr witt".split())


@pytest.mark.parametrize("world_key", WORLDS)
def test_split_rejoins_byte_for_byte(world_key):
    prompt = _prompt(world_key)
    header, blocks, footer = layout.split_prompt(prompt)
    assert (header + "".join(blocks.values()) + footer).encode("utf-8") == prompt.encode("utf-8")
    assert header.startswith("## Register")
    assert "## Citation contract" in header
    record_keys = [k for k in blocks if not layout.is_shared(k)]
    assert record_keys and all(f"[[{k}]]" in blocks[k].split("\n", 1)[0] for k in record_keys)
    assert [k for k in blocks if layout.is_shared(k)] == ["section:gravities", "section:quotes-we-hold"]


def test_split_refuses_a_prompt_without_record_blocks():
    with pytest.raises(ValueError):
        layout.split_prompt("## Register\n\nx\n")


@pytest.fixture(scope="module")
def desert():
    prompt = _prompt("desert")
    return prompt, load_world_records("desert"), layout.split_prompt(prompt)[1]


def test_dossier_is_the_cell_records_plus_every_witness_and_story(desert):
    _, records, blocks = desert
    ids = layout.dossier_ids(records, CELLS, blocks)
    expected = {
        r["id"] for r in records.values()
        if r["record_type"] in layout.VOICE_TYPES
        and r["id"] in blocks
        and (r["record_type"] in ("doctrinal_witness", "story") or set(CELLS) & set(r.get("canon_cells") or []))
    }
    assert ids == expected
    types = {records[i]["record_type"] for i in ids}
    assert types <= set(layout.VOICE_TYPES)
    assert {r["id"] for r in records.values() if r["record_type"] in ("doctrinal_witness", "story")} <= ids
    for i in ids:
        r = records[i]
        assert r["record_type"] in ("doctrinal_witness", "story") or set(CELLS) & set(r["canon_cells"])


def test_no_cells_leaves_only_witnesses_and_stories(desert):
    _, records, blocks = desert
    ids = layout.dossier_ids(records, [], blocks)
    assert {records[i]["record_type"] for i in ids} == {"doctrinal_witness", "story"}


def test_index_lines_are_deterministic_one_per_voice_record(desert):
    _, records, blocks = desert
    lines = layout.index_lines(records, blocks)
    assert lines == layout.index_lines(records, blocks)
    assert len(lines) == len([k for k in blocks if not layout.is_shared(k)])
    assert all(len(line) < 400 and line.startswith("- [[") for line in lines)
    sample = next(line for line in lines if "desert.term.anachoresis" in line)
    assert "Term: anachoresis" in sample and "cells: F4-I,F5-P" in sample


def test_assemble_c_carries_only_dossier_blocks_and_lists_the_rest_as_index_lines(desert):
    prompt, records, blocks = desert
    ids = layout.dossier_ids(records, CELLS, blocks)
    text = layout.assemble_c(prompt, records, CELLS)
    headings = re.findall(r"^## .* \(cite as \[\[([^\[\]]+)\]\]\)$", text, re.MULTILINE)
    core = {i for i in headings if records[i]["record_type"] == "world_core"}
    assert set(headings) - core == ids
    for key, block in blocks.items():
        if not layout.is_shared(key) and key not in ids:
            assert block not in text
            assert f"- [[{key}]] " in text
    for key in ids:
        assert blocks[key] in text
    assert text.index("## Index") < min(text.index(blocks[k]) for k in ids)
    assert len(text) < len(prompt)


def test_assemble_c_keeps_the_compiler_text_in_original_order(desert):
    prompt, records, blocks = desert
    text = layout.assemble_c(prompt, records, CELLS)
    ids = layout.dossier_ids(records, CELLS, blocks)
    positions = [text.index(t) for k, t in blocks.items() if layout.is_shared(k) or k in ids]
    assert positions == sorted(positions)


def test_native_documents_titles_equal_dossier_ids_and_drop_the_marker(desert):
    prompt, records, blocks = desert
    system, documents = layout.assemble_native(prompt, records, CELLS)
    ids = layout.dossier_ids(records, CELLS, blocks)
    assert [d["title"] for d in documents] == [k for k in blocks if k in ids]
    assert {d["title"] for d in documents} == ids
    for d in documents:
        assert d["type"] == "document" and d["citations"] == {"enabled": True}
        assert d["source"]["type"] == "text" and d["source"]["media_type"] == "text/plain"
        head = d["source"]["data"].split("\n", 1)[0]
        assert "cite as" not in head and f"[[{d['title']}]]" not in head
        assert d["source"]["data"].split("\n", 1)[1] == blocks[d["title"]].split("\n", 1)[1]
    assert "## Citation contract\n\n" + layout.NATIVE_CONTRACT + "\n\n## Limit discipline" in system
    assert "Every id is COPIED" not in system
    for key in blocks:
        if not layout.is_shared(key):
            assert f"## {blocks[key].split(chr(10), 1)[0][3:]}" not in system


def test_replace_citation_contract_reports_the_replaced_text(desert):
    prompt, _, _ = desert
    header, _, _ = layout.split_prompt(prompt)
    new_header, replaced = layout.replace_citation_contract(header)
    assert replaced.startswith("Every sentence that makes a specific claim is tagged")
    assert replaced not in new_header
    assert new_header.replace(layout.NATIVE_CONTRACT + "\n", replaced) == header


def test_manifest_shape():
    m = layout.manifest("c", ["F1-I"], {"b", "a"}, 12)
    assert m == {"arm": "c", "cells": ["F1-I"], "dossier_ids": ["a", "b"], "prompt_chars": 12}


# ---- answerers with fake clients -------------------------------------------------

_USAGE = SimpleNamespace(input_tokens=10, output_tokens=5, cache_creation_input_tokens=0, cache_read_input_tokens=0)
ASK = "Who was Jesus, to you and your people? What did your community actually know about him?"
CANON = {"fleet.canon.q1": {"id": "fleet.canon.q1", "record_type": "canon_question", "cell": "C-I", "text": ASK}}
_PROMPT = (
    "## Register\n\nSpeak.\n\n## Citation contract\n\nTag every claim [[x.y]].\n\n"
    "## Below this line is our world's own record\n\nGround.\n\n"
    "## Witness (C-I) (cite as [[fix.dw.jesus]])\n\nWe did not see him.\n\n"
    "## Term: bread (cite as [[fix.term.bread]])\n\nBread, daily.\n\n"
    "## Story (cite as [[fix.story.road]])\n\nA road.\n"
)
_RECORDS = [
    {"id": "fix.dw.jesus", "record_type": "doctrinal_witness", "canon_cells": ["C-I"], "text": "We did not see him."},
    {"id": "fix.term.bread", "record_type": "term", "canon_cells": ["F5-P"], "quick_meaning": "Bread, daily."},
    {"id": "fix.story.road", "record_type": "story", "canon_cells": ["F4-P"], "text": "A road."},
]
_EMPTY = {"doctrinal_witness": [], "terms": [], "stories": [], "quotes": [], "honest_limit": [], "gravities": [], "forces": [], "contested_claims": []}


def _world():
    return LoadedWorld(
        world_key="fix", manifest_hash="sha256:t", prompt_text=_PROMPT, capsule_text="", repository={"records": _RECORDS},
        quotes={"quotes": []}, figures={}, coverage={"C-I": {**_EMPTY, "doctrinal_witness": ["fix.dw.jesus"]}}, frame={},
    )


class _StreamCtx:
    def __init__(self, chunks):
        self._chunks = chunks

    def __enter__(self):
        return SimpleNamespace(text_stream=iter(self._chunks), get_final_message=lambda: SimpleNamespace(usage=_USAGE))

    def __exit__(self, *exc):
        return False


class _FakeMessages:
    def __init__(self, chunks=(), response=None):
        self.chunks, self.response = chunks, response
        self.stream_calls, self.create_calls = [], []

    def stream(self, **kwargs):
        self.stream_calls.append(kwargs)
        return _StreamCtx(self.chunks)

    def create(self, **kwargs):
        self.create_calls.append(kwargs)
        return self.response


class _FakeClient:
    def __init__(self, **kwargs):
        self.messages = _FakeMessages(**kwargs)


def test_dossier_answerer_sends_the_assembled_layout_as_system():
    client = _FakeClient(chunks=["We did not see him [[fix.dw.jesus]]."])
    answerer = DossierAnswerer(world=_world(), canon_questions=CANON, client=client, model_id="m")
    result = answerer.answer("C-I", ASK)
    assert result.text == "We did not see him."
    assert result.citations == ["fix.dw.jesus"]
    call = client.messages.stream_calls[0]
    records = {r["id"]: r for r in _RECORDS}
    assert call["system"][0]["text"] == layout.assemble_c(_PROMPT, records, answerer.last_manifest["cells"])
    assert "## Ground for this turn" in call["messages"][0]["content"]
    assert "C-I" in answerer.last_manifest["cells"]
    assert answerer.last_manifest["arm"] == "c"
    assert "fix.term.bread" not in answerer.last_manifest["dossier_ids"]
    assert answerer.last_manifest["prompt_chars"] == len(call["system"][0]["text"])


def _response(*blocks):
    return SimpleNamespace(content=list(blocks), usage=_USAGE, stop_reason="end_turn")


def _cite(index, title):
    return SimpleNamespace(type="char_location", document_index=index, document_title=title)


def test_native_answerer_maps_document_citations_to_record_ids():
    response = _response(
        SimpleNamespace(type="text", text="We did not see him. ", citations=[_cite(0, "fix.dw.jesus")]),
        SimpleNamespace(type="text", text="We walked a road.", citations=[_cite(1, "fix.story.road"), _cite(0, "fix.dw.jesus")]),
        SimpleNamespace(type="text", text="That is all.", citations=None),
    )
    client = _FakeClient(response=response)
    answerer = NativeCitationAnswerer(world=_world(), canon_questions=CANON, client=client, model_id="m")
    result = answerer.answer("C-I", ASK)

    call = client.messages.create_calls[0]
    docs = [b for b in call["messages"][0]["content"] if b["type"] == "document"]
    assert [d["title"] for d in docs] == ["fix.dw.jesus", "fix.story.road"]
    assert call["messages"][0]["content"][-1]["type"] == "text"
    assert layout.NATIVE_CONTRACT in call["system"][0]["text"]
    assert result.text == "We did not see him. We walked a road.That is all."
    assert result.citations == ["fix.dw.jesus", "fix.story.road"]
    assert result.citation_entries == [
        {"sentence": "We did not see him.", "record_ids": ["fix.dw.jesus"]},
        {"sentence": "We walked a road.", "record_ids": ["fix.dw.jesus", "fix.story.road"]},
        {"sentence": "That is all.", "record_ids": []},
    ]
    assert result.source_record_id == "fix.dw.jesus"
    assert result.source_record_type == "doctrinal_witness"
    assert answerer.last_raw_response_text == (
        "We did not see him.  [[fix.dw.jesus]]We walked a road. [[fix.dw.jesus]] [[fix.story.road]]That is all."
    )
    assert answerer.last_manifest["arm"] == "native"
    assert answerer.last_manifest["dossier_ids"] == ["fix.dw.jesus", "fix.story.road"]


def test_read_response_accepts_dict_blocks_and_drops_unresolvable_citations():
    response = {"content": [
        {"type": "thinking", "thinking": "x"},
        {"type": "text", "text": "A.", "citations": [{"document_index": 1}, {"document_index": 7}]},
    ]}
    text, entries, _ = read_response(response, ["a", "b"])
    assert text == "A."
    assert entries == [{"sentence": "A.", "record_ids": ["b"]}]


# ---- runner --------------------------------------------------------------------

def _no_network(*args, **kwargs):
    raise AssertionError("a billed or network call was attempted")


def test_settings_only_makes_no_billed_call(monkeypatch):
    monkeypatch.setattr(e1_run, "resolve_model_id", lambda pattern, region: "us.anthropic.claude-sonnet-4-5-20250929-v1:0")
    monkeypatch.setattr(e1_run, "make_client", _no_network)
    report = e1_run.run("us-east-1", "c", world_keys=["desert"], authorized_by="test-harness", settings_only=True)
    assert report["settings_only"] is True
    assert report["run_settings"]["arm"] == "c"
    assert report["estimated_usd_preflight"] > 0
    native = e1_run.run("us-east-1", "native", world_keys=["desert"], authorized_by="test-harness", settings_only=True)
    assert native["run_settings"]["voice_call"].startswith("messages.create")


def test_a_run_over_the_ceiling_aborts_before_any_model_resolution(monkeypatch):
    monkeypatch.setattr(e1_run, "resolve_model_id", _no_network)
    monkeypatch.setattr(e1_run, "make_client", _no_network)
    with pytest.raises(SystemExit, match="exceeds --max-usd"):
        e1_run.run("us-east-1", "c", world_keys=["desert"], max_usd=0.01, authorized_by="test-harness")


def test_runner_refuses_blank_authorizer_unknown_world_and_unpriced_model(monkeypatch):
    monkeypatch.setattr(e1_run, "make_client", _no_network)
    with pytest.raises(SystemExit, match="authorized-by"):
        e1_run.run("us-east-1", "c", world_keys=["desert"], authorized_by=" ")
    with pytest.raises(SystemExit, match="not a real formation world"):
        e1_run.run("us-east-1", "c", world_keys=["nope"], authorized_by="x")
    with pytest.raises(SystemExit, match="no approved price table"):
        e1_run.run("us-east-1", "c", world_keys=["desert"], authorized_by="x", voice_model_pattern="unpriced-model")
    with pytest.raises(SystemExit, match="--arm"):
        e1_run.run("us-east-1", "z", world_keys=["desert"], authorized_by="x")


def test_the_usage_proxy_records_a_non_streaming_call():
    response = _response(SimpleNamespace(type="text", text="Yes.", citations=[_cite(0, "doc.a")]))
    inner = SimpleNamespace(messages=_FakeMessages(response=response))
    client = e1_run._E1Client(inner)
    documents = [{"type": "document", "title": "doc.a", "source": {}, "citations": {"enabled": True}}]
    client.messages.create(model="m", max_tokens=5, messages=[{"role": "user", "content": [*documents, {"type": "text", "text": "q"}]}])
    assert client.messages.log == [_USAGE]
    call = client.messages.calls[0]
    assert call["raw_text"] == "Yes. [[doc.a]]" and call["stop_reason"] == "end_turn" and "seconds_total" in call


WHOLE_WORLDS = ["alx", "cappadocian", "desert", "don", "gallic", "hal", "ijc", "pahc", "rzg", "syr", "witt"]


@pytest.mark.parametrize("world_key", WHOLE_WORLDS)
def test_native_whole_attaches_every_record_once(world_key):
    import re as _re
    from engine.m3 import e1_layout as L
    prompt = _whole_prompt(world_key)
    header, blocks, footer = L.split_prompt(prompt)
    system, documents = L.assemble_native_whole(prompt)
    titles = [d["title"] for d in documents]
    expected = [k for k in blocks if not L.is_shared(k)]
    for key, text in blocks.items():
        if L.is_shared(key):
            expected += _re.findall(r"^- \[\[([^\[\]\s]+)\]\] ", text, _re.MULTILINE)
    assert sorted(titles) == sorted(expected)
    assert len(titles) == len(set(titles))
    assert documents[-1]["cache_control"] == {"type": "ephemeral"}
    assert all("cache_control" not in d for d in documents[:-1])
    assert all(d["citations"] == {"enabled": True} for d in documents)
    new_header, _ = L.replace_citation_contract(header)
    assert system == new_header + footer
    assert L.NATIVE_CONTRACT in system


def _whole_prompt(world_key):
    from pathlib import Path
    from engine.m1.registry import load_registry
    from engine.m4.world_loader import LazyWorldLoader
    entry = load_registry()[world_key]
    world, _ = LazyWorldLoader().load(
        world_key, package_dir=Path(entry["package"]["location"]), expected_manifest_hash=entry["package"]["manifest_hash"]
    )
    return world.prompt_text
