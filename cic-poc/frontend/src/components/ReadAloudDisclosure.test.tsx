import { render, within } from '@testing-library/react';
import { beforeEach, describe, expect, it } from 'vitest';
import { ReadAloudDisclosure } from './ReadAloudDisclosure';

describe('ReadAloudDisclosure', () => {
  beforeEach(() => {
    sessionStorage.clear();
  });

  it("shows Mark's Option A sentence, naming the actual representative, on first render", () => {
    const { container } = render(<ReadAloudDisclosure representativeName="Julian of Norwich" turnKey={0} />);
    expect(
      within(container).getByText("This reads the words on screen aloud in your device's own voice — it isn't Julian of Norwich speaking.")
    ).toBeInTheDocument();
  });

  it('disappears once a new turn becomes the latest one - one disclosure, not a permanent banner', () => {
    const { container, rerender } = render(<ReadAloudDisclosure representativeName="Julian of Norwich" turnKey={0} />);
    expect(within(container).getByText(/This reads the words on screen aloud/)).toBeInTheDocument();

    rerender(<ReadAloudDisclosure representativeName="Julian of Norwich" turnKey={1} />);

    expect(within(container).queryByText(/This reads the words on screen aloud/)).not.toBeInTheDocument();
  });

  it('does not reappear on a fresh mount in the same tab once already seen (survives a reload)', () => {
    const first = render(<ReadAloudDisclosure representativeName="Julian of Norwich" turnKey={0} />);
    first.unmount();

    // A reload creates an entirely new component tree, but sessionStorage
    // (unlike React state) survives it - the same guarantee this app's own
    // lib/sessionStore.ts already relies on for "the same tab."
    const { container } = render(<ReadAloudDisclosure representativeName="Julian of Norwich" turnKey={0} />);
    expect(within(container).queryByText(/This reads the words on screen aloud/)).not.toBeInTheDocument();
  });
});
