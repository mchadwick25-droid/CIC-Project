import { ArrivingLockup } from '../components/ArrivingLockup';
import { WORLDS } from '../data/worlds';

interface WorldListProps {
  onSelect: (worldKey: string) => void;
}

export function WorldList({ onSelect }: WorldListProps) {
  return (
    <div>
      <ArrivingLockup />
      <div className="world-list">
        {WORLDS.map((world) => (
          <button key={world.worldKey} className="world-card" onClick={() => onSelect(world.worldKey)}>
            <img className="world-card__portrait" src={world.portraitImage} alt="" />
            <div style={{ flex: 1, minWidth: 0 }}>
              <div className="world-card__header">
                <div className="world-card__name">{world.representativeName}</div>
                <div className="world-card__era sans" style={{ color: world.accentColor }}>
                  c. {world.eraStart}–{world.eraEnd}
                </div>
              </div>
              <div className="world-card__subtitle">
                {world.roleLabel} · {world.place}
              </div>
              <p className="world-card__thinness">{world.thinnessStatement}</p>
            </div>
          </button>
        ))}
      </div>
    </div>
  );
}
