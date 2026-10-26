"""Render the Question Repository YAML into the artifact page. Scratchpad only."""
import glob, html, os, sys
from collections import Counter, defaultdict
import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "question-repository-v0.html")

frame = yaml.safe_load(open(os.path.join(HERE, "00-frame.yaml")))
questions = []
for f in sorted(glob.glob(os.path.join(HERE, "0[1-4]-*.yaml")) + glob.glob(os.path.join(HERE, "06-*.yaml"))):
    questions += yaml.safe_load(open(f))["questions"]
extra = os.path.join(HERE, "05-research-additions.yaml")
if os.path.exists(extra):
    questions += yaml.safe_load(open(extra))["questions"]

SQ = yaml.safe_load(open(os.path.join(HERE, "07-subquestions.yaml")))["subquestions"]
ids = [q["id"] for q in questions]
dups = [i for i, n in Counter(ids).items() if n > 1]
if dups:
    sys.exit(f"duplicate ids: {dups}")

K, C, FL = frame["kinds"], frame["clusters"], frame["flags"]
by_c = defaultdict(list)
for q in questions:
    by_c[q["c"]].append(q)
src_count = Counter(q["s"] for q in questions)
kind_count = Counter(k for q in questions for k in q["k"])
flag_count = Counter(f for q in questions for f in q.get("f", []))

def e(s): return html.escape(str(s), quote=True)
TAGCLS = {"EXISTS": "e", "PREDICTED": "p", "REAL": "r", "RESEARCH": "x"}

def qrow(q):
    tags = f'<span class="tag {TAGCLS[q["s"]]}">{q["s"]}</span>'
    for f in q.get("f", []):
        tags += f'<span class="tag f">{e(f)}</span>'
    kinds = " ".join(f'<span class="k">{e(k)}</span>' for k in q["k"])
    ref = f'<span class="ref">{e(q["ref"])}</span>' if q.get("ref") else ""
    if q.get("moved_from"):
        ref += f'<span class="ref">moved from {e(q["moved_from"])}</span>'
    return (f'<li id="{e(q["id"])}"><span class="id">{e(q["id"])}</span>'
            f'<span class="body"><q>{e(q["t"])}</q> {ref}</span>'
            f'<span class="meta">{tags}{kinds}</span></li>')

kind_cards = ""
for kid, k in K.items():
    kind_cards += (f'<div class="kind"><span class="kid">{kid}</span><h3>{e(k["name"])}</h3>'
                   f'<p><b>Wants:</b> {e(k["wants"])}</p><p class="voice">{e(k["voice"])}</p>'
                   f'<p class="n">{kind_count[kid]} questions tagged</p></div>')

qid = {q["id"]: q for q in questions}
def sq_kinds(sq): return sorted({k for i in sq["ids"] for k in qid[i]["k"]})
cluster_html = ""
for cid, name in C.items():
    sqs = [x for x in SQ if x["c"] == cid]
    qs = by_c[cid]
    cs = Counter(q["s"] for q in qs)
    cluster_html += (f'<section class="cluster" id="{cid}"><header><h3>{cid} · {e(name)}</h3>'
                     f'<span class="count">{len(sqs)} sub-questions · {len(qs)} wordings ({cs["EXISTS"]} exist, {cs["PREDICTED"]} predicted'
                     f'{", " + str(cs["REAL"]) + " real" if cs["REAL"] else ""}{", " + str(cs["RESEARCH"]) + " from research" if cs["RESEARCH"] else ""})</span></header>')
    for sq in sqs:
        can = qid[sq["canonical"]]
        others = [qid[i] for i in sq["ids"] if i != sq["canonical"]]
        flags = sorted({f for i in sq["ids"] for f in qid[i].get("f", [])})
        ftags = "".join(f'<span class="tag f">{e(f)}</span>' for f in flags)
        ktags = " ".join(f'<span class="k">{e(k)}</span>' for k in sq_kinds(sq))
        cluster_html += (f'<div class="sq" id="{e(sq["id"])}"><div class="sqh"><span class="sqid">{e(sq["id"])}</span>'
                         f'<span class="sqlabel">{e(sq["label"])}</span><span class="meta">{ftags}{ktags}</span></div>'
                         f'<ol class="qs">{qrow(can)}</ol>'
                         + (f'<details><summary>{len(others)} more wording{"s" if len(others)!=1 else ""}</summary><ol class="qs">{"".join(qrow(q) for q in others)}</ol></details>' if others else "")
                         + '</div>')
    cluster_html += '</section>'

matrix = '<table><thead><tr><th>Cluster</th>' + "".join(f'<th>{k}</th>' for k in K) + '<th>Sub-q</th><th>Wordings</th></tr></thead><tbody>'
for cid, name in C.items():
    sqs = [x for x in SQ if x["c"] == cid]
    cnt = Counter(k for sq in sqs for k in sq_kinds(sq))
    matrix += f'<tr><td class="cn">{cid} {e(name)}</td>' + "".join(
        f'<td class="{"z" if cnt[k]==0 else ""}">{cnt[k] or "·"}</td>' for k in K) + f'<td><b>{len(sqs)}</b></td><td>{len(by_c[cid])}</td></tr>'
