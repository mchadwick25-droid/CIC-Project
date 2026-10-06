import { renderHook, waitFor } from '@testing-library/react';
import { afterEach, describe, expect, it, vi } from 'vitest';
import { useWorlds } from './useWorlds';
import * as api from '../lib/api';
import type { WorldSummary } from '../types/conversation';

function summary(world_key: string, app: WorldSummary['app']): WorldSummary {
  return {
    world_key,
    census_id: world_key,
    display_name: world_key,
    card_name: world_key,
    representative: { name: 'Rep', role_label: 'Role' },
    time_window: { start: 100, end: 200 },
    place: 'Place',
    thinness_statement: '',
    doorway_description: 'Doorway',
    horizon: null,
    living_tradition_flag: false,
    starters: [],
    app,
  };
}

describe('useWorlds', () => {
  afterEach(() => vi.restoreAllMocks());

  it('orders worlds by their registry place and takes portrait and colour from it', async () => {
    vi.spyOn(api, 'getWorlds').mockResolvedValue({
      worlds: [
        summary('b', { order: 2, accent_color: '#222222', portrait: '/b.webp' }),
        summary('a', { order: 1, accent_color: '#111111', portrait: '/a.webp' }),
      ],
    });
    const { result } = renderHook(() => useWorlds());
    await waitFor(() => expect(result.current.isLoading).toBe(false));
    expect(result.current.worlds.map((w) => w.worldKey)).toEqual(['a', 'b']);
    expect(result.current.worlds[0].portraitImage).toBe('/a.webp');
    expect(result.current.worlds[0].accentColor).toBe('#111111');
  });

  it('leaves out a world whose registry entry has no app block', async () => {
    vi.spyOn(api, 'getWorlds').mockResolvedValue({
      worlds: [summary('a', { order: 1, accent_color: '#111111', portrait: '/a.webp' }), summary('c', null)],
    });
    const { result } = renderHook(() => useWorlds());
    await waitFor(() => expect(result.current.isLoading).toBe(false));
    expect(result.current.worlds.map((w) => w.worldKey)).toEqual(['a']);
  });
});
