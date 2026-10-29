"""Builds the conversations page for "fleet graded run 1" from the files in
engine/m3/reports/fleet-graded-run-1/. Writes conversations.html there."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT))
from engine.m3 import protocol, sealed_probes  # noqa: E402

OUT = ROOT / "engine" / "m3" / "reports" / "fleet-graded-run-1"
RUN3 = ROOT / "engine" / "m3" / "reports" / "live-admission-report-lpc-2026-10-28-run3.json.answers.jsonl"
ORDER = ["lpc", "gallic", "desert", "ijc", "alx", "witt", "rzg", "pahc", "hal", "syr", "cappadocian", "don"]
CAP = 12.0


def jl(path):
    if not path.exists():
        return []
    rows = []
    for line in path.read_text().splitlines():
        try:
            rows.append(json.loads(line))
        except ValueError:
            pass
    return rows


def main():
    cp = json.loads((OUT / "checkpoint.json").read_text()) if (OUT / "checkpoint.json").exists() else {"worlds": {}, "spent_usd": 0.0}
    battery = protocol.battery()
    questions = [sealed_probes.read_probe(b["probe_id"])["text"] for b in battery]
    run3 = {r["index"]: r for r in jl(RUN3)}
    extra = json.loads((OUT / "extra.json").read_text()) if (OUT / "extra.json").exists() else {}
    reviews = json.loads((OUT / "reviews.json").read_text()) if (OUT / "reviews.json").exists() else {}
    worlds, running_world, running_spent = [], None, 0.0
    for w in ORDER:
        st = cp["worlds"].get(w, {})
        n = st.get("attempts", 0)
        ra = st.get("review_attempt")
        tag = w if (ra == 1 or n <= 1) else f"{w}-attempt{n}"
        report = OUT / f"{tag}.json"
        answers = jl(Path(str(report) + ".answers.jsonl"))
        settles = [r for r in jl(OUT / f"ledger-{tag}.jsonl") if r.get("event") == "settle"]
        final = json.loads(report.read_text())["worlds"].get(w) if report.exists() else None
        probes = []
        for i, b in enumerate(battery):
            fin = final["per_probe"][i] if final and i < len(final["per_probe"]) else None
            ans = answers[i] if i < len(answers) else None
            tr = (fin or {}).get("transcript") or {}
            text = tr.get("answer_text") or (ans or {}).get("answer_text")
            if text is None:
                probes.append({"i": i, "id": b["probe_id"], "cell": b["cell"], "q": questions[i], "a": None})
                continue
            probes.append({
                "i": i, "id": b["probe_id"], "cell": b["cell"], "q": questions[i], "a": text,
                "cites": tr.get("citations") or (ans or {}).get("citations") or [],
                "entries": tr.get("citation_entries") or [],
                "passed": fin["passed"] if fin else None,
                "checks": [{"n": c["check"], "ok": c["passed"], "f": [str(x) for x in c.get("findings", [])][:3]} for c in (fin or {}).get("checks", [])],
                "cost": round(settles[i]["priced_dollars"], 4) if i < len(settles) else None,
                "prev": ({"a": run3[i]["answer_text"], "cites": run3[i].get("citations", [])} if w == "lpc" and i in run3 else None),
            })
        status = st.get("status", "waiting")
        if status == "running":
            running_world, running_spent = w, st.get("spent_usd_world", 0.0)
        worlds.append({"key": w, "status": status, "attempts": n, "spent": st.get("spent_usd_world"),
                       "passed": (final or {}).get("pass_count"), "size": (final or {}).get("battery_size") or 28,
                       "answered": len([p for p in probes if p["a"]]), "probes": probes,
                       "review": reviews.get(w), "extra": extra.get(w)})
    data = {"cap": CAP, "spent": round(cp.get("spent_usd", 0.0) + running_spent, 4), "running": running_world,
            "done": sum(1 for w in worlds if w["status"] == "done"), "worlds": worlds, "extra_note": extra.get("_note")}
    html = (Path(__file__).parent / "conversations_template.html").read_text().replace(
        "__DATA__", json.dumps(data).replace("</", "<\\/"))
    (OUT / "conversations.html").write_text(html)
    print(f"wrote {OUT / 'conversations.html'} ({len(html)//1024} KB), spent ${data['spent']}")


if __name__ == "__main__":
    main()
