"""Totals for the operator's quality view: the quality-control store and the
latest daily audit rollup. Totals only. No question, answer or session id
leaves this module, so the view shows no conversation."""
import json
from pathlib import Path

from engine.m7.qc_store import QCStore
from engine.m7.scheduler import STATUS_FILENAME

ROLLUP_FILENAME = "fleet-rollup.json"


def _json_field(raw: str) -> dict:
    try:
        value = json.loads(raw)
    except (TypeError, ValueError):
        return {}
    return value if isinstance(value, dict) else {}


def _latest_rollup(m7_audit_root: Path | None) -> dict | None:
    if m7_audit_root is None:
        return None
    try:
        status = json.loads((m7_audit_root / STATUS_FILENAME).read_text())
        rollup = json.loads((Path(status["out_dir"]) / ROLLUP_FILENAME).read_text())
    except (OSError, ValueError, KeyError):
        return None
    return {
        "as_of_run": status.get("run_at"),
        "sessions_audited": rollup.get("sessions_audited", 0),
        "findings_by_severity": rollup.get("findings_by_severity", {}),
        "findings_by_instrument": rollup.get("findings_by_instrument", {}),
        "reading": rollup.get("register", {}),
    }


def get_quality_summary(qc_store: QCStore | None, m7_audit_root: Path | None = None) -> dict:
    by_world: dict[str, dict] = {}
    by_routing: dict[str, int] = {}
    weeks: set[str] = set()
    total = text_free = 0
    for row in qc_store.rows() if qc_store is not None else []:
        flags, marks, scores = _json_field(row["flags"]), _json_field(row["marks"]), _json_field(row["scores"])
        world = by_world.setdefault(row["world"], {
            "world": row["world"], "turns": 0, "conversations": set(), "text_free_turns": 0,
            "degraded_turns": 0, "cited_sentences": 0, "attached_sentences": 0, "horizon_mentions": 0,
        })
        world["turns"] += 1
        world["conversations"].add(row["conversation_token"])
        world["text_free_turns"] += 1 if flags.get("text_free") else 0
        world["degraded_turns"] += 1 if scores.get("degraded_by_net") else 0
        world["cited_sentences"] += int(marks.get("cited_sentences") or 0)
        world["attached_sentences"] += int(marks.get("attached_sentences") or 0)
        world["horizon_mentions"] += int(scores.get("horizon_mentions") or 0)
        by_routing[row["routing"]] = by_routing.get(row["routing"], 0) + 1
        weeks.add(row["week"])
        total += 1
        text_free += 1 if flags.get("text_free") else 0
    worlds = [{**w, "conversations": len(w["conversations"])} for w in by_world.values()]
    return {
        "turns": total,
        "text_free_turns": text_free,
        "weeks": sorted(weeks),
        "by_world": sorted(worlds, key=lambda w: (-w["turns"], w["world"])),
        "by_routing": dict(sorted(by_routing.items())),
        "audit": _latest_rollup(m7_audit_root),
    }
