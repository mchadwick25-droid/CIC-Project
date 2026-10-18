/**
 * Arrival happens inside the room: the identity-and-disclosure content
 * the retired Doorway screen carried now opens the conversation itself,
 * above the Facilitator's door turn - one click fewer, nothing
 * undisclosed. Every quoted line below is carried VERBATIM from that
 * screen, whose own header traced each sentence to the Program-Spec
 * (SS9/SS165/SS166) - this move relocates approved prose, it does not
 * compose new prose.
 *
 * ONE EXCEPTION, deliberate and flagged rather than silent: the final
 * sentence of `arrival__disclosure` (the ✲ mark explainer) IS new prose,
 * not relocated - it extends this existing disclosure rather than
 * adding a new first-tap UI element (no new component, no new state).
 */
import { useState } from 'react';
import type { WorldEntry } from '../data/worlds';

interface ArrivalProps {
  world: WorldEntry;
}

export function Arrival({ world }: ArrivalProps) {
  // On a phone the doorway folds to its first two lines, so the message box
  // and the disclosure share the first screen; its words never change.
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
        {world.roleLabel} · <span className="sans">{world.place}</span>
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

      <div className="arrival__disclosure sans">
        <p>
          The system exists to reveal Jesus through the witness of his church across history. Every other outcome serves
          this one. Revealing is witness, never recruitment: each world testifies from its own sources, and
          interpretation remains the participant's own. We believe an honest, transparent telling of the church's story
          will reveal Christ's faithfulness — it is never a pushed objective.
        </p>
        <p>{world.representativeName}'s name is ours; every quote and claim is theirs, and you can check each one.</p>
        <p>Look for the ✲ mark after a claim — tap it to see exactly where it comes from.</p>
      </div>

      <details className="arrival__thinness">
        <summary className="arrival__thinness-label sans">What this voice knows well — and doesn't</summary>
        <p>{world.thinnessStatement}</p>
      </details>
      {world.livingTraditionFlag && (
        <p className="arrival__living-tradition">This is a bounded historical reconstruction, not today's church of the same name.</p>
      )}
    </div>
  );
}
