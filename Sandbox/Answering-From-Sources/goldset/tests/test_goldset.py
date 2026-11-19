import json
import random
from pathlib import Path

from goldset import catch_rate, evidence, labeller, pool, seeds, split, stream

PACK = {"item_id": "gs-x", "blocks": [
    {"id": "R1", "kind": "record", "record_id": "w.quote.a", "text": "Cyprian wrote: “the Church is one” and it is not divided."},
    {"id": "L", "kind": "lexicon", "text": "- catholic (distortion risk: high)"},
]}


def reply(**fields):
    base = {"verdict": "supported", "failure_class": None, "other_classes": [], "evidence": [{"block": "R1", "words": "the Church is one"}], "reason": "r", "record_concern": None}
    return json.dumps({**base, **fields})


def test_verbatim_evidence_is_required():
    assert labeller.parse_reply(reply(), PACK)["ok"]
    assert labeller.parse_reply(reply(evidence=[{"block": "R1", "words": "\"the Church is one\""}]), PACK)["ok"]
    bad = labeller.parse_reply(reply(evidence=[{"block": "R1", "words": "the Church is united"}]), PACK)
    assert not bad["ok"] and "found verbatim" in bad["why"]
    assert not labeller.parse_reply(reply(evidence=[{"block": "R1", "words": "the"}]), PACK)["ok"]
    assert not labeller.parse_reply(reply(evidence=[{"block": "R1", "words": "t is not divided"}]), PACK)["ok"]
    assert labeller.parse_reply(reply(evidence=[{"block": "R1", "words": "it is not divided"}]), PACK)["ok"]
    assert not labeller.parse_reply(reply(evidence=["the Church is one"]), PACK)["ok"]
    marked = {"item_id": "x", "blocks": [{"id": "P1", "kind": "passage", "text": "For neither\u27e6/cited\u27e7 does any of us set himself up"}]}
    assert labeller.parse_reply(reply(evidence=[{"block": "P1", "words": "For neither does any of us"}]), marked)["ok"]
    assert not labeller.parse_reply(reply(evidence=[{"block": "P9", "words": "the Church"}]), PACK)["ok"]
    assert not labeller.parse_reply(reply(evidence=[]), PACK)["ok"]


def test_class_vocabulary():
    assert not labeller.parse_reply(reply(verdict="unsupported"), PACK)["ok"]
    assert not labeller.parse_reply(reply(failure_class="false_friend"), PACK)["ok"]
    ok = labeller.parse_reply(reply(verdict="unsupported", failure_class="unsupported_other"), PACK)
    assert ok["ok"] and labeller.gold_class(ok["label"]) == "unsupported"
    ok = labeller.parse_reply("Here: " + reply(verdict="unsupported", failure_class="embedded_voice"), PACK)
    assert labeller.gold_class(ok["label"]) == "embedded_voice"


def test_dropped_negation_inflects_and_needs_the_record_words():
    records = {"w.dw.a": {"text": "We did not pretend the failure away, and we did not make the fallen unforgivable."}}
    item = {"sentence": "We did not pretend the failure away, and we did not make the fallen unforgivable.", "bindings": [{"id": "w.dw.a"}]}
    made = seeds.dropped_negation(item, records)
    assert made["sentence"].startswith("We pretended the failure away")
    assert seeds.dropped_negation({**item, "bindings": [{"id": "missing"}]}, records) is None
    item = {"sentence": "He is never alone: his Word and his Spirit are his own.", "bindings": [{"id": "w.dw.b"}]}
    made = seeds.dropped_negation(item, {"w.dw.b": {"text": "he is never alone: his word and his spirit are his own"}})
    assert made["sentence"] == "He is alone: his Word and his Spirit are his own."


