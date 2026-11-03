"""The V7 reader harness: blind reader requests, adjudication, scoring and the review sample.

It makes no model call. It writes request files and reads reply files.

  export        one request per answer for each of reader-1 and reader-2, a manifest, and the key files in --key-dir
  seed-copies   adds seeded-defect copies to an export as further opaque items; seals their key
  adjudicate    writes a third-reader request for every item that meets the trigger
  after-october writes the follow-up request that shows the October findings, once a reader has filed every blind reply
  score         reads the replies and writes the score tables as JSON and markdown
  mark-pack     builds the JSON that the human review page loads

Requests hold probe wording, so every output directory except score's tables must lie outside the
repository and outside the main checkout. The key directory (key.json, seed.json, seed_key.json) lies
outside the export directory too. Each request is one item and refers to no other, so a reader runs
one item per fresh context.
"""
import argparse
import hashlib
import json
import random
import re
import statistics
import sys
from pathlib import Path

from engine.m1.loader import load_world_records
from engine.m3 import sealed_probes, v7_passages
from engine.m3.v7_run import WORLDS, protected_roots

REPO_ROOT = Path(__file__).resolve().parents[2]
FEATURE_DIR = REPO_ROOT / "Build" / "Ministry" / "Features" / "V7-Controlled-Test"
RUBRIC_PATH = FEATURE_DIR / "Rubric.md"
SET_DIR = FEATURE_DIR / "Set"
REPORTS_DIR = REPO_ROOT / "engine" / "m3" / "reports"
TEXTS_ROOT = REPO_ROOT

READERS = ("reader-1", "reader-2")
ADJUDICATOR = "adjudicator"
RUBRIC_END = "## How the readers work"
DIMENSIONS = (
    "source_accuracy", "contextual_integrity", "interpretive_fidelity", "answers_the_question",
    "fidelity_to_the_world", "natural_and_engaging", "honest_uncertainty", "world_embodiment",
    "conversational_quality", "general_user_accessibility",
)
RIGOR_DIMENSIONS = DIMENSIONS[:3]
ACCESS_DIMENSION = DIMENSIONS[9]
DEPTHS = ("rich", "adequate", "thin", "flat")
ERROR_TYPES = (
    "out of context", "claim beyond the source", "one author as the tradition", "does not answer",
    "beyond the author's intent", "modern projection", "flattened uncertainty", "invented", "misquoted", "other",
)
DEFECT_TYPES = {
    "wrong_frame": {"out of context"},
    "author_generalized": {"one author as the tradition"},
    "modern_projection": {"modern projection"},
    "unsupported_inference": {"claim beyond the source"},
    **{re.sub(r"[\s-]+", "_", t): {t} for t in ERROR_TYPES},
}
CONFIDENCES = ("sure", "fairly sure", "unsure")
TIERS = (1, 2, 3)
EXACT_AGREEMENT_FLOOR = 0.60
CATCH_RATE_FLOOR = 0.90
MIN_SEEDED = 10
MATCH_THRESHOLD = 0.5
SPAN_THRESHOLD = 0.5
MARK_PASSAGE_WORDS = 160
RISK_LEVELS = ("high", "medium")
CARD_LABEL = "Project-authored reading note. It is not an authority. Check it against the source passage."
COMMON_FIELDS = ("id", "record_type", "confidence", "sources", "use_note")
TYPE_FIELDS = {
    "quote": ("text", "modern_rendering", "modern_lens_note", "speaker_or_author", "setting"),
    "story": ("narrative_tier", "tellable_as", "text", "telling", "heart", "events", "absent_detail", "modern_contrast"),
    "term": ("world_word", "plain_meaning", "quick_meaning", "senses", "false_friend", "distortion_risk", "prior_sense"),
    "gravity": ("name", "description", "manifestations", "classification"),
    "force": ("name", "kind", "description", "manifestations"),
    "contested_claim": ("claim", "held_against", "concedes", "divergence_partners"),
    "honest_limit": ("statement", "why_sources_cannot_answer", "nearest_material"),
    "doctrinal_witness": ("text", "positions", "tensions", "answers_obliquely", "oblique_reason"),
    "demonstration": ("exchange",),
    "world_core": ("horizon", "formation_logic", "thinness", "cautions", "living_traditions"),
    "voice_craft": ("identity", "flavor_notes", "characteristic_concerns"),
    "figure": ("names", "dates", "narratable"),
}
FORBIDDEN_IN_BLIND = (r"\barm\b", r"october", r"second[ _-]pass", r"referee", r"fleet[ -]graded")
QUOTED_FRAGMENT = re.compile(r"(?<![\w])'([^']{8,}?)'(?![\w])|\"([^\"]{8,}?)\"|“([^”]{8,}?)”")
CONFIRMING_PREFIXES = ("this is correct", "correct", "accurate", "this is accurate", "this is broadly", "broadly fine",
                       "this is fair", "defensible", "fair but")

ERROR_SCHEMA = {
    "type": "object",
    "required": ["answer_words", "source_words", "type", "tier", "confidence", "evidence"],
    "properties": {
        "answer_words": {"type": "string", "description": "the exact words of the answer"},
        "source_words": {"type": "string", "description": "the exact words of the source that show the error"},
        "type": {"enum": list(ERROR_TYPES), "description": "or 'other: <what>'"},
        "tier": {"enum": list(TIERS), "description": "1 false or invented; 2 misleading scope, context or interpretation; 3 craft"},
        "confidence": {"enum": list(CONFIDENCES)},
        "evidence": {"type": "string", "description": "the source and lines that show the error"},
    },
}
REPLY_SCHEMA = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "type": "object",
    "required": ["item_id", "reader", "scores", "depth", "errors"],
    "properties": {
        "item_id": {"type": "string"},
        "reader": {"type": "string"},
        "scores": {
            "type": "object",
            "required": list(DIMENSIONS),
            "properties": {
                d: {"type": "object", "required": ["score", "reason"],
                    "properties": {"score": {"enum": [0, 1, 2]}, "reason": {"type": "string", "description": "one sentence"}}}
                for d in DIMENSIONS
            },
        },
        "depth": {"enum": list(DEPTHS)},
        "errors": {"type": "array", "items": ERROR_SCHEMA},
    },
}
AFTER_OCTOBER_SCHEMA = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "type": "object",
    "required": ["item_id", "reader", "added_errors"],
    "properties": {
        "item_id": {"type": "string"},
        "reader": {"type": "string"},
        "added_errors": {"type": "array", "items": {**ERROR_SCHEMA, "required": ERROR_SCHEMA["required"] + ["after_october_review"],
                                                      "properties": {**ERROR_SCHEMA["properties"], "after_october_review": {"const": True}}}},
    },
}
INSTRUCTIONS = (
    "Score the answer on each rubric dimension, 0, 1 or 2, with one sentence of reason. Give its depth. "
    "List every error with the exact words of the answer and the exact words of the source. "
    "Check each quotation and claim against the source passage. A reading note is project-authored: check it too. "
    "Reply with one JSON object in the reply format."
)
PASSAGE_NOTE = (
    "Each passage is the cited place with its surrounding division. A source listed under source_passages_unresolved "
    "has no passage text: its passage was not located."
)


