# Launch prompt — Conversation & Round Usage Caps (no accounts)

Paste this into a fresh thread. Run it in Sonnet for the back-and-forth — this
is a genuinely open, gray-zone design question, not a mechanical build; there
isn't a clean, obviously-correct answer, and it needs real thinking-through
with Mark before anything gets built, not a first idea shipped as the answer.

**Scope note, read this first:**
- **In scope:** how to limit how many conversations, and how many rounds per
  conversation, a single participant can access as the pilot's audience
  potentially grows past "a personal ask not to forward the link."
- **Explicitly out of scope, two different ways:**
  1. **No sign-in, no accounts, no auth-based gating.** `session_cap.py` and
     `app/auth.py` already exist — a real, Supabase-backed per-user session
     cap (`profiles.max_sessions`, default 5) — but Mark deliberately chose
     no sign-in for this pilot on 2026-07-20, which makes that whole
     mechanism a permanent no-op as currently deployed (it only bites a
     signed-in user, and there are none). **That thread went further than
     Mark wanted — don't read it as the direction to extend or complete.**
     Read `session_cap.py` and `auth.py` to understand what already exists
     and why it's parked, not as a system to wire back up.
  2. **The paid/monthly tier.** A real question, but a later one — see
     `Ministry/Funding/CiC_Go_Live_Cost_Model_V0_1.md` Part C.2 for the
     already-sequenced monetization ladder (tip link → recurring pledge →
     gate a feature behind payment → institutional licenses). The paid tier
     is deliberately rung 3, meant to wait for signal from rungs 1-2. This
     thread is about the cap alone.

---

**You're not starting from zero. Read, in this order:**

1. `cic-poc/backend/app/message_cap.py` — the mechanism actually live today:
   an identity-free, per-conversation turn cap (`CONVERSATION_TURN_CAP_SOLO
   = 40`, `..._TABLE = 100`), deliberately generous, meant to catch a
   runaway session rather than cut short real use. Its own docstring already
   names the gap this thread exists to close: it protects one conversation
   from running forever, not the total number of conversations one person
   can start. This is the pattern to extend the spirit of, not replace.
2. `cic-poc/backend/app/session_cap.py` and `app/auth.py` — read for what NOT
   to rebuild (see scope note above), and because `session_cap.py`'s own
   docstring is a genuinely good write-up of why a *shared* budget (one pool
   everyone draws from) is the wrong shape (whoever arrives first burns the
   whole pilot's spend) — that reasoning still applies even without accounts,
   and should inform whatever identity-free mechanism this thread proposes.
3. `Ministry/Funding/CiC_Go_Live_Cost_Model_V0_1.md` — the real numbers this
   cap protects: an Anthropic Console hard spending ceiling ($100–150/month
   to start) already in place as one backstop, translating to roughly
   150–500 real conversations before it bites; a fuller $500/month budget
   scenario reaching ~500–1,250 conversations / ~330–830 people. Also: real,
   dated cost pressure — Sonnet 5's introductory pricing ends 2026-08-31,
   ~50% higher per-token cost after, nothing else changing.
4. `Ministry/Communication/Vision, Mission, Convictions, and Foundational
   Commitments V1.1.docx` — Participant Agency and Trustworthy Transparency
   govern this directly: whatever mechanism gets designed has to be honest
   with a participant about the fact that a limit exists and roughly why,
   not a silent, unexplained throttle or a dark-pattern nudge toward paying
   to remove it (that's the paid tier's job, later, not this thread's).

## The actual design question — think it through, don't default to the heaviest option

Without accounts, there is no clean way to know "this is the same person
again." Every real option has a real cost, and naming that plainly is the
job of this thread's first pass, not picking one and moving on:

- **Tighten/extend the existing identity-free turn cap's own logic** —
  e.g., a lighter, honest-system-faith client-side counter (cookie or
  `localStorage`), cheap to build, easily cleared by anyone who wants to,
  consistent with the "informal ask" spirit already chosen for this pilot.
- **IP-based limiting** — catches more real abuse, but genuinely
  mis-targets: two church members on the same building's wifi, or a
  classroom, look identical to one person testing limits.
- **Rely on and tighten the Anthropic Console spending ceiling itself** as
  the actual backstop, accepting that it's blunt (bites everyone at once
  once near the ceiling, not per-person) — simplest, already live, arguably
  already *is* a cap in spirit, just not a per-person one.
- Anything else this thread's own research surfaces — this list is a
  starting point, not the menu.

## What to produce first

Work through this with Mark the way the front-end/product skill describes:
absorb whatever he dumps, ask one sharp question at a time for what hasn't
surfaced yet (starting point: how much friction is he actually willing to
put in front of a genuine seeker, versus how tightly does the budget
actually need protecting), and close with a concrete, named recommendation —
not a menu handed back unresolved. Log the actual decision in
`Ministry/Features/Front-End-Integration-Strategy/Decision-Log.md` once
Mark reacts, per that skill's own logging discipline.
