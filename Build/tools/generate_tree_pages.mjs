#!/usr/bin/env node
/**
 * Generate static tree pages for every census movement, and a retired page for each retired movement with no redirect.
 *
 * Output: one HTML file per movement at cft-website/tree/<slug>.html
 * Creates: cic-website/sitemap.xml, cic-website/robots.txt
 *
 * Each tree page includes:
 * - Title and meta description from census
 * - Open Graph metadata
 * - Movement name, era, dates, status, region
 * - Lineage (edges in/out as links)
 * - Sources from census
 * - Links to built world tradition pages (when applicable)
 * - Faithways Studio attribution
 */

import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { createRequire } from 'module';
import { narrationTextFor, recordingMatchesText } from './generate_tree_narration.mjs';
import { fingerprint as docStoryFingerprint } from './generate_docstory_narration.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const rootDir = path.resolve(__dirname, '..', '..');
const argAt = name => { const i = process.argv.indexOf(name); return i >= 0 ? path.resolve(process.argv[i + 1]) : null; };
const censusPath = argAt('--census') || path.join(rootDir, 'cic-website/data/world-census.json');
const outRoot = argAt('--out') || rootDir;
createRequire(import.meta.url)(path.join(rootDir, 'cic-website/assets/place-line.js'));
const { formatPlace } = globalThis.CFTPlace;
const treeDir = path.join(outRoot, 'cft-website/tree');
const websiteDir = path.join(outRoot, 'cic-website');
const audioDir = argAt('--audio') || path.join(rootDir, 'cft-website/audio/tree');
const docStoryManifestPath = path.join(path.dirname(audioDir), 'docstories', 'manifest.json');
const docStoryManifest = fs.existsSync(docStoryManifestPath) ? JSON.parse(fs.readFileSync(docStoryManifestPath, 'utf-8')) : {};

// Read census data
const census = JSON.parse(fs.readFileSync(censusPath, 'utf-8'));
const anyWorldOpen = census.movements.some(m => m.publicOpen);
const siteContent = JSON.parse(fs.readFileSync(path.join(rootDir, 'Build/tools/tree_site_pages.json'), 'utf-8'));
const conversationsLive = siteContent.conversationsLive === true || process.argv.includes('--conversations-live');

const PAGE_STYLE = `<style>
:root{
  --parchment:#F6F6F2; --vellum:#FFFFFF;
  --ink:#2A2521; --ink-faded:#6C6257; --madder:#A13E2B; --madder-deep:#7E2F20;
  --tyrian:#6B3FA0; --graphite:#8A837C; --rule:rgba(241,233,221,.16);
  --ground:#17130F; --surface:#1E1913;
  --text:#F1E9DD; --muted:#B8AEA1;
  --action:#E08C74; --action-hover:#F0A98F;
  --control:#A39B92;
  --link-grow:#86cf9c; --link-influence:#c79a5e; --link-conflict:#f06a64; --link-contact:#a39a8c;
  --btn-fill:#A13E2B; --btn-text:#F6EFE0; --btn-edge:#E08C74;
  --serif:'Alegreya','Iowan Old Style',Georgia,serif;
  --sans:'Alegreya Sans','Trebuchet MS',system-ui,sans-serif;
  --wide:64rem; --col:44rem; --measure:38rem;
}
*{box-sizing:border-box}
body{margin:0;background:var(--ground);color:var(--text);font-family:var(--serif);font-size:1.0625rem;line-height:1.65}
a{color:var(--action);text-decoration-thickness:1px;text-underline-offset:.16em}
a:hover{color:var(--action-hover)}
:focus-visible{outline:2px solid var(--action);outline-offset:3px;border-radius:2px}
img{max-width:100%;height:auto;display:block}
h1,h2,h3{font-family:var(--serif);font-weight:500;line-height:1.15;margin:0;text-wrap:balance}
h1{font-size:2rem;margin-bottom:1rem}
h2{font-size:1.4rem;margin:1.5rem 0 .75rem}
h3{font-size:1.1rem;margin:1rem 0 .5rem}
p{margin:0 0 1rem}
ul{padding-left:1.5rem}
li{margin-bottom:.5rem}
.vh{position:absolute!important;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
.skip-link{position:absolute;left:-999px;top:auto;background:var(--ink);color:var(--parchment);padding:.6rem 1rem;z-index:100;font-family:var(--sans)}
.skip-link:focus{position:fixed;left:1rem;top:1rem}
.eyebrow{font-family:var(--sans);font-size:.8125rem;letter-spacing:.13em;text-transform:uppercase;color:var(--action);font-weight:600;margin:0 0 .6rem}
.site-header{background:var(--surface);border-bottom:1px solid var(--rule)}
.site-header .row{max-width:var(--wide);margin:0 auto;padding:.6rem 1.25rem;display:flex;flex-wrap:wrap;align-items:center;gap:.5rem 1rem}
.wordmark{font-family:var(--serif);font-weight:700;font-size:1.2rem;letter-spacing:.01em;color:var(--text);text-decoration:none;white-space:nowrap;padding:.5rem 0;display:inline-block}
.wordmark em{font-style:italic;font-weight:400}
.page{max-width:var(--col);margin:0 auto;padding:2rem 1.25rem;overflow-wrap:break-word}
.titleblock{margin-bottom:2rem}
.ident{font-family:var(--sans);font-size:.9rem;color:var(--muted);margin:0 0 .5rem}
.kind-label{display:inline-block;font-family:var(--sans);font-size:.9rem;color:var(--muted);border:1px dashed currentColor;border-radius:999px;padding:.1rem .7rem;margin:-.4rem 0 0}
.lineage-section{margin:1.5rem 0;padding-left:.9rem;border-left:3px solid var(--link-contact)}
.lineage-section.link-grow{border-left-color:var(--link-grow)}.lineage-section.link-grow h3{color:var(--link-grow)}
.lineage-section.link-influence{border-left-color:var(--link-influence)}.lineage-section.link-influence h3{color:var(--link-influence)}
.lineage-section.link-conflict{border-left-color:var(--link-conflict)}.lineage-section.link-conflict h3{color:var(--link-conflict)}
.lineage-section.link-contact h3{color:var(--link-contact)}
.lineage-list{list-style:none;padding:0}
.lineage-section h4{font-size:1.05rem;margin:.2rem 0 .4rem}
.lineage-section.link-influence h4{color:var(--link-influence)}.lineage-section.link-conflict h4{color:var(--link-conflict)}.lineage-section.link-contact h4{color:var(--link-contact)}.lineage-section.link-grow h4{color:var(--link-grow)}
.lineage-rest-heading{margin:2rem 0 .2rem}
.lineage-kind{font-family:var(--sans);font-size:.8rem;letter-spacing:.03em;color:var(--muted);margin-right:.2rem}
.lineage-none{color:var(--muted);font-style:italic}
.lineage-strip{display:flex;flex-wrap:wrap;gap:.3rem .7rem;align-items:baseline;font-family:var(--sans);font-size:.95rem;background:var(--surface);border-radius:4px;padding:.55rem .8rem;margin:1rem 0 0}
.lineage-arrow{color:var(--muted)}
.lineage-list li{margin:0 0 .5rem;padding:0}
.lineage-list a{color:var(--action)}
.confidence-note{font-style:italic;color:var(--muted);font-size:.95rem}
.lineage-major{font-family:var(--sans);font-size:.8rem;letter-spacing:.03em;font-weight:600;color:var(--action);white-space:nowrap}
.lineage-outcome{display:block;font-size:.95rem;margin-top:.2rem}
.lineage-confidence{font-family:var(--sans);font-size:.8rem;letter-spacing:.03em;color:var(--muted);border:1px solid currentColor;border-radius:3px;padding:0 4px;white-space:nowrap}
.sources-list{list-style:none;padding:0}
.sources-list li{margin:0 0 .75rem;padding:0}
.sources-list a{font-weight:600}
.source-type{font-family:var(--sans);font-size:.85rem;color:var(--muted)}
.source-note{font-size:.95rem;color:var(--muted)}
.quotes-note{font-family:var(--sans);font-size:.9rem;color:var(--muted);margin:.6rem 0}
.quotes-panel{margin:1rem 0;border-top:1px solid var(--rule);padding-top:.6rem}
.quotes-panel summary{cursor:pointer;font-family:var(--sans);font-weight:600}
.narration{display:flex;align-items:center;gap:.6rem;flex-wrap:wrap;margin:1.5rem 0}
.narration audio{display:block;height:2.2rem;max-width:220px;width:220px;flex:0 0 auto}
.narration-label{flex:1 1 100%;font-family:var(--sans);font-weight:700;margin:0}
.narration-label span{font-weight:400;color:var(--muted)}
.action-links{margin:1.5rem 0;padding:1rem;background:var(--surface);border-radius:4px}
.action-links p{margin:0 0 .8rem;font-family:var(--sans);font-size:.95rem}
.action-links a{display:inline-block;padding:.6rem 1rem;background:var(--btn-fill);color:var(--btn-text);text-decoration:none;border-radius:4px;margin-right:.5rem;margin-bottom:.5rem}
.action-links a:hover{background:var(--madder-deep)}
.door-quiet{font-family:var(--sans);font-size:.92rem;color:var(--muted);margin:1.5rem 0}
.told-within{font-family:var(--sans);font-size:.95rem;margin:.4rem 0 0}
.people-list{list-style:none;padding:0;margin:0}
.people-list li{margin:.4rem 0}
.people-list .ident{display:inline;margin:0 0 0 .4rem}
.people-note{color:var(--muted)}
.facts{margin:0 0 1.5rem}
.short-desc{font-size:1.15rem;line-height:1.55;margin:0 0 1rem}
.brief-sources{margin:1rem 0;border-top:1px solid var(--rule);padding-top:.6rem}
.read-along{margin:1rem 0}
.read-along>summary{cursor:pointer;font-family:var(--sans);font-weight:600}
.tl-all{font-family:var(--sans);font-weight:600;font-size:.95rem;min-height:44px;padding:0 1rem;margin:0 0 .6rem;border:1px solid var(--rule);border-radius:999px;background:none;color:var(--action);cursor:pointer}
details.tl-period{border-bottom:1px solid var(--rule)}
details.tl-period>summary{cursor:pointer;padding:.6rem 0;min-height:44px;box-sizing:border-box}
.tl-pw{font-family:var(--sans);font-weight:700;color:var(--action);font-variant-numeric:tabular-nums}
.tl-wit{font-style:italic;color:var(--muted)}
ol.tl{list-style:none;padding:0 0 0 1rem;border-left:2px solid var(--rule);margin:.4rem 0 1rem}
ol.tl li{margin:0 0 .7rem}
.tl-when{display:block;font-family:var(--sans);font-weight:700;font-size:.9rem}
.tl-note{display:block;font-size:.88rem;color:var(--muted)}
.facts dt{font-family:var(--sans);font-size:.8rem;letter-spacing:.08em;text-transform:uppercase;color:var(--action);margin-top:.7rem}
.facts dd{margin:.1rem 0 0}
.part-group{font-family:var(--sans);font-size:.8rem;letter-spacing:.08em;text-transform:uppercase;color:var(--action);margin:1rem 0 .2rem}
.verdict{font-family:var(--sans);font-size:.78rem;letter-spacing:.04em;color:var(--muted);border:1px dashed currentColor;border-radius:999px;padding:0 .5rem;margin-left:.4rem;white-space:nowrap}
.source-group{font-family:var(--sans);font-weight:600;margin:1rem 0 .3rem}
.review-status{font-family:var(--sans);font-size:.92rem;color:var(--muted);margin:2.5rem 0 0;padding-top:1rem;border-top:1px solid var(--rule)}
.site-footer{border-top:1px solid var(--rule);background:var(--surface);font-family:var(--sans);font-size:.85rem;color:var(--muted);margin-top:3rem;padding:1.5rem 1.25rem}
.site-footer .row{max-width:var(--wide);margin:0 auto}
.site-header nav{display:flex;flex-wrap:wrap;gap:.4rem 1rem;align-items:center;margin-left:auto;font-family:var(--sans);font-size:.92rem}
.site-header nav a{color:var(--action);text-decoration:none;display:inline-flex;align-items:center;min-height:44px}
.site-header nav a:hover{color:var(--action-hover)}
.site-header nav .feedback-toggle{min-height:44px}
.site-footer nav{display:flex;flex-wrap:wrap;gap:.4rem 1.1rem;margin-top:.6rem}
.site-footer nav a{display:inline-flex;align-items:center;min-height:44px}
.site-footer a{color:var(--action)}
.give{display:flex;flex-wrap:wrap;gap:.6rem;margin:1rem 0}
.give a{display:inline-block;padding:.6rem 1.2rem;background:var(--btn-fill);color:var(--btn-text);text-decoration:none;border-radius:4px}
.terms{margin:0 0 1rem}
.terms dt{font-family:var(--sans);font-weight:600;margin-top:.9rem}
.terms dd{margin:.2rem 0 0}
.terms svg{display:inline-block;vertical-align:middle;margin-right:.5rem}
.cite{margin:.4rem 0 1.2rem;padding:.6rem .9rem;border-left:3px solid var(--action);background:var(--surface);overflow-wrap:anywhere}
.cite-label{font-family:var(--sans);font-weight:600;margin:1rem 0 .2rem}
</style>`;