def test_attribution_inflation_only_from_one_authors_quotes():
    records = {"w.quote.a": {"record_type": "quote", "speaker_or_author": "w.figure.origen"}, "w.dw.a": {"record_type": "doctrinal_witness"}}
    item = {"sentence": "Origen wrote that the scriptures have body, soul and spirit.", "bindings": [{"id": "w.quote.a"}]}
    made = seeds.attribution_inflation(item, records, random.Random(0))
    assert made["sentence"].endswith("that the scriptures have body, soul and spirit.")
    assert not made["sentence"].startswith("Origen")
    assert seeds.attribution_inflation({**item, "bindings": [{"id": "w.dw.a"}]}, records, random.Random(0)) is None
    assert seeds.attribution_inflation({**item, "sentence": "He wrote that the scriptures have body, soul and spirit."}, records, random.Random(0)) is None


def test_test_sets_use_each_seed_once():
    accepted = []
    for t in seeds.EXPECTED_CLASS:
        n = 60 if t == "control" else 15
        accepted += [{"seed_id": f"sd-{t}-{k}", "seed_type": t, "expected_class": seeds.EXPECTED_CLASS[t]} for k in range(n)]
    sets = seeds.test_sets(accepted)
    ids = [s["seed_id"] for name in seeds.TEST_SETS for s in sets[name]]
    assert len(ids) == len(set(ids)) == 3 * 40
    assert all(len(sets[name]) == 40 for name in seeds.TEST_SETS)


def test_catch_rate_counts_misses_and_false_alarms():
    key, labels = [], []
    for n in range(20):
        key.append({"line_id": f"s{n}", "kind": "seed", "ref": f"sd{n}", "seed_type": "dropped_negation", "expected_class": "negation_modal_shift", "test_set": "q"})
        verdict = "unsupported" if n < 19 else "supported"
        labels.append({"line_id": f"s{n}", "model_id": "m", "label": {"verdict": verdict, "failure_class": "negation_modal_shift" if verdict == "unsupported" else None, "other_classes": [], "reason": ""}})
    for n in range(20):
        key.append({"line_id": f"c{n}", "kind": "control", "ref": f"c{n}", "seed_type": "control", "expected_class": "supported", "test_set": "q"})
        verdict = "unsupported" if n == 0 else "supported"
        labels.append({"line_id": f"c{n}", "model_id": "m", "label": {"verdict": verdict, "failure_class": "unsupported_other" if verdict == "unsupported" else None, "other_classes": [], "reason": ""}})
    result = catch_rate.report(key, labels, "q")
    assert result["seeds_caught"] == 19 and result["meets_catch_threshold"] and result["false_alarms"] == 1
    assert result["controls_supported"] == 19 and result["qualifies"]
    labels[0]["label"] = None
    labels[21]["label"] = {"verdict": "cannot_judge", "failure_class": None, "other_classes": [], "reason": ""}
    result = catch_rate.report(key, labels, "q")
    assert not result["meets_catch_threshold"] and result["control_misses"] == 1 and result["controls_supported"] == 18
    assert not result["qualifies"]
    import pytest
    with pytest.raises(ValueError):
        catch_rate.report(key, labels + [{**labels[1], "model_id": "other"}], "q")


def test_stream_hides_the_key():
    items = [{"item_id": "gs-1", "world": "w", "records_commit": "c", "bindings": [], "sentence": "a", "gate": {}}]
    planted = [{"seed_id": "sd-1", "seed_type": "false_friend", "expected_class": "false_friend", "test_set": "q", "world": "w", "records_commit": "c", "bindings": [], "sentence": "b"}]
    lines, key = stream.build_stream(items, planted, "salt")
    assert {k for line in lines for k in line} == {"line_id", "item_id", "world", "records_commit", "bindings", "sentence"}
    assert {r["kind"] for r in key} == {"pool", "seed"}
    assert stream.build_stream(items, planted, "salt")[0] == lines


