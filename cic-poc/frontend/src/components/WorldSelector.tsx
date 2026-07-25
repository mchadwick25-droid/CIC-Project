/**
 * WorldSelector component - displays available worlds and representatives.
 *
 * This is the entry screen before starting a conversation. Selection always
 * allows 1-MAX_WORLDS worlds; the Single/Multiple toggle is retired (§4) -
 * mode is emergent from seat count, named on the Begin button itself
 * rather than chosen up front.
 */

import { useState, useEffect } from 'react';
import type { World, WorldsResponse } from '../types/conversation';
import { WORLD_MEDIA } from '../data/worldMedia';

const API_BASE = '/api';

// Prototype/Phase 1 scope cap - kept at 3 (not the full design ceiling of 5)
// to keep cost and conversational complexity manageable at this stage.
const MAX_WORLDS = 3;

// World.period is a display string ("c. 312–451 CE", "70–200 CE") - the
// leading number is always its start year, so the tiles can be ordered by
// when each world's own life actually began without a separate sortable
// field on the manifest.
function startYear(period: string): number {
  const match = period.match(/\d+/);
  return match ? parseInt(match[0], 10) : Number.MAX_SAFE_INTEGER;
}

interface WorldSelectorProps {
  /** Called with the final selected worlds (1-MAX_WORLDS) when Begin is pressed. */
  onBegin: (worlds: World[]) => void;
}

export function WorldSelector({ onBegin }: WorldSelectorProps) {
  const [worlds, setWorlds] = useState<World[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [selectedWorlds, setSelectedWorlds] = useState<World[]>([]);

  useEffect(() => {
    async function fetchWorlds() {
      try {
        const response = await fetch(`${API_BASE}/worlds`);
        if (!response.ok) {
          throw new Error(`Failed to fetch worlds: ${response.statusText}`);
        }
        const data: WorldsResponse = await response.json();
        const sorted = [...data.worlds].sort((a, b) => startYear(a.period) - startYear(b.period));
        setWorlds(sorted);
        setIsLoading(false);

        // Pre-select worlds handed off from the Atlas/pilot pages
        // (?worlds=id,id&mode=interview|table) - the URL contract those
        // static pages were already built against, never actually wired up
        // on this end until now. Pre-selects only; Begin is still the one
        // required click, same as picking worlds by hand - the Atlas
        // suggests, it never starts a conversation on its own. `mode` needs
        // no separate handling: it's already emergent from seat count here
        // (see this component's own header comment, §4).
        const params = new URLSearchParams(window.location.search);
        const worldIdsParam = params.get('worlds');
        if (worldIdsParam) {
          const requestedIds = worldIdsParam.split(',').map(id => id.trim()).filter(Boolean);
          const matched = requestedIds
            .map(id => sorted.find(w => w.id === id))
            .filter((w): w is World => w !== undefined)
            .slice(0, MAX_WORLDS);
          if (matched.length > 0) {
            setSelectedWorlds(matched);
          }
        }
      } catch (err) {
        setError(err instanceof Error ? err.message : 'Unknown error');
        setIsLoading(false);
      }
    }

    fetchWorlds();
  }, []);

  const handleWorldClick = (world: World) => {
    setSelectedWorlds(prev => {
      const isSelected = prev.some(w => w.id === world.id);
      if (isSelected) {
        return prev.filter(w => w.id !== world.id);
      } else if (prev.length < MAX_WORLDS) {
        return [...prev, world];
      }
      return prev; // Max worlds reached
    });
  };

  const handleBeginConversation = () => {
    if (selectedWorlds.length === 0) return;
    onBegin(selectedWorlds);
  };

  const isWorldSelected = (world: World) => {
    return selectedWorlds.some(w => w.id === world.id);
  };

  const getSelectionOrder = (world: World) => {
    const index = selectedWorlds.findIndex(w => w.id === world.id);
    return index >= 0 ? index + 1 : null;
  };

  if (isLoading) {
    return (
      <div className="world-selector">
        <div className="world-selector__loading">
          <div className="loading-dots">
            <span className="loading-dot"></span>
            <span className="loading-dot"></span>
            <span className="loading-dot"></span>
          </div>
          <p>Loading available worlds...</p>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="world-selector">
        <div className="world-selector__error">
          <p>Failed to load worlds: {error}</p>
        </div>
      </div>
    );
  }

  // The naming replaces the control (§4): mode is emergent from seat count,
  // never a "lite vs. full" distinction - the difference is per-turn
  // readability at 3-4 voices, not two depths of encounter.
  const beginButtonText =
    selectedWorlds.length === 0
      ? 'Select a tradition to begin'
      : selectedWorlds.length === 1
        ? `Begin a Deep Interview with ${selectedWorlds[0].representative.name}`
        : `Begin — Compare Worlds: ${selectedWorlds.map(w => w.representative.name).join(', ')}`;

  return (
    <div className="world-selector">
      <div className="world-selector__header">
        <h2>Choose a Tradition</h2>
        <p>
          Select one or more worlds (up to {MAX_WORLDS}) to invite their representatives to The Table
        </p>
      </div>

      <div className="world-selector__grid">
        {worlds.map((world) => {
          const order = getSelectionOrder(world);
          const media = WORLD_MEDIA[world.id];
          return (
            <div
              key={world.id}
              className={`world-card ${isWorldSelected(world) ? 'world-card--selected' : ''}`}
              style={{ '--world-color': world.color } as React.CSSProperties}
              onClick={() => handleWorldClick(world)}
            >
              {order !== null && (
                <div className="world-card__selection-badge">{order}</div>
              )}

              <div className="world-card__header">
                <div>
                  <h3 className="world-card__name">{world.name}</h3>
                  {world.subtitle && (
                    <span className="world-card__subtitle">({world.subtitle})</span>
                  )}
                </div>
                <span className="world-card__period">{world.period}</span>
              </div>

              <p className="world-card__region">{world.region}</p>

              <p className="world-card__description">{world.description}</p>

              <div className="world-card__representative">
                <div className="world-card__rep-header">
                  <span className="world-card__rep-label">Representative</span>
                </div>
                <h4 className="world-card__rep-name">{world.representative.name}</h4>
                <p className="world-card__rep-title">{world.representative.title}</p>
                <p className="world-card__rep-description">
                  {world.representative.description}
                </p>

                {media && (
                  <img
                    className="world-card__portrait-image"
                    src={media.portraitImage}
                    alt={`Portrait of ${world.representative.name}`}
                  />
                )}
              </div>
            </div>
          );
        })}
      </div>

      <div className="world-selector__action">
        <button
          className="chat-button chat-button--primary chat-button--large"
          onClick={handleBeginConversation}
          disabled={selectedWorlds.length === 0}
        >
          {beginButtonText}
        </button>
      </div>
    </div>
  );
}
