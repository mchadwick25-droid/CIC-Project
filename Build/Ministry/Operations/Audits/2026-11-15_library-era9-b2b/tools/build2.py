#!/usr/bin/env python3
"""build2.py : table.txt + overrides.json + g*/picks.json (+ notes_out_*.json) -> spec.json and staged files in S/stage/.
Line numbers everywhere in the output are lines of the staged (= vendored) file."""
import json, re, os, sys, glob
sys.path.insert(0, os.path.dirname(__file__)); import ia
S = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HDR = 12
picks = {}
for g in "A B C D E R X".split():
    f = f"{S}/g{g}/picks.json"
    if os.path.exists(f):
        for p in json.load(open(f)): p["_g"] = g; picks[p["ia_id"]] = p
LANG = {"eng": "eng", "ger": "deu", "deu": "deu", "dut": "nld", "nld": "nld", "wel": "cym", "cym": "cym", "fre": "fra", "fra": "fra", "lat": "lat"}
OV = json.load(open(f"{S}/tools/overrides.json"))
MC = f"{S}/metacache"; os.makedirs(MC, exist_ok=True)
def meta(i):
    f = f"{MC}/{i}.json"
    if not os.path.exists(f): open(f, "wb").write(ia.get("https://archive.org/metadata/" + i))
    return json.load(open(f)).get("metadata", {})
def ocrq(s): return re.split(r"[;.(:,]", clean(s))[0].strip().lower() or 'fair'
def clean(s): return re.sub(r"\s+", " ", str(s or "")).strip()
def dot(s):
    s = clean(s); return s if not s or s[-1] in ".!?" else s + "."
def roman(n):
    out = ""
    for v, t in [(1000,"M"),(900,"CM"),(500,"D"),(400,"CD"),(100,"C"),(90,"XC"),(50,"L"),(40,"XL"),(10,"X"),(9,"IX"),(5,"V"),(4,"IV"),(1,"I")]:
        while n >= v: out += t; n -= v
    return out
def strip_host(raw):
    """Remove Google's own preamble (its 'Google' mark, the notice that begins 'This is a digital copy of a book',
    through the web-address line that closes 'About Google Book Search'), when the file opens with it."""
    L = raw.split(b"\n")
    sq = lambda l: re.sub(rb"\s+", b" ", l).strip()
    dk = next((k for k, l in enumerate(L[:40]) if sq(l).startswith(b"This is a digital copy of a book")), None)
    if dk is None: return raw, None
    nb = [k for k, l in enumerate(L[:dk]) if l.strip()]
    assert all(re.fullmatch(rb"Go ?ogle", sq(L[k])) for k in nb), ("text before preamble", [L[k] for k in nb])
    startk = nb[0] if nb else dk
    ak = next(k for k, l in enumerate(L[:200]) if sq(l) in (b"About Google Book Search", "\u00dcber Google Buchsuche".encode()))
    end = next(k for k in range(ak + 1, ak + 12) if b"http" in L[k] or b":/" in L[k] or b"com/" in L[k].replace(b" ", b""))
    cut = L[startk:end + 1]
    body = b"\n".join(L[:startk] + L[end + 1:])
    return body, f"Google's own preamble to its scans ({len(cut)} lines, {len(raw) - len(body):,} bytes: the notice that begins 'This is a digital copy of a book', through the web-address line that closes its section '{sq(L[ak]).decode()}') was removed at intake"
def find_basis(y, L):
    for k, ln in enumerate(L[HDR:HDR + 460]):
        t = ln.strip(); c = t.replace(" ", "").replace(".", "").replace(",", "")
        if len(t) <= 40 and (re.search(r"\b%d\b" % y, t) or roman(y) in c) and not re.search(r"copyright|entered|act of|library|digitiz|^[A-Z]{1,3} *[0-9]{2,5} ", t, re.I):
            return k + HDR + 1, t
    return None, None
NOTES = {}
for f in glob.glob(f"{S}/notes_out_*.json"):
    for n in json.load(open(f)): NOTES[n["key"]] = n
