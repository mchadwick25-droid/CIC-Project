const { chromium, devices } = require('playwright');
(async()=>{const b=await chromium.launch();
for(const [label,opts] of [['desktop',{viewport:{width:1440,height:900}}],['phone',devices['iPhone 13']]]){
const c=await b.newContext(opts);const p=await c.newPage();p.on('pageerror',e=>console.log('PAGEERR',e.message));
await p.goto('http://localhost:8765/');await p.waitForTimeout(2500);
const r=await p.evaluate(async()=>{
 const vis=e=>{if(!e)return false;let n=e;while(n&&n.nodeType===1){const c=getComputedStyle(n);if(c.display==='none'||c.visibility==='hidden')return false;n=n.parentNode;}const b=e.getBoundingClientRect();return b.width>0||b.height>0;};
 const R=(e,kind,id)=>{const b=e.getBoundingClientRect();return {kind,id,x0:b.left,y0:b.top,x1:b.right,y1:b.bottom};};
 const out=[];
 for(const key of riverWho.keys()){
  const [lane,era]=key.split(':').map(Number);
  setWho({type:'river',lane,era},{on:true});
  await new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)));
  const it=[];
  document.querySelectorAll('#nodes .node.who-lit').forEach(g=>{const id=g.dataset.id;const l=g.querySelector('.lbl');if(vis(l)&&!l.classList.contains('lbl-cull'))it.push(R(l,'name',id));const ic=g.querySelector('.trad-ico');if(vis(ic))it.push(R(ic,'house',id));});
  document.querySelectorAll('#who .who-name').forEach((g,i)=>{const t=g.querySelector('text');if(vis(t))it.push(R(t,'who','w'+i));});
  document.querySelectorAll('.river-pill[aria-pressed="true"]').forEach(g=>{const c=g.querySelector('.who-cap');if(vis(c))it.push(R(c,'bubble','b'));});
  const hit=(a,b)=>a.x0<b.x1-1&&a.x1>b.x0+1&&a.y0<b.y1-1&&a.y1>b.y0+1;
  let n=0;const ex=[];
  for(let i=0;i<it.length;i++)for(let j=i+1;j<it.length;j++){if(it[i].id===it[j].id)continue;if(hit(it[i],it[j])){n++;if(ex.length<3)ex.push(it[i].kind+':'+it[i].id+' x '+it[j].kind+':'+it[j].id);}}
  const offscreen=[...document.querySelectorAll('#who .who-name')].filter(g=>{const b=g.getBoundingClientRect();return b.right<0||b.left>innerWidth||b.bottom<0||b.top>innerHeight;}).length;
  out.push({key,n,shown:document.querySelectorAll('#who .who-name').length,offscreen,ex});
 }
 clearWho();return out;});
const bad=r.filter(x=>x.n);console.log(label,'river-eras',r.length,'with overlaps',bad.length,'total',bad.reduce((a,x)=>a+x.n,0),'names off-screen',r.reduce((a,x)=>a+x.offscreen,0),'of',r.reduce((a,x)=>a+x.shown,0));
bad.slice(0,8).forEach(x=>console.log('  ',x.key,x.n,x.ex.join('; ')));
await c.close();}
await b.close();})();