const ANALYTICS_TOKEN = siteContent.analyticsToken;
const analyticsTag = ANALYTICS_TOKEN ? `<script defer src="https://static.cloudflareinsights.com/beacon.min.js" data-cf-beacon='{"token": "${ANALYTICS_TOKEN}"}'></script>\n` : '';

function siteHeader(up) {
  return `<header class="site-header">
  <a href="${up}" class="skip-link">Skip to the map</a>
  <div class="row">
    <a href="${up}" class="wordmark">Church Family Tree</a>
    <nav aria-label="Site">
      <a href="https://churchinconversation.com/">Church in Conversation &rarr;</a>
      <a href="${up}support.html">Help us grow</a>
      <button type="button" class="feedback-toggle" id="feedback-toggle" aria-haspopup="dialog" aria-expanded="false">Tell us what you think</button>
    </nav>
  </div>
</header>`;
}

function siteFooter(up) {
  return `<footer class="site-footer">
  <div class="row">
    <p>&copy; 2026 Faithways Studio, Inc., a Colorado public benefit corporation &middot; <a href="${up}license.html">License</a>. The same team makes <a href="https://churchinconversation.com/">Church in Conversation</a>.</p>
    <nav aria-label="About the tree">
      <a href="${up}about.html">About</a>
      <a href="${up}method.html">Method</a>
      <a href="${up}data.html">Data and citation</a>
      <a href="${up}privacy.html">Privacy</a>
      <a href="${up}terms.html">Terms</a>
      <a href="${up}license.html">License</a>
      <a href="${up}support.html">Help us grow</a>
    </nav>
  </div>
</footer>`;
}

// Ensure tree directory exists
if (!fs.existsSync(treeDir)) {
  fs.mkdirSync(treeDir, { recursive: true });
}
if (!fs.existsSync(websiteDir)) {
  fs.mkdirSync(websiteDir, { recursive: true });
}

// Build a map of slugs to movements for easy lookup
const movementMap = new Map();
census.movements.forEach(m => {
  movementMap.set(m.id, m);
});

// Build edges map (both directions for easy lookup)
const edgesFrom = new Map(); // from -> [edges]
const edgesTo = new Map(); // to -> [edges]
census.edges.forEach(edge => {
  if (!edgesFrom.has(edge.from)) edgesFrom.set(edge.from, []);
  if (!edgesTo.has(edge.to)) edgesTo.set(edge.to, []);
  edgesFrom.get(edge.from).push(edge);
  edgesTo.get(edge.to).push(edge);
});

// Map movement IDs to built tradition pages (the 11 live worlds)
const builtWorlds = new Set([
  'post-apostolic-house-church',
  'alexandria-catechetical',
  'desert-monasticism',
  'syriac-edessa-nisibis',
  'cappadocian-nicene-pastoral-monastic-tradition',
  'hieronymian-ascetic-literary',
  'gallic-monastic-ascetic-christianity',
  'donatism',
  'lutheran-wittenberg-and-its-congregations',
  'the-reformed-cities-zurich-and-geneva',
  'imperial-juridical-christianity'
]);

