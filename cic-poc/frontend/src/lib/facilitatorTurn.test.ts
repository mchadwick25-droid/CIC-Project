import { describe, expect, it } from 'vitest';
import { facilitatorClass, safetyAttributes } from './facilitatorTurn';

describe('facilitatorTurn', () => {
  it('sets a safety turn apart, and announces it', () => {
    expect(facilitatorClass(false, 'safety')).toBe('turn turn--facilitator turn--safety');
    expect(safetyAttributes('safety')).toEqual({ role: 'alert', 'data-hold-start': 'true' });
  });

  it('leaves every other Facilitator turn as it was, the line for an unread message included', () => {
    for (const kind of ['limit', 'bridge', 'close', 'door', undefined]) {
      expect(facilitatorClass(false, kind)).toBe('turn turn--facilitator');
      expect(safetyAttributes(kind)).toEqual({});
    }
    expect(facilitatorClass(true, 'safety')).toBe('turn turn--facilitator turn--welcome');
  });
});
