"""The independent AI adjudication of the packet items, in place of a human
ruling (Mark, 2026-10-29: "i would trust an objective ai view").

Three reads of each item, each by a fresh Claude Code subagent that sees none
of the others:

  opus     the labeller's instructions and the full evidence pack
  fable    the same, on another model
  referee  an outside referee: the sentence and the source passages only,
           with none of our records, notes or lexicon

The first two are blind to the earlier labels, except on an item where the
earlier readers disagreed: there both earlier readings are shown, with their
quoted evidence, as claims to test. The referee never sees an earlier reading.

A label stands when at least two of the three reads give the same class. If
no two agree the item is contested: it is left out of the gold set, counted
and listed, never forced. A read that could not judge counts as a read, so an
item where only one read could judge is contested too.

  python -m goldset.adjudicate export --pool <pool.jsonl> --constructed <constructed.jsonl> \\
      --packet <packet.json> [--packet ...] --dir <work dir>
  (subagents write <work dir>/replies/<name>.txt for each prompts/<name>.md)
  python -m goldset.adjudicate import (the same) --out <adjudications.jsonl>
"""
import argparse
import json
import time
from collections import Counter
from pathlib import Path

from goldset.common import read_jsonl, sha256_text
from goldset.evidence import build_pack, render_pack
from goldset.labeller import SYSTEM_PROMPT, gold_class, parse_reply, user_message

READERS = {"opus": "claude-opus-5-5", "fable": "claude-fable-5-1", "referee": "claude-opus-5-5"}

ADJUDICATOR_NOTE = """

You are adjudicating: your reading decides the gold label used to measure automatic checkers, so take the most careful reading the evidence allows. If EARLIER READINGS are given, they are two earlier readers' claims that disagree; test each against the evidence yourself and do not defer to either."""

REFEREE_PROMPT = """You are an outside referee, a scholar of early and medieval Christian sources and of the editions they survive in. You check one sentence that a historical Representative of a Christian tradition said, against the source passages it rests on. The Representative speaks in the first person plural ("we", "our") for its own tradition. You see only the edition text, never the project's own notes about it.

You are given SOURCE PASSAGES [P1 ...]: the edition text, with its division. The lines cited are marked. Editors' notes appear as [editor's note: ...]; they are the editor's words, not the source's. A passage may be a translation; its language is given.

Decide whether the sentence is supported by these passages. Judge only what the sentence asserts. Use what you know of the period only to read the passages correctly, never to supply a claim the passages do not make.

Verdicts:
- "supported": every assertion in the sentence is stated in the passages or follows closely from them, attributed to the right speaker, with the same force.
- "unsupported": at least one assertion is not in the passages, is contradicted by them, or changes what they say.
- "no_claim": the sentence asserts nothing about the tradition, its people, texts or history.
- "cannot_judge": the passages do not let you decide (say exactly what is missing). If no passage is given, this is your verdict.

When the verdict is "unsupported", give the failure class that best describes it, and any others that also apply:
- "false_friend": the sentence depends on reading a word in a modern sense the source does not carry.
- "negation_modal_shift": the sentence drops, adds or reverses a negation, or shifts a modal or quantifier.
- "generalisation": the sentence states as the tradition's own position what the passage gives as one author's view, one text, one occasion or one group; or turns one instance into a habit.
- "embedded_voice": the sentence gives as the tradition's or the author's own view words that in the passage belong to someone else: an opponent, an interlocutor, a correspondent, a hostile witness, or an editor.
- "unsupported_other": anything else unsupported.

Bind every verdict to the exact words: copy, character for character, at least four and no more than about forty consecutive words from one passage, and name its block id. For "cannot_judge" with no passage, give an empty evidence list.

Reply with one JSON object and nothing else:
{"verdict": "...", "failure_class": null or "...", "other_classes": [], "evidence": [{"block": "P1", "words": "..."}], "reason": "one or two plain sentences", "record_concern": null}"""


ITEMS: dict[str, dict] = {}


def _item(row: dict) -> dict:
    """The item as it was labelled (world, commit, bindings, sentence), from
    the pool or the constructed items, by id."""
    item = ITEMS[row["item_id"]]
    return {"item_id": row["item_id"], **{k: item[k] for k in ("world", "records_commit", "bindings", "sentence")}}


def referee_pack(pack: dict) -> dict:
    return {**pack, "blocks": [b for b in pack["blocks"] if b["kind"] == "passage" and b.get("status") == "ok"]}


def earlier_readings(row: dict) -> str | None:
    """Both earlier readings, for an item where they disagree."""
    if row["why"] not in ("disagreement", "constructed, not read as intended"):
        return None
    first = row.get("specialist") or {}
    if row["why"] == "disagreement":
        second = row.get("second") or {}
    else:
        made = row["constructed"]
        second = {"class": made["class"], "reason": made["construction"], "evidence": [{"block": "R1", "words": made["record_words"]}]}
    out = ["EARLIER READINGS (two readers who disagree; test both)"]
    for name, reading in (("Reading A", first), ("Reading B", second)):
        quotes = "; ".join(f"[{e['block']}] \"{e['words']}\"" for e in reading.get("evidence") or [])
        out.append(f"{name}: {reading.get('class')}. {reading.get('reason', '')} Evidence: {quotes or 'none'}")
    return "\n".join(out)


