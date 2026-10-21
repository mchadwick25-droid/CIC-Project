import { act, cleanup, render } from '@testing-library/react';
import { afterEach, describe, expect, it, vi } from 'vitest';
import { Enter } from './Enter';

afterEach(() => {
  cleanup();
  vi.useRealTimers();
});

describe('Enter', () => {
  it('opens a new block on the next frame, and shows a block already on the page open at once', () => {
    vi.useFakeTimers();
    const { container } = render(
      <>
        <Enter>new</Enter>
        <Enter still>old</Enter>
      </>,
    );
    const [fresh, old] = Array.from(container.querySelectorAll('.enter'));
    expect(fresh.classList.contains('enter--open')).toBe(false);
    expect(old.classList.contains('enter--open')).toBe(true);
    act(() => {
      vi.advanceTimersByTime(50);
    });
    expect(fresh.classList.contains('enter--open')).toBe(true);
  });

  it('closes smoothly, then leaves the page', () => {
    vi.useFakeTimers();
    const { container, rerender } = render(<Enter still>hello</Enter>);
    rerender(<Enter still shown={false}>hello</Enter>);
    expect(container.querySelector('.enter--open')).toBeNull();
    expect(container.textContent).toBe('hello');
    act(() => {
      vi.advanceTimersByTime(800);
    });
    expect(container.textContent).toBe('');
  });

  it('opens again from nothing when a closed block comes back', () => {
    vi.useFakeTimers();
    const { container, rerender } = render(<Enter still>hello</Enter>);
    rerender(<Enter still shown={false}>hello</Enter>);
    act(() => {
      vi.advanceTimersByTime(800);
    });
    expect(container.textContent).toBe('');
    rerender(<Enter still shown>hello</Enter>);
    expect(container.querySelector('.enter')).not.toBeNull();
    expect(container.querySelector('.enter--open')).toBeNull();
    act(() => {
      vi.advanceTimersByTime(50);
    });
    expect(container.querySelector('.enter--open')).not.toBeNull();
  });
});
