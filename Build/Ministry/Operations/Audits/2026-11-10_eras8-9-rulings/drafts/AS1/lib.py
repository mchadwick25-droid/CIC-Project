import re, os, json
ROOT='/home/user/CIC-Project'
S='/tmp/claude-0/-home-user-CIC-Project/72e14c9d-dd48-5323-8587-66a2d3d177e0/scratchpad/g89b/AS1'
MISSES=[]
sq=lambda s: re.sub(r'\s+',' ',s).strip()
FILES={
 'WH':'cic/texts/whitehouse_lingerings-of-light-in-a-dark-land_1873.txt',
 'COL':'cic/texts/propaganda-fide_collectanea-decreta-instructiones-rescripta-v1-lat_1907.txt',
 'PHI':'cic/texts/philipos_syrian-christians-of-malabar_howard1869.txt',
 'PAG':'cic/texts/pages_histoire-religion-chretienne-japon-annexes-fra_1870.txt',
}
SRC=json.load(open(S+'/raw/SOURCES.json'))
_c={}
def lines_of(path):
    if path not in _c: _c[path]=open(path,encoding='utf8',errors='replace').read().split('\n')
    return _c[path]
def find_lines(key,quote):
    L=lines_of(os.path.join(ROOT,FILES[key])); q=sq(quote)
    for a in range(len(L)):
        for span in range(1,10):
            t=sq(' '.join(L[a:a+span]))
            if q in t:
                if q in sq(' '.join(L[a+1:a+span])): break
                return f"{a+1}-{a+span}" if span>1 else str(a+1)
    MISSES.append(('LIB',key,quote)); return '0'
_r={}
def raw_has(name,quote):
    if name not in _r: _r[name]=sq(open(f'{S}/raw/{name}.txt',encoding='utf8',errors='replace').read())
    t=_r[name]
    if sq(quote) not in t: MISSES.append(('RAW',name,quote))
# evidence constructors
def lib(key,quote,rendering=None,note=None):
    d={'file':FILES[key],'lines':find_lines(key,quote),'quote':quote}
    if rendering: d['rendering']=rendering
    if note: d['note']=note
    return d
def raw(name,quote,rendering=None,note=None):
    raw_has(name,quote)
    d={'url':SRC[name]['url'],'accessed':SRC[name]['accessed'],'raw_file':f'raw/{name}.txt','quote':quote}
    if rendering: d['rendering']=rendering
    if note: d['note']=note
    return d
def rec(record,note=None):
    d={'record':record}
    if note: d['note']=note
    return d
# link source constructors
def lsrc_lib(kind,work,key,quote,locus=None,license='public-domain'):
    d={'kind':kind,'source_id':None,'work':work,'file':FILES[key],'lines':find_lines(key,quote),'locus':locus,'quote':quote,'license':license}
    if kind=='secondary': d.pop('source_id'); d.pop('license'); 
    if kind=='secondary' and locus is None: d.pop('locus')
    return d
def lsrc_raw(kind,work,name,quote,locus,license='public-domain'):
    raw_has(name,quote)
    d={'kind':kind,'work':work,'url':SRC[name]['url'],'accessed':SRC[name]['accessed'],'raw_file':f'raw/{name}.txt','locus':locus,'quote':quote}
    if kind=='primary': d['source_id']=None; d['license']=license
    return d
