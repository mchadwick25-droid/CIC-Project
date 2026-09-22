/**
 * Build-Plan.md Stage 3c: "ship behind a flag defaulting to current
 * behavior until R10 and label copy are ruled." Both are ruled now (R10:
 * Rulings-Pending.md; label copy: Decision-Log.md Entry 41) and Mark's
 * own seeker read-through, the gate R17 itself named, passed on both
 * halves (Entries 46, 48) - the flag defaults ON as of Entry 49.
 *
 * VITE_ prefix required for Vite to expose it to client code at all
 * (anything without it never reaches the bundle, by Vite's own design -
 * not a convention this file invents). Undefined/anything else now stays
 * on the anchor-driven renderer; only the literal string "off" reverts to
 * the legacy one, so a misconfigured or accidentally-empty env var can
 * never silently flip participant-facing behavior back - the same
 * discipline this file always had, inverted along with the default.
 */
export const useAnchorRenderer = import.meta.env.VITE_TRANSPARENCY_ANCHOR_RENDERER !== 'off';
