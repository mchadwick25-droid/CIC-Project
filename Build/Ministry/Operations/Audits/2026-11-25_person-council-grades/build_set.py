"""Build the set of person and council stories, and the packets the readers read.

Run from the repository root:
python Build/Ministry/Operations/Audits/2026-11-25_person-council-grades/build_set.py
Reads only; writes Set.json and packets/ in this folder.
"""
import glob
import json
import os
import re
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..', '..'))
CENSUS = os.path.join(ROOT, 'cic-website', 'data', 'world-census.json')
LEDGER = os.path.join(ROOT, 'Build', 'Ministry', 'Features', 'Church-Family-Tree', 'Story-Ledger.md')
RANK = os.path.join(HERE, '..', '2026-11-23_what-and-why-rank')
SCAN_COMMIT = '80acd0ae'  # main just before the 11-23 readings were committed
REFERENCES = {'basil-of-caesarea', 'epiphanius-of-salamis', 'john-chrysostom'}
TOUR = {'josephus'}  # the one person the Getting started tour opens (cft-website/index.html, TOURS)
FLOOR = {'person': 300, 'council': 260}  # two minutes at each kind kit's pace (450 and 390 words to three minutes)
LISTEN_PACKET = 23
SCAN_PACKET = 24


def ledger_batches():
    out = {}
    for m in re.finditer(r'\(`([^`]+)`\) \| (person|council) \| (\d+) \|', open(LEDGER, encoding='utf-8').read()):
        out[m.group(1)] = m.group(3)
    return out


def read_keys(pattern):
    keys = set()
    for f in glob.glob(os.path.join(RANK, 'readings', pattern)):
        keys |= set(re.findall(r'^## (\S+)', open(f, encoding='utf-8').read(), re.M))
    return keys


def main():
    census = json.load(open(CENSUS, encoding='utf-8'))
    movements = {m['id']: m for m in census['movements']}
    old = json.loads(subprocess.run(['git', 'show', SCAN_COMMIT + ':cic-website/data/world-census.json'],
                                    cwd=ROOT, capture_output=True, text=True, check=True).stdout)
    old = {m['id']: m.get('longDescription') for m in old['movements']}
    batches = ledger_batches()
    bare = read_keys('A-*.md') | read_keys('B-*.md')
    modern = read_keys('M-*.md')
    rows = []
    for m in census['movements']:
        kind = {'person': 'person', 'major-council': 'council'}.get(m.get('kind'))
        if not kind or not m.get('longDescription'):
            continue
        key = 'tree/' + m['id']
        text = m['longDescription']
        home = movements.get(m.get('toldWithin') or '', {})
        reused = key in bare and key in modern and old.get(m['id']) == text
        rows.append({
            'id': m['id'], 'name': m['name'], 'kind': kind, 'era': m['era'],
            'batch': batches.get(m['id'], 'before the kit'),
            'reference': m['id'] in REFERENCES,
            'words': len(text.split()), 'floor': FLOOR[kind],
            'scan': '11-23 rank' if reused else 'this audit',
            'changed_since_scan': key in bare and old.get(m['id']) != text,
            'tour': m['id'] in TOUR,
            'major': kind == 'council' or bool(m.get('major')),
            'home': m.get('toldWithin') or '',
            'home_built': home.get('status') == 'Built & Live',
            'home_living': bool(home.get('living')),
        })
    rows.sort(key=lambda r: (r['era'], r['id']))
    json.dump(rows, open(os.path.join(HERE, 'Set.json'), 'w', encoding='utf-8'), indent=1, ensure_ascii=False)

    def write(name, title, items, prefix):
        with open(os.path.join(HERE, 'packets', name + '.md'), 'w', encoding='utf-8') as f:
            f.write(f'# Packet {name}: {title}\n')
            for r in items:
                f.write(f"\n## {prefix}{r['id']}\n\n{movements[r['id']]['name']}\n\n{movements[r['id']]['longDescription'].strip()}\n")

    for i in range(0, len(rows), LISTEN_PACKET):
        write(f'L{i // LISTEN_PACKET + 1:02d}', 'person and council stories (census longDescription)', rows[i:i + LISTEN_PACKET], '')
    scan = [r for r in rows if r['scan'] == 'this audit']
    for i in range(0, len(scan), SCAN_PACKET):
        write(f'S{i // SCAN_PACKET + 1:02d}', 'person and council stories (census longDescription)', scan[i:i + SCAN_PACKET], 'tree/')
    from collections import Counter
    print(len(rows), Counter(r['kind'] for r in rows), Counter(r['scan'] for r in rows))
    print('batches', Counter(r['batch'] for r in rows))


if __name__ == '__main__':
    main()
