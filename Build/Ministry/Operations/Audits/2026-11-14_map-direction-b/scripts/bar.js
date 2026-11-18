const { chromium } = require('playwright');
(async()=>{const b=await chromium.launch();
for(const w of [641,690,700,768,820,900,1000,1180]){const p=await b.newPage({viewport:{width:w,height:1000}});const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.goto('http://localhost:8765/');await p.waitForTimeout(1500);
const rows=async()=>p.evaluate(()=>{const tops=new Set([...document.querySelectorAll('#switchbar>*')].filter(e=>!e.hidden&&e.offsetParent).map(e=>Math.round(e.getBoundingClientRect().top)));const bar=document.getElementById('switchbar');return {rows:tops.size,overflow:bar.scrollWidth>bar.clientWidth+1};});
const r1=await rows();await p.evaluate(()=>setWho({type:'river',lane:5,era:1},{on:true}));await p.waitForTimeout(300);const r2=await rows();
console.log(w,'rows',r1.rows,r1.overflow?'OVERFLOW':'','| with Who',r2.rows,r2.overflow?'OVERFLOW':'',errs.join(';'));await p.close();}
await b.close();})();