def test_split_is_fixed_by_id_and_seal_detects_edits(tmp_path):
    import pytest
    assert split.half("gs-abc") == split.half("gs-abc")
    halves = [split.half(f"gs-{n}") for n in range(400)]
    assert 150 < halves.count(split.HELDOUT) < 250
    held = next(f"gs-{n}" for n in range(400) if split.half(f"gs-{n}") == split.HELDOUT)
    item = {"item_id": held, "world": "w", "records_commit": "c", "bindings": [], "sentence": "a", "label": {"verdict": "supported"}}
    split.write_halves([item], tmp_path, "2026-10-29")
    split.write_halves([item], tmp_path, "2026-10-30")
    relabelled = {**item, "label": {"verdict": "unsupported", "failure_class": "unsupported_other", "other_classes": []}}
    with pytest.raises(SystemExit):
        split.write_halves([relabelled], tmp_path, "2026-10-30")
    split.write_halves([relabelled], tmp_path, "2026-10-30", {held: "Mark adjudicated"})
    with pytest.raises(SystemExit):
        split.write_halves([], tmp_path, "2026-10-31")
    split.write_halves([], tmp_path, "2026-10-31", {held: "withdrawn"})
    split.write_halves([], tmp_path, "2026-11-01")
    seals = split.yaml.safe_load((tmp_path / "seals.yaml").read_text())
    assert seals["seals"][0]["withdrawn"] and len(seals["seals"][0]["history"]) == 2


def test_loci_and_short_line_ranges():
    found = evidence.loci("SS1-4 -- verified directly against cic/texts/anf05_x.xml, lines 47307-47420; Latin at cic/texts/cyprian-lat_h.txt, line 40782")
    assert found == [("anf05_x.xml", 47307, 47420), ("cyprian-lat_h.txt", 40782, 40782)]
    assert evidence.loci("Letter 7 (npnf206_jerome.xml)") == [("npnf206_jerome.xml", None, None)]
    assert evidence.loci("cic/texts/a.xml, lines 12746-47")[0] == ("a.xml", 12746, 12747)
    assert evidence.loci("cic/texts/a.xml, lines 1299-03")[0] == ("a.xml", 1299, 1303)
    assert evidence.loci("cic/texts/a.xml, outlines 5")[0] == ("a.xml", None, None)
    assert evidence.file_language("cyprian_opera-lat_hartel.txt") == "lat"


def test_pool_key_ignores_closing_punctuation():
    assert pool._draft_key("He said so [[quote:w.quote.a]].") == pool._draft_key("He said so  [[quote:w.quote.a]]")


def _gold(item_id, verdict, cls=None, gate="ok"):
    label = {"verdict": verdict, "failure_class": cls, "other_classes": []}
    return {"item_id": item_id, "label": label, "gate": {"verdict": gate}}


def test_trial_scores_judges_and_gates_against_gold():
    from goldset import trial
    gold = [_gold("a", "unsupported", "embedded_voice", gate="ok"), _gold("b", "unsupported", "unsupported_other", gate="withhold"),
            _gold("c", "supported"), _gold("d", "supported", gate="withhold"), _gold("e", "no_claim")]
    verdicts = {"verifier": {"a": {"supported": False}, "b": {"supported": True}, "c": {"supported": True}, "d": {"supported": True}}}
    made = {**_gold("x", "unsupported", "false_friend"), "origin": "constructed"}
    both = trial.score(gold + [made], {**verdicts, "verifier": {**verdicts["verifier"], "x": {"supported": False}}})
    assert both["constructed"]["items"] == 1 and both["constructed"]["deciders"]["judge:verifier"]["recall_unsupported"] == 1.0
    result = both["natural"]
    assert result["items"] == 4
    judge = result["deciders"]["judge:verifier"]
    assert (judge["recall_unsupported"], judge["precision_unsupported"]) == (0.5, 1.0)
    gates = result["deciders"]["current_gates"]
    assert (gates["recall_unsupported"], gates["precision_unsupported"]) == (0.5, 0.5)
    queue = trial.adjudication_queue(gold, verdicts, sample=0)
    assert [q["item_id"] for q in queue] == ["b"]


