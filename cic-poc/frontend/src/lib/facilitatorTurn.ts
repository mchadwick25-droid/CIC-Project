/** How a Facilitator turn is drawn: a safety turn stands apart from the narration around it. */
export function facilitatorClass(welcome: boolean, kind: string | undefined): string {
  const base = welcome ? 'turn turn--facilitator turn--welcome' : 'turn turn--facilitator';
  return kind === 'safety' && !welcome ? `${base} turn--safety` : base;
}

/** A safety turn is announced when it arrives, and marks where the transcript scrolls to so its first line is read. */
export function safetyAttributes(kind: string | undefined): { role?: 'alert'; 'data-hold-start'?: 'true' } {
  return kind === 'safety' ? { role: 'alert', 'data-hold-start': 'true' } : {};
}
