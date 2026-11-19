"""Extract arm A of the V7 controlled test (Spec V1) into ../Set/.

A is fleet graded run 1 for alx, pahc and syr. Its files are on branch
claude/fleet-run-1-analysis only, in the engine's m3 reports folder
fleet-graded-run-1. They are read with `git show`, never checked out.

No probe text, no draft text and no request is written out. Probes are
named by probe id and cell only.

    python3 -I Build/Ministry/Features/V7-Controlled-Test/tools/extract_a.py [--out DIR]
"""
import argparse
import hashlib
import json
import random
import re
import subprocess
from pathlib import Path

import yaml

SEED = 20261103  # written before the draw

WORLDS = ("alx", "pahc", "syr")
FAMILIES = ("C", "F1", "F2", "F3", "F4", "F5", "F6")
REGISTERS = ("I", "E", "P", "T")
PER_FAMILY = 2

SOURCE_REF = "origin/claude/fleet-run-1-analysis"
SOURCE_COMMIT = "4973efc8287e13ffcc775c198c1ca0f94234904d"  # that branch's head when A was frozen
RUN_DIR = "engine/m3/reports/fleet-graded-run-1/"
ANALYSIS_DIR = RUN_DIR + "analysis-2026-10-29/"
USAGE_FIELDS = ("input_tokens", "output_tokens", "cache_creation_input_tokens", "cache_read_input_tokens")
MARKER = re.compile(r"\[\[([^\[\]]+)\]\]")

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[4]
SET_DIR = HERE.parent / "Set"
QUESTION_SET = REPO / "Build/Ministry/Features/Answering-From-Sources/Cross-World-Test_2026-11-02/alx/set.yaml"


def git(*args: str) -> bytes:
    return subprocess.run(["git", *args], cwd=REPO, capture_output=True, check=True).stdout


def source_sha() -> str:
    """The pinned source commit, which must be present locally."""
    git("cat-file", "-e", SOURCE_COMMIT + "^{commit}")
    return SOURCE_COMMIT


def show(path: str, sha: str) -> bytes:
    return git("show", f"{sha}:{path}")


def show_json(path: str, sha: str):
    return json.loads(show(path, sha))


def show_jsonl(path: str, sha: str) -> list:
    return [json.loads(line) for line in show(path, sha).decode().splitlines() if line.strip()]


def run_probes(run: dict, world: str) -> list:
    probes = run["worlds"][world]["per_probe"]
    if len(probes) != 28:
        raise SystemExit(f"{world}: {len(probes)} probes, not 28")
    return probes


def settle_by_probe(probes: list, ledger: list, world: str) -> list:
    """One voice call per probe. Settle lines are in probe order, and each
    one's usage equals that probe's usage. Both must hold."""
    settles = [line for line in ledger if line["event"] == "settle"]
    if len(settles) != len(probes):
        raise SystemExit(f"{world}: {len(settles)} settle lines for {len(probes)} probes")
    for probe, settle in zip(probes, settles):
        if settle["usage"] != probe["usage"]:
            raise SystemExit(f"{world}: settle line out of step with {probe['probe_id']}")
    return [settle["priced_dollars"] for settle in settles]


def q_ids() -> dict:
    questions = yaml.safe_load(QUESTION_SET.read_text(encoding="utf-8"))["questions"]
    return {q["probe_id"]: (q["id"], q["cell"]) for q in questions}


