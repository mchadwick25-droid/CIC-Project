/**
 * The launch system (Mark's ruling, 2026-08-28): the world cards launch
 * BOTH kinds of conversation, with clear differentiation - the Interview
 * is one click and you are in the room; the Table is convened on purpose,
 * from here and only here, with guidance on what sits well together.
 * The friction gradient is deliberate: the easy thing is the cheap thing,
 * and a Table is a fuller sitting.
 */
import { ArrivingLockup } from '../components/ArrivingLockup';
import { PAIRINGS, suggestionsFor } from '../data/pairings';
import type { WorldEntry } from '../data/worlds';

const TABLE_SEAT_LIMIT = 3;

interface LaunchProps {
  worlds: WorldEntry[];
  isLoading: boolean;
  error: string | null;
  seated: string[];
  tableFocus: boolean;
  convening: boolean;
  tableError: string | null;
  onBeginInterview: (worldKey: string) => void;
  onToggleSeat: (worldKey: string) => void;
  onSeatPairing: (worldKeys: string[]) => void;
  onConvene: () => void;
}

export function Launch({
  worlds, isLoading, error, seated, tableFocus, convening, tableError,
  onBeginInterview, onToggleSeat, onSeatPairing, onConvene,
}: LaunchProps) {
  const byKey = new Map(worlds.map((w) => [w.worldKey, w]));
  const seatedWorlds = seated.map((k) => byKey.get(k)).filter((w): w is WorldEntry => w !== undefined);
  const suggestions = seated.length === 0 ? PAIRINGS : suggestionsFor(seated);
  const canConvene = seated.length >= 2 && seated.length <= TABLE_SEAT_LIMIT;

  return (
    <div className="launch">
      <ArrivingLockup />
      {error && <div className="conversation__error" style={{ margin: '0 var(--spacing-lg)' }}>{error}</div>}
      {isLoading && !error && <p className="world-list__loading sans">Gathering the worlds…</p>}

      <div className="world-list">
        {worlds.map((world) => {
          const isSeated = seated.includes(world.worldKey);
          const seatsFull = !isSeated && seated.length >= TABLE_SEAT_LIMIT;
          return (
            <div key={world.worldKey} className={`world-card${isSeated ? ' world-card--seated' : ''}`}>
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
                <div className="world-card__actions">
                  <button
                    type="button"
                    className="world-card__interview sans"
                    style={{ background: world.accentColor }}
                    onClick={() => onBeginInterview(world.worldKey)}
                  >
                    Begin the Interview
                  </button>
                  <button
                    type="button"
                    className="world-card__seat sans"
                    onClick={() => onToggleSeat(world.worldKey)}
                    disabled={seatsFull}
                    aria-pressed={isSeated}
                  >
                    {isSeated ? 'Seated at the Table ✓' : 'Add to the Table'}
                  </button>
                </div>
              </div>
            </div>
          );
        })}
      </div>

      <div className={`table-field${tableFocus ? ' table-field--focus' : ''}`} id="table-field">
        <h2 className="table-field__title">Convene a Table</h2>
        <p className="table-field__intro">
          A Table seats two or three of these voices in one conversation. Each question you bring is answered around
          the table in turn — genuinely different ways of thinking, side by side — for a sitting of five rounds. It
          asks a little more of you than an interview, and gives back more than one world at a time.
        </p>

        {suggestions.length > 0 && (
          <div className="table-field__suggestions">
            <div className="table-field__label sans">{seated.length === 0 ? 'Seatings that sit well together' : 'Complete this seating'}</div>
            {suggestions.map((p) => (
              <button key={p.id} type="button" className="pairing" onClick={() => onSeatPairing(p.worldKeys)}>
                <span className="pairing__title sans">
                  {p.title}
                  {p.proven && <span className="pairing__proven sans"> · the proven pairing</span>}
                </span>
                <span className="pairing__names sans">
                  {p.worldKeys.map((k) => byKey.get(k)?.representativeName ?? k).join(' · ')}
                </span>
                <span className="pairing__why">{p.why}</span>
              </button>
            ))}
          </div>
        )}

        {tableError && <div className="conversation__error">{tableError}</div>}

        <div className="table-field__convene">
          <div className="table-field__seats sans">
            {seatedWorlds.length === 0
              ? 'No seats chosen yet — add voices from the cards above, or pick a seating.'
              : seatedWorlds.map((w) => (
                  <button key={w.worldKey} type="button" className="seat-chip sans" style={{ borderColor: w.accentColor }} onClick={() => onToggleSeat(w.worldKey)}>
                    {w.representativeName} <span aria-hidden="true">×</span>
                  </button>
                ))}
          </div>
          <button type="button" className="table-field__button" onClick={onConvene} disabled={!canConvene || convening}>
            {convening ? 'Convening…' : seated.length < 2 ? 'Seat at least two voices' : 'Convene the Table'}
          </button>
        </div>
      </div>
    </div>
  );
}
