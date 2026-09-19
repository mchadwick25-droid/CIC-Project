#!/usr/bin/env node
/**
 * Node CLI wrapper over cic-website/assets/orientation-render.mjs, used by
 * tools/generate_tradition_pages.py so the static tradition-page generator
 * runs the EXACT SAME render functions the Atlas panel imports directly in
 * the browser - one source of truth for world_front-compiled JSON -> HTML,
 * per two surfaces (Website V2 world_front design, site cutover stage).
 *
 * Usage:
 *   node tools/render_orientation_cli.mjs <compiled.json> <slug> <representativeName>
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

const out = {};
for (const [name, fn] of Object.entries(RENDERERS)) {
  out[name] = name === "documented_stories" ? fn(compiled, { idPrefix: `${slug}-story` }) : fn(compiled);
}
out.questions = renderQuestions(compiled, { slug, representativeName });

process.stdout.write(JSON.stringify(out));
