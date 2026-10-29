"""Seeded defects for testing a labeller, and known-supported controls beside
them, so a labeller that flags everything cannot pass.

Four defect types, each made by a fixed rule from the worlds' own records, so
the defect is certain by construction and checkable by anyone:

  dropped_negation       a pool sentence whose negated clause is the bound
                         record's own words, with the negation removed: the
                         sentence now contradicts the record.
  attribution_inflation  a pool sentence that names one author and is bound
                         only to that author's quote records, with the author
                         replaced by the whole community.
  false_friend           a term record's own lexicon flag ("must not be read
                         as X") stated as the term's meaning, bound to that
                         term record.
  embedded_voice         the words of an outsider or opponent, from a quote
                         record whose register is etic, stated as the
                         tradition's own conviction, bound to that record.

Controls are a record's own sentence, copied from its voiced text, bound to
that record: supported by construction.

Every candidate is printed for a reading before it enters a test; a candidate
the reading rejects is marked so and never used. Each seed and control is
used in one test only.

  python -m goldset.seeds --pool <pool.jsonl> --out <seed bank.jsonl>
"""
import argparse
import json
import random
import re
from collections import Counter
from pathlib import Path

from goldset.common import read_jsonl, records_at, stable_id, write_jsonl, yaml
from goldset.labeller import _fold

EXPECTED_CLASS = {
    "dropped_negation": "negation_modal_shift",
    "attribution_inflation": "generalisation",
    "false_friend": "false_friend",
    "embedded_voice": "embedded_voice",
    "control": "supported",
}

_IRREGULAR_PAST = {
    "be": "was", "become": "became", "begin": "began", "bring": "brought", "buy": "bought", "come": "came",
    "do": "did", "eat": "ate", "find": "found", "forget": "forgot", "get": "got", "give": "gave", "go": "went",
    "have": "had", "hear": "heard", "hold": "held", "keep": "kept", "know": "knew", "lead": "led", "leave": "left",
    "let": "let", "lose": "lost", "make": "made", "mean": "meant", "put": "put", "read": "read", "run": "ran",
    "say": "said", "see": "saw", "seek": "sought", "sell": "sold", "send": "sent", "set": "set", "sit": "sat",
    "speak": "spoke", "spend": "spent", "stand": "stood", "take": "took", "teach": "taught", "tell": "told",
    "think": "thought", "understand": "understood", "win": "won", "write": "wrote", "fall": "fell", "feel": "felt",
    "flee": "fled", "forgive": "forgave", "grow": "grew", "hide": "hid", "rise": "rose", "shut": "shut", "throw": "threw",
}
_DO_NOT = re.compile(r"\b(did|does|do)(?: not|n't) (?:(always|ever|simply|just|even|really) )?([a-z]+)\b")
_AUX_NOT = re.compile(r"\b(was|were|is|are|could|would|should|had|has|have|will|can|must|might|may)(?: not|n't)\b")
_NEVER = re.compile(r"\bnever ")


def _past(verb: str) -> str:
    if verb in _IRREGULAR_PAST:
        return _IRREGULAR_PAST[verb]
    if verb.endswith("e"):
        return verb + "d"
    if re.search(r"[^aeiou]y$", verb):
        return verb[:-1] + "ied"
    return verb + "ed"


def _third(verb: str) -> str:
    if verb in ("be", "have", "do", "go"):
        return {"be": "is", "have": "has", "do": "does", "go": "goes"}[verb]
    if re.search(r"(s|sh|ch|x|z|o)$", verb):
        return verb + "es"
    if re.search(r"[^aeiou]y$", verb):
        return verb[:-1] + "ies"
    return verb + "s"


def _drop(m: re.Match) -> str:
    aux, adverb, verb = m.group(1), m.group(2), m.group(3)
    verb = {"did": _past, "does": _third}.get(aux, lambda v: v)(verb)
    return f"{adverb} {verb}" if adverb else verb


_NEGATIONS = [(_DO_NOT, _drop), (_AUX_NOT, lambda m: m.group(1).replace("can", "can")), (_NEVER, lambda m: "")]


