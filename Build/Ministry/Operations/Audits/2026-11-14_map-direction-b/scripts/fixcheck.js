const { chromium, devices } = require('playwright');
(async()=>{const b=await chromium.launch();
const go=async(opts,url='http://localhost:8765/')=>{const c=await b.newContext(opts);const p=await c.newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));await p.goto(url);await p.waitForTimeout(2000);p.errs=errs;return p;};
const D={viewport:{width:1440,height:900}};
// 2 house click opens card
let p=await go(D);
const res=await p.evaluate(async()=>{const m=byId['alexandria-catechetical'];scale=1.2;tx=innerWidth/2-m._x*scale;ty=innerHeight/2-m._y*scale;applyTransform();applyDetail();labelFitRun();await new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)));
 const r=document.querySelector('.node[data-id="alexandria-catechetical"] .trad-ico').getBoundingClientRect();const el=document.elementFromPoint((r.left+r.right)/2,(r.top+r.bottom)/2);return el.closest('.node')?'node':el.closest('.prof-pill')?'figure':el.tagName;});
console.log('2 house hit ->',res);
// 1 caps at zoom 9
console.log('1 caps', await p.evaluate(async()=>{scale=9;applyTransform();applyDetail();labelFitRun();await new Promise(r=>requestAnimationFrame(r));const px=e=>Math.round(e.getBoundingClientRect().height);return {council:px(document.querySelector('.council-lbl')),across:getComputedStyle(document.querySelector('.across-lbl')).fontSize, ring:+document.querySelector('.node .focus-ring').getAttribute('r')*scale};}));
// 4 escape from tray returns focus
console.log('4', await p.evaluate(async()=>{scale=0.9;applyTransform();applyDetail();const pill=document.querySelector('.river-pill');pill.focus();pill.dispatchEvent(new KeyboardEvent('keydown',{key:'Enter',bubbles:true}));await new Promise(r=>setTimeout(r,300));const row=document.querySelector('.tray-row');row.focus();row.dispatchEvent(new KeyboardEvent('keydown',{key:'Escape',bubbles:true}));await new Promise(r=>setTimeout(r,200));return [document.activeElement.className.baseVal||document.activeElement.tagName,document.getElementById('mapStatus').textContent];}));
console.log('errs',p.errs);
// 3 deep link feedback
p=await go(D,'http://localhost:8765/?world=desert-monasticism');console.log('3 deep link feedback', await p.evaluate(()=>!!document.querySelector('#panel .page-feedback')));
// 5 phone show on map from card
p=await go(devices['iPhone 13']);console.log('5 phone', await p.evaluate(async()=>{openPanel(byId['desert-monasticism']);await new Promise(r=>setTimeout(r,300));const b=panelBody.querySelector('.who-btn[data-who]');b.focus();b.click();await new Promise(r=>setTimeout(r,500));return [document.activeElement.id||document.activeElement.tagName, panel.classList.contains('open')];}));
// 6 resize with card open and who on
console.log('6 resize', await p.evaluate(async()=>{const row=document.querySelector('.tray-row');row.click();await new Promise(r=>setTimeout(r,300));window.dispatchEvent(new Event('resize'));await new Promise(r=>setTimeout(r,300));return panel.classList.contains('open');}));
// 7 tablet
p=await go(devices['iPad Mini']);console.log('7 tablet', await p.evaluate(async()=>{openPanel(byId['alexandria-catechetical']);await new Promise(r=>setTimeout(r,300));panelBody.querySelector('.who-btn[data-who]').click();await new Promise(r=>setTimeout(r,600));const vis=[...document.querySelectorAll('#who .who-name')].filter(g=>{const r=g.getBoundingClientRect();const tr=document.getElementById('whoTray').getBoundingClientRect();return r.left>tr.right&&r.right<innerWidth&&r.top>0&&r.bottom<innerHeight&&!(panel.classList.contains('open')&&r.right>panel.getBoundingClientRect().left);}).length;return [vis,document.querySelectorAll('#who .who-name').length,panel.classList.contains('open')];}));
await b.close();})();
