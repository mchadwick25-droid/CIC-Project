import json

import yaml

from goldset import fit

PAIRS = (
    [{"pair_id": f"p{n:02d}", "kind": "planted", "expected": "off_point", "question": "q", "record_id": "r"} for n in range(1, 21)]
    + [{"pair_id": f"p{n:02d}", "kind": "control", "expected": "fits", "question": "q", "record_id": "r"} for n in range(21, 41)]
)


def row(pair_id, verdict, limit=False):
    judgement = None if verdict is None else {"fit": verdict, "reason": "", "limit_stated": limit}
    decision = None if judgement is None else ("keep" if verdict == "fits" or (verdict == "partly" and limit) else "drop")
    return {"pair_id": pair_id, "judgement": judgement, "decision": decision}


def rows(planted_missed=0, controls_dropped=0):
    out = [row(f"p{n:02d}", "fits" if n <= planted_missed else "off_point") for n in range(1, 21)]
    return out + [row(f"p{n:02d}", "off_point" if n - 20 <= controls_dropped else "fits") for n in range(21, 41)]


def test_nineteen_of_twenty_planted_pairs_dropped_meets_the_bar():
    result = fit.score(PAIRS, rows(planted_missed=1))
    assert result["planted_dropped"] == 19 and result["meets_bar"] is True
    assert result["planted"]["wrong"] == ["p01"]


def test_eighteen_does_not_meet_the_bar():
    assert fit.score(PAIRS, rows(planted_missed=2))["meets_bar"] is False


def test_a_planted_pair_with_no_readable_reply_blocks_the_bar_and_is_counted():
    reply_rows = rows()
    reply_rows[0] = row("p01", None)
    result = fit.score(PAIRS, reply_rows)
    assert result["planted"]["unreadable_or_missing"] == 1 and result["meets_bar"] is False


def test_controls_wrongly_dropped_are_reported_apart_from_the_bar():
    result = fit.score(PAIRS, rows(controls_dropped=3))
    assert result["controls_wrongly_dropped"] == 3 and result["meets_bar"] is True


def test_export_and_import_round_trip(tmp_path, monkeypatch):
    record = {"id": "r", "record_type": "quote", "modern_rendering": "Spoken.", "use_note": {"means": "m", "not_for": []}}
    pairs = PAIRS[:2]
    assert fit.export_prompts(pairs, {"r": record}, tmp_path) == 2
    assert (tmp_path / "prompts" / "p01.md").read_text().startswith("SYSTEM\n")
    (tmp_path / "replies" / "p01.txt").write_text('{"fit": "off_point", "reason": "x", "limit_stated": false}')
    imported = fit.import_replies(pairs, "model", tmp_path)
    assert [(r["pair_id"], r["decision"]) for r in imported] == [("p01", "drop")]


def test_a_set_of_the_wrong_size_or_with_a_repeated_id_is_refused():
    import pytest

    with pytest.raises(ValueError):
        fit.check_pairs(PAIRS[:-1])
    with pytest.raises(ValueError):
        fit.check_pairs(PAIRS[:39] + [dict(PAIRS[0])])


def test_the_decision_is_recomputed_from_the_judgement_not_taken_from_the_row():
    rows_ = rows()
    rows_[0] = {"pair_id": "p01", "judgement": {"fit": "fits", "reason": "", "limit_stated": False}, "decision": "drop"}
    assert fit.score(PAIRS, rows_)["planted"]["wrong"] == ["p01"]


def test_pairs_load_from_yaml(tmp_path):
    path = tmp_path / "pairs.yaml"
    path.write_text(yaml.safe_dump({"pairs": PAIRS}))
    assert len(fit.load_pairs(path)) == 40
