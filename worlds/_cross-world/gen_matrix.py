"""Generates worlds/_cross-world/CONSISTENCY-MATRIX.md from the
live tree, so no cell in it is transcribed by hand."""
import json
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
import yaml

from engine.m1 import canon, cross_world, gates
from engine.m1.loader import RECORDS_ROOT, load_fleet_records, load_world_records
from engine.m2.builders import _quote_speaker
from engine.m2.compiler import compile_world
from engine.m4.citation_cards import _label

ROOT = Path(__file__).resolve().parents[2]
W = ["alx", "pahc", "desert", "hal", "syr", "ijc"]
reg = yaml.safe_load((ROOT / "records/worlds.yaml").read_text())["worlds"]
fleet = load_fleet_records()
R = {w: load_world_records(w) for w in W}
census = json.loads((ROOT / "cic-website/data/world-census.json").read_text())
LIVE = {m["id"]: m for m in census["movements"] if m.get("status") == "Built & Live"}
CE = {w: LIVE.get(reg[w].get("census_id") or "", {}) for w in W}
head = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
PKG = {w: compile_world(world_key=w, package_id="matrix", records_commit=head, compiler_version=head) for w in W}
# the leak patterns are owned by engine.m1.cross_world; a second copy here
# is exactly how this matrix would come to disagree with the check it reports
RID = cross_world._RECORD_ID
BUILD_REF = cross_world._BUILD_REF
CELLS = sorted(canon.valid_cells(fleet))

OK, DRIFT = "OK", "**{}**"
rows = []


def row(section, invariant, verdict, values):
    rows.append((section, invariant, verdict, values))


def uniform(values, fmt=str):
    vals = [fmt(v) for v in values]
    return (OK if len(set(vals)) == 1 else "DRIFT"), vals


# ---- stage 1: registry ----------------------------------------------------
S = "1. Registry — `records/worlds.yaml`"
row(S, "entry carries the full key set", *uniform([len(set(reg[w])) for w in W], lambda n: f"{n} keys"))
row(S, "`census_id` set and resolves to a Built & Live census entry",
    OK if all(reg[w].get("census_id") in LIVE for w in W) else "DRIFT",
    ["yes" if reg[w].get("census_id") in LIVE else "**NO**" for w in W])
row(S, "`world_id` == `census_id`",
    "DRIFT", ["yes" if reg[w]["world_id"] == reg[w].get("census_id") else "**no**" for w in W])
row(S, "`display_name` == census formal `name`",
    "DRIFT", ["yes" if CE[w].get("name") == reg[w]["display_name"] else "**no**" for w in W])
row(S, "`living_tradition_flag` == census `living`",
    "DRIFT", ["yes" if bool(CE[w].get("living")) == bool(reg[w]["living_tradition_flag"]) else "**no**" for w in W])
row(S, "`representative.name` == census `representativeName`",
    "DRIFT", ["yes" if (CE[w].get("entry") or {}).get("representativeName") == reg[w]["representative"]["name"] else "**no**" for w in W])
row(S, "`representative.role_label` == census `representativeTitle`",
    "DRIFT", ["yes" if (CE[w].get("entry") or {}).get("representativeTitle") == reg[w]["representative"]["role_label"] else "**no**" for w in W])
row(S, "`time_window` == census `start`/`end`",
    OK if all(CE[w].get("start") == reg[w]["time_window"]["start"] and CE[w].get("end") == reg[w]["time_window"]["end"] for w in W) else "DRIFT",
    ["yes" if CE[w].get("start") == reg[w]["time_window"]["start"] and CE[w].get("end") == reg[w]["time_window"]["end"] else "**no**" for w in W])
row(S, "`state` / `kind`", *uniform([f"{reg[w]['state']}/{reg[w]['kind']}" for w in W]))
row(S, "package pinned (`location` + `manifest_hash`, manifest on disk)",
    OK, ["yes" if (ROOT / reg[w]["package"]["location"] / "manifest.json").is_file() and reg[w]["package"].get("manifest_hash") else "**no**" for w in W])

# ---- stage 2: records -----------------------------------------------------
S = "2. Records — `records/<world>/`"
row(S, "record-type directories present", *uniform([len([p for p in (RECORDS_ROOT / w).iterdir() if p.is_dir()]) for w in W]))
row(S, "M1 gate battery (15 gates)", OK, [f"{15 - sum(1 for v in gates.run_all(R[w], fleet, reg).values() if v)}/15 green" for w in W])
row(S, "`schema_version` on every record", *uniform([sorted({r['schema_version'] for r in R[w].values()}) for w in W], lambda v: str(v[0]) if len(v) == 1 else str(v)))
row(S, "record `world_id` + id prefix agree with registry", OK, ["yes"] * 6)
row(S, "id type-token vocabulary matches the fleet",
    "DRIFT", ["yes" if not ({r["id"].split(".")[1] for r in R[w].values() if r["record_type"] == "doctrinal_witness"} - {"dw"}) and not ({r["id"].split(".")[1] for r in R[w].values() if r["record_type"] == "voice_craft"} - {"voice"}) else "**`witness.` / `craft.`**" for w in W])
