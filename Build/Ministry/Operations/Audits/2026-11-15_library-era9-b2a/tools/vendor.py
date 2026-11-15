#!/usr/bin/env python3
"""vendor.py <spec.json> [--dry]  : write cic/texts file, staging yaml, REGISTRY entry, seed row for each spec item.
Spec item keys: filename, ia_id, src, title, creator, publisher, year, year_basis, host_rights, stamps (opt),
language, ocr, content, want, seed_world, seed_author, why, rows[ {work, author, locus, atlas_ids, role,
confidence, voice_of?, language, date{}, translator{}?, edition_date{}, note} ]"""
import json, sys, os, yaml
R = "/home/user/CIC-Project"
BATCH = "era 9 batch 2a"
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_strip
def q(s): return "'" + s.replace("'", "''") + "'"
def main():
    spec = json.load(open(sys.argv[1])); dry = "--dry" in sys.argv
    reg = []; seed = []
    for s in spec:
        raw = open(s["src"], "rb").read()
        n = len(raw)
        assert n == s["bytes"], (s["filename"], n, s["bytes"])
        L0 = raw.decode("utf-8").split("\n")
        if s.get("cut_at"): L0 = L0[:s["cut_at"] - 1]
        if s.get("pre_upto"): L0 = L0[s["pre_upto"]:]
        L, stripped = build_strip.strip_host(L0)
        stripped = s["stripped"]
        body = "\n".join(L).encode(); assert len(body) == s["body_bytes"]
        cut = s.get("cut"); tail = " The edition's own text follows as the host gives it; nothing was normalized or corrected."
        if cut and stripped: prov = f"At intake the file was cut and the host's own additions were removed, and nothing else: {cut}; removed: {stripped}." + tail
        elif cut: prov = f"At intake the file was cut and nothing else was changed: {cut}." + tail
        elif stripped: prov = f"At intake the host's own additions were removed and nothing else: {stripped}." + tail
        else: prov = "Extracted unaltered: the item's own djvu.txt is reproduced whole after this header; nothing was stripped, normalized or corrected."
        if (s.get("left") or 0) >= 5: prov += f" About {s['left']:,} lines still carry the scanner's page mark where the OCR broke it over two lines or misread it; they were left in place."
        rights = f'Public Domain (pd-us-by-date: published {s["year"]}); {s["host_rights"]}'
        if s.get("stamps"): rights += "; " + s["stamps"]
        hdr = [
            f'Title: {s["title"]}',
            f'Creator: {s["creator"]}',
            f'Publisher: {s["publisher"]}',
            f'Publication Date: {s["year"]} ({s["year_basis"]})',
            f'Rights: {rights}',
            f'Language: {s["language"]}',
            f'Source: archive.org item {s["ia_id"]}, full text from the item\'s own djvu.txt. Fetched directly 2026-11-15 by the Library thread; the byte count of the downloaded file ({n:,}) equals the size archive.org lists for the djvu.txt.',
            f'Provenance note: {prov} Rights basis: published {s["year"]}, out of US copyright by date. OCR quality: {s["ocr"]} Line numbers cited in this header are this file\'s own line numbers.',
            f'Content note: {s["content"]}',
        ]
        for h in hdr: assert "\n" not in h
        out = ("\n".join(hdr) + "\n\n" + "_" * 70 + "\n\n").encode() + body
        stem = s["filename"][:-4]
        st = {"source_file": s["filename"], "assignments": s["rows"]}
        reg.append(f'- filename: {s["filename"]}\n  supplied_by: {q("Claude (Library thread, Church Family Tree wants, " + BATCH + ": located on archive.org, item metadata read, title page read, djvu.txt fetched directly, byte count equal to the host" + chr(39) + "s listed size, the volume" + chr(39) + "s end read)")}\n  date_added: \'2026-11-15\'\n  notes: {q(s["title"] + ". " + rights + ". Archive item " + s["ia_id"] + ". OCR quality: " + s["ocr"] + " CONTENTS: " + s["content"] + " WANT: " + s["want"])}\n')
        seed.append(f'  - title: {q(s["title"])}\n    author: {q(s["seed_author"])}\n    year: \'{s["year"]}\'\n    world: {s["seed_world"]}\n    why: {q(s["why"])}\n    url: https://archive.org/details/{s["ia_id"]}\n    rights_basis: {q(rights)}\n    verified_by: {q(f"Library thread, {BATCH}: archive.org metadata read, title page read, djvu.txt fetched, byte count {n:,} equal to the listed size, the volume" + chr(39) + "s end read")}\n    status: downloaded\n    vendored_as: {s["filename"]}\n')
        if not dry:
            p = f'{R}/cic/texts/{s["filename"]}'
            assert not os.path.exists(p), p
            open(p, "wb").write(out)
            yaml.safe_dump(st, open(f'{R}/cic/corpus-map/_staging/{stem}.yaml', "w"), sort_keys=False, allow_unicode=True, width=110)
        print("ok", s["filename"], n)
    if not dry:
        with open(f"{R}/cic/texts/REGISTRY.yaml", "a") as f: f.write("".join(reg))
        with open(f"{R}/Build/worlds/_cross-world/download-queue-seed.yaml", "a") as f: f.write("".join(seed))
if __name__ == "__main__": main()
