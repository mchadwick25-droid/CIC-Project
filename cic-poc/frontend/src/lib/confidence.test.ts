import { describe, expect, it } from 'vitest';
import { confidencePhrase } from './confidence';

describe('confidencePhrase', () => {
  it.each([
    ['Documented', 'Recorded directly in a source from the time.'],
    ['Widely Accepted', 'What historians broadly agree happened.'],
    ['Dominant Modern Reconstruction', 'The leading modern reading of the evidence.'],
    ['Contested', 'Historians disagree about this.'],
    ['Inferential-Thin', 'Based on thin evidence, mostly inference.'],
  ])('maps formation_confidence %s to its own plain phrase', (level, expected) => {
    expect(confidencePhrase({ formation_confidence: level })).toBe(expected);
  });

  it('returns null for a null confidence envelope (never invents a phrase)', () => {
    expect(confidencePhrase(null)).toBeNull();
  });

  it('returns null for an undefined confidence envelope', () => {
    expect(confidencePhrase(undefined)).toBeNull();
  });

  it('returns null when formation_confidence is missing from the envelope', () => {
    expect(confidencePhrase({ citation_specificity: 'A' })).toBeNull();
  });

  it("returns null for a formation_confidence value outside the schema's five enum values (R8: 'Not Attested' is not a sixth value)", () => {
    expect(confidencePhrase({ formation_confidence: 'Not Attested' })).toBeNull();
  });
});
