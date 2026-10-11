"""E3: citation attachment on stored drafts. For each uncited claim
sentence in a stored "off" draft (engine/m3/reports/e2), a Haiku 4.5
call proposes the one record that carries it, and a second Haiku 4.5
call checks each proposal against that record's own text; only a
"carries" verdict is attached. The draft's text is never changed - the
step only adds citations to sentences that had none.

Paid run: every setting is printed before the first billed call, and
spend is checked against --max-usd before every probe.
"""
import argparse
import json
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import anthropic

from engine.m1.registry import load_registry
from engine.m4.grounding_net import _groundable_text
from engine.m7.standing_measure import load_world_records, quote_aware_sentences
from engine.m8.cost import estimate_cost
from engine.m8.price_tables import price_for_model
from engine.provider import guard
from engine.provider.bedrock import make_client, normalize_usage, resolve_model_id

REPO_ROOT = Path(__file__).resolve().parents[2]
E2_DIR = Path(__file__).resolve().parent / "reports" / "e2"
REPORT_DIR = Path(__file__).resolve().parent / "reports" / "e3"
PROPOSE_MAX_TOKENS = 2000
VERIFY_MAX_TOKENS = 5

PROPOSE = (
    "You check citations for the Representative whose world is described above. Below are sentences it said "
    "without a citation. For each one, find the single record in the world above whose own text carries the "
    "sentence's specific claim, and give that record's id copied exactly from the list of valid ids at the end of "
    "these instructions (the same ids the world above shows inside [[...]]). Never build an id from a heading, a "
    "cell code or a title. Choose a record only when its text actually states or directly entails the claim; a "
    "record on the same topic that does not carry the claim is not enough. If no record carries the claim, answer "
    'null. Answer with JSON only: [{"id": "S1", "record_id": "world.type.slug" or null}, ...], one entry per '
    "sentence, nothing else."
)
VERIFY = (
    "You check one citation. You get a sentence and the text of the record it cites. Answer \"carries\" only if the "
    "record's text itself states or directly entails every specific claim in the sentence (people, places, dates, "
    "numbers, events, practices, teachings). Paraphrase and modern wording are fine. Answer \"partly\" if the record "
    "carries the core but the sentence adds any specific detail the record does not state. Answer \"no\" if the "
    "record does not carry the main claim. Use only the record text, never outside knowledge. Reply with one word: "
    "carries, partly or no."
)


def stored_drafts() -> dict[str, dict[str, dict]]:
    """world -> probe_id -> the stored "off" transcript, from the E2 fleet
    pair runs and the hal/rzg three-arm sample."""
    drafts: dict[str, dict[str, dict]] = {}
    paths = sorted((E2_DIR / "fleet").glob("e2-pair-*.json")) + [E2_DIR / "e2-sample-hal-rzg-2026-10-03.json"]
    for path in paths:
        for world, rows in json.loads(path.read_text())["worlds"].items():
            for row in rows:
                if row["arms"]:
                    drafts.setdefault(world, {})[row["probe_id"]] = row["arms"]["off"]
    return drafts


def _call(client, **kw):
    for attempt in range(7):
        try:
            return client.messages.create(**kw)
        except anthropic.RateLimitError:
            time.sleep(2 ** attempt)
    raise RuntimeError("rate limited seven times in a row")


def parse_proposals(text: str) -> list[dict]:
    """The first JSON array in the reply, tolerating text after it; [] when
    there is none. Entries that are not objects are dropped."""
    start = text.find("[")
    if start < 0:
        return []
    try:
        value, _ = json.JSONDecoder().raw_decode(text[start:])
    except json.JSONDecodeError:
        return []
    return [p for p in value if isinstance(p, dict)] if isinstance(value, list) else []


def first_word(text: str) -> str:
    words = re.findall(r"[a-z]+", text.lower())
    return words[0] if words else ""


