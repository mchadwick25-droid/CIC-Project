import sys,types,inspect,importlib,tempfile,pathlib,traceback
sys.path.insert(0,'.')
m=types.ModuleType('pytest')
class _Mark:
    def parametrize(self,name,vals):
        def d(f): f._params=(name,vals); return f
        return d
    def __getattr__(self,n): return lambda *a,**k:(a[0] if a and callable(a[0]) else (lambda f:f))
m.mark=_Mark()
FIX={}
def fixture(f=None,**k):
    def reg(g): FIX[g.__name__]=g; return g
    return reg(f) if f else reg
m.fixture=fixture
class Raises:
    def __init__(s,e,match=None): s.e=e
    def __enter__(s): return s
    def __exit__(s,t,v,tb):
        if t is None: raise AssertionError('did not raise')
        return issubclass(t,s.e)
m.raises=lambda e,match=None:Raises(e,match)
m.approx=lambda x,**k:x
sys.modules['pytest']=m
class MP:
    def __init__(s): s.u=[]
    def setattr(s,t,n,v=None,raising=True):
        if isinstance(t,str):
            mod,_,attr=t.rpartition('.'); t=importlib.import_module(mod); v=n; n=attr
        s.u.append((t,n,getattr(t,n,None))); setattr(t,n,v)
    def setitem(s,d,k,v): s.u.append(('item',d,k,d.get(k,'__MISSING__'))); d[k]=v
    def delitem(s,d,k,raising=True): s.u.append(('item',d,k,d.get(k,'__MISSING__'))); d.pop(k,None)
    def setenv(s,k,v):
        import os; s.setitem(os.environ,k,v)
    def delenv(s,k,raising=True):
        import os; s.delitem(os.environ,k)
    def undo(s):
        for x in reversed(s.u):
            if x[0]=='item':
                _,d,k,v=x
                if v=='__MISSING__': d.pop(k,None)
                else: d[k]=v
            else: setattr(*x)
mod=importlib.import_module(sys.argv[1])
ok=fail=0
for n,f in list(vars(mod).items()):
    if not n.startswith('test_') or not callable(f): continue
    params=[None]
    if hasattr(f,'_params'): params=f._params[1]
    for p in params:
        mp=MP(); args={}
        sig=inspect.signature(f)
        try:
            for a in sig.parameters:
                if a=='monkeypatch': args[a]=mp
                elif a=='tmp_path': args[a]=pathlib.Path(tempfile.mkdtemp())
                elif hasattr(f,'_params') and a==f._params[0]: args[a]=p
                elif a in FIX:
                    fx=FIX[a]; fa={b:(mp if b=='monkeypatch' else pathlib.Path(tempfile.mkdtemp()) if b=='tmp_path' else None) for b in inspect.signature(fx).parameters}
                    args[a]=fx(**fa)
                else: raise RuntimeError('unknown fixture '+a)
            f(**args); ok+=1
        except Exception:
            fail+=1; print('FAIL',n,p); traceback.print_exc(limit=3)
        finally: mp.undo()
print(sys.argv[1],'ok',ok,'fail',fail)
