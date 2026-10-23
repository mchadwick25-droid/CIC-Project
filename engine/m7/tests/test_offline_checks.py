"""engine.m7.offline_checks: the report-only turn checks, run after the
conversation from what the event log carries."""
from engine.m7.instruments import run_all
from engine.m7.offline_checks import offline_checks
from engine.m7.session_reader import AuditSession, VoiceTurnRecord

RECORDS = {"w.dw.bread": {"id": "w.dw.bread", "record_type": "doctrinal_witness", "text": "We kept the bread together each week."}}


def _turn(seq, text, sentences, output_defects=()):
    return VoiceTurnRecord(seq=seq, speaker="w", text=text, citations=[], grounding={"sentences": sentences},
                           output_defects=list(output_defects), degraded_by_net=False, round_no=None)


def _session(*turns):
    return AuditSession(session_id="s", mode="interview", world_keys=["w"], closed=False, close_reason=None,
                        participant_messages=[{"seq": 1, "text": "who was Jesus"}], voice_turns=list(turns))


UNCITED = {"sentence": "Bishop Cyprian died in Carthage in 258.", "tags": [], "verdict": "withhold", "why": "untagged specific claim"}


def test_an_uncited_claim_is_reported_from_the_logged_net_result():
    found = offline_checks(_session(_turn(2, UNCITED["sentence"], [UNCITED])), {"w": RECORDS})
    assert any(f.instrument == "uncited_claims" and f.severity == "info" for f in found)


def test_output_families_are_recomputed_for_turns_logged_after_slimming():
    text = "**We** kept the bread together each week."
    found = offline_checks(_session(_turn(2, text, [])), {"w": RECORDS})
    assert any(f.instrument == "display" and f.severity == "review" for f in found)


def test_a_turn_logged_before_slimming_is_not_recomputed():
    logged = [{"family": "display", "finding": "literal asterisks", "sentence": "**We** kept the bread."}]
    found = offline_checks(_session(_turn(2, "**We** kept the bread.", [], logged)), {"w": RECORDS})
    assert not any(f.instrument == "display" for f in found)


def test_run_all_carries_the_offline_findings():
    audit = run_all(_session(_turn(2, UNCITED["sentence"], [UNCITED])), repositories={"w": RECORDS})
    assert any(f.instrument == "uncited_claims" for f in audit["findings"])


PERSON_RECORDS = {
    "w.figure.justin": {"id": "w.figure.justin", "record_type": "figure", "names": [{"name": "Justin", "tag": "in-world"}]},
    "w.figure.clement": {"id": "w.figure.clement", "record_type": "figure", "names": [{"name": "Clement", "tag": "in-world"}]},
    "w.dw.chain": {"id": "w.dw.chain", "record_type": "doctrinal_witness",
                   "text": "Clement wrote that the apostles preached what they received and appointed others after them. "
                           "Justin tells how the memoirs were read on Sunday."},
}
CREDITED = {"sentence": "Justin said the apostles preached what they received and appointed others after them.",
            "tags": ["w.dw.chain"], "verdict": "ok", "why": "grounded"}


def test_words_credited_to_a_person_the_cited_passage_does_not_name_are_flagged_for_review():
    # pahc Q2, 14 October: 1 Clement's chain credited to Justin
    found = offline_checks(_session(_turn(2, CREDITED["sentence"], [CREDITED])), {"w": PERSON_RECORDS})
    assert [f.severity for f in found if f.instrument == "person_claims"] == ["review"]
    right = {**CREDITED, "sentence": CREDITED["sentence"].replace("Justin", "Clement")}
    found = offline_checks(_session(_turn(2, right["sentence"], [right])), {"w": PERSON_RECORDS})
    assert not [f for f in found if f.instrument == "person_claims"]
