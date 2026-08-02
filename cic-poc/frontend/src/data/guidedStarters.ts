/**
 * Typed access to guided_starters.json - the "Don't know what to ask?"
 * content. Static, bundled data (no backend endpoint), so this is a plain
 * lookup module, not an async hook - see useGuidedStarters below for the
 * per-seated-world convenience used by QuestionSheet.
 */

import raw from './guided_starters.json';
import type { GuidedStartersData, GuidedStarterWorld } from '../types/conversation';

const DATA = raw as GuidedStartersData;

const WORLDS_BY_ID = new Map<string, GuidedStarterWorld>(
  DATA.worlds.map((w) => [w.world_id, w])
);

export function getGuidedStartersForWorld(worldId: string): GuidedStarterWorld | undefined {
  return WORLDS_BY_ID.get(worldId);
}

/**
 * Every seated world that has Guided Starters content, in the same order
 * as the table's own world list. A world with no drafted content (e.g.
 * Imperial-Juridical, never in this batch's scope) is silently omitted
 * rather than shown with an empty sheet.
 */
export function getGuidedStartersForTable(worldIds: string[]): GuidedStarterWorld[] {
  return worldIds
    .map((id) => WORLDS_BY_ID.get(id))
    .filter((w): w is GuidedStarterWorld => w !== undefined);
}
