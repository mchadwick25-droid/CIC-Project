import json, html, os, sys
R = '/home/user/CIC-Project'
F = R + '/Build/Ministry/Operations/Audits/2026-11-26_era1-cards'
OUT = sys.argv[1]
cen = json.load(open(R + '/cic-website/data/world-census.json'))
M = {m['id']: m for m in cen['movements']}
edges = cen['edges']
ev = json.load(open(F + '/Evidence.json'))
esc = lambda s: html.escape(str(s)) if s is not None else ''

CARDS = [
  ('montanism-the-new-prophecy', 'Tradition', 'entry'),
  ('alexandria-catechetical', 'Built world', 'entry'),
  ('polycarp-of-smyrna', 'Person', 'card'),
  ('councils-of-rome-and-carthage-251', 'Council', 'council'),
  ('era-1', 'Era', 'era'),
  ('the-sister-who-saw-visions-during-the-service', 'Story', 'new'),
  ('post-apostolic-house-church--montanism-the-new-prophecy', 'Connection', 'new'),
  ('river-africa', 'River', 'new'),
]
OWN = {'Person': 'Key works', 'Council': 'What happened', 'Story': 'Who tells it', 'Connection': 'What passed', 'River': 'How it began'}

def nm(i):
    m = M.get(i); return (m.get('shortName') or m['name']) if m else i

def lineage(i):
    up, down = [], []
    for e in edges:
        if e['type'] in ('gave rise to', 'continued as', 'broke with'):
            if e['to'] == i: up.append((e['type'], e['from']))
            if e['from'] == i: down.append((e['type'], e['to']))
    return up, down

def chips(items, more):
    s = ''.join(f'<span class="chip">{esc(t)}</span>' for t in items[:3])
    if len(items) > 3 or more: s += '<span class="chip more">and more</span>'
    return s

def fold(title, body, open_=False):
    return f'<details class="fold"{" open" if open_ else ""}><summary>{esc(title)}</summary><div class="fold-body">{body}</div></details>'

def none_held(s='Nothing held yet for this section.'):
    return f'<p class="none">{esc(s)}</p>'

def para_list(xs):
    if not xs: return none_held()
    out = []
    for x in xs:
        if isinstance(x, dict):
            x = x.get('text') or x.get('name') or json.dumps(x, ensure_ascii=False)
        out.append(f'<li>{esc(x)}</li>')
    return '<ul class="plain">' + ''.join(out) + '</ul>'

def timeline_html(tl):
    if not tl: return none_held()
    out = []
    for per in tl:
        lines = ''.join(f'<li><span class="when">{esc(l["when"])}</span> {esc(l["text"])} <span class="ref">{esc(l["reference"])}</span>' + (f'<span class="note">{esc(l["note"])}</span>' if l.get('note') else '') + '</li>' for l in per['lines'])
        w = f'<p class="witness">As {esc(per["witness"])} tells it</p>' if per.get('witness') else ''
        out.append(f'<details class="period"><summary><span class="when">{esc(per["when"])}</span> {esc(per["headline"])}</summary>{w}<ul class="tl">{lines}</ul></details>')
    return '<div class="periods">' + ''.join(out) + '</div>'

def sources_html(srcs, mw):
    s = ''
    if srcs:
        items = []
        for x in srcs:
            if isinstance(x, dict):
                t = x.get('work') or x.get('title') or ''
                if x.get('author') and x.get('title'): t = f'{x["author"]}, {x["title"]}'
                items.append(f'<li>{esc(t)}</li>')
            else: items.append(f'<li>{esc(x)}</li>')
        s += '<ul class="plain">' + ''.join(items) + '</ul>'
    else: s += none_held('No old sources recorded yet.')
    s += '<h5>Modern works</h5>'
    if mw: s += '<ul class="plain">' + ''.join(f'<li>{esc(w.get("author",""))}, <i>{esc(w.get("title",""))}</i>' + (f' — {esc(w["note"])}' if w.get('note') else '') + '</li>' for w in mw) + '</ul>'
    else: s += none_held('No modern works listed yet.')
    return s

