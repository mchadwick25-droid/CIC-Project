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

/**
 * Read-aloud step 1 (Mark's ruling, 2026-09-22: "start with read-aloud
 * free... test one step at a time" - see Ministry/Technology/
 * CiC_ReadAloud_Step1_Design_Note.md). Same reasoning as the flag above:
 * only the literal string "on" turns it on, so an unset or misconfigured
 * env var can never silently start speaking to a participant. Defaults
 * off until Mark rules on the disclosure sentence (design note Q7) and
 * this step is ready to ship.
 */
export const readAloudEnabled = import.meta.env.VITE_READ_ALOUD === 'on';
