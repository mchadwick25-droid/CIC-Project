#!/usr/bin/env python3
import json, re, os, sys
sys.path.insert(0, os.path.dirname(__file__)); import ia
S = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
picks = {}
for g in "A B C1 C2 D E F".split():
    for p in json.load(open(f"{S}/g{g}/picks.json")):
        p["_g"] = g; picks[p["ia_id"]] = p
picks["declarationslett00dolluoft"] = {"_g": "D", "row": 195, "ia_id": "declarationslett00dolluoft",
  "title_page_words": "Declarations and Letters on the Vatican Decrees, 1869-1887, by Ignaz von Dollinger. Authorised translation",
  "author_as_printed": "Ignaz von Dollinger", "editor_translator_as_printed": "the editor's preface is unsigned on its first page; the host record names F. H. Reusch as editor; the translator is not named on the title page",
  "place_publisher_as_printed": "Edinburgh: T. & T. Clark, 38 George Street", "imprint_year": 1891,
  "imprint_read_at": "page image leaf n8 ('1891.'); the OCR at line 93 reads '189,'", "language": "eng",
  "ocr_quality": "clean.", "content_note": "Dollinger's declarations and letters on the decrees of the Vatican council, from 1869 to 1887, in an English translation. A publisher's list stands before the title page. The editor's preface begins at OCR line 97 and quotes a letter of Dollinger's of 2 October 1886; contents lists stand at lines 218 and 267. Some documents are printed in French. The pieces were not mapped.",
  "divisions": "numbered declarations and letters, listed in the contents at OCR lines 218 and 267", "editorial_matter": "the editor's preface from OCR line 97", "mixed_voices": "letters to Dollinger may be printed beside his answers; not mapped",
  "cautions": "A translation; the German original (Briefe und Erklarungen, 1890) was located but its OCR cannot be read.", "wanted_passages": []}
LANG = {"eng": "eng", "ger": "deu", "deu": "deu", "dut": "nld", "nld": "nld", "wel": "cym", "cym": "cym", "rus": "rus", "lat": "lat"}
TR = {"whatischristiani00harn_2": "Thomas Bailey Saunders", "bloodofjesuswhat00wald": "J. G. Princell", "lifepastorflied00fliegoog": "Catherine Winkworth", "historyofinsurre00call": "John Oxenford"}
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
IMG = {"retrospectioni00eddy": 8, "memoirsofjosephj02gurn": 6, "nationalapostasy00kebl": 2, "gtu_32400003383456": 6, "historyofamerica00noyeuoft": 8, "indarkestengland00bootuoft": 8, "christianbaptis00campgoog": 9, "lecturesonreviva00finn_1": 6, "viewsprophecies00himegoog": 9, "booksofthaepingd00medh": 2, "lettersonmorala00thomgoog": 9, "declarationslett00dolluoft": 8, "lifeofedwardirvi02olipuoft": 6, "memoirsalexande00richgoog": 10, "tipingtienkwohhi01lind": 8, "tractaatvande00kuyp": 6, "hometalks00noyegoog": None}
def roman(n):
    out = ""
    for v, t in [(1000,"M"),(900,"CM"),(500,"D"),(400,"CD"),(100,"C"),(90,"XC"),(50,"L"),(40,"XL"),(10,"X"),(9,"IX"),(5,"V"),(4,"IV"),(1,"I")]:
        while n >= v: out += t; n -= v
    return out
def find_basis(i, y, L):
    if IMG.get(i) is not None: return f"read on the scan's page image, leaf n{IMG[i]}; the OCR does not give it cleanly", None
    for k, ln in enumerate(L[:420]):
        t = ln.strip(); c = t.replace(" ", "").replace(".", "").replace(",", "")
        if len(t) <= 34 and (re.search(r"\b%d\b" % y, t) or roman(y) in c) and not re.search(r"copyright|entered|act of|library|digitiz|^[A-Z]{1,3} *[0-9]{2,5} ", t, re.I):
            return f"OCR line {k+1}, on the title page", t
    return None, None
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
    L = raw.decode("utf-8", "replace").split("\n")
    fb, shown = find_basis(i, int(o.get("year") or p["imprint_year"]), L)
    basis = o.get("basis") or fb
    if not basis: print("NO-BASIS", i, clean(p["imprint_read_at"])[:120]); basis = "UNSET"
    else: print("BASIS", i[:28], "|", basis[:40], "|", shown)
    content = dot(o.get("content") or keep(p["content_note"]))
    if not o.get("content"):
        for lab, k in (("Divisions", "divisions"), ("Editorial matter", "editorial_matter"), ("Mixed voices", "mixed_voices")):
            if nn(p.get(k)) and keep(p[k]): content += f" {lab}: {dot(keep(p[k]))}"
    if i in NOTES: content = dot(clean(NOTES[i]["content"]))
    for x in o.get("strip", []): assert x in content, (i, x); content = clean(content.replace(x, ""))
    if o.get("strip_re"): assert re.search(o["strip_re"], content), i; content = clean(re.sub(o["strip_re"], "", content))
    if o.get("title_sub") and o["title_sub"][0] in title: title = title.replace(*o["title_sub"])
    if o.get("add"): content += " " + o["add"]
    content += f" About {words:,} words."
    wp = p.get("wanted_passages") or []
    locus = "the whole volume; not mapped"
    wp = [w for w in wp if re.fullmatch(r"[\d ,\-and;]+", clean(w.get("ocr_lines"))) and not NARR.search(clean(w.get("what")))]
    if i in NOTES: locus = clean(NOTES[i]["locus"]); wp = []
    if o.get("locus"): locus = o["locus"]
    elif wp:
        locus = "; ".join(f"{clean(w.get('what'))[:90]} at OCR lines {clean(w.get('ocr_lines'))}" for w in wp[:4]) + "; add 12 to OCR line numbers; the rest not mapped"
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
    spec.append({"filename": fn + ".txt", "ia_id": i, "src": src, "bytes": len(raw), "title": title, "creator": creator, "publisher": pub, "year": y, "year_basis": basis,
                 "host_rights": hr, "stamps": o.get("stamps"), "language": lang, "ocr": dot(o.get("ocr") or p["ocr_quality"]), "content": content,
                 "want": "Wanted Sources (2026-11-12), " + want + ".", "seed_world": atlas.split(",")[0], "seed_author": creator, "why": "Wanted Sources, " + want + ".", "rows": [row], "words": words})
json.dump(spec, open(f"{S}/spec.json", "w"), ensure_ascii=False, indent=1)
print(len(spec), "files", sum(s["bytes"] for s in spec) // 1e6, "MB", sum(s["words"] for s in spec), "words")
for s in []: print(f'{s["filename"][:60]} | T: {s["title"][:150]} | C: {s["creator"][:110]} | P: {s["publisher"][:90]} | {s["year"]}')
