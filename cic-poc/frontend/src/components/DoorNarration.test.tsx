import { act, cleanup, fireEvent, render, screen } from '@testing-library/react';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import { DOOR_PAUSE_MS, DoorNarration } from './DoorNarration';

class FakeAudio {
  static instances: FakeAudio[] = [];
  paused = true;
  currentTime = 0;
  preload = '';
  listeners: Record<string, () => void> = {};
  play = vi.fn(() => {
    this.paused = false;
    return Promise.resolve();
  });
  pause = vi.fn(() => {
    this.paused = true;
  });
  constructor(public src: string) {
    FakeAudio.instances.push(this);
  }
  addEventListener(name: string, fn: () => void) {
    this.listeners[name] = fn;
  }
}

beforeEach(() => {
  FakeAudio.instances = [];
  vi.useFakeTimers();
  vi.stubGlobal('Audio', FakeAudio);
});

afterEach(() => {
  cleanup();
  vi.useRealTimers();
  vi.unstubAllGlobals();
});

describe('DoorNarration', () => {
  it("loads the world's own file and waits a moment before speaking", async () => {
    render(<DoorNarration worldKey="ijc" participantTurns={0} />);
    const audio = FakeAudio.instances[0];
    expect(audio.src).toBe('/audio/door/ijc.mp3');
    expect(audio.play).not.toHaveBeenCalled();
    await act(async () => {
      vi.advanceTimersByTime(DOOR_PAUSE_MS);
    });
    expect(audio.play).toHaveBeenCalledTimes(1);
    expect(screen.getByRole('button', { name: 'Stop the welcome' })).toBeInTheDocument();
  });

  it('offers a plain play button when the browser refuses sound nobody asked for', async () => {
    render(<DoorNarration worldKey="ijc" participantTurns={0} />);
    const audio = FakeAudio.instances[0];
    audio.play.mockImplementationOnce(() => Promise.reject(new Error('NotAllowedError')));
    await act(async () => {
      vi.advanceTimersByTime(DOOR_PAUSE_MS);
    });
    const button = screen.getByRole('button', { name: 'Hear the welcome' });
    await act(async () => {
      fireEvent.click(button);
    });
    expect(audio.play).toHaveBeenCalledTimes(2);
    expect(screen.getByRole('button', { name: 'Stop the welcome' })).toBeInTheDocument();
  });

  it('stops and rewinds from the button', async () => {
    render(<DoorNarration worldKey="ijc" participantTurns={0} />);
    await act(async () => {
      vi.advanceTimersByTime(DOOR_PAUSE_MS);
    });
    await act(async () => {
      fireEvent.click(screen.getByRole('button', { name: 'Stop the welcome' }));
    });
    expect(FakeAudio.instances[0].pause).toHaveBeenCalled();
    expect(screen.getByRole('button', { name: 'Hear the welcome' })).toBeInTheDocument();
  });

  it('stops when the participant sends a message', async () => {
    const { rerender } = render(<DoorNarration worldKey="ijc" participantTurns={0} />);
    await act(async () => {
      vi.advanceTimersByTime(DOOR_PAUSE_MS);
    });
    rerender(<DoorNarration worldKey="ijc" participantTurns={1} />);
    expect(FakeAudio.instances[0].paused).toBe(true);
    expect(screen.getByRole('button', { name: 'Hear the welcome' })).toBeInTheDocument();
  });

  it('shows nothing when the file is missing, and never speaks after leaving the screen', async () => {
    const { container, unmount } = render(<DoorNarration worldKey="ijc" participantTurns={0} />);
    const audio = FakeAudio.instances[0];
    await act(async () => {
      audio.listeners.error();
    });
    expect(container).toBeEmptyDOMElement();
    unmount();
    vi.advanceTimersByTime(DOOR_PAUSE_MS);
    expect(audio.play).not.toHaveBeenCalled();
  });
});