def prompt(reader: str, row: dict) -> tuple[str, dict]:
    pack = build_pack(_item(row))
    if reader == "referee":
        pack = referee_pack(pack)
        body = f"SOURCE PASSAGES\n\n{render_pack(pack) or '(no passage could be located for this sentence)'}\n\nSENTENCE TO CHECK\n{row['sentence']}"
        return f"SYSTEM\n{REFEREE_PROMPT}\n\nUSER\n{body}\n", pack
    message = user_message(row["sentence"], pack)
    earlier = earlier_readings(row)
    if earlier:
        message += f"\n\n{earlier}"
    return f"SYSTEM\n{SYSTEM_PROMPT}{ADJUDICATOR_NOTE}\n\nUSER\n{message}\n", pack


def name(row: dict, reader: str) -> str:
    return f"{row['item_id']}.{reader}"


def export(rows: list[dict], work: Path) -> Counter:
    (work / "prompts").mkdir(parents=True, exist_ok=True)
    (work / "replies").mkdir(exist_ok=True)
    written = Counter()
    for row in rows:
        for reader in READERS:
            text, _ = prompt(reader, row)
            (work / "prompts" / f"{name(row, reader)}.md").write_text(text, encoding="utf-8")
            written[reader] += 1
    (work / "prompt_sha256.txt").write_text(
        f"adjudicator {sha256_text(SYSTEM_PROMPT + ADJUDICATOR_NOTE)}\nreferee {sha256_text(REFEREE_PROMPT)}\n", encoding="utf-8")
    return written


def outcome(classes: list[str | None]) -> tuple[str | None, int]:
    """The class at least two reads share, and how many share it."""
    counted = Counter(c for c in classes if c is not None)
    if not counted:
        return None, 0
    top, n = counted.most_common(1)[0]
    return (top, n) if n >= 2 else (None, n)


def import_replies(rows: list[dict], work: Path) -> tuple[list[dict], list[str]]:
    out, retry = [], []
    for row in rows:
        reads = {}
        for reader, model in READERS.items():
            path = work / "replies" / f"{name(row, reader)}.txt"
            again = work / "replies" / f"{name(row, reader)}.retry.txt"
            if not path.exists():
                reads[reader] = None
                continue
            text, pack = prompt(reader, row)
            checked = parse_reply(path.read_text(encoding="utf-8"), pack)
            if not checked["ok"] and again.exists():
                checked = parse_reply(again.read_text(encoding="utf-8"), pack)
            elif not checked["ok"]:
                retry_text = text + f"\nASSISTANT (your earlier reply)\n{path.read_text(encoding='utf-8')}\n\nUSER\nThat reply cannot be used: {checked['why']}. Reply again with one JSON object, copying evidence words exactly from the named block.\n"
                (work / "prompts" / f"{name(row, reader)}.retry.md").write_text(retry_text, encoding="utf-8")
                retry.append(name(row, reader))
            reads[reader] = {"model_id": model, "label": checked.get("label"), "check": "ok" if checked["ok"] else checked["why"]}
        classes = [gold_class(r["label"]) if r and r["label"] else None for r in reads.values()]
        standing, agreeing = outcome(classes)
        out.append({"item_id": row["item_id"], "why": row["why"], "origin": "constructed" if row.get("constructed") else "natural",
                    "reads": reads, "classes": dict(zip(READERS, classes)), "standing_class": standing, "agreeing_reads": agreeing,
                    "contested": standing is None, "route": "in plan (Claude Code subagents), no metered call",
                    "at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())})
    return out, retry


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("command", choices=("export", "import"))
    parser.add_argument("--pool", type=Path, required=True)
    parser.add_argument("--constructed", type=Path, required=True)
    parser.add_argument("--packet", type=Path, action="append", required=True)
    parser.add_argument("--dir", type=Path, required=True)
    parser.add_argument("--out", type=Path)
    args = parser.parse_args(argv)
    rows = [row for path in args.packet for row in json.loads(path.read_text(encoding="utf-8"))]
    ITEMS.update({i["item_id"]: i for i in read_jsonl(args.pool)})
    ITEMS.update({c["construct_id"]: c for c in read_jsonl(args.constructed)})
    if args.command == "export":
        print(json.dumps({"prompts_written": export(rows, args.dir)}))
        return 0
    out, retry = import_replies(rows, args.dir)
    args.out.write_text("".join(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n" for r in out), encoding="utf-8")
    missing = sum(r is None for o in out for r in o["reads"].values())
    print(json.dumps({"items": len(out), "standing": sum(not o["contested"] for o in out), "contested": sum(o["contested"] for o in out),
                      "reads_missing": missing, "awaiting_retry": len(retry)}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
