#!/usr/bin/env node
/**
 * Add CSS styling for tree-link to all tradition pages.
 */

import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const rootDir = path.resolve(__dirname, '..', '..');
const traditionsDir = path.join(rootDir, 'cic-website/traditions');

const treeLinkCSS = `.tree-link{font-family:var(--sans);font-size:.95rem;margin:1rem 0;padding:.8rem 1rem;background:var(--surface);border-left:3px solid var(--action);border-radius:4px}
.tree-link a{font-weight:600;color:var(--action)}
.tree-link a:hover{color:var(--action-hover)}`;

// Get all tradition HTML files
const files = fs.readdirSync(traditionsDir).filter(f => f.endsWith('.html'));

files.forEach(file => {
  const filepath = path.join(traditionsDir, file);
  let content = fs.readFileSync(filepath, 'utf-8');

  // Check if CSS already added (look for .tree-link in style tag)
  if (content.includes('.tree-link')) {
    return;
  }

  // Find the closing </style> tag and add before it
  const styleEnd = content.lastIndexOf('</style>');
  if (styleEnd === -1) {
    console.log(`Warning: no </style> tag found in ${file}`);
    return;
  }

  // Add the CSS before the closing tag
  content = content.substring(0, styleEnd) + treeLinkCSS + '\n' + content.substring(styleEnd);

  fs.writeFileSync(filepath, content, 'utf-8');
  console.log(`Added tree-link CSS to ${file}`);
});

console.log('\nDone adding tree-link CSS.');
