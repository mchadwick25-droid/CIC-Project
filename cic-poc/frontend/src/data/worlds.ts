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
// without a portrait. Nine formation worlds as of 2026-09-16 (don added
// once Mark flipped it open and its own Representative portrait, Fidelis
// - approved 2026-09-10, sitting unshipped in Brand-Assets since - was
// finally wired to the two live-serving asset locations).
export const WORLD_ORDER = ['alx', 'pahc', 'desert', 'hal', 'syr', 'ijc', 'cappadocian', 'gallic', 'don'];

// 2026-09-17 dark-mode change order: every accentColor below was lightened
// from its original Stage 7.5 light-mode hex (kept in each comment for
// provenance/hue reasoning) to clear WCAG AA against the app's new dark
// background (#17130F) in both of its actual uses - as text
// (.turn__speaker, .arrival__seat-detail) and as a button/swatch fill
// with dark text on top (.world-card__interview, .arrival__seat-portrait).
// Script-computed, not eyeballed: every value here measures >=5.3:1 as
// text on the dark ground and >=5.0:1 for dark surface-text laid on top
// of it as a fill. Hue and relative saturation preserved from the
// original pick in each case, only lightness raised.
export const WORLD_ASSETS: Record<string, WorldAssets> = {
  // was #B45309 (gold-leaf itself - now reserved separately for
  // --color-representative's own dark-safe value, #DC9A3E, so this needed
  // to move to stay distinct from it too).
  alx: { portraitImage: '/images/portraits/alexandria.png', accentColor: '#DE670B' },
  pahc: { portraitImage: '/images/portraits/house-churches.png', accentColor: '#439975' },
  desert: { portraitImage: '/images/portraits/desert.png', accentColor: '#9D893B' },
  hal: { portraitImage: '/images/portraits/bethlehem.png', accentColor: '#B77889' },
  syr: { portraitImage: '/images/portraits/syriac.png', accentColor: '#5493A0' },
  ijc: { portraitImage: '/images/portraits/empire.png', accentColor: '#B67D50' },
  // Seventh world, added 2026-09-01 once Chilo's portrait was locked (Mark: "yes, lock it in").
  // Light-mode color was #A0522D (a warm sienna/terracotta, echoing the loaf's own baked crust) -
  // checked against every color above and the two reserved semantic tokens (--color-tyrian
  // #6B3FA0, the lexicon/transparency apparatus's own pigment; --color-participant/"lapis"
  // #1E40AF) for a distinct hue.
  cappadocian: { portraitImage: '/images/portraits/cappadocian.jpg', accentColor: '#CB7247' },
  // Eighth world, added 2026-09-13 once Renatus's portrait was locked (Mark: "yes, lock it in").
  // Light-mode color was #5A6B74 (a cool slate blue-grey, grounded in this world's own repeated
  // cold-of-Gaul theme) - checked against every color above and the two reserved semantic tokens
  // for a distinct hue and temperature (per gallic_Representative_Portrait_Grounding_Brief.md).
  gallic: { portraitImage: '/images/portraits/gallic.jpg', accentColor: '#798D97' },
  // Ninth world, re-admitted 2026-09-17. Light-mode color was #6A2525 (a deep oxblood/martyrdom
  // red, grounded in this world's own martyrs'-graves-read-aloud practice and the Deo laudes
  // acclamation) - checked against every color above and the two reserved semantic tokens for a
  // distinct hue; the nearest neighbor is hal's own muted rose, 16 degrees away in hue, same
  // margin as the original light-mode pick. Script-computed for this same 2026-09-17 dark-mode
  // pass (don wasn't live yet when the rest of the fleet went through it): H/S held from the
  // light-mode value, L raised to 61.8% - the first point clearing both thresholds (>=5.3:1 vs
  // the dark ground, >=5.07:1 vs --color-surface #1E1913 as dark text on top of it as a fill).
  don: { portraitImage: '/images/portraits/donatism.png', accentColor: '#CD6F6F' },
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