def a_lines(world: str, run: dict, ledger: list, qmap: dict) -> list:
    probes = run_probes(run, world)
    priced = settle_by_probe(probes, ledger, world)
    lines = []
    for probe, usd in zip(probes, priced):
        t = probe["transcript"]
        if set(t["request"]) - {"model", "max_tokens"}:
            raise SystemExit(f"{world}: {probe['probe_id']} request holds more than model and max_tokens")
        q_id, q_cell = qmap[probe["probe_id"]]
        if q_cell != probe["cell"]:
            raise SystemExit(f"{world}: {probe['probe_id']} cell differs from the question set")
        lines.append({
            "world": world,
            "probe_id": probe["probe_id"],
            "cell": probe["cell"],
            "q_id": q_id,
            "answer_text": t["answer_text"],
            "citations": t["citations"],
            "citation_entries": t["citation_entries"],
            "offered_record_ids": None,
            "offered_record_ids_status": "not saved by the run: the request field holds only model and max_tokens",
            "draft_marker_ids": sorted(set(MARKER.findall(t["raw_text"]))),
            "usage": {k: probe["usage"][k] for k in USAGE_FIELDS},
            "seconds_to_first_text": t["seconds_to_first_text"],
            "seconds_total": t["seconds_total"],
            "stop_reason": t["stop_reason"],
            "priced_usd": usd,
            "run_checks_passed": probe["passed"],
        })
    return lines


def run_settings(runs: dict, ledgers: dict, sha: str) -> dict:
    worlds = {}
    for world in WORLDS:
        run = runs[world]
        rs = run["run_settings"]
        settles = [line for line in ledgers[world] if line["event"] == "settle"]
        worlds[world] = {
            "repo_commit": rs["repo_commit"],
            "voice_model_id": rs["voice_model_id"],
            "voice_max_tokens": rs["voice_max_tokens"],
            "voice_temperature": rs["voice_temperature"],
            "region": rs["region"],
            "package_manifest_hash": rs["package_manifest_hash"][world],
            "package_content_hash": rs["package_content_hash"][world],
            "shape_hash": rs["shape_hash"],
            "seal_hash": rs["seal_hash"],
            "battery_size": rs["battery_size"],
            "safety_call": rs["safety_call"],
            "reader_call": rs["reader_call"],
            "self_revision": rs["self_revision"],
            "live_test": sorted({line["live_test"] for line in ledgers[world]}),
            "ledger_settle_lines": len(settles),
            "ledger_priced_usd_total": sum(line["priced_dollars"] for line in settles),
            "report_actual_usd_spent": run["actual_usd_spent"],
        }
    return {"source_ref": SOURCE_REF.removeprefix("origin/"), "source_commit": sha, "source_folder": "fleet-graded-run-1", "worlds": worlds}


def reviews(world: str, run: dict, sha: str, key: dict) -> dict:
    probes = run_probes(run, world)
    second = show_json(f"{ANALYSIS_DIR}second-pass/{world}.json", sha)
    outside = show_json(f"{ANALYSIS_DIR}outside-referees/out-{world}.json", sha)
    packet = show(f"{ANALYSIS_DIR}outside-referees/{world}.md", sha)

    by_probe_second = {}
    for answer in second["answers"]:
        probe = probes[answer["n"] - 1]
        if probe["cell"] != answer["cell"]:
            raise SystemExit(f"{world}: second-pass n={answer['n']} cell differs from the run")
        by_probe_second[probe["probe_id"]] = answer
    if len(by_probe_second) != 28:
        raise SystemExit(f"{world}: second pass covers {len(by_probe_second)} probes")

    by_probe_outside = {}
    for item in outside["items"]:
        entry = key[f"{world}:{item['item']}"]
        probe = probes[entry["n"] - 1]
        if probe["cell"] != entry["cell"]:
            raise SystemExit(f"{world}: referee item {item['item']} cell differs from the run")
        if not packet_holds_answer(packet.decode(), item["item"], probe["transcript"]["answer_text"]):
            raise SystemExit(f"{world}: referee packet item {item['item']} does not hold {probe['probe_id']}'s answer")
        by_probe_outside[probe["probe_id"]] = {"cell": probe["cell"], "n": entry["n"], **item}

    return {
        "world": world,
        "source_ref": SOURCE_REF.removeprefix("origin/"),
        "source_commit": sha,
        "second_pass": {
            "file": "analysis-2026-10-29/second-pass/" + world + ".json",
            "rubric_file": "analysis-2026-10-29/RUBRIC.md",
            "world_summary": second["world_summary"],
            "by_probe": by_probe_second,
        },
        "outside_referees": {
            "file": "analysis-2026-10-29/outside-referees/out-" + world + ".json",
            "key_file": "analysis-2026-10-29/outside-referees/KEY.json",
            "packet_file": "analysis-2026-10-29/outside-referees/" + world + ".md",
            "packet_sha256": hashlib.sha256(packet).hexdigest(),
            "packet_copied": False,
            "world_label": outside["world"],
            "checks_performed": outside.get("checks_performed", []),
            "overall_view": outside["overall_view"],
            "items_reviewed": len(outside["items"]),
            "by_probe": by_probe_outside,
        },
    }


