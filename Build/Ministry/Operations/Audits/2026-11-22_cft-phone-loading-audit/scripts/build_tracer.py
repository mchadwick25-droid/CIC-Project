#!/usr/bin/env python3
"""Make an instrumented copy of the Church Family Tree map that logs every data field the page reads.

Usage: build_tracer.py SOURCE_INDEX_HTML DEST_INDEX_HTML

The copy wraps the page's embedded data (`const DATA = {...}`) in a Proxy. Each read of a field is
counted under window.__reads[window.__phase][path], where path looks like DATA.movements[].card.role.
Whole-object enumeration (spread, Object.keys, JSON.stringify) is counted under window.__enum.
The driver (audit_run.js) sets window.__phase before each scenario. Serve DEST next to the map's
other files and drive it with a browser. The copy is for measuring only; it is never published.
"""
import json
import sys

src, dest = sys.argv[1], sys.argv[2]
html = open(src, encoding='utf8').read()
start = html.index('=', html.index('const DATA')) + 1
body = html[start:]
lead = body[:len(body) - len(body.lstrip())]
body = body.lstrip()
_, end = json.JSONDecoder().raw_decode(body)
rest = body[end:]
assert rest.startswith('\n;'), 'the data literal is not followed by ";" as expected'

TRACER = r"""
;
window.__phase='startup'; window.__reads={}; window.__enum={};
(function(){
  const cache=new WeakMap();
  const bump=(bucket,key)=>{const p=window.__phase,b=(bucket[p]=bucket[p]||{});b[key]=(b[key]||0)+1;};
  function wrap(o,path){
    if(o===null||typeof o!=='object')return o;
    if(cache.has(o))return cache.get(o);
    const isArr=Array.isArray(o);
    const px=new Proxy(o,{
      get(t,k,r){
        const v=Reflect.get(t,k,r);
        if(typeof k!=='string')return v;
        if(isArr){ if(/^\d+$/.test(k))return wrap(v,path+'[]'); return v; }
        if(typeof v==='function')return v;
        bump(window.__reads,path+'.'+k);
        return wrap(v,path+'.'+k);
      },
      has(t,k){ if(typeof k==='string'&&!isArr)bump(window.__reads,path+'.'+k+' (in)'); return Reflect.has(t,k); },
      ownKeys(t){ if(!isArr)bump(window.__enum,path); return Reflect.ownKeys(t); }
    });
    cache.set(o,px); return px;
  }
  window.__rawData=DATA_RAW;
  window.DATA_PROXY=wrap(DATA_RAW,'DATA');
})();
const DATA=window.DATA_PROXY;
"""

out = html[:start] + lead + body[:end] + TRACER + rest[2:]
out = out.replace('const DATA = {', 'const DATA_RAW = {', 1)
open(dest, 'w', encoding='utf8').write(out)
print('wrote', dest, len(out), 'bytes')
