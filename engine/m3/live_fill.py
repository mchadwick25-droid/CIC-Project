"""A live model answers the requests a test-set run has written to disk, in place of whoever wrote the
reply files by hand. The run itself is unchanged: the same prompts, the same reply files, the same
steps after them (engine.m3.test100, test100_bound, test100_check), so every prompt, reply and rating
stays saved and can be scored again.

  python -m engine.m3.live_fill pending --work DIR --region R --live-test NAME --cap-usd N --authorized-by WHO [--only q001 ...]
  python -m engine.m3.live_fill check   --work DIR --stage read|rewrite|reread --region R --live-test NAME --cap-usd N --authorized-by WHO [--only ...]

`pending` answers each `pending/<key>.request.json` with no reply yet: a voice request is answered
with the voice model, streamed as in the conversation path; a forced-tool request (the safety and
reader gates) is answered with the gate model through the same forced tool call. `check` answers each
`check/<stage>/prompts/<question>.md` with no reply yet, with the voice model.

Billed calls: the command goes through the spend guard (engine.provider.guard), so it is refused
without a live-test name and a dollar cap, announces its models and cap before the first call, stops
before the cap and appends every call to the guard's ledger. Every setting is passed on the command
or fixed here and printed first (`--settings-only` prints them and exits before any call).
"""
import argparse
import json
import re
import sys
from pathlib import Path

from engine.provider import guard

VOICE_MAX_TOKENS = 2048
VOICE_TIMEOUT = 90.0
GATE_MAX_TOKENS = 512
GATE_TIMEOUT = 60.0
CHECK_MAX_TOKENS = {"read": 4096, "rewrite": 2048, "reread": 4096}
CHECK_TIMEOUT = 120.0
_SECTION = re.compile(r"\ASYSTEM\n(?P<system>.*?)\n\nUSER\n(?P<user>.*)\Z", re.DOTALL)


def settings(args) -> dict:
    return {
        "mode": args.mode, "work": str(args.work), "stage": getattr(args, "stage", None), "only": args.only or "all",
        "region": args.region, "voice_model_pattern": args.voice_model, "gate_model_pattern": args.gate_model,
        "voice": {"max_tokens": VOICE_MAX_TOKENS, "timeout_s": VOICE_TIMEOUT, "streamed": True, "temperature": "SDK default (not passed)"},
        "gate": {"max_tokens": GATE_MAX_TOKENS, "timeout_s": GATE_TIMEOUT, "forced_tool": True, "temperature": "SDK default (not passed)"},
        "check_max_tokens": CHECK_MAX_TOKENS, "check_timeout_s": CHECK_TIMEOUT, "system_prompt_cache": "ephemeral cache mark on the last system block",
        "authorized_by": args.authorized_by,
    }


def pending_jobs(work: Path, only: list[str] | None) -> list[dict]:
    jobs = []
    for request_path in sorted((work / "pending").glob("*.request.json")):
        key = request_path.name[: -len(".request.json")]
        question = key.split(".")[0]
        if only and question not in only:
            continue
        request = json.loads(request_path.read_text(encoding="utf-8"))
        extension = "txt" if request["kind"] == "voice" else "json"
        reply = work / "replies" / f"{key}.{extension}"
        if not reply.exists():
            jobs.append({"key": key, "request": request, "reply": reply})
    return jobs


def check_jobs(work: Path, stage: str, only: list[str] | None) -> list[dict]:
    jobs = []
    for prompt in sorted((work / "check" / stage / "prompts").glob("*.md")):
        if only and prompt.stem not in only:
            continue
        reply = work / "check" / stage / "replies" / f"{prompt.stem}.txt"
        if not reply.exists():
            jobs.append({"key": prompt.stem, "prompt": prompt, "reply": reply})
    return jobs


def _system_blocks(request: dict) -> list[dict]:
    blocks = [{"type": "text", "text": Path(p).read_text(encoding="utf-8")} for p in request["system_files"]]
    if blocks:
        blocks[-1]["cache_control"] = {"type": "ephemeral"}
    return blocks


