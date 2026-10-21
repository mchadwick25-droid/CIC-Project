import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import { peakBalance } from './balancePeak';

describe('peakBalance', () => {
  beforeEach(() => localStorage.clear());
  afterEach(() => vi.restoreAllMocks());

  it('keeps the most tokens this browser has seen', () => {
    expect(peakBalance(550)).toBe(550);
    expect(peakBalance(300)).toBe(550);
    expect(peakBalance(1100)).toBe(1100);
    expect(peakBalance(40)).toBe(1100);
  });

  it('measures against the balance in view when storage is blocked', () => {
    vi.spyOn(Storage.prototype, 'getItem').mockImplementation(() => {
      throw new Error('blocked');
    });
    expect(peakBalance(275)).toBe(275);
  });
});
