"""End-to-end phase-1 audit over constructed event logs (Artifact-8 §2-§4):
reader, instruments, report layers, CLI sweep. The two claims these tests
guard hardest: every formerly-unread output now has a reader, and no
participant text ever reaches the fleet layer.
"""
import json
import uuid

from engine.m4.store import Store
from engine.m7.cli import audit
from engine.m7.instruments import (
    ask_coverage,
    canon_candidate_asks,
    encounter_openings,
    governance,
    isolation,
    offer_rates,
    register_frame,
    repetition,
    run_all,
    safety_review,
    unread_outputs,
)
from engine.m7.session_reader import read_session

PARTICIPANT_ASK = "did the desert monks abandon their families forever"


def _gate(asks, register="informational"):
    return {
        "asks": asks, "register": register,
        "out_of_scope": {"class": "none", "pressed": False}, "modern_terms": [],
        "safety": {"signal": "NO_SIGNAL", "confidence": "high"},
        "route": "voice", "directive": {}, "degraded": False,
    }


def _voice(speaker, text, citations, **extra):
    payload = {
        "speaker": speaker, "text": text, "citations": citations,
        "glosses": [], "figures_used": [], "quote_offers": [],
        "attempts_meta": {}, "output_defects": [],
    }
    payload.update(extra)
    return payload


def _append(store, sid, etype, payload):
    store.append(session_id=sid, event_uuid=str(uuid.uuid4()), event_type=etype, payload=payload)


def seed_interview(store, sid):
    """An interview with one of everything the instruments look for."""
    _append(store, sid, "session_started", {
        "mode": "interview", "frame": "general_seeker", "code_hash": "abc",
        "world_key": "des", "package_manifest_hash": "sha256:x",
    })
    _append(store, sid, "participant_message", {"text": PARTICIPANT_ASK, "client_msg_id": "m1"})
    _append(store, sid, "gate_decision", _gate([{"order": 1, "text": PARTICIPANT_ASK}]))
    # The answering turn: covers the ask, cites its own world, but carries
    # every formerly-unread output in a non-clean state.
    _append(store, sid, "voice_turn", _voice(
        "des",
        "Some monks did leave their families to go into the desert, and some "
        "families followed them there. The elders spoke of this parting as a "
        "wound that prayer carried, not one it erased, and letters still "
        "moved between the cells and the villages they had left behind.",
        [{"sentence": "Some monks did leave their families to go into the desert, and some families followed them there.",
          "record_ids": ["des.source.apophthegmata-1"]},
         {"sentence": "letters moved", "record_ids": ["hal.source.foreign-1"]}],  # isolation defect
        grounding={"sentences": [
            {"verdict": "ok", "tags": []},
            {"verdict": "withheld", "tags": ["des.source.apophthegmata-9"]},
        ]},
        output_defects=["floor_line_missing"],
        do_not_voice_violation="quoted a do_not_voice span",
    ))
    # A second ask that draws no coverage at all -> ask_coverage review.
    _append(store, sid, "participant_message", {"text": "what about taxes", "client_msg_id": "m2"})
    _append(store, sid, "gate_decision", _gate([{"order": 1, "text": "what about zebra quills"}], register="personal_wound"))
    _append(store, sid, "voice_turn", _voice(
        "des", "The elders spoke of prayer and of bread, of the long silence of the cells.",
        [{"sentence": "s", "record_ids": ["des.story.cell-visit"]}],
        degraded_by_net=True,
    ))
    # Safety turn as the last exchange, participant never speaks again,
    # closed by idle -> intervention-followed-by-abandonment.
    _append(store, sid, "facilitator_turn", {"kind": "safety", "text": "I want to pause here with you."})
    _append(store, sid, "session_closed", {"reason": "idle"})


