"""Tests for corpus_structure._strip_tags_if_markup and its two callers
(outline(), and corpus_index.passage_units() which reuses it). Run:
python cic/engine/tests_corpus_structure.py

Same check()/results/sys.exit() convention as tests_corpus_map.py in this
same directory.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import corpus_structure as cs
import corpus_index as ci

TEXTS_DIR = cs.TEXTS_DIR


def check(label, ok):
    print(f"  {'OK ' if ok else '***'} {label}")
    return ok


results = []

# --- a real vendored .txt volume ------------------------------------------
salvian_path = TEXTS_DIR / "salvian_on-the-government-of-god_sanford1930.txt"
salvian_raw = salvian_path.read_text(encoding="utf-8", errors="replace")

results.append(check("Salvian has no <div1-3> markers (exercises the fallback branch)",
                     not list(cs._DIV.finditer(salvian_raw))))

salvian_stripped = cs._strip_tags_if_markup(salvian_path, salvian_raw)
results.append(check("a .txt file is returned byte-identical, not tag-stripped",
                     salvian_stripped == salvian_raw))

lost_span_1 = salvian_raw[84411:139805]
lost_span_2 = salvian_raw[144235:317304]
results.append(check("a long span spanning several stray '<'/'>' characters survives verbatim",
                     len(lost_span_1) == 55394 and "How then can God be said to neglect" in lost_span_1))
results.append(check("a second such span survives verbatim",
                     len(lost_span_2) == 173069 and "divine wrath is the punishment of the sinner" in lost_span_2))

salvian_units = ci.passage_units(salvian_path)
results.append(check("passage_units() carries the full untouched text through",
                     len(salvian_units) == 1 and salvian_units[0]["text"] == salvian_raw.strip()))

# --- a synthetic stray "<" in prose ----------------------------------------
generic_txt = Path("a-fake-plain-text-file.txt")
stray_bracket_prose = (
    "The philosopher wrote: our lives < our expectations, and yet we endure.\n\n"
    "A later paragraph, far from that stray mark, closes with a real greater-than: 2 > 1."
)
results.append(check("a stray '<' in plain prose deletes nothing, whatever the older '>' is",
                     cs._strip_tags_if_markup(generic_txt, stray_bracket_prose) == stray_bracket_prose))

# --- a real .xml volume with no <div1-3> markers, still real markup -------
webbe_path = TEXTS_DIR / "webbe_world-english-bible-british-edition.xml"
if webbe_path.exists():
    webbe_raw = webbe_path.read_text(encoding="utf-8", errors="replace")
    results.append(check("webbe has no <div1-3> markers either (same fallback branch as Salvian)",
                         not list(cs._DIV.finditer(webbe_raw))))
    webbe_stripped = cs._strip_tags_if_markup(webbe_path, webbe_raw)
    results.append(check("a real .xml file with no <div1-3> markers still gets its tags stripped",
                         "<p sfm=" not in webbe_stripped and "<v id=" not in webbe_stripped
                         and len(webbe_stripped) < len(webbe_raw)))
else:
    print("  (skipped: webbe volume not present in this checkout)")

# --- a synthetic .xml case, independent of the vendored corpus -----------
generic_xml_prose = Path("a-fake-markup-file.xml")
tagged = '<p sfm="ip">Some real prose <i>with emphasis</i> inside a real tag.</p>'
results.append(check("a .xml file's real tags are still stripped",
                     "<p" not in cs._strip_tags_if_markup(generic_xml_prose, tagged)
                     and "<i>" not in cs._strip_tags_if_markup(generic_xml_prose, tagged)))

# --- fleet-wide: every .txt file loses 0 characters to tag-stripping ------
lossy = []
for p in cs.volumes():
    if p.suffix != ".txt":
        continue
    raw = p.read_text(encoding="utf-8", errors="replace")
    if list(cs._DIV.finditer(raw)):
        continue  # a real div-marked .txt (if any) never reaches this branch
    stripped = cs._strip_tags_if_markup(p, raw)
    if len(stripped) != len(raw):
        lossy.append((p.name, len(raw) - len(stripped)))
results.append(check(f"fleet-wide: 0 .txt files lose any characters to tag-stripping ({len(lossy)} found)",
                     not lossy))
for name, lost in lossy:
    print(f"       still lossy: {name}: {lost} chars")

print("\nall passed" if all(results) else "\nFAILURES")
sys.exit(0 if all(results) else 1)
