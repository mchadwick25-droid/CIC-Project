#!/usr/bin/env python3
"""Church Family Tree use report: queries Workers Analytics Engine (dataset cft_events)
and writes one JSON file per question: {"rows": [...], "meta": [...]}.
Needs a read-only Cloudflare token (Account Analytics: Read) sent as a bearer header.
Usage: cft_usage_report.py OUTDIR [DAYS]"""
import json, os, re, subprocess, sys, datetime

ACCOUNT = "97079693bee8c4ff0d06135d9e505f47"
OUT = sys.argv[1]
DAYS = int(sys.argv[2]) if len(sys.argv) > 2 else 60
# Rows left out: the deploy check, and the launch test visit made by the build session (2026-11-21 13:14 UTC).
EXCLUDE = ("blob2 != 'deploy-check' AND NOT (timestamp >= toDateTime('2026-11-21 13:14:00') "
           "AND timestamp < toDateTime('2026-11-21 13:20:00'))")
def owner_clause():
    """Visitor ids that opened the map with ?count=off send one "owner" event. Every event from them is left out, past and future."""
    r = subprocess.run(["curl", "-s", "-m", "60", "-X", "POST",
        f"https://api.cloudflare.com/client/v4/accounts/{ACCOUNT}/analytics_engine/sql",
        "--data", "SELECT blob5 AS id FROM cft_events WHERE blob1 = 'owner' AND blob5 != '' GROUP BY id FORMAT JSON"],
        capture_output=True, text=True)
    ids = [x["id"] for x in json.loads(r.stdout).get("data", []) if re.fullmatch(r"[a-f0-9]{32}", x["id"])]
    return ("blob5 NOT IN (" + ",".join(f"'{i}'" for i in ids) + ")") if ids else "1 = 1"

WINDOW = f"timestamp > NOW() - INTERVAL '{DAYS}' DAY AND blob1 != 'owner' AND {owner_clause()} AND {EXCLUDE}"
DAY = "formatDateTime(timestamp, '%Y-%m-%d')"

QUERIES = {
  "daily": (f"SELECT {DAY} AS day, sum(_sample_interval) AS visits, "
            f"sumIf(_sample_interval, blob2 = 'new') AS new_visitors, "
            f"sumIf(_sample_interval, blob2 = 'returning') AS returning_visitors "
            f"FROM cft_events WHERE blob1 = 'visit' AND {WINDOW} GROUP BY day ORDER BY day"),
  "sources": (f"SELECT blob3 AS source, sum(_sample_interval) AS visits FROM cft_events "
              f"WHERE blob1 = 'visit' AND {WINDOW} GROUP BY source ORDER BY visits DESC"),
  "devices": (f"SELECT blob4 AS device, sum(_sample_interval) AS visits FROM cft_events "
              f"WHERE blob1 = 'visit' AND {WINDOW} GROUP BY device ORDER BY visits DESC"),
  "opened": (f"SELECT blob2 AS kind, blob3 AS item, sum(_sample_interval) AS opens FROM cft_events "
             f"WHERE blob1 = 'open' AND {WINDOW} GROUP BY kind, item ORDER BY opens DESC LIMIT 25"),
  "listened": (f"SELECT blob2 AS group_, blob3 AS clip, sumIf(_sample_interval, blob4 = 'start') AS started, "
               f"sumIf(_sample_interval, blob4 = '50') AS reached_half, "
               f"sumIf(_sample_interval, blob4 = 'end') AS finished FROM cft_events "
               f"WHERE blob1 = 'listen' AND {WINDOW} GROUP BY group_, clip ORDER BY started DESC LIMIT 25"),
  "tours": (f"SELECT blob2 AS tour, sum(_sample_interval) AS events, sumIf(_sample_interval, double1 = 1) AS finished "
            f"FROM cft_events WHERE blob1 = 'tour' AND {WINDOW} GROUP BY tour ORDER BY events DESC"),
  "layers": (f"SELECT blob2 AS layer, sum(_sample_interval) AS turned_on FROM cft_events "
             f"WHERE blob1 = 'layer' AND {WINDOW} GROUP BY layer ORDER BY turned_on DESC"),
  "countries": (f"SELECT blob6 AS country, blob7 AS region, sum(_sample_interval) AS visits, "
                f"count(DISTINCT blob5) AS visitors FROM cft_events WHERE blob1 = 'visit' AND blob6 != '' AND {WINDOW} "
                f"GROUP BY country, region ORDER BY visits DESC LIMIT 40"),
  "cities": (f"SELECT blob9 AS city, blob6 AS country, sum(_sample_interval) AS visits, count(DISTINCT blob5) AS visitors "
             f"FROM cft_events WHERE blob1 = 'visit' AND blob9 != '' AND {WINDOW} GROUP BY city, country ORDER BY visits DESC LIMIT 40"),
  "campaigns": (f"SELECT blob10 AS tagged_link, sum(_sample_interval) AS visits, count(DISTINCT blob5) AS visitors "
                f"FROM cft_events WHERE blob1 = 'visit' AND blob10 != '' AND blob10 != '//' AND {WINDOW} "
                f"GROUP BY tagged_link ORDER BY visits DESC LIMIT 40"),
  "browsers": (f"SELECT blob8 AS browser, sum(_sample_interval) AS visits FROM cft_events "
               f"WHERE blob1 = 'visit' AND blob8 != '' AND {WINDOW} GROUP BY browser ORDER BY visits DESC"),
  "totals": (f"SELECT sumIf(_sample_interval, blob1 = 'visit') AS visits, "
             f"sumIf(_sample_interval, blob1 = 'visit' AND blob2 = 'returning') AS returning_visits, "
             f"sumIf(_sample_interval, blob1 = 'open') AS cards_opened, "
             f"sumIf(_sample_interval, blob1 = 'listen' AND blob4 = 'start') AS recordings_started, "
             f"sumIf(_sample_interval * double1, blob1 = 'active') / 60 AS active_minutes, "
             f"sumIf(_sample_interval, blob1 = 'grow' AND blob2 = 'shown') AS support_note_shown, "
             f"sumIf(_sample_interval, blob1 = 'grow' AND blob2 = 'link') AS support_link_followed "
             f"FROM cft_events WHERE {WINDOW}"),
}

