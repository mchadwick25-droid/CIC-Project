import sys
sys.path.insert(0,'.')
from engine.m1.loader import load_world_records, load_fleet_records
from engine.m1.registry import load_registry
from engine.m1.quote_locus import gate_quote_locus
from engine.m1.rendering_review import gate_rendering_review
reg=load_registry(); fleet=None
worlds=sys.argv[1].split(',')
verbose=len(sys.argv)>2
for w in worlds:
    r=load_world_records(w)
    ql=gate_quote_locus(r,fleet,reg); rr=gate_rendering_review(r,fleet,reg)
    print(w,'quote-locus',len(ql),'rendering-review',len(rr))
    if verbose:
        for f in ql+rr: print('  ',f[:600])
