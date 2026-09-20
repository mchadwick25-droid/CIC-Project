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
// without a portrait. Eleven formation worlds as of 2026-09-20 (witt added
// once its own package was admitted; its Representative portrait, Nikolaus
// - approved 2026-09-19, "lock it in" - Mark placed into GitHub as
// nikolaus.jpg, per site-portrait/witt's own now-CLOSED cross_world entry;
// copied here to match, since this file previously pointed at nikolaus.png,
// which was never the real file's own extension).
export const WORLD_ORDER = ['alx', 'pahc', 'desert', 'hal', 'syr', 'ijc', 'cappadocian', 'gallic', 'don', 'rzg', 'witt'];

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
  // Tenth world, admitted 2026-09-18. No light-mode legacy value - added after the
  // 2026-09-17 dark-mode-only migration, so computed directly for the dark ground.
  // Hue/saturation grounded in this world's own repeated austerity/subtraction theme
  // (the silenced Zurich organ, the plain black gown, worship built around subtraction
  // rather than ornament - Doc_07 SS5's "subtraction, not addition" formation logic) -
  // a restrained, cool charcoal-slate (H=240deg), deliberately the fleet's lowest
  // saturation (12%, below gallic's own 14.9%, the next-quietest) while still reading
  // as a distinct accent rather than plain grey. Script-computed: L=58.1% is the first
  // point clearing >=5.0:1 against BOTH the dark ground (5.31:1) and --color-surface as
  // dark text laid on top of it as a fill (5.01:1) simultaneously - matching don's own
  // >=5.3:1/>=5.0:1 margin pattern. Checked against every value above and the two
  // reserved semantic tokens (--color-tyrian #6B3FA0, --color-participant/"lapis"
  // #1E40AF) for hue distance; nearest neighbor is lapis at 14.1deg, low collision risk
  // given the near-fourfold saturation gap between them.
  rzg: { portraitImage: '/images/portraits/theophilus.jpg', accentColor: '#8787A1' },
  // Eleventh world, admitted 2026-09-20. Reuses the accent color already fixed for this world in
  // cic-website/table.html rather than picking a new one - #579C40, a moderate forest green.
  // Script-computed just now against this file's own two dark-mode thresholds: 5.49:1 vs the dark
  // ground #17130F (clears >=5.3:1) and 5.18:1 vs --color-surface #1E1913 as dark text on top of it
  // as a fill (clears >=5.0:1) - both actually verified here, not assumed from table.html's own
  // prior use of the same hex value.
  witt: { portraitImage: '/images/portraits/nikolaus.jpg', accentColor: '#579C40' },
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
