"""Reading level of each regraded brief with names out, and with names, from engine.m1.profile_readability.

Names out is the profile tool's own figure: it drops every word the tool finds as a proper name
(people, places, works) from the syllable count. The with-names reading ease uses every word.
Run from the repository root; writes Readability_Names_Out.json in this folder.
"""
import json
import os
import sys

sys.path.insert(0, os.getcwd())
import engine.m1.profile_readability as p  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
out = {}
for k, txt in json.load(open(os.path.join(HERE, 'Texts.json'), encoding='utf-8')).items():
    s = p.grade_profile_text(txt)
    words = [raw for raw, _, _ in p._forms(p.normalize(txt))]
    spw = sum(p._count_syllables(w) for w in words) / len(words)
    fre = 206.835 - 1.015 * s.words_per_sentence - 84.6 * spw
    out[k] = {'words': s.words, 'grade_names_out': round(s.fk_names_out, 1), 'grade_with_names': round(s.fk, 1),
              'ease_names_out': round(s.fre_names_out, 1), 'ease_with_names': round(fre, 1),
              'passes_names_out': s.fk_names_out <= 10 and s.fre_names_out >= 60}
json.dump(out, open(os.path.join(HERE, 'Readability_Names_Out.json'), 'w', encoding='utf-8'), indent=1)
print(sum(v['passes_names_out'] for v in out.values()), 'of', len(out), 'pass names out')