def seed_table(store, sid):
    _append(store, sid, "session_started", {
        "mode": "table", "frame": "general_seeker", "code_hash": "abc",
        "world_keys": ["des", "cap"], "package_manifest_hashes": {"des": "sha256:x", "cap": "sha256:y"},
    })
    _append(store, sid, "participant_message", {"text": PARTICIPANT_ASK, "client_msg_id": "t1"})
    _append(store, sid, "gate_decision", _gate([{"order": 1, "text": PARTICIPANT_ASK}]))
    _append(store, sid, "turn_selected", {"round_no": 1, "position": 1, "world_key": "des", "reason": "direct address", "degraded": False})
    long_answer = ("The desert monks did not all abandon their families forever. Some kept "
                   "letters moving between the cells and their villages for many years. "
                   "The elders taught that a monk who forgot his mother's name had lost "
                   "the desert itself, for the desert was meant to enlarge love, not end it.")
    _append(store, sid, "voice_turn", _voice(
        "des", long_answer,
        [{"sentence": "s", "record_ids": ["des.source.apophthegmata-1"]}],
    ))
    _append(store, sid, "turn_selected", {"round_no": 1, "position": 2, "world_key": "cap", "reason": "fallback order", "degraded": True})
    _append(store, sid, "voice_turn", _voice(
        "cap", long_answer,  # same text, different voice - repetition counts per-voice only
        [{"sentence": "s", "record_ids": ["cap.quote.basil-3"]}],
    ))
    _append(store, sid, "round_closed", {"round_no": 1, "reason": "selector_closed", "turns": 2,
                                         "governance": {"flags": ["dominance:des"], "share": {"des": 0.8}}})
    # Round 2: the same voice repeats itself verbatim -> repetition finding.
    _append(store, sid, "turn_selected", {"round_no": 2, "position": 1, "world_key": "des", "reason": "follow-up", "degraded": False})
    _append(store, sid, "voice_turn", _voice(
        "des", long_answer,
        [{"sentence": "s", "record_ids": ["des.source.apophthegmata-1"]}],
    ))
    _append(store, sid, "round_closed", {"round_no": 2, "reason": "floor_unmet_exhausted", "turns": 1})
    _append(store, sid, "session_closed", {"reason": "participant"})


def _sessions(tmp_path):
    store = Store(tmp_path / "events.db")
    i_sid, t_sid = "int-" + uuid.uuid4().hex[:8], "tab-" + uuid.uuid4().hex[:8]
    seed_interview(store, i_sid)
    seed_table(store, t_sid)
    return store, i_sid, t_sid


# --- reader ---

def test_reader_lifts_the_four_unread_outputs_and_rounds(tmp_path):
    store, i_sid, t_sid = _sessions(tmp_path)
    s = read_session(store, i_sid)
    assert s.mode == "interview" and s.world_keys == ["des"]
    t0 = s.voice_turns[0]
    assert t0.do_not_voice_violation == "quoted a do_not_voice span"
    assert t0.output_defects == ["floor_line_missing"]
    assert t0.grounding["sentences"][1]["verdict"] == "withheld"
    assert s.voice_turns[1].degraded_by_net is True
    assert t0.round_no is None  # interview turns carry no round

    t = read_session(store, t_sid)
    assert t.mode == "table" and t.world_keys == ["des", "cap"]
    assert [vt.round_no for vt in t.voice_turns] == [1, 1, 2]
    assert t.rounds_closed[0]["governance"]["flags"] == ["dominance:des"]
    assert t.closed and t.close_reason == "participant"


def test_reader_survives_log_without_session_started(tmp_path):
    store = Store(tmp_path / "events.db")
    _append(store, "orphan", "participant_message", {"text": "hello", "client_msg_id": "x"})
    s = read_session(store, "orphan")
    assert s.mode == "unknown" and s.event_count == 1


# --- store sweep ---

def test_list_session_ids_orders_and_filters(tmp_path):
    store, i_sid, t_sid = _sessions(tmp_path)
    assert store.list_session_ids() == [i_sid, t_sid]
    assert store.list_session_ids(since="2020-01-01") == [i_sid, t_sid]
    assert store.list_session_ids(since="2099-01-01") == []


