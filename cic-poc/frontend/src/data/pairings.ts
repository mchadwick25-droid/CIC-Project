/**
 * The Table's recommended seatings - the launch tray's guidance data,
 * carried verbatim in substance from the C6 pairing record
 * (Ministry/Technology/CiC_Table_Pairings_V1_2026-08-28.md). DRAFT
 * status: that document awaits Mark's sign-off; refining these
 * suggestions is a data edit here, never a code change - exactly the
 * module boundary the launch-system ruling (2026-08-28) asked for.
 *
 * P4 (hal + desert) is deliberately NOT offered: the C6 record schedules
 * it for battery-accompanied runs, not first public offering.
 */

export interface Pairing {
  id: string;
  worldKeys: string[];
  title: string;
  why: string;
  proven: boolean;
}

export const PAIRINGS: Pairing[] = [
  {
    id: 'P1',
    worldKeys: ['alx', 'desert'],
    title: 'The school and the desert',
    why: 'Learning pursued through argument beside faith pursued through a life stripped bare — the contrast this Table was built to hold.',
    proven: true,
  },
  {
    id: 'P2',
    worldKeys: ['pahc', 'ijc'],
    title: 'The arc of the church',
    why: 'The faith as a meal in somebody’s house, long before empire noticed it, beside the faith as an institution the empire writes to.',
    proven: false,
  },
  {
    id: 'P3',
    worldKeys: ['syr', 'alx'],
    title: 'Two ways of knowing',
    why: 'The same Scripture met through Greek argument and through Syriac poetry — different ways of thinking, not just different conclusions.',
    proven: false,
  },
  {
    id: 'F1',
    worldKeys: ['alx', 'desert', 'pahc'],
    title: 'School, desert, and household',
    why: 'Three shapes of formation across the whole ancient arc, no two alike — the fullest Table on offer.',
    proven: false,
  },
];

/** Pairings compatible with the seats already chosen - the tray's
 * suggestion list. With no seats chosen, everything is on offer; with
 * seats chosen, only seatings that include all of them. */
export function suggestionsFor(seated: string[]): Pairing[] {
  return PAIRINGS.filter((p) => seated.every((k) => p.worldKeys.includes(k)) && p.worldKeys.length > seated.length);
}
