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
    expect(await screen.findByRole('status')).toHaveTextContent('Code saved on this device.');
    expect(screen.getByRole('button', { name: 'Remove code' })).toBeInTheDocument();
  });

  it('refuses a bad entry in plain words and keeps the field open', async () => {
    const { CodeEntry } = await load(true);
    render(<CodeEntry />);
    fireEvent.click(screen.getByRole('button', { name: 'I have a code' }));
    fireEvent.change(screen.getByLabelText('Your code'), { target: { value: 'hello' } });
    fireEvent.click(screen.getByRole('button', { name: 'Use this code' }));
    expect(await screen.findByRole('alert')).toHaveTextContent("That doesn't look like a code. Check it and try again.");
    expect(screen.getByLabelText('Your code')).toBeInTheDocument();
  });

  it('shows the balance the server reported, singular and plural, and never a price', async () => {
    const { CodeEntry, deeper } = await load(true);
    deeper.saveCode(CODE);
    const { container } = render(<CodeEntry />);
    deeper.reportBalance(12, false);
    expect(await screen.findByText('12 exchanges left on your code.')).toBeInTheDocument();
    deeper.reportBalance(1, false);
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

  it('offers to get a code in a popup, and saves the code the popup sends back', async () => {
    const open = vi.fn().mockReturnValue({});
    vi.stubGlobal('open', open);
    const { CodeEntry } = await load(true);
    render(<CodeEntry />);
    fireEvent.click(screen.getByRole('button', { name: 'Get a code' }));
    expect(open).toHaveBeenCalledWith('https://churchinconversation.com/go-deeper.html', 'cic-get-code', expect.any(String));
    fireEvent(window, new MessageEvent('message', { origin: 'https://churchinconversation.com', data: { type: 'cic-deeper-code', codes: [CODE] } }));
    expect(await screen.findByText('Code saved on this device.')).toBeInTheDocument();
    vi.unstubAllGlobals();
  });

  it('opens the page in this tab when the browser blocks the popup', async () => {
    vi.stubGlobal('open', vi.fn().mockReturnValue(null));
    const assign = vi.fn();
    vi.stubGlobal('location', { ...window.location, assign });
    const { CodeEntry } = await load(true);
    render(<CodeEntry />);
    fireEvent.click(screen.getByRole('button', { name: 'Get a code' }));
    expect(assign).toHaveBeenCalledWith('https://churchinconversation.com/go-deeper.html');
    vi.unstubAllGlobals();
  });

  it('asks before using a code that came with a link, says it would replace one already held, and only then saves it', async () => {
    window.history.replaceState(null, '', `/#cic-claim=${'r'.repeat(22)}`);
    const fetchMock = vi.fn().mockResolvedValue(new Response(JSON.stringify({ codes: [CODE], exchanges: 40 }), { status: 200 }));
    vi.stubGlobal('fetch', fetchMock);
    localStorage.setItem('cic_codes', JSON.stringify(['BCDE2345EFGH6789JKLM']));
    const { CodeEntry } = await load(true);
    render(<CodeEntry />);
    expect(screen.getByText(/A code came with this link\. Use it\?/)).toHaveTextContent('You already have a code. This one will be added to it.');
    expect(fetchMock).not.toHaveBeenCalled();
    expect(JSON.parse(localStorage.getItem('cic_codes') ?? '[]')).toEqual(['BCDE2345EFGH6789JKLM']);
    fireEvent.click(screen.getByRole('button', { name: 'Use it' }));
    expect(await screen.findByText('Code saved on this device.')).toBeInTheDocument();
    expect(JSON.parse(localStorage.getItem('cic_codes') ?? '[]')).toEqual(['BCDE2345EFGH6789JKLM', CODE]);
    vi.unstubAllGlobals();
  });

  it('keeps the held code when the person says not now', async () => {
    window.history.replaceState(null, '', `/#cic-claim=${'r'.repeat(22)}`);
    localStorage.setItem('cic_codes', JSON.stringify([CODE]));
    const { CodeEntry } = await load(true);
    render(<CodeEntry />);
    fireEvent.click(screen.getByRole('button', { name: 'Not now' }));
    expect(await screen.findByRole('button', { name: 'Remove code' })).toBeInTheDocument();
    expect(JSON.parse(localStorage.getItem('cic_codes') ?? '[]')).toEqual([CODE]);
  });

  it('does not save a code sent from anywhere else', async () => {
    const { CodeEntry } = await load(true);
    render(<CodeEntry />);
    fireEvent(window, new MessageEvent('message', { origin: 'https://evil.example', data: { type: 'cic-deeper-code', codes: [CODE] } }));
    expect(screen.getByRole('button', { name: 'I have a code' })).toBeInTheDocument();
  });

  it('shows a getting-low line and a Get more button, and never hides the way to get more', async () => {
    const open = vi.fn().mockReturnValue({});
    vi.stubGlobal('open', open);
    const { CodeEntry, deeper } = await load(true);
    deeper.saveCode(CODE);
    render(<CodeEntry />);
    deeper.reportBalance(4, true);
    expect(await screen.findByText(/4 exchanges left on your code\. Your code is running low\./)).toBeInTheDocument();
    fireEvent.click(screen.getByRole('button', { name: 'Get more' }));
    expect(open).toHaveBeenCalled();
    deeper.reportBalance(40, false);
    expect(await screen.findByText('40 exchanges left on your code.')).toBeInTheDocument();
    expect(screen.getByRole('button', { name: 'Get more' })).toBeInTheDocument();
    vi.unstubAllGlobals();
  });
});
