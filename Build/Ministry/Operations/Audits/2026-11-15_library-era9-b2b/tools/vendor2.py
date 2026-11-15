#!/usr/bin/env python3
"""vendor2.py <spec.json> [--dry] : copy staged files into cic/texts, write staging yaml, REGISTRY entries, seed rows."""
import json, sys, os, yaml, shutil
R = "/home/user/CIC-Project"; S = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BATCH = "era 9 batch 2b"
def q(s): return "'" + s.replace("'", "''") + "'"
spec = json.load(open(sys.argv[1])); dry = "--dry" in sys.argv
reg = []; seed = []
for s in spec:
    assert "PENDING" not in s["content"] and "UNSET" not in s["rights"] + str(s["rows"]), s["filename"]
    stem = s["filename"][:-4]; n = s["bytes0"]
    st = {"source_file": s["filename"]}
    if s.get("authors_ruled"): st["authors_ruled"] = s["authors_ruled"]
    st["assignments"] = s["rows"]
    reg.append(f'- filename: {s["filename"]}\n  supplied_by: {q("Claude (Library thread, Church Family Tree wants, " + BATCH + ": located on archive.org, item metadata read, title page read, djvu.txt fetched directly, byte count equal to the host" + chr(39) + "s listed size, the volume" + chr(39) + "s end read)")}\n  date_added: \'2026-11-15\'\n  notes: {q(s["title"] + ". " + s["rights"] + ". Archive item " + s["ia_id"] + ". OCR quality: " + s["ocr"] + " CONTENTS: " + s["content"] + " WANT: " + s["want"])}\n')
    seed.append(f'  - title: {q(s["title"])}\n    author: {q(s["creator"])}\n    year: \'{s["year"]}\'\n    world: {s["seed_world"]}\n    why: {q(s["why"])}\n    url: https://archive.org/details/{s["ia_id"]}\n    rights_basis: {q(s["rights"])}\n    verified_by: {q(f"Library thread, {BATCH}: archive.org metadata read, title page read, djvu.txt fetched, byte count {n:,} equal to the listed size, the volume" + chr(39) + "s end read")}\n    status: downloaded\n    vendored_as: {s["filename"]}\n')
    if not dry:
        p = f'{R}/cic/texts/{s["filename"]}'; assert not os.path.exists(p), p
        shutil.copyfile(f'{S}/stage/{s["filename"]}', p)
        yaml.safe_dump(st, open(f'{R}/cic/corpus-map/_staging/{stem}.yaml', "w"), sort_keys=False, allow_unicode=True, width=110)
    print("ok", s["filename"])
if not dry:
    with open(f"{R}/cic/texts/REGISTRY.yaml", "a") as f: f.write("".join(reg))
    with open(f"{R}/Build/worlds/_cross-world/download-queue-seed.yaml", "a") as f: f.write("".join(seed))
