"""The V7 controlled-test runner: sealed probes answered through the admission
answering core, one probe at a time, with arm b's reading-context switch set
in memory on the loaded world.

Each probe runs the admission pipeline: evidence assembly with no reader asks,
placeable stories where the world places them, the rendered evidence block
ahead of the probe, one voice call against the cached world prompt (asked
again on a failed stream, up to three calls), then apply_net with quote
placement. There is no gate, turn directive, recitation retry or
self-revision. Each answered probe is appended to --out as one JSON line the
moment it returns; <out>.summary.json holds the run settings, the totals and
the live-test summary.

Every paid setting is named on the command: --model-id, --region,
--max-tokens. A live run also carries --live-test and --cap-usd
(engine.provider.guard); without them, and without --reply-files, the command
exits 2 before it loads a world or builds a client. --expect-package-hash
stops the run before any call when the registered package differs.

--reply-files <dir> answers every voice call from <dir>/<probe>.voice.<n>.txt,
the raw tagged text the model would have streamed. A call with no reply file
writes its request to <dir>/pending/ and the probe is left unanswered (exit
4). The requests carry sealed probe wording, so <dir> must lie outside the
repository.

--project-cost prints the mean priced cost per turn of the records in --out,
the projection for --remaining further turns, and whether spent plus that
projection passes --stop-above (exit 3 if it does). Given with probes, it runs
after them over the records this run wrote.

Exit codes: 0 done, 1 stopped (cap reached or a failed call), 2 refused,
3 projection past the threshold, 4 replies pending.
"""
import argparse
import dataclasses
import inspect
import json
import os
import subprocess
import sys
import time
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path

from engine.m1 import canon
from engine.m1.loader import load_fleet_records, load_world_records
from engine.m1.registry import load_registry
from engine.m2.manifest import package_content_hash
from engine.m3 import grading, harness, protocol, sealed_probes
from engine.m3.masking import mask_for_grading
from engine.m4 import evidence as m4_evidence
from engine.m4.generation import stream_voice_turn
from engine.m4.quote_placement import PlacementContext
from engine.m4.story_placement import with_placeable_stories
from engine.m4.turn import apply_net
from engine.m4.world_loader import LazyWorldLoader
from engine.m8.cost import estimate_cost
from engine.m8.price_tables import price_for_route
from engine.provider import guard
from engine.provider.bedrock import NormalizedUsage, make_client, normalize_usage

REPO_ROOT = Path(__file__).resolve().parents[2]
WORLDS = ("alx", "pahc", "syr")
ARMS = ("a", "b")
READING_CONTEXT = "reading_context"
VOICE_CALL_ATTEMPTS = 3
CALL_KIND = "voice_generation"
PROVIDER = "bedrock"

EXIT_DONE = 0
EXIT_STOPPED = 1
EXIT_REFUSED = guard.EXIT_REFUSED
EXIT_PROJECTION = 3
EXIT_PENDING = 4


class PendingReply(Exception):
    """A dry-mode call with no reply file yet; its request is written to the pending directory."""


class _ReplyStream:
    def __init__(self, text: str):
        self.text_stream = iter([text] if text else [])
        self._text = text

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False

    def get_final_message(self):
        usage = type("Usage", (), {"input_tokens": 0, "output_tokens": 0, "cache_creation_input_tokens": 0, "cache_read_input_tokens": 0})()
        block = type("Block", (), {"type": "text", "text": self._text})()
        return type("Message", (), {"usage": usage, "stop_reason": "end_turn", "content": [block]})()


class ReplyFileClient:
    """Stands where the model client stands and answers each voice call
    from <reply_dir>/<probe>.voice.<n>.txt."""

    def __init__(self, reply_dir: Path):
        self.reply_dir = reply_dir
        self.pending_dir = reply_dir / "pending"
        self.messages = self
        self.probe_id: str | None = None
        self._count = 0

    def start_probe(self, probe_id: str) -> None:
        self.probe_id = probe_id
        self._count = 0

    def stream(self, **kwargs):
        self._count += 1
        key = f"{self.probe_id}.voice.{self._count}"
        path = self.reply_dir / f"{key}.txt"
        if path.exists():
            return _ReplyStream(path.read_text(encoding="utf-8"))
        self.pending_dir.mkdir(parents=True, exist_ok=True)
        system = kwargs.get("system")
        request = {
            "model": kwargs.get("model"),
            "max_tokens": kwargs.get("max_tokens"),
            "system": [system] if isinstance(system, str) else [b.get("text", "") for b in system or []],
            "messages": kwargs.get("messages", []),
            "reply_file": str(path),
        }
        (self.pending_dir / f"{key}.request.json").write_text(json.dumps(request, ensure_ascii=False, indent=1), encoding="utf-8")
        raise PendingReply(key)


