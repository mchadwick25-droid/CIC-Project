import { fireEvent, render, within } from '@testing-library/react';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import { ReadAloudControl } from './ReadAloudControl';

class FakeUtterance {
  onend: (() => void) | null = null;
  onerror: (() => void) | null = null;
  constructor(public text: string) {}
}

function stubSupportedWithVoices() {
  const speechSynthesis = {
    speak: vi.fn(),
    cancel: vi.fn(),
    getVoices: vi.fn(() => [{ name: 'Fake Voice' }]),
    addEventListener: vi.fn(),
    removeEventListener: vi.fn(),
  };
  vi.stubGlobal('speechSynthesis', speechSynthesis);
  vi.stubGlobal('SpeechSynthesisUtterance', FakeUtterance);
  return speechSynthesis;
}

afterEach(() => {
  vi.unstubAllGlobals();
});

describe('ReadAloudControl - availability', () => {
  it('renders nothing when the browser has no speech synthesis at all', () => {
    const { container } = render(<ReadAloudControl text="Hello." turnKey={0} />);
    expect(container).toBeEmptyDOMElement();
  });

  it('renders nothing when speech synthesis exists but has no voices installed', () => {
    vi.stubGlobal('speechSynthesis', {
      speak: vi.fn(),
      cancel: vi.fn(),
      getVoices: vi.fn(() => []),
      addEventListener: vi.fn(),
      removeEventListener: vi.fn(),
    });
    vi.stubGlobal('SpeechSynthesisUtterance', FakeUtterance);
    const { container } = render(<ReadAloudControl text="Hello." turnKey={0} />);
    expect(container).toBeEmptyDOMElement();
  });

  it('renders the control when voices are available', () => {
    stubSupportedWithVoices();
    const { container } = render(<ReadAloudControl text="Hello." turnKey={0} />);
    expect(within(container).getByRole('button', { name: 'Read aloud' })).toBeInTheDocument();
  });
});

describe('ReadAloudControl - play/stop', () => {
  beforeEach(() => {
    stubSupportedWithVoices();
  });

  it('speaks on click and flips to a pressed Stop-reading state', () => {
    const speechSynthesis = stubSupportedWithVoices();
    const { container } = render(<ReadAloudControl text="Hello there." turnKey={0} />);

    const button = within(container).getByRole('button', { name: 'Read aloud' });
    expect(button).toHaveAttribute('aria-pressed', 'false');

    fireEvent.click(button);

    expect(speechSynthesis.speak).toHaveBeenCalledTimes(1);
    const stopButton = within(container).getByRole('button', { name: 'Stop reading' });
    expect(stopButton).toHaveAttribute('aria-pressed', 'true');
  });

  it('clicking while playing cancels speech and returns to idle - one control does play, pause*, and stop', () => {
    const speechSynthesis = stubSupportedWithVoices();
    const { container } = render(<ReadAloudControl text="Hello there." turnKey={0} />);

    fireEvent.click(within(container).getByRole('button', { name: 'Read aloud' }));
    fireEvent.click(within(container).getByRole('button', { name: 'Stop reading' }));

    expect(speechSynthesis.cancel).toHaveBeenCalled();
    expect(within(container).getByRole('button', { name: 'Read aloud' })).toHaveAttribute('aria-pressed', 'false');
  });

  it('emits exactly one cic:read-aloud-play event per play, for the usage metric', () => {
    stubSupportedWithVoices();
    const listener = vi.fn();
    window.addEventListener('cic:read-aloud-play', listener);
    const { container } = render(<ReadAloudControl text="Hello there." turnKey={0} />);

    fireEvent.click(within(container).getByRole('button', { name: 'Read aloud' }));
    window.removeEventListener('cic:read-aloud-play', listener);

    expect(listener).toHaveBeenCalledTimes(1);
  });

  it('a new turn key mid-playback stops the old turn and resets to idle', () => {
    const speechSynthesis = stubSupportedWithVoices();
    const { container, rerender } = render(<ReadAloudControl text="First turn." turnKey={0} />);

    fireEvent.click(within(container).getByRole('button', { name: 'Read aloud' }));
    expect(within(container).getByRole('button', { name: 'Stop reading' })).toBeInTheDocument();

    rerender(<ReadAloudControl text="Second turn." turnKey={1} />);

    expect(speechSynthesis.cancel).toHaveBeenCalled();
    expect(within(container).getByRole('button', { name: 'Read aloud' })).toHaveAttribute('aria-pressed', 'false');
  });

  it('unmounting mid-playback cancels speech rather than leaving the browser talking', () => {
    const speechSynthesis = stubSupportedWithVoices();
    const { container, unmount } = render(<ReadAloudControl text="Hello there." turnKey={0} />);

    fireEvent.click(within(container).getByRole('button', { name: 'Read aloud' }));
    unmount();

    expect(speechSynthesis.cancel).toHaveBeenCalled();
  });
});
