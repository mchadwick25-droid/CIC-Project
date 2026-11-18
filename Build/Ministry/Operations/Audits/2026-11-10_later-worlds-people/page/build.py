import json,html,collections,re
E=html.escape
F=json.load(open('final_rows.json'))
C={r['cid']:r for r in json.load(open('consolidated.json'))}
cen=json.load(open('/home/user/CIC-Project/cic-website/data/world-census.json')); mv={m['id']:m for m in cen['movements']}
def st(i):
    try: return int(re.sub(r'\D','',str(mv[i]['start'])) or 9999)
    except: return 9999
one=[r['name'] for r in C.values() if len(r['traditions_at_5'])==1]
groups=collections.defaultdict(list)
for r in F:
    if r['recommendation']=='out': continue
    groups[r['home']['id']].append(r)
order=sorted(groups,key=lambda h:(st(h),h))
QLAB={'founder':'Question A · founder','own_words':'Question B · own words','one_witness':'Question C · one witness'}
def card(r):
    rec=r['recommendation']; q=r.get('question')
    trs=''.join(f"""<li><div class=tl><span class=tname>{E(t.get('census_name') or t['name'])}</span><span class=num>from {E(str(t.get('start','')))} · {t['clean']} passages</span></div>
<blockquote>“{E((t.get('quote') or {}).get('text') or '')}”<cite>{E((t.get('quote') or {}).get('file') or '')}:{(t.get('quote') or {}).get('line') or ''}</cite></blockquote></li>""" for t in r['counted_traditions'] if t.get('clean',0)>=5)
    fo=r.get('founder_of')
    return f"""<article class="card {rec}" id="{r['cid']}"><header><h4>{E(r['name'])}</h4><span class="pill {rec}">{'Include' if rec=='include' else 'Hold'}</span>{f'<span class=qchip>{QLAB[q]}</span>' if q else ''}</header>
<p class=meta>{E(r['dates'])}</p>
<p>{E(r['why'])}</p>
<dl><dt>Own words</dt><dd>{E(r.get('own_words') or '')}</dd>
<dt>Founder</dt><dd>{E(fo['name']) if fo else 'No movement is his or hers'}</dd>
<dt>Recommendation</dt><dd>{E(r['reason'])}</dd></dl>
<p class=sub>Named in later traditions' own texts</p><ul class=trads>{trs}</ul>
{f'<details><summary>Notes for checking</summary><p class=small>{E(r["doubts"])}</p></details>' if r.get('doubts') else ''}</article>"""
secs=''
for h in order:
    m=mv.get(h,{})
    secs+=f"""<section class=grp><h3>{E(m.get('name',h))} <span class=num>{E(str(m.get('dates','')))}</span></h3><div class=cards>{''.join(card(r) for r in sorted(groups[h],key=lambda r:r['cid']))}</div></section>"""
inc=[r for r in F if r['recommendation']=='include']; hold=[r for r in F if r['recommendation']=='hold']; out=[r for r in F if r['recommendation']=='out']
fnd=[r['name'] for r in F if r.get('question')=='founder']
fndw=['Novatian','Apollinaris of Laodicea','Huldrych Zwingli']
noq=[r['name'] for r in hold if not r.get('question')]
summ=''.join(f"<li><a href='#{r['cid']}'>{E(r['name'])}</a></li>" for r in inc)
outl=''.join(f"<li><b>{E(r['name'])}</b>: {E(r['reason'])}</li>" for r in out)
tpl=open('page/template.html').read()
for k,v in {'%%INC%%':str(len(inc)),'%%HOLD%%':str(len(hold)),'%%SUMM%%':summ,'%%SECS%%':secs,'%%OUT%%':outl,'%%ONE%%':E(', '.join(sorted(one))),'%%NONE%%':E(', '.join(noq)),
            '%%FND%%':E(', '.join(fnd)),'%%NONE_N%%':str(len(noq)),'%%ONE_N%%':str(len(one))}.items(): tpl=tpl.replace(k,v)
open('page/Later_Worlds_People.html','w').write(tpl)
print(len(inc),len(hold),len(out),len(one),fnd,noq)
