"""Labelling inside the Claude plan, with no metered call: the same prompt the
runner would send is written to one file per stream line; a Claude Code
subagent of the named model reads each prompt file and writes its reply to a
file of the same name; the replies are then checked by the same code as a
metered run and kept as labels.

The prompt files hold only what a metered labeller would see (the system
prompt, the evidence pack and the sentence). The stream's key, the pool, the
gates' decisions and any judge output are never written beside them. A reply
the check rejects gets a retry file with the reason, once; a second rejection
leaves the line unlabelled, as in runner.py.

  python -m goldset.inplan export --stream <stream.jsonl> --dir <work dir>
  (the subagent writes <work dir>/replies/<line_id>.txt for each prompts/<line_id>.md)
  python -m goldset.inplan import --stream <stream.jsonl> --dir <work dir> --model <name> --out <labels.jsonl>
"""
import argparse
import json
import time
from pathlib import Path

from goldset.common import read_jsonl, sha256_text
from goldset.evidence import build_pack, located
from goldset.labeller import SYSTEM_PROMPT, parse_reply, user_message
from goldset.runner import stream_line_item

RETRY_NOTE = "That reply cannot be used: {why}. Reply again with one JSON object, copying evidence words exactly from the named block."


def prompt_text(line: dict, pack: dict) -> str:
    return f"SYSTEM\n{SYSTEM_PROMPT}\n\nUSER\n{user_message(line['sentence'], pack)}\n"


def export(lines: list[dict], work: Path) -> int:
    prompts = work / "prompts"
    prompts.mkdir(parents=True, exist_ok=True)
    (work / "replies").mkdir(exist_ok=True)
    for line in lines:
        pack = build_pack(stream_line_item(line))
        (prompts / f"{line['line_id']}.md").write_text(prompt_text(line, pack), encoding="utf-8")
    (work / "prompt_sha256.txt").write_text(sha256_text(SYSTEM_PROMPT) + "\n", encoding="utf-8")
    return len(lines)


def import_replies(lines: list[dict], work: Path, model: str) -> tuple[list[dict], list[str]]:
    """Labels for every line with a reply; lines needing a retry get a retry
    prompt and are left out until their second reply is in."""
    rows, retry = [], []
    for line in lines:
        first = work / "replies" / f"{line['line_id']}.txt"
        second = work / "replies" / f"{line['line_id']}.retry.txt"
        if not first.exists():
            continue
        pack = build_pack(stream_line_item(line))
        attempts = []
        for path in (first, second):
            if not path.exists():
                break
            reply = path.read_text(encoding="utf-8")
            checked = parse_reply(reply, pack)
            attempts.append({"reply": reply, "check": "ok" if checked["ok"] else checked["why"]})
            if checked["ok"]:
                break
        last_ok = attempts[-1]["check"] == "ok"
        if not last_ok and len(attempts) == 1:
            retry_prompt = prompt_text(line, pack) + f"\nASSISTANT (your earlier reply)\n{attempts[0]['reply']}\n\nUSER\n" + RETRY_NOTE.format(why=attempts[0]["check"]) + "\n"
            (work / "prompts" / f"{line['line_id']}.retry.md").write_text(retry_prompt, encoding="utf-8")
            retry.append(line["line_id"])
            continue
        label = parse_reply(attempts[-1]["reply"], pack)["label"] if last_ok else None
        rows.append({
            "line_id": line["line_id"], "model_id": model, "route": "in plan (Claude Code subagent), no metered call",
            "label": label, "attempts": attempts, "passage_located": located(pack),
            "at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        })
    return rows, retry


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    sub = parser.add_subparsers(dest="command", required=True)
    for name in ("export", "import"):
        p = sub.add_parser(name)
        p.add_argument("--stream", type=Path, required=True)
        p.add_argument("--dir", type=Path, required=True)
        p.add_argument("--limit", type=int)
        if name == "import":
            p.add_argument("--model", required=True, help="the model the subagent ran on, as named")
            p.add_argument("--out", type=Path, required=True)
    args = parser.parse_args(argv)
    lines = read_jsonl(args.stream)[: args.limit]
    if args.command == "export":
        print(json.dumps({"prompts_written": export(lines, args.dir)}))
        return 0
    rows, retry = import_replies(lines, args.dir, args.model)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text("".join(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n" for r in rows), encoding="utf-8")
    print(json.dumps({"labelled": sum(r["label"] is not None for r in rows), "unlabelled": sum(r["label"] is None for r in rows),
                      "awaiting_retry": len(retry), "no_reply_yet": len(lines) - len(rows) - len(retry)}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