class _TimedStream:
    def __init__(self, inner, call: dict):
        self._inner = inner
        self._call = call
        self.text_stream = self._timed(inner.text_stream)

    def _timed(self, chunks):
        for chunk in chunks:
            if self._call["seconds_to_first_text"] is None:
                self._call["seconds_to_first_text"] = round(time.monotonic() - self._call["_started"], 3)
            yield chunk

    def get_final_message(self):
        message = self._inner.get_final_message()
        self._call["usage"] = normalize_usage(message.usage)
        self._call["stop_reason"] = getattr(message, "stop_reason", None)
        self._call["raw_text"] = "".join(
            getattr(block, "text", "") for block in (getattr(message, "content", None) or []) if getattr(block, "type", None) == "text"
        )
        return message


class _TimedStreamContext:
    def __init__(self, inner_ctx, call: dict):
        self._inner_ctx = inner_ctx
        self._call = call

    def __enter__(self):
        return _TimedStream(self._inner_ctx.__enter__(), self._call)

    def __exit__(self, *exc):
        try:
            return self._inner_ctx.__exit__(*exc)
        finally:
            self._call["seconds_total"] = round(time.monotonic() - self._call["_started"], 3)


class TimedClient:
    """Passes each messages.stream call to the inner client and keeps, per
    call, the request, the time to the first text chunk, the total time,
    the usage, the stop reason and the raw text."""

    def __init__(self, inner):
        self.inner = inner
        self.messages = self
        self.calls: list[dict] = []

    def stream(self, **kwargs):
        call = {
            "request": kwargs, "seconds_to_first_text": None, "seconds_total": None, "usage": None,
            "stop_reason": None, "raw_text": None, "_started": time.monotonic(),
        }
        self.calls.append(call)
        return _TimedStreamContext(self.inner.messages.stream(**kwargs), call)


def render_block(turn_evidence: dict, world) -> str:
    """The evidence block. A render_evidence_block that takes the loaded
    world is given it, so a switch on world.frame reaches the render."""
    if "world" in inspect.signature(m4_evidence.render_evidence_block).parameters:
        return m4_evidence.render_evidence_block(turn_evidence, world=world)
    return m4_evidence.render_evidence_block(turn_evidence)


def _flag_off(world):
    return dataclasses.replace(world, frame={k: v for k, v in world.frame.items() if k != READING_CONTEXT})


class V7Answerer:
    """The admission answering core for one loaded world."""

    def __init__(self, *, world, canon_questions: dict, client: TimedClient, model_id: str, max_tokens: int):
        self.world = world
        self.canon_questions = canon_questions
        self.client = client
        self.model_id = model_id
        self.max_tokens = max_tokens
        self.repository_records = m4_evidence.repository_records_by_id(world.repository)
        self.thin_topics = m4_evidence.thin_topics_for(self.repository_records)

    def prepare(self, probe_text: str) -> dict:
        turn_evidence = m4_evidence.assemble_evidence(
            message=probe_text,
            asks=None,
            canon_questions=self.canon_questions,
            coverage=self.world.coverage,
            repository_records=self.repository_records,
            thin_topics=self.thin_topics,
        )
        if self.world.frame.get("story_placement"):
            turn_evidence = with_placeable_stories(turn_evidence, self.repository_records)
        block = render_block(turn_evidence, self.world)
        block_off = render_block(turn_evidence, _flag_off(self.world))
        user_message = f"{block}\n{probe_text}" if turn_evidence["candidates"] else probe_text
        return {"turn_evidence": turn_evidence, "block": block, "block_off": block_off, "user_message": user_message}

    def answer(self, probe_text: str) -> dict:
        prepared = self.prepare(probe_text)
        turn_evidence = prepared["turn_evidence"]
        first_call = len(self.client.calls)
        for _attempt in range(VOICE_CALL_ATTEMPTS):
            outcome = stream_voice_turn(
                self.client, self.model_id, system_prompt=self.world.prompt_text, message=prepared["user_message"],
                max_tokens=self.max_tokens,
            )
            if outcome.status == "ok":
                break
        calls = self.client.calls[first_call:]
        if outcome.status != "ok":
            raise VoiceCallFailed(f"voice call failed after {len(calls)} attempts: {outcome.status} {outcome.value}", calls)
        text, citation_entries, _net_result = apply_net(
            outcome.value.text, repository_records=self.repository_records, thin_topics=self.thin_topics,
            quotable_texts=[probe_text], window_end=(self.world.frame.get("time_window") or {}).get("end"),
            placement=PlacementContext.for_evidence(
                turn_evidence["candidates"],
                offered_stories=frozenset(c["id"] for c in turn_evidence["candidates"] if c.get("placeable")),
            ),
        )
        return {
            "text": text,
            "citation_entries": citation_entries,
            "citations": sorted({rid for entry in citation_entries for rid in entry["record_ids"]}),
            "offered_record_ids": [c["id"] for c in turn_evidence["candidates"]],
            "evidence_chars": len(prepared["block"]),
            "evidence_chars_flag_off": len(prepared["block_off"]),
            "calls": calls,
        }