function slugify(str) {
  return str
    .toLowerCase()
    .trim()
    .replace(/[^\w\s-]/g, '')
    .replace(/\s+/g, '-')
    .replace(/-+/g, '-');
}

function escapeHtml(text) {
  if (!text) return '';
  return text
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');
}

function truncateDescription(text, maxLength = 160) {
  if (!text) return '';
  if (text.length <= maxLength) return text;
  return text.substring(0, maxLength).replace(/\s+\S*$/, '') + '…';
}

function formatSourcesList(sources) {
  if (!sources || !Array.isArray(sources) || sources.length === 0) {
    return '<p>No sources recorded.</p>';
  }

  let html = '<ul class="sources-list">';
  sources.forEach(source => {
    let item = '<li>';
    if (source.url) {
      item += `<a href="${escapeHtml(source.url)}" target="_blank" rel="noopener noreferrer">${escapeHtml(source.work)}</a>`;
    } else {
      item += escapeHtml(source.work);
    }

    if (source.type) {
      item += ` <span class="source-type">(${escapeHtml(source.type)})</span>`;
    }

    if (source.note) {
      item += ` — <span class="source-note">${escapeHtml(source.note)}</span>`;
    }

    item += '</li>';
    html += item;
  });
  html += '</ul>';
  return html;
}

const LINEAGE_HEADINGS = [
  ['gave rise to', 'in', 'Grew Out Of', 'grow'],
  ['gave rise to', 'out', 'Gave Rise To', 'grow'],
  ['continued as', 'in', 'Continues', 'grow'],
  ['continued as', 'out', 'Continued As', 'grow'],
  ['influenced', 'in', 'Influenced By', 'influence'],
  ['influenced', 'out', 'Influenced', 'influence'],
  ['argued against', 'out', 'Argued Against', 'conflict'],
  ['argued against', 'in', 'Opposed By', 'conflict'],
  ['broke with', 'both', 'Broke With', 'conflict'],
  ['in contact with', 'both', 'In Contact With', 'contact'],
  ['member of', 'out', 'Member Of', 'contact'],
  ['member of', 'in', 'Members', 'contact'],
];

// Major links (Decision-Log 2026-11-08): lineage and breaks by type, any other link by its outcome.
const MAJOR_BY_TYPE = new Set(['gave rise to', 'continued as', 'broke with']);
function isMajorEdge(edge) {
  return MAJOR_BY_TYPE.has(edge.type) || (typeof edge.outcome === 'string' && edge.outcome.trim() !== '');
}

function buildPlainLineageHtml(movementId, movement) {
  const incoming = edgesTo.get(movementId) || [];
  const outgoing = edgesFrom.get(movementId) || [];
  let html = '';
  for (const [type, side, heading, family] of LINEAGE_HEADINGS) {
    const items = [];
    if (side !== 'out') incoming.filter(e => e.type === type).forEach(e => items.push([e, e.from]));
    if (side !== 'in') outgoing.filter(e => e.type === type).forEach(e => items.push([e, e.to]));
    const rows = items.filter(([, otherId]) => movementMap.has(otherId));
    if (!rows.length) continue;
    html += `<div class="lineage-section link-${family}">\n`;
    html += `<h3>${heading}</h3>\n<ul class="lineage-list">\n`;
    rows.forEach(([edge, otherId]) => {
      const other = movementMap.get(otherId);
      html += `<li id="${escapeHtml(edge.id)}"><a href="${other.id}.html">${escapeHtml(other.name)}</a>`;
      html += ` <span class="lineage-confidence">${escapeHtml(edge.confidence)}</span>`;
      if (isMajorEdge(edge)) html += ` <span class="lineage-major">Major</span>`;
      if (edge.note) html += ` — <span class="confidence-note">${escapeHtml(edge.note)}</span>`;
      if (edge.outcome) html += `<span class="lineage-outcome"><i>Lasting result:</i> ${escapeHtml(edge.outcome)}</span>`;
      html += '</li>\n';
    });
    html += '</ul>\n</div>\n';
  }
  return html;
}

// A tradition's connections, grouped by kind: direct descent first (Mark, 2026-11-22: "lets stay with just
// connecting the traditions"), then breaks, then influence, argument and contact. A person, a council or a
// movement across churches keeps the plain list above.
const DESCENT_TYPES = new Set(['gave rise to', 'continued as']);
const PARENT_KIND = { 'gave rise to': 'grew out of', 'continued as': 'continues' };
const isTradition = (m) => !!m && (!m.kind || m.kind === 'tradition');
const bothTraditions = (e) => isTradition(movementMap.get(e.from)) && isTradition(movementMap.get(e.to));

function lineageParts(movementId, movement) {
  const incoming = edgesTo.get(movementId) || [];
  const outgoing = edgesFrom.get(movementId) || [];
  const descent = (e) => DESCENT_TYPES.has(e.type) && bothTraditions(e);
  const split = (e) => e.type === 'broke with' && bothTraditions(e);
  const rest = (e) => !descent(e) && !split(e);
  const parents = incoming.filter(descent).map(e => ({ edge: e, otherId: e.from, kind: PARENT_KIND[e.type] }));
  const children = outgoing.filter(descent).map(e => ({ edge: e, otherId: e.to, kind: e.type }));
  const nextEntry = movement.continuesAs ? movementMap.get(movement.continuesAs) : null;
  const next = nextEntry && !children.some(c => c.otherId === nextEntry.id) ? nextEntry : null;
  const splits = outgoing.filter(split).map(e => ({ edge: e, otherId: e.to, kind: 'broke with' }))
    .concat(incoming.filter(split).map(e => ({ edge: e, otherId: e.from, kind: 'broke with' })));
  return { parents, children, next, splits, restIn: incoming.filter(rest), restOut: outgoing.filter(rest) };
}

function lineageItem(edge, otherId, kind) {
  const other = movementMap.get(otherId);
  let html = `<li id="${escapeHtml(edge.id)}"><span class="lineage-kind">${escapeHtml(kind)}</span> <a href="${other.id}.html">${escapeHtml(other.name)}</a>`;
  html += ` <span class="lineage-confidence">${escapeHtml(edge.confidence)}</span>`;
  if (isMajorEdge(edge)) html += ` <span class="lineage-major">Major</span>`;
  if (edge.note) html += ` — <span class="confidence-note">${escapeHtml(edge.note)}</span>`;
  if (edge.outcome) html += `<span class="lineage-outcome"><i>Lasting result:</i> ${escapeHtml(edge.outcome)}</span>`;
  return html + '</li>\n';
}

function lineageGroup(family, heading, rows, none) {
  let html = `<div class="lineage-section link-${family}">\n<h3>${heading}</h3>\n`;
  html += rows.length ? `<ul class="lineage-list">\n${rows.join('')}</ul>\n` : `<p class="lineage-none">${none}</p>\n`;
  return html + '</div>\n';
}

function buildTraditionLineageHtml(movementId, movement) {
  const P = lineageParts(movementId, movement);
  const others = P.restIn.length + P.restOut.length;
  let html = lineageGroup('grow', 'Descended from', P.parents.map(x => lineageItem(x.edge, x.otherId, x.kind)), 'No direct parent is recorded.');
  const kids = P.children.map(x => lineageItem(x.edge, x.otherId, x.kind));
  if (P.next) {
    const link = (edgesFrom.get(movementId) || []).find(e => e.type === 'continued as' && e.to === P.next.id);
    kids.push(link ? lineageItem(link, P.next.id, 'continued as')
      : `<li><span class="lineage-kind">continued as · not yet graded</span> <a href="${P.next.id}.html">${escapeHtml(P.next.name)}</a></li>\n`);
  }
  html += lineageGroup('grow', 'Direct descendants', kids, `No direct descendant is recorded.${others ? ' Its other links are influence, argument and contact.' : ''}`);
  if (P.splits.length) html += lineageGroup('conflict', 'Broke With', P.splits.map(x => lineageItem(x.edge, x.otherId, x.kind)), '');
  if (others) {
    html += '<h3 class="lineage-rest-heading">Influence, argument and contact</h3>\n';
    for (const [type, side, heading, family] of LINEAGE_HEADINGS) {
      const items = [];
      if (side !== 'out') P.restIn.filter(e => e.type === type).forEach(e => items.push([e, e.from]));
      if (side !== 'in') P.restOut.filter(e => e.type === type).forEach(e => items.push([e, e.to]));
      const rows = items.filter(([, otherId]) => movementMap.has(otherId));
      if (!rows.length) continue;
      html += `<div class="lineage-section link-${family}">\n<h4>${heading}</h4>\n<ul class="lineage-list">\n`;
      rows.forEach(([edge, otherId]) => { html += lineageItem(edge, otherId, edge.type); });
      html += '</ul>\n</div>\n';
    }
  }
  return html;
}