def test_judgement_parsing():
    from goldset import trial
    assert trial.parse_judgement("verifier", 'ok {"supported": false, "reason": "x"}', 1)["supported"] is False
    assert trial.parse_judgement("verifier", '{"supported": "no"}', 1) is None
    got = trial.parse_judgement("citation_recall", '{"entailed": true, "needed": [1, 9], "reason": ""}', 2)
    assert got["supported"] is True and got["citation_precision"] == 0.5


def test_inplan_round_trip_checks_replies_and_offers_one_retry(tmp_path, monkeypatch):
    from goldset import inplan
    monkeypatch.setattr(inplan, "build_pack", lambda item: PACK)
    lines = [{"line_id": "ln-1", "item_id": "gs-1", "world": "w", "records_commit": "c", "bindings": [], "sentence": "s"},
             {"line_id": "ln-2", "item_id": "gs-2", "world": "w", "records_commit": "c", "bindings": [], "sentence": "s"}]
    assert inplan.export(lines, tmp_path) == 2
    text = (tmp_path / "prompts" / "ln-1.md").read_text()
    assert "SENTENCE TO CHECK" in text and "gs-1" not in text
    (tmp_path / "replies" / "ln-1.txt").write_text(reply())
    (tmp_path / "replies" / "ln-2.txt").write_text(reply(evidence=[{"block": "R1", "words": "invented words here now"}]))
    rows, retry = inplan.import_replies(lines, tmp_path, "opus")
    assert [r["line_id"] for r in rows] == ["ln-1"] and retry == ["ln-2"]
    assert (tmp_path / "prompts" / "ln-2.retry.md").exists()
    (tmp_path / "replies" / "ln-2.retry.txt").write_text("not json")
    rows, retry = inplan.import_replies(lines, tmp_path, "opus")
    assert retry == [] and rows[1]["label"] is None and len(rows[1]["attempts"]) == 2


def test_agreement_queues_disagreements_and_key_classes():
    from goldset import agreement
    def lab(v, c=None):
        return {"label": {"verdict": v, "failure_class": c, "other_classes": []}, "model_id": "m"}
    first = {"a": lab("supported"), "b": lab("unsupported", "generalisation"), "c": lab("supported"), "d": lab("supported")}
    second = {"a": lab("supported"), "b": lab("unsupported", "generalisation"), "c": lab("unsupported", "unsupported_other"), "d": lab("supported")}
    result = agreement.compare(first, second, sample=1)
    assert result["items_both_labelled"] == 4 and result["disagreements"] == 1
    assert [q["item_id"] for q in result["queue"][:2]] == ["b", "c"] and len(result["queue"]) == 3
    assert result["verdict_agreement"] == 0.75


def test_locus_paths_and_numerals():
    from goldset import locus
    assert locus.number("XIV") == 14 and locus.number("iv") == 4 and locus.number("12") == 12 and locus.number("abc") is None
    assert locus.path_of("Book II, ch. 3 - what we look to") == [2, 3]
    assert locus.path_of("VII.24") == [7, 24]
    assert locus.path_of("Letter XXII (to Eustochium), sec. 30 - the dream") == [22, 30]
    assert locus.path_of("the 1539 preface") == []
    assert locus._names("Vita Antonii (Life of Antony), c. 356 - epitome") == [{"vita", "antonii"}, {"life", "antony"}]


def test_stream_plants_constructed_items_under_their_own_kind():
    made = [{"construct_id": "cx-1", "kind": "constructed", "seed_type": "embedded_voice", "expected_class": "embedded_voice",
             "world": "w", "records_commit": "c", "bindings": [], "sentence": "c"}]
    lines, key = stream.build_stream([], [], "salt", constructed=made)
    assert [(r["kind"], r["ref"], r["expected_class"]) for r in key] == [("constructed", "cx-1", "embedded_voice")]
    assert set(lines[0]) == {"line_id", "item_id", "world", "records_commit", "bindings", "sentence"}


