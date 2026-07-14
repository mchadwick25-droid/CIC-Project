/**
 * React hook for fetching and managing lexicon data.
 */

import { useState, useEffect, useCallback } from 'react';
import type { LexiconTerm, LexiconResponse } from '../types/conversation';

const API_BASE = '/api';

interface UseLexiconResult {
  terms: LexiconTerm[];
  termMap: Map<string, LexiconTerm>;
  isLoading: boolean;
  error: string | null;
  findTerm: (text: string) => LexiconTerm | undefined;
}

export function useLexicon(worldIds: string[] | string | null): UseLexiconResult {
  const [terms, setTerms] = useState<LexiconTerm[]>([]);
  const [termMap, setTermMap] = useState<Map<string, LexiconTerm>>(new Map());
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

        // Build a map for quick lookups (term + aliases -> LexiconTerm)
        const map = new Map<string, LexiconTerm>();
        for (const term of allTerms) {
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
        setTermMap(map);
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
    isLoading,
    error,
    findTerm,
  };
}
