/**
 * The pre-session identity/disclosure screen (Main.dc.html). Deliberately
 * lighter than that mockup: the mockup's "Who built this, and what we hope"
 * paragraph and "What brings you here?" frame chips were illustrative copy
 * for the design pass, not approved participant-facing text or a real
 * server field - engine/api's MessageRequest takes only {text,
 * client_msg_id}, nothing like a register/frame. The Facilitator's own
 * SYSTEM_NATURE turn (engine/m4/facilitator_turns.py, Mark-approved) already
 * gives the "we use AI, here's how" disclosure once the conversation opens -
 * duplicating it here in different words would be a second, unapproved
 * version of the same claim.
 */
import type { WorldEntry } from '../data/worlds';

interface DoorwayProps {
  world: WorldEntry;
  onBack: () => void;
  onBegin: () => void;
  isLoading: boolean;
  error: string | null;
}

export function Doorway({ world, onBack, onBegin, isLoading, error }: DoorwayProps) {
  return (
    <div className="doorway">
      <button type="button" className="doorway__back sans" onClick={onBack}>
        ← Back to worlds
      </button>

      <div className="doorway__portrait" style={{ background: world.accentColor }}>
        <img src={world.portraitImage} alt={world.representativeName} />
      </div>
      <div className="doorway__era sans" style={{ color: world.accentColor }}>
        {world.displayName} · c. {world.eraStart}–{world.eraEnd}
      </div>
      <h1 className="doorway__name">{world.representativeName}</h1>
      <p className="doorway__role">{world.roleLabel}</p>
      <p className="doorway__place sans">{world.place}</p>

      <div className="doorway__thinness">
        <div className="doorway__thinness-label sans">What this voice knows well — and doesn't</div>
        <p>{world.thinnessStatement}</p>
      </div>

      {error && <div className="conversation__error" style={{ margin: 'var(--spacing-md) 0 0' }}>{error}</div>}

      <button type="button" className="doorway__begin" onClick={onBegin} disabled={isLoading}>
        {isLoading ? 'Opening…' : `Begin with ${world.representativeName}`}
      </button>
      <p className="doorway__footnote">This conversation is built from real sources you can check.</p>
    </div>
  );
}