# --- instruments ---

def test_unread_outputs_all_three_severities(tmp_path):
    store, i_sid, _ = _sessions(tmp_path)
    findings = unread_outputs(read_session(store, i_sid))
    by = {f.instrument: f for f in findings}
    assert by["do_not_voice"].severity == "defect"
    assert by["output_defects"].severity == "review"
    assert by["net_withheld"].severity == "info"
    assert by["net_withheld"].record_ids == ["des.source.apophthegmata-9"]
    assert by["degraded_by_net"].severity == "info"


def test_isolation_flags_foreign_citation_only(tmp_path):
    store, i_sid, t_sid = _sessions(tmp_path)
    findings = isolation(read_session(store, i_sid))
    assert len(findings) == 1
    assert findings[0].severity == "defect"
    assert findings[0].record_ids == ["hal.source.foreign-1"]
    assert isolation(read_session(store, t_sid)) == []


def test_ask_coverage_flags_only_the_uncovered_ask(tmp_path):
    store, i_sid, t_sid = _sessions(tmp_path)
    findings = ask_coverage(read_session(store, i_sid))
    assert len(findings) == 1 and findings[0].severity == "review"
    assert ask_coverage(read_session(store, t_sid)) == []


def test_repetition_within_one_voice(tmp_path):
    store, _, t_sid = _sessions(tmp_path)
    findings = repetition(read_session(store, t_sid))
    assert len(findings) == 1
    assert "des repeated" in findings[0].detail


def test_safety_abandonment_is_review(tmp_path):
    store, i_sid, _ = _sessions(tmp_path)
    findings = safety_review(read_session(store, i_sid))
    assert len(findings) == 1
    assert findings[0].instrument == "safety_abandonment" and findings[0].severity == "review"


def test_register_frame_catches_all_three_families(tmp_path):
    """The three real cases: Mark's screen (syr, 'To this world Jesus
    is...'), P1-L4 (Papnoute in the third person), F1-L4 (the
    'Papnoute (Desert Monasticism):' label echo)."""
    store = Store(tmp_path / "events.db")
    sid = "frame-" + uuid.uuid4().hex[:8]
    _append(store, sid, "session_started", {
        "mode": "interview", "frame": "general_seeker", "code_hash": "abc",
        "world_key": "syr", "package_manifest_hash": "sha256:x",
    })
    _append(store, sid, "voice_turn", _voice(
        "syr", "To this world Jesus is the Only-Begotten of God.", []))
    _append(store, sid, "voice_turn", _voice(
        "syr", "Mar Yausep has spoken of the covenant before.", []))
    _append(store, sid, "voice_turn", _voice(
        "syr", "Mar Yausep (Syriac Christianity): We remember the flood of 201.", []))
    _append(store, sid, "voice_turn", _voice(
        "syr", "We remember the covenant, and we sing what we believe.", []))
    names = {"syr": ["Mar Yausep", "Syriac Christianity (Edessa/Nisibis)"]}
    findings = register_frame(read_session(store, sid), names)
    assert all(f.severity == "review" for f in findings)
    details = " | ".join(f.detail for f in findings)
    assert "third person" in details and '"this world"' in details
    assert "its own name" in details
    assert "label echo" in details
    # the clean communal turn produced nothing: 1 this-world + 2 own-name + 1 label echo
    assert len(findings) == 4
    # without names, the name detector stays silent rather than guessing
    assert all("its own name" not in f.detail for f in register_frame(read_session(store, sid), None))


def test_encounter_openings_counted(tmp_path):
    store, i_sid, _ = _sessions(tmp_path)
    findings = encounter_openings(read_session(store, i_sid))
    assert len(findings) == 1 and findings[0].severity == "info"
    assert "voice answered: True" in findings[0].detail


def test_governance_flags_and_selector_degradation(tmp_path):
    store, _, t_sid = _sessions(tmp_path)
    findings = governance(read_session(store, t_sid))
    details = [f.detail for f in findings]
    assert any("dominance:des" in d for d in details)
    assert any("floor-unmet" in d for d in details)
    assert any(f.instrument == "selector_degraded" for f in findings)


