import { describe, expect, it } from 'vitest';
import { eraFor } from './eras';

describe('eraFor', () => {
  it('puts a world in the era its time window opens in', () => {
    expect(eraFor(150)).toMatchObject({ no: 'I', name: 'Early Church', tint: '#C9973A' });
    expect(eraFor(330)).toMatchObject({ no: 'II', name: 'Imperial Church', tint: '#7E9B6E' });
    expect(eraFor(1520)).toMatchObject({ no: 'VII', name: 'Reformation', tint: '#6C8DB5' });
  });

  it('changes era on the census date itself', () => {
    expect(eraFor(311).no).toBe('I');
    expect(eraFor(312).no).toBe('II');
    expect(eraFor(1906).no).toBe('X');
  });

  it('falls back to the first era before it, and to gold where the census names no tint', () => {
    expect(eraFor(30).no).toBe('I');
    expect(eraFor(800)).toMatchObject({ no: 'IV', tint: '#D9B35C' });
  });
});
