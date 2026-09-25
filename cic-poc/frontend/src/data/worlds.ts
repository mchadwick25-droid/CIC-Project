/**
 * The eleven seated worlds' front-end-only assets - portrait image and
 * accent color, neither of which the registry carries (records/worlds.yaml
 * has no per-world color; portraits are static files already wired for the
 * old World Selector, reused as-is). Everything else about a world -
 * display name, representative, period, place, thinness statement, doorway
 * description, starter questions - comes from GET /api/worlds (see
 * hooks/useWorlds.ts), which reads it straight from the compiled package.
 *
 * Accent colors: the registry itself names no per-world color, so each is
 * picked here, checked against every other world's own color and the two
 * reserved semantic tokens (lapis, tyrian) to avoid a collision or an
 * invented off-palette hue.
 */
export interface WorldAssets {
  portraitImage: string;
  accentColor: string;
}

// Display order on the world-list screen - not the
// registry's own file order (which interleaves desert and pahc
// differently). A world_key GET /api/worlds returns that isn't listed here
// has no known assets yet and is left off the list rather than shown
// without a portrait. witt's Representative portrait, Nikolaus,
// lives in GitHub as nikolaus.jpg.
export const WORLD_ORDER = ['alx', 'pahc', 'desert', 'hal', 'syr', 'ijc', 'cappadocian', 'gallic', 'don', 'rzg', 'witt', 'lpc'];

// Every accentColor below is a lightened variant of the hue each per-world
// comment grounds (kept there for provenance/hue reasoning), raised to
// clear WCAG AA against the app's dark background (#17130F) in both of
// its actual uses - as text (.turn__speaker, .arrival__seat-detail) and
// as a button/swatch fill with dark text on top (.world-card__interview,
// .arrival__seat-portrait). Script-computed, not eyeballed: every value
// here measures >=5.3:1 as text on the dark ground and >=5.0:1 for dark
// surface-text laid on top of it as a fill. Hue and relative saturation
// are preserved from each grounding pick, only lightness raised.
export const WORLD_ASSETS: Record<string, WorldAssets> = {
  // Stays distinct from gold-leaf and from --color-representative's own
  // reserved dark-safe value (#DC9A3E).
  alx: { portraitImage: '/images/portraits/alexandria.png', accentColor: '#DE670B' },
  pahc: { portraitImage: '/images/portraits/house-churches.png', accentColor: '#439975' },
  desert: { portraitImage: '/images/portraits/desert.png', accentColor: '#9D893B' },
  hal: { portraitImage: '/images/portraits/bethlehem.png', accentColor: '#B77889' },
  syr: { portraitImage: '/images/portraits/syriac.png', accentColor: '#5493A0' },
  ijc: { portraitImage: '/images/portraits/empire.png', accentColor: '#B67D50' },
  // Hue grounded in #A0522D (a warm sienna/terracotta, echoing the loaf's own baked crust) -
  // checked against every color above and the two reserved semantic tokens (--color-tyrian
  // #6B3FA0, the lexicon/transparency apparatus's own pigment; --color-participant/"lapis"
  // #1E40AF) for a distinct hue.
  cappadocian: { portraitImage: '/images/portraits/cappadocian.jpg', accentColor: '#CB7247' },
  // Hue grounded in #5A6B74 (a cool slate blue-grey, this world's own repeated
  // cold-of-Gaul theme) - checked against every color above and the two reserved semantic tokens
  // for a distinct hue and temperature (per gallic_Representative_Portrait_Grounding_Brief.md).
  gallic: { portraitImage: '/images/portraits/gallic.jpg', accentColor: '#798D97' },
  // Hue grounded in #6A2525 (a deep oxblood/martyrdom
  // red, this world's own martyrs'-graves-read-aloud practice and the Deo laudes
  // acclamation) - checked against every color above and the two reserved semantic tokens for a
  // distinct hue; the nearest neighbor is hal's own muted rose, 16 degrees away in hue.
  // H/S held from the grounding value, L raised to 61.8% - the first point clearing both
  // thresholds (>=5.3:1 vs the dark ground, >=5.07:1 vs --color-surface #1E1913 as dark
  // text on top of it as a fill).
  don: { portraitImage: '/images/portraits/donatism.png', accentColor: '#CD6F6F' },
  // No light-mode-derived hue for this world; computed directly for the
  // dark ground. Hue/saturation grounded in this world's own repeated austerity/subtraction theme
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
  // Reuses the accent color already fixed for this world in
  // cic-website/table.html rather than picking a new one - #579C40, a moderate forest green.
  // Verified against this file's own two dark-mode thresholds: 5.49:1 vs the dark
  // ground #17130F (clears >=5.3:1) and 5.18:1 vs --color-surface #1E1913 as dark text on top of it
  // as a fill (clears >=5.0:1).
  witt: { portraitImage: '/images/portraits/nikolaus.jpg', accentColor: '#579C40' },
  // H=305deg (orchid/plum), the widest open hue gap against every color above and the two
  // reserved semantic tokens. S=42%, L=58.5% clears both dark-mode thresholds: 5.30:1 vs the
  // dark ground #17130F and 5.00:1 vs --color-surface #1E1913 as a fill under dark text.
  lpc: { portraitImage: '/images/portraits/datus.jpg', accentColor: '#C269BA' },
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
