"""The writer half of M7 (Artifact-8 §4): three outputs per run, each with
its access posture stated in its own bytes.

- sessions/<session_id>.json - the full per-session audit. Operator-only:
  it carries participant text by necessity (same posture as the event log
  itself, Artifact-6).
- fleet-rollup.json + fleet-digest.md - the shareable layer. NO participant
  text ever: session ids, world keys, voice excerpts and record ids only.
- canon-candidates.json - recurring participant asks. Operator-only.

Deletion lineage (Artifact-8 §4, spec §8): every derived file names the
session_ids it was computed from, so a deletion request is a grep. The
per-session file's lineage is its own id; the rollup and canon files carry
the full list.
"""
import json
from collections import Counter
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path

# Keys in a per-session audit dict that carry participant-authored text.
# The rollup builder strips by construction (it only reads the keys it
# aggregates), but naming them here keeps the boundary auditable.
PARTICIPANT_TEXT_KEYS = ("canon_asks",)

SEVERITY_ORDER = ("defect", "review", "info")


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def write_session_audit(out_dir: Path, audit: dict) -> Path:
    """sessions/<id>.json - operator-only (participant text inside)."""
    sessions_dir = out_dir / "sessions"
    sessions_dir.mkdir(parents=True, exist_ok=True)
    doc = {
        "artifact": "cic-m7-session-audit",
        "access": "operator-only: contains participant text (Artifact-8 §4)",
        "generated_at": _now(),
        "lineage_session_ids": [audit["session_id"]],
        **audit,
        "findings": [asdict(f) for f in audit["findings"]],
    }
    path = sessions_dir / f"{audit['session_id']}.json"
    path.write_text(json.dumps(doc, indent=2, sort_keys=False) + "\n")
    return path


def build_utilization(audits: list[dict], shelves: dict[str, dict] | None) -> dict | None:
    """Corpus utilization per world (Mark, 2026-08-29: "what percentage of
    the current sources are being accessed"): the union of every record id
    cited across these sessions, against each world's citable shelf.
    `shelves` maps world_key -> {"citable_ids": [...], "by_type": {type:
    [ids...]}} (the CLI builds it from the pinned packages, read-only).
    Record ids only - no participant text."""
    if not shelves:
        return None
    cited: dict[str, set] = {}
    for a in audits:
        for rid in a.get("cited_record_ids") or []:
            cited.setdefault(rid.split(".", 1)[0], set()).add(rid)
    out = {}
    for world, shelf in sorted(shelves.items()):
        citable = set(shelf.get("citable_ids") or [])
        hit = cited.get(world, set()) & citable
        by_type = {}
        for rtype, ids in sorted((shelf.get("by_type") or {}).items()):
            n_hit = len(hit & set(ids))
            by_type[rtype] = {"cited": n_hit, "total": len(ids)}
        out[world] = {
            "citable": len(citable),
            "cited_distinct": len(hit),
            "pct": round(len(hit) / len(citable) * 100, 1) if citable else None,
            "by_type": by_type,
            "cited_ids": sorted(hit),
        }
    return out


def build_rollup(audits: list[dict], shelves: dict[str, dict] | None = None) -> dict:
    """The fleet aggregate. Reads only non-participant keys; findings ride
    whole because a Finding never carries participant text by contract
    (instruments.Finding: voice text and ids only). `shelves` (optional,
    CLI-built from the pinned packages) turns on the utilization block."""
    severity_counts: Counter = Counter()
    instrument_counts: Counter = Counter()
    findings = []
    offer_totals: Counter = Counter()
    scored, fk_sum, fre_sum, unscored = 0, 0.0, 0.0, 0
    mode_counts: Counter = Counter()
    sessions_summary = []
    for a in audits:
        mode_counts[a["mode"]] += 1
        for f in a["findings"]:
            severity_counts[f.severity] += 1
            instrument_counts[f.instrument] += 1
            findings.append(asdict(f))
        offer_totals.update(a["offer_rates"])
        for m in a["register_metrics"]:
            if m.get("scored"):
                scored += 1
                fk_sum += m["fk_grade"]
                fre_sum += m["fre"]
            else:
                unscored += 1
        sessions_summary.append({
            "session_id": a["session_id"],
            "mode": a["mode"],
            "world_keys": a["world_keys"],
            "closed": a["closed"],
            "close_reason": a["close_reason"],
            "counts": a["counts"],
            "findings_by_severity": dict(Counter(f.severity for f in a["findings"])),
        })
    findings.sort(key=lambda f: SEVERITY_ORDER.index(f["severity"]))
    return {
        "artifact": "cic-m7-fleet-rollup",
        "access": "shareable: no participant text (Artifact-8 §4)",
        "generated_at": _now(),
        "lineage_session_ids": [a["session_id"] for a in audits],
        "sessions_audited": len(audits),
        "modes": dict(mode_counts),
        "findings_by_severity": dict(severity_counts),
        "findings_by_instrument": dict(instrument_counts),
        "findings": findings,
        "offer_rates": dict(offer_totals),
        "register": {
            "turns_scored": scored,
            "turns_unscored": unscored,
            "mean_fk_grade": round(fk_sum / scored, 2) if scored else None,
            "mean_fre": round(fre_sum / scored, 2) if scored else None,
        },
        "sessions": sessions_summary,
        "utilization": build_utilization(audits, shelves),
    }


