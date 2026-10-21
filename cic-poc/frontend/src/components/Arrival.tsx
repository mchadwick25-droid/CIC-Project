/** Who the voice is: the About panel's content. */
import { useState } from 'react';
import type { WorldEntry } from '../data/worlds';

interface ArrivalProps {
  world: WorldEntry;
}

export function Arrival({ world }: ArrivalProps) {
  const [horizonOpen, setHorizonOpen] = useState(false);
  return (
    <div className="arrival">
      <div className="arrival__portrait" style={{ background: world.accentColor }}>
        <img src={world.portraitImage} alt={world.representativeName} />
      </div>
      <div className="arrival__era sans" style={{ color: world.accentColor }}>
        {world.cardName} · c. {world.eraStart}–{world.eraEnd}
      </div>
      {/* The scholarly register earns its line only when it's a genuinely
          different name - e.g. syr's "studied as Syriac Christianity
          (Edessa/Nisibis)" merely restated the kicker plus a parenthetical
          the place line already carries. */}
      {!world.displayName.startsWith(world.cardName) && (
        <div className="arrival__scholarly sans">studied as {world.displayName}</div>
      )}
      <h1 className="arrival__name">{world.representativeName}</h1>
      <p className="arrival__role">
        <span className="sans">{world.place}</span>
      </p>

      {world.doorwayDescription && (
        <>
          <p className={horizonOpen ? 'arrival__horizon arrival__horizon--open' : 'arrival__horizon'}>{world.doorwayDescription}</p>
          {!horizonOpen && (
            <button type="button" className="arrival__horizon-more sans" onClick={() => setHorizonOpen(true)}>
              Read more
            </button>
          )}
        </>
      )}

      {world.livingTraditionFlag && (
        <p className="arrival__living-tradition">This is a bounded historical reconstruction, not today's church of the same name.</p>
      )}
    </div>
  );
}
