import { act, cleanup, fireEvent, render, screen } from '@testing-library/react';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';

const CODE = 'ABCD2345EFGH6789JKLM';

async function load(enabled: boolean) {
  vi.resetModules();
  vi.stubEnv('VITE_DEEPER_ENABLED', enabled ? 'on' : '');
  const { GoDeeperPanel } = await import('./GoDeeperPanel');
  const deeper = await import('../lib/deeper');
  return { GoDeeperPanel, deeper };
}

const openPanel = () => fireEvent.click(screen.getByRole('button', { name: 'Go deeper' }));

beforeEach(() => localStorage.clear());
afterEach(() => {
  cleanup();
  vi.unstubAllEnvs();
});

describe('GoDeeperPanel', () => {
  it('shows nothing when the app is built with the module off', async () => {
    const { GoDeeperPanel, deeper } = await load(false);
    const { container } = render(<GoDeeperPanel />);
    expect(container).toBeEmptyDOMElement();
    act(() => deeper.noteLimit());
    expect(container).toBeEmptyDOMElement();
  });

  it('stays closed until the person asks, and closes again', async () => {
    const { GoDeeperPanel } = await load(true);
    render(<GoDeeperPanel />);
    expect(screen.queryByRole('complementary')).not.toBeInTheDocument();
    openPanel();
    expect(screen.getByRole('complementary', { name: 'Go deeper' })).toHaveTextContent(
      'Tokens pay for each new conversation and each round. Add more any time. Your conversation stays open.'
    );
    fireEvent.keyDown(window, { key: 'Escape' });
    expect(screen.queryByRole('complementary')).not.toBeInTheDocument();
    openPanel();
    fireEvent.click(screen.getByRole('button', { name: 'Close' }));
    expect(screen.queryByRole('complementary')).not.toBeInTheDocument();
  });

  it('opens when a turn comes back refused', async () => {
    const { GoDeeperPanel, deeper } = await load(true);
    render(<GoDeeperPanel />);
    act(() => deeper.noteLimit());
    expect(screen.getByRole('complementary', { name: 'Go deeper' })).toBeInTheDocument();
  });

  it('takes a code in the panel and says it is saved', async () => {
    const { GoDeeperPanel, deeper } = await load(true);
    render(<GoDeeperPanel />);
    openPanel();
    fireEvent.click(screen.getByRole('button', { name: 'I have a code' }));
    fireEvent.change(screen.getByLabelText('Your code'), { target: { value: 'abcd 2345 efgh 6789 jklm' } });
    fireEvent.click(screen.getByRole('button', { name: 'Use this code' }));
    expect(await screen.findByRole('button', { name: 'Show my code' })).toBeInTheDocument();
    expect(deeper.codeHeaders()).toEqual({ 'X-Cic-Code': CODE });
  });

  it('refuses a bad entry in plain words and keeps the field open', async () => {
    const { GoDeeperPanel } = await load(true);
    render(<GoDeeperPanel />);
    openPanel();
    fireEvent.click(screen.getByRole('button', { name: 'I have a code' }));
    fireEvent.change(screen.getByLabelText('Your code'), { target: { value: 'hello' } });
    fireEvent.click(screen.getByRole('button', { name: 'Use this code' }));
    expect(await screen.findByRole('alert')).toHaveTextContent("That doesn't look like a code. Check it and try again.");
    expect(screen.getByLabelText('Your code')).toBeInTheDocument();
  });

  it('shows a token count with the thousands grouped, and never a price', async () => {
    const { GoDeeperPanel, deeper } = await load(true);
    deeper.saveCode(CODE);
    const { container } = render(<GoDeeperPanel />);
    act(() => deeper.reportBalance(CODE, 1100, false));
    expect(await screen.findByText('1,100 tokens left.')).toBeInTheDocument();
    act(() => deeper.reportBalance(CODE, 40, false));
    expect(await screen.findByText('40 tokens left.')).toBeInTheDocument();
    openPanel();
    expect(container.textContent).not.toMatch(/[$€£]|price|\bcost/i);
  });

  it('shows a free visitor their free tokens left in the strip, and a code holder their code count instead', async () => {
    const { GoDeeperPanel, deeper } = await load(true);
    render(<GoDeeperPanel />);
    expect(screen.queryByText(/free tokens left/)).not.toBeInTheDocument();
    act(() => deeper.reportFreeLeft(1100));
    expect(await screen.findByText('1,100 free tokens left.')).toBeInTheDocument();
    act(() => deeper.reportFreeLeft(440));
    expect(await screen.findByText('440 free tokens left.')).toBeInTheDocument();
    act(() => {
      deeper.saveCode(CODE);
      deeper.reportBalance(CODE, 1100, false);
    });
    expect(await screen.findByText('1,100 tokens left.')).toBeInTheDocument();
    expect(screen.queryByText(/free tokens left/)).not.toBeInTheDocument();
  });

  it('shows no free count while the module is off', async () => {
    const { GoDeeperPanel, deeper } = await load(false);
    const { container } = render(<GoDeeperPanel />);
    act(() => deeper.reportFreeLeft(1100));
    expect(container.textContent).toBe('');
  });

  it('says tokens are running low, and always offers more', async () => {
    const open = vi.fn().mockReturnValue({});
    vi.stubGlobal('open', open);
    const { GoDeeperPanel, deeper } = await load(true);
    deeper.saveCode(CODE);
    render(<GoDeeperPanel />);
    act(() => deeper.reportBalance(CODE, 90, true));
    expect(await screen.findAllByText(/90 tokens left\. Your tokens are running low\./)).not.toHaveLength(0);
    openPanel();
    fireEvent.click(screen.getByRole('button', { name: 'Get more tokens' }));
    expect(open).toHaveBeenCalledWith('https://churchinconversation.com/go-deeper.html', 'cic-get-code', expect.any(String));
    vi.unstubAllGlobals();
  });

  it('opens the page in this tab when the browser blocks the popup', async () => {
    vi.stubGlobal('open', vi.fn().mockReturnValue(null));
    const assign = vi.fn();
    vi.stubGlobal('location', { ...window.location, assign });
    const { GoDeeperPanel } = await load(true);
    render(<GoDeeperPanel />);
    openPanel();
    fireEvent.click(screen.getByRole('button', { name: 'Get more tokens' }));
    expect(assign).toHaveBeenCalledWith('https://churchinconversation.com/go-deeper.html');
    vi.unstubAllGlobals();
  });

  it('keeps a code out of sight until the person asks, and hides it again', async () => {
    const { GoDeeperPanel, deeper } = await load(true);
    deeper.saveCode(CODE);
    const { container } = render(<GoDeeperPanel />);
    openPanel();
    expect(container.textContent).not.toContain('ABCD');
    fireEvent.click(screen.getByRole('button', { name: 'Show my code' }));
    expect(screen.getByText('Your code is ABCD 2345 EFGH 6789 JKLM. Keep it safe. Enter it on another device to use your tokens there.')).toBeInTheDocument();
    fireEvent.click(screen.getByRole('button', { name: 'Hide my code' }));
    expect(container.textContent).not.toContain('ABCD');
  });

  it('does not bring a code back on screen when the panel opens itself after it was closed', async () => {
    const { GoDeeperPanel, deeper } = await load(true);
    deeper.saveCode(CODE);
    const { container } = render(<GoDeeperPanel />);
    openPanel();
    fireEvent.click(screen.getByRole('button', { name: 'Show my code' }));
    expect(container.textContent).toContain('ABCD 2345');
    fireEvent.click(screen.getByRole('button', { name: 'Close' }));
    act(() => deeper.noteLimit());
    expect(screen.getByRole('complementary', { name: 'Go deeper' })).toBeInTheDocument();
    expect(container.textContent).not.toContain('ABCD');
    expect(screen.getByRole('button', { name: 'Show my code' })).toBeInTheDocument();
  });

  it('returns focus to the Go deeper control when the panel closes', async () => {
    const { GoDeeperPanel } = await load(true);
    render(<GoDeeperPanel />);
    openPanel();
    fireEvent.click(screen.getByRole('button', { name: 'Close' }));
    expect(screen.getByRole('button', { name: 'Go deeper' })).toHaveFocus();
    openPanel();
    fireEvent.keyDown(window, { key: 'Escape' });
    expect(screen.getByRole('button', { name: 'Go deeper' })).toHaveFocus();
  });

  it('removes the code in use', async () => {
    const { GoDeeperPanel, deeper } = await load(true);
    deeper.saveCode(CODE);
    render(<GoDeeperPanel />);
    openPanel();
    fireEvent.click(screen.getByRole('button', { name: 'Remove code' }));
    expect(screen.queryByRole('button', { name: 'Show my code' })).not.toBeInTheDocument();
    expect(deeper.codeHeaders()).toEqual({});
  });

  it('saves the code a popup sends back, and no code sent from anywhere else', async () => {
    const { GoDeeperPanel, deeper } = await load(true);
    render(<GoDeeperPanel />);
    fireEvent(window, new MessageEvent('message', { origin: 'https://evil.example', data: { type: 'cic-deeper-code', codes: [CODE] } }));
    expect(deeper.codeHeaders()).toEqual({});
    fireEvent(window, new MessageEvent('message', { origin: 'https://churchinconversation.com', data: { type: 'cic-deeper-code', codes: [CODE] } }));
    expect(deeper.codeHeaders()).toEqual({ 'X-Cic-Code': CODE });
  });

  it('opens at once for a code that came with a link, asks before using it, says it would be added to one already held, and only then saves it', async () => {
    window.history.replaceState(null, '', `/#cic-claim=${'r'.repeat(22)}`);
    const fetchMock = vi.fn().mockResolvedValue(new Response(JSON.stringify({ codes: [CODE], tokens: 40 }), { status: 200 }));
    vi.stubGlobal('fetch', fetchMock);
    localStorage.setItem('cic_codes', JSON.stringify(['BCDE2345EFGH6789JKLM']));
    const { GoDeeperPanel } = await load(true);
    render(<GoDeeperPanel />);
    expect(screen.getByText(/A code came with this link\. Use it\?/)).toHaveTextContent('You already have a code. This one will be added to it.');
    expect(fetchMock).not.toHaveBeenCalled();
    expect(JSON.parse(localStorage.getItem('cic_codes') ?? '[]')).toEqual(['BCDE2345EFGH6789JKLM']);
    fireEvent.click(screen.getByRole('button', { name: 'Use it' }));
    expect(await screen.findByRole('button', { name: 'Show my code' })).toBeInTheDocument();
    expect(JSON.parse(localStorage.getItem('cic_codes') ?? '[]')).toEqual(['BCDE2345EFGH6789JKLM', CODE]);
    vi.unstubAllGlobals();
  });

  it('keeps the held code when the person says not now', async () => {
    window.history.replaceState(null, '', `/#cic-claim=${'r'.repeat(22)}`);
    localStorage.setItem('cic_codes', JSON.stringify([CODE]));
    const { GoDeeperPanel } = await load(true);
    render(<GoDeeperPanel />);
    fireEvent.click(screen.getByRole('button', { name: 'Not now' }));
    expect(await screen.findByRole('button', { name: 'Show my code' })).toBeInTheDocument();
    expect(JSON.parse(localStorage.getItem('cic_codes') ?? '[]')).toEqual([CODE]);
  });
});

