/**
 * The six seated worlds, straight from records/worlds.yaml (kind: formation,
 * state: built) - not the "fix" fixture, which BASELINES.md and
 * PHASE-1-LAUNCH.md are both explicit is "not a real world, never admitted
 * or open." Every field below is copied verbatim from the registry entry
 * named in its comment; nothing here is invented copy.
 *
 * No /api/worlds endpoint exists yet, so this is baked in at build time.
 * Portrait images already exist as static assets (previously wired for the
 * old World Selector) - reused as-is, not recreated.
 *
 * Accent colors match the ones fixed in the Stage 7.5 design canvas review
 * (2026-08-24): the registry itself names no per-world color, and five of
 * six first-draft picks collided with reserved semantic tokens (lapis,
 * tyrian) or were invented off-palette hues.
 */
export interface WorldEntry {
  worldKey: string; // records/worlds.yaml key - what POST /api/session expects
  censusId: string | null; // records/worlds.yaml's own census_id - cic-website/data/world-census.json's matching entry id, and what its "Launch an Interview" links carry as ?worlds=. null where worlds.yaml itself hasn't verified the mapping yet (desert, as of 2026-08-25) - left unset rather than guessed, so that one link just falls through to the world list instead of a deep link.
  displayName: string;
  representativeName: string;
  roleLabel: string;
  place: string;
  eraStart: number;
  eraEnd: number;
  thinnessStatement: string;
  portraitImage: string;
  accentColor: string;
}

export const WORLDS: WorldEntry[] = [
  {
    worldKey: 'alx',
    censusId: 'alexandria-catechetical',
    displayName: 'Alexandrian Christianity',
    representativeName: 'Theon',
    roleLabel: 'Catechetical Teacher',
    place: 'Alexandria and Egypt',
    eraStart: 150,
    eraEnd: 400,
    thinnessStatement:
      "Richest in teaching, argument, and the theology of formation; thinner on women's own words, ordinary believers, and rural Coptic Egypt.",
    portraitImage: '/images/portraits/alexandria.png',
    accentColor: '#B45309',
  },
  {
    worldKey: 'pahc',
    censusId: 'post-apostolic-house-church',
    displayName: 'Post-Apostolic House-Church Christianity',
    representativeName: 'Chloe',
    roleLabel: 'Household Leader',
    place: 'Antioch/Syria, Asia Minor, Rome',
    eraStart: 70,
    eraEnd: 200,
    thinnessStatement:
      "Richest in letters, church order, and worship practice; thinner on women's own words, enslaved members, the non-literate majority, and any material remains.",
    portraitImage: '/images/portraits/house-churches.png',
    accentColor: '#2F6B52',
  },
  {
    worldKey: 'desert',
    censusId: null, // worlds.yaml: "not yet verified against the running Atlas frontend this session - carried as an open item"
    displayName: 'Desert Monasticism',
    representativeName: 'Papnoute',
    roleLabel: 'Abba (Elder)',
    place: 'Egyptian and Palestinian desert monasticism',
    eraStart: 320,
    eraEnd: 430,
    thinnessStatement:
      "Richest in the Apophthegmata's own elder-and-disciple sayings tradition and Antony's own Vita; thinner on ordinary participants outside the collected-sayings tradition, on the Pachomian federation's own interior life beyond its founding, and on women's own voices (a small number of amma sayings, not a fuller corpus).",
    portraitImage: '/images/portraits/desert.png',
    accentColor: '#7A6A2E',
  },
  {
    worldKey: 'hal',
    censusId: 'hieronymian-ascetic-literary',
    displayName: 'Hieronymian Ascetic-Literary Christianity',
    representativeName: 'Albina',
    roleLabel: 'Widow of the Household',
    place: 'Bethlehem and Rome',
    eraStart: 382,
    eraEnd: 420,
    thinnessStatement:
      "Richest in Jerome's own letters, translation prefaces, and the remembered lives of the Roman women who sustained the work; thinner on the women's own words (none survive), ordinary monastery residents, and daily-life detail beyond one letter.",
    portraitImage: '/images/portraits/bethlehem.png',
    accentColor: '#8C4A5C',
  },
  {
    worldKey: 'syr',
    censusId: 'syriac-edessa-nisibis',
    displayName: 'Syriac Christianity (Edessa/Nisibis)',
    representativeName: 'Yausep',
    roleLabel: 'Mar',
    place: 'The Syriac-speaking ecology across the Roman-Persian Mesopotamian frontier',
    eraStart: 200,
    eraEnd: 410,
    thinnessStatement:
      "Richest in hymns, doctrinal teaching, and covenant asceticism (Ephrem, Aphrahat); thinner on ordinary believers, women's own words, and the years after Ephrem's death.",
    portraitImage: '/images/portraits/syriac.png',
    accentColor: '#3D6B75',
  },
  {
    worldKey: 'ijc',
    censusId: 'imperial-juridical-christianity',
    displayName: 'Imperial and Juridical Christianity',
    representativeName: 'Marius',
    roleLabel: 'Deacon of the Letters',
    place: 'Rome, Constantinople, Milan',
    eraStart: 312,
    eraEnd: 451,
    thinnessStatement:
      "Richest in councils, canons, letters, and the contest over who holds final authority in the church; thinner on ordinary believers' daily lives, women's own words, and the defeated Homoian side's own voice.",
    portraitImage: '/images/portraits/empire.png',
    accentColor: '#7A5233',
  },
];

export function findWorld(worldKey: string): WorldEntry | undefined {
  return WORLDS.find((w) => w.worldKey === worldKey);
}

export function findWorldByCensusId(censusId: string): WorldEntry | undefined {
  return WORLDS.find((w) => w.censusId === censusId);
}