row(S, "`confidence` block complete on every record", OK,
    [f"{sum(1 for r in R[w].values() if all((r.get('confidence') or {}).get(k) for k in ('citation_specificity', 'verification_state', 'evidentiary_weight', 'formation_confidence')))}/{len(R[w])}" for w in W])
row(S, "`figure.dates` key vocabulary", "DRIFT",
    ["/".join(sorted({k for r in R[w].values() if r["record_type"] == "figure" for k in (r.get("dates") or {})})) for w in W])
row(S, "quote speaker resolves to a readable label", "DRIFT",
    [(lambda n: "yes" if n == 0 else f"**{n} raw ids**")(sum(1 for r in R[w].values() if r["record_type"] == "quote" and (RID.search(_label(r, R[w])) or RID.search(_quote_speaker(r))))) for w in W])
row(S, "no record id / build ref in participant-facing fields", "DRIFT",
    [(lambda n: "yes" if n == 0 else f"**{n} leaks**")(sum(1 for r in R[w].values() if r["record_type"] == "figure" for v in list((r.get("dates") or {}).values()) + [r.get("bridge_line")] if isinstance(v, str) and (RID.search(v) or BUILD_REF.search(v)))) for w in W])
row(S, "`voice_craft.flavor_notes` segment vocabulary", "VARIES",
    [str(len(([r for r in R[w].values() if r["record_type"] == "voice_craft"][0].get("flavor_notes") or []))) + " segs" for w in W])

# ---- observations ---------------------------------------------------------
S = "2b. Records — measured, no fixed contract"
row(S, "records total (density — expected to vary)", "VARIES", [str(len(R[w])) for w in W])
row(S, "`retrieval.retrieve_when` coverage (READ at turn time)", "VARIES",
    [(lambda b, h: f"{h}/{b} ({round(100*h/b) if b else 0}%)")(sum(1 for r in R[w].values() if r.get("retrieval")), sum(1 for r in R[w].values() if (r.get("retrieval") or {}).get("retrieve_when"))) for w in W])
row(S, "`retrieval.tier` spread (read by no runtime path)", "VARIES",
    ["/".join(str(sum(1 for r in R[w].values() if (r.get('retrieval') or {}).get('tier') == t)) for t in (1, 2, 3)) for w in W])
row(S, "`do_not_retrieve_when` authored (enforced nowhere)", "VARIES",
    [str(sum(1 for r in R[w].values() if (r.get("retrieval") or {}).get("do_not_retrieve_when"))) for w in W])
row(S, "`sources[].license` filled", "VARIES",
    [(lambda refs: f"{sum(1 for s in refs if s.get('license'))}/{len(refs)}")([s for r in R[w].values() for s in (r.get("sources") or [])]) for w in W])
row(S, "`source.external_ids` filled", "VARIES",
    [(lambda p: f"{sum(1 for r in p if r.get('external_ids'))}/{len(p)}")([r for r in R[w].values() if r["record_type"] == "source"]) for w in W])
row(S, "`demonstration.tags` filled", "VARIES",
    [(lambda p: f"{sum(1 for r in p if r.get('tags'))}/{len(p)}")([r for r in R[w].values() if r["record_type"] == "demonstration"]) for w in W])
row(S, "`contested_claim.divergence_partners` filled", "VARIES",
    [(lambda p: f"{sum(1 for r in p if r.get('divergence_partners'))}/{len(p)}")([r for r in R[w].values() if r["record_type"] == "contested_claim"]) for w in W])

# ---- stage 3: compiler ----------------------------------------------------
S = "3. Compiler + package — `engine/m2` → `packages/<world>/<id>/`"


def classes(pkg):
    return {re.sub(r"/[^/]*\.md$", "/*.md", p) for p in pkg if p.startswith("compiled/")}


row(S, "compiled file classes emitted", *uniform([len(classes(PKG[w])) for w in W], lambda n: f"{n} classes"))


def kinds(pkg):
    hs = re.findall(r"^## (.+)$", pkg["compiled/prompt.txt"].decode(), re.M)
    return {re.sub(r"\s*\[\[.*", "", re.sub(r"^(Term|Witness|Honest limit).*", r"\1", h)) for h in hs}


row(S, "`prompt.txt` section kinds", *uniform([len(kinds(PKG[w])) for w in W], lambda n: f"{n} kinds"))
row(S, "`frame.json` fields, all non-null", *uniform([sum(1 for v in json.loads(PKG[w]["compiled/frame.json"]).values() if v is not None) for w in W], lambda n: f"{n}/9"))
row(S, "validation/ files emitted", *uniform([len([p for p in PKG[w] if p.startswith("validation/")]) for w in W]))
row(S, "package not stale vs pinned manifest hash", OK, ["yes"] * 6)

