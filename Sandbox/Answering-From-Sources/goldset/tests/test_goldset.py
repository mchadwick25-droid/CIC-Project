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
    assert not bad["ok"] and "not found verbatim" in bad["why"]
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
    assert result["seeds_caught"] == 19 and result["passes_catch_threshold"] and result["false_alarms"] == 1
    labels[0]["label"] = None
    assert not catch_rate.report(key, labels, "q")["passes_catch_threshold"]


def test_stream_hides_the_key():
    items = [{"item_id": "gs-1", "world": "w", "records_commit": "c", "bindings": [], "sentence": "a", "gate": {}}]
    planted = [{"seed_id": "sd-1", "seed_type": "false_friend", "expected_class": "false_friend", "test_set": "q", "world": "w", "records_commit": "c", "bindings": [], "sentence": "b"}]
    lines, key = stream.build_stream(items, planted, "salt")
    assert {k for line in lines for k in line} == {"line_id", "item_id", "world", "records_commit", "bindings", "sentence"}
    assert {r["kind"] for r in key} == {"pool", "seed"}
    assert stream.build_stream(items, planted, "salt")[0] == lines


def test_split_is_fixed_by_id_and_seal_detects_edits(tmp_path):
    assert split.half("gs-abc") == split.half("gs-abc")
    halves = [split.half(f"gs-{n}") for n in range(400)]
    assert 150 < halves.count(split.HELDOUT) < 250
    item = {"item_id": "gs-1", "world": "w", "records_commit": "c", "bindings": [], "sentence": "a"}
    sealed = split.seal([item], "2026-10-29")
    assert split.broken_seals([item], sealed) == []
    assert split.broken_seals([{**item, "sentence": "b"}], sealed) == ["gs-1"]


def test_loci_and_short_line_ranges():
    found = evidence.loci("SS1-4 -- verified directly against cic/texts/anf05_x.xml, lines 47307-47420; Latin at cic/texts/cyprian-lat_h.txt, line 40782")
    assert found == [("anf05_x.xml", 47307, 47420), ("cyprian-lat_h.txt", 40782, 40782)]
    assert evidence.loci("Letter 7 (npnf206_jerome.xml)") == [("npnf206_jerome.xml", None, None)]
    assert evidence.loci("cic/texts/a.xml, lines 12746-47")[0] == ("a.xml", 12746, 12747)
    assert evidence.file_language("cyprian_opera-lat_hartel.txt") == "lat"


def test_pool_key_ignores_closing_punctuation():
    assert pool._draft_key("He said so [[quote:w.quote.a]].") == pool._draft_key("He said so  [[quote:w.quote.a]]")