def test_packet_keeps_every_queued_item_and_every_specialist_key_class():
    from goldset import packet
    def lab(c):
        return {"label": {"verdict": "supported" if c == "supported" else "unsupported", "failure_class": None if c == "supported" else c, "other_classes": []}}
    specialist = {"a": lab("supported"), "b": lab("generalisation"), "e": lab("false_friend")}
    queue = [{"item_id": "c", "why": "disagreement"}, {"item_id": "d", "why": "key class"},
             {"item_id": "b", "why": "key class"}, {"item_id": "a", "why": "random sample of agreements"}]
    assert packet.order(specialist, queue) == [("c", "disagreement"), ("b", "key class (specialist)"), ("e", "key class (specialist)"),
                                               ("d", "key class (second labeller)"), ("a", "random sample of agreements")]


def test_constructed_packet_queues_misreads_natural_key_classes_and_a_sample():
    from goldset import packet
    def lab(c):
        return {"label": {"verdict": "supported" if c == "supported" else "unsupported", "failure_class": None if c == "supported" else c, "other_classes": []}}
    specialist = {"cx-1": lab("embedded_voice"), "cx-2": lab("negation_modal_shift"), "gs-1": lab("false_friend"), "gs-2": lab("supported")}
    constructed = {"cx-1": {"expected_class": "embedded_voice"}, "cx-2": {"expected_class": "embedded_voice"}}
    assert packet.constructed_order(specialist, constructed, sample=5) == [
        ("cx-2", "constructed, not read as intended"), ("gs-1", "key class (specialist)"), ("cx-1", "random sample of constructed items")]


def test_gold_build_lets_a_ruling_win_and_keeps_evidence_only_for_the_same_reading():
    from goldset import build
    spec = {"verdict": "unsupported", "failure_class": "generalisation", "other_classes": [], "evidence": [{"block": "R1", "words": "a b c d"}]}
    same = build.ruled_label({"verdict": "unsupported", "class": "generalisation", "note": "agree"}, spec)
    other = build.ruled_label({"verdict": "supported", "class": "supported", "note": "the record says so"}, spec)
    assert same["evidence"] == spec["evidence"] and other["evidence"] == [] and other["failure_class"] is None
    items = [{"origin": "natural", "label": same, "label_source": "mark"}, {"origin": "constructed", "label": spec, "label_source": "construction"}]
    assert build.counts(items)["constructed"] == {"items": 1, "by_class": {"generalisation": 1}, "by_label_source": {"construction": 1}}


def test_numbered_work_found_by_the_editions_own_piece_number():
    from goldset import locus
    def div(n, kind, short, title="To Eustochium.", start=1):
        return {"level": 2, "start": start, "end": start + 9, "title": title, "n": n, "id": "v." + n, "type": kind, "short": short}
    nodes = (div("XXII", "Letter", "Letter XXII", start=1), div("CVIII", "Letter", "Letter CVIII", start=20), div("CVIII", "Homily", "Homily CVIII", start=40))
    assert locus._numbered_work(nodes, "Epistula 108, to Eustochium (404)")["start"] == 20
    assert locus._numbered_work(nodes, "Letter 22 - on virginity")["start"] == 1
    assert locus._numbered_work(nodes, "Epistula 5") is None
    assert locus._numbered_work(nodes, "Vita Malchi") is None


def test_adjudication_stands_on_two_of_three_and_names_the_read_it_quotes():
    from goldset import adjudicate, build
    assert adjudicate.outcome(["supported", "supported", "generalisation"]) == ("supported", 2)
    assert adjudicate.outcome(["supported", "generalisation", "cannot_judge"]) == (None, 1)
    assert adjudicate.outcome(["supported", None, None]) == (None, 1)
    fable = {"verdict": "unsupported", "failure_class": "generalisation", "other_classes": [], "evidence": [{"block": "R1", "words": "w x y z"}], "reason": "r"}
    adj = {"item_id": "a", "standing_class": "generalisation", "classes": {"opus": "supported", "fable": "generalisation", "referee": "generalisation"},
           "reads": {"opus": {"label": {}}, "fable": {"label": fable}, "referee": {"label": {}}}}
    label = build.adjudicated_label(adj)
    assert label["evidence_from"] == "fable" and label["failure_class"] == "generalisation"
