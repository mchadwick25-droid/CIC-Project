import { test } from 'node:test';
import assert from 'node:assert/strict';
import fs from 'fs';
import path from 'path';
import { spawnSync } from 'child_process';
import { fileURLToPath } from 'url';

// Each narration script, run for real but without --approved-run and
// --char-cap, must stop at the gate. The key is a placeholder and fetch is
// replaced with one that fails the test, so the run can reach no service.
const toolsDir = path.dirname(fileURLToPath(import.meta.url));
const worldsDir = path.join(toolsDir, '../../cic-website/data/worlds');
const firstWorld = fs.readdirSync(worldsDir).find((f) => f.endsWith('.json')).replace('.json', '');
const noNetwork = 'data:text/javascript,globalThis.fetch=()=>{console.error("NETWORK CALL ATTEMPTED");process.exit(99)};';
const paid = ['--voice-id', 'v', '--model', 'm'];

const scripts = [
  ['generate_tree_narration.mjs', [...paid, '--force', '--limit', '1']],
  ['generate_docstory_narration.mjs', [...paid, '--output-format', 'mp3_44100_64', '--force', '--limit', '1']],
  ['generate_site_narration.mjs', [...paid, '--output-format', 'mp3_44100_64', '--settings-json', '{}', '--force']],
  ['generate_world_narration.mjs', [...paid, '--world', firstWorld, '--api-speed', '1', '--tempo', '1', '--settings-json', '{}', '--force']],
];

function run(script, args) {
  return spawnSync(process.execPath, ['--import', noNetwork, path.join(toolsDir, script), ...args], {
    encoding: 'utf-8',
    env: { ...process.env, ELEVENLABS_API_KEY: 'placeholder-not-a-key' },
  });
}

for (const [script, args] of scripts) {
  test(`${script}: without --approved-run it stops before any request`, () => {
    const r = run(script, args);
    assert.notEqual(r.status, 0);
    assert.notEqual(r.status, 99, r.stderr);
    assert.match(r.stderr, /--approved-run "<name>" is required/);
    assert.doesNotMatch(r.stdout, /PAID RUN/);
  });

  test(`${script}: without --char-cap it stops before any request`, () => {
    const r = run(script, [...args, '--approved-run', 'r']);
    assert.notEqual(r.status, 0);
    assert.notEqual(r.status, 99, r.stderr);
    assert.match(r.stderr, /--char-cap <n> is required/);
    assert.doesNotMatch(r.stdout, /PAID RUN/);
  });

  test(`${script}: over its cap it stops before any request`, () => {
    const r = run(script, [...args, '--approved-run', 'r', '--char-cap', '1']);
    assert.notEqual(r.status, 0);
    assert.notEqual(r.status, 99, r.stderr);
    assert.match(r.stderr, /over its --char-cap of 1/);
    assert.doesNotMatch(r.stdout, /PAID RUN/);
  });
}
