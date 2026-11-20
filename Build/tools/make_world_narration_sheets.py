"""Write one source sheet per narrated piece of a built world, for its narrator rewrite.

Usage (from the repo root): python3 Build/tools/make_world_narration_sheets.py <census-id> <outdir> <pieces.json>
"""
import json, re, sys, glob, os, yaml
world, outdir, pj = sys.argv[1:4]
root = os.getcwd()
P = [p for p in json.load(open(pj)) if p['world'] == world]
comp = json.load(open(f'{root}/cic-website/data/worlds/{world}.json'))
o = comp['orientation']

def load(rid):
    code = rid.split('.')[0]
    hits = glob.glob(f'{root}/records/{code}/*/{rid}.md')
    if not hits: return None, None
    raw = open(hits[0]).read()
    fm = yaml.safe_load(raw.split('\n---', 1)[0].lstrip('-\n')) if raw.startswith('---') else {}
    return fm, os.path.relpath(hits[0], root)

code = None
for s in o.get('documented_stories', []): code = s['story_id'].split('.')[0]; break
quotes = []
for f in glob.glob(f'{root}/records/{code}/quote/*.md'):
    fm, rel = load(os.path.basename(f)[:-3])
    if fm: quotes.append((fm, rel))
norm = lambda t: re.sub(r'\s+', ' ', (t or '')).replace('’', "'").replace('‘', "'").strip()

def conf(fm):
    c = fm.get('confidence') or {}
    return c.get('formation_confidence'), c.get('divergence_note')

os.makedirs(outdir, exist_ok=True)
for p in P:
    k = p['key']; L = [f'# Sheet: {world} / {k}', '', '## Original text (as narrated now)', '', p['text'], '']
    ids = []
    if k.startswith('docstory-'):
        sid = k[len('docstory-'):]
        st = next(s for s in o['documented_stories'] if s['story_id'] == sid)
        L += ['## Display fields (not narrated; for context)', '', f"- title: {st.get('title')}", f"- when: {st.get('when')}", f"- confidence: {st.get('confidence')}", '']
        ids = [sid]
        fm, _ = load(sid)
        if fm: ids += [r['target'] for r in fm.get('relations', []) or [] if r.get('target')]
    else:
        units = o.get(k, [])
        for u in units: ids += u.get('grounded_in', [])
    L += ['## Grounding records', '']
    seen = set()
    for rid in ids:
        if rid in seen: continue
        seen.add(rid); fm, rel = load(rid)
        if not fm: L.append(f'- {rid}: (record not found)'); continue
        fc, dn = conf(fm)
        L.append(f'### {rid} ({rel})'); L.append(f'- formation_confidence: {fc}')
        if dn: L.append(f'- divergence_note: {norm(dn)}')
        for fld in ('absent_detail', 'tellable_as'):
            if fm.get(fld): L.append(f'- {fld}: {norm(fm[fld])}')
        L.append('')
    L += ['## Quoted spans and their quote records', '']
    spans = re.findall(r'[“"]([^”"]{4,})[”"]', p['text'])
    if not spans: L.append('(none)')
    for sp in spans:
        L.append(f'- span: "{sp}"')
        found = [(fm, rel) for fm, rel in quotes if norm(sp).rstrip('.,') in norm(fm.get('modern_rendering')) or norm(sp).rstrip('.,') in norm(fm.get('text'))]
        if not found: L.append('  - NO QUOTE RECORD CONTAINS THIS SPAN')
        for fm, rel in found:
            L.append(f"  - record: {fm['id']} ({rel})")
            for s in fm.get('sources', []) or []: L.append(f"  - locus: {norm(s.get('locus'))}")
            L.append(f"  - source wording: {norm(fm.get('text'))}")
            L.append(f"  - modern_rendering: {norm(fm.get('modern_rendering'))}")
    open(f'{outdir}/{k}.sheet.md', 'w').write('\n'.join(L) + '\n')
    open(f'{outdir}/{k}.orig.txt', 'w').write(p['text'] + '\n')
print(len(P), 'sheets')
