/**
 * The name/figure bridge's own inline mark (VR_1A_Transparency_Gap_
 * 2026-08-09.md): a figure named in a turn's text, using InlineBridge's
 * shared hover/click (desktop) and tap/tap-through (phone) grammar. Level
 * 2 is the one-line bridge_line every figure record already carries;
 * Level 3 adds both recorded names (in-world and scholarly, whichever the
 * voice actually said) and what's known of the dates - the deeper
 * discovery, not just a definition.
 */
import type { FigureUsed } from '../types/conversation';
import { InlineBridge } from './InlineBridge';

function formatDates(dates: FigureUsed['dates']): string | null {
  const parts = Object.entries(dates)
    .filter(([, value]) => value)
    .map(([key, value]) => `${key}: ${value}`);
  return parts.length ? parts.join(' · ') : null;
}

interface FigureBridgeMarkProps {
  label: string;
  figure: FigureUsed;
}

export function FigureBridgeMark({ label, figure }: FigureBridgeMarkProps) {
  const dates = formatDates(figure.dates);
  return (
    <InlineBridge
      label={label}
      markClassName="name-bridge-mark"
      level2={<p>{figure.bridge_line}</p>}
      level3Title="Who is this?"
      level3={
        <>
          <ul className="level3__names">
            {figure.names.map((n) => (
              <li key={n.tag}>
                <span className="level3__names-tag">{n.tag === 'in-world' ? 'Called, in this world' : 'Known to scholars as'}</span>
                {n.name}
              </li>
            ))}
          </ul>
          {figure.bridge_line && <p>{figure.bridge_line}</p>}
          {dates && <p className="level3__dates">{dates}</p>}
        </>
      }
    />
  );
}