function buildLineageStrip(movementId, movement, label = 'Direct line of descent') {
  if (!isTradition(movement)) return '';
  const P = lineageParts(movementId, movement);
  if (!P.parents.length && !P.children.length && !P.next) return '';
  const link = (id) => `<a href="${id}.html">${escapeHtml(movementMap.get(id).name)}</a>`;
  const uniq = (a) => [...new Set(a)];
  const side = (ids, none) => ids.length ? ids.slice(0, 3).map(link).join(' · ') + (ids.length > 3 ? ' <span class="lineage-none">and more, under Connections</span>' : '') : `<span class="lineage-none">${none}</span>`;
  const left = side(uniq(P.parents.map(x => x.otherId)), 'no parent recorded');
  const right = side(uniq(P.children.map(x => x.otherId).concat(P.next ? [P.next.id] : [])), 'no descendant recorded');
  return `<nav class="lineage-strip" aria-label="${escapeHtml(label)}"><span>${left}</span><span class="lineage-arrow" aria-hidden="true">→</span><b>${escapeHtml(movement.name)}</b><span class="lineage-arrow" aria-hidden="true">→</span><span>${right}</span></nav>`;
}

// The direct line at the top of each page (Stage Two Kit, section 1): a tradition's own, a person's home
// tradition's, and for a council the major council before it and the one after.
function directLineHtml(movement) {
  if (movement.kind === 'person') {
    const home = movement.toldWithin ? movementMap.get(movement.toldWithin) : null;
    return home ? buildLineageStrip(home.id, home, "Their tradition's direct line") : '';
  }
  if (movement.kind === 'major-council') {
    const list = census.movements.filter(m => m.kind === 'major-council').sort((a, b) => a.start - b.start || a.name.localeCompare(b.name));
    const i = list.indexOf(movement), before = list[i - 1], after = list[i + 1];
    if (!before && !after) return '';
    const side = (c, none) => c ? `<a href="${c.id}.html">${escapeHtml(c.name)}</a>` : `<span class="lineage-none">${none}</span>`;
    return `<nav class="lineage-strip" aria-label="Major councils before and after"><span>${side(before, 'none before')}</span><span class="lineage-arrow" aria-hidden="true">→</span><b>${escapeHtml(movement.name)}</b><span class="lineage-arrow" aria-hidden="true">→</span><span>${side(after, 'none after')}</span></nav>`;
  }
  return buildLineageStrip(movement.id, movement);
}

function buildLineageHtml(movementId, movement) {
  return isTradition(movement) ? buildTraditionLineageHtml(movementId, movement) : buildPlainLineageHtml(movementId, movement);
}

const worldsDataDir = path.join(rootDir, 'cic-website/data/worlds');

// A built world with its own compiled orientation.story (cic-website/data/worlds/<id>.json)
// has superseded its census longDescription, and its narration lives in audio/worlds/
// (see tools/generate_world_narration.mjs). The tree page therefore carries no
// description recording for it.
function hasOwnWorldStory(movementId) {
  const dataPath = path.join(worldsDataDir, `${movementId}.json`);
  if (!fs.existsSync(dataPath)) return false;
  const data = JSON.parse(fs.readFileSync(dataPath, 'utf-8'));
  const story = data?.orientation?.story;
  return Array.isArray(story) && story.length > 0;
}

const treeManifestPath = path.join(audioDir, 'manifest.json');
const treeAudioManifest = fs.existsSync(treeManifestPath) ? JSON.parse(fs.readFileSync(treeManifestPath, 'utf-8')) : {};

// A recording's length as m:ss, from its size and the bitrate in its output format.
export function briefClock(rec) {
  if (!rec || !rec.bytes) return '';
  const kbps = Number((/_(\d+)$/.exec(rec.outputFormat || '') || [])[1]) || 64;
  const total = Math.round(rec.bytes * 8 / (kbps * 1000));
  return `${Math.floor(total / 60)}:${String(total % 60).padStart(2, '0')}`;
}

// The Listen player shows only while the recording's stored fingerprint
// matches the text the page now reads.
function hasNarration(movement) {
  if (hasOwnWorldStory(movement.id)) return false;
  return recordingMatchesText(treeAudioManifest[movement.id], narrationTextFor(movement, { dataDir: worldsDataDir }));
}

// Review status (Decision-Log 2026-11-06, ruling 18), in plain words on every page.
const REVIEW_WORDS = {
  'AI-checked': 'checked with AI tools. No scholar or church partner has reviewed it yet.',
  'partner-contributed': 'written with a church partner from this tradition. No scholar has reviewed it yet.',
  'scholar-reviewed': 'reviewed by a scholar.',
};
function reviewLine(movement) {
  const words = REVIEW_WORDS[movement.reviewStatus];
  if (!words) throw new Error(`${movement.id}: unknown reviewStatus ${movement.reviewStatus}`);
  return `<p class="review-status"><b>Review:</b> ${words} <a href="../data.html#review">Help review the tree</a></p>`;
}

// A person entry is told within one tradition, or within none (ruling 14; "The gap sweep
// ruled", 2026-11-09). It carries that tradition's door, shown while the world is open.
function toldWithinLine(movement) {
  if (movement.kind !== 'person') return '';
  const home = movement.toldWithin ? movementMap.get(movement.toldWithin) : null;
  if (!home) return `<p class="told-within">A person whose story no single tradition tells.</p>`;
  return `<p class="told-within">A person. The tradition that tells their story: <a href="${home.id}.html">${escapeHtml(home.name)}</a>.</p>`;
}

const WHO_ENTRIES_ONLY = true;

// A major council's people are its Who click: a person entry links to its page; a named line shows its verdict in plain words.
const VERDICT_WORDS = { WHO: 'Profile to come', STORY: 'Told in a story', LISTED: 'Listed', 'NOT SCORED': 'Not yet assessed' };
function councilPeopleHtml(movement) {
  const items = (movement.people || []).map(p => {
    if (p.person) {
      const who = movementMap.get(p.person);
      return `<li><a href="${who.id}.html">${escapeHtml(who.name)}</a> · ${escapeHtml(p.part)}</li>`;
    }
    return `<li>${escapeHtml(p.name)}<span class="verdict">${escapeHtml(VERDICT_WORDS[p.verdict] || p.verdict)}</span> · ${escapeHtml(p.part)}</li>`;
  });
  if (!items.length) return '';
  return `<h3>Who</h3>
    <ul class="people-list">
${items.join('\n')}
    </ul>`;
}

function peopleHtml(movement) {
  if (movement.kind === 'major-council') return councilPeopleHtml(movement);
  const listed = movement.people || [];
  const people = WHO_ENTRIES_ONLY ? listed.filter(p => p.person) : listed;
  if (!people.length) {
    if (listed.length) return '';
    if (!movement.peopleNote) return '';
    return `<h3>People</h3>
    <p class="people-note">${escapeHtml(movement.peopleNote)}</p>`;
  }
  const items = people.map(p => {
    if (p.person) {
      const who = movementMap.get(p.person);
      return `<li><a href="${who.id}.html">${escapeHtml(who.name)}</a><span class="ident">${escapeHtml(who.dates)}</span></li>`;
    }
    return `<li>${escapeHtml(p.name)}</li>`;
  }).join('\n');
  return `<h3>People</h3>
    <ul class="people-list">
${items}
    </ul>`;
}


