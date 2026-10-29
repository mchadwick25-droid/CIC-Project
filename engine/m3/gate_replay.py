"""The current gates' decision on every sentence of a saved admission draft,
replayed at the commit the run was made at. No model call.

The admission run saved each probe's draft (`raw_text`) and what shipped
(`answer_text`). This passes the saved draft through the same answerer the
run used (engine.m3.generation.LiveModelAnswerer) with a client that returns
the draft instead of calling a model, and keeps the shaper's net_result,
which the answerer itself discards. It reads the sealed probe wording to
rebuild the turn's evidence and placement exactly; that wording is never
written out (probes are named by probe_id only), which is why this lives in
engine/m3, the one authorized reader.

Run it with the engine of the run's own commit, from a worktree at that
commit with its package restored:

  cd <worktree at the run's repo_commit>
  python -m engine.m2.cli restore <world>
  python <this file> --worktree . --report <run report.json> --out <decisions.jsonl>

One line per draft sentence: world, probe_id, the sentence as drafted, the
gates' verdict and reason, and whether it was removed. The run's shipped
answer must come back unchanged for every probe, text and citations alike, or the replay stops.
"""
import argparse
import json
import sys
from pathlib import Path


class _SavedDraftStream:
    def __init__(self, text: str):
        self.text_stream = iter([text])
        self._text = text

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False

    def get_final_message(self):
        usage = type("Usage", (), {"input_tokens": 0, "output_tokens": 0, "cache_creation_input_tokens": 0, "cache_read_input_tokens": 0})()
        return type("Message", (), {"usage": usage, "stop_reason": "end_turn"})()


class SavedDraftClient:
    """Stands where the model client stood: hands back the saved draft."""

    def __init__(self):
        self.draft = ""
        self.messages = self

    def stream(self, **_kwargs):
        return _SavedDraftStream(self.draft)


def replay(report: dict, worktree: Path) -> list[dict]:
    sys.path.insert(0, str(worktree.resolve()))
    from engine.m1.loader import load_fleet_records
    from engine.m1.registry import load_registry
    from engine.m3 import generation
    from engine.m3.sealed_probes import read_probe
    from engine.m4.world_loader import LazyWorldLoader

    captured: list[dict] = []
    real_apply_net = generation.apply_net

    def keeping_net_result(*args, **kwargs):
        text, citations, net_result = real_apply_net(*args, **kwargs)
        captured.append(net_result)
        return text, citations, net_result

    generation.apply_net = keeping_net_result
    try:
        return _replay_worlds(report, worktree, generation, captured, read_probe, load_fleet_records, load_registry, LazyWorldLoader)
    finally:
        generation.apply_net = real_apply_net


def _replay_worlds(report, worktree, generation, captured, read_probe, load_fleet_records, load_registry, LazyWorldLoader) -> list[dict]:
    registry = load_registry()
    canon_questions = load_fleet_records()
    loader = LazyWorldLoader()
    rows: list[dict] = []
    for world, block in report["worlds"].items():
        entry = registry[world]
        want = report["run_settings"]["package_manifest_hash"][world]
        if entry["package"]["manifest_hash"] != want:
            raise SystemExit(f"{world}: the worktree pins {entry['package']['manifest_hash']}, the run pinned {want}")
        loaded, _timing = loader.load(world, package_dir=worktree / entry["package"]["location"], expected_manifest_hash=want)
        client = SavedDraftClient()
        answerer = generation.LiveModelAnswerer(world=loaded, canon_questions=canon_questions, client=client, model_id=report["voice_model_id"])
        for probe in block["per_probe"]:
            transcript = probe.get("transcript") or {}
            if not transcript.get("raw_text"):
                continue
            client.draft = transcript["raw_text"]
            captured.clear()
            result = answerer.answer(probe["cell"], read_probe(probe["probe_id"])["text"])
            if result.text != transcript["answer_text"]:
                raise SystemExit(f"{world} {probe['probe_id']}: the replay does not reproduce the shipped answer")
            saved = [(e["sentence"], list(e["record_ids"])) for e in transcript.get("citation_entries") or [] if not e.get("attached")]
            if [(e["sentence"], list(e["record_ids"])) for e in result.citation_entries] != saved:
                raise SystemExit(f"{world} {probe['probe_id']}: the replay does not reproduce the shipped citations")
            net_result = captured[-1]
            for entry_ in net_result["sentences"]:
                rows.append({
                    "world": world, "probe_id": probe["probe_id"], "draft": entry_.get("draft") or entry_["sentence"],
                    "shown": entry_["sentence"], "verdict": entry_["verdict"], "why": entry_.get("why"), "removed": False,
                    "cited": entry_["verdict"] == "ok" and bool(entry_.get("tags")),
                })
            for gone in net_result["reply_shape"]["removed"]:
                rows.append({
                    "world": world, "probe_id": probe["probe_id"], "draft": gone.get("draft") or gone["sentence"],
                    "shown": None, "verdict": "withhold", "why": gone["why"], "removed": True, "cited": False,
                })
    return rows


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--worktree", type=Path, required=True)
    parser.add_argument("--report", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args(argv)
    rows = replay(json.loads(args.report.read_text(encoding="utf-8")), args.worktree)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text("".join(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n" for r in rows), encoding="utf-8")
    probes = {(r["world"], r["probe_id"]) for r in rows}
    print(json.dumps({"probes_reproduced": len(probes), "sentences": len(rows), "removed": sum(r["removed"] for r in rows)}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