class VoiceCallFailed(RuntimeError):
    def __init__(self, message: str, calls: list[dict]):
        super().__init__(message)
        self.calls = calls


class _Grader:
    """The admission battery's per-probe grading (engine.m3.harness.run_battery)."""

    def __init__(self, world_key: str):
        records = load_world_records(world_key)
        self.records = records
        self.known_source_ids = harness._transitive_source_ids(records)
        self.evidence_status_ids = {r["id"] for r in records.values() if r.get("record_type") in canon.evidence_status_types()}
        self.known_quote_texts = {r["text"] for r in records.values() if r.get("record_type") == "quote" and r.get("text")}

    def grade(self, *, probe_id: str, cell: str, probe_text: str, answer: dict) -> tuple[bool, list[dict]]:
        transcript = mask_for_grading(
            probe_id=probe_id, cell=cell, probe_text=probe_text, answer_text=answer["text"], citations=answer["citations"],
            citation_entries=answer["citation_entries"],
        )
        checks = [
            grading.source_boundedness_check(transcript, self.known_source_ids, evidence_status_ids=self.evidence_status_ids,
                                             repository_records=self.records),
            grading.register_check(transcript, self.known_quote_texts),
        ]
        return all(c.passed for c in checks), [asdict(c) for c in checks]


def project_cost(records: list[dict], *, remaining: int, stop_above: float) -> dict:
    """The mean priced cost per turn, scaled to `remaining` further turns,
    and whether spent plus that projection passes `stop_above`."""
    costs = [r["priced_usd"] for r in records if r.get("priced_usd") is not None]
    spent = sum(costs)
    mean = spent / len(costs) if costs else 0.0
    further = mean * remaining
    return {
        "turns": len(costs),
        "spent_usd": round(spent, 6),
        "mean_usd_per_turn": round(mean, 6),
        "remaining_turns": remaining,
        "projected_further_usd": round(further, 6),
        "projected_total_usd": round(spent + further, 6),
        "stop_above_usd": stop_above,
        "passes_threshold": spent + further > stop_above,
    }


def _repo_commit() -> str | None:
    try:
        return subprocess.run(["git", "rev-parse", "HEAD"], cwd=REPO_ROOT, capture_output=True, text=True, check=True).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return None


def _inside_repo(path: Path) -> bool:
    resolved = path.resolve()
    return resolved == REPO_ROOT or REPO_ROOT in resolved.parents


def select_probes(probes: str | None, probe_file: str | None) -> list[dict]:
    """The battery entries named, in the order named; 'all' is the whole battery in battery order."""
    battery = protocol.battery()
    by_id = {seal["probe_id"]: seal for seal in battery}
    if probe_file is not None:
        lines = Path(probe_file).read_text(encoding="utf-8").splitlines()
        ids = [line.split("#", 1)[0].strip() for line in lines]
    elif probes.strip() == "all":
        return list(battery)
    else:
        ids = probes.split(",")
    ids = [i.strip() for i in ids if i.strip()]
    unknown = [i for i in ids if i not in by_id]
    if unknown:
        raise SystemExit(f"not in the sealed battery: {unknown}")
    if len(set(ids)) != len(ids):
        raise SystemExit("a probe is named more than once")
    return [by_id[i] for i in ids]


