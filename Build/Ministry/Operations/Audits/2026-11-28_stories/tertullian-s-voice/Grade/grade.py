"""Grade the 15 new era 1 person briefs from the scans and the listener read.

The rules are ../2026-11-25_person-council-grades/grade.py, unchanged. Every brief is scanned
here (none reuses the 11-23 rank, whose readings were of older text), and each row carries its
old grade from ../2026-11-25_person-council-grades/Grades.csv. Run from the repository root:
python Build/Ministry/Operations/Audits/2026-11-28_era1-new-grades/grade.py
Reads only; writes Grades.csv, Grades.json and Rebuild_Order.csv in this folder.
"""
import csv
import glob
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
OLD = os.path.join(HERE, '..', '2026-11-25_person-council-grades', 'Grades.csv')
ORDER = 'FDCBA'
ACTION = {'F': 'must be redone', 'D': 'should be redone', 'C': 'would benefit',
          'B': 'OK to keep', 'A': 'great as is'}


def lower(a, b):
    return a if ORDER.index(a) < ORDER.index(b) else b


def rigor(items):
    bare = [i for i in items if i['test'] == 'bare statement']
    modern = [i for i in items if i['test'] == 'modern opinion']
    guess = [i for i in modern if i.get('kind') == 'guess']
    crucial_modern = [i for i in modern if i['weight'] == 3]
    crucial_bare = [i for i in bare if i['weight'] == 3]
    supporting_bare = [i for i in bare if i['weight'] == 2]
    counts = f"{len(bare)} bare (3:{len(crucial_bare)} 2:{len(supporting_bare)}), {len(modern)} modern ({len(guess)} guess)"
    if guess:
        return 'F', f"modern guess told as the record: \"{guess[0]['quote']}\"", counts
    if len(modern) >= 3:
        return 'F', f"{len(modern)} modern-opinion findings", counts
    if crucial_modern:
        return 'F', f"Crucial modern finding: \"{crucial_modern[0]['quote']}\"", counts
    if crucial_bare:
        return 'D', f"Crucial bare statement: \"{crucial_bare[0]['quote']}\"", counts
    if len(modern) == 2:
        return 'D', '2 modern-opinion findings', counts
    if len(modern) == 1:
        return 'C', f"1 modern finding: \"{modern[0]['quote']}\"", counts
    if supporting_bare:
        return 'C', f"{len(supporting_bare)} Supporting bare statement(s): \"{supporting_bare[0]['quote']}\"", counts
    if bare:
        return 'B', f"only Passing findings ({len(bare)})", counts
    return 'B', 'no fault found by the scans', counts


def parse_listener():
    out = {}
    for f in sorted(glob.glob(os.path.join(HERE, 'listener', 'L*.md'))):
        text = open(f, encoding='utf-8').read()
        for block in re.split(r'^## ', text, flags=re.M)[1:]:
            pid = block.split('\n', 1)[0].strip()

            def num(label):
                m = re.search(r'^' + label + r':\s*(\d+)', block, re.M)
                return int(m.group(1)) if m else None

            opening = re.search(r'^Opening:\s*(.*?)\|\s*(\d)', block, re.M)
            drift = re.search(r'^Drift:\s*(.*)$', block, re.M)
            form = re.search(r'^Form:\s*(\w+)\s*\|?\s*(.*)$', block, re.M)
            listen = re.search(r'^Listen to end:\s*(\w+)', block, re.M)
            out[pid] = {
                'file': os.path.basename(f),
                'unfilled': num('Unfilled test lines'),
                'opening': int(opening.group(2)) if opening else None,
                'opening_note': opening.group(1).strip() if opening else '',
                'bare': num('Bare statements'),
                'tells': num('AI tells'),
                'thread': num('Thread-losing sentences'),
                'blocking': num('Blocking total'),
                'drift': drift.group(1).strip() if drift else '',
                'listen': (listen.group(1).lower() == 'yes') if listen else None,
                'form': form.group(1).lower() if form else '',
                'form_note': form.group(2).strip() if form else '',
            }
    return out


def craft(r, words, floor):
    parts = [r['unfilled'], r['opening'], r['bare'], r['tells'], r['thread']]
    blocking = sum(p or 0 for p in parts)
    leave = r['listen'] is False
    summary = r['form'] == 'summary'
    if leave and (blocking >= 8 or summary):
        g = 'F'
    elif leave or blocking >= 8:
        g = 'D'
    elif blocking >= 4:
        g = 'C'
    elif blocking >= 1:
        g = 'B'
    else:
        g = 'A'
    if summary:
        g = lower(g, 'F' if words < floor else 'D')
    why = []
    if summary:
        why.append(f"summary, {words} words" + (f' (under the ~{floor}-word floor)' if words < floor else ''))
    if leave:
        why.append('listener would leave')
    why.append(f"{blocking} blocking")
    counts = (f"{blocking} blocking: {r['unfilled']} test lines, {r['opening']} opening, "
              f"{r['bare']} bare, {r['tells']} tells, {r['thread']} thread")
    return g, '; '.join(why), counts, blocking


REACH = [('tour', 'first-visit tour'), ('major', 'major'), ('home_built', 'home in a built world'),
         ('home_living', 'living home')]


