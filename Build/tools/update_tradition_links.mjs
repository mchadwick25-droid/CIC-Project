#!/usr/bin/env node
/**
 * Update the 11 built tradition pages with links to their tree pages.
 * Inserts a link after the title block and before the ai-line.
 */

import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const rootDir = path.resolve(__dirname, '..', '..');
const traditionsDir = path.join(rootDir, 'cic-website/traditions');

const builtWorlds = [
  'alexandria-catechetical',
  'cappadocian-nicene-pastoral-monastic-tradition',
  'desert-monasticism',
  'donatism',
  'gallic-monastic-ascetic-christianity',
  'hieronymian-ascetic-literary',
  'imperial-juridical-christianity',
  'lutheran-wittenberg-and-its-congregations',
  'post-apostolic-house-church',
  'syriac-edessa-nisibis',
  'the-reformed-cities-zurich-and-geneva'
];

const treeLink = `    <p class="tree-link"><a href="../tree/WORLDID.html">View this tradition in the Church Family Tree</a></p>`;

builtWorlds.forEach(worldId => {
  const filepath = path.join(traditionsDir, `${worldId}.html`);

  if (!fs.existsSync(filepath)) {
    console.log(`Warning: ${worldId}.html not found`);
    return;
  }

  let content = fs.readFileSync(filepath, 'utf-8');

  // Check if link already exists
  if (content.includes('tree-link')) {
    console.log(`Skipping ${worldId}: tree link already present`);
    return;
  }

  // Find the ai-line and insert before it
  const aiLinePattern = /(\s*)<p class="ai-line">/;
  const match = content.match(aiLinePattern);

  if (match) {
    const indent = match[1];
    const linkWithIndent = treeLink.replace('WORLDID', worldId).replace(/^    /, indent);
    content = content.replace(aiLinePattern, `${linkWithIndent}\n\n$1<p class="ai-line">`);

    fs.writeFileSync(filepath, content, 'utf-8');
    console.log(`Updated ${worldId}`);
  } else {
    console.log(`Warning: couldn't find ai-line in ${worldId}`);
  }
});

console.log('\nDone updating tradition pages with tree links.');
