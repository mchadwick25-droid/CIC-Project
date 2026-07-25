/**
 * Real photographs for the World Selector tiles - a Representative profile
 * portrait per world (Ministry/Communication/Brand-Assets/Representative-
 * Portraits/), copied into public/images/ so Vite serves it directly.
 *
 * `worldImage` (the architectural/artifact tile-background photos, one per
 * world, sourced from Wikimedia Commons) is deliberately NOT wired up here -
 * pulled 2026-07-24 pending a rights/licensing question Mark was told about
 * (payment/permission required for 5 of the 6). Files themselves were
 * removed from public/images/world-media/; the sourcing research is still on
 * record at Brand-Assets/World-Media/ (not deleted, flagged there instead)
 * in case it's resolved later. See In-App-Icons-Graphics Decision-Log.
 *
 * Keyed by world_id (world_manifest.py) - same convention as WORLD_ICONS in
 * worldIcons.tsx.
 */
export interface WorldMedia {
  /** The Representative's approved profile portrait. */
  portraitImage: string;
}

export const WORLD_MEDIA: Record<string, WorldMedia> = {
  'post-apostolic-house-church': {
    portraitImage: '/images/portraits/house-churches.png',
  },
  'alexandria-catechetical': {
    portraitImage: '/images/portraits/alexandria.png',
  },
  'syriac-edessa-nisibis': {
    portraitImage: '/images/portraits/syriac.png',
  },
  'imperial-juridical-christianity': {
    portraitImage: '/images/portraits/empire.png',
  },
  'desert-monasticism': {
    portraitImage: '/images/portraits/desert.png',
  },
  'hieronymian-ascetic-literary': {
    portraitImage: '/images/portraits/bethlehem.png',
  },
};
