"""Score this one brief with the 2026-11-28 whole-text method, unchanged.

grade.py and grade_whole.py are copied from ../../../2026-11-28_era1-new-grades/ (their HERE is
this folder). This runner calls grade_whole.score() on this folder's Set.json, scans and listener,
and skips main(), which needs that folder's calibration files. Run from the repository root.
"""
import importlib.util, json, os
HERE = os.path.dirname(os.path.abspath(__file__))

def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

g = load('grade_here', os.path.join(HERE, 'grade.py'))
gw = load('grade_whole_here', os.path.join(HERE, 'grade_whole.py'))
rows = gw.score(g, HERE, os.path.join(HERE, 'Set.json'), os.path.join(HERE, 'trust', 'Trust_Results.json'))
json.dump(rows, open(os.path.join(HERE, 'Grade_Whole.json'), 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
for r in rows:
    print(r['id'], 'rigor', r['rigor'], r['rigor_load'], 'craft', r['craft'], r['craft_load'], 'overall', r['overall'], '-', r['action'])
    for f in r['findings']:
        print(' ', f['dim'], f['kind'], f['band'], f['size'], '|', f['quote'])
