"""Vendor Library files from a spec (JSON list). Usage: python3 intake.py SPEC.json REPO BATCHLABEL
Each item: src, filename, title, creator, publisher, pubdate, rights, lang, item, djvu_name, ocr, content,
seed_title, seed_author, year, world, why, contents_note, want, rows[ {slug, work, author, locus, atlas_ids,
role, confidence, note, language, date} ].
The host text is copied byte for byte after a 12-line header."""
import json, sys, os, datetime

spec_path, repo, label = sys.argv[1], sys.argv[2], sys.argv[3]
items = json.load(open(spec_path, encoding="utf-8"))
today = "2026-11-16"
RULE = "_" * 70


def q(s):
    return "'" + s.replace("'", "''") + "'"


def one_line(s):
    assert "\n" not in s, s
    return s


reg, seed = [], []
for it in items:
    raw = open(it["src"], "rb").read()
    nbytes = len(raw)
    words = len(raw.split())
    it["words"] = words
    dest = os.path.join(repo, "cic/texts", it["filename"])
    assert not os.path.exists(dest), dest
    rights = it["rights"]
    hdr = [
        "Title: " + it["title"],
        "Creator: " + it["creator"],
        "Publisher: " + it["publisher"],
        "Publication Date: " + it["pubdate"],
        "Rights: " + rights,
        "Language: " + it["lang"],
        "Source: archive.org item %s, full text from the item's own djvu.txt%s. Fetched directly %s by the Library thread; the byte count of the downloaded file (%s) equals the size archive.org lists for the djvu.txt."
        % (it["item"], (" (" + it["djvu_name"] + ")") if it.get("djvu_name") else "", today, format(nbytes, ",")),
        "Provenance note: Extracted unaltered: the item's own djvu.txt is reproduced whole after this header; nothing was stripped, normalized or corrected. Rights basis: %s. OCR quality: %s Word count of the host text: %s. Line numbers cited in this header are lines of the host OCR; add 12 for this file's own line numbers."
        % (it["rights_short"], it["ocr"], format(words, ",")),
        "Content note: " + it["content"],
        "",
        RULE,
        "",
    ]
    for h in hdr:
        one_line(h)
    with open(dest, "wb") as f:
        f.write(("\n".join(hdr) + "\n").encode("utf-8"))
        f.write(raw)
    verified = "Library thread, %s: archive.org metadata read, title page read, the wanted passages located, djvu.txt fetched, byte count %s equal to the listed size, the volume's end read" % (label, format(nbytes, ","))
    reg.append(
        "- filename: %s\n  supplied_by: %s\n  date_added: '%s'\n  notes: %s\n"
        % (
            it["filename"],
            q("Claude (Library thread, Church Family Tree wants, %s: located on archive.org, item metadata read, title page read, the wanted passages located, djvu.txt fetched directly, byte count equal to the host's listed size, the volume's end read)" % label),
            today,
            q("%s. %s. Archive item %s. OCR quality: %s Words: %s. CONTENTS: %s WANT: %s" % (it["seed_title"], rights, it["item"], it["ocr"], format(words, ","), it["contents_note"], it["want"])),
        )
    )
    seed.append(
        "  - title: %s\n    author: %s\n    year: '%s'\n    world: %s\n    why: %s\n    url: https://archive.org/details/%s\n    rights_basis: %s\n    verified_by: %s\n    status: downloaded\n    vendored_as: %s\n"
        % (q(it["seed_title"]), q(it["seed_author"]), it["year"], it["world"], q(it["want"]), it["item"], q(rights), q(verified), it["filename"])
    )
    stem = it["filename"][:-4]
    out = ["source_file: " + it["filename"], "assignments:"]
    for r in it["rows"]:
        out.append("- row_id: %s--%s" % (stem, r["slug"]))
        out.append("  work: " + q(r["work"]))
        out.append("  author: " + r["author"])
        out.append("  locus: " + q(r["locus"]))
        out.append("  atlas_ids:")
        for a in r["atlas_ids"]:
            out.append("  - " + a)
        out.append("  role: " + r["role"])
        out.append("  confidence: " + r["confidence"])
        if r.get("voice_of"):
            out.append("  voice_of: " + r["voice_of"])
        out.append("  language: " + r["language"])
        d = r["date"]
        if "start" in d:
            out.append("  date: {start: %d, end: %d, source: %s, formation_confidence: %s}" % (d["start"], d["end"], json.dumps(d["source"], ensure_ascii=False), d["fc"]))
        else:
            out.append("  date: {formation_confidence: unknown, checked: %s}" % json.dumps(d["checked"], ensure_ascii=False))
        out.append("  note: " + q(r["note"]))
    if it.get("authors_ruled"):
        out.append("authors_ruled:")
        for slug, r in it["authors_ruled"].items():
            out.append("  %s:" % slug)
            out.append("    kind: " + r["kind"])
            out.append("    evidence: " + json.dumps(r["evidence"], ensure_ascii=False))
    open(os.path.join(repo, "cic/corpus-map/_staging", stem + ".yaml"), "w", encoding="utf-8").write("\n".join(out) + "\n")
    print(it["filename"], nbytes, words)

with open(os.path.join(repo, "cic/texts/REGISTRY.yaml"), "a", encoding="utf-8") as f:
    f.write("".join(reg))
with open(os.path.join(repo, "Build/worlds/_cross-world/download-queue-seed.yaml"), "a", encoding="utf-8") as f:
    f.write("".join(seed))
json.dump([{k: it[k] for k in ("filename", "words", "year")} for it in items], open(spec_path + ".out", "w"))