def attach(client, model: str, table, *, prompt_text: str, valid_ids: list[str], records: dict[str, dict],
           transcript: dict) -> tuple[dict, float]:
    """Returns (the transcript with verified citations added, dollars)."""
    sentences = quote_aware_sentences(transcript["answer_text"])
    uncited = [s for s in sentences if s in set(transcript["uncited_claim_sentences"])]
    added, trail, cost = [], [], 0.0
    if uncited:
        lines = []
        for n, s in enumerate(uncited, 1):
            i = sentences.index(s)
            before = sentences[i - 1] if i else "(start of reply)"
            lines.append(f'S{n}: "{s}" (just before it: "{before}")')
        resp = _call(client, model=model, max_tokens=PROPOSE_MAX_TOKENS,
                     system=[{"type": "text", "text": prompt_text, "cache_control": {"type": "ephemeral"}},
                             {"type": "text", "text": PROPOSE + "\n\nValid ids:\n" + "\n".join(valid_ids)}],
                     messages=[{"role": "user", "content": "\n".join(lines)}])
        cost += estimate_cost(normalize_usage(resp.usage), table).dollars
        for p in parse_proposals(resp.content[0].text):
            m = re.fullmatch(r"S(\d+)", str(p.get("id", "")))
            n = int(m.group(1)) if m else 0
            rid = p.get("record_id")
            if not (1 <= n <= len(uncited)) or rid not in records or rid not in valid_ids:
                trail.append({"sentence": uncited[n - 1] if 1 <= n <= len(uncited) else None, "proposed": rid, "verdict": "rejected"})
                continue
            v = _call(client, model=model, max_tokens=VERIFY_MAX_TOKENS, system=VERIFY,
                      messages=[{"role": "user", "content": f"Sentence: {uncited[n - 1]}\n\nRecord {rid}:\n{_groundable_text(records[rid])}"}])
            cost += estimate_cost(normalize_usage(v.usage), table).dollars
            verdict = first_word(v.content[0].text)
            trail.append({"sentence": uncited[n - 1], "proposed": rid, "verdict": verdict})
            if verdict == "carries":
                added.append({"sentence": uncited[n - 1], "record_ids": [rid], "attached": True})
    out = {**transcript, "citation_entries": list(transcript["citation_entries"]) + added,
           "uncited_claim_sentences": [s for s in transcript["uncited_claim_sentences"] if s not in {a["sentence"] for a in added}],
           "attach_trail": trail}
    return out, cost


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    guard.add_arguments(p)
    p.add_argument("--region", required=True)
    p.add_argument("--worlds", required=True)
    p.add_argument("--max-usd", type=float, required=True)
    p.add_argument("--authorized-by", required=True)
    p.add_argument("--probes", default=None, help="comma-separated probe ids (default every stored draft)")
    p.add_argument("--settings-only", action="store_true")
    p.add_argument("--out", default=None)
    args = p.parse_args(argv)

    registry = load_registry()
    worlds = args.worlds.split(",")
    model = resolve_model_id("us.anthropic.claude-haiku-4-5", args.region)
    drafts = stored_drafts()
    settings = {
        "worlds": worlds, "drafts": {w: len(drafts.get(w, {})) for w in worlds}, "probes": args.probes, "model": model,
        "propose_max_tokens": PROPOSE_MAX_TOKENS, "verify_max_tokens": VERIFY_MAX_TOKENS, "temperature": "API default",
        "propose_instruction": PROPOSE, "verify_instruction": VERIFY, "kept": "verdict 'carries' only",
        "max_usd": args.max_usd, "authorized_by": args.authorized_by,
        "package_manifest_hash": {w: registry[w]["package"]["manifest_hash"] for w in worlds},
    }
    print(json.dumps({"run_settings": settings}, indent=2), flush=True)
    if args.settings_only:
        return 0

    client = make_client(args.region)
    table = price_for_model(model)
    report = {"run_settings": settings, "started": datetime.now(timezone.utc).isoformat(timespec="seconds"), "worlds": {}}
    spent, aborted = 0.0, None
    for w in worlds:
        prompt_text = (REPO_ROOT / registry[w]["package"]["location"] / "compiled" / "prompt.txt").read_text()
        valid_ids = sorted(set(re.findall(r"\[\[([a-z0-9_.-]+)\]\]", prompt_text)))
        records = load_world_records(w)
        report["worlds"][w] = {}
        wanted = set(args.probes.split(",")) if args.probes else None
        for probe_id, transcript in sorted(drafts[w].items()):
            if wanted is not None and probe_id not in wanted:
                continue
            if spent >= args.max_usd:
                aborted = f"stopped before {w}:{probe_id}: spent {spent:.4f} >= cap {args.max_usd}"
                break
            out, cost = attach(client, model, table, prompt_text=prompt_text, valid_ids=valid_ids, records=records,
                               transcript=transcript)
            spent += cost
            report["worlds"][w][probe_id] = {"attach": out, "usd": round(cost, 6)}
            print(json.dumps({"world": w, "probe": probe_id, "usd": round(cost, 4), "spent": round(spent, 4),
                              "added": sum(1 for e in out["citation_entries"] if e.get("attached"))}), flush=True)
        if aborted:
            break
    report.update(actual_usd_spent=round(spent, 6), aborted_reason=aborted)
    out_path = Path(args.out) if args.out else REPORT_DIR / f"e3-{datetime.now(timezone.utc):%Y-%m-%dT%H-%M-%SZ}.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n")
    print(f"wrote {out_path}; spent {spent:.4f}; aborted={aborted}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