def _append(path: Path, line: dict) -> None:
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps(line, ensure_ascii=False) + "\n")
        f.flush()
        os.fsync(f.fileno())


def _priced(calls: list[dict], table) -> float:
    return sum(estimate_cost(call["usage"], table).dollars for call in calls if call["usage"] is not None)


def _usage(call: dict | None) -> dict | None:
    usage = call["usage"] if call else None
    return asdict(usage) if isinstance(usage, NormalizedUsage) else None


def _record(*, seal: dict, args, settings: dict, answer: dict, passed: bool, checks: list[dict], priced_usd: float) -> dict:
    last = answer["calls"][-1]
    return {
        "probe_id": seal["probe_id"],
        "cell": seal["cell"],
        "arm": args.arm,
        "world": args.world,
        "passed": passed,
        "checks": checks,
        "answer_text": answer["text"],
        "raw_text": last["raw_text"],
        "citations": answer["citations"],
        "citation_entries": answer["citation_entries"],
        "offered_record_ids": answer["offered_record_ids"],
        "usage": _usage(last),
        "seconds_to_first_text": last["seconds_to_first_text"],
        "seconds_total": last["seconds_total"],
        "stop_reason": last["stop_reason"],
        "attempts": len(answer["calls"]),
        "priced_usd": round(priced_usd, 6),
        "model_id": args.model_id,
        "max_tokens": args.max_tokens,
        "region": args.region,
        "package_manifest_hash": settings["package_manifest_hash"],
        "repo_commit": settings["repo_commit"],
        "additions_chars": answer["evidence_chars"] - answer["evidence_chars_flag_off"],
        "evidence_chars": answer["evidence_chars"],
        "evidence_chars_flag_off": answer["evidence_chars_flag_off"],
    }


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    guard.add_arguments(parser)
    parser.add_argument("--world", choices=WORLDS)
    parser.add_argument("--arm", choices=ARMS)
    which = parser.add_mutually_exclusive_group()
    which.add_argument("--probes", help="comma-separated sealed probe ids, or 'all'")
    which.add_argument("--probe-file", help="one sealed probe id per line; '#' starts a comment")
    parser.add_argument("--out", required=True, help="JSON-lines record file; a run refuses one that exists")
    parser.add_argument("--model-id", help="the exact voice model id")
    parser.add_argument("--region")
    parser.add_argument("--max-tokens", type=int)
    parser.add_argument("--expect-package-hash", help="the world's package manifest hash the run must use")
    parser.add_argument("--reply-files", help="answer every voice call from reply files in this directory (no model call)")
    parser.add_argument("--project-cost", action="store_true")
    parser.add_argument("--remaining", type=int, help="with --project-cost: the further turns to project")
    parser.add_argument("--stop-above", type=float, help="with --project-cost: the dollar threshold for spent plus projection")
    return parser


def _print_projection(records: list[dict], args) -> int:
    projection = project_cost(records, remaining=args.remaining, stop_above=args.stop_above)
    print(json.dumps({"projection": projection}, indent=2), flush=True)
    return EXIT_PROJECTION if projection["passes_threshold"] else EXIT_DONE


