/**
 * Real photographs for the World Selector tiles - one architectural/artifact
 * image per world (Ministry/Communication/Brand-Assets/World-Media/) and one
 * Representative profile portrait (.../Representative-Portraits/), both
 * copied into public/images/ so Vite serves them directly.
 *
 * Keyed by world_id (world_manifest.py) - same convention as WORLD_ICONS in
 * worldIcons.tsx. Sourcing/license/attribution for each world image lives in
 * Brand-Assets/World-Media/world-media-sources.json - not duplicated here.
 */
export interface WorldMedia {
  /** Real architectural/artifact photo, tied to this world's own region and era. */
  worldImage: string;
  /** The Representative's approved profile portrait. */
  portraitImage: string;
}

export const WORLD_MEDIA: Record<string, WorldMedia> = {
  'post-apostolic-house-church': {
    worldImage: '/images/world-media/house-churches.jpg',
    portraitImage: '/images/portraits/house-churches.png',
  },
  'alexandria-catechetical': {
    worldImage: '/images/world-media/alexandria.jpg',
    portraitImage: '/images/portraits/alexandria.png',
  },
  'syriac-edessa-nisibis': {
    worldImage: '/images/world-media/syriac.jpg',
    portraitImage: '/images/portraits/syriac.png',
  },
  'imperial-juridical-christianity': {
    worldImage: '/images/world-media/empire.jpg',
    portraitImage: '/images/portraits/empire.png',
  },
  'desert-monasticism': {
    worldImage: '/images/world-media/desert.jpg',
    portraitImage: '/images/portraits/desert.png',
  },
  'hieronymian-ascetic-literary': {
    worldImage: '/images/world-media/bethlehem.jpg',
    portraitImage: '/images/portraits/bethlehem.png',
  },
};
