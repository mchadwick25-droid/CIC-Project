/**
 * The name/figure bridge's own inline mark: a figure named in a turn's
 * text, using InlineBridge's shared hover/click (desktop) and
 * tap/tap-through (phone) grammar.
 *
 * Level 3 leads with what's actually being said here and where it comes
 * from (`sourced_by` - the real primary sources behind this sentence, per
 * engine.m4.name_bridge.attach_cited_sources), not with the figure's own
 * biography: the point is not just who a named figure is, but the
 * reference behind what they're saying, so a participant can actually
 * look at the source document. Who-this-is (both recorded names,
 * whichever the voice actually said, and the dates) stays, but as the
 * second thing, not the point.
 */
import type { FigureUsed } from '../types/conversation';
import { InlineBridge } from './InlineBridge';
import { SourceList } from './SourceList';

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
      level3Title={figure.matched_name}
      level3={
        <>
          <p className="level3__section-label">What's said here, sourced from</p>
          <SourceList sources={figure.sourced_by} empty="Nothing in this sentence was drawn from a source." />

          <p className="level3__section-label">Who this is</p>
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
