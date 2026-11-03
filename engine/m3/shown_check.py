"""Checks that what a stand-in reader or rater was shown is what the engine offered.

  python -m engine.m3.shown_check voice --work DIR
  python -m engine.m3.shown_check items --items ITEMS.json --db INDEX.sqlite

`voice` reads every `pending/<key>.request.json` of a test-set run. For each voice request it compares the
record ids the engine offered (the `- [[id]]` lines of its messages) with the ids in the prompt file the helper
is given, and counts the prompt file and each system file against what one read returns whole: the Read
tool returns at most 2000 lines of at most 2000 characters, and a file past 80000 bytes (about 20000 tokens) is
not read in one piece. It also reports where the offered passages sit in the offer. A request fails when an offered id
is missing from its prompt file or when a file is too long to be read whole.

`items` reads a rater's item list (each item holds `passage_id` and `passage`) and the passage index, and
fails any item whose passage text is shorter than the passage in the index.

Exit status is 1 when any check fails. No model call.
"""
import argparse
import json
import sqlite3
import sys
from pathlib import Path

from engine.m3.reply_client import ids_in, offered_ids

MAX_LINES = 2000
MAX_LINE_CHARS = 2000
MAX_BYTES = 80000
_PASSAGE_TAG = ".passage."


def _size(path: Path) -> dict:
    data = path.read_bytes()
    return {"file": path.name, "lines": data.count(b"\n") + 1, "bytes": len(data), "longest_line": max(len(x) for x in data.decode("utf-8").split("\n"))}


def _too_long(size: dict) -> bool:
    return size["lines"] > MAX_LINES or size["bytes"] > MAX_BYTES or size["longest_line"] > MAX_LINE_CHARS


def check_voice_request(request_path: Path) -> dict:
    request = json.loads(request_path.read_text(encoding="utf-8"))
    key = request_path.name[: -len(".request.json")]
    prompt = request_path.with_name(f"{key}.prompt.txt")
    offered = offered_ids(request)
    shown = ids_in(prompt.read_text(encoding="utf-8"))
    sizes = [_size(prompt)] + [_size(Path(p)) for p in request["system_files"]]
    passages = [i for i, found in enumerate(offered) if _PASSAGE_TAG in found]
    return {
        "key": key,
        "offered": len(offered),
        "missing": [i for i in offered if i not in shown],
        "too_long": [s["file"] for s in sizes if _too_long(s)],
        "passage_positions": [f"{i + 1} of {len(offered)}" for i in passages],
    }


def check_voice(work: Path) -> list[dict]:
    results = []
    for request_path in sorted((work / "pending").glob("*.request.json")):
        if json.loads(request_path.read_text(encoding="utf-8"))["kind"] == "voice":
            results.append(check_voice_request(request_path))
    return results


def check_items(items: list[dict], db_path: Path) -> list[dict]:
    connection = sqlite3.connect(db_path)
    try:
        failures = []
        for item in items:
            row = connection.execute("SELECT text FROM passages WHERE passage_id = ?", (item["passage_id"],)).fetchone()
            full = len(row[0].split()) if row else None
            shown = len(item["passage"].split())
            if full is None or shown < full:
                failures.append({"id": item["id"], "passage_id": item["passage_id"], "shown_words": shown, "passage_words": full})
        return failures
    finally:
        connection.close()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    sub = parser.add_subparsers(dest="mode", required=True)
    voice = sub.add_parser("voice")
    voice.add_argument("--work", type=Path, required=True)
    items = sub.add_parser("items")
    items.add_argument("--items", type=Path, required=True)
    items.add_argument("--db", type=Path, required=True)
    args = parser.parse_args(argv)
    if args.mode == "voice":
        results = check_voice(args.work)
        failed = [r for r in results if r["missing"] or r["too_long"]]
        print(json.dumps({"requests": len(results), "failed": len(failed), "with_passages": sum(1 for r in results if r["passage_positions"]),
                          "results": results}, indent=1))
        return 1 if failed else 0
    failures = check_items(json.loads(args.items.read_text(encoding="utf-8")), args.db)
    print(json.dumps({"failed": len(failures), "failures": failures}, indent=1))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