_AUTHOR_LEAD = re.compile(
    r"^(?:In [^,]{3,60}, )?(?P<name>(?:Saint |Bishop |Abba |Pope )?[A-Z][a-z]+(?: (?:of|the) [A-Z][a-z]+)?) "
    r"(?P<verb>wrote|writes|taught|teaches|said|says|argued|argues|insisted|insists|told|tells|warned|warns|urged|urges|"
    r"explained|explains|reminded|reminds|preached|preaches|held|holds|believed|believes|described|describes|declared|declares|"
    r"put it|puts it)\b(?: (?:plainly|simply|bluntly|directly|clearly))?(?: (?:that|this))?[,:]?\s*"
)
_PRONOUNS = {"He", "She", "It", "They", "We", "This", "That", "There", "One"}
_LEAD_FILLER = re.compile(r"^(?:that|this|plainly|simply|so|thus)\b[,:]?\s*", re.IGNORECASE)
_COMMUNITY = ("All of us held", "Our whole church taught", "Every one of us believed", "We all agreed")
_FALSE_FRIEND_FRAMES = (
    "For us, {term} meant {reading}.",
    "When we spoke of {term}, we meant {reading}.",
    "{Term} was, quite simply, {reading}.",
)
_EMBEDDED_FRAMES = (
    "We said it of ourselves, plainly: {words}",
    "This was our own conviction: {words}",
    "We taught our people this: {words}",
)
_SENTENCE = re.compile(r"[^.!?]+[.!?]")


def _voiced_text(record: dict) -> str:
    return " ".join(str(record.get(f) or "") for f in ("text", "modern_rendering", "plain_meaning"))


def dropped_negation(item: dict, records: dict) -> dict | None:
    record_text = _fold(" ".join(_voiced_text(records.get(b["id"]) or {}) for b in item["bindings"]))
    for pattern, replacement in _NEGATIONS:
        m = pattern.search(item["sentence"])
        if not m:
            continue
        words = item["sentence"].split()
        clause = _fold(item["sentence"][max(0, m.start() - 40): m.end() + 40])
        window = " ".join(clause.split()[1:-1])
        if len(window.split()) < 6 or window not in record_text:
            continue
        mutated = item["sentence"][: m.start()] + replacement(m) + item["sentence"][m.end():]
        if mutated != item["sentence"] and len(words) >= 6:
            return {"sentence": mutated, "construction": f"removed '{m.group(0)}'; the record has: ...{window}..."}
    return None


def attribution_inflation(item: dict, records: dict, rng: random.Random) -> dict | None:
    bound = [records.get(b["id"]) for b in item["bindings"]]
    if not bound or any(r is None or r.get("record_type") != "quote" for r in bound):
        return None
    m = _AUTHOR_LEAD.match(item["sentence"])
    if not m or m.group("name") in _PRONOUNS:
        return None
    speakers = {str(r.get("speaker_or_author") or "") for r in bound}
    if not any(m.group("name").split()[0].lower() in s.lower() for s in speakers):
        return None
    rest = _LEAD_FILLER.sub("", item["sentence"][m.end():]).lstrip("'\u2018\"\u201c")
    if len(rest.split()) < 5 or not rest[0].isalpha():
        return None
    lead = rng.choice(_COMMUNITY)
    return {"sentence": f"{lead} that {rest[0].lower()}{rest[1:]}", "construction": f"'{m.group(0).strip()}' became '{lead} that'"}


def inflated_meanings(records: dict, rng: random.Random) -> list[dict]:
    """A one-author quote record's own `means` line, its author replaced by
    the whole community, bound to that quote record."""
    out = []
    for record in records.values():
        means = str((record.get("use_note") or {}).get("means") or "")
        if record.get("record_type") != "quote" or record.get("register") != "emic":
            continue
        m = _AUTHOR_LEAD.match(means)
        if not m or m.group("name") in _PRONOUNS or m.group("verb").startswith(("described", "describes", "told", "tells")):
            continue
        rest = _LEAD_FILLER.sub("", means[m.end():]).strip()
        if len(rest.split()) < 6 or not rest[0].isalpha() or rest.lower().startswith(("he ", "she ", "his ", "her ")):
            continue
        lead = rng.choice(_COMMUNITY)
        out.append({"sentence": f"{lead} that {rest[0].lower()}{rest[1:]}", "bindings": [{"kind": "record", "id": record["id"]}],
                    "construction": f"the quote record's means line '{m.group(0).strip()}' became '{lead} that'"})
    return out