def write_rollup(out_dir: Path, rollup: dict) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / "fleet-rollup.json"
    path.write_text(json.dumps(rollup, indent=2, sort_keys=False) + "\n")
    return path


def write_digest(out_dir: Path, rollup: dict) -> Path:
    """fleet-digest.md - the rollup's human read, same no-participant-text
    posture. Report-only prose: numbers and findings, no verdicts a bar
    hasn't earned (principle 10)."""
    out_dir.mkdir(parents=True, exist_ok=True)
    lines = [
        "# M7 Fleet Digest",
        "",
        f"Generated {rollup['generated_at']} over {rollup['sessions_audited']} "
        f"session(s) ({', '.join(f'{v} {k}' for k, v in sorted(rollup['modes'].items())) or 'none'}).",
        "No participant text appears in this file (Artifact-8 §4).",
        "",
        "## Findings",
        "",
    ]
    sev = rollup["findings_by_severity"]
    if not rollup["findings"]:
        lines.append("None. Every instrument ran; nothing surfaced.")
    else:
        lines.append(" · ".join(f"{sev.get(s, 0)} {s}" for s in SEVERITY_ORDER))
        lines.append("")
        for f in rollup["findings"]:
            rid = f" [{', '.join(f['record_ids'])}]" if f["record_ids"] else ""
            lines.append(f"- **{f['severity']}** ({f['instrument']}, session {f['session_id']}): {f['detail']}{rid}")
    reg = rollup["register"]
    lines += [
        "",
        "## Register (mechanical, whole-turn — phase 1)",
        "",
        f"{reg['turns_scored']} turn(s) scored, {reg['turns_unscored']} unscored (short turns "
        "report as unscored, never as clean).",
    ]
    if reg["mean_fk_grade"] is not None:
        lines.append(f"Mean FK grade {reg['mean_fk_grade']}, mean FRE {reg['mean_fre']} "
                     "(report-only; the spec's plain/grounding split is phase 2).")
    lines += [
        "",
        "## Offer rates (citation type segments)",
        "",
        ", ".join(f"{k}: {v}" for k, v in sorted(rollup["offer_rates"].items())) or "no citations recorded",
        "",
    ]
    util = rollup.get("utilization")
    if util:
        lines += ["## Corpus utilization", "",
                  "Distinct records cited across these sessions, against each world's citable shelf:", ""]
        for w, u in util.items():
            types = ", ".join(f"{t} {v['cited']}/{v['total']}" for t, v in u["by_type"].items() if v["total"])
            lines.append(f"- **{w}**: {u['cited_distinct']}/{u['citable']} ({u['pct']}%) — {types}")
        lines.append("")
    lines += [
        "## Lineage",
        "",
        f"Computed from session_ids: {', '.join(rollup['lineage_session_ids']) or 'none'}",
        "",
    ]
    path = out_dir / "fleet-digest.md"
    path.write_text("\n".join(lines))
    return path


def write_canon_candidates(out_dir: Path, audits: list[dict], min_count: int = 2) -> Path:
    """canon-candidates.json - operator-only (participant-authored asks).
    An ask recurring across sessions (or min_count times overall) is raw
    material for the Question Canon; Mark decides what enters (spec stage
    9: 'a real question enters the canon' - a person rules, this file only
    counts)."""
    out_dir.mkdir(parents=True, exist_ok=True)
    counts: Counter = Counter()
    sessions_for: dict[str, set] = {}
    for a in audits:
        for ask in a["canon_asks"]:
            counts[ask] += 1
            sessions_for.setdefault(ask, set()).add(a["session_id"])
    candidates = [
        {"ask": ask, "count": n, "session_ids": sorted(sessions_for[ask])}
        for ask, n in counts.most_common()
        if n >= min_count or len(sessions_for[ask]) > 1
    ]
    doc = {
        "artifact": "cic-m7-canon-candidates",
        "access": "operator-only: contains participant-authored asks (Artifact-8 §4)",
        "generated_at": _now(),
        "lineage_session_ids": [a["session_id"] for a in audits],
        "min_count": min_count,
        "total_distinct_asks": len(counts),
        "candidates": candidates,
    }
    path = out_dir / "canon-candidates.json"
    path.write_text(json.dumps(doc, indent=2, sort_keys=False) + "\n")
    return path