def _words(text: str) -> str:
    return " ".join(re.findall(r"\w+", text.lower()))


def packet_holds_answer(packet: str, item: int, answer_text: str) -> bool:
    parts = re.split(r"^## Item (\d+)\s*$", packet, flags=re.MULTILINE)
    sections = {int(parts[i]): parts[i + 1] for i in range(1, len(parts) - 1, 2)}
    return _words(answer_text) in _words(sections.get(item, ""))


def repeat_draw(seed: int = SEED) -> dict:
    """Per world: 2 cells per family, 14 in all, with each register drawn
    3 or 4 times (4+4+3+3). Worlds are drawn in a fixed order from one
    generator, so the draw depends only on the seed."""
    rng = random.Random(seed)
    worlds = {}
    for world in WORLDS:
        heavy = rng.sample(REGISTERS, 2)
        target = {r: (4 if r in heavy else 3) for r in REGISTERS}
        while True:
            picks = {f: sorted(rng.sample(REGISTERS, PER_FAMILY), key=REGISTERS.index) for f in FAMILIES}
            counts = {r: sum(r in regs for regs in picks.values()) for r in REGISTERS}
            if counts == target:
                break
        cells = [f"{f}-{r}" for f in FAMILIES for r in picks[f]]
        worlds[world] = {
            "probe_ids": [f"{c.lower()}-probe-01" for c in cells],
            "cells": cells,
            "register_counts": target,
        }
    return {"seed": seed, "per_world": 2 * len(FAMILIES), "total": 2 * len(FAMILIES) * len(WORLDS), "worlds": worlds}


def write_json(path: Path, obj) -> None:
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_sums(out: Path) -> None:
    names = sorted(p.name for p in out.iterdir() if p.is_file() and p.name != "SHA256SUMS")
    lines = [f"{hashlib.sha256((out / n).read_bytes()).hexdigest()}  {n}" for n in names]
    (out / "SHA256SUMS").write_text("\n".join(lines) + "\n", encoding="utf-8")


def extract(out: Path) -> None:
    out.mkdir(parents=True, exist_ok=True)
    sha = source_sha()
    qmap = q_ids()
    key = show_json(f"{ANALYSIS_DIR}outside-referees/KEY.json", sha)
    runs = {w: show_json(f"{RUN_DIR}{w}.json", sha) for w in WORLDS}
    ledgers = {w: show_jsonl(f"{RUN_DIR}ledger-{w}.jsonl", sha) for w in WORLDS}
    for world in WORLDS:
        lines = a_lines(world, runs[world], ledgers[world], qmap)
        (out / f"A_{world}.jsonl").write_text(
            "".join(json.dumps(line, ensure_ascii=False) + "\n" for line in lines), encoding="utf-8")
        write_json(out / f"A_reviews_{world}.json", reviews(world, runs[world], sha, key))
    write_json(out / "A_run_settings.json", run_settings(runs, ledgers, sha))
    write_json(out / "repeat_draw.json", repeat_draw())
    write_sums(out)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, default=SET_DIR)
    extract(parser.parse_args().out)


if __name__ == "__main__":
    main()