function bullets(items) {
  return `<ul>${items.map(t => `<li>${escapeHtml(t)}</li>`).join('')}</ul>`;
}

function sourceLine(s) {
  const meta = [s.author, s.date, s.language].filter(Boolean).map(escapeHtml).join(' · ');
  return `<li>${escapeHtml(s.title)}${meta ? ` — <span class="source-note">${meta}</span>` : ''}${s.disputed ? ` <span class="source-note">(${escapeHtml(s.disputed)})</span>` : ''}</li>`;
}

function sourceGroups(groups, labels) {
  let html = '';
  for (const [key, label] of labels) {
    const list = (groups && groups[key]) || [];
    if (list.length) html += `<p class="source-group">${escapeHtml(label)}</p><ul class="sources-list">${list.map(sourceLine).join('')}</ul>`;
  }
  return html;
}

function factsHtml(rows) {
  const items = rows.filter(([, v]) => v).map(([k, v]) => `<dt>${escapeHtml(k)}</dt><dd>${v}</dd>`);
  return items.length ? `<dl class="facts">${items.join('')}</dl>` : '';
}

// The one control on a page's timeline: open or close every period at once. Without script the periods still open one by one.
const TIMELINE_SCRIPT = "document.querySelectorAll('.tl-all').forEach(function(b){var ps=b.parentNode.querySelectorAll('details.tl-period');b.hidden=false;b.addEventListener('click',function(){var open=[].some.call(ps,function(p){return !p.open;});[].forEach.call(ps,function(p){p.open=open;});b.textContent=open?'Close every period':'Open every period';});});";

// The printed wording behind the brief's quotations and the references the brief draws on, below the brief.
function quotesHtml(card) {
  const qo = card.quotationOriginals || [], refs = card.briefReferences || [];
  if (!qo.length && !refs.length) return '';
  let html = qo.length ? '<p class="quotes-note">Quotations are given in our modern English. The printed wording of each is below.</p>' : '';
  html += '<details class="quotes-panel"><summary>Quotations and references</summary>';
  if (qo.length) html += `<p class="source-group">Quotations</p><ul class="sources-list">${qo.map(e => `<li><span class="source-type">In our modern English</span><br>\u201c${escapeHtml(e.modern)}\u201d<br><span class="source-type">As printed</span><br>\u201c${escapeHtml(e.printed)}\u201d<br><span class="source-note">${escapeHtml(e.work)}</span>${e.uncertain ? `<br><span class="source-note">${escapeHtml(e.uncertain)}</span>` : ''}</li>`).join('')}</ul>`;
  if (refs.length) html += `<p class="source-group">References</p><ul class="sources-list">${refs.map(r => `<li>${escapeHtml(r)}</li>`).join('')}</ul>`;
  return html + '</details>';
}

// An entry's documented stories, each told in full with the printed wording of its quotations, and its recording
// when the docstory manifest holds one made from this text.
function storiesHtml(movement) {
  const stories = movement.documentedStories || [];
  return stories.map((st, i) => {
    const key = `${movement.id}-${i}`;
    const rec = docStoryManifest[key];
    const audio = rec && rec.hash === docStoryFingerprint(st.text)
      ? `<div class="narration"><audio controls preload="none" src="../audio/docstories/${key}.mp3"></audio></div>` : '';
    const text = st.text.split('\n').map(p => p.trim()).filter(p => p).map(p => `<p>${escapeHtml(p)}</p>`).join('');
    return `<h3>${escapeHtml(st.title)}</h3>${audio}<div class="reading">${text}</div>${quotesHtml(st)}`;
  }).join('');
}

// A movement's kind, as the reader sees it. A movement with no kind is a church body and carries no label.
const KIND_LABEL = { 'cross-church movement': 'A movement across churches', 'major-council': 'Major council' };

// The card layout as a page (Stage Two Kit, section 1): the short description, the direct line and the brief,
// with its old sources under it, then the menu in order: Timeline, People and stories, the kind's own sections,
// Connections, Legacy and today, Open questions, Sources with Modern works kept apart. An empty section is left off.
const section = (title, body, id) => body ? `<section${id ? ` id="${id}"` : ''}>
    <h2>${title}</h2>
    ${body}
  </section>` : '';
const sub = (title, body) => body ? `<h3>${title}</h3>${body}` : '';

function briefSourcesHtml(list) {
  if (!list || !list.length) return '';
  return `<div class="brief-sources"><p class="source-group">Old sources for this brief</p><ul class="sources-list">${list.map(s => `<li>${s.author && !String(s.title).startsWith(s.author) ? `${escapeHtml(s.author)}, ` : ''}${escapeHtml(s.title)}</li>`).join('')}</ul></div>`;
}

function modernWorksHtml(list) {
  if (!list || !list.length) return '';
  return `<ul class="sources-list">${list.map(w => {
    const title = w.url ? `<a href="${escapeHtml(w.url)}" target="_blank" rel="noopener noreferrer">${escapeHtml(w.title)}</a>` : escapeHtml(w.title);
    return `<li>${title} — <span class="source-note">${escapeHtml(w.author)}${w.year ? `, ${escapeHtml(w.year)}` : ''}</span>${w.note ? ` <span class="source-note">${escapeHtml(w.note)}</span>` : ''}</li>`;
  }).join('')}</ul>`;
}

// The timeline in periods, each closed until opened, with a control to open them all.
function timelineHtml(periods) {
  if (!periods || !periods.length) return '';
  const line = l => `<li${/^date unknown$/i.test(l.when) ? ' class="undated"' : ''}><span class="tl-when">${escapeHtml(l.when)}</span> ${escapeHtml(l.text)} <span class="source-note">(${escapeHtml(l.reference)})</span>${l.note ? `<span class="tl-note">${escapeHtml(l.note)}</span>` : ''}</li>`;
  return (periods.length > 1 ? '<button type="button" class="tl-all" hidden>Open every period</button>' : '') + periods.map(p =>
    `<details class="tl-period"><summary><span class="tl-pw">${escapeHtml(p.when)}</span> <span class="tl-ph">${escapeHtml(p.headline)}</span></summary>${p.witness ? `<p class="tl-wit">${escapeHtml(p.witness)}</p>` : ''}<ol class="tl">${p.lines.map(line).join('')}</ol></details>`).join('');
}

const COUNCIL_PARTS = ['Gathered', 'Condemned', 'Refused', 'Affected'];

