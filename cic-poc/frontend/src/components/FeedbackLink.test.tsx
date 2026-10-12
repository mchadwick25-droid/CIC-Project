import { render, screen } from '@testing-library/react';
import { describe, expect, it } from 'vitest';
import { FeedbackLink } from './FeedbackLink';

describe('FeedbackLink', () => {
  it('opens the feedback form in a new tab', () => {
    render(<FeedbackLink />);
    const link = screen.getByRole('link', { name: 'Tell us what you found' });
    expect(link).toHaveAttribute('href', 'https://tally.so/r/PdMgbd');
    expect(link).toHaveAttribute('target', '_blank');
    expect(link.getAttribute('rel')).toContain('noopener');
  });
});
