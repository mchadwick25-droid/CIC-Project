/**
 * A seated world as the app shows it: everything comes from GET /api/worlds
 * (hooks/useWorlds.ts), including its place in the list, portrait and accent
 * colour, which the registry entry carries under `app`.
 */
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