// Each kind's fields, in the card's order.
function cardParts(movement) {
  const isPerson = movement.kind === 'person', isCouncil = movement.kind === 'major-council';
  const card = isPerson ? movement.card || {} : isCouncil ? movement.council || {} : movement;
  const parts = { card, short: card.shortDescription || (isPerson || isCouncil ? card.knownFor : '') || movement.teaser || '', timelineHead: '', people: '', ownTitle: '', own: '', connections: '', legacy: '', questions: '', sources: '' };
  if (isPerson) {
    parts.timelineHead = factsHtml([['Dates', card.datesNote && escapeHtml(card.datesNote)], ['Place', card.placeNote && escapeHtml(card.placeNote)], ['Role', card.role && escapeHtml(card.role)]]);
    parts.ownTitle = 'Key Works';
    parts.own = card.keyWorks && card.keyWorks.length ? `<ul>${card.keyWorks.map(w => `<li><b>${escapeHtml(w.title)}</b>: ${escapeHtml(w.about)}</li>`).join('')}</ul>` : '';
    const councils = census.movements.filter(c => c.kind === 'major-council' && (c.people || []).some(p => p.person === movement.id));
    parts.connections = sub('At Major Councils', councils.length ? `<ul>${councils.map(c => `<li><a href="${c.id}.html">${escapeHtml(c.name)}</a>, ${escapeHtml(c.dates)}: ${escapeHtml(c.people.find(p => p.person === movement.id).part)}</li>`).join('')}</ul>` : '');
    const traces = (card.legacy && card.legacy.traces) || [], remembered = (card.legacy && card.legacy.remembered) || [];
    parts.legacy = sub('What traces to them', traces.length ? bullets(traces) : '') + sub("How they're remembered", remembered.length ? bullets(remembered) : '');
    parts.questions = card.uncertain && card.uncertain.length ? bullets(card.uncertain) : '';
    parts.sources = sourceGroups(card.sources, [['ownWords', 'Their own words'], ['about', 'Written about them']]);
  } else if (isCouncil) {
    const list = items => items && items.length ? bullets(items) : '';
    parts.timelineHead = factsHtml([['Dates', escapeHtml(card.datesNote || movement.dates)], ['Rivers', card.rivers && escapeHtml(card.rivers.join(', '))]]);
    parts.ownTitle = 'What Happened';
    parts.own = sub('Called by', card.calledBy ? `<p>${escapeHtml(card.calledBy)}</p>` : '') + sub('Why They Met', list(card.issue)) + sub('How the Council Worked', list(card.howItWorked)) + sub('What They Decided', list(card.decided));
    if (card.traditions && card.traditions.length) {
      let touched = '';
      for (const part of COUNCIL_PARTS) {
        const group = card.traditions.filter(t => t.part === part);
        if (group.length) touched += `<p class="part-group">${part}</p><ul>${group.map(t => `<li><a href="${t.id}.html">${escapeHtml(t.name)}</a>: ${escapeHtml(t.note)}</li>`).join('')}</ul>`;
      }
      parts.connections = sub('Traditions It Touched', touched);
    }
    parts.legacy = sub('What Came of It', list(card.outcome));
    const record = card.record && card.record.length ? `<ul>${card.record.map(w => `<li><b>${escapeHtml(w.witness)}</b> (${escapeHtml(w.kind)}${w.side ? `, ${escapeHtml(w.side)}` : ''}): ${escapeHtml(w.note)}</li>`).join('')}</ul>` : '';
    parts.questions = sub('What Is Uncertain', list(card.uncertain)) + sub('Whose Account We Have', record);
    parts.sources = sourceGroups(card.sources, [['fromTheCouncil', 'From the council'], ['fromThoseThere', 'From those who were there'], ['writtenLater', 'Written later']]);
  } else {
    parts.connections = (hasContent(movement.relationsSummary) ? sub('In Its Own Record', `<p><i>${escapeHtml(movement.relationsSummary)}</i></p>`) : '') + buildLineageHtml(movement.id, movement);
    const exp = movement.experienceToday && movement.experienceToday.length ? `<ul>${movement.experienceToday.map(e => `<li><a href="${escapeHtml(e.url)}" target="_blank" rel="noopener noreferrer">${escapeHtml(e.text)}</a></li>`).join('')}</ul>` : '';
    parts.legacy = sub('Why It Is on the Tree', movement.why ? `<p>${escapeHtml(movement.why)}</p>` : '') + sub('Legacy', movement.legacy ? paragraphs(movement.legacy) : '') + sub('Experience It Today', exp);
    parts.questions = movement.uncertain && movement.uncertain.length ? bullets(movement.uncertain) : '';
    parts.sources = sub('Doctrinal Floor Note', hasContent(movement.floorNote) ? `<p>${escapeHtml(movement.floorNote)}</p>` : '') + sub('How Sure the Record Is', hasContent(movement.sourcing) ? `<p>${escapeHtml(movement.sourcing)}</p>` : '') + formatSourcesList(movement.sources);
  }
  if (isPerson) parts.connections = (movement.toldWithin && movementMap.get(movement.toldWithin) ? sub('Tradition', `<p><a href="${movement.toldWithin}.html">${escapeHtml(movementMap.get(movement.toldWithin).name)}</a></p>`) : '') + parts.connections + (buildLineageHtml(movement.id, movement) ? sub('Connections on the Map', buildLineageHtml(movement.id, movement)) : '');
  const voices = !isPerson && !isCouncil && movement.voices && movement.voices.length ? bullets(movement.voices) : '';
  parts.people = (isCouncil && card.attended && card.attended.length ? sub('Who Came', bullets(card.attended)) : '') + peopleHtml(movement) + sub('Voices in the Record', voices) + sub('Documented Stories', storiesHtml(movement));
  return parts;
}
const hasContent = v => typeof v === 'string' && v.trim() !== '' && v.trim() !== '-';
const paragraphs = text => text.split('\n').map(p => p.trim()).filter(p => p).map(p => `<p>${escapeHtml(p)}</p>`).join('');

function generatePageHtml(movement) {
  const isPerson = movement.kind === 'person';
  const isCouncil = movement.kind === 'major-council';
  const doorWorld = isCouncil ? null : isPerson ? (movement.toldWithin ? movementMap.get(movement.toldWithin) : null) : movement;
  const parts = cardParts(movement);
  const isBuilt = !!doorWorld && builtWorlds.has(doorWorld.id);
  const narrated = hasNarration(movement);

  // Get description for meta tag - use sourcing as fallback
  const metaDesc = truncateDescription(
    movement.longDescription || movement.sourcing || movement.name,
    160
  );

  // Era info
  const era = census.eras.find(e => e.num === movement.era);
  const eraName = era ? era.title : `Era ${movement.era}`;

  const placeLine = movement.placeLabel ? formatPlace(movement, { today: true }) : '';
  const html = `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>${escapeHtml(movement.name)} — Church Family Tree</title>
<meta name="description" content="${escapeHtml(metaDesc)}">
<meta property="og:title" content="${escapeHtml(movement.name)}">
<meta property="og:description" content="${escapeHtml(metaDesc)}">
<meta property="og:type" content="website">
<meta property="og:url" content="https://www.churchfamilytree.com/tree/${movement.id}">
<meta property="og:image" content="https://www.churchfamilytree.com/share/church-family-tree.jpg">
<link rel="canonical" href="https://www.churchfamilytree.com/tree/${movement.id}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="../assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Alegreya:ital,wght@0,400;0,500;0,700;1,400;1,500&family=Alegreya+Sans:ital,wght@0,400;0,500;0,600;0,700;1,400&display=swap" rel="stylesheet">
${PAGE_STYLE}
<link rel="stylesheet" href="../assets/feedback.css">
${analyticsTag}</head>
<body>
${siteHeader('../')}

<main class="page" id="content">
  <div class="titleblock">
    <p class="ident">${escapeHtml(eraName)} · ${escapeHtml(movement.dates)} · ${escapeHtml(movement.region)}</p>
    ${placeLine.includes('today in') ? `<p class="ident">${escapeHtml(placeLine)}</p>` : ''}
    <h1>${escapeHtml(movement.name)}</h1>
    ${toldWithinLine(movement)}
    ${KIND_LABEL[movement.kind] ? `<p class="kind-label">${escapeHtml(KIND_LABEL[movement.kind])}</p>` : ''}
    ${isPerson && movement.card && movement.card.label ? `<p class="kind-label">${escapeHtml(movement.card.label)}</p>` : ''}
    ${isPerson && parts.card.otherNames ? `<p class="ident">Also called ${parts.card.otherNames.map(o => escapeHtml(typeof o === 'string' ? o : `${o.name} (${o.note})`)).join(', ')}</p>` : ''}
  </div>
  ${parts.short ? `<p class="short-desc">${escapeHtml(parts.short)}</p>` : ''}
  ${directLineHtml(movement)}

  ${isBuilt && doorWorld.publicOpen && conversationsLive ? `
  <div class="action-links">
    <a href="https://churchinconversation.com/traditions/${doorWorld.id}.html">Meet ${escapeHtml(doorWorld.entry?.representativeName || 'this tradition')} on Church in Conversation</a>
  </div>
  ` : isBuilt && doorWorld.publicOpen ? `
  <p class="door-quiet">Conversations with ${escapeHtml(doorWorld.entry?.representativeName || 'this tradition')} are coming soon to Church in Conversation.</p>
  ` : isBuilt && !anyWorldOpen ? `
  <p class="door-quiet"><a href="https://churchinconversation.com/">Church in Conversation</a>, from the same team.</p>
  ` : ''}

  <section>
    <h2>About This ${isCouncil ? 'Council' : isPerson ? 'Person' : 'Movement'}</h2>
    ${narrated ? `
    <div class="narration">
      <p class="narration-label">Audio Brief · Narrated Edition${briefClock(treeAudioManifest[movement.id]) ? ` <span>${briefClock(treeAudioManifest[movement.id])}</span>` : ''}</p>
      <audio controls preload="none" src="../audio/tree/${movement.id}.mp3"></audio>
    </div>
    ` : ''}
    ${movement.longDescription ? `${narrated ? '<details class="read-along"><summary>Read along</summary>' : ''}<div class="reading">${escapeHtml(movement.longDescription).split('\n').map(p => p.trim()).filter(p => p).map(p => `<p>${p}</p>`).join('')}</div>${quotesHtml(parts.card)}${briefSourcesHtml(parts.card.briefSources)}${narrated ? '</details>' : ''}` : (movement.sourcing ? `<p>${escapeHtml(movement.sourcing)}</p>` : '<p>No detailed description available.</p>')}
  </section>

  ${section('Timeline', parts.timelineHead + timelineHtml(parts.card.timeline), 'timeline')}
  ${section('People and Stories', parts.people)}
  ${parts.ownTitle ? section(parts.ownTitle, parts.own) : ''}
  ${section('Connections', parts.connections)}
  ${section('Legacy and Today', parts.legacy)}
  ${section('Open Questions', parts.questions)}
  ${section('Sources', parts.sources + sub('Modern Works', modernWorksHtml(movement.modernWorks)))}

  ${reviewLine(movement)}
</main>

${siteFooter('../')}
${narrated ? '<script src="../assets/narration-player.js" defer></script>\n' : ''}${(parts.card.timeline || []).length > 1 ? `<script>${TIMELINE_SCRIPT}</script>\n` : ''}<script src="../assets/feedback.js" defer></script>
</body>
</html>`;

  return html;
}