def answer_pending(client, job: dict, voice_model: str, gate_model: str) -> str:
    request = job["request"]
    messages = [{"role": m["role"], "content": m["text"]} for m in request["messages"]]
    system = _system_blocks(request)
    if request["kind"] == "voice":
        chunks = []
        with client.messages.stream(model=voice_model, max_tokens=VOICE_MAX_TOKENS, system=system, messages=messages, timeout=VOICE_TIMEOUT) as stream:
            for text in stream.text_stream:
                chunks.append(text)
        return "".join(chunks)
    tool = {"name": request["kind"], "description": "Report the result.", "input_schema": request["reply_schema"]}
    response = client.messages.create(
        model=gate_model, max_tokens=GATE_MAX_TOKENS, system=system, tools=[tool], tool_choice={"type": "tool", "name": tool["name"]},
        messages=messages, timeout=GATE_TIMEOUT,
    )
    block = next(b for b in response.content if getattr(b, "type", None) == "tool_use")
    return json.dumps(block.input, ensure_ascii=False)


def answer_check(client, job: dict, stage: str, voice_model: str) -> str:
    parts = _SECTION.match(job["prompt"].read_text(encoding="utf-8"))
    if parts is None:
        raise ValueError(f"{job['prompt']}: not a SYSTEM/USER prompt file")
    response = client.messages.create(
        model=voice_model, max_tokens=CHECK_MAX_TOKENS[stage], system=parts["system"], messages=[{"role": "user", "content": parts["user"]}],
        timeout=CHECK_TIMEOUT,
    )
    return "".join(b.text for b in response.content if getattr(b, "type", None) == "text")


def run(args, client, voice_model: str, gate_model: str) -> dict:
    jobs = pending_jobs(args.work, args.only) if args.mode == "pending" else check_jobs(args.work, args.stage, args.only)
    done = 0
    for job in jobs:
        text = answer_pending(client, job, voice_model, gate_model) if args.mode == "pending" else answer_check(client, job, args.stage, voice_model)
        job["reply"].parent.mkdir(parents=True, exist_ok=True)
        job["reply"].write_text(text, encoding="utf-8")
        done += 1
        print(f"answered {job['key']} ({len(text)} characters)", flush=True)
    return {"answered": done}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("mode", choices=("pending", "check"))
    parser.add_argument("--work", type=Path, required=True)
    parser.add_argument("--stage", choices=tuple(CHECK_MAX_TOKENS))
    parser.add_argument("--only", nargs="*")
    parser.add_argument("--region", required=True)
    parser.add_argument("--voice-model", required=True, help="inference profile id or pattern; must match exactly one live profile")
    parser.add_argument("--gate-model", required=True, help="inference profile id or pattern for the safety and reader calls")
    parser.add_argument("--authorized-by", required=True)
    parser.add_argument("--settings-only", action="store_true")
    guard.add_arguments(parser)
    args = parser.parse_args(argv)
    if args.mode == "check" and not args.stage:
        parser.error("check needs --stage")
    print(json.dumps(settings(args), indent=1), flush=True)
    jobs = pending_jobs(args.work, args.only) if args.mode == "pending" else check_jobs(args.work, args.stage, args.only)
    kinds = {}
    for job in jobs:
        kind = job["request"]["kind"] if args.mode == "pending" else args.stage
        kinds[kind] = kinds.get(kind, 0) + 1
    print(json.dumps({"calls_to_make": len(jobs), "by_kind": kinds}), flush=True)
    if args.settings_only:
        return 0
    from engine.provider.bedrock import make_client, resolve_model_id

    client = make_client(args.region)
    voice_model = resolve_model_id(args.voice_model, args.region)
    gate_model = resolve_model_id(args.gate_model, args.region)
    guard.note_model(voice_model)
    guard.note_model(gate_model)
    print(json.dumps({**run(args, client, voice_model, gate_model), "run": guard.run_summary()}, default=str), flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
