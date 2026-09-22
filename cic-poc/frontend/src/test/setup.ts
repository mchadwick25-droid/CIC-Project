import '@testing-library/jest-dom/vitest';

// jsdom doesn't implement window.matchMedia (used by hooks/useBreakpoint.ts,
// which every InlineBridge-based mark calls) - the standard test-environment
// polyfill, not an application behavior change. Always reports "not phone"
// (matches: false), which is what every existing desktop-oriented component
// test already assumes implicitly by never mocking a phone viewport.
if (typeof window !== 'undefined' && !window.matchMedia) {
  window.matchMedia = (query: string) => ({
    matches: false,
    media: query,
    onchange: null,
    addListener: () => {},
    removeListener: () => {},
    addEventListener: () => {},
    removeEventListener: () => {},
    dispatchEvent: () => false,
  }) as unknown as MediaQueryList;
}
