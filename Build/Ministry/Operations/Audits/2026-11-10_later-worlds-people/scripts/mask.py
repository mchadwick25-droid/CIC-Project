"""Per shelf row: the lines of its file that hold the shelved work's own text.
Span: the row's locus where it names line ranges or an XML div path; otherwise the whole file.
Masked out inside the span: XML <note> content and apparatus divs (corpus_structure's own patterns),
a closing index (an index/register heading in the last quarter of a .txt file, to the end),
index-entry lines (a name then two or more page numbers) and contents lines (dot leaders)."""
import json,re,sys,bisect,pickle,collections
sys.path.insert(0,'.')
from cic.engine.corpus_structure import _APPARATUS,_BARE_APPENDIX,_DIV,_TITLE,_unescape
S=sys.argv[1]
rows=json.load(open(S+'/shelf_rows.json'))
IDXH=re.compile(r'^\s*(general\s+)?(index|indices|indexes|register|namenregister|personenregister|sachregister|index\s+nominum|index\s+of\s+\w+|table\s+des\s+mati[eè]res|inhalt|inhaltsverzeichnis|verzeichnis)\b[\w\s,.]{0,40}$',re.I)
IDXL=re.compile(r'^.{2,80}?,\s*(?:[ivxlc]+\.?\s*,?\s*)?\d+[a-z]?(?:\s*[-–]\s*\d+)?(?:\s*[,;]\s*(?:[ivxlc]+\.?\s*)?\d+[a-z]?(?:\s*[-–]\s*\d+)?){1,}\.?\s*$')
DOTS=re.compile(r'(\.\s?){4,}\s*\d+\s*$')
RANGE=re.compile(r'lines?\s+~?\s*(\d[\d,]*)\s*[-–]\s*~?\s*(\d[\d,]*)',re.I)
DIVP=re.compile(r'\bdiv([1-3])\s+(\d+(?:\.\d+)*)')
cache={}
def fileinfo(fn):
    if fn in cache: return cache[fn]
    raw=open('cic/texts/'+fn,encoding='utf-8',errors='replace').read()
    lines=raw.split('\n'); n=len(lines)
    starts=[0];
    for l in lines[:-1]: starts.append(starts[-1]+len(l)+1)
    lno=lambda off: bisect.bisect_right(starts,off)  # 1-based
    bad=set(); secs={}
    if fn.endswith('.xml'):
        for m in re.finditer(r'<note\b.*?</note>',raw,re.S):
            bad.update(range(lno(m.start()),lno(m.end())+1))
        marks=[(m.start(),int(m.group(1)),_unescape((_TITLE.search(m.group(2)) or [None,''])[1] if _TITLE.search(m.group(2)) else '')) for m in re.finditer(r'<div([1-3])\b([^>]*)>',raw)]
        trail=[]
        for i,(off,lv,t) in enumerate(marks):
            if len(trail)>=lv: trail=trail[:lv]; trail[lv-1]+=1
            else: trail=trail+[1]*(lv-len(trail))
            end=len(raw)
            for o2,l2,_ in marks[i+1:]:
                if l2<=lv: end=o2; break
            a,b=lno(off),lno(end)
            secs[(lv,'.'.join(map(str,trail)))]=(a,b)
            if _APPARATUS.match(t.strip()) or _BARE_APPENDIX.match(t.strip()): bad.update(range(a,b+1))
    else:
        cut=None
        for i in range(int(n*0.75),n):
            if IDXH.match(lines[i]) and len(lines[i].strip())<60: cut=i+1; break
        if cut: bad.update(range(cut,n+1))
    for i,l in enumerate(lines,1):
        if IDXL.match(l) or DOTS.search(l): bad.add(i)
    cache[fn]=(n,bad,secs); return cache[fn]
span=collections.defaultdict(dict) # T -> file -> set(lines) or None(whole)
how=collections.Counter()
for r in rows:
    fn=r['file']
    if fn not in span[r['T']]: span[r['T']][fn]=set()
    cur=span[r['T']][fn]
    if cur is None: continue
    loc=r.get('locus') or ''
    rg=RANGE.findall(loc); dv=DIVP.findall(loc)
    if rg:
        for a,b in rg:
            a,b=int(a.replace(',','')),int(b.replace(',',''))
            if b>=a: cur.update(range(a,b+1))
        how['range']+=1; continue
    if dv and fn.endswith('.xml'):
        n,bad,secs=fileinfo(fn); ok=False
        for lv,p in dv:
            if (int(lv),p) in secs: a,b=secs[(int(lv),p)]; cur.update(range(a,b+1)); ok=True
        if ok: how['div']+=1; continue
    span[r['T']][fn]=None; how['whole']+=1
pickle.dump({T:{f:(None if v is None else frozenset(v)) for f,v in d.items()} for T,d in span.items()},open(S+'/span.pkl','wb'))
needed={r['file'] for r in rows}
bad={f:frozenset(fileinfo(f)[1]) for f in needed}
pickle.dump(bad,open(S+'/bad.pkl','wb'))
print(how, 'masked lines total',sum(len(v) for v in bad.values()))
