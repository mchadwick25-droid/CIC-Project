/**
 * Fetches GET /api/worlds once on mount. Each world's place in the list,
 * portrait and accent colour come with it, from its registry entry, so an
 * admitted world appears without a new build of the app.
 */
import { useEffect, useState } from 'react';
import { getWorlds } from '../lib/api';
import type { WorldEntry } from '../data/worlds';
import type { WorldSummary } from '../types/conversation';

function toEntry(summary: WorldSummary): WorldEntry | null {
  const app = summary.app;
  if (!app || !summary.representative || !summary.time_window) return null;
  return {
    worldKey: summary.world_key,
    censusId: summary.census_id,
    displayName: summary.display_name ?? summary.world_key,
    cardName: summary.card_name ?? summary.display_name ?? summary.world_key,
    representativeName: summary.representative.name,
    roleLabel: summary.representative.role_label,
    place: summary.place ?? '',
    eraStart: summary.time_window.start,
    eraEnd: summary.time_window.end,
    thinnessStatement: summary.thinness_statement ?? '',
    // Prefer the registry's plain-English doorway paragraph; fall back to
    // the model-facing horizon only for an entry that hasn't authored one.
    doorwayDescription: summary.doorway_description ?? summary.horizon,
    livingTraditionFlag: summary.living_tradition_flag,
    starters: summary.starters,
    portraitImage: app.portrait,
    accentColor: app.accent_color,
  };
}

interface WorldsState {
  worlds: WorldEntry[];
  isLoading: boolean;
  error: string | null;
}

export function useWorlds() {
  const [state, setState] = useState<WorldsState>({ worlds: [], isLoading: true, error: null });

  useEffect(() => {
    let cancelled = false;
    getWorlds()
      .then(({ worlds }) => {
        if (cancelled) return;
        const order = new Map(worlds.map((w) => [w.world_key, w.app?.order ?? Infinity]));
        const entries = worlds.map(toEntry).filter((w): w is WorldEntry => w !== null);
        entries.sort((a, b) => (order.get(a.worldKey) ?? Infinity) - (order.get(b.worldKey) ?? Infinity));
        setState({ worlds: entries, isLoading: false, error: null });
      })
      .catch(() => {
        if (cancelled) return;
        setState({ worlds: [], isLoading: false, error: 'Could not load the worlds.' });
      });
    return () => {
      cancelled = true;
    };
  }, []);

  return state;
}
