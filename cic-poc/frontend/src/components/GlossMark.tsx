/**
 * The term card: the word's inline mark, a hover with its quick meaning,
 * how sure we are and how easily it is misheard, and a click page of
 * labelled layers.
 *
 * "In this world" and "How we hear it today" are the term's own split
 * fields, shown side by side. A term not yet split shows the whole
 * translational block under "In this world" alone. Where a term's source
 * names no vendored text, or no edition, the page says "unavailable"; it
 * never supplies a link or a date of its own.
 */
import type { GlossUsed, SourceReference } from '../types/conversation';
import { confidencePhrase } from '../lib/confidence';
import {
  TERM_LAYER_FRIENDS,
  TERM_LAYER_PLAIN,
  TERM_LAYER_RESTS_ON,
  TERM_LAYER_TODAY,
  TERM_LAYER_WORLD,
  TERM_RISK_PHRASES,
  TERM_UNAVAILABLE,
} from '../lib/markCopy';
import { EditionFacts } from './EditionFacts';
import { InlineBridge } from './InlineBridge';

interface GlossMarkProps {
  label: string;
  gloss: GlossUsed;
}

function Unavailable({ what }: { what: string }) {
  return (
    <span className="term-mark__unavailable">
      {what}: {TERM_UNAVAILABLE}
    </span>
  );
}

function RestsOn({ source }: { source: SourceReference }) {
  const spans = source.vendored ?? [];
  return (
    <li>
      <span>{source.citation ?? source.work ?? source.source_id}</span>
      {source.author && ` — ${source.author}`}
      {source.locus && `, ${source.locus}`}
      <br />
      {source.edition && <span>{source.edition}<br /></span>}
      <EditionFacts source={source} />
      <br />
      {spans.length > 0 ? (
        spans.map((ref) => (
          <span key={`${ref.file}:${ref.lines}`}>
            {ref.label ? `${ref.label} text` : 'Text'}: <code>{ref.file}</code>, lines {ref.lines}
          </span>
        ))
      ) : (
        <Unavailable what="Line span in the Library" />
      )}
    </li>
  );
}

export function GlossMark({ label, gloss }: GlossMarkProps) {
  const phrase = confidencePhrase(gloss.confidence);
  const risk = gloss.distortion_risk ? TERM_RISK_PHRASES[gloss.distortion_risk] : null;
  const split = Boolean(gloss.heard_today && gloss.meant_here);
  const worldSense = split ? gloss.meant_here : gloss.translational_sense;
  const id = gloss.id;
  const restsOn = gloss.rests_on ?? [];
  return (
    <InlineBridge
      label={label}
      markClassName="name-bridge-mark"
      level2={
        <>
          <p>{gloss.quick_meaning ?? gloss.plain_meaning}</p>
          {phrase && <p className="term-mark__confidence">{phrase}</p>}
          {risk && <p className="term-mark__flag">{risk}</p>}
        </>
      }
      level3Title={gloss.matched_name}
      level3={
        <>
          {gloss.plain_meaning && (
            <div className="term-mark__layer" role="group" aria-labelledby={`${id}-plain`}>
              <p className="term-mark__layer-label" id={`${id}-plain`}>{TERM_LAYER_PLAIN}</p>
              <p>{gloss.plain_meaning}</p>
            </div>
          )}

          {(worldSense || split) && (
            <div className={split ? 'term-mark__contrast' : undefined}>
              {split && (
                <div className="term-mark__layer" role="group" aria-labelledby={`${id}-today`}>
                  <p className="term-mark__layer-label" id={`${id}-today`}>{TERM_LAYER_TODAY}</p>
                  <p>{gloss.heard_today}</p>
                </div>
              )}
              <div className="term-mark__layer" role="group" aria-labelledby={`${id}-world`}>
                <p className="term-mark__layer-label" id={`${id}-world`}>{TERM_LAYER_WORLD}</p>
                <p>{worldSense}</p>
              </div>
            </div>
          )}

          {gloss.false_friend.length > 0 && (
            <div className="term-mark__layer" role="group" aria-labelledby={`${id}-friends`}>
              <p className="term-mark__layer-label" id={`${id}-friends`}>{TERM_LAYER_FRIENDS}</p>
              <ul className="level3__false-friend">
                {gloss.false_friend.map((f) => (
                  <li key={f}>{f}</li>
                ))}
              </ul>
            </div>
          )}

          <div className="term-mark__layer" role="group" aria-labelledby={`${id}-rests`}>
            <p className="term-mark__layer-label" id={`${id}-rests`}>{TERM_LAYER_RESTS_ON}</p>
            {restsOn.length > 0 ? (
              <ul>
                {restsOn.map((s, i) => (
                  <RestsOn key={`${s.source_id}-${i}`} source={s} />
                ))}
              </ul>
            ) : (
              <p><Unavailable what="Sources" /></p>
            )}
            {phrase && <p className="term-mark__confidence">{phrase}</p>}
          </div>
        </>
      }
    />
  );
}
