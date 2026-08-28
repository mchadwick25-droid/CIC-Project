/**
 * Arrival happens inside the room (Mark's ruling, 2026-08-28): the
 * identity-and-disclosure content the retired Doorway screen carried now
 * opens the conversation itself, above the Facilitator's door turn - one
 * click fewer, nothing undisclosed. Every quoted line below is carried
 * VERBATIM from that screen, whose own header traced each sentence to the
 * Program-Spec (SS9/SS165/SS166) and Mark's own approval discipline - this
 * move relocates approved prose, it does not compose new prose.
 */
import type { WorldEntry } from '../data/worlds';

interface ArrivalProps {
  world: WorldEntry;
}

export function Arrival({ world }: ArrivalProps) {
  return (
    <div className="arrival">
      <div className="arrival__portrait" style={{ background: world.accentColor }}>
        <img src={world.portraitImage} alt={world.representativeName} />
      </div>
      <div className="arrival__era sans" style={{ color: world.accentColor }}>
        {world.displayName} · c. {world.eraStart}–{world.eraEnd}
      </div>
      <h1 className="arrival__name">{world.representativeName}</h1>
      <p className="arrival__role">
        {world.roleLabel} · <span className="sans">{world.place}</span>
      </p>

      {world.horizon && <p className="arrival__horizon">{world.horizon}</p>}

      <div className="arrival__thinness">
        <div className="arrival__thinness-label sans">What this voice knows well — and doesn't</div>
        <p>{world.thinnessStatement}</p>
        {world.livingTraditionFlag && (
          <p className="arrival__living-tradition">This is a bounded historical reconstruction, not today's church of the same name.</p>
        )}
      </div>

      <div className="arrival__disclosure sans">
        <p>
          The system exists to reveal Jesus through the witness of his church across history. Every other outcome serves
          this one. Revealing is witness, never recruitment: each world testifies from its own sources, and
          interpretation remains the participant's own. We believe an honest, transparent telling of the church's story
          will reveal Christ's faithfulness — it is never a pushed objective.
        </p>
        <p>{world.representativeName}'s name is ours; every quote and claim is theirs, and you can check each one.</p>
      </div>
    </div>
  );
}