def reach(e):
    return sum(1 for k, _ in REACH if e[k])


def reach_basis(e):
    return ', '.join(label for k, label in REACH if e[k])


def reach_key(x):
    # Mark's order: the first-visit tour, then major, then a home in a built world, then a living home.
    return tuple(0 if label in x['reach_basis'].split(', ') else 1 for _, label in REACH)


def scan_items():
    """The held findings of this audit's own scans.

    A guess whose hedge is only on a date counts as an ordinary modern finding (Mark, 2026-11-26);
    Hedged_Dates.json lists them.
    """
    items = {}
    own = os.path.join(HERE, 'scans', 'Held_Findings.json')
    if os.path.exists(own):
        for key, its in json.load(open(own, encoding='utf-8')).items():
            items[key] = its
    hd = os.path.join(HERE, 'Hedged_Dates.json')
    if os.path.exists(hd):
        for d in json.load(open(hd, encoding='utf-8')):
            for i in items.get('tree/' + d['id'], []):
                if i.get('kind') == 'guess' and i['quote'] == d['quote']:
                    i['kind'] = 'hedged date'
    return items


def main():
    tset = json.load(open(os.path.join(HERE, 'Set.json'), encoding='utf-8'))
    own_keys = set()
    own = os.path.join(HERE, 'scans', 'Held_Findings.json')
    if os.path.exists(own):
        own_keys = set(json.load(open(own, encoding='utf-8')))
    trust = {}
    tp = os.path.join(HERE, 'trust', 'Trust_Results.json')
    if os.path.exists(tp):
        trust = json.load(open(tp, encoding='utf-8'))
    items = scan_items()
    listen = parse_listener()
    old = {r['id']: r for r in csv.DictReader(open(OLD, encoding='utf-8'))}
    rows = []
    for e in tset:
        key = 'tree/' + e['id']
        rg, rwhy, rcounts = rigor(items.get(key, []))
        scan = e['scan']
        if scan == 'this audit' and key not in own_keys:
            raise SystemExit('no scan of this audit for ' + key)
        r = listen.get(e['id'])
        if r is None:
            raise SystemExit('no listener read for ' + e['id'])
        cg, cwhy, ccounts, blocking = craft(r, e['words'], e['floor'])
        if e['id'] in trust:
            t = trust[e['id']]
            if t['all_hold']:
                rg, rwhy = 'A', 'trust read: every sentence held or a fair summary'
            elif t.get('ruled'):
                rg = t['ruled']
                rwhy += f"; trust read found {t['not_holding']} sentence(s) that do not hold; {t['ruling']}"
            else:
                rg = 'F'
                rwhy += f"; trust read found {t['not_holding']} sentence(s) that do not hold (failed trust read is F, Mark 2026-11-25)"
        overall = lower(rg, cg)
        reason = f"rigor {rg}: {rwhy}; craft {cg}: {cwhy}"
        rows.append({
            'id': e['id'], 'name': e['name'], 'kind': e['kind'], 'era': e['era'], 'batch': e['batch'],
            'reference': 'yes' if e['reference'] else '', 'words': e['words'],
            'rigor': rg, 'rigor_basis': f"{rwhy} [{rcounts}; scan: {scan}]",
            'craft': cg, 'craft_counts': ccounts,
            'listen_to_end': 'yes' if r['listen'] else 'no', 'form': r['form'],
            'drift': r['drift'], 'overall': overall, 'action': ACTION[overall],
            'reason': reason, 'blocking': blocking,
            'reach': reach(e), 'reach_basis': reach_basis(e),
            'old_overall': old[e['id']]['overall'], 'old_rigor': old[e['id']]['rigor'], 'old_craft': old[e['id']]['craft'],
        })
    rows.sort(key=lambda x: (ORDER.index(x['overall']), -x['blocking'], x['id']))
    cols = ['id', 'name', 'old_overall', 'old_rigor', 'old_craft', 'kind', 'era', 'batch', 'reference', 'words', 'rigor', 'rigor_basis', 'craft', 'craft_counts', 'listen_to_end',
            'form', 'drift', 'overall', 'action']
    with open(os.path.join(HERE, 'Grades.csv'), 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction='ignore')
        w.writeheader()
        w.writerows(rows)
    json.dump(rows, open(os.path.join(HERE, 'Grades.json'), 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
    order = sorted(rows, key=lambda x: (ORDER.index(x['overall']), reach_key(x), -x['blocking'], x['id']))
    with open(os.path.join(HERE, 'Rebuild_Order.csv'), 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(['rank', 'id', 'name', 'kind', 'era', 'batch', 'reference', 'overall', 'action',
                    'rigor', 'craft', 'reach', 'reach_basis'])
        for i, x in enumerate(order, 1):
            w.writerow([i, x['id'], x['name'], x['kind'], x['era'], x['batch'], x['reference'], x['overall'],
                        x['action'], x['rigor'], x['craft'], x['reach'], x['reach_basis']])
    from collections import Counter
    print('overall', Counter(r['overall'] for r in rows))
    print('rigor', Counter(r['rigor'] for r in rows))
    print('craft', Counter(r['craft'] for r in rows))


if __name__ == '__main__':
    main()
