"""S1-04: the judge trial in shadow. Two judges, different models, read each
gold item the way a production judge would (the sentence and its bound
records, nothing more) and are scored against the gold labels beside the
current gates' decisions on the same sentences.

  verifier               is the sentence supported by its bound records?
  citation-recall judge  is the sentence entailed by its citations taken
                         together, and which citations does it need?

Tuning (prompt changes) reads the calibration half only. The held-out half is
read here, by `score --half heldout`, once the judges are frozen; a run on the
held-out half records the judge prompts' hashes, so a later prompt change is
visible against it.

  python -m goldset.trial judge --judge verifier --model <id> --half calibration --out <verdicts.jsonl> --settings-only
  python -m goldset.trial score --half heldout --verdicts <v.jsonl> --verdicts <c.jsonl> --out <report.json>
"""
import argparse
import json
import random
import sys
import time
from collections import Counter
from pathlib import Path

from goldset.common import GOLD_DIR, read_jsonl, records_at, sha256_text
from goldset.evidence import record_block
from goldset.labeller import KEY_CLASSES, _JSON, gold_class
from goldset.split import CALIBRATION, HELDOUT

MAX_TOKENS = 400
EXPECTED_OUTPUT_TOKENS = 120
CHARS_PER_TOKEN = 3.5
REGION = "us-east-1"

JUDGE_PROMPTS = {
    "verifier": (
        "You check one sentence a historical Representative said against the records it was bound to. "
        "The Representative speaks as \"we\" for its own tradition. The sentence is supported only if every "
        "assertion in it is stated in the records or follows closely from them, with the same speaker and the "
        "same force: no dropped or added negation, no stronger modal or quantifier, no one author's view stated "
        "as the whole tradition's unless a record says it is, no outsider's or opponent's words given as the "
        "tradition's own, no word read in a modern sense the record warns against, no added detail.\n"
        'Reply with one JSON object only: {"supported": true or false, "reason": "one short sentence"}'
    ),
    "citation_recall": (
        "You are given a sentence and the records it cites, numbered. Decide whether the cited records, taken "
        "together, entail everything the sentence asserts (with the same speaker and the same force), and which "
        "records are needed for that. Use no outside knowledge.\n"
        'Reply with one JSON object only: {"entailed": true or false, "needed": [record numbers], "reason": "one short sentence"}'
    ),
}


def gold_path(half: str) -> Path:
    return GOLD_DIR / f"{half}.jsonl"


def judge_message(item: dict) -> str:
    records = records_at(item["records_commit"], item["world"])
    blocks = []
    for n, binding in enumerate(item["bindings"], start=1):
        record = records.get(binding["id"])
        blocks.append(f"[{n}] " + (record_block(record) if record else f"{binding['id']}: no such record"))
    return "RECORDS\n\n" + "\n\n".join(blocks) + f"\n\nSENTENCE\n{item['sentence']}"


def parse_judgement(judge: str, reply: str, bindings: int) -> dict | None:
    found = _JSON.search(reply or "")
    if not found:
        return None
    try:
        data = json.loads(found.group(0))
    except json.JSONDecodeError:
        return None
    key = "supported" if judge == "verifier" else "entailed"
    if not isinstance(data.get(key), bool):
        return None
    out = {"supported": data[key], "reason": str(data.get("reason") or "")}
    if judge == "citation_recall":
        needed = [n for n in data.get("needed") or [] if isinstance(n, int) and 1 <= n <= bindings]
        out["citation_precision"] = len(set(needed)) / bindings if bindings else None
    return out


