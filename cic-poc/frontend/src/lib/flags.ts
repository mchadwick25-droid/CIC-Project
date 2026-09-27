/**
 * Defaults ON.
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

/**
 * Only the literal string "on" turns this on, so an unset or misconfigured
 * env var can never silently start speaking to a participant.
 */
export const readAloudEnabled = import.meta.env.VITE_READ_ALOUD === 'on';
