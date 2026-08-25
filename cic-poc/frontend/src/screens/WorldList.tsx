import { ArrivingLockup } from '../components/ArrivingLockup';
import type { WorldEntry } from '../data/worlds';

interface WorldListProps {
  worlds: WorldEntry[];
  isLoading: boolean;
  error: string | null;
  onSelect: (worldKey: string) => void;
}

export function WorldList({ worlds, isLoading, error, onSelect }: WorldListProps) {
  return (
    <div>
      <ArrivingLockup />
      {error && <div className="conversation__error" style={{ margin: '0 var(--spacing-lg)' }}>{error}</div>}
      {isLoading && !error && <p className="world-list__loading sans">Gathering the worlds…</p>}
      <div className="world-list">
        {worlds.map((world) => (
          <button key={world.worldKey} className="world-card" onClick={() => onSelect(world.worldKey)}>
            <img className="world-card__portrait" src={world.portraitImage} alt="" />
            <div style={{ flex: 1, minWidth: 0 }}>
              <div className="world-card__tradition sans" style={{ color: world.accentColor }}>
                {world.displayName}
              </div>
              <div className="world-card__header">
                <div className="world-card__name">
                  {world.representativeName} <span className="world-card__role">· {world.roleLabel}</span>
                </div>
                <div className="world-card__era sans">
                  c. {world.eraStart}–{world.eraEnd}
                </div>
              </div>
              <div className="world-card__subtitle">{world.place}</div>
              <p className="world-card__thinness">{world.thinnessStatement}</p>
            </div>
          </button>
        ))}
      </div>
    </div>
  );
}