def run_judge(judge: str, model_id: str, items: list[dict], out: Path, client) -> None:
    from engine.provider import guard

    done = {r["item_id"] for r in read_jsonl(out)}
    prompt_hash = sha256_text(JUDGE_PROMPTS[judge])
    with out.open("a", encoding="utf-8") as handle:
        for item in items:
            if item["item_id"] in done:
                continue
            try:
                response = client.messages.create(
                    model=model_id, max_tokens=MAX_TOKENS, system=JUDGE_PROMPTS[judge],
                    messages=[{"role": "user", "content": judge_message(item)}],
                )
            except guard.LiveTestCapReached as stop:
                print(f"stopped at the cap: {stop}", flush=True)
                return
            reply = "".join(getattr(block, "text", "") for block in response.content)
            row = {
                "item_id": item["item_id"], "judge": judge, "model_id": model_id, "prompt_sha256": prompt_hash,
                "reply": reply, "judgement": parse_judgement(judge, reply, len(item["bindings"])),
                "usage": {"input_tokens": response.usage.input_tokens, "output_tokens": response.usage.output_tokens},
                "at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            }
            handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")
            handle.flush()


def _rates(pairs: list[tuple[bool, bool]]) -> dict:
    """(gold unsupported, flagged) pairs: recall and precision on
    "unsupported", with the counts behind them."""
    tp = sum(1 for g, f in pairs if g and f)
    fn = sum(1 for g, f in pairs if g and not f)
    fp = sum(1 for g, f in pairs if not g and f)
    return {
        "items": len(pairs), "gold_unsupported": tp + fn, "flagged": tp + fp, "true_flags": tp,
        "recall_unsupported": tp / (tp + fn) if tp + fn else None,
        "precision_unsupported": tp / (tp + fp) if tp + fp else None,
    }


def _kappa(a: list[bool], b: list[bool]) -> float | None:
    n = len(a)
    if not n:
        return None
    observed = sum(x == y for x, y in zip(a, b)) / n
    pa, pb = sum(a) / n, sum(b) / n
    expected = pa * pb + (1 - pa) * (1 - pb)
    return (observed - expected) / (1 - expected) if expected < 1 else None


def gates_flag(item: dict) -> bool | None:
    """The current gates flagged the sentence: removed it, or kept it without
    its citation. None for a constructed item, which the gates never saw."""
    gate = item.get("gate") or {}
    if gate.get("verdict") in (None, "unmatched"):
        return None
    return gate["verdict"] != "ok"


def score(gold: list[dict], verdicts: dict[str, dict[str, dict]]) -> dict:
    """Recall and precision on "unsupported" for each judge and for the
    current gates, overall and per class, on the gold items that carry a
    supported/unsupported label; agreement of each judge with the gold
    labels (the specialist's, as adjudicated)."""
    judged = [i for i in gold if i["label"]["verdict"] in ("supported", "unsupported")]
    report: dict = {"items": len(judged), "classes": dict(Counter(gold_class(i["label"]) for i in judged)), "deciders": {}}
    deciders = {**{f"judge:{name}": (lambda i, n=name: (verdicts[n].get(i["item_id"]) or {}).get("supported")) for name in verdicts},
                "current_gates": lambda i: (None if gates_flag(i) is None else not gates_flag(i))}
    for name, supported_of in deciders.items():
        rows = [(i, supported_of(i)) for i in judged]
        rows = [(i, s) for i, s in rows if s is not None]
        pairs = [(i["label"]["verdict"] == "unsupported", not s) for i, s in rows]
        per_class = {}
        for cls in sorted({gold_class(i["label"]) for i, _ in rows}):
            members = [(i, s) for i, s in rows if gold_class(i["label"]) == cls]
            per_class[cls] = {"items": len(members), "flagged": sum(1 for _, s in members if not s)}
        report["deciders"][name] = {
            **_rates(pairs), "per_class": per_class, "not_judged": len(judged) - len(rows),
            "kappa_with_gold": _kappa([g for g, _ in pairs], [f for _, f in pairs]),
        }
    return report


def adjudication_queue(gold: list[dict], verdicts: dict[str, dict[str, dict]], sample: int, seed: int = 20261029) -> list[dict]:
    """Every item where a judge disagrees with the specialist's label in a
    key class (or the specialist's unsupported label names a key class), and
    a random sample of the other disagreements and agreements."""
    must, rest = [], []
    for item in gold:
        label = item["label"]
        gold_supported = label["verdict"] == "supported"
        if label["verdict"] not in ("supported", "unsupported"):
            continue
        disagree = [name for name, by_item in verdicts.items()
                    if (by_item.get(item["item_id"]) or {}).get("supported") not in (None, gold_supported)]
        classes = {label.get("failure_class"), *label.get("other_classes", [])}
        entry = {"item_id": item["item_id"], "disagreeing_judges": disagree, "specialist_class": gold_class(label)}
        if disagree and (classes & set(KEY_CLASSES) or not gold_supported):
            must.append(entry)
        else:
            rest.append(entry)
    rng = random.Random(seed)
    return must + rng.sample(rest, min(sample, len(rest)))


def main(argv: list[str] | None = None) -> int:
    from engine.m8.price_tables import price_for_route
    from engine.provider import guard

    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    sub = parser.add_subparsers(dest="command", required=True)
    run = sub.add_parser("judge")
    run.add_argument("--judge", choices=sorted(JUDGE_PROMPTS), required=True)
    run.add_argument("--model", required=True)
    run.add_argument("--half", choices=(CALIBRATION, HELDOUT), required=True)
    run.add_argument("--limit", type=int)
    run.add_argument("--out", type=Path, required=True)
    run.add_argument("--settings-only", action="store_true")
    guard.add_arguments(run)
    scoring = sub.add_parser("score")
    scoring.add_argument("--half", choices=(CALIBRATION, HELDOUT), required=True)
    scoring.add_argument("--verdicts", type=Path, action="append", required=True)
    scoring.add_argument("--out", type=Path)
    args = parser.parse_args(argv)

    gold = read_jsonl(gold_path(args.half))
    if args.command == "score":
        verdicts: dict[str, dict[str, dict]] = {}
        for path in args.verdicts:
            for row in read_jsonl(path):
                verdicts.setdefault(row["judge"], {})[row["item_id"]] = row["judgement"] or {}
        result = {"half": args.half, **score(gold, verdicts)}
        text = json.dumps(result, indent=2)
        if args.out:
            args.out.write_text(text + "\n", encoding="utf-8")
        print(text)
        return 0

    items = gold[: args.limit]
    price = price_for_route("voice_generation", args.model, "bedrock")
    input_tokens = sum((len(JUDGE_PROMPTS[args.judge]) + len(judge_message(i))) / CHARS_PER_TOKEN for i in items)
    output_tokens = EXPECTED_OUTPUT_TOKENS * len(items)
    settings = {
        "judge": args.judge, "model_id": args.model, "region": REGION, "half": args.half, "items": len(items),
        "max_tokens": MAX_TOKENS, "temperature": "API default (not set)", "prompt_sha256": sha256_text(JUDGE_PROMPTS[args.judge]),
        "input_tokens": round(input_tokens), "output_tokens": output_tokens,
        "estimated_usd": None if price is None else input_tokens * price.input_per_token + output_tokens * price.output_per_token,
    }
    print(json.dumps(settings, indent=2), flush=True)
    if args.settings_only:
        return 0
    if price is None:
        print(f"no approved price for {args.model}", file=sys.stderr)
        return 2
    from goldset.runner import make_client_for

    args.out.parent.mkdir(parents=True, exist_ok=True)
    run_judge(args.judge, args.model, items, args.out, make_client_for(args.model))
    print(json.dumps({"priced_total_usd": guard.priced_total()}), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