// Generate all pages
const pages = [];
let missingFields = [];

census.movements.forEach(movement => {
  const html = generatePageHtml(movement);
  const filepath = path.join(treeDir, `${movement.id}.html`);
  fs.writeFileSync(filepath, html, 'utf-8');

  pages.push({
    id: movement.id,
    name: movement.name,
    status: movement.status
  });

  // Track missing fields
  if (!movement.name) missingFields.push({ id: movement.id, field: 'name' });
  if (!movement.status) missingFields.push({ id: movement.id, field: 'status' });
});


// A movement retired into another keeps its address: its old page goes, and the tree's
// _redirects file sends both forms of the address on, permanently (meta.identifiers).
const redirects = (census.retiredMovements || []).filter(r => r.redirectTo);
for (const r of redirects) fs.rmSync(path.join(treeDir, `${r.id}.html`), { force: true });
fs.writeFileSync(path.join(outRoot, 'cft-website/_redirects'), redirects
  .flatMap(r => [`/tree/${r.id} /tree/${r.redirectTo} 301`, `/tree/${r.id}.html /tree/${r.redirectTo} 301`])
  .map(l => l + '\n').join(''), 'utf-8');

// The tree's own pages: about, method, data, privacy, support
const LONG_DATE = new Intl.DateTimeFormat('en-US', { year: 'numeric', month: 'long', day: 'numeric', timeZone: 'UTC' });
const release = census.meta.release;
if (!release || !Number.isInteger(release.number) || !/^\d{4}-\d{2}-\d{2}$/.test(release.date)) {
  throw new Error('census meta.release needs a whole number and a YYYY-MM-DD date');
}
const releaseDate = LONG_DATE.format(new Date(`${release.date}T00:00:00Z`));
const latestEra = census.eras.reduce((a, b) => (b.num > a.num ? b : a));
function mustFind(list, id, what) {
  const found = list.find(x => x.id === id);
  if (!found) throw new Error(`citation example: no ${what} with ID ${id} in the census`);
  return found;
}
const exampleMovement = mustFind(census.movements, siteContent.citationExamples.movement, 'movement');
const exampleLink = mustFind(census.edges, siteContent.citationExamples.link, 'link');
const nameOf = id => movementMap.get(id).name;
const facts = {
  releaseNumber: String(release.number),
  releaseDate,
  movementCount: String(census.movements.length),
  traditionCount: String(census.movements.filter(m => !m.kind).length),
  riverCount: String(new Set(census.movements.filter(m => !m.kind).map(m => m.laneOrder)).size),
  eraCount: String(census.eras.length),
  toldInFullCount: String(census.movements.filter(m => !m.kind && m.status === 'Built & Live').length),
  linkCount: String(census.edges.length),
  latestEraTitle: latestEra.title,
  latestEraDates: latestEra.dates,
  exampleMovementId: exampleMovement.id,
  exampleMovementName: exampleMovement.name,
  exampleLinkId: exampleLink.id,
  exampleLinkSentence: `${nameOf(exampleLink.from)} ${exampleLink.type} ${nameOf(exampleLink.to)}`,
  exampleLinkGrade: exampleLink.confidence,
  exampleLinkPage: exampleLink.to,
};
function fill(text) {
  return text.replace(/\{\{(\w+)\}\}/g, (_, key) => {
    if (!(key in facts)) throw new Error(`site page text names an unknown fact: ${key}`);
    return facts[key];
  });
}
function linkify(text) {
  return escapeHtml(fill(text))
    .replace(/\[([^\]]+)\]\(([a-z0-9-]+\.html(?:#[a-z0-9-]+)?)\)/g, '<a href="$2">$1</a>')
    .replace(/(?<!href=")(https:\/\/[^\s<]+[^\s<.,;:)])/g, '<a href="$1">$1</a>')
    .replace(/([a-z]+@[a-z.]+\.[a-z]+)/g, '<a href="mailto:$1">$1</a>');
}
const LINE_PATTERNS = { solid: '', 'long-dash': '6,3', 'short-dash': '2,3', dots: '1,4' };
function lineSample(item) {
  if (!item.line) return '';
  const dash = LINE_PATTERNS[item.line.pattern];
  if (dash === undefined) throw new Error(`unknown line pattern: ${item.line.pattern}`);
  const stroke = item.line.color ? `var(--link-${item.line.color})` : 'var(--text)';
  return `<svg width="34" height="10" viewBox="0 0 34 10" aria-hidden="true" focusable="false"><line x1="1" y1="5" x2="33" y2="5" stroke="${stroke}" stroke-width="2"${dash ? ` stroke-dasharray="${dash}"` : ''}/></svg>`;
}
function sectionBody(sec, extra) {
  let html = sec.paragraphs.map(p => `  <p>${linkify(p)}</p>`).join('\n');
  if (sec.list) {
    html += `\n  <ul>\n${sec.list.map(item => `    <li>${linkify(item)}</li>`).join('\n')}\n  </ul>`;
  }
  if (sec.terms) {
    html += `\n  <dl class="terms">\n${sec.terms.map(t => `    <dt>${lineSample(t)}${escapeHtml(fill(t.term))}</dt>\n    <dd>${linkify(t.text)}</dd>`).join('\n')}\n  </dl>`;
  }
  if (sec.citations) {
    html += '\n' + sec.citations.map(c => `  <p class="cite-label">${escapeHtml(fill(c.label))}</p>\n  <p class="cite">${linkify(c.text)}</p>`).join('\n');
  }
  if (sec.after) html += '\n' + sec.after.map(p => `  <p>${linkify(p)}</p>`).join('\n');
  if (sec.extra === 'give') html += '\n' + extra;
  return html;
}
function sitePage(key, extra = '') {
  const page = siteContent[key];
  const body = page.sections.map(sec => `<section${sec.id ? ` id="${sec.id}"` : ''}>
  <h2>${escapeHtml(sec.heading)}</h2>
${sectionBody(sec, extra)}
</section>`).join('\n');
  return `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>${escapeHtml(page.title)} — Church Family Tree</title>
${page.description ? `<meta name="description" content="${escapeHtml(fill(page.description))}">\n` : ''}<link rel="canonical" href="https://www.churchfamilytree.com/${key}">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Alegreya:ital,wght@0,400;0,500;0,700;1,400;1,500&family=Alegreya+Sans:ital,wght@0,400;0,500;0,600;0,700;1,400&display=swap" rel="stylesheet">
${PAGE_STYLE}
<link rel="stylesheet" href="assets/feedback.css">
${analyticsTag}</head>
<body>
${siteHeader('/')}
<main class="page" id="content">
  <div class="titleblock"><h1>${escapeHtml(page.title)}</h1></div>
${body}
</main>
${siteFooter('/')}
<script src="assets/feedback.js" defer></script>
</body>
</html>`;
}
const give = siteContent.give || {};
const giveButtons = give.once && give.monthly
  ? `  <div class="give"><a href="${give.once}">${escapeHtml(give.onceLabel || 'Give once')}</a><a href="${give.monthly}">${escapeHtml(give.monthlyLabel || 'Give monthly')}</a></div>\n`
  : '';
const SITE_PAGES = ['about', 'method', 'data', 'privacy', 'support', 'terms'];
for (const key of SITE_PAGES) {
  fs.writeFileSync(path.join(outRoot, 'cft-website', `${key}.html`), sitePage(key, giveButtons), 'utf-8');
}

// The license policy is one text for both sites. The tree serves its own copy, built from
// cic-website/license.html, so the tree links to its own address and the two copies cannot drift.
function licensePage() {
  const source = fs.readFileSync(path.join(rootDir, 'cic-website/license.html'), 'utf-8');
  const main = source.slice(source.indexOf('<main id="main">') + '<main id="main">'.length, source.indexOf('</main>'));
  const hero = main.match(/<section class="hero"[\s\S]*?<h1>([\s\S]*?)<\/h1>[\s\S]*?<\/section>/);
  const body = main.replace(hero[0], '')
    .replace(/href="(?!https?:|mailto:|#)(?!license\.html|terms\.html)([a-z-]+\.html(?:#[a-z-]+)?)"/g, 'href="https://churchinconversation.com/$1"');
  const description = source.match(/<meta name="description" content="([^"]*)"/)[1];
  return `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>License — Church Family Tree</title>
<meta name="description" content="${description}">
<link rel="canonical" href="https://www.churchfamilytree.com/license">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Alegreya:ital,wght@0,400;0,500;0,700;1,400;1,500&family=Alegreya+Sans:ital,wght@0,400;0,500;0,600;0,700;1,400&display=swap" rel="stylesheet">
${PAGE_STYLE}
<link rel="stylesheet" href="assets/feedback.css">
${analyticsTag}</head>
<body>
${siteHeader('/')}
<main class="page" id="content">
  <div class="titleblock"><p class="eyebrow">License</p><h1>${hero[1].trim()}</h1></div>
${body.trim()}
</main>
${siteFooter('/')}
<script src="assets/feedback.js" defer></script>
</body>
</html>`;
}
fs.writeFileSync(path.join(outRoot, 'cft-website', 'license.html'), licensePage(), 'utf-8');

// The page Cloudflare serves for any address that has no file (wrangler.cft.jsonc, not_found_handling).
// It can be served at any depth, so every link and asset it uses is absolute.
function notFoundPage() {
  return `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Page not found — Church Family Tree</title>
<meta name="robots" content="noindex">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Alegreya:ital,wght@0,400;0,500;0,700;1,400;1,500&family=Alegreya+Sans:ital,wght@0,400;0,500;0,600;0,700;1,400&display=swap" rel="stylesheet">
${PAGE_STYLE}
<link rel="stylesheet" href="/assets/feedback.css">
${analyticsTag}</head>
<body>
${siteHeader('/')}
<main class="page" id="content">
  <div class="titleblock"><h1>Page not found</h1></div>
<section>
  <p>We can’t find that page. It may have moved, or the address may have a typing mistake.</p>
  <p><a href="/">Go to the map</a>, or read <a href="/about">what the tree covers</a>.</p>
</section>
</main>
${siteFooter('/')}
<script src="/assets/feedback.js" defer></script>
</body>
</html>`;
}
fs.writeFileSync(path.join(outRoot, 'cft-website', '404.html'), notFoundPage(), 'utf-8');

// A retired movement with no redirect keeps its address. Its page says only what the census records:
// the name, the date it was retired, and the reason.
function retiredPageHtml(r) {
  const retiredOn = LONG_DATE.format(new Date(`${r.date}T00:00:00Z`));
  return `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>${escapeHtml(r.name)} (retired) — Church Family Tree</title>
<meta name="description" content="${escapeHtml(`This entry was retired from the Church Family Tree on ${retiredOn}.`)}">
<meta name="robots" content="noindex">
<link rel="icon" href="../assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Alegreya:ital,wght@0,400;0,500;0,700;1,400;1,500&family=Alegreya+Sans:ital,wght@0,400;0,500;0,600;0,700;1,400&display=swap" rel="stylesheet">
${PAGE_STYLE}
<link rel="stylesheet" href="../assets/feedback.css">
${analyticsTag}</head>
<body>
${siteHeader('../')}

<main class="page" id="content" data-retired="true">
  <div class="titleblock">
    <p class="eyebrow">Retired entry</p>
    <h1>${escapeHtml(r.name)}</h1>
  </div>
  <p>This entry was retired from the tree on ${escapeHtml(retiredOn)}.</p>
  <p>${escapeHtml(r.reason)}</p>
  <p><a href="../index.html">Return to the map</a></p>
</main>

${siteFooter('../')}
<script src="../assets/feedback.js" defer></script>
</body>
</html>`;
}
for (const r of census.retiredMovements ?? []) {
  if (r.redirectTo) continue;
  if (!r.name || !r.date || !r.reason) throw new Error(`retired movement ${r.id} needs a name, date and reason for its page`);
  fs.writeFileSync(path.join(treeDir, `${r.id}.html`), retiredPageHtml(r), 'utf-8');
}

// Generate sitemap.xml for each site
const sitemapXml = urls => `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${urls.map(url => `  <url>
    <loc>${url}</loc>
  </url>`).join('\n')}
</urlset>`;
const sitemapUrls = [
  'https://churchinconversation.com/',
  'https://churchinconversation.com/index.html',
  'https://churchinconversation.com/about.html',
  'https://churchinconversation.com/support.html',
  'https://churchinconversation.com/license.html',
  'https://churchinconversation.com/terms.html',
  ...Array.from(builtWorlds).map(id => `https://churchinconversation.com/traditions/${id}.html`)
];
fs.writeFileSync(path.join(websiteDir, 'sitemap.xml'), sitemapXml(sitemapUrls), 'utf-8');
const treeSitemapUrls = [
  'https://www.churchfamilytree.com/',
  ...SITE_PAGES.map(key => `https://www.churchfamilytree.com/${key}`),
  'https://www.churchfamilytree.com/license',
  ...census.movements.map(m => `https://www.churchfamilytree.com/tree/${m.id}`)
];
fs.writeFileSync(path.join(outRoot, 'cft-website/sitemap.xml'), sitemapXml(treeSitemapUrls), 'utf-8');

// Generate robots.txt
// Crawlers that gather text to train AI models are asked to stay out, per the
// license policy (cic-website/license.html, "Training AI"). Search engines and
// assistants fetching a page for a person are not training, and stay allowed.
const aiTrainingCrawlers = [
  'GPTBot', 'ClaudeBot', 'anthropic-ai', 'Google-Extended', 'Applebot-Extended',
  'CCBot', 'meta-externalagent', 'Bytespider', 'cohere-training-data-crawler'
];
const robots = `${aiTrainingCrawlers.map(ua => `User-agent: ${ua}\nDisallow: /`).join('\n\n')}

User-agent: *
Allow: /
Sitemap: https://churchinconversation.com/sitemap.xml`;

fs.writeFileSync(path.join(websiteDir, 'robots.txt'), robots, 'utf-8');
fs.writeFileSync(path.join(outRoot, 'cft-website/robots.txt'), robots.replace('https://churchinconversation.com/sitemap.xml', 'https://www.churchfamilytree.com/sitemap.xml'), 'utf-8');

// Report
console.log('\n=== Tree Pages Generation Report ===\n');
console.log(`Generated ${pages.length} pages in ${treeDir}`);
console.log(`Generated sitemap.xml (${sitemapUrls.length} URLs) and the tree's sitemap.xml (${treeSitemapUrls.length} URLs)`);
console.log(`Generated robots.txt`);

if (missingFields.length > 0) {
  console.log(`\nMovements with missing fields:`);
  missingFields.forEach(({ id, field }) => {
    console.log(`  - ${id}: missing ${field}`);
  });
}

console.log('\nDone.');
