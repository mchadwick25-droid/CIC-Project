const { chromium } = require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1440,height:900}});
p.on('pageerror',e=>console.log('PAGEERR',e.message));
await p.goto('http://localhost:8765/');await p.waitForTimeout(2500);
for(const s of [0.2,0.32,0.39,0.47,0.58,0.7,0.9,1.4,1.8,2.6,4,7]){
 const r=await p.evaluate(async s=>{
  scale=s;tx=0;ty=0;applyTransform();applyDetail();labelFitRun();
  await new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)));
  const vis=e=>{if(!e)return false;let n=e;while(n&&n.nodeType===1){const c=getComputedStyle(n);if(c.display==='none'||c.visibility==='hidden')return false;n=n.parentNode;}const b=e.getBoundingClientRect();return b.width>0||b.height>0;};
  const R=(e,kind,id)=>{const b=e.getBoundingClientRect();return {kind,id,x0:b.left,y0:b.top,x1:b.right,y1:b.bottom};};
  const it=[];
  document.querySelectorAll('#nodes .node').forEach(g=>{const id=g.dataset.id;
    const ic=g.querySelector('.trad-ico');if(vis(ic))it.push(R(ic,'house',id));
    const l=g.querySelector('.lbl');if(vis(l)&&!l.classList.contains('lbl-cull'))it.push(R(l,'name',id));});
  document.querySelectorAll('.prof-pill').forEach(g=>{const f=g.querySelector('.who-fig');if(vis(f))it.push(R(f,'figure',g.dataset.id));});
  document.querySelectorAll('.river-pill').forEach(g=>{const c=g.querySelector('.who-cap');if(vis(c))it.push(R(c,'bubble','b'+g.dataset.who));});
  document.querySelectorAll('.story').forEach((g,i)=>{const b=g.querySelector('.story-book');if(vis(b))it.push(R(b,'story','s'+i));});
  document.querySelectorAll('.council').forEach(g=>{const r=g.querySelector('.council-ring'),l=g.querySelector('.council-lbl');if(vis(r))it.push(R(r,'council',g.dataset.id));if(vis(l))it.push(R(l,'councilname',g.dataset.id));});
  const hit=(a,b)=>a.x0<b.x1-1&&a.x1>b.x0+1&&a.y0<b.y1-1&&a.y1>b.y0+1;
  const pairs={},ex=[];it.sort((a,b)=>a.y0-b.y0);
  for(let i=0;i<it.length;i++)for(let j=i+1;j<it.length;j++){const a=it[i],c=it[j];if(c.y0>a.y1)break;if(a.id===c.id)continue;if(hit(a,c)){const k=[a.kind,c.kind].sort().join(' x ');pairs[k]=(pairs[k]||0)+1;if(ex.length<8)ex.push(k+': '+a.id+' / '+c.id);}}
  const named=document.querySelectorAll('#nodes .node').length-document.querySelectorAll('#nodes .lbl.lbl-cull').length;
  return {pairs,total:Object.values(pairs).reduce((x,y)=>x+y,0),n:it.length,ex};
 },s);
 console.log('scale',s,'overlaps',r.total,'marks',r.n,JSON.stringify(r.pairs));
 if(process.argv[2]&&r.total)console.log('  '+r.ex.join('\n  '));
}
await b.close();})();