matrix += '</tbody></table>'

page = f"""<title>Question Repository v0</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&display=swap">
<style>
/* Layout: reading column for the brief; kind cards in a grid; a coverage matrix; then the full repository, one section per cluster. */
:root{{--bg:#f2f3f5;--paper:#fff;--fg:#1c2130;--muted:#5a6275;--rule:#d5d9e1;--accent:#1f5f6b;--accent-soft:#dfeef0;
--exist:#2b5fa8;--exist-bg:#e3ebf8;--pred:#7a5a12;--pred-bg:#f7edd3;--real:#2f7d4f;--real-bg:#e3f2e8;--res:#6d4aa3;--res-bg:#ece5f6;--flag:#a3352c;--flag-bg:#f8e3e0;
--display:"IBM Plex Sans",system-ui,sans-serif;--body:"Source Serif 4",Georgia,serif}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#161a22;--paper:#1f242e;--fg:#e7e9ee;--muted:#a3aab8;--rule:#343b48;--accent:#7fc2c9;--accent-soft:#1d3238;
--exist:#9ab9ee;--exist-bg:#1f2d47;--pred:#e2b55f;--pred-bg:#3d2f14;--real:#8fd3a8;--real-bg:#1f3a2a;--res:#c3a8ee;--res-bg:#2f2544;--flag:#f0968c;--flag-bg:#46221f;color-scheme:dark}}}}
:root[data-theme="dark"]{{--bg:#161a22;--paper:#1f242e;--fg:#e7e9ee;--muted:#a3aab8;--rule:#343b48;--accent:#7fc2c9;--accent-soft:#1d3238;
--exist:#9ab9ee;--exist-bg:#1f2d47;--pred:#e2b55f;--pred-bg:#3d2f14;--real:#8fd3a8;--real-bg:#1f3a2a;--res:#c3a8ee;--res-bg:#2f2544;--flag:#f0968c;--flag-bg:#46221f;color-scheme:dark}}
body{{background:var(--bg);color:var(--fg);font-family:var(--body);font-size:17px;line-height:1.5;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));padding-block:32px 64px}}
.wrap{{max-width:1100px;margin:0 auto;display:grid;gap:40px}} .col{{max-width:70ch}}
h1,h2,h3{{font-family:var(--display);text-wrap:balance;line-height:1.2;margin:0}} h1{{font-size:2rem;font-weight:600}} h2{{font-size:1.3rem;font-weight:600;padding-top:8px;border-top:2px solid var(--fg)}} h3{{font-size:1.02rem;font-weight:600}}
p{{margin:0}} .stack{{display:grid;gap:12px}} .eyebrow{{font-family:var(--display);font-size:.75rem;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);font-weight:500}}
.lede{{font-size:1.1rem}} .note{{font-family:var(--display);font-size:.9rem;color:var(--muted);line-height:1.45}}
.status{{display:flex;flex-wrap:wrap;gap:8px;font-family:var(--display);font-size:.82rem}} .status span{{border:1px solid var(--rule);padding:4px 10px;border-radius:3px;background:var(--paper)}} .status .live{{border-color:var(--accent);color:var(--accent);font-weight:500}}
.tag{{display:inline-block;font-family:var(--display);font-size:.66rem;font-weight:600;letter-spacing:.04em;padding:1px 6px;border-radius:3px;margin-right:4px;vertical-align:middle}}
.tag.e{{background:var(--exist-bg);color:var(--exist)}} .tag.p{{background:var(--pred-bg);color:var(--pred)}} .tag.r{{background:var(--real-bg);color:var(--real)}} .tag.x{{background:var(--res-bg);color:var(--res)}} .tag.f{{background:var(--flag-bg);color:var(--flag)}}
.legend{{display:flex;flex-wrap:wrap;gap:8px 18px;font-family:var(--display);font-size:.82rem;align-items:center}}
.kinds{{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:14px}}
.kind{{background:var(--paper);border:1px solid var(--rule);border-top:3px solid var(--accent);padding:14px 16px;display:grid;gap:6px;min-width:0;font-size:.93rem}}
.kind .kid{{font-family:var(--display);font-size:.74rem;color:var(--muted)}} .kind .voice{{font-style:italic;color:var(--muted)}} .kind .n{{font-family:var(--display);font-size:.76rem;color:var(--accent)}}
.tablewrap{{overflow-x:auto;border:1px solid var(--rule);background:var(--paper)}}
table{{border-collapse:collapse;width:100%;min-width:860px;font-family:var(--display);font-size:.8rem;font-variant-numeric:tabular-nums}} th,td{{padding:6px 8px;border-bottom:1px solid var(--rule);text-align:center}} th{{background:var(--bg);font-weight:600;font-size:.74rem}} td.cn{{text-align:left;white-space:nowrap}} td.z{{color:var(--rule)}}
.cluster{{background:var(--paper);border:1px solid var(--rule);padding:16px 18px;display:grid;gap:10px;min-width:0}}
.cluster header{{display:flex;flex-wrap:wrap;justify-content:space-between;gap:6px 14px;align-items:baseline;border-bottom:1px solid var(--rule);padding-bottom:8px}}
.cluster .count{{font-family:var(--display);font-size:.78rem;color:var(--muted)}}
.sq{{display:grid;gap:6px;padding:10px 0;border-top:1px solid var(--rule)}} .sqh{{display:flex;flex-wrap:wrap;gap:6px 10px;align-items:baseline}} .sqid{{font-family:var(--display);font-size:.74rem;color:var(--accent);font-weight:600}} .sqlabel{{font-family:var(--display);font-weight:600;font-size:.95rem}} details summary{{font-family:var(--display);font-size:.78rem;color:var(--muted);cursor:pointer;padding-left:4.2rem}} details ol{{margin-top:6px}}\n.qs{{list-style:none;margin:0;padding:0;display:grid;gap:7px}}
.qs li{{display:grid;grid-template-columns:4.2rem 1fr auto;gap:8px;align-items:baseline;font-size:.95rem;min-width:0}}
.qs .id{{font-family:var(--display);font-size:.72rem;color:var(--muted)}} .qs .body{{min-width:0}} .qs q{{quotes:"“" "”"}}
.qs .ref{{font-family:var(--display);font-size:.7rem;color:var(--muted);margin-left:6px}}
.qs .meta{{font-family:var(--display);font-size:.7rem;white-space:nowrap}} .qs .meta .k{{color:var(--muted);margin-left:3px}}
@media (max-width:640px){{body{{font-size:16px}} h1{{font-size:1.6rem}} .qs li{{grid-template-columns:1fr}} .qs .meta{{white-space:normal}}}}
</style>
<div class="wrap">
<header class="col stack">
  <p class="eyebrow">Question program · step one · repository draft v0.4</p>
  <h1>Who comes to the table, and what they ask</h1>
  <p class="lede">The visitor-side question repository: twelve kinds of visitor, {len(C)} clusters, {len(SQ)} sub-questions, {len(questions)} wordings. Each question is quoted from the repo, reported from the pilot or from Mark, or predicted here in visitor wording. Nothing on this page is an answer.</p>
  <div class="status"><span class="live">Phase: divergent, filled out for reaction</span><span>{src_count["EXISTS"]} exist in the repo</span><span>{src_count["PREDICTED"]} predicted</span><span>{src_count["REAL"]} real</span>{f'<span>{src_count["RESEARCH"]} from research review</span>' if src_count["RESEARCH"] else ''}<span>{sum(flag_count.values())} flagged</span><span>{len(SQ)} sub-questions are the coverage unit</span></div>
  <div class="legend"><span><span class="tag e">EXISTS</span>canon, curriculum, starters, site links or probes</span><span><span class="tag p">PREDICTED</span>written here</span><span><span class="tag r">REAL</span>pilot or Mark, with date</span><span><span class="tag x">RESEARCH</span>added from the research review</span><span><span class="tag f">FAC · NF · VERSE · NAMED</span>Facilitator ground · never faced · one passage · named person</span></div>
  <p class="note">Real visitor wording is thin: about 15 to 18 dashboard questions so far, held on the server. The 40 RESEARCH questions come from the Opus review (separate page), accepted by Mark on 25 October 2026, each with its study named. Known limits of that evidence: it is mostly US, Protestant and often ministry-commissioned; Pew, PRRI, Gallup and the peer-reviewed grief work carry the most weight; nothing was found on what students, history lovers, Orthodox or Global South visitors ask. The real pilot questions are the better guide there and are worth growing.</p>
</header>
<section class="stack"><div class="col stack"><h2>The twelve kinds</h2></div><div class="kinds">{kind_cards}</div></section>
<section class="stack"><div class="col stack"><h2>Coverage by kind and cluster</h2><p class="note">How many sub-questions each kind touches in each cluster. A dot is zero. Sub-questions are the unit; wordings under them are kept for retrieve-when lines and probes but not counted.</p></div><div class="tablewrap">{matrix}</div></section>
<section class="stack"><div class="col stack"><h2>The repository</h2><p class="note">One section per cluster, one block per sub-question: the canonical wording first, the other wordings folded beneath. Ids are stable (append only), so later searches and Open Gaps entries can cite them. An item moved between clusters keeps its birth id and shows where it came from; C17 (challenging the system) was split out on 25 October so the content clusters hold only questions the worlds answer in character.</p></div>{cluster_html}</section>
</div>
"""
open(OUT, "w").write(page)
print(f"wrote {OUT}: {len(questions)} questions; {dict(src_count)}; flags {dict(flag_count)}")
print("per kind:", dict(sorted(kind_count.items())))
