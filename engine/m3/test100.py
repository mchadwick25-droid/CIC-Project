"""Runs the frozen lpc 100-question set through the engine's own turn path
with no model call. Every model call is answered from a reply file
(engine.m3.reply_client); a question whose replies are not all written yet
is left pending and its requests are written out for whoever drafts them.

It reads sealed probe wording for the 28 sealed questions, as engine.m3.gate_replay
does, so every directory it writes to must lie outside the repository: the pending
requests of a sealed question carry its wording.

  python -m engine.m3.test100 --set <lpc_100_questions.yaml> --world lpc \
      --work <dir outside the repo>

One pass runs every question as far as its replies allow. Run it again after the
replies are written. A finished question leaves `answers/<id>.json` in the work
directory: the shipped text, its citations, the routing, and the net's verdict on
every draft sentence.
"""
import argparse
import hashlib
import json
from pathlib import Path

import yaml

from engine.m3.reply_client import PendingReply, ReplyFileClient

REPO_ROOT = Path(__file__).resolve().parents[2]
SHADOW_SETTINGS = {
    "voice_model_id": "reply-file", "safety_model_id": "reply-file",
    "r27_enforce": True, "self_revision_enabled": True, "citation_attach_enabled": False, "streaming_enabled": False,
}


def load_set(path: Path) -> list[dict]:
    seal = path.with_suffix(".sha256")
    if seal.exists() and seal.read_text().split()[0] != hashlib.sha256(path.read_bytes()).hexdigest():
        raise SystemExit(f"{path.name} no longer matches its seal")
    return yaml.safe_load(path.read_text(encoding="utf-8"))["questions"]


def question_text(question: dict) -> str:
    if question["group"] == "A":
        from engine.m3.sealed_probes import read_probe

        return read_probe(question["probe_id"])["text"]
    return question["wording"]


def _outside_repo(path: Path) -> Path:
    resolved = path.resolve()
    if resolved == REPO_ROOT or REPO_ROOT in resolved.parents:
        raise SystemExit(f"{path} is inside the repository; the work directory must be outside it")
    return resolved


def _row(question: dict, result, net_results: list[dict], raw_drafts: list[str]) -> dict:
    net = net_results[-1] if net_results else {}
    return {
        "id": question["id"], "group": question["group"], "text": result.text, "citations": result.citations,
        "citation_entries": result.citation_entries, "routing_action": result.live_turn.routing_action,
        "routing_reason": result.live_turn.routing_reason, "sends": result.live_turn.sends,
        "raw_text": raw_drafts[-1] if raw_drafts else "",
        "net_sentences": net.get("sentences", []), "reply_shape": net.get("reply_shape"),
    }


def run_pass(*, questions: list[dict], world_key: str, work: Path, worktree: Path = REPO_ROOT) -> dict:
    from engine.m1.registry import load_registry
    from engine.m3.generation import LiveModelAnswerer, LivePathSettings
    from engine.m4 import turn as m4_turn
    from engine.m4.world_loader import LazyWorldLoader

    registry = load_registry()
    entry = registry[world_key]
    loaded, _timing = LazyWorldLoader().load(
        world_key, package_dir=worktree / entry["package"]["location"], expected_manifest_hash=entry["package"]["manifest_hash"],
    )
    reply_dir, pending_dir, answers_dir = work / "replies", work / "pending", work / "answers"
    answers_dir.mkdir(parents=True, exist_ok=True)
    for stale in pending_dir.glob("*") if pending_dir.exists() else []:
        stale.unlink()
    captured: list[dict] = []
    drafts: list[str] = []
    real_apply_net = m4_turn.apply_net

    def keeping_net_result(*args, **kwargs):
        text, citations, net_result = real_apply_net(*args, **kwargs)
        captured.append(net_result)
        drafts.append(args[0] if args else kwargs["raw_text"])
        return text, citations, net_result

    m4_turn.apply_net = keeping_net_result
    done, pending = [], []
    try:
        for question in questions:
            if (answers_dir / f"{question['id']}.json").exists():
                done.append(question["id"])
                continue
            client = ReplyFileClient(question_id=question["id"], reply_dir=reply_dir, pending_dir=pending_dir)
            answerer = LiveModelAnswerer(world=loaded, registry=registry, client=client, settings=LivePathSettings(**SHADOW_SETTINGS))
            captured.clear()
            drafts.clear()
            try:
                result = answerer.answer(question.get("cell") or question["id"], question_text(question))
            except PendingReply:
                pending.append(question["id"])
                continue
            (answers_dir / f"{question['id']}.json").write_text(
                json.dumps(_row(question, result, list(captured), list(drafts)), ensure_ascii=False, indent=1, sort_keys=True), encoding="utf-8",
            )
            done.append(question["id"])
    finally:
        m4_turn.apply_net = real_apply_net
    return {"done": len(done), "pending": len(pending), "pending_ids": pending, "pending_requests": sorted(p.name for p in pending_dir.glob("*.prompt.txt")) if pending_dir.exists() else []}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--set", type=Path, required=True, dest="question_set")
    parser.add_argument("--world", required=True)
    parser.add_argument("--work", type=Path, required=True)
    parser.add_argument("--only", nargs="*", help="run only these question ids")
    args = parser.parse_args(argv)
    work = _outside_repo(args.work)
    questions = load_set(args.question_set)
    if args.only:
        questions = [q for q in questions if q["id"] in set(args.only)]
    summary = run_pass(questions=questions, world_key=args.world, work=work)
    print(json.dumps({k: v for k, v in summary.items() if k != "pending_ids"}, indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
