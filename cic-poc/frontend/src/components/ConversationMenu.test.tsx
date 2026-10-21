import { cleanup, fireEvent, render, screen } from '@testing-library/react';
import { createRef } from 'react';
import { afterEach, describe, expect, it, vi } from 'vitest';
import { ConversationMenu } from './ConversationMenu';

afterEach(cleanup);

function setup(extra: Partial<Parameters<typeof ConversationMenu>[0]> = {}) {
  const props = {
    buttonRef: createRef<HTMLButtonElement>(),
    aboutLabel: 'About Theon',
    onAbout: vi.fn(),
    onFeedback: vi.fn(),
    onReport: vi.fn(),
    onLeave: vi.fn(),
    onDelete: vi.fn(),
    ...extra,
  };
  render(<ConversationMenu {...props} />);
  return props;
}

const openMenu = () => fireEvent.click(screen.getByRole('button', { name: 'More' }));

describe('ConversationMenu', () => {
  it('stays shut until opened, then lists the five choices with Delete last', () => {
    setup();
    expect(screen.queryByRole('menu')).not.toBeInTheDocument();
    openMenu();
    const names = screen.getAllByRole('menuitem').map((item) => item.textContent);
    expect(names).toEqual(['About Theon', 'Tell us what you think', 'Report a problem', 'Leave for now', 'Delete this conversation']);
    expect(screen.getByRole('button', { name: 'More' })).toHaveAttribute('aria-expanded', 'true');
  });

  it('drops Report and Delete when the page has nothing to report or delete', () => {
    setup({ onReport: undefined, onDelete: undefined });
    openMenu();
    expect(screen.getAllByRole('menuitem').map((item) => item.textContent)).toEqual(['About Theon', 'Tell us what you think', 'Leave for now']);
  });

  it('runs the choice and closes', () => {
    const props = setup();
    openMenu();
    fireEvent.click(screen.getByRole('menuitem', { name: 'Leave for now' }));
    expect(props.onLeave).toHaveBeenCalledTimes(1);
    expect(screen.queryByRole('menu')).not.toBeInTheDocument();
  });

  it('puts focus on the first choice, moves with the arrow keys and closes on Escape back to the button', () => {
    setup();
    openMenu();
    const items = screen.getAllByRole('menuitem');
    expect(items[0]).toHaveFocus();
    fireEvent.keyDown(items[0], { key: 'ArrowDown' });
    expect(items[1]).toHaveFocus();
    fireEvent.keyDown(items[1], { key: 'End' });
    expect(items[items.length - 1]).toHaveFocus();
    fireEvent.keyDown(items[items.length - 1], { key: 'Escape' });
    expect(screen.queryByRole('menu')).not.toBeInTheDocument();
    expect(screen.getByRole('button', { name: 'More' })).toHaveFocus();
  });

  it('closes on a press outside', () => {
    setup();
    openMenu();
    fireEvent.pointerDown(document.body);
    expect(screen.queryByRole('menu')).not.toBeInTheDocument();
  });
});
