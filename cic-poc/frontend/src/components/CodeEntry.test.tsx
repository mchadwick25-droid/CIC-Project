import { cleanup, fireEvent, render, screen } from '@testing-library/react';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';

const CODE = 'ABCD2345EFGH6789JKLM';

async function load(enabled: boolean) {
  vi.resetModules();
  vi.stubEnv('VITE_DEEPER_ENABLED', enabled ? 'on' : '');
  const { CodeEntry } = await import('./CodeEntry');
  const deeper = await import('../lib/deeper');
  return { CodeEntry, deeper };
}

beforeEach(() => localStorage.clear());
afterEach(() => {
  cleanup();
  vi.unstubAllEnvs();
});

describe('CodeEntry', () => {
  it('shows nothing when the app is built with the module off', async () => {
    const { CodeEntry } = await load(false);
    const { container } = render(<CodeEntry />);
    expect(container).toBeEmptyDOMElement();
  });

  it('opens a field, takes a code, and says it is saved', async () => {
    const { CodeEntry } = await load(true);
    render(<CodeEntry />);
    fireEvent.click(screen.getByRole('button', { name: 'I have a code' }));
    fireEvent.change(screen.getByLabelText('Your code'), { target: { value: 'abcd 2345 efgh 6789 jklm' } });
    fireEvent.click(screen.getByRole('button', { name: 'Use this code' }));
    expect(screen.getByRole('status')).toHaveTextContent('Code saved on this device.');
    expect(screen.getByRole('button', { name: 'Remove code' })).toBeInTheDocument();
  });

  it('refuses a bad entry in plain words and keeps the field open', async () => {
    const { CodeEntry } = await load(true);
    render(<CodeEntry />);
    fireEvent.click(screen.getByRole('button', { name: 'I have a code' }));
    fireEvent.change(screen.getByLabelText('Your code'), { target: { value: 'hello' } });
    fireEvent.click(screen.getByRole('button', { name: 'Use this code' }));
    expect(screen.getByRole('alert')).toHaveTextContent("That doesn't look like a code. Check it and try again.");
    expect(screen.getByLabelText('Your code')).toBeInTheDocument();
  });

  it('shows the balance the server reported, singular and plural, and never a price', async () => {
    const { CodeEntry, deeper } = await load(true);
    deeper.saveCode(CODE);
    const { container } = render(<CodeEntry />);
    deeper.setRemaining(12);
    expect(await screen.findByText('12 exchanges left on your code.')).toBeInTheDocument();
    deeper.setRemaining(1);
    expect(await screen.findByText('1 exchange left on your code.')).toBeInTheDocument();
    expect(container.textContent).not.toMatch(/[$€£]|price|\bcost/i);
  });

  it('removes the code', async () => {
    const { CodeEntry, deeper } = await load(true);
    deeper.saveCode(CODE);
    render(<CodeEntry />);
    fireEvent.click(screen.getByRole('button', { name: 'Remove code' }));
    expect(screen.getByRole('button', { name: 'I have a code' })).toBeInTheDocument();
    expect(deeper.codeHeaders()).toEqual({});
  });
});