os.makedirs(f"{S}/stage", exist_ok=True)
spec = []; notes_in = []
for l in open(f"{S}/tools/table.txt"):
    if l.startswith("#") or not l.strip(): continue
    i, fn, atlas, role, conf, dt, want = l.rstrip("\n").split("|")
    p = picks[i]; o = OV.get(i, {})
    src = f"{S}/g{p['_g']}/dl/{i}_djvu.txt"
    raw0 = open(src, "rb").read(); m = meta(i)
    djvu = [f for f in json.load(open(f"{MC}/{i}.json"))["files"] if f["name"].endswith("_djvu.txt")][0]
    assert str(len(raw0)) == str(djvu["size"]), ("SIZE", i)
    assert "access-restricted-item" not in m, i
    assert not re.search("inlibrary|printdisabled", str(m.get("collection"))), ("LENDING", i)
    raw, stripped = strip_host(raw0)
    y = int(o.get("year") or p["imprint_year"])
    if "licenseurl" in m:
        assert "publicdomain" in m["licenseurl"], (i, m["licenseurl"])
        hr = f"the archive.org record carries the Public Domain Mark (licenseurl {m['licenseurl']}), and the imprint date agrees"
    elif "possible-copyright-status" in m:
        hr = f"the archive.org record says possible-copyright-status {clean(m['possible-copyright-status']).rstrip('.')}, and the imprint date agrees"
    elif "rights" in m:
        hr = "the archive.org record's rights statement reads: " + re.sub(r"<[^>]+>", "", clean(m["rights"]))[:300]
    else:
        hr = "the archive.org record carries no rights field, so the imprint date is the basis"
    lang = o.get("language") or LANG.get(clean(p["language"])[:3].lower()); assert lang, (i, p["language"])
    title = o.get("title") or clean(p["title_page_words"]).rstrip(".")
    creator = o.get("creator") or clean(p["author_as_printed"])
    pub = o.get("publisher") or clean(p["place_publisher_as_printed"])
    words = len(raw.decode("utf-8", "replace").split())
    # staged file with a placeholder content line, to fix line numbers
    def header(content, basis):
        rights = f'Public Domain (pd-us-by-date: published {y}); {hr}'
        if o.get("nodate"):
            rights = rights.replace("and the imprint date agrees", "and the date agrees").replace("so the imprint date is the basis", "so the date named here is the basis") + ("; the scan has no title page" if o.get("notp") else "; the title page prints no year") + ", and the date used is that of " + basis
        if o.get("stamps"): rights += "; " + o["stamps"]
        prov = "Extracted unaltered: the item's own djvu.txt is reproduced whole after this header; nothing was stripped, normalized or corrected." if not stripped else f"The item's own djvu.txt is reproduced after this header with one host addition taken out: {stripped}. Nothing else was stripped, normalized or corrected, and the edition's own words are untouched."
        size = f"the byte count of the downloaded file ({len(raw0):,}) equals the size archive.org lists for the djvu.txt"
        h = [f"Title: {title}", f"Creator: {creator}", f"Publisher: {pub}", f"Publication Date: {y} ({basis})", f"Rights: {rights}", f"Language: {lang}",
             f"Source: archive.org item {i}, full text from the item's own djvu.txt. Fetched directly 2026-11-15 by the Library thread; {size}.",
             f"Provenance note: {prov} Rights basis: published {y}, out of US copyright by date. OCR quality: {dot(o.get('ocr') or ocrq(p['ocr_quality']))} Line numbers cited in this header are this file's own lines.",
             f"Content note: {content}"]
        for x in h: assert "\n" not in x, (i, x[:50])
        return rights, ("\n".join(h) + "\n\n" + "_" * 70 + "\n\n").encode() + raw
    L = (b"\n" * HDR + raw).decode("utf-8", "replace").split("\n")
    ln, shown = find_basis(y, L)
    basis = o.get("basis") or (f"line {ln}, on the title page" if ln else None)
    if not basis: print("NO-BASIS", i, clean(p.get("imprint_read_at"))[:140]); basis = "UNSET"
    else: print("BASIS", i[:30], "|", basis[:60], "|", shown, "| picker:", clean(p.get("imprint_read_at"))[:60])
    n = NOTES.get(i)
    content = dot(clean(o.get("content") or (n and n["content"]) or "PENDING")) + f" About {words:,} words."
    locus = o.get("locus") or (n and clean(n["locus"])) or "the whole volume; not mapped"
    rights, out = header(content, basis)
    open(f"{S}/stage/{fn}.txt", "wb").write(out)
    notes_in.append({"file": f"{S}/stage/{fn}.txt", "key": i, "title": title, "draft": clean(p.get("content_note")), "draft_divisions": clean(p.get("divisions")), "draft_editorial": clean(p.get("editorial_matter")), "draft_mixed": clean(p.get("mixed_voices")), "draft_cautions": clean(p.get("cautions")), "stripped_lines": 0 if not stripped else int(re.search(r"\((\d+) lines", stripped).group(1))})
    work = o.get("work") or (title if len(title) <= 110 else title[:110].rsplit(" ", 1)[0])
    if dt == "U":
        date = {"formation_confidence": "unknown", "checked": f"the title page and front matter of this printing ({y}); they do not state when the text was first written"}
    else:
        a, b = dt.split("-"); date = {"start": int(a), "end": int(b), "source": o.get("date_source") or (basis if o.get("nodate") else f"the printing's own title page: {basis}"), "formation_confidence": o.get("date_conf") or "Documented"}
    row = {"work": work, "author": o.get("author") or fn.split("_")[0], "locus": locus, "atlas_ids": atlas.split(","), "role": role, "confidence": conf, "language": lang, "date": date}
    if o.get("translator"): row["translator"] = {"name": o["translator"], "source": o.get("translator_source") or "the title page", "formation_confidence": "Documented"}
    row["edition_date"] = {"year": y, "source": basis, "formation_confidence": "Documented"}
    row["note"] = o.get("note") or dot(want[0].upper() + want[1:])
    spec.append({"filename": fn + ".txt", "ia_id": i, "title": title, "creator": creator, "publisher": pub, "year": y, "rights": rights, "language": lang,
                 "ocr": dot(o.get("ocr") or ocrq(p["ocr_quality"])), "content": content, "want": "Wanted Sources (2026-11-12), " + want + ".", "seed_world": atlas.split(",")[0],
                 "why": "Wanted Sources, " + want + ".", "rows": [row], "words": words, "bytes0": len(raw0), "authors_ruled": o.get("authors_ruled")})
json.dump(spec, open(f"{S}/spec.json", "w"), ensure_ascii=False, indent=1)
json.dump(notes_in, open(f"{S}/notes_in.json", "w"), ensure_ascii=False, indent=1)
print(len(spec), "files", sum(s["words"] for s in spec), "words")
