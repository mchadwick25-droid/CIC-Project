# World Map ↔ cic-poc Integration — Assessment V0.1

**Status:** Exploration complete and **working**, on branch
`claude/world-map-integration-exploration`. Zero changes to `main` or to the
pilot branch (`claude/cic-poc-backend-facilitator-upgrade`) — the running program
is untouched. The merge decision and its timing belong to the front-end thread,
per the standing coordination boundary; Mark authorized this exploration
directly (2026-07-16).

---

## 1. What was built and verified (it works now)

Spec Part 4's "middle step" — the map as a supplementary view feeding the
existing selection flow — implemented end-to-end and verified live against the
real dev servers (backend + frontend), in both directions:

- **App → Map:** the world-selection screen gains one line under the world
  cards: *"🗺 See these worlds across two thousand years — open the World
  Orientation Map."* It opens the full interactive map (all 178 census entries,
  tour, wet-ink, everything) served as a static asset at `/world-map/`.
- **Map → App:** opened with `?app=1`, the map's launch actions change behavior:
  *Have an interview with {Rep}* returns to the app as
  `/?worlds=<id>&mode=interview`; the tray's *Sit down at the Table* returns as
  `/?worlds=<id,id>&mode=table`. The app reads the handoff once, flips the
  Single/Multiple toggle to match, preselects the worlds on the existing
  selector (selection badges, Begin button armed), and scrubs the URL so a
  refresh can't replay a stale selection.
- **Verified live:** two-world table handoff (House-Churches + Desert →
  "Multiple Representatives," badges 1/2, "Begin Conversation with 2
  Representatives") and single-interview handoff (map → Chloe → "Begin
  Conversation with Chloe"). TypeScript compiles clean (`tsc --noEmit`).

**Deliberate design point:** the map never auto-starts a session. It preselects;
the participant confirms with the existing Begin button. Selection consent stays
where it already lives, and the backend is entirely unaware anything changed.

## 2. Touch surface (the whole diff)

| File | Change |
|---|---|
| `cic-poc/frontend/src/components/TheTable.tsx` | ~25 lines: module-scope handoff parse, mode-toggle initialization, URL scrub effect, map link |
| `cic-poc/frontend/src/components/WorldSelector.tsx` | ~12 lines: optional `initialWorldIds` prop, preselect on fetch |
| `cic-poc/frontend/public/world-map/index.html` | new static asset (281 KB, fully self-contained — no dependencies, no network calls) |

No backend changes. No new npm dependencies. No changes to session logic,
prompts, or transcripts. Deployed as a Render static site, `public/` assets ship
with the build unchanged, and the root-relative link works on any origin.

**One engineering lesson worth keeping** (cost an hour, now on record): parsing
one-shot URL params inside a React `useState` initializer breaks under
StrictMode's dev double-mount when the same code also scrubs the URL — the
second mount reads an already-scrubbed URL. Parse at module scope; scrub in an
effect.

## 3. What fuller integration would take (tiers, with honest estimates)

- **Tier A — what this branch already is** (map as optional orientation view +
  handoff): done. Merge cost ≈ one evening including QA on the deployed site.
- **Tier B — map as the primary selection surface** (replaces the tile grid;
  Deep Interview / Compare Worlds emerge from seat count instead of the upfront
  toggle): 2–4 evenings. Requires real front-end-thread decisions first: what
  happens to the tiles, where onboarding sits relative to the map, and the
  mobile answer (the map's phone fallback is currently a link to the list-form
  census browser; as *primary* selector that's not good enough — the
  era-accordion from the visual-architecture doc becomes required work).
- **Tier C — "Take a tour" activation:** the map's ghost button wires to the
  hospitality thread's Chloe tour the same way (static asset at
  `/world-map/tour-chloe.html`, same handoff pattern back). Cost ≈ hours once
  that thread's deliverable exists. In-conversation tours (the Representative
  guiding live) are a different, backend-shaped project — not estimated here.
- **Tier D — the honesty layer reaching testers** ("why isn't X here?" through
  Ask-the-Facilitator, per spec Part 4's cheapest step): backend serves the
  census JSON + a facilitator-prompt addition; 1–2 evenings. Independent of the
  map UI entirely.

## 4. Risks and cautions for the merge decision

1. **Pilot stability first.** The standing ops rule (front-end log, 2026-07-15)
   holds: never redeploy during a scheduled sitting window, and Prototype
   Testing 1's transcripts are the pilot's irreplaceable output. Recommendation:
   **do not merge before or during Prototype Testing 1** unless Mark explicitly
   wants testers to see the map — in which case merge *before* invitations go
   out, never mid-pilot, and add one line to the tester brief.
2. **The map is design-frozen content, not reviewed content.** Its census copy
   (statuses, briefs, floor notes) has been through Mark's passes but no
   external review. Testers reading it are reading V0.x draft copy; that is
   honest to disclose if it ships to them.
3. **The `WID` mapping** (map refs → backend world ids) is a small hand-synced
   table — exactly the class the manifest refactor eliminated backend-side. At
   Tier B, generate it from the census/manifest rather than maintaining it by
   hand (Engineering Considerations Catalog, world-data-schema seam).
4. **Bundle/deploy footprint:** +281 KB static; no runtime cost; no CSP issues
   (everything inline).

## 5. Recommendation

Hold the branch as-is through Prototype Testing 1; let the front-end thread take
the merge decision with the pilot schedule in front of it. If Mark wants a
mid-pilot taste without deploy risk: the standalone demo artifacts already do
that job by email. Tier D (the honesty layer via the Facilitator) is the one
piece worth considering *sooner*, because testers will ask "why only ancient
worlds?" and the census already contains the answer.