describe('GoDeeperPanel, pilot', () => {
  it('opens beside the conversation with the pack ready, in the approved words', async () => {
    vi.resetModules();
    vi.stubEnv('VITE_DEEPER_ENABLED', 'on');
    vi.stubGlobal(
      'fetch',
      vi.fn().mockResolvedValue({ status: 200, ok: true, json: async () => ({ joined: true, code: 'ABCD 2345 EFGH 6789 JKLM', tokens: 1100, conversations: 10 }) })
    );
    window.history.replaceState(null, '', '/#cic-pilot=general');
    const { GoDeeperPanel } = await import('./GoDeeperPanel');
    render(<GoDeeperPanel />);
    const panel = await screen.findByRole('complementary', { name: 'Go deeper' });
    await vi.waitFor(() => expect(panel).toHaveTextContent('Your free pack is ready'));
    expect(panel).toHaveTextContent('You have 1,100 tokens, about 10 conversations. They are saved in this browser, so there is nothing to copy.');
    fireEvent.click(screen.getByRole('button', { name: 'Start a conversation' }));
    expect(screen.queryByRole('complementary')).not.toBeInTheDocument();
    vi.unstubAllGlobals();
  });

  it('says a shared connection has taken its share, with no link to a form', async () => {
    vi.resetModules();
    vi.stubEnv('VITE_DEEPER_ENABLED', 'on');
    vi.stubGlobal('fetch', vi.fn().mockResolvedValue({ status: 409, ok: false, json: async () => ({ joined: false, reason: 'address_limit' }) }));
    window.history.replaceState(null, '', '/#cic-pilot=general');
    const { GoDeeperPanel } = await import('./GoDeeperPanel');
    render(<GoDeeperPanel />);
    expect(await screen.findByText('This connection has already taken the free packs the pilot allows.')).toBeInTheDocument();
    expect(screen.queryByRole('link')).not.toBeInTheDocument();
    vi.unstubAllGlobals();
  });
});
