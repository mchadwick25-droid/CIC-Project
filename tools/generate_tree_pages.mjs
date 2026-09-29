#!/usr/bin/env node
/**
 * Generate static tree pages for all 292 movements from the census.
 *
 * Output: 292 HTML files at cic-website/tree/<slug>.html
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

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const rootDir = path.resolve(__dirname, '..');
const censusPath = path.join(rootDir, 'cic-website/data/world-census.json');
const treeDir = path.join(rootDir, 'cic-website/tree');
const websiteDir = path.join(rootDir, 'cic-website');
const audioDir = path.join(rootDir, 'cic-website/audio/tree');

// Read census data
const census = JSON.parse(fs.readFileSync(censusPath, 'utf-8'));

// Ensure tree directory exists
if (!fs.existsSync(treeDir)) {
  fs.mkdirSync(treeDir, { recursive: true });
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

function buildLineageHtml(movementId, movement) {
  let html = '';

  // Edges going in (what formed this)
  const parentsEdges = edgesTo.get(movementId) || [];
  if (parentsEdges.length > 0) {
    html += '<div class="lineage-section">\n';
    html += '<h3>Formed From</h3>\n<ul class="lineage-list">\n';
    parentsEdges.forEach(edge => {
      const parent = movementMap.get(edge.from);
      if (parent) {
        html += `<li><a href="${parent.id}.html">${escapeHtml(parent.name)}</a>`;
        if (edge.note) {
          html += ` — <span class="confidence-note">${escapeHtml(edge.note)}</span>`;
        }
        html += '</li>\n';
      }
    });
    html += '</ul>\n</div>\n';
  }

  // Edges going out (what it formed/influenced)
  const childrenEdges = edgesFrom.get(movementId) || [];
  if (childrenEdges.length > 0) {
    html += '<div class="lineage-section">\n';
    html += '<h3>Formed or Influenced</h3>\n<ul class="lineage-list">\n';
    childrenEdges.forEach(edge => {
      const child = movementMap.get(edge.to);
      if (child) {
        html += `<li><a href="${child.id}.html">${escapeHtml(child.name)}</a>`;
        if (edge.note) {
          html += ` — <span class="confidence-note">${escapeHtml(edge.note)}</span>`;
        }
        html += '</li>\n';
      }
    });
    html += '</ul>\n</div>\n';
  }

  return html;
}

const worldsDataDir = path.join(rootDir, 'cic-website/data/worlds');

// A built world with its own compiled orientation.story (cic-website/data/worlds/<id>.json)
// has superseded its census longDescription - see tools/generate_tree_narration.mjs's own
// narrationTextFor(). The committed audio for these still narrates the old longDescription
// text, not narrationTextFor()'s current text, so the page here shows no narration for them
// until they're re-narrated on the correct text - a mismatched player is worse than none.
function hasMismatchedNarration(movementId) {
  const dataPath = path.join(worldsDataDir, `${movementId}.json`);
  if (!fs.existsSync(dataPath)) return false;
  const data = JSON.parse(fs.readFileSync(dataPath, 'utf-8'));
  const story = data?.orientation?.story;
  return Array.isArray(story) && story.length > 0;
}

function hasNarration(movementId) {
  if (hasMismatchedNarration(movementId)) return false;
  return fs.existsSync(path.join(audioDir, `${movementId}.mp3`));
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

  // Status label
  const statusMeta = census.statusMeta[movement.status];
  const statusLabel = statusMeta ? statusMeta.shortWord : movement.status;
  const statusDesc = statusMeta ? statusMeta.description : '';

  const html = `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>${escapeHtml(movement.name)} — Church in Conversation</title>
<meta name="description" content="${escapeHtml(metaDesc)}">
<meta property="og:title" content="${escapeHtml(movement.name)}">
<meta property="og:description" content="${escapeHtml(metaDesc)}">
<meta property="og:type" content="website">
<meta property="og:url" content="https://churchinconversation.com/tree/${movement.id}.html">
<meta property="og:image" content="https://churchinconversation.com/assets/atlas-preview.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="../assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Alegreya:ital,wght@0,400;0,500;0,700;1,400;1,500&family=Alegreya+Sans:ital,wght@0,400;0,500;0,600;0,700;1,400&display=swap" rel="stylesheet">
<style>
:root{
  --parchment:#F6F6F2; --vellum:#FFFFFF;
  --ink:#2A2521; --ink-faded:#6C6257; --madder:#A13E2B; --madder-deep:#7E2F20;
  --tyrian:#6B3FA0; --graphite:#8A837C; --rule:rgba(241,233,221,.16);
  --ground:#17130F; --surface:#1E1913;
  --text:#F1E9DD; --muted:#B8AEA1;
  --action:#E08C74; --action-hover:#F0A98F;
  --control:#A39B92;
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
.page{max-width:var(--col);margin:0 auto;padding:2rem 1.25rem}
.titleblock{margin-bottom:2rem}
.ident{font-family:var(--sans);font-size:.9rem;color:var(--muted);margin:0 0 .5rem}
.status-label{font-family:var(--sans);font-size:.95rem;color:var(--action);margin:1rem 0}
.meta-grid{display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin:1.5rem 0}
@media (max-width:640px){.meta-grid{grid-template-columns:1fr}}
.meta-item{padding:.8rem;background:var(--surface);border-radius:4px}
.meta-label{font-family:var(--sans);font-size:.8rem;text-transform:uppercase;letter-spacing:.1em;color:var(--muted);margin:0}
.meta-value{font-family:var(--serif);font-size:1.1rem;color:var(--text);margin:.3rem 0 0}
.lineage-section{margin:1.5rem 0}
.lineage-list{list-style:none;padding:0}
.lineage-list li{margin:0 0 .5rem;padding:0}
.lineage-list a{color:var(--action)}
.confidence-note{font-style:italic;color:var(--muted);font-size:.95rem}
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
.site-footer{border-top:1px solid var(--rule);background:var(--surface);font-family:var(--sans);font-size:.85rem;color:var(--muted);margin-top:3rem;padding:1.5rem 1.25rem}
.site-footer .row{max-width:var(--wide);margin:0 auto}
</style>
</head>
<body>
<a href="../index.html" class="skip-link">Skip to home</a>

<header class="site-header">
  <div class="row">
    <a href="../index.html" class="wordmark">Church <em>in</em> Conversation</a>
  </div>
</header>

<div class="page">
  <div class="titleblock">
    <p class="ident">${escapeHtml(eraName)} · ${escapeHtml(movement.dates)} · ${escapeHtml(movement.region)}</p>
    <h1>${escapeHtml(movement.name)}</h1>
    <div class="status-label">
      <strong>${escapeHtml(statusLabel)}</strong>
      ${statusDesc ? `<p style="font-size: 0.95rem; color: var(--muted); margin: 0.5rem 0 0;">${escapeHtml(statusDesc)}</p>` : ''}
    </div>
  </div>

  <div class="meta-grid">
    <div class="meta-item">
      <p class="meta-label">Era</p>
      <p class="meta-value">${escapeHtml(eraName)}</p>
    </div>
    <div class="meta-item">
      <p class="meta-label">Time Period</p>
      <p class="meta-value">${escapeHtml(movement.dates)}</p>
    </div>
    <div class="meta-item">
      <p class="meta-label">Region</p>
      <p class="meta-value">${escapeHtml(movement.region)}</p>
    </div>
    <div class="meta-item">
      <p class="meta-label">Status</p>
      <p class="meta-value">${escapeHtml(statusLabel)}</p>
    </div>
  </div>

  ${isBuilt ? `
  <div class="action-links">
    <p><strong>Visit this tradition:</strong></p>
    <a href="../traditions/${movement.id}.html">Read the Story</a>
    <a href="../talk.html?worlds=${movement.id}&mode=interview&from=tree%2F${movement.id}.html">Have a Conversation</a>
  </div>
  ` : ''}

  <section>
    <h2>About This Movement</h2>
    ${narrated ? `
    <div class="narration">
      <audio controls preload="none">
        <source src="../audio/tree/${movement.id}.mp3" type="audio/mpeg">
      </audio>
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

<footer class="site-footer">
  <div class="row">
    <p>&copy; 2026 Church in Conversation. A safe space to explore faith and the story of Jesus, part of Faithways Studio, Inc.</p>
  </div>
</footer>
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

// Generate sitemap.xml
const sitemapUrls = [
  'https://churchinconversation.com/',
  'https://churchinconversation.com/index.html',
  'https://churchinconversation.com/about.html',
  'https://churchinconversation.com/support.html',
  'https://churchinconversation.com/atlas.html',
  ...Array.from(builtWorlds).map(id => `https://churchinconversation.com/traditions/${id}.html`),
  ...census.movements.map(m => `https://churchinconversation.com/tree/${m.id}.html`)
];

const sitemap = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${sitemapUrls.map(url => `  <url>
    <loc>${url}</loc>
  </url>`).join('\n')}
</urlset>`;

fs.writeFileSync(path.join(websiteDir, 'sitemap.xml'), sitemap, 'utf-8');

// Generate robots.txt
const robots = `User-agent: *
Allow: /
Sitemap: https://churchinconversation.com/sitemap.xml`;

fs.writeFileSync(path.join(websiteDir, 'robots.txt'), robots, 'utf-8');

// Report
console.log('\n=== Tree Pages Generation Report ===\n');
console.log(`Generated ${pages.length} pages in ${treeDir}`);
console.log(`Generated sitemap.xml (${sitemapUrls.length} URLs)`);
console.log(`Generated robots.txt`);

if (missingFields.length > 0) {
  console.log(`\nMovements with missing fields:`);
  missingFields.forEach(({ id, field }) => {
    console.log(`  - ${id}: missing ${field}`);
  });
}

// Status label strings used
const statusLabels = new Set();
census.movements.forEach(m => {
  if (census.statusMeta[m.status]) {
    statusLabels.add(census.statusMeta[m.status].shortWord);
  }
});

console.log(`\nStatus label strings used (${statusLabels.size} unique):`);
Array.from(statusLabels).sort().forEach(label => {
  console.log(`  - "${label}"`);
});

console.log('\nDone.');
