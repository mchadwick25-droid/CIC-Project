#!/usr/bin/env node
/**
 * Node CLI wrapper over cic-website/assets/orientation-render.mjs, used by
 * Build/tools/generate_tradition_pages.py so the static tradition-page generator
 * runs the EXACT SAME render functions the Atlas panel imports directly in
 * the browser - one source of truth for world_front-compiled JSON -> HTML,
 * per two surfaces (Website V2 world_front design, site cutover stage).
 *
 * Usage:
 *   node Build/tools/render_orientation_cli.mjs <compiled.json> <slug> <representativeName>
 *
 * Prints a JSON object {sectionName: htmlString, ...} on stdout, one key
 * per exported renderer in orientation-render.mjs plus "questions" (which
 * needs the slug/representative-name context the other renderers don't).
 */
import { readFileSync } from "node:fs";
import {
  RENDERERS,
  renderQuestions,
} from "../cic-website/assets/orientation-render.mjs";

const [, , jsonPath, slug, representativeName] = process.argv;
if (!jsonPath || !slug || !representativeName) {
  console.error("usage: render_orientation_cli.mjs <compiled.json> <slug> <representativeName>");
  process.exit(2);
}

const compiled = JSON.parse(readFileSync(jsonPath, "utf-8"));

// Tradition pages drop the inline "This world's own hedge" callout under
// each Voice (Website V2 world_front card redesign, 2026-09-21: the
// project owner asked that gap/thinness content not be pushed as default
// card reading) - the Atlas panel keeps it, since it imports RENDERERS
// directly in the browser and calls renderVoices(compiled) with no opts,
// which still defaults to showHedge: true. This CLI is the tradition-page
// path only, so this is the one place that default gets overridden.
const out = {};
for (const [name, fn] of Object.entries(RENDERERS)) {
  if (name === "documented_stories") {
    out[name] = fn(compiled, { idPrefix: `${slug}-story` });
  } else if (name === "voices") {
    out[name] = fn(compiled, { showHedge: false });
  } else {
    out[name] = fn(compiled);
  }
}
out.questions = renderQuestions(compiled, { slug, representativeName });

process.stdout.write(JSON.stringify(out));
