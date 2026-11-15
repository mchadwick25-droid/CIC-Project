const { chromium } = require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1440,height:900}});const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.goto('http://localhost:8765/');await p.waitForTimeout(2000);
let lost=0;
for(let run=0;run<10;run++){
 const r=await p.evaluate(async run=>{const m=byId['cistercian-monasticism']||churchBodies[40+run];scale=0.9;tx=innerWidth/2-m._x*scale;ty=innerHeight/2-m._y*scale;applyTransform();applyDetail();await new Promise(r=>setTimeout(r,120));
  const g=document.querySelector(`.node[data-id="${m.id}"]`);g.focus();for(let i=0;i<4;i++){zoomCentre(1/1.25);await new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)));}
  await new Promise(r=>setTimeout(r,150));return document.activeElement.tagName;},run);
 if(r==='BODY')lost++;}
console.log('zoom out from tradition, focus lost in',lost,'of 10',errs);await b.close();})();
