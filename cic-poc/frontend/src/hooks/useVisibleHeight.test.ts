import { renderHook } from '@testing-library/react';
import { afterEach, describe, expect, it } from 'vitest';
import { useVisibleHeight } from './useVisibleHeight';

function stubViewport(height: number, scale: number) {
  Object.defineProperty(window, 'visualViewport', {
    configurable: true,
    value: Object.assign(new EventTarget(), { height, scale }),
  });
}

describe('useVisibleHeight', () => {
  afterEach(() => {
    Object.defineProperty(window, 'visualViewport', { configurable: true, value: undefined });
  });

  it('follows the visible height when a keyboard shrinks it', () => {
    stubViewport(400, 1);
    renderHook(() => useVisibleHeight());
    expect(document.documentElement.style.getPropertyValue('--app-height')).toBe('400px');
  });

  it('keeps the layout height when pinch-zoom shrinks the visual viewport', () => {
    stubViewport(400, 2);
    renderHook(() => useVisibleHeight());
    expect(document.documentElement.style.getPropertyValue('--app-height')).toBe('800px');
  });
});