def main(argv: list[str] | None = None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    parser = _parser()
    args = parser.parse_args(argv)
    if args.project_cost and (args.remaining is None or args.stop_above is None):
        parser.error("--project-cost needs --remaining and --stop-above")
    runs = args.probes is not None or args.probe_file is not None
    out = Path(args.out)
    if not runs:
        if not args.project_cost:
            parser.error("name the probes with --probes or --probe-file, or pass --project-cost")
        return _print_projection([json.loads(line) for line in out.read_text(encoding="utf-8").splitlines() if line.strip()], args)

    missing = [flag for flag, value in (("--world", args.world), ("--arm", args.arm), ("--model-id", args.model_id),
                                        ("--region", args.region), ("--max-tokens", args.max_tokens),
                                        ("--expect-package-hash", args.expect_package_hash)) if value is None]
    if missing:
        parser.error(f"a run names every setting on the command: {', '.join(missing)}")
    if args.max_tokens <= 0:
        parser.error("--max-tokens must be positive")
    dry = args.reply_files is not None
    if dry and _inside_repo(Path(args.reply_files)):
        raise SystemExit(f"{args.reply_files} is inside the repository; the reply directory must be outside it")
    if not dry and guard.parse_live_test(argv) is None:
        print(guard.RULE, file=sys.stderr, flush=True)
        return EXIT_REFUSED
    if out.exists():
        raise SystemExit(f"{out} exists; a run writes a new record file")
    table = price_for_route(CALL_KIND, args.model_id, PROVIDER)
    if table is None:
        raise SystemExit(f"no approved price for model {args.model_id!r}")

    seals = select_probes(args.probes, args.probe_file)
    entry = load_registry()[args.world]
    registered = entry["package"]["manifest_hash"]
    if args.expect_package_hash != registered:
        raise SystemExit(
            f"--expect-package-hash {args.expect_package_hash} does not match {args.world}'s registered package hash "
            f"{registered}; stopped before any call"
        )
    package_dir = REPO_ROOT / entry["package"]["location"]
    world, _timing = LazyWorldLoader().load(args.world, package_dir=package_dir, expected_manifest_hash=args.expect_package_hash)
    if args.arm == "b":
        world = dataclasses.replace(world, frame={**world.frame, READING_CONTEXT: True})

    live_test = None if dry else guard.parse_live_test(argv)
    settings = {
        "live_test": live_test.name if live_test else None,
        "cap_usd": live_test.cap_usd if live_test else None,
        "mode": "reply files" if dry else "live",
        "model_id": args.model_id,
        "region": args.region,
        "max_tokens": args.max_tokens,
        "route": guard.describe_route(PROVIDER, [args.model_id], args.region),
        "price_source": table.source,
        "world": args.world,
        "arm": args.arm,
        "reading_context": world.frame.get(READING_CONTEXT, False),
        "probe_count": len(seals),
        "package_manifest_hash": registered,
        "package_content_hash": package_content_hash(package_dir),
        "path": "admission answering core: evidence assembly, one voice call, apply_net; no gate, directive, retry or self-revision",
        "voice_call_attempts": VOICE_CALL_ATTEMPTS,
        "repo_commit": _repo_commit(),
    }
    print(json.dumps({"run_settings": settings}, indent=2), flush=True)

    if dry:
        inner = ReplyFileClient(Path(args.reply_files))
    else:
        guard.note_model(args.model_id)
        inner = make_client(args.region)
    client = TimedClient(inner)
    answerer = V7Answerer(world=world, canon_questions=load_fleet_records(), client=client, model_id=args.model_id,
                          max_tokens=args.max_tokens)
    grader = _Grader(args.world)

    out.parent.mkdir(parents=True, exist_ok=True)
    out.touch()
    started_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
    written: list[dict] = []
    pending: list[str] = []
    stopped = None
    for seal in seals:
        probe_id = seal["probe_id"]
        probe_text = sealed_probes.read_probe(probe_id)["text"]
        if dry:
            inner.start_probe(probe_id)
        spent_before = guard.priced_total()
        try:
            answer = answerer.answer(probe_text)
        except PendingReply as reply:
            pending.append(str(reply))
            continue
        except guard.LiveTestCapReached as error:
            stopped = f"cap reached before {probe_id}: {error}"
            break
        except VoiceCallFailed as error:
            stopped = f"{probe_id}: {error}"
            break
        priced_usd = guard.priced_total() - spent_before if live_test else _priced(answer["calls"], table)
        passed, checks = grader.grade(probe_id=probe_id, cell=seal["cell"], probe_text=probe_text, answer=answer)
        record = _record(seal=seal, args=args, settings=settings, answer=answer, passed=passed, checks=checks, priced_usd=priced_usd)
        _append(out, record)
        written.append(record)

    summary = {
        "run_settings": settings,
        "started_at": started_at,
        "finished_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "turns": len(written),
        "priced_usd": round(sum(r["priced_usd"] for r in written), 6),
        "pending_replies": pending,
        "stopped": stopped,
        "live_test": guard.run_summary(),
        "ledger": guard.ledger_path() if live_test else None,
    }
    Path(f"{out}.summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: summary[k] for k in ("turns", "priced_usd", "stopped", "live_test")} | {"pending_replies": len(pending)}, indent=2),
          flush=True)

    if stopped:
        return EXIT_STOPPED
    if pending:
        return EXIT_PENDING
    if args.project_cost:
        return _print_projection(written, args)
    return EXIT_DONE


if __name__ == "__main__":
    sys.exit(main())
