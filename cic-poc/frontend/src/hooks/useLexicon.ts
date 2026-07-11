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

export function useLexicon(worldId: string | null): UseLexiconResult {
  const [terms, setTerms] = useState<LexiconTerm[]>([]);
  const [termMap, setTermMap] = useState<Map<string, LexiconTerm>>(new Map());
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    async function fetchLexicon() {
      if (!worldId) {
        setIsLoading(false);
        return;
      }

      setIsLoading(true);
      try {
        const response = await fetch(`${API_BASE}/lexicon?world_id=${encodeURIComponent(worldId)}`);
        if (!response.ok) {
          throw new Error(`Failed to fetch lexicon: ${response.statusText}`);
        }

        const data: LexiconResponse = await response.json();
        setTerms(data.terms);

        // Build a map for quick lookups (term + aliases -> LexiconTerm)
        const map = new Map<string, LexiconTerm>();
        for (const term of data.terms) {
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
  }, [worldId]);

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
