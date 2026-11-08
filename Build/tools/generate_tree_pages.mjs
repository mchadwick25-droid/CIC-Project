#!/usr/bin/env node
/**
 * Generate static tree pages for all 292 movements from the census.
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

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const rootDir = path.resolve(__dirname, '..', '..');
const argAt = name => { const i = process.argv.indexOf(name); return i >= 0 ? path.resolve(process.argv[i + 1]) : null; };
const censusPath = argAt('--census') || path.join(rootDir, 'cic-website/data/world-census.json');
const outRoot = argAt('--out') || rootDir;
createRequire(import.meta.url)(path.join(rootDir, 'cic-website/assets/place-line.js'));
const { formatPlace } = globalThis.CFTPlace;
const treeDir = path.join(outRoot, 'cft-website/tree');
const websiteDir = path.join(outRoot, 'cic-website');
const audioDir = path.join(rootDir, 'cft-website/audio/tree');

// Read census data
const census = JSON.parse(fs.readFileSync(censusPath, 'utf-8'));
const anyWorldOpen = census.movements.some(m => m.publicOpen);
const siteContent = JSON.parse(fs.readFileSync(path.join(rootDir, 'Build/tools/tree_site_pages.json'), 'utf-8'));

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
.lineage-section{margin:1.5rem 0;padding-left:.9rem;border-left:3px solid var(--link-contact)}
.lineage-section.link-grow{border-left-color:var(--link-grow)}.lineage-section.link-grow h3{color:var(--link-grow)}
.lineage-section.link-influence{border-left-color:var(--link-influence)}.lineage-section.link-influence h3{color:var(--link-influence)}
.lineage-section.link-conflict{border-left-color:var(--link-conflict)}.lineage-section.link-conflict h3{color:var(--link-conflict)}
.lineage-section.link-contact h3{color:var(--link-contact)}
.lineage-list{list-style:none;padding:0}
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
.narration{display:flex;align-items:center;gap:.6rem;flex-wrap:wrap;margin:1.5rem 0}
.narration audio{display:block;height:2.2rem;max-width:220px;width:220px;flex:0 0 auto}
.narration-disclosure{font-family:var(--sans);font-size:.85rem;color:var(--muted);margin:0}
.action-links{margin:1.5rem 0;padding:1rem;background:var(--surface);border-radius:4px}
.action-links p{margin:0 0 .8rem;font-family:var(--sans);font-size:.95rem}
.action-links a{display:inline-block;padding:.6rem 1rem;background:var(--btn-fill);color:var(--btn-text);text-decoration:none;border-radius:4px;margin-right:.5rem;margin-bottom:.5rem}
.action-links a:hover{background:var(--madder-deep)}
.door-quiet{font-family:var(--sans);font-size:.92rem;color:var(--muted);margin:1.5rem 0}
.site-footer{border-top:1px solid var(--rule);background:var(--surface);font-family:var(--sans);font-size:.85rem;color:var(--muted);margin-top:3rem;padding:1.5rem 1.25rem}
.site-footer .row{max-width:var(--wide);margin:0 auto}
.site-header nav{display:flex;flex-wrap:wrap;gap:.4rem 1rem;align-items:center;margin-left:auto;font-family:var(--sans);font-size:.92rem}
.site-header nav a{color:var(--action);text-decoration:none}
.site-header nav a:hover{color:var(--action-hover)}
.site-footer nav{display:flex;flex-wrap:wrap;gap:.4rem 1.1rem;margin-top:.6rem}
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
  return `<a href="${up}" class="skip-link">Skip to the map</a>

<header class="site-header">
  <div class="row">
    <a href="${up}" class="wordmark">Church Family Tree</a>
    <nav aria-label="Site">
      <a href="https://churchinconversation.com/">Church in Conversation &rarr;</a>
      <a href="${up}support.html">Support the tree</a>
      <button type="button" class="feedback-toggle" id="feedback-toggle" aria-haspopup="dialog" aria-expanded="false">Tell us what you think</button>
    </nav>
  </div>
</header>`;
}

function siteFooter(up) {
  return `<footer class="site-footer">
  <div class="row">
    <p>A Faithways Studio project. The same team makes <a href="https://churchinconversation.com/">Church in Conversation</a>.</p>
    <nav aria-label="About the tree">
      <a href="${up}about.html">About</a>
      <a href="${up}method.html">Method</a>
      <a href="${up}data.html">Data and citation</a>
      <a href="${up}privacy.html">Privacy</a>
      <a href="https://churchinconversation.com/license">License</a>
      <a href="${up}support.html">Support the tree</a>
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
];

// Major links (Decision-Log 2026-11-08): lineage and breaks by type, any other link by its outcome.
const MAJOR_BY_TYPE = new Set(['gave rise to', 'continued as', 'broke with']);
function isMajorEdge(edge) {
  return MAJOR_BY_TYPE.has(edge.type) || (typeof edge.outcome === 'string' && edge.outcome.trim() !== '');
}

function buildLineageHtml(movementId, movement) {
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

function hasNarration(movementId) {
  if (hasOwnWorldStory(movementId)) return false;
  return Boolean(treeAudioManifest[movementId]);
}

function generatePageHtml(movement) {
  const isBuilt = builtWorlds.has(movement.id);
  const narrated = hasNarration(movement.id);

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
<meta property="og:image" content="https://churchinconversation.com/assets/og-image.jpg">
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

<div class="page">
  <div class="titleblock">
    <p class="ident">${escapeHtml(eraName)} · ${escapeHtml(movement.dates)} · ${escapeHtml(movement.region)}</p>
    ${placeLine.includes('today in') ? `<p class="ident">${escapeHtml(placeLine)}</p>` : ''}
    <h1>${escapeHtml(movement.name)}</h1>
  </div>

  ${isBuilt && movement.publicOpen ? `
  <div class="action-links">
    <a href="https://churchinconversation.com/traditions/${movement.id}.html">Meet ${escapeHtml(movement.entry?.representativeName || 'this tradition')} on Church in Conversation</a>
  </div>
  ` : isBuilt && !anyWorldOpen ? `
  <p class="door-quiet"><a href="https://churchinconversation.com/">Church in Conversation</a>, from the same team.</p>
  ` : ''}

  <section>
    <h2>About This Movement</h2>
    ${narrated ? `
    <div class="narration">
      <audio controls preload="none" src="../audio/tree/${movement.id}.mp3"></audio>
      <p class="narration-disclosure">Synthesized voice — not a recording.</p>
    </div>
    ` : ''}
    ${movement.longDescription ? `<div class="reading">${escapeHtml(movement.longDescription).split('\n').map(p => p.trim()).filter(p => p).map(p => `<p>${p}</p>`).join('')}</div>` : (movement.sourcing ? `<p>${escapeHtml(movement.sourcing)}</p>` : '<p>No detailed description available.</p>')}
  </section>

  <section>
    <h2>In Its Own Record</h2>
    ${buildLineageHtml(movement.id, movement)}
  </section>

  <section>
    <h2>Sources</h2>
    ${formatSourcesList(movement.sources)}
  </section>
</div>

${siteFooter('../')}
${narrated ? '<script src="../assets/narration-player.js" defer></script>\n' : ''}<script src="../assets/feedback.js" defer></script>
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
${page.description ? `<meta name="description" content="${escapeHtml(fill(page.description))}">\n` : ''}<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Alegreya:ital,wght@0,400;0,500;0,700;1,400;1,500&family=Alegreya+Sans:ital,wght@0,400;0,500;0,600;0,700;1,400&display=swap" rel="stylesheet">
${PAGE_STYLE}
<link rel="stylesheet" href="assets/feedback.css">
${analyticsTag}</head>
<body>
${siteHeader('/')}
<div class="page">
  <div class="titleblock"><h1>${escapeHtml(page.title)}</h1></div>
${body}
</div>
${siteFooter('/')}
<script src="assets/feedback.js" defer></script>
</body>
</html>`;
}
const give = siteContent.give || {};
const giveButtons = give.once && give.monthly
  ? `  <div class="give"><a href="${give.once}">Give once</a><a href="${give.monthly}">Give monthly</a></div>\n`
  : '';
const SITE_PAGES = ['about', 'method', 'data', 'privacy', 'support'];
for (const key of SITE_PAGES) {
  fs.writeFileSync(path.join(outRoot, 'cft-website', `${key}.html`), sitePage(key, giveButtons), 'utf-8');
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
  ...Array.from(builtWorlds).map(id => `https://churchinconversation.com/traditions/${id}.html`)
];
fs.writeFileSync(path.join(websiteDir, 'sitemap.xml'), sitemapXml(sitemapUrls), 'utf-8');
const treeSitemapUrls = [
  'https://www.churchfamilytree.com/',
  ...SITE_PAGES.map(key => `https://www.churchfamilytree.com/${key}.html`),
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
