/**
 * Build-Plan.md Stage 3c: "ship behind a flag defaulting to current
 * behavior until R10 and label copy are ruled." One flag, one job - VITE_
 * prefix required for Vite to expose it to client code at all (anything
 * without it never reaches the bundle, by Vite's own design - not a
 * convention this file invents). Undefined/anything else stays on the
 * current, already-live renderer; only the literal string "on" switches
 * to the engine-driven one, so a misconfigured or accidentally-empty env
 * var can never silently flip participant-facing behavior.
 */
export const useAnchorRenderer = import.meta.env.VITE_TRANSPARENCY_ANCHOR_RENDERER === 'on';
