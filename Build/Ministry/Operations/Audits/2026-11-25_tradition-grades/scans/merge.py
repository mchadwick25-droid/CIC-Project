"""Match the two bare-statement reads and list what the third read must decide.

Run from the repository root. Writes Third_Read_Packet.md and Merge.json; with --finish,
after the third read, also writes Held_Findings.json.
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

A = parse(os.path.join(HERE, 'bare_A.md'))
B = parse(os.path.join(HERE, 'bare_B.md'))
M = parse(os.path.join(HERE, 'modern_M.md'))
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
packet = os.path.join(HERE, '..', 'packets', 'S01.md')
with open(os.path.join(HERE, 'Third_Read_Packet.md'), 'w', encoding='utf-8') as f:
    f.write('# Third read packet\n\nThe pieces are in `Build/Ministry/Operations/Audits/2026-11-25_tradition-grades/packets/S01.md`. Read each piece whole before ruling on its findings.\n\n')
    for t in third:
        fx = t['f']
        extra = f"missing: {fx.get('missing')}" if t['test'] == 'bare statement' else f"kind: {fx.get('kind')} | who: {fx.get('who')}"
        f.write(f"## {t['id']}\nPiece: {t['key']}\nHeart: {A[t['key']]['heart']}\nTest: {t['test']}\nFinding: \"{fx['quote']}\" | {extra} | weights given: {t['weights']}\n\n")
print(sum(len(v) for v in held.values()), 'agreed;', len(third), 'to third read', sum(t['test']=='modern opinion' for t in third), 'modern')


def finish():
    """Fold the third read's rulings into Held_Findings.json (run with --finish)."""
    data = json.load(open(os.path.join(HERE, 'Merge.json'), encoding='utf-8'))
    text = open(os.path.join(HERE, 'third_read.md'), encoding='utf-8').read()
    rulings = {}
    for block in re.split(r'^## ', text, flags=re.M)[1:]:
        fid = block.split('\n', 1)[0].strip()
        r = re.search(r'^Ruling:\s*(.*)$', block, re.M).group(1).strip().lower()
        w = re.search(r'^Weight:\s*(\d)', block, re.M)
        rulings[fid] = (r.startswith('holds'), int(w.group(1)) if w else None)
    held = data['held']
    for t in data['third']:
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