def false_friends(records: dict, rng: random.Random) -> list[dict]:
    out = []
    for record in records.values():
        if record.get("record_type") != "term" or not record.get("false_friend") or not record.get("world_word"):
            continue
        reading = str(rng.choice(record["false_friend"])).strip().rstrip(".")
        reading = re.split(r"\s+--\s+|;", reading)[0].strip()
        if len(reading.split()) < 2:
            continue
        term = str(record["world_word"])
        frame = rng.choice(_FALSE_FRIEND_FRAMES)
        sentence = frame.format(term=term, Term=term[0].upper() + term[1:], reading=reading)
        out.append({"sentence": sentence, "bindings": [{"kind": "record", "id": record["id"]}],
                    "construction": f"the term record's flag says {term!r} must not be read as {reading!r}"})
    return out


def embedded_voices(records: dict, rng: random.Random) -> list[dict]:
    out = []
    for record in records.values():
        if record.get("record_type") != "quote" or record.get("register") != "etic":
            continue
        rendering = " ".join(str(record.get("modern_rendering") or record.get("text") or "").split())
        sentences = [re.sub(r"^(?:But|And|So|For|Yet|Now|Then|Nor)\b,?\s*", "", s.strip()) for s in _SENTENCE.findall(rendering) if 8 <= len(s.split()) <= 30]
        sentences = [s[0].upper() + s[1:] for s in sentences if s and not s.lower().startswith(("nor ", "or "))]
        if not sentences:
            continue
        words = rng.choice(sentences)
        frame = rng.choice(_EMBEDDED_FRAMES)
        out.append({"sentence": frame.format(words=words), "bindings": [{"kind": "record", "id": record["id"]}],
                    "construction": f"etic words of {record.get('speaker_or_author')!r} voiced as the tradition's own"})
    return out


def controls(item: dict, records: dict, rng: random.Random) -> dict | None:
    record = records.get(item["bindings"][0]["id"]) or {}
    sentences = [s.strip() for s in _SENTENCE.findall(" ".join(str(record.get("text") or "").split())) if 8 <= len(s.split()) <= 30 and '"' not in s]
    if not sentences or record.get("record_type") not in ("doctrinal_witness", "story", "term"):
        return None
    return {"sentence": rng.choice(sentences), "bindings": [item["bindings"][0]], "construction": "copied from the record's own text"}


def build_bank(pool: list[dict], seed: int = 20261029) -> list[dict]:
    rng = random.Random(seed)
    bank = []

    def add(seed_type: str, base: dict, made: dict) -> None:
        bank.append({
            "seed_id": stable_id("sd", seed_type, base["world"], made["sentence"]),
            "seed_type": seed_type, "expected_class": EXPECTED_CLASS[seed_type],
            "world": base["world"], "records_commit": base["records_commit"],
            "sentence": made["sentence"], "bindings": made.get("bindings") or base["bindings"],
            "base_item_id": base.get("item_id"), "construction": made["construction"],
            "reading": None,
        })

    commits = {}
    for item in pool:
        commits.setdefault(item["world"], item)
    for item in pool:
        records = records_at(item["records_commit"], item["world"])
        made = dropped_negation(item, records)
        if made:
            add("dropped_negation", item, made)
        made = attribution_inflation(item, records, rng)
        if made:
            add("attribution_inflation", item, made)
    for world, base in sorted(commits.items()):
        records = records_at(base["records_commit"], world)
        for made in inflated_meanings(records, rng):
            add("attribution_inflation", base, made)
        for made in false_friends(records, rng):
            add("false_friend", base, made)
        for made in embedded_voices(records, rng):
            add("embedded_voice", base, made)
        worlds_items = [i for i in pool if i["world"] == world and i["bindings"][0]["kind"] == "record"]
        for item in rng.sample(worlds_items, min(12, len(worlds_items))):
            made = controls(item, records, rng)
            if made:
                add("control", item, made)
    more = random.Random(seed + 1)
    for world, base in sorted(commits.items()):
        records = records_at(base["records_commit"], world)
        worlds_items = [i for i in pool if i["world"] == world and i["bindings"][0]["kind"] == "record"]
        for item in more.sample(worlds_items, min(24, len(worlds_items))):
            made = controls(item, records, more)
            if made:
                add("control", item, made)
    unique = {s["seed_id"]: s for s in bank}
    return sorted(unique.values(), key=lambda s: (s["seed_type"], s["world"], s["seed_id"]))