def run(sql):
    r = subprocess.run(["curl", "-s", "-m", "60", "-X", "POST",
        f"https://api.cloudflare.com/client/v4/accounts/{ACCOUNT}/analytics_engine/sql",
        "--data", sql + " FORMAT JSON"], capture_output=True, text=True)
    d = json.loads(r.stdout)
    if "data" not in d: raise SystemExit(f"query failed: {r.stdout[:400]}")
    return d["data"], [m["name"] for m in d["meta"]]

def num(v):
    try:
        f = float(v); return int(f) if f == int(f) else round(f, 1)
    except (TypeError, ValueError): return v

os.makedirs(OUT, exist_ok=True)
stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
STR = ("city","tagged_link","country","region","browser","day","source","device","kind","item","group_","clip","tour","layer")
report = {"generated": stamp, "days": DAYS}
for name, sql in QUERIES.items():
    data, cols = run(sql)
    rows = [{k: (v if k in STR else num(v)) for k, v in row.items()} for row in data]
    report[name] = {"columns": cols, "rows": rows, "meta": [
        {"label": "Query (Workers Analytics Engine SQL)", "value": sql, "type": "code", "lang": "sql"},
        {"label": "Run at", "value": stamp},
        {"label": "Left out", "value": "The deploy check row, the launch test visit of 2026-11-21 13:14 UTC, and every event from a visitor id that opened the map with ?count=off. Automated browsers and bots never send events."}]}
    print(name, len(rows), "rows")
# Visitors by id: each visitor's visit days, counted in Python so the query stays simple.
vd, _ = run(f"SELECT blob5 AS visitor, {DAY} AS day, sum(_sample_interval) AS visits FROM cft_events "
             f"WHERE blob1 = 'visit' AND blob5 != '' AND {WINDOW} GROUP BY visitor, day LIMIT 100000")
days, visits = {}, {}
for r in vd:
    days.setdefault(r["visitor"], set()).add(r["day"]); visits[r["visitor"]] = visits.get(r["visitor"], 0) + float(r["visits"])
# A visit is one visitor on one day. Time in use and cards opened are summed the same way.
vt, _ = run(f"SELECT blob5 AS visitor, {DAY} AS day, sumIf(_sample_interval * double1, blob1 = 'active') AS secs, "
             f"sumIf(_sample_interval, blob1 = 'open') AS opens FROM cft_events "
             f"WHERE blob5 != '' AND {WINDOW} GROUP BY visitor, day LIMIT 100000")
visit_days = max(1, len(vt))
n = len(days)
report["visitors"] = {"unique_visitors": n,
    "returning_visitors": sum(1 for d in days.values() if len(d) > 1),
    "visits_per_visitor": round(sum(visits.values()) / n, 2) if n else 0,
    "minutes_in_use_per_visit": round(sum(float(r["secs"]) for r in vt) / 60 / visit_days, 1),
    "cards_opened_per_visit": round(sum(float(r["opens"]) for r in vt) / visit_days, 1),
    "note": "A visit is one visitor on one day. Counted by visitor id since the ids began (2026-11-27); earlier visits carry no id. Owner ids are left out."}
print("visitors", n)
json.dump(report, open(os.path.join(OUT, "cft_usage.json"), "w"), indent=1)
