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
 * not relocated - Stage 6e (Ministry/Features/Conversation-Transparency-
 * Engine/Decision-Log.md), R10's own "label copy" requirement, per
 * Mark's own direction to extend this existing disclosure rather than
 * add a new first-tap UI element (respects R17's per-screen element
 * budget by construction - no new component, no new state). DRAFT
 * COPY, not yet Mark's own word - built so the mechanism is complete,
 * per the same discipline Stage 6b's confidence phrases followed.
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

      {world.doorwayDescription && <p className="arrival__horizon">{world.doorwayDescription}</p>}

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
        <p>Look for the ✲ mark after a claim — tap it to see exactly where it comes from.</p>
      </div>
    </div>
  );
}
