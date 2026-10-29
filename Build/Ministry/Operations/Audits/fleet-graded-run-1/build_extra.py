"""Writes extra.json for the conversations page: the lpc validation conversations in full."""
import json
from pathlib import Path

OUT = Path(__file__).resolve().parents[5] / "engine" / "m3" / "reports" / "fleet-graded-run-1"
ROOT_BUILD = Path(__file__).resolve().parents[5] / "Build" / "worlds"
VAL = OUT / "lpc-validation"
items = []
for f in sorted(VAL.glob("*.json"), key=lambda p: (p.stem != "deep-interview", p.stem)):
    d = json.loads(f.read_text())
    if d.get("stopped_by_cap_at") and not d["results"]:
        continue
    for i, r in enumerate(d["results"]):
        res = r["result"]
        ve = res.get("voice_event")
        if ve:
            text, cites = ve["text"], ve.get("citations") or []
        else:
            fe = (res.get("facilitator_events") or [{}])[0]
            text, cites = "Facilitator turn (the voice stayed silent).\n\n" + (fe.get("text") or ""), []
        ids = sorted({rid for c in cites for rid in (c.get("record_ids") if isinstance(c, dict) else [c])})
        if ids:
            text += "\n\nRecords cited: " + ", ".join(ids)
        items.append({"tag": f"{f.stem} · turn {i + 1}", "q": r["message"], "a": text,
                      "status": res.get("routing_action", "")})
REPLAY = OUT / "replay"
OLD = Path(__file__).resolve().parents[5] / "engine" / "m4" / "reports"
WORLDS = ["gallic", "desert", "ijc", "alx", "witt", "rzg", "pahc", "hal", "syr", "cappadocian", "don"]


def answer(res):
    ve = res.get("voice_event")
    if ve:
        return ve["text"]
    fe = (res.get("facilitator_events") or [{}])[0]
    return "Facilitator turn (the voice stayed silent).\n\n" + (fe.get("text") or "")


data = {"lpc": [{"title": "lpc validation conversations",
                 "sub": f"{len(items)} turns across all 30 conversations used in run 3, deep interview first.",
                 "items": items}]}
for w in WORLDS:
    f = REPLAY / f"{w}.json"
    old_f = OLD / f"live-turn-report-{w}-2026-10-13-eleven-world-test.json"
    if not f.exists():
        continue
    new = json.loads(f.read_text())["results"]
    old = json.loads(old_f.read_text())["results"] if old_f.exists() else []
    rows = []
    for i, r in enumerate(new):
        text = answer(r["result"])
        if i < len(old):
            text += "\n\n\u2014 Older answer to the same question, 13 October test (different format and engine; read it qualitatively only) \u2014\n\n" + answer(old[i]["result"])
        rows.append({"tag": f"replay \u00b7 question {i + 1}", "q": r["message"], "a": text, "status": r["result"].get("routing_action", "")})
    cj = ROOT_BUILD / w / "Review-Artifacts" / "Fleet_Run1_Replay_Side_By_Side_2026-10-29.counts.json"
    sub = "The same six questions the 13 October test asked, as one conversation on today's code. The older answer follows each new answer."
    if cj.exists():
        c = json.loads(cj.read_text())
        sub += f" Opus: new answers PASS {c['pass']}, FAIL {c['fail']}, NOT SCORED {c['not_scored']} of 6; against the older answers better {c['better']}, same {c['same']}, worse {c['worse']}."
    data.setdefault(w, []).append({"title": "Six-question replay (29 October)", "sub": sub, "items": rows})
(OUT / "extra.json").write_text(json.dumps(data, indent=1))
print(len(items), "turns")