def brief_html(text, srcs):
    if not text: return none_held('No brief.')
    ps = ''.join(f'<p>{esc(p)}</p>' for p in text.split('\n') if p.strip())
    sl = ''
    if srcs: sl = '<h5>From the old sources</h5><ul class="plain">' + ''.join(f'<li>{esc((s.get("author")+", ") if s.get("author") else "")}{esc(s.get("title"))}</li>' for s in srcs) + '</ul>'
    return f'<details class="brief"><summary>Read along</summary><div class="fold-body">{ps}</div></details>{sl}'

def card_html(cid, kind, home):
    L = json.load(open(f'{F}/{cid}.layout.json'))
    E = ev.get(cid, {})
    d = E.get('dates', {})
    if home == 'era':
        era = [e for e in cen['eras'] if e.get('num') == 1][0]
        title = era['title']; place = 'The whole tree'
    elif home == 'new':
        title = L['title']; place = L.get('place') or ''
    else:
        m = M[cid]; title = m['name']; place = m.get('placeLabel') or E.get('place') or ''
    shown = d.get('shown') or L.get('dates') or ''
    sd = L.get('shortDescription') or (L.get('card') or {}).get('shortDescription') or (L.get('council') or {}).get('shortDescription')
    tl = L.get('timeline') or (L.get('card') or {}).get('timeline') or (L.get('council') or {}).get('timeline')
    unc = L.get('uncertain') or (L.get('card') or {}).get('uncertain') or (L.get('council') or {}).get('uncertain')
    bs = L.get('briefSources') or (L.get('card') or {}).get('briefSources') or (L.get('council') or {}).get('briefSources')
    # direct line
    if home == 'entry':
        up, down = lineage(cid)
        dl = f'<div class="dl"><span class="dl-k">Grew from</span>{chips([nm(f) for t,f in up], False) or "<span class=chip none>none on the tree</span>"}</div><div class="dl"><span class="dl-k">Led to</span>{chips([nm(t2) for t,t2 in down], False) or "<span class=chip none>none on the tree</span>"}</div>'
    elif home == 'card':
        hm = M[cid].get('toldWithin'); dl = f'<div class="dl"><span class="dl-k">Told within</span><span class="chip">{esc(nm(hm))}</span></div>'
    elif home == 'council':
        cs = sorted([m for m in cen['movements'] if m.get('kind') == 'major-council'], key=lambda m: m['start'])
        i = [m['id'] for m in cs].index(cid)
        b = cs[i-1]['name'] if i > 0 else 'none before'; a = cs[i+1]['name'] if i+1 < len(cs) else 'none after'
        dl = f'<div class="dl"><span class="chip none">{esc(b)}</span><span class="arr">→</span><b>this council</b><span class="arr">→</span><span class="chip">{esc(a)}</span></div>'
    elif home == 'era':
        dl = '<div class="dl"><span class="chip none">none before</span><span class="arr">→</span><b>Era 1</b><span class="arr">→</span><span class="chip">Era 2</span></div>'
    else:
        x = L.get('directLine') or {}
        if kind == 'Story':
            dl = '<div class="dl"><span class="dl-k">Told under</span>' + chips([t['name'] for t in x.get('toldUnder', [])], False) + '</div><div class="dl"><span class="dl-k">Acts in it</span>' + chips([t.get('name', t.get('id')) for t in x.get('actsInIt', [])], False) + '</div>'
        elif kind == 'Connection':
            dl = f'<div class="dl"><span class="chip">{esc(x["from"]["name"])}</span><span class="arr">{esc(x.get("kind",""))} →</span><span class="chip">{esc(x["to"]["name"])}</span></div><div class="dl"><span class="dl-k">Confidence</span><span class="chip none">{esc(x.get("confidence") or x.get("confidenceInWords") or "")}</span></div>'
        else:
            p = x.get('parent') or {}
            kids = x.get('children') or []
            dl = f'<div class="dl"><span class="dl-k">Leaves</span><span class="chip">{esc(p.get("name"))}</span><span class="chip none">{esc(p.get("basis",""))}</span></div><div class="dl"><span class="dl-k">Rivers that leave it</span>' + (chips([k.get("name") for k in kids], False) if kids else '<span class="chip none">none in era 1</span>') + '</div>'
    player = '<div class="player"><span class="play">▶</span><span class="bar"></span><span class="t">Listen</span></div>'
    # brief
    if home == 'entry': brief = brief_html(M[cid].get('longDescription'), bs)
    elif home in ('card', 'council'): brief = brief_html(M[cid].get('longDescription'), bs)
    elif home == 'era': brief = none_held('The era brief is not yet written.'); player = ''
    elif kind == 'Story': brief = brief_html(L.get('text'), L.get('textSources'))
    elif kind == 'Connection': brief = f'<div class="note-text"><h5>The connection note</h5><p>{esc(L.get("text"))}</p></div>'; player = ''
    else: brief = none_held('A river has no brief.'); player = ''
    # menu
    menu = [fold('Timeline', timeline_html(tl))]
    if home in ('entry', 'card', 'council'):
        m = M[cid]
        ppl = [p.get('name') or nm(p.get('person')) for p in m.get('people', [])]
        if home == 'council': ppl = (m.get('council') or {}).get('attended') or ppl
        ds = [s.get('title') for s in m.get('documentedStories', []) or []]
        menu.append(fold('People and stories', (para_list(ppl) if ppl else none_held('No people listed yet.')) + ('<h5>Documented stories</h5>' + para_list(ds) if ds else '')))
        if home == 'card':
            kw = (m.get('card') or {}).get('keyWorks') or []
            menu.append(fold('Key works', para_list([f'{k.get("title")}: {k.get("about","")}' for k in kw]) if kw else none_held()))
        if home == 'council':
            c = m.get('council') or {}
            menu.append(fold('What happened', ''.join(f'<h5>{esc(k.capitalize())}</h5>{para_list(c[k] if isinstance(c[k], list) else [c[k]])}' for k in ('issue', 'calledBy', 'decided', 'outcome') if c.get(k))))
        cn = [f'{nm(e["from"])} {e["type"]} {nm(e["to"])}' for e in edges if cid in (e['from'], e['to'])]
        menu.append(fold('Connections', para_list(cn) if cn else none_held('No connections on the tree yet.')))
        lg = m.get('legacy') or (m.get('card') or {}).get('legacy')
        menu.append(fold('Legacy and today', para_list([lg] if isinstance(lg, str) else (lg or [])) + (para_list([x.get('text') if isinstance(x, dict) else x for x in m.get('experienceToday') or []]) if m.get('experienceToday') else '')))
    elif home == 'era':
        menu.append(fold('People and stories', none_held('The era card lists its traditions, people and councils from the map.')))
        menu.append(fold('Connections', none_held('The era card links to the eras before and after.')))
        menu.append(fold('Legacy and today', none_held()))
    else:
        ps = L.get('peopleAndStories')
        if isinstance(ps, dict):
            body = ''
            for k, v in ps.items():
                body += f'<h5>{esc(k.capitalize())}</h5>' + para_list([(f'{x.get("name")}: {x.get("as","")}' if isinstance(x, dict) and x.get('as') else (f'{x.get("name")} ({x.get("dates")})' if isinstance(x, dict) and x.get('dates') else x)) for x in (v if isinstance(v, list) else [v])])
        else: body = para_list(ps)
        menu.append(fold('People and stories', body))
        own = L.get('whoTellsIt') or L.get('whatPassed') or L.get('howItBegan')
        if isinstance(own, dict): own = [own.get('reason') or '', f'Basis: {own.get("basis","")}; confidence: {own.get("confidence","")}']
        menu.append(fold(OWN[kind], para_list(own if isinstance(own, list) else [own])))
        cn = [(f'{x.get("edge") or x.get("id")}: {x.get("as") or x.get("in") or x.get("type","")}') if isinstance(x, dict) else x for x in L.get('connections') or []]
        menu.append(fold('Connections', para_list(cn)))
        lg = L.get('legacyAndToday')
        if isinstance(lg, dict): lg = [lg.get('text')]
        menu.append(fold('Legacy and today', para_list(lg if isinstance(lg, list) else [lg]) if lg else none_held()))
    menu.append(fold('Open questions', para_list(unc)))
    if home in ('entry', 'card', 'council'):
        m = M[cid]; srcs = m.get('sources') or (m.get('card') or {}).get('sources') or (m.get('council') or {}).get('sources') or []
        menu.append(fold('Sources', sources_html(srcs, m.get('modernWorks'))))
    else:
        menu.append(fold('Sources', sources_html(L.get('sources'), L.get('modernWorks'))))
    phone = f'''<div class="phone"><div class="screen">
<p class="kind">{esc(kind)}</p><h3>{esc(title)}</h3><p class="dp">{esc(shown)}{" · " + esc(place) if place else ""}</p>
<p class="sd">{esc(sd)}</p>{dl}{player}{brief}<div class="menu">{''.join(menu)}</div></div></div>'''
    # evidence
    rows = ''.join(f'<tr><td>{esc(r.get("claim"))}</td><td>{esc(r.get("work"))}<br><code>{esc(os.path.basename(r.get("file") or ""))}</code> <span class="ln">l. {esc(r.get("lines"))}</span></td><td class="q">{("&ldquo;"+esc(r["quote"])+"&rdquo;") if r.get("quote") else "<em>"+esc(r.get("note","no held line"))+"</em>"}</td></tr>' for r in E.get('shortDescription', []))
    tle = E.get('timeline') or []
    tlrows = ''
    for pi, per in enumerate(tl or []):
        for li, l in enumerate(per['lines']):
            try: r = tle[pi][li]
            except Exception: r = {}
            tlrows += f'<tr><td><span class="when">{esc(l["when"])}</span> {esc(l["text"])}</td><td>{esc(r.get("work"))}<br><code>{esc(os.path.basename(r.get("file") or ""))}</code> <span class="ln">l. {esc(r.get("lines"))}</span></td><td class="q">{("&ldquo;"+esc(r["quote"])+"&rdquo;") if r.get("quote") else "<em>see reference</em>"}</td></tr>'
    datebox = f'<p class="datebox"><b>Shown dates:</b> {esc(shown)}' + (f'<br><b>Census now:</b> {esc(d.get("census"))}' if d.get('census') else '') + (f'<br>{esc(d.get("reason"))}' if d.get('reason') else '') + '</p>'
    fixes = E.get('existingTextFixes') or []
    opn = E.get('openPoints') or []
    extra = ''
    if fixes: extra += '<h5>Existing texts flagged for a fix (not changed here)</h5>' + para_list(fixes)
    if opn: extra += '<h5>Open points</h5>' + para_list(opn)
    evid = f'''<div class="evidence"><h4>Evidence</h4>{datebox}
<h5>Short description</h5><div class="tw"><table><thead><tr><th>Claim</th><th>Held source</th><th>Its words</th></tr></thead><tbody>{rows}</tbody></table></div>
<details class="tle"><summary>Timeline evidence ({sum(len(p["lines"]) for p in (tl or []))} lines)</summary><div class="tw"><table><thead><tr><th>Line</th><th>Held source</th><th>Its words</th></tr></thead><tbody>{tlrows}</tbody></table></div></details>{extra}</div>'''
    return f'<section class="pair" id="{esc(cid)}">{phone}{evid}</section>'

body = ''.join(card_html(*c) for c in CARDS)
page = open(os.path.dirname(OUT) + '/template.html').read().replace('{{BODY}}', body)
open(OUT, 'w').write(page)
print('ok', len(page))
