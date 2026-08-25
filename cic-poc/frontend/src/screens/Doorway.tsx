/**
 * The pre-session identity/disclosure screen (Main.dc.html; Program-Spec
 * SS165's "detailed world card" - portrait and name; display name, period,
 * place; thinness statement; the living-tradition distinction where
 * flagged; self-disclosure; persona provenance; starter questions; the
 * launch). Every quoted line below is the spec's own words, not composed
 * here - SS9 (O0) and SS166 give both disclosure sentences verbatim, and
 * SS165 gives the living-tradition sentence verbatim. New participant-
 * facing prose still goes through Mark's own draft-and-approve discipline
 * (see engine/m4/facilitator_turns.py's docstring); quoting text he
 * already approved at the highest level - the Program-Spec itself - is
 * not that.
 *
 * The Facilitator's own SYSTEM_NATURE turn (engine/m4/facilitator_turns.py,
 * Mark-approved) separately gives the fuller "we use AI, here's how"
 * disclosure once the conversation opens - this screen's self-disclosure
 * is about who built this and why, a different claim, not a duplicate.
 */
import type { WorldEntry, WorldStarter } from '../data/worlds';

interface DoorwayProps {
  world: WorldEntry;
  onBack: () => void;
  onBegin: () => void;
  isLoading: boolean;
  error: string | null;
}

// Up to 3 starters spanning distinct cell tags (basic/identity, personal,
// critical/etic) rather than the first 3 alphabetically - a nervous
// participant benefits more from seeing the range of what's askable than
// from an arbitrary sample. Falls back to the first 3 if a world's starter
// set doesn't cover all three suffixes.
function sampleStarters(starters: WorldStarter[]): WorldStarter[] {
  const bySuffix = (suffix: string) => starters.find((s) => s.cell.endsWith(suffix));
  const picked = [bySuffix('-I'), bySuffix('-P'), bySuffix('-E')].filter((s): s is WorldStarter => s !== undefined);
  const deduped = picked.filter((s, i) => picked.findIndex((p) => p.cell === s.cell) === i);
  return deduped.length >= 2 ? deduped : starters.slice(0, 3);
}

export function Doorway({ world, onBack, onBegin, isLoading, error }: DoorwayProps) {
  const starters = sampleStarters(world.starters);

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

      {world.horizon && <p className="doorway__horizon">{world.horizon}</p>}

      <div className="doorway__thinness">
        <div className="doorway__thinness-label sans">What this voice knows well — and doesn't</div>
        <p>{world.thinnessStatement}</p>
        {world.livingTraditionFlag && (
          <p className="doorway__living-tradition">This is a bounded historical reconstruction, not today's church of the same name.</p>
        )}
      </div>

      {starters.length > 0 && (
        <div className="doorway__starters">
          <div className="doorway__starters-label sans">Questions you might ask</div>
          <ul>
            {starters.map((s) => (
              <li key={s.cell}>{s.text}</li>
            ))}
          </ul>
        </div>
      )}

      <div className="doorway__disclosure sans">
        <p>
          The system exists to reveal Jesus through the witness of his church across history. Every other outcome serves
          this one. Revealing is witness, never recruitment: each world testifies from its own sources, and
          interpretation remains the participant's own. We believe an honest, transparent telling of the church's story
          will reveal Christ's faithfulness — it is never a pushed objective.
        </p>
        <p>{world.representativeName}'s name is ours; every quote and claim is theirs, and you can check each one.</p>
      </div>

      {error && <div className="conversation__error" style={{ margin: 'var(--spacing-md) 0 0' }}>{error}</div>}

      <button type="button" className="doorway__begin" onClick={onBegin} disabled={isLoading}>
        {isLoading ? 'Opening…' : `Begin with ${world.representativeName}`}
      </button>
      <p className="doorway__footnote">This conversation is built from real sources you can check.</p>
    </div>
  );
}