class Refused(Exception):
    """The command refuses to run; main returns exit code 2."""


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _write_json(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def _read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def _inside_protected(path: Path) -> bool:
    resolved = path.resolve()
    return any(resolved == root or root in resolved.parents for root in protected_roots())


def require_outside_repo(path: Path) -> Path:
    """The path, refused when it lies inside the repository or the main checkout."""
    if _inside_protected(path):
        raise Refused(f"{path} is inside the repository or its main checkout; requests hold probe text, so write outside them")
    return path


def _require_apart(first: Path, second: Path) -> None:
    a, b = first.resolve(), second.resolve()
    if a == b or a in b.parents or b in a.parents:
        raise Refused(f"{first} and {second} must be separate directories, neither inside the other")


def item_id(seed: int, key: str) -> str:
    return "i" + hashlib.sha256(f"{seed}|{key}".encode("utf-8")).hexdigest()[:12]


def item_key(world: str, arm: str, run: int, probe_id: str) -> str:
    return f"{world}|{arm}|{run}|{probe_id}"


def shuffled(ids: list[str], seed: int, label: str) -> list[str]:
    """The ids in a seeded order that depends only on the sorted ids, the seed and the label."""
    ordered = sorted(ids)
    random.Random(f"{seed}|order|{label}").shuffle(ordered)
    return ordered


def write_seed(key_dir: Path, seed: int) -> None:
    """The seed file, written before any id or order is drawn; an existing file must hold the same seed."""
    path = key_dir / "seed.json"
    if path.exists():
        if _read_json(path)["seed"] != seed:
            raise Refused(f"{path} holds a different seed")
        return
    _write_json(path, {"seed": seed})


def read_seed(key_dir: Path) -> int:
    path = key_dir / "seed.json"
    if not path.exists():
        raise Refused(f"no seed.json in {key_dir}")
    return _read_json(path)["seed"]


def register_of(cell: str) -> str:
    """The register letter of a cell code: the last letter after the final hyphen (C-E has three characters, F4-T four)."""
    letter = cell.rsplit("-", 1)[-1]
    if letter not in ("I", "E", "P", "T"):
        raise ValueError(f"cell {cell!r} does not end in a register letter")
    return letter


def rubric_text() -> str:
    """Rubric.md up to its reader-method section; that section names the arms and the October reviews."""
    text = RUBRIC_PATH.read_text(encoding="utf-8")
    head = text.split(RUBRIC_END, 1)[0].rstrip() + "\n"
    for pattern in FORBIDDEN_IN_BLIND:
        if re.search(pattern, head, re.IGNORECASE):
            raise Refused(f"the rubric text matches {pattern!r}; a blind request may not carry it")
    return head


def _load_records(world: str) -> dict[str, dict]:
    return load_world_records(world)


def read_question(probe_id: str) -> str:
    return sealed_probes.read_probe(probe_id)["text"]


def _tokens(text: str) -> set[str]:
    return {t for t in re.findall(r"\w+", (text or "").lower()) if len(t) > 2}


def containment(part: str, whole: str) -> float:
    """The share of part's words (three letters or more) that whole also holds."""
    a = _tokens(part)
    return len(a & _tokens(whole)) / len(a) if a else 0.0


def overlaps(first: str, second: str, threshold: float = MATCH_THRESHOLD) -> bool:
    return max(containment(first, second), containment(second, first)) >= threshold


def _record_view(record: dict) -> dict:
    fields = COMMON_FIELDS + TYPE_FIELDS.get(record.get("record_type"), ())
    view = {k: record[k] for k in fields if record.get(k) not in (None, "", [], {})}
    card = record.get("reading_card")
    if card:
        view["reading_card"] = {"label": CARD_LABEL, "card": card}
    return view


def lexicon_flags(records: dict[str, dict]) -> dict:
    """The world's term records whose distortion_risk is high or medium, with their false-friend senses."""
    terms = [
        {"id": r["id"], "world_word": r.get("world_word"), "distortion_risk": r["distortion_risk"],
         "false_friend": r.get("false_friend") or [], "plain_meaning": r.get("plain_meaning")}
        for r in records.values() if r.get("record_type") == "term" and r.get("distortion_risk") in RISK_LEVELS
    ]
    terms.sort(key=lambda t: t["id"])
    if not terms:
        return {"terms": [], "note": "No term record of this world carries a distortion_risk of high or medium."}
    return {"terms": terms, "note": "From the distortion_risk and false_friend fields of the world's term records."}


class Context:
    """Per-world records, flags and per-probe questions, read once."""

    def __init__(self):
        self._records: dict[str, dict] = {}
        self._questions: dict[str, str] = {}

    def records(self, world: str) -> dict:
        if world not in self._records:
            self._records[world] = _load_records(world)
        return self._records[world]

    def question(self, probe_id: str) -> str:
        if probe_id not in self._questions:
            self._questions[probe_id] = read_question(probe_id)
        return self._questions[probe_id]

    def cited(self, world: str, ids: list[str], cap: int = v7_passages.DIVISION_MAX_WORDS) -> dict:
        records = self.records(world)
        out = {"views": [], "passages": [], "unresolved": [], "missing": []}
        for rid in ids:
            if rid not in records:
                out["missing"].append(rid)
                continue
            out["views"].append(_record_view(records[rid]))
            got = v7_passages.resolve_record(records[rid], records, TEXTS_ROOT, cap)
            out["passages"].extend(got["passages"])
            out["unresolved"].extend(got["unresolved"])
        return out


def _passage_view(p: dict) -> dict:
    return {k: p[k] for k in ("record_id", "source_id", "locus", "file", "division_path", "lines", "trimmed", "text")}


def build_request(item: dict, reader: str, ctx: Context, rubric: str) -> dict:
    cited = ctx.cited(item["world"], item["citations"])
    request = {
        "item_id": item["id"], "kind": "blind", "reader": reader, "world": item["world"],
        "instructions": INSTRUCTIONS, "rubric": rubric, "reply_format": REPLY_SCHEMA,
        "question": ctx.question(item["probe_id"]), "answer": item["answer"],
        "cited_records": cited["views"], "source_passages": [_passage_view(p) for p in cited["passages"]],
        "source_passages_note": PASSAGE_NOTE, "lexicon_risk_flags": lexicon_flags(ctx.records(item["world"])),
    }
    if cited["unresolved"]:
        request["source_passages_unresolved"] = cited["unresolved"]
    if cited["missing"]:
        request["cited_records_not_found"] = cited["missing"]
    return request


def _request_path(out: Path, label: str, item: str) -> Path:
    return out / "requests" / label / f"{item}.json"


def _reply_path(out: Path, label: str, item: str) -> Path:
    return out / "replies" / label / f"{item}.json"


def read_set_answers(set_dir: Path, world: str) -> list[dict]:
    path = set_dir / f"A_{world}.jsonl"
    items = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        rec = json.loads(line)
        items.append({"world": rec["world"], "arm": "a", "run": 1, "probe_id": rec["probe_id"], "cell": rec["cell"],
                      "answer": rec["answer_text"], "citations": list(rec.get("citations") or [])})
    return items


def read_run_answers(path: Path, run: int, arm: str = "b") -> tuple[list[dict], int]:
    """The answered records of one v7_run --out file, and the count skipped for an error or no text."""
    items, skipped = [], 0
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        rec = json.loads(line)
        if rec.get("error") or not rec.get("answer_text"):
            skipped += 1
            continue
        items.append({"world": rec["world"], "arm": arm, "run": run, "probe_id": rec["probe_id"], "cell": rec["cell"],
                      "answer": rec["answer_text"], "citations": list(rec.get("citations") or [])})
    return items, skipped


def collect_items(set_dir: Path, worlds: list[str], b_files: list[Path]) -> tuple[list[dict], int]:
    items = [i for w in worlds for i in read_set_answers(set_dir, w)]
    skipped = 0
    for run, path in enumerate(b_files, start=1):
        got, skip = read_run_answers(path, run)
        items.extend(i for i in got if i["world"] in worlds)
        skipped += skip
    keys = [item_key(i["world"], i["arm"], i["run"], i["probe_id"]) for i in items]
    if len(set(keys)) != len(keys):
        raise Refused("two answers share a world, arm, run and probe")
    return items, skipped


def _assign_ids(items: list[dict], seed: int) -> None:
    seen = {}
    for i in items:
        i["key"] = item_key(i["world"], i["arm"], i["run"], i["probe_id"])
        i["id"] = item_id(seed, i["key"])
        if i["id"] in seen:
            raise Refused("two items hash to the same id; choose another seed")
        seen[i["id"]] = i["key"]


def _manifest(out: Path, seed: int, item_ids: list[str]) -> dict:
    return {
        "run_one_item_per_fresh_context": True,
        "items": {
            iid: {r: {"request": str(_request_path(out, r, iid)), "reply": str(_reply_path(out, r, iid))} for r in READERS}
            for iid in sorted(item_ids)
        },
        "order": {r: shuffled(item_ids, seed, r) for r in READERS},
    }


def _fresh_dir(path: Path) -> None:
    require_outside_repo(path)
    if path.exists() and any(path.iterdir()):
        raise Refused(f"{path} is not empty")
    path.mkdir(parents=True, exist_ok=True)


def cmd_export(args) -> int:
    out, key_dir = Path(args.out), Path(args.key_dir)
    require_outside_repo(key_dir)
    _require_apart(out, key_dir)
    _fresh_dir(out)
    key_dir.mkdir(parents=True, exist_ok=True)
    if (key_dir / "key.json").exists():
        raise Refused(f"{key_dir} already holds a key")
    write_seed(key_dir, args.seed)
    worlds = args.worlds.split(",")
    items, skipped = collect_items(Path(args.set_dir), worlds, [Path(p) for p in args.b])
    _assign_ids(items, args.seed)
    ctx, rubric = Context(), rubric_text()
    for item in items:
        for reader in READERS:
            _write_json(_request_path(out, reader, item["id"]), build_request(item, reader, ctx, rubric))
    for reader in READERS:
        (out / "replies" / reader).mkdir(parents=True, exist_ok=True)
    _write_json(out / "reply_schema.json", REPLY_SCHEMA)
    key = {"items": {i["id"]: {k: i[k] for k in ("key", "world", "arm", "run", "probe_id", "cell")} for i in items}}
    _write_json(key_dir / "key.json", key)
    _write_json(out / "manifest.json", _manifest(out, args.seed, [i["id"] for i in items]))
    print(json.dumps({"items": len(items), "requests": len(items) * len(READERS), "skipped_b_records": skipped,
                      "key_sha256": _sha256(key_dir / "key.json")}, indent=1))
    flagless = sorted(w for w in worlds if not lexicon_flags(ctx.records(w))["terms"])
    if flagless:
        print(f"no lexicon risk flags for: {', '.join(flagless)}", file=sys.stderr)
    return 0


def accepted_error_types(defect_type: str) -> set[str]:
    return DEFECT_TYPES.get(re.sub(r"[\s-]+", "_", defect_type.strip().lower()), set())


def cmd_seed_copies(args) -> int:
    out, key_dir = Path(args.export_dir), Path(args.key_dir)
    require_outside_repo(out)
    require_outside_repo(key_dir)
    _require_apart(out, key_dir)
    seed_key_path = key_dir / "seed_key.json"
    if seed_key_path.exists():
        raise Refused("this export already has a seed key")
    seed = read_seed(key_dir)
    key = _read_json(key_dir / "key.json")
    manifest = _read_json(out / "manifest.json")
    by_key = {v["key"]: iid for iid, v in key["items"].items()}
    copies = _read_json(Path(args.copies))
    if len(copies) < MIN_SEEDED:
        raise Refused(f"{len(copies)} seeded copies; at least {MIN_SEEDED} are needed")
    sealed, new_ids = {}, []
    for n, copy in enumerate(copies):
        for field in ("base", "answer_text", "defect_type", "expected_location"):
            if not str(copy.get(field) or "").strip():
                raise Refused(f"seeded copy {n} has no {field}")
        if not accepted_error_types(copy["defect_type"]):
            raise Refused(f"seeded copy {n}: defect type {copy['defect_type']!r} is not one of {sorted(DEFECT_TYPES)}")
        if copy["base"] not in by_key:
            raise Refused(f"seeded copy {n}: base {copy['base']!r} is not an item of this export")
        iid = item_id(seed, f"seeded|{n}|{copy['base']}")
        if iid in key["items"] or iid in sealed:
            raise Refused("a seeded id collides with another id")
        for reader in READERS:
            request = _read_json(_request_path(out, reader, by_key[copy["base"]]))
            request["item_id"], request["answer"] = iid, copy["answer_text"]
            _write_json(_request_path(out, reader, iid), request)
        sealed[iid] = {"base": copy["base"], "defect_type": copy["defect_type"], "expected_location": copy["expected_location"],
                       "answer_text": copy["answer_text"]}
        new_ids.append(iid)
    for reader in READERS:
        (out / "replies" / reader).mkdir(parents=True, exist_ok=True)
    _write_json(out / "manifest.json", _manifest(out, seed, list(manifest["items"]) + new_ids))
    _write_json(seed_key_path, {"items": sealed})
    print(json.dumps({"seeded": len(new_ids), "seed_key_sha256": _sha256(seed_key_path)}, indent=1))
    return 0


def validate_reply(reply, item: str, reader: str) -> list[str]:
    """The reasons a blind or adjudication reply does not fit the reply format; empty when it fits."""
    if not isinstance(reply, dict):
        return ["not an object"]
    problems = []
    if reply.get("item_id") != item:
        problems.append("item_id does not match")
    if reply.get("reader") != reader:
        problems.append("reader does not match")
    scores = reply.get("scores")
    if not isinstance(scores, dict):
        problems.append("scores missing")
    else:
        for d in DIMENSIONS:
            s = scores.get(d)
            if not isinstance(s, dict) or s.get("score") not in (0, 1, 2) or isinstance(s.get("score"), bool):
                problems.append(f"score for {d} is not 0, 1 or 2")
            elif not str(s.get("reason") or "").strip():
                problems.append(f"reason for {d} missing")
    if reply.get("depth") not in DEPTHS:
        problems.append("depth is not one of rich, adequate, thin, flat")
    problems.extend(_error_problems(reply.get("errors"), "errors"))
    return problems


def _error_problems(errors, label: str) -> list[str]:
    if not isinstance(errors, list):
        return [f"{label} is not a list"]
    problems = []
    for n, e in enumerate(errors):
        if not isinstance(e, dict):
            problems.append(f"{label}[{n}] is not an object")
            continue
        for f in ("answer_words", "source_words", "evidence"):
            if not isinstance(e.get(f), str):
                problems.append(f"{label}[{n}].{f} missing")
        if not str(e.get("type") or "").split(":")[0].strip() in ERROR_TYPES:
            problems.append(f"{label}[{n}].type is not a listed type")
        if e.get("tier") not in TIERS or isinstance(e.get("tier"), bool):
            problems.append(f"{label}[{n}].tier is not 1, 2 or 3")
        if e.get("confidence") not in CONFIDENCES:
            problems.append(f"{label}[{n}].confidence is not sure, fairly sure or unsure")
    return problems


def _base_type(error: dict) -> str:
    return str(error["type"]).split(":")[0]


def _unmatched(errors: list[dict], others: list[dict]) -> bool:
    return any(not any(overlaps(e["answer_words"], o["answer_words"]) and _base_type(e) == _base_type(o) for o in others) for e in errors)


def needs_adjudication(first: dict, second: dict) -> bool:
    """True when any dimension score differs, either reader's error has no overlapping error from the other at any tier,
    or either found a tier 1 or 2 error."""
    if any(first["scores"][d]["score"] != second["scores"][d]["score"] for d in DIMENSIONS):
        return True
    if _unmatched(first["errors"], second["errors"]) or _unmatched(second["errors"], first["errors"]):
        return True
    return any(e["tier"] in (1, 2) for r in (first, second) for e in r["errors"])


def _load_reply(out: Path, label: str, item: str, problems: list | None = None):
    path = _reply_path(out, label, item)
    if not path.exists():
        return None
    try:
        reply = _read_json(path)
    except ValueError:
        reply = None
    found = validate_reply(reply, item, label) if reply is not None else ["not valid JSON"]
    if found:
        if problems is not None:
            problems.append({"item_id": item, "reader": label, "problems": found})
        return None
    return reply


def cmd_adjudicate(args) -> int:
    out = Path(args.export_dir)
    require_outside_repo(out)
    manifest = _read_json(out / "manifest.json")
    problems, waiting, written = [], [], []
    for iid in sorted(manifest["items"]):
        first, second = (_load_reply(out, r, iid, problems) for r in READERS)
        if first is None or second is None:
            waiting.append(iid)
            continue
        if not needs_adjudication(first, second):
            continue
        request = _read_json(_request_path(out, READERS[0], iid))
        request.update({
            "kind": "adjudication", "reader": ADJUDICATOR,
            "instructions": INSTRUCTIONS + " Two readers have already read this answer. Rule on every disagreement and on every tier 1 or 2 finding.",
            "reader_findings": [{"reader": "first reader", **_findings(first)}, {"reader": "second reader", **_findings(second)}],
        })
        _write_json(_request_path(out, ADJUDICATOR, iid), request)
        written.append(iid)
    (out / "replies" / ADJUDICATOR).mkdir(parents=True, exist_ok=True)
    listing = {iid: {"request": str(_request_path(out, ADJUDICATOR, iid)), "reply": str(_reply_path(out, ADJUDICATOR, iid))}
               for iid in written}
    _write_json(out / "adjudication_manifest.json", {"run_one_item_per_fresh_context": True, "items": listing,
                                                      "waiting_for_readers": waiting, "invalid_replies": problems})
    print(json.dumps({"adjudication_requests": len(written), "waiting_for_readers": len(waiting), "invalid_replies": len(problems)}, indent=1))
    return 0


def _findings(reply: dict) -> dict:
    return {"scores": reply["scores"], "depth": reply["depth"], "errors": reply["errors"]}


def october_entry(set_dir: Path, world: str, probe_id: str) -> dict:
    reviews = _read_json(set_dir / f"A_reviews_{world}.json")
    return {
        "second_pass": reviews["second_pass"]["by_probe"].get(probe_id),
        "outside_referee": reviews["outside_referees"]["by_probe"].get(probe_id),
    }


def cmd_after_october(args) -> int:
    out, key_dir = Path(args.export_dir), Path(args.key_dir)
    require_outside_repo(out)
    require_outside_repo(key_dir)
    key = _read_json(key_dir / "key.json")
    manifest = _read_json(out / "manifest.json")
    seeded = _read_json(key_dir / "seed_key.json")["items"] if (key_dir / "seed_key.json").exists() else {}
    problems, held_back, listing = [], {}, {}
    for reader in READERS:
        filed = {iid: _load_reply(out, reader, iid, problems) for iid in manifest["items"]}
        missing = sorted(iid for iid, reply in filed.items() if reply is None)
        if missing:
            held_back[reader] = len(missing)
            continue
        for iid, meta in sorted(key["items"].items()):
            if meta["arm"] != "a" or meta["run"] != 1 or iid in seeded:
                continue
            request = _read_json(_request_path(out, reader, iid))
            request.update({
                "kind": "after_october",
                "instructions": ("Your scores are filed. Below are the October second-pass grades and outside-referee findings for this "
                                 "answer. You may add errors you missed. Mark each one after_october_review: true. Reply with one JSON "
                                 "object in the reply format."),
                "reply_format": AFTER_OCTOBER_SCHEMA, "your_filed_reply": _findings(filed[iid]),
                "october_review": october_entry(Path(args.set_dir), meta["world"], meta["probe_id"]),
            })
            path = out / "requests" / "after-october" / reader / f"{iid}.json"
            _write_json(path, request)
            listing[f"{reader}/{iid}"] = {"request": str(path), "reply": str(out / "replies" / "after-october" / reader / f"{iid}.json")}
    _write_json(out / "after_october_manifest.json", {"run_one_item_per_fresh_context": True, "items": listing,
                                                       "readers_held_back_missing_blind_replies": held_back, "invalid_replies": problems})
    print(json.dumps({"after_october_requests": len(listing), "readers_held_back": held_back}, indent=1))
    return 0


def agreement(pairs: list[tuple[int, int]]) -> dict:
    """Exact and within-one agreement over pairs of scores."""
    n = len(pairs)
    if not n:
        return {"n": 0, "exact": None, "within_one": None}
    return {"n": n, "exact": sum(a == b for a, b in pairs) / n, "within_one": sum(abs(a - b) <= 1 for a, b in pairs) / n}


def distribution(values: list[float]) -> dict:
    return {str(v): sum(1 for x in values if x == v) for v in (0, 1, 2)}


def _summary(values: list[float]) -> dict:
    return {"n": len(values), "mean": round(statistics.fmean(values), 3) if values else None, "distribution": distribution(values)}


def _final_errors(first: dict, second: dict, adjudicated: dict | None) -> list[dict]:
    merged = []
    for e in (adjudicated["errors"] if adjudicated is not None else first["errors"] + second["errors"]):
        if not any(overlaps(e["answer_words"], m["answer_words"]) for m in merged):
            merged.append(e)
    return merged


def catches(reply: dict, planted: dict) -> bool:
    """True when one of the reader's errors has the planted defect's type and quotes at least SPAN_THRESHOLD of the planted span's words."""
    wanted = accepted_error_types(planted["defect_type"])
    return any(str(e["type"]).split(":")[0] in wanted and containment(planted["expected_location"], e["answer_words"]) >= SPAN_THRESHOLD
               for e in reply["errors"])


def seeded_catch(seeded: dict, replies: dict) -> dict:
    """Per reader, the share of seeded copies whose planted defect one of that reader's errors catches."""
    result = {"seeded": len(seeded), "by_reader": {}, "missing": []}
    for r in READERS:
        caught = sum(1 for iid, s in seeded.items() if replies[r].get(iid) and catches(replies[r][iid], s))
        read = sum(1 for iid in seeded if replies[r].get(iid))
        result["by_reader"][r] = {"read": read, "caught": caught, "rate": caught / len(seeded) if seeded else None}
    result["missing"] = sorted(iid for iid in seeded if any(not replies[r].get(iid) for r in READERS))
    result["found_by_either"] = sum(1 for iid, s in seeded.items() if any(replies[r].get(iid) and catches(replies[r][iid], s) for r in READERS))
    return result


def catch_gate(catch: dict) -> dict:
    """Scores count only when both readers have read every seeded copy, there are at least MIN_SEEDED, and each caught at least 9 in 10."""
    reasons = []
    if catch["seeded"] < MIN_SEEDED:
        reasons.append(f"only {catch['seeded']} seeded copies; at least {MIN_SEEDED} are needed")
    if catch["missing"]:
        reasons.append(f"{len(catch['missing'])} seeded copies are not read by both readers yet")
    for r, v in catch["by_reader"].items():
        if v["rate"] is None or v["rate"] < CATCH_RATE_FLOOR:
            reasons.append(f"{r} caught {v['caught']} of {catch['seeded']}, below {int(CATCH_RATE_FLOOR * 100)}%")
    return {"scores_count": not reasons, "reasons": reasons}


def _fragments(note: str) -> list[str]:
    return [next(g for g in m if g) for m in QUOTED_FRAGMENT.findall(note or "")]


def known_october_errors(set_dir: Path, world: str) -> list[dict]:
    """Every October finding on A that may be an error: each outside-referee doubted claim, and each second-pass rigor note for a
    non-SOUND answer and craft note for an answer not marked SHIP. `match_text` is the words a B finding is matched against; it is
    empty for a second-pass note that quotes no answer words."""
    reviews = _read_json(set_dir / f"A_reviews_{world}.json")
    known = []
    for probe, entry in sorted(reviews["outside_referees"]["by_probe"].items()):
        for d in entry.get("doubted_claims") or []:
            known.append({"world": world, "probe_id": probe, "source": "outside referee", "claim": d["claim"], "problem": d["problem"],
                          "match_text": [d["claim"]],
                          "may_be_confirmation": d["problem"].strip().lower().startswith(CONFIRMING_PREFIXES)})
    for probe, entry in sorted(reviews["second_pass"]["by_probe"].items()):
        notes = []
        if entry.get("rigor") != "SOUND" and entry.get("rigor_note"):
            notes.append(("rigor", entry["rigor_note"]))
        if entry.get("overall") != "SHIP" and entry.get("craft_note"):
            notes.append(("craft", entry["craft_note"]))
        for kind, note in notes:
            known.append({"world": world, "probe_id": probe, "source": f"second pass {kind}", "claim": note, "problem": note,
                          "match_text": _fragments(note), "may_be_confirmation": False})
    return known


def _load_all(out: Path, key_dir: Path) -> dict:
    key = _read_json(key_dir / "key.json")
    seeded = _read_json(key_dir / "seed_key.json")["items"] if (key_dir / "seed_key.json").exists() else {}
    manifest = _read_json(out / "manifest.json")
    problems = []
    replies = {r: {} for r in READERS}
    for r in READERS:
        for iid in manifest["items"]:
            got = _load_reply(out, r, iid, problems)
            if got is not None:
                replies[r][iid] = got
    adjudicated = {}
    for iid in manifest["items"]:
        got = _load_reply(out, ADJUDICATOR, iid, problems)
        if got is not None:
            adjudicated[iid] = got
    after = {}
    for r in READERS:
        folder = out / "replies" / "after-october" / r
        for path in sorted(folder.glob("*.json")) if folder.exists() else []:
            try:
                reply = _read_json(path)
            except ValueError:
                problems.append({"item_id": path.stem, "reader": r, "problems": ["after-october reply is not valid JSON"]})
                continue
            found = _error_problems(reply.get("added_errors") if isinstance(reply, dict) else None, "added_errors")
            if found:
                problems.append({"item_id": path.stem, "reader": r, "problems": found})
                continue
            after.setdefault(path.stem, []).extend(reply["added_errors"])
    return {"key": key, "seeded": seeded, "manifest": manifest, "replies": replies, "adjudicated": adjudicated, "after": after,
            "problems": problems}


def final_values(first: dict, second: dict, adjudicated: dict | None) -> dict | None:
    """Per dimension, the adjudicated score where one exists, else the readers' common score; None when they differ and no ruling exists."""
    values = {}
    for d in DIMENSIONS:
        if adjudicated is not None:
            values[d] = adjudicated["scores"][d]["score"]
        elif first["scores"][d]["score"] == second["scores"][d]["score"]:
            values[d] = first["scores"][d]["score"]
        else:
            return None
    return values


def deterministic_measures(answer: str, cited_ids: list[str]) -> dict:
    """Word count, sentence count, cited records and cited quote records of one answer."""
    sentences = [s for s in re.split(r"(?<=[.!?])\s+", answer.strip()) if s]
    return {"words": len(answer.split()), "sentences": len(sentences), "cited_records": len(set(cited_ids)),
            "cited_quotes": len({c for c in cited_ids if ".quote." in c})}


def _mean_measures(rows: list[dict]) -> dict:
    return {k: round(statistics.fmean(r[k] for r in rows), 2) for k in ("words", "sentences", "cited_records", "cited_quotes")} if rows else {}


def older_engine_band(band_dir: Path, worlds: list[str]) -> dict:
    """Per world, the mean of each deterministic measure for each older-engine run (r1 to r3), its spread across runs and its
    check pass rate. The older-engine answers are not read by the readers."""
    band = {}
    for world in worlds:
        runs = {}
        for path in sorted(band_dir.glob(f"live-admission-report-baseline-r*-{world}-*.json")):
            run = re.search(r"baseline-(r\d+)-", path.name).group(1)
            probes = _read_json(path)["worlds"][world]["per_probe"]
            rows = [deterministic_measures(p["transcript"]["answer_text"], p["transcript"].get("citations") or []) for p in probes]
            runs[run] = {"n": len(rows), **_mean_measures(rows), "check_pass_rate": round(sum(bool(p.get("passed")) for p in probes) / len(probes), 3)}
        if runs:
            spread = {k: {"min": min(r[k] for r in runs.values()), "max": max(r[k] for r in runs.values())}
                      for k in ("words", "sentences", "cited_records", "cited_quotes")}
            band[world] = {"runs": runs, "spread": spread}
    return band


def _by_world_arm(out: Path, key_items: dict) -> dict:
    rows = {}
    for iid, m in key_items.items():
        if m["run"] != 1:
            continue
        req = _read_json(_request_path(out, READERS[0], iid))
        measure = deterministic_measures(req["answer"], [r["id"] for r in req["cited_records"]])
        rows.setdefault(m["world"], {}).setdefault(m["arm"], []).append(measure)
    return {w: {arm: {"n": len(v), **_mean_measures(v)} for arm, v in arms.items()} for w, arms in rows.items()}


def _bump(table: dict, *path) -> None:
    for step in path[:-1]:
        table = table.setdefault(step, {})
    table[path[-1]] = table.get(path[-1], 0) + 1


def compute_tables(out: Path, key_dir: Path, set_dir: Path, band_dir: Path | None = None) -> dict:
    data = _load_all(out, key_dir)
    key_items, seeded = data["key"]["items"], data["seeded"]
    r1, r2, adj = data["replies"][READERS[0]], data["replies"][READERS[1]], data["adjudicated"]
    final, awaiting, depth_by, errors_by = {}, [], {}, {}
    for iid in key_items:
        if iid not in r1 or iid not in r2:
            continue
        values = final_values(r1[iid], r2[iid], adj.get(iid))
        if values is None:
            awaiting.append(iid)
            continue
        final[iid] = values
        a = adj.get(iid)
        depth_by[iid] = a["depth"] if a else (r1[iid]["depth"] if r1[iid]["depth"] == r2[iid]["depth"] else "split")
        errors_by[iid] = _final_errors(r1[iid], r2[iid], a)

    cells = {}
    for iid in final:
        m = key_items[iid]
        if m["run"] == 1:
            for world in (m["world"], "all"):
                cells.setdefault((m["arm"], world), []).append(iid)
    scores = {d: {} for d in DIMENSIONS}
    depth = {}
    for (arm, world), ids in sorted(cells.items()):
        for d in DIMENSIONS:
            scores[d].setdefault(arm, {})[world] = _summary([final[i][d] for i in ids])
        depth.setdefault(arm, {})[world] = {k: sum(1 for i in ids if depth_by[i] == k) for k in (*DEPTHS, "split")}

    by_probe_b = {}
    for iid, m in key_items.items():
        if m["arm"] == "b" and iid in final:
            by_probe_b.setdefault((m["world"], m["probe_id"]), {})[m["run"]] = iid
    repeats = [v for v in by_probe_b.values() if 1 in v and 2 in v]
    noise = {}
    for d in DIMENSIONS:
        pairs = [(final[v[1]][d], final[v[2]][d]) for v in repeats]
        noise[d] = {**agreement(pairs), "mean_abs_difference": round(statistics.fmean(abs(a - b) for a, b in pairs), 3) if pairs else None}

    both = [i for i in key_items if i in r1 and i in r2]
    reader_agreement = {}
    for d in DIMENSIONS:
        stat = agreement([(r1[i]["scores"][d]["score"], r2[i]["scores"][d]["score"]) for i in both])
        stat["readers_unreliable_here"] = stat["exact"] is not None and stat["exact"] < EXACT_AGREEMENT_FLOOR
        reader_agreement[d] = stat

    error_counts, after_counts = {}, {}
    for iid, errs in errors_by.items():
        m = key_items[iid]
        if m["run"] == 1:
            for e in errs:
                for world in (m["world"], "all"):
                    _bump(error_counts, world, m["arm"], str(e["type"]).split(":")[0], str(e["tier"]))
    for iid, errs in data["after"].items():
        m = key_items.get(iid)
        if m is None:
            continue
        for e in errs:
            for world in (m["world"], "all"):
                _bump(after_counts, world, m["arm"], str(e["type"]).split(":")[0], str(e["tier"]))

    if seeded:
        catch = seeded_catch(seeded, data["replies"])
    else:
        catch = {"seeded": 0, "by_reader": {r: {"read": 0, "caught": 0, "rate": None} for r in READERS}, "missing": [], "found_by_either": 0}
    gate = catch_gate(catch)

    worlds = sorted({m["world"] for m in key_items.values()})
    october, comparison_rows = [], []
    b_run1 = {(m["world"], m["probe_id"]): iid for iid, m in key_items.items() if m["arm"] == "b" and m["run"] == 1}
    for world in worlds:
        if not (set_dir / f"A_reviews_{world}.json").exists():
            continue
        reviews = _read_json(set_dir / f"A_reviews_{world}.json")["second_pass"]["by_probe"]
        for iid, m in key_items.items():
            if m["world"] == world and m["arm"] == "a" and m["run"] == 1 and iid in final and m["probe_id"] in reviews:
                grades = reviews[m["probe_id"]]
                comparison_rows.append({
                    "world": world, "probe_id": m["probe_id"], "rigor": grades.get("rigor"), "readable": grades.get("readable"),
                    "understandable": grades.get("understandable"),
                    "fresh_dims_1_to_3": round(statistics.fmean(final[iid][d] for d in RIGOR_DIMENSIONS), 3),
                    "fresh_dim_10": final[iid][ACCESS_DIMENSION],
                })
        for known in known_october_errors(set_dir, world):
            iid = b_run1.get((world, known["probe_id"]))
            if iid is None or iid not in errors_by:
                status, in_text = "not read in B", None
            else:
                answer = _read_json(_request_path(out, READERS[0], iid))["answer"]
                in_text = any(containment(f, answer) >= 0.6 for f in known["match_text"]) if known["match_text"] else None
                if not known["match_text"]:
                    status = "unmatched (for V10)"
                elif any(overlaps(e["answer_words"], f) for e in errors_by[iid] for f in known["match_text"]):
                    status = "candidate repeated"
                else:
                    status = "no candidate found"
            october.append({**known, "b_status": status, "claim_wording_in_b_answer": in_text})
    comparison = {}
    for column, dim in (("rigor", "fresh_dims_1_to_3"), ("readable", "fresh_dim_10"), ("understandable", "fresh_dim_10")):
        grouped = {}
        for row in comparison_rows:
            grouped.setdefault(str(row[column]), []).append(row[dim])
        comparison[column] = {g: {"n": len(v), "mean_fresh": round(statistics.fmean(v), 3)} for g, v in sorted(grouped.items())}

    band = older_engine_band(band_dir, worlds) if band_dir is not None and band_dir.exists() else {}
    return {
        "scores": scores, "depth": depth, "noise_floor": {"repeat_probes": len(repeats), "by_dimension": noise},
        "reader_agreement": reader_agreement, "error_counts": error_counts, "after_october_error_counts": after_counts,
        "seeded_catch": catch, "gate": gate, "october_errors": october,
        "october_comparison": {"by_grade": comparison, "rows": comparison_rows},
        "older_engine_band": {"note": "Deterministic measures only. The older-engine answers were not read by the readers.",
                              "by_world": band, "current_arms_by_world": _by_world_arm(out, {i: m for i, m in key_items.items() if i in r1})},
        "awaiting_adjudication": sorted(awaiting), "invalid_replies": data["problems"], "items_scored": len(final),
    }


def _pct(x) -> str:
    return "-" if x is None else f"{round(x * 100)}%"


def _error_table(lines: list[str], counts: dict) -> None:
    if not counts:
        lines += ["None.", ""]
        return
    lines += ["| World | Arm | Type | Tier 1 | Tier 2 | Tier 3 |", "|---|---|---|---|---|---|"]
    for world in sorted(counts):
        for arm in sorted(counts[world]):
            for typ in sorted(counts[world][arm]):
                lines.append(f"| {world} | {arm} | {typ} | " + " | ".join(str(counts[world][arm][typ].get(k, 0)) for k in "123") + " |")
    lines.append("")


def render_markdown(t: dict) -> str:
    lines = ["# V7 reader scores", ""]
    if not t["gate"]["scores_count"]:
        lines += ["**SCORES DO NOT COUNT.**", "The seeded catch rate is below the line. The reader instructions must be fixed and the reading redone.", ""]
        lines += [f"- {r}" for r in t["gate"]["reasons"]] + [""]
    lines += [f"Items scored: {t['items_scored']}. Items awaiting a ruling: {len(t['awaiting_adjudication'])}. "
              f"Replies that did not fit the format: {len(t['invalid_replies'])}.", ""]
    lines += ["## Scores per dimension", "", "Each cell is the mean over n answers. Adjudicated values are used where a ruling exists.", ""]
    worlds = sorted({w for d in t["scores"].values() for arm in d.values() for w in arm})
    lines += ["| Dimension | Arm | " + " | ".join(worlds) + " |", "|---|---|" + "---|" * len(worlds)]
    for d, arms in t["scores"].items():
        for arm in sorted(arms):
            lines.append(f"| {d} | {arm} | " + " | ".join(
                f"{arms[arm][w]['mean']} (n={arms[arm][w]['n']}; 0/1/2 = {'/'.join(str(arms[arm][w]['distribution'][k]) for k in '012')})"
                if w in arms[arm] else "-" for w in worlds) + " |")
    lines += ["", "## B noise floor", "", f"Run 1 against run 2 on {t['noise_floor']['repeat_probes']} repeat probes.", "",
              "| Dimension | n | Exact | Within one | Mean difference |", "|---|---|---|---|---|"]
    for d, s in t["noise_floor"]["by_dimension"].items():
        lines.append(f"| {d} | {s['n']} | {_pct(s['exact'])} | {_pct(s['within_one'])} | {s['mean_abs_difference']} |")
    lines += ["", "## Reader agreement", "", f"A dimension with exact agreement under {int(EXACT_AGREEMENT_FLOOR * 100)}% is marked unreliable.", "",
              "| Dimension | n | Exact | Within one | Note |", "|---|---|---|---|---|"]
    for d, s in t["reader_agreement"].items():
        lines.append(f"| {d} | {s['n']} | {_pct(s['exact'])} | {_pct(s['within_one'])} | {'readers unreliable here' if s['readers_unreliable_here'] else ''} |")
    lines += ["", "## Errors by world, type and tier", "", "Blind reading:", ""]
    _error_table(lines, t["error_counts"])
    lines += ["Added after October review:", ""]
    _error_table(lines, t["after_october_error_counts"])
    c = t["seeded_catch"]
    lines += ["## Seeded catch rate", "", f"Seeded copies: {c['seeded']}. A catch needs the planted defect type and at least half of the planted span's words "
              f"inside the reader's quoted words. Scores count only if each reader catches at least 9 in 10.", ""]
    for r, v in c["by_reader"].items():
        lines.append(f"- {r}: caught {v['caught']} of {c['seeded']} (read {v['read']}).")
    lines += [f"- Found by at least one reader: {c['found_by_either']}.", ""]
    lines += ["## Fresh scores against the October grades on A", "", "Dimensions 1 to 3 against the October rigor grade. Dimension 10 against the readable and understandable grades.", "",
              "| October column | Grade | n | Mean fresh score |", "|---|---|---|---|"]
    for column, grades in t["october_comparison"]["by_grade"].items():
        for grade, s in grades.items():
            lines.append(f"| {column} | {grade} | {s['n']} | {s['mean_fresh']} |")
    band = t["older_engine_band"]
    lines += ["", "## Older-engine band", "", band["note"], "",
              "| World | Run | Words | Sentences | Cited records | Cited quotes | Check pass rate |", "|---|---|---|---|---|---|---|"]
    for world, b in sorted(band["by_world"].items()):
        for run, m in b["runs"].items():
            lines.append(f"| {world} | older {run} | {m['words']} | {m['sentences']} | {m['cited_records']} | {m['cited_quotes']} | {_pct(m['check_pass_rate'])} |")
        for arm, m in sorted(band["current_arms_by_world"].get(world, {}).items()):
            lines.append(f"| {world} | arm {arm} | {m['words']} | {m['sentences']} | {m['cited_records']} | {m['cited_quotes']} | - |")
    lines += ["", "## Known October errors in A, against B", "",
              "Each row is a mechanical candidate match. A person must confirm it in V10. 'No candidate found' does not mean B avoided the error.", "",
              "| World | Probe | Source | B | Wording in B answer | May be a confirmation |", "|---|---|---|---|---|---|"]
    for e in t["october_errors"]:
        lines.append(f"| {e['world']} | {e['probe_id']} | {e['source']} | {e['b_status']} | {e['claim_wording_in_b_answer']} | {e['may_be_confirmation']} |")
    return "\n".join(lines) + "\n"


def cmd_score(args) -> int:
    out, tables = Path(args.export_dir), Path(args.tables_dir)
    t = compute_tables(out, Path(args.key_dir), Path(args.set_dir), Path(args.band_dir))
    tables.mkdir(parents=True, exist_ok=True)
    _write_json(tables / "tables.json", t)
    (tables / "tables.md").write_text(render_markdown(t), encoding="utf-8")
    print(json.dumps({"items_scored": t["items_scored"], "scores_count": t["gate"]["scores_count"],
                      "awaiting_adjudication": len(t["awaiting_adjudication"])}, indent=1))
    return 0


def pick_probes(candidates: list[dict], count: int, seed: int, world: str) -> list[dict]:
    """A seeded weighted draw without replacement; quote-placing answers and T or E registers weigh more."""
    rng = random.Random(f"{seed}|mark|{world}")
    scored = []
    for c in sorted(candidates, key=lambda c: c["probe_id"]):
        weight = 1.0 + (2.0 if c["places_quote"] else 0.0) + (1.0 if register_of(c["cell"]) in ("T", "E") else 0.0)
        scored.append((rng.random() ** (1.0 / weight), c))
    scored.sort(key=lambda s: -s[0])
    return [c for _, c in scored[:count]]


def cmd_mark_pack(args) -> int:
    out, key_dir = Path(args.out), Path(args.key_dir)
    require_outside_repo(key_dir)
    _require_apart(out, key_dir)
    _fresh_dir(out)
    key_dir.mkdir(parents=True, exist_ok=True)
    write_seed(key_dir, args.seed)
    worlds = args.worlds.split(",")
    a_items = [i for w in worlds for i in read_set_answers(Path(args.set_dir), w)]
    b_items, _ = read_run_answers(Path(args.b), 1)
    a_by = {(i["world"], i["probe_id"]): i for i in a_items}
    b_by = {(i["world"], i["probe_id"]): i for i in b_items if i["world"] in worlds}
    ctx, items, key = Context(), [], {}
    for world in worlds:
        common = sorted(p for (w, p) in a_by if w == world and (w, p) in b_by)
        if len(common) < args.per_world:
            raise Refused(f"{world}: {len(common)} probes answered in both arms; {args.per_world} are needed")
        candidates = []
        for p in common:
            both = (a_by[(world, p)], b_by[(world, p)])
            candidates.append({"probe_id": p, "cell": both[0]["cell"],
                               "places_quote": any(".quote." in rid for i in both for rid in i["citations"])})
        for chosen in pick_probes(candidates, args.per_world, args.seed, world):
            for arm_item in (a_by[(world, chosen["probe_id"])], b_by[(world, chosen["probe_id"])]):
                k = item_key(world, arm_item["arm"], arm_item["run"], arm_item["probe_id"])
                iid = item_id(args.seed, f"mark|{k}")
                cited = ctx.cited(world, arm_item["citations"], MARK_PASSAGE_WORDS)
                items.append({"item_id": iid, "world": world, "question": ctx.question(chosen["probe_id"]),
                              "answer": arm_item["answer"], "cited_records": cited["views"],
                              "source_lines": [{k2: p[k2] for k2 in ("record_id", "division_path", "lines", "text")}
                                               for p in cited["passages"]]})
                key[iid] = {"key": k, "world": world, "arm": arm_item["arm"], "probe_id": chosen["probe_id"], "cell": chosen["cell"]}
    by_id = {i["item_id"]: i for i in items}
    order = shuffled(list(by_id), args.seed, "mark")
    _write_json(out / "mark_pack.json", {"items": [by_id[i] for i in order]})
    _write_json(key_dir / "mark_pack_key.json", {"items": key})
    print(json.dumps({"items": len(items), "per_world": args.per_world, "key_sha256": _sha256(key_dir / "mark_pack_key.json")}, indent=1))
    return 0


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    e = sub.add_parser("export", help="write the reader requests, the manifest and the key files")
    e.add_argument("--set-dir", default=str(SET_DIR))
    e.add_argument("--b", action="append", default=[], required=True, help="a v7_run --out file; the first is run 1, the next run 2")
    e.add_argument("--worlds", default=",".join(WORLDS))
    e.add_argument("--out", required=True)
    e.add_argument("--key-dir", required=True)
    e.add_argument("--seed", type=int, required=True)
    s = sub.add_parser("seed-copies", help="add seeded-defect copies to an export")
    s.add_argument("--export-dir", required=True)
    s.add_argument("--key-dir", required=True)
    s.add_argument("--copies", required=True)
    a = sub.add_parser("adjudicate", help="write the third-reader requests")
    a.add_argument("--export-dir", required=True)
    o = sub.add_parser("after-october", help="write the follow-up requests that show the October findings")
    o.add_argument("--export-dir", required=True)
    o.add_argument("--key-dir", required=True)
    o.add_argument("--set-dir", default=str(SET_DIR))
    c = sub.add_parser("score", help="write the score tables")
    c.add_argument("--export-dir", required=True)
    c.add_argument("--key-dir", required=True)
    c.add_argument("--set-dir", default=str(SET_DIR))
    c.add_argument("--band-dir", default=str(max(REPORTS_DIR.glob("baseline-*"), default=REPORTS_DIR)),
                   help="the older-engine baseline report folder")
    c.add_argument("--tables-dir", required=True)
    m = sub.add_parser("mark-pack", help="build the human review sample")
    m.add_argument("--set-dir", default=str(SET_DIR))
    m.add_argument("--b", required=True, help="the run 1 v7_run --out file")
    m.add_argument("--worlds", default=",".join(WORLDS))
    m.add_argument("--per-world", type=int, default=12)
    m.add_argument("--out", required=True)
    m.add_argument("--key-dir", required=True)
    m.add_argument("--seed", type=int, required=True)
    return parser


COMMANDS = {"export": cmd_export, "seed-copies": cmd_seed_copies, "adjudicate": cmd_adjudicate,
            "after-october": cmd_after_october, "score": cmd_score, "mark-pack": cmd_mark_pack}


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(sys.argv[1:] if argv is None else argv)
    try:
        return COMMANDS[args.command](args)
    except Refused as refusal:
        print(f"refused: {refusal}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
