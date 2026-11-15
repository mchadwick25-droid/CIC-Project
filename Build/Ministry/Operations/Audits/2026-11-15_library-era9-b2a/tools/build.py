#!/usr/bin/env python3
import json, re, os, sys
sys.path.insert(0, os.path.dirname(__file__)); import ia
S = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
picks = {}
for g in "A B C D E F X".split():
    if not os.path.exists(f"{S}/g{g}/picks.json"): continue
    for p in json.load(open(f"{S}/g{g}/picks.json")):
        p["_g"] = g; picks[p["ia_id"]] = p
LANG = {"fre": "fra", "fra": "fra", "spa": "spa", "por": "por", "gre": "ell", "ell": "ell", "ara": "ara", "arm": "hye", "hye": "hye", "jpn": "jpn", "chi": "zho", "zho": "zho", "mlg": "mlg", "xho": "xho", "sot": "sot", "tgl": "tgl", "ukr": "ukr", "pol": "pol", "bul": "bul", "amh": "amh", "ita": "ita", "eng": "eng", "ger": "deu", "deu": "deu", "dut": "nld", "nld": "nld", "wel": "cym", "cym": "cym", "rus": "rus", "lat": "lat"}
TR = json.load(open(f"{S}/tools/translators.json")) if os.path.exists(f"{S}/tools/translators.json") else {}
OV = json.load(open(f"{S}/tools/overrides.json")) if os.path.exists(f"{S}/tools/overrides.json") else {}
def clean(s):
    s = re.sub(r"\s+", " ", str(s or "")).strip()
    return s
def dot(s):
    s = clean(s); return s if not s or s[-1] in ".!?" else s + "."
NARR = re.compile(r"pick|located|not taken|not fetched|downloaded|see report|report|wanted-row|searched|\bbelow\b|avoid|Use the|candidate|host date|not checked|not sampled|not viewed|flag", re.I)
def keep(text):
    out = [x for x in re.split(r"(?<=[.!?])\s+", clean(text)) if x and not NARR.search(x)]
    return " ".join(out)
IMG = json.load(open(f"{S}/tools/img.json")) if os.path.exists(f"{S}/tools/img.json") else {}
def roman(n):
    out = ""
    for v, t in [(1000,"M"),(900,"CM"),(500,"D"),(400,"CD"),(100,"C"),(90,"XC"),(50,"L"),(40,"XL"),(10,"X"),(9,"IX"),(5,"V"),(4,"IV"),(1,"I")]:
        while n >= v: out += t; n -= v
    return out
from build_strip import strip_host
def find_basis(i, y, L):
    if IMG.get(str(i)) is not None: return f"read on the scan's page image, leaf n{IMG[i]}; the OCR does not give it cleanly", None
    for k, ln in enumerate(L[:420]):
        t = ln.strip()
        if re.fullmatch(r"\W*(%d|%s)\W*" % (y, " ?".join(roman(y))), t): return f"line {k+13} of this file, on the title page", t
    for k, ln in enumerate(L[:420]):
        t = ln.strip(); c = t.replace(" ", "").replace(".", "").replace(",", "")
        if len(t) <= 34 and (re.search(r"\b%d\b" % y, t) or roman(y) in c) and not re.search(r"copyright|entered|act of|library|digitiz|^[A-Z]{1,3} *[0-9]{2,5} ", t, re.I):
            return f"line {k+13} of this file, on the title page", t
    return None, None
def grade(t):
    t = clean(t).lower(); c = "clean" in t; f = "fair" in t or "not sampled" in t; g = "good" in t
    out = "clean to fair" if (c and f) else "fair to good" if (f and g) else "clean" if c else "fair"
    return out + (", in the old spelling" if "old spelling" in t or "old orthography" in t else "")
def nn(s): return clean(s) and clean(s).lower() not in ("none", "null", "none seen", "n/a")
import glob
NOTES = {}
for f in glob.glob(f"{S}/notes_out_*.json"):
    for n in json.load(open(f)): NOTES[n["key"]] = n
