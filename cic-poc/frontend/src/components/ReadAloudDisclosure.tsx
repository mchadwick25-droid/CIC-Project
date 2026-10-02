/**
 * A visible one-line note under the conversation bar the first time the
 * read-aloud control renders in a session - never a tooltip or
 * aria-describedby alone (a participant on touch never sees either).
 * The control's own accessible name is untouched by this - this is a
 * separate line, not the button's label.
 *
 * "The first time" is tied to the control's first target turn, not to
 * every render: shown while `turnKey` is still whatever it was when this
 * mounted, gone as soon as a new turn becomes the latest one - one
 * disclosure, not a permanent banner repeated on every turn after that.
 * `hasSeenReadAloudDisclosure`/`markReadAloudDisclosureSeen`
 * (lib/readAloud.ts) remember "already shown" across a reload of the
 * same tab - without that, reloading mid-conversation while the note is
 * still showing would look like a second "first time" once React state
 * resets.
 */
import { useEffect, useRef, useState } from 'react';
import { hasSeenReadAloudDisclosure, markReadAloudDisclosureSeen, readAloudDisclosureText } from '../lib/readAloud';

interface ReadAloudDisclosureProps {
  representativeName: string;
  turnKey: string | number;
}

export function ReadAloudDisclosure({ representativeName, turnKey }: ReadAloudDisclosureProps) {
  const [show, setShow] = useState(() => !hasSeenReadAloudDisclosure());
  const shownForKeyRef = useRef(turnKey);

  useEffect(() => {
    if (show) markReadAloudDisclosureSeen();
  }, [show]);

  useEffect(() => {
    if (turnKey !== shownForKeyRef.current) setShow(false);
  }, [turnKey]);

  if (!show) return null;

  return <div className="read-aloud-disclosure sans">{readAloudDisclosureText(representativeName)}</div>;
}