def test_offer_rates_from_type_segment(tmp_path):
    store, _, t_sid = _sessions(tmp_path)
    rates = offer_rates(read_session(store, t_sid))
    assert rates == {"source": 2, "quote": 1}


def test_canon_asks_are_normalized_participant_text(tmp_path):
    store, i_sid, _ = _sessions(tmp_path)
    asks = canon_candidate_asks(read_session(store, i_sid))
    assert PARTICIPANT_ASK in asks  # already lowercase/plain
    assert "what about zebra quills" in asks


def test_register_metrics_score_long_turns_and_mark_short_unscored(tmp_path):
    store, _, t_sid = _sessions(tmp_path)
    a = run_all(read_session(store, t_sid))
    scored = [m for m in a["register_metrics"] if m["scored"]]
    assert scored, "the long table answers must score"
    assert all("fk_grade" in m and "fre" in m for m in scored)
    assert any("first_sentence_first_ask_overlap" in m for m in a["register_metrics"])


# --- reports + CLI ---

def test_cli_audit_writes_all_layers_and_keeps_participant_text_out_of_fleet(tmp_path):
    store, i_sid, t_sid = _sessions(tmp_path)
    out = tmp_path / "audit-out"
    rollup = audit(str(tmp_path / "events.db"), out)

    assert rollup["sessions_audited"] == 2
    assert rollup["findings_by_severity"]["defect"] >= 2  # do_not_voice + isolation
    assert rollup["lineage_session_ids"] == [i_sid, t_sid]

    # Per-session files exist and (necessarily, operator-only) carry the text.
    session_doc = json.loads((out / "sessions" / f"{i_sid}.json").read_text())
    assert session_doc["lineage_session_ids"] == [i_sid]
    assert PARTICIPANT_ASK in json.dumps(session_doc)

    # The fleet layer NEVER carries participant text (Artifact-8 §4).
    rollup_text = (out / "fleet-rollup.json").read_text()
    digest_text = (out / "fleet-digest.md").read_text()
    for fleet_bytes in (rollup_text, digest_text):
        assert PARTICIPANT_ASK not in fleet_bytes
        assert "zebra" not in fleet_bytes
        assert i_sid in fleet_bytes  # lineage names every session

    # Canon candidates: recurring ask across both sessions, operator-only.
    canon = json.loads((out / "canon-candidates.json").read_text())
    assert canon["lineage_session_ids"] == [i_sid, t_sid]
    top = canon["candidates"][0]
    assert top["ask"] == PARTICIPANT_ASK
    assert top["count"] == 2 and top["session_ids"] == sorted([i_sid, t_sid])
    # the one-off ask from a single session is not a candidate
    assert all(c["ask"] != "what about zebra quills" for c in canon["candidates"])


def test_cli_since_scopes_the_sweep(tmp_path):
    store, i_sid, t_sid = _sessions(tmp_path)
    out = tmp_path / "audit-out-since"
    rollup = audit(str(tmp_path / "events.db"), out, since="2099-01-01")
    assert rollup["sessions_audited"] == 0
    assert rollup["lineage_session_ids"] == []
    assert (out / "fleet-digest.md").exists()


def test_cli_main_exit_code_signals_defects(tmp_path, capsys):
    from engine.m7.cli import main
    store, _, _ = _sessions(tmp_path)
    code = main(["audit", "--events-db", str(tmp_path / "events.db"), "--out", str(tmp_path / "o")])
    assert code == 1  # defects present in the seeded data
    assert "audited 2 session(s)" in capsys.readouterr().out

    clean = Store(tmp_path / "clean.db")
    seed_table(clean, "tab-clean")
    # the table seed carries review/info findings but no defect
    code = main(["audit", "--events-db", str(tmp_path / "clean.db"), "--out", str(tmp_path / "o2")])
    assert code == 0
