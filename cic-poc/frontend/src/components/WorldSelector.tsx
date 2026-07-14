/**
 * WorldSelector component - displays available worlds and representatives.
 *
 * This is the entry screen before starting a conversation.
 * Supports both single-world and multi-world table selection (up to MAX_WORLDS worlds).
 */

import { useState, useEffect } from 'react';
import type { World, WorldsResponse } from '../types/conversation';

const API_BASE = '/api';

// Prototype/Phase 1 scope cap - kept at 3 (not the full design ceiling of 5)
// to keep cost and conversational complexity manageable at this stage.
const MAX_WORLDS = 3;

interface WorldSelectorProps {
  onSelectWorld: (world: World) => void;
  onSelectWorlds?: (worlds: World[]) => void;
  multiSelect?: boolean;
}

export function WorldSelector({ onSelectWorld, onSelectWorlds, multiSelect = false }: WorldSelectorProps) {
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
        setWorlds(data.worlds);
        setIsLoading(false);
      } catch (err) {
        setError(err instanceof Error ? err.message : 'Unknown error');
        setIsLoading(false);
      }
    }

    fetchWorlds();
  }, []);

  const handleWorldClick = (world: World) => {
    if (multiSelect) {
      // Toggle selection in multi-select mode
      setSelectedWorlds(prev => {
        const isSelected = prev.some(w => w.id === world.id);
        if (isSelected) {
          return prev.filter(w => w.id !== world.id);
        } else if (prev.length < MAX_WORLDS) {
          return [...prev, world];
        }
        return prev; // Max worlds reached
      });
    } else {
      // Single select mode
      setSelectedWorlds([world]);
    }
  };

  const handleBeginConversation = () => {
    if (selectedWorlds.length === 0) return;

    if (multiSelect && onSelectWorlds && selectedWorlds.length > 1) {
      onSelectWorlds(selectedWorlds);
    } else {
      onSelectWorld(selectedWorlds[0]);
    }
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

  const buttonText = selectedWorlds.length === 0
    ? 'Select a world to begin'
    : selectedWorlds.length === 1
      ? `Begin Conversation with ${selectedWorlds[0].representative.name}`
      : `Begin Conversation with ${selectedWorlds.length} Representatives`;

  return (
    <div className="world-selector">
      <div className="world-selector__header">
        <h2>Choose a Tradition</h2>
        <p>
          {multiSelect
            ? `Select one or more worlds (up to ${MAX_WORLDS}) to invite their representatives to The Table`
            : 'Select a world to enter into conversation with its representative'}
        </p>
      </div>

      <div className="world-selector__grid">
        {worlds.map((world) => {
          const order = multiSelect ? getSelectionOrder(world) : null;
          return (
            <div
              key={world.id}
              className={`world-card ${isWorldSelected(world) ? 'world-card--selected' : ''}`}
              style={{ '--world-color': world.color } as React.CSSProperties}
              onClick={() => handleWorldClick(world)}
            >
              {multiSelect && order !== null && (
                <div className="world-card__selection-badge">{order}</div>
              )}

              <div className="world-card__header">
                <h3 className="world-card__name">{world.name}</h3>
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
              </div>
            </div>
          );
        })}
      </div>

      {selectedWorlds.length > 0 && (
        <div className="world-selector__action">
          <button
            className="chat-button chat-button--primary chat-button--large"
            onClick={handleBeginConversation}
          >
            {buttonText}
          </button>
        </div>
      )}

      {selectedWorlds.length === 0 && worlds.length > 0 && (
        <div className="world-selector__hint">
          <p>
            {multiSelect
              ? 'Click on worlds to select them, then begin the conversation'
              : 'Click on a world to learn more and begin a conversation'}
          </p>
        </div>
      )}
    </div>
  );
}
