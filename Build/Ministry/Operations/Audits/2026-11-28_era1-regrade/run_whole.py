"""Grade the six regraded briefs on the whole text with ../2026-11-28_era1-new-grades/grade_whole.py.

grade_whole.py and its committed weights are used as they stand: this script imports it and calls
its own score(). The held findings and the listener read are this folder's, read through that
folder's grade.py with its folder pointed here. Run from the repository root, after
scans/merge.py --finish:
python Build/Ministry/Operations/Audits/2026-11-28_era1-regrade/run_whole.py
Writes Grades_Whole.csv and Grades_Whole.json in this folder.
"""
import csv
import importlib.util
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
METHOD = os.path.join(HERE, '..', '2026-11-28_era1-new-grades')


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    gw = load('grade_whole', os.path.join(METHOD, 'grade_whole.py'))
    g = load('grade28', os.path.join(METHOD, 'grade.py'))
    g.HERE = HERE
    tset = json.load(open(os.path.join(HERE, 'Set.json'), encoding='utf-8'))
    rows = gw.score(g, HERE, os.path.join(HERE, 'Set.json'), os.path.join(HERE, 'trust', 'Trust_Results.json'))
    before = {e['id']: e['before'] for e in tset}
    left = json.load(open(os.path.join(HERE, 'Left_By_Source.json'), encoding='utf-8'))
    read = json.load(open(os.path.join(HERE, 'Readability_Names_Out.json'), encoding='utf-8'))
    for x in rows:
        b = before[x['id']]
        x['before'] = b if b == 'new' else b['overall']
        x['strict_rigor'] = gw.strict(x)
        x['readability'] = read[x['id']]
        for f in x['findings']:
            f['left_by_source'] = f['kind'] == 'bare' and any(q in f['quote'] or f['quote'] in q for q in left.get(x['id'], []))
    rows.sort(key=lambda x: (gw.POINTS[x['overall']], -(x['rigor_load'] + x['craft_load']), x['id']))
    json.dump(rows, open(os.path.join(HERE, 'Grades_Whole.json'), 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
    cols = ['id', 'name', 'words', 'rigor', 'rigor_load', 'craft', 'craft_load', 'overall', 'action', 'before', 'strict_rigor']
    with open(os.path.join(HERE, 'Grades_Whole.csv'), 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction='ignore')
        w.writeheader()
        w.writerows(rows)
    for x in rows:
        print(x['overall'], x['rigor'], x['craft'], x['before'], x['id'], len(x['findings']))


if __name__ == '__main__':
    main()
