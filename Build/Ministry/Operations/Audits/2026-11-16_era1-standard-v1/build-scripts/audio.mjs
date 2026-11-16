import { requestTextFor } from '/home/user/CIC-Project/Build/tools/generate_tree_narration.mjs';
import { readFileSync, writeFileSync, readdirSync } from 'node:fs';
const base = '/home/user/CIC-Project/Build/Ministry/Features/Church-Family-Tree/';
const dirs = ['Who-Profiles/era1/batch1','Who-Profiles/era1/batch2','Who-Profiles/era1/batch3','Council-Profiles/era1'];
for (const d of dirs) for (const f of readdirSync(base + d).filter(f => f.endsWith('.brief.txt'))) {
  const t = readFileSync(base + d + '/' + f, 'utf8').trim();
  const out = requestTextFor(t, { openTag: '[calmly]', closingTag: '[warmly]' });
  writeFileSync(base + d + '/audio/' + f.replace('.brief.txt', '.audio.txt'), out + '\n');
}
console.log('done');
