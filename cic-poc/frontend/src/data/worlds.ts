/**
 * The six seated worlds' front-end-only assets - portrait image and accent
 * color, neither of which the registry carries (records/worlds.yaml has no
 * per-world color; portraits are static files already wired for the old
 * World Selector, reused as-is). Everything else about a world - display
 * name, representative, period, place, thinness statement, doorway description, starter
 * questions - now comes from GET /api/worlds (see hooks/useWorlds.ts),
 * which reads it straight from the compiled package rather than a
 * hand-copied second version of the registry. That second copy is exactly
 * what this file used to be, and exactly what its own comment used to
 * admit: "No /api/worlds endpoint exists yet, so this is baked in at build
 * time... nothing here is invented copy." The endpoint exists now.
 *
 * Accent colors match the ones fixed in the Stage 7.5 design canvas review
 * (2026-08-24): the registry itself names no per-world color, and five of
 * six first-draft picks collided with reserved semantic tokens (lapis,
 * tyrian) or were invented off-palette hues.
 */
export interface WorldAssets {
  portraitImage: string;
  accentColor: string;
}

// Display order on the world-list screen, fixed since Stage 7.5 - not the
// registry's own file order (which interleaves desert and pahc
// differently). A world_key GET /api/worlds returns that isn't listed here
// has no known assets yet and is left off the list rather than shown
// without a portrait - there are exactly six formation worlds today.
export const WORLD_ORDER = ['alx', 'pahc', 'desert', 'hal', 'syr', 'ijc'];

export const WORLD_ASSETS: Record<string, WorldAssets> = {
  alx: { portraitImage: '/images/portraits/alexandria.png', accentColor: '#B45309' },
  pahc: { portraitImage: '/images/portraits/house-churches.png', accentColor: '#2F6B52' },
  desert: { portraitImage: '/images/portraits/desert.png', accentColor: '#7A6A2E' },
  hal: { portraitImage: '/images/portraits/bethlehem.png', accentColor: '#8C4A5C' },
  syr: { portraitImage: '/images/portraits/syriac.png', accentColor: '#3D6B75' },
  ijc: { portraitImage: '/images/portraits/empire.png', accentColor: '#7A5233' },
};

export interface WorldStarter {
  cell: string;
  text: string;
}

export interface WorldEntry {
  worldKey: string;
  censusId: string | null;
  displayName: string; // scholarly name ("to show rigor")
  cardName: string; // friendly name ("the right picture in their mind")
  representativeName: string;
  roleLabel: string;
  place: string;
  eraStart: number;
  eraEnd: number;
  thinnessStatement: string;
  // Plain-English doorway paragraph (registry-owned; the API's model-facing
  // horizon is folded in as the fallback at the useWorlds mapping).
  doorwayDescription: string | null;
  livingTraditionFlag: boolean;
  starters: WorldStarter[];
  portraitImage: string;
  accentColor: string;
}

export function findWorld(worlds: WorldEntry[], worldKey: string): WorldEntry | undefined {
  return worlds.find((w) => w.worldKey === worldKey);
}

export function findWorldByCensusId(worlds: WorldEntry[], censusId: string): WorldEntry | undefined {
  return worlds.find((w) => w.censusId === censusId);
}
