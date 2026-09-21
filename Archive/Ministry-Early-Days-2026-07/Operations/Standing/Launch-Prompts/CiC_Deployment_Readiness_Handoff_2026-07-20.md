# Deployment readiness handoff — what's ready to go live tonight, what isn't, and what Hub needs to do

Paste this into System Hub. Mark's ask: get the completed products (the Atlas, the
conversation program) ready to upload into the new website format Hub is building,
with a real, active website up tonight or tomorrow morning.

---

**What governs:** standard git-safety protocol. Everything below is code/config
already committed and pushed to `main` (`513ae2d`) — nothing here needs a branch
decision, it's already landed. The only things left are infrastructure actions this
thread does or Mark does directly (account creation, secrets) — not more engineering.

## What's actually ready, verified live today

1. **The Atlas** — merged (`37168c4`). The Story view replaces the old map iframe on
   the live website. Personally re-verified after merging: all 5 worlds correct,
   search/chips/panels/honest-redirects work, zero console errors, zero horizontal
   overflow on phone (your nav-bar fix, `d02b41e`, carried through cleanly — confirmed
   375px = 375px scrollWidth). Nothing left to do here.

2. **The conversation program (`cic-poc`) — the core experience is solid.** All 5
   worlds (House-Churches, Syriac, Desert, Bethlehem Circle, Alexandria) live and
   correct. Lexicon highlighting, citations, and three governance bridges all verified
   live with real API calls today: the anachronism/modern-term bridge, and a new
   epistemology bridge (fixes a frame-break on documentation-vs-inference questions -
   `99a25e8`, independently reviewed and confirmed sound in your own `1be1bde`).

3. **`cic-poc` is now deployable as ONE service** (`975ee35`, today). Found and fixed a
   real blocker: the frontend hardcodes `API_BASE = '/api'` as a same-origin path, with
   no env var to point it elsewhere — fine locally (Vite's dev proxy), but a
   production static build had no such proxy and would have broken the moment frontend
   and backend lived on different origins. Fix: FastAPI now serves the built frontend
   directly (mounts `dist/assets`, falls through to `index.html` for anything not
   matched by `/api/*` or `/health`). Verified end-to-end on the combined setup:
   onboarding, world selection, a real streamed conversation, and a genuine
   frame-breaker question ("Who are you?") all worked correctly from one port.
   A working `Dockerfile` + `.dockerignore` are committed too — not Docker-build-tested
   (no Docker in this environment), but structure-verified against
   `requirements.txt`/`pyproject.toml`; most hosts build it themselves at deploy time
   anyway.

## What Hub (or Mark) still needs to do — infrastructure only, not engineering

1. **Provision an actual host** for the `cic-poc/backend` Dockerfile (Render, Railway,
   Fly.io all support this directly — pick whichever this project already has
   momentum with). This needs real account creation — not something I do on Mark's
   behalf.
2. **Set two environment variables** on that host:
   - `ANTHROPIC_API_KEY` — required, real secret.
   - `CORS_ORIGINS` — good practice to set explicitly to the real domain even though
     the combined-serving fix makes this less load-bearing than it would've been
     cross-origin. See the Dockerfile's own header comment and `.env.example`.
3. **Point the real domain/subdomain at it.** Everything else (Supabase, pilot
   logging, mock mode) is optional and safely no-ops until configured — don't block on
   any of it.

## What is honestly NOT ready — say this plainly if "all features" comes up

The core conversation is solid, but it's still running the **pre-redesign UI** —
Increment 1 (long-form transcript, table bar, brand tokens) hasn't been built, so
what ships tonight looks like the old chat-bubble interface, not the approved
redesign. Also not included: Representative Modes/role selection (built on a branch,
never validated live), Guided Questions (zero UI), the S0 three-door threshold and
Guided Onboarding (zero code), and Hosted Tour (explicitly deferred by Mark until
token reset, Friday 2026-07-24 — do not build or prioritize this before then). Full,
current status of every feature is
`Ministry/Operations/Audits/CiC_Full_UX_Feature_Checklist_2026-07-20.md` — treat it as
the source of truth for what the new site's copy should claim, not this handoff.

## Logging

`Ministry/Operations/Standing/CiC_System_Hub_Decision_Log.md`, same as always.
