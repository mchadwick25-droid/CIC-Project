"""Match the two bare-statement reads and list what the third read must decide.

Copied from ../../2026-11-28_era1-new-grades/scans/merge.py, with this folder's packets.
Run from the repository root. Reads S<nn>_bare_A.md, S<nn>_bare_B.md and S<nn>_modern.md for
each scan packet; writes Third_Read_Packet.md and Merge.json; with --finish, after the third read
(third_read_*.md), also writes Held_Findings.json.
"""
import json, os, re
HERE = os.path.dirname(os.path.abspath(__file__))

def parse(path, modern=False):
    out = {}
    for block in re.split(r'^## ', open(path, encoding='utf-8').read(), flags=re.M)[1:]:
        key = block.split('\n', 1)[0].strip()
        heart = re.search(r'^Heart:\s*(.*)$', block, re.M)
        items = []
        for m in re.finditer(r'^- "(.*)"\s*\|(.*)$', block, re.M):
            f = {'quote': m.group(1)}
            for part in m.group(2).split('|'):
                if ':' in part:
                    k, v = part.split(':', 1)
                    f[k.strip()] = v.strip()
            f['weight'] = int(re.sub(r'\D', '', f.get('weight', '1')) or 1)
            items.append(f)
        out[key] = {'heart': heart.group(1).strip() if heart else '', 'items': items}
    return out

def norm(s):
    return re.sub(r'[^a-z0-9 ]', '', s.lower()).split()

def same(a, b):
    x, y = norm(a), norm(b)
    if not x or not y:
        return False
    sx, sy = set(x), set(y)
    return len(sx & sy) / min(len(sx), len(sy)) >= 0.6

import glob
A, B, M, SOURCE = {}, {}, {}, {}
for p in sorted(glob.glob(os.path.join(HERE, '..', 'packets', 'S*.md'))):
    s = os.path.basename(p)[:-3]
    a = parse(os.path.join(HERE, s + '_bare_A.md'))
    SOURCE.update({k: s for k in a})
    A.update(a)
    B.update(parse(os.path.join(HERE, s + '_bare_B.md')))
    M.update(parse(os.path.join(HERE, s + '_modern.md')))
for need in (B, M):
    missing = set(A) ^ set(need)
    if missing:
        raise SystemExit('reads do not cover the same pieces: ' + ', '.join(sorted(missing)))
held, third = {}, []
n = 0
for key in A:
    held[key] = []
    used = set()
    for fa in A[key]['items']:
        match = None
        for j, fb in enumerate(B.get(key, {'items': []})['items']):
            if j not in used and same(fa['quote'], fb['quote']):
                match = j
                break
        if match is not None:
            used.add(match)
            fb = B[key]['items'][match]
            if abs(fa['weight'] - fb['weight']) >= 2:
                n += 1
                third.append({'id': f'S{n:03d}', 'key': key, 'test': 'bare statement', 'f': fa, 'weights': [fa['weight'], fb['weight']]})
            else:
                held[key].append({'quote': fa['quote'], 'missing': fa.get('missing'), 'weight': max(fa['weight'], fb['weight']),
                                  'weights': [fa['weight'], fb['weight']], 'asks': fa.get('asks'), 'test': 'bare statement', 'decided_by': 'both readers'})
        else:
            n += 1
            third.append({'id': f'S{n:03d}', 'key': key, 'test': 'bare statement', 'f': fa, 'weights': [fa['weight']]})
    for j, fb in enumerate(B.get(key, {'items': []})['items']):
        if j not in used:
            n += 1
            third.append({'id': f'S{n:03d}', 'key': key, 'test': 'bare statement', 'f': fb, 'weights': [fb['weight']]})
    for fm in M.get(key, {'items': []})['items']:
        n += 1
        third.append({'id': f'S{n:03d}', 'key': key, 'test': 'modern opinion', 'f': fm, 'weights': [fm['weight']]})
json.dump({'held': held, 'third': third, 'hearts': {k: A[k]['heart'] for k in A}}, open(os.path.join(HERE, 'Merge.json'), 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
for s in sorted(set(SOURCE.values())):
    with open(os.path.join(HERE, f'Third_Read_Packet_{s}.md'), 'w', encoding='utf-8') as f:
        f.write(f'# Third read packet {s}\n\nThe pieces are in `Build/Ministry/Operations/Audits/2026-11-28_era1-regrade/packets/{s}.md`. Read each piece whole before ruling on its findings.\n\n')
        for t in third:
            if SOURCE[t['key']] != s:
                continue
            fx = t['f']
            extra = f"missing: {fx.get('missing')}" if t['test'] == 'bare statement' else f"kind: {fx.get('kind')} | who: {fx.get('who')}"
            f.write(f"## {t['id']}\nPiece: {t['key']}\nHeart: {A[t['key']]['heart']}\nTest: {t['test']}\nFinding: \"{fx['quote']}\" | {extra} | weights given: {t['weights']}\n\n")
print(sum(len(v) for v in held.values()), 'agreed;', len(third), 'to third read', sum(t['test']=='modern opinion' for t in third), 'modern')


def finish():
    """Fold the third read's rulings into Held_Findings.json (run with --finish)."""
    data = json.load(open(os.path.join(HERE, 'Merge.json'), encoding='utf-8'))
    text = ''.join(open(f, encoding='utf-8').read() for f in sorted(glob.glob(os.path.join(HERE, 'third_read_*.md'))))
    rulings = {}
    for block in re.split(r'^## ', text, flags=re.M)[1:]:
        fid = block.split('\n', 1)[0].strip()
        r = re.search(r'^Ruling:\s*(.*)$', block, re.M).group(1).strip().lower()
        w = re.search(r'^Weight:\s*(\d)', block, re.M)
        rulings[fid] = (r.startswith('holds'), int(w.group(1)) if w else None)
    held = data['held']
    for t in data['third']:
        if t['id'] not in rulings:
            raise SystemExit('no third-read ruling for ' + t['id'])
        ok, w = rulings[t['id']]
        if not ok:
            continue
        f = dict(t['f'])
        f.update({'weight': w, 'test': t['test'], 'decided_by': 'Opus third read', 'id': t['id']})
        held[t['key']].append(f)
    json.dump(held, open(os.path.join(HERE, 'Held_Findings.json'), 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
    print(sum(len(v) for v in held.values()), 'held;', sum(1 for v in rulings.values() if v[0]), 'of', len(rulings), 'third-read findings hold')


if __name__ == '__main__':
    import sys
    if '--finish' in sys.argv:
        finish()
