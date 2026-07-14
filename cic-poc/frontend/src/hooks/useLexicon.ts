/**
 * React hook for fetching and managing lexicon data.
 */

import { useState, useEffect, useCallback } from 'react';
import type { LexiconTerm, LexiconResponse } from '../types/conversation';

const API_BASE = '/api';

interface UseLexiconResult {
  terms: LexiconTerm[];
  /**
   * Merged term map across every world at the table. Two different worlds
   * can legitimately alias to the same everyday word (confirmed live: both
   * "elder" and "renunciation" are shared aliases between two of the four
   * worlds' own lexicons) - on a merged map, whichever world's terms were
   * added last silently wins that key, so a representative's own word can
   * end up hover/click-linked to a DIFFERENT world's definition. Safe to use
   * only for purposes that don't care which world a match belongs to (e.g.
   * "has this string been seen anywhere in the conversation before" for the
   * first-occurrence highlight dedup) - never for resolving what a specific
   * representative's own message should link to. Use termMapsByWorld for that.
   */
  termMap: Map<string, LexiconTerm>;
  /** One term map per world_id, built from ONLY that world's own terms - the
   * correct, collision-free map to use when rendering a specific
   * representative's message (look up by that representative's world_id). */
  termMapsByWorld: Map<string, Map<string, LexiconTerm>>;
  isLoading: boolean;
  error: string | null;
  findTerm: (text: string) => LexiconTerm | undefined;
}

function buildTermMap(terms: LexiconTerm[]): Map<string, LexiconTerm> {
  const map = new Map<string, LexiconTerm>();
  for (const term of terms) {
    // Add the main term (extract just the primary word)
    const primaryTerm = term.term.split('/')[0].trim();
    const simpleTerm = primaryTerm.replace(/\s*\([^)]*\)\s*/g, '').trim();
    map.set(simpleTerm.toLowerCase(), term);

    // Add aliases
    for (const alias of term.aliases) {
      const simpleAlias = alias.replace(/["""]/g, '').trim();
      if (simpleAlias.length > 2) {
        map.set(simpleAlias.toLowerCase(), term);
      }
    }
  }
  return map;
}

export function useLexicon(worldIds: string[] | string | null): UseLexiconResult {
  const [terms, setTerms] = useState<LexiconTerm[]>([]);
  const [termMap, setTermMap] = useState<Map<string, LexiconTerm>>(new Map());
  const [termMapsByWorld, setTermMapsByWorld] = useState<Map<string, Map<string, LexiconTerm>>>(new Map());
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  // Normalize to an array and derive a stable key so the effect only
  // re-fires when the actual set of worlds changes, not on every render.
  const idsArray = worldIds == null ? [] : Array.isArray(worldIds) ? worldIds : [worldIds];
  const idsKey = idsArray.join(',');

  useEffect(() => {
    async function fetchLexicon() {
      if (idsArray.length === 0) {
        setIsLoading(false);
        return;
      }

      setIsLoading(true);
      try {
        // Fetch every world at the table, not just the primary one - a
        // multi-world table's highlighting must cover every representative's
        // own vocabulary (e.g. the Syriac world's raza/Iḥidaya, the desert
        // world's Hēsychia/Koinōnia), not only the first world's terms.
        const responses = await Promise.all(
          idsArray.map((id) => fetch(`${API_BASE}/lexicon?world_id=${encodeURIComponent(id)}`))
        );
        for (const response of responses) {
          if (!response.ok) {
            throw new Error(`Failed to fetch lexicon: ${response.statusText}`);
          }
        }
        const dataList: LexiconResponse[] = await Promise.all(responses.map((r) => r.json()));
        const allTerms = dataList.flatMap((data) => data.terms);
        setTerms(allTerms);

        // Merged map - see the collision caveat on the returned termMap field.
        setTermMap(buildTermMap(allTerms));

        // One map per world, built from only that world's own terms - this
        // is what a specific representative's message should actually be
        // highlighted against.
        const byWorld = new Map<string, Map<string, LexiconTerm>>();
        idsArray.forEach((id, index) => {
          byWorld.set(id, buildTermMap(dataList[index].terms));
        });
        setTermMapsByWorld(byWorld);
        setIsLoading(false);
      } catch (err) {
        setError(err instanceof Error ? err.message : 'Unknown error');
        setIsLoading(false);
      }
    }

    fetchLexicon();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [idsKey]);

  const findTerm = useCallback(
    (text: string): LexiconTerm | undefined => {
      return termMap.get(text.toLowerCase());
    },
    [termMap]
  );

  return {
    terms,
    termMap,
    termMapsByWorld,
    isLoading,
    error,
    findTerm,
  };
}