spec = []
for l in open(f"{S}/tools/table.txt"):
    if l.startswith("#") or not l.strip(): continue
    i, fn, atlas, role, conf, dt, want = l.rstrip("\n").split("|")
    p = picks[i]; o = OV.get(i, {})
    src = f"{S}/g{p['_g']}/dl/{i}_djvu.txt"
    raw = open(src, "rb").read(); words = len(raw.decode("utf-8", "replace").split())
    m = json.loads(ia.get("https://archive.org/metadata/" + i)).get("metadata", {})
    assert "access-restricted-item" not in m, i
    if "licenseurl" in m:
        assert "publicdomain" in m["licenseurl"], (i, m["licenseurl"])
        hr = f"the archive.org record carries the Public Domain Mark (licenseurl {m['licenseurl']}), and the imprint date agrees"
    elif "possible-copyright-status" in m:
        hr = f"the archive.org record says possible-copyright-status {clean(m['possible-copyright-status'])}, and the imprint date agrees"
        hr = hr.replace("..", ".")
    elif "rights" in m:
        hr = "the archive.org record's rights statement reads: " + re.sub(r"<[^>]+>", "", clean(m["rights"]))[:300]
    else:
        hr = "the archive.org record carries no rights field, so the imprint date is the basis"
    y = int(o.get("year") or p["imprint_year"]); lang = o.get("language") or LANG.get(clean(p["language"])[:3].lower(), None)
    assert lang, (i, p["language"])
    title = o.get("title") or clean(p["title_page_words"]).rstrip(".")
    creator = o.get("creator") or clean(p["author_as_printed"])
    if not o.get("creator") and nn(p.get("editor_translator_as_printed")): creator += "; " + clean(p["editor_translator_as_printed"])
    pub = o.get("publisher") or clean(p["place_publisher_as_printed"])
    L0 = raw.decode("utf-8").split("\n")
    cut = None
    if o.get("cut_at"):
        assert re.search(o["cut_check"], L0[o["cut_at"] - 1]), (i, L0[o["cut_at"] - 1])
        cut = f"the host file also holds {o['cut_what']}, which is not taken: the text is cut before host OCR line {o['cut_at']:,} (of {len(L0):,})"
        L0 = L0[:o["cut_at"] - 1]
    pre = None
    if o.get("pre_upto"):
        assert re.search(o["pre_check"], L0[o["pre_upto"] - 1]), (i, L0[o["pre_upto"] - 1])
        pre = f"{o['pre_what']} (host OCR lines 1-{o['pre_upto']})"; L0 = L0[o["pre_upto"]:]
    L, stripped = strip_host(L0)
    stripped = "; and ".join(x for x in (pre, stripped) if x) or None
    left = sum(1 for x in L if re.fullmatch(r"\W*(Digiti[sz]ed by|Hosted by)\W*", re.sub(r"\s+", " ", x).strip(), re.I) or re.fullmatch(r"\W*(\w{0,8} ?[,.] ?)?G[oO0]{2}[gq][l1I][eC]\W*", re.sub(r"\s+", " ", x).strip()))
    delta = o.get("delta", 0)
    def shift(t):
        if not delta: return t
        def f(m): return m.group(1) + re.sub(r"\d+", lambda x: str(int(x.group(0)) + delta), m.group(2))
        return re.sub(r"\b(lines? )((?:\d+(?:-\d+)?(?:, and |, | and | to |; )?)+)", f, t)
    body = "\n".join(L); words = len(body.split())
    fb, shown = find_basis(i, int(o.get("year") or p["imprint_year"]), L)
    basis = o.get("basis") or fb
    if o.get("basis_re"):
        ks = [k for k in range(min(len(L), o.get("basis_max", 1500))) if re.search(o["basis_re"], re.sub(r"\s+", " ", L[k]))]
        assert ks, (i, o["basis_re"]); k = ks[0]
        basis = o["basis_tpl"].format(n=k + 13, t=re.sub(r"\s+", " ", L[k]).strip().replace("'", ""))
        print("RE-BASIS", i[:28], "|", basis[:200])
    if not basis: print("NO-BASIS", i, clean(p["imprint_read_at"])[:120]); basis = "UNSET"
    else: print("BASIS", i[:28], "|", basis[:40], "|", shown)
    content = dot(o.get("content") or keep(p.get("content_note") or "Draft; the content note is written after the text is checked"))
    if not o.get("content"):
        for lab, k in (("Divisions", "divisions"), ("Editorial matter", "editorial_matter"), ("Mixed voices", "mixed_voices")):
            if nn(p.get(k)) and keep(p[k]): content += f" {lab}: {dot(keep(p[k]))}"
    if i in NOTES:
        content = dot(shift(clean(NOTES[i]["content"])))
        title = clean(NOTES[i].get("title") or title).rstrip("."); creator = clean(NOTES[i].get("creator") or creator); pub = clean(NOTES[i].get("publisher") or pub)
    fs = o.get("final_sub", {})
    if "title" in fs: assert fs["title"][0] in title, i; title = title.replace(*fs["title"])
    if "creator" in fs: assert fs["creator"][0] in creator, i; creator = creator.replace(*fs["creator"])
    if o.get("content_sub"): assert o["content_sub"][0] in content, (i, content[:300]); content = content.replace(*o["content_sub"])
    for x in o.get("strip", []): assert x in content, (i, x); content = clean(content.replace(x, ""))
    if o.get("strip_re"): assert re.search(o["strip_re"], content), i; content = clean(re.sub(o["strip_re"], "", content))
    if o.get("title_sub") and o["title_sub"][0] in title: title = title.replace(*o["title_sub"])
    if o.get("add"): content += " " + o["add"]
    content += f" About {words:,} words."
    wp = p.get("wanted_passages") or []
    locus = "the whole volume; not mapped"
    wp = [w for w in wp if re.fullmatch(r"[\d ,\-and;]+", clean(w.get("ocr_lines"))) and not NARR.search(clean(w.get("what")))]
    if i in NOTES: locus = shift(clean(NOTES[i]["locus"])); wp = []
    if o.get("locus"): locus = o["locus"]
    elif wp:
        locus = "; ".join(f"{clean(w.get('what'))[:90]} at OCR lines {clean(w.get('ocr_lines'))}" for w in wp[:4]) + "; the rest not mapped"
    work = o.get("work") or (title if len(title) <= 110 else title[:110].rsplit(" ", 1)[0])
    if dt == "U":
        date = {"formation_confidence": "unknown", "checked": f"the title page and front matter of this printing ({y}); they do not state when the text was first written"}
    else:
        a, b = dt.split("-"); date = {"start": int(a), "end": int(b), "source": o.get("date_source") or (basis if o.get("nodate") else f"the printing's own title page: {basis}"), "formation_confidence": "Documented"}
    if o.get("nodate"):
        hr = hr.replace("and the imprint date agrees", "and the date agrees").replace("so the imprint date is the basis", "so the date named here is the basis")
        hr += "; the date used is that of " + basis
    row = {"work": work, "author": fn.split("_")[0], "locus": locus, "atlas_ids": atlas.split(","), "role": role, "confidence": conf, "language": lang, "date": date}
    if i in TR: row["translator"] = {"name": TR[i], "source": "the title page", "formation_confidence": "Documented"}
    row["edition_date"] = {"year": y, "source": basis, "formation_confidence": "Documented"}
    row["note"] = o.get("note") or dot(want[0].upper() + want[1:])
    if o.get("note_add"): row["note"] += " " + o["note_add"]
    spec.append({"filename": fn + ".txt", "ia_id": i, "src": src, "bytes": len(raw), "stripped": stripped, "cut_at": o.get("cut_at"), "pre_upto": o.get("pre_upto"), "cut": cut, "left": left, "body_bytes": len(body.encode()), "title": title, "creator": creator, "publisher": pub, "year": y, "year_basis": basis,
                 "host_rights": hr, "stamps": o.get("stamps"), "language": lang, "ocr": dot(o.get("ocr") or grade(p["ocr_quality"])), "content": content,
                 "want": "Wanted Sources (2026-11-12), " + want + ".", "seed_world": atlas.split(",")[0], "seed_author": creator, "why": "Wanted Sources, " + want + ".", "rows": [row], "words": words})
json.dump(spec, open(f"{S}/spec.json", "w"), ensure_ascii=False, indent=1)
print(len(spec), "files", sum(s["bytes"] for s in spec) // 1e6, "MB", sum(s["words"] for s in spec), "words")
for s in []: print(f'{s["filename"][:60]} | T: {s["title"][:150]} | C: {s["creator"][:110]} | P: {s["publisher"][:90]} | {s["year"]}')
