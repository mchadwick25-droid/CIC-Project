import { cleanup, fireEvent, render, screen } from '@testing-library/react';
import { afterEach, describe, expect, it, vi } from 'vitest';
import { FeedbackPopup } from './FeedbackPopup';

describe('FeedbackPopup', () => {
  afterEach(cleanup);

  it('links to the form with the moment it came from, in a new tab', () => {
    render(<FeedbackPopup variant="ending" turns={0} onClose={() => {}} />);
    const link = screen.getByRole('link', { name: 'Tell us' });
    expect(link).toHaveAttribute('href', 'https://tally.so/r/PdMgbd?from=ending');
    expect(link).toHaveAttribute('target', '_blank');
    expect(link.getAttribute('rel')).toContain('noopener');
  });

  it('says how many questions the last visit had', () => {
    const { rerender } = render(<FeedbackPopup variant="return" turns={1} onClose={() => {}} />);
    expect(screen.getByText('Last time you stopped after one question. What happened?')).toBeInTheDocument();
    rerender(<FeedbackPopup variant="return" turns={3} onClose={() => {}} />);
    expect(screen.getByText('Last time you stopped after 3 questions. What happened?')).toBeInTheDocument();
  });

  it('closes on the decline button, on the link, and on Escape', () => {
    const onClose = vi.fn();
    render(<FeedbackPopup variant="invite" turns={0} onClose={onClose} />);
    fireEvent.click(screen.getByRole('button', { name: 'Not now' }));
    fireEvent.click(screen.getByRole('link', { name: 'Share feedback' }));
    fireEvent.keyDown(document, { key: 'Escape' });
    expect(onClose).toHaveBeenCalledTimes(3);
  });
});