TEST_SETS = ("tryout", "qualify", "retest")
DEFECTS_PER_TYPE = 5
CONTROLS_PER_SET = 20


def accepted_seeds(bank: list[dict], readings: dict, pool: list[dict]) -> list[dict]:
    """The bank's candidates the reading accepted, with their repairs, plus
    the hand-written ones. A control that is the original of an accepted
    defect is dropped, so no test holds a sentence and its own mutation."""
    by_id = {s["seed_id"]: s for s in bank}
    out = []
    for seed_type, entries in (readings.get("accepted") or {}).items():
        for entry in entries:
            seed_id, repair = (entry, None) if isinstance(entry, str) else (entry["id"], entry.get("repair"))
            seed = dict(by_id[seed_id])
            if seed["seed_type"] != seed_type:
                raise ValueError(f"{seed_id} is read as {seed_type} but the bank made it as {seed['seed_type']}")
            if repair:
                seed.update(sentence=repair, repaired_from=seed["sentence"])
            out.append({**seed, "reading": "accepted"})
    for made in readings.get("authored") or []:
        out.append({
            "seed_id": stable_id("sd", made["seed_type"], made["world"], made["sentence"]),
            "seed_type": made["seed_type"], "expected_class": EXPECTED_CLASS[made["seed_type"]],
            "world": made["world"], "records_commit": made["records_commit"], "sentence": made["sentence"],
            "bindings": made["bindings"], "base_item_id": None, "construction": made["construction"], "reading": "authored",
        })
    originals = {_fold(i["sentence"]) for i in pool if i["item_id"] in {s["base_item_id"] for s in out if s["seed_type"] != "control"}}
    return [s for s in out if not (s["seed_type"] == "control" and _fold(s["sentence"]) in originals)]


def test_sets(accepted: list[dict], salt: str = "seed-tests-2026-10-29") -> dict[str, list[dict]]:
    """Each accepted seed in one test set at most: five of each defect type
    and twenty controls per set, in a fixed order drawn from a hash."""
    def order(seed: dict) -> str:
        return stable_id("o", salt, seed["seed_id"], length=16)

    sets: dict[str, list[dict]] = {name: [] for name in TEST_SETS}
    for seed_type in EXPECTED_CLASS:
        group = sorted((s for s in accepted if s["seed_type"] == seed_type), key=order)
        size = CONTROLS_PER_SET if seed_type == "control" else DEFECTS_PER_TYPE
        for n, name in enumerate(TEST_SETS):
            chunk = group[n * size: (n + 1) * size]
            if len(chunk) < size:
                raise ValueError(f"{seed_type}: {len(group)} accepted, {size * len(TEST_SETS)} needed for {len(TEST_SETS)} sets")
            sets[name].extend({**s, "test_set": name} for s in chunk)
    return sets


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--pool", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True, help="the candidate bank")
    parser.add_argument("--readings", type=Path, help="with this, also write the test sets beside the bank")
    args = parser.parse_args(argv)
    pool = read_jsonl(args.pool)
    bank = build_bank(pool)
    write_jsonl(args.out, bank)
    print(json.dumps(Counter((s["seed_type"]) for s in bank), sort_keys=True))
    if args.readings:
        accepted = accepted_seeds(bank, yaml.safe_load(args.readings.read_text(encoding="utf-8")), pool)
        sets = test_sets(accepted)
        write_jsonl(args.out.with_name("seed-tests.jsonl"), [s for name in TEST_SETS for s in sets[name]])
        print(json.dumps({name: Counter(s["seed_type"] for s in sets[name]) for name in TEST_SETS}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
