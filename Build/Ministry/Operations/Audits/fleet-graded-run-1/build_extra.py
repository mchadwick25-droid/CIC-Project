"""Writes extra.json for the conversations page: the lpc validation conversations in full."""
import json
from pathlib import Path

OUT = Path(__file__).resolve().parents[5] / "engine" / "m3" / "reports" / "fleet-graded-run-1"
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
data = {"lpc": [{"title": "lpc validation conversations",
                 "sub": f"{len(items)} turns from 27 of the 30 conversations used in run 3. thinness-2, thinness-3 and thinness-4 were not run because the $12 cap was reached.",
                 "items": items}]}
(OUT / "extra.json").write_text(json.dumps(data, indent=1))
print(len(items), "turns")