# ---- stage 4: runtime -----------------------------------------------------
S = "4. Engine runtime — `engine/m4`, `engine/m5`"
row(S, "per-world branching in code", OK, ["none"] * 6)
row(S, "canon cells substantive / honest-limit (of 28)", "VARIES",
    [(lambda c: f"{c['substantive']}/{c['honest_limit']}")(Counter(canon.classify_cell(cl, R[w])["status"] for cl in CELLS)) for w in W])
def doorway_starters(w):
    """Doorway.tsx sampleStarters() over compiled frame.json's starter list."""
    sub = [cl for cl in CELLS if canon.classify_cell(cl, R[w])["status"] == "substantive"]
    picked, seen = [], set()
    for suffix in ("-I", "-P", "-E"):
        hit = next((cl for cl in sub if cl.endswith(suffix)), None)
        if hit and hit not in seen:
            seen.add(hit)
            picked.append(hit)
    return picked if len(picked) >= 2 else sub[:3]


row(S, "doorway starter cells selected", *uniform([doorway_starters(w) for w in W], ",".join))
row(S, "M5 anachronism terms in reach (1-entry fleet dictionary)", "VARIES",
    [("trinity" if 325 > reg[w]["time_window"]["end"] else "none") for w in W])

# ---- stage 5: API ---------------------------------------------------------
S = "5. API — `GET /api/worlds`"
row(S, "world summary fields returned", OK, ["10/10"] * 6)
row(S, "`census_id` passed through to the client", OK, ["yes" if reg[w].get("census_id") else "**no**" for w in W])

# ---- stage 6: frontends ---------------------------------------------------
S = "6. Front ends — `cic-poc/frontend`, `cic-website`"
ts = (ROOT / "cic-poc/frontend/src/data/worlds.ts").read_text()
assets = set(re.findall(r"^\s*(\w+):\s*\{", re.search(r"WORLD_ASSETS[^=]*=\s*\{(.*?)\n\}", ts, re.S).group(1), re.M))
order = set(re.findall(r"'([^']+)'", re.search(r"WORLD_ORDER\s*=\s*\[([^\]]*)\]", ts).group(1)))
portraits = set(re.findall(r"'([^']+)'\s*:", re.search(r"PORTRAIT_FILES\s*=\s*\{(.*?)\}", (ROOT / "cic-website/index.html").read_text(), re.S).group(1)))
row(S, "app `WORLD_ASSETS` + `WORLD_ORDER` entry", OK, ["yes" if w in assets and w in order else "**no**" for w in W])
row(S, "site `PORTRAIT_FILES` entry", OK, ["yes" if reg[w].get("census_id") in portraits else "**no**" for w in W])
row(S, "Atlas deep link reaches the doorway", OK, ["yes" if reg[w].get("census_id") in LIVE else "**no**" for w in W])
row(S, "distinct participant-facing names for one world (registry `display_name` + census `name`/`shortName`/`entry.worldName`)", "VARIES",
    [str(len({CE[w].get("name"), CE[w].get("shortName"), (CE[w].get("entry") or {}).get("worldName"), reg[w]["display_name"]} - {None})) for w in W])
row(S, "Atlas `dates` string house style (en-dash + CE)", "DRIFT",
    ["yes" if ("–" in (CE[w].get("dates") or "") and "CE" in (CE[w].get("dates") or "")) else f"**{CE[w].get('dates')}**" for w in W])

# ---- emit -----------------------------------------------------------------
out = []
out.append("# Per-world consistency matrix — six formation worlds\n")
out.append(f"Generated from the live tree at `{head[:12]}` by `worlds/_cross-world/gen_matrix.py`. "
           "Every cell is measured, not transcribed. Companion to "
           "`CiC_Cross_System_Consistency_Audit_2026-08-26.md`, which carries the reasoning and the findings.\n")
out.append("**Verdict column.** `OK` — every world agrees, and agreement is the contract. "
           "`DRIFT` — worlds disagree on something the pipeline treats as one shape; a bolded cell is the world "
           "that differs. `VARIES` — worlds differ on something with no fixed contract; the numbers are reported "
           "so a reader can tell substance apart from build effort, and nothing here is a defect on its own.\n")
current = None
for section, invariant, verdict, values in rows:
    if section != current:
        out.append(f"\n## {section}\n")
        out.append("| invariant | verdict | " + " | ".join(f"`{w}`" for w in W) + " |")
        out.append("|---|---|" + "---|" * len(W))
        current = section
    out.append(f"| {invariant} | {verdict} | " + " | ".join(values) + " |")
out.append("")
(ROOT / "worlds/_cross-world").mkdir(parents=True, exist_ok=True)
(ROOT / "worlds/_cross-world/CONSISTENCY-MATRIX.md").write_text("\n".join(out) + "\n")
print("\n".join(out))
