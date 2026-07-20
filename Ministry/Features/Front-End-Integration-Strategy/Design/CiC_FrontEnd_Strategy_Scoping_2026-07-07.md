# Front-End / Product Strategy — Scoping Outline

**Purpose:** Before any deep design or tool work starts, this lays out the actual decision points — not answers. Meant to seed a dedicated thread once you've reacted to it. Nothing here has been built or committed to.

**What already governs this, and can't be traded away:** the Vision/Mission/Convictions document (Ministry/Communication) is binding on every product decision below, specifically:
- *Participant Agency* — the system creates conditions for discovery, never pressure toward a conclusion.
- *Trustworthy Transparency* — sources, tensions, uncertainty must be reachable by the participant, not just held internally by the build.
- *Encounter Over Persuasion* — a Representative that argues for its tradition has stopped witnessing. The UI can't quietly invite that.
- *Technology Serves Encounter, Never Replaces It* — tech is not the object of trust.
- The Vision doc's own success test (Article 6): did the encounter keep the Representative itself, protect the participant's authorship, present the world honestly with its tensions held, and leave interpretation to the participant. Whatever front end gets built has to make these four things checkable, not just aspirational.

The Ministry/Technology folder is currently empty — no prior front-end work exists anywhere in the project. This is a genuinely open decision space, not a continuation of something already started.

## Phase ladder (reusing the project's own phase names from the Funding Strategy doc, not inventing new ones)

**Prototype Alpha** — smallest possible thing that lets a real person talk to a Representative.
- Who's actually testing? (You alone, a handful of trusted reviewers, a small group?)
- One Representative/world, or several to compare?
- Simplest viable interface — does this even need custom front-end work yet, or can it live inside an existing chat surface (Claude Project, a simple web chat)?
- What must be visible even at this stage for it to be trustworthy rather than just a demo — any sourcing/confidence visible to the tester, or is that still internal-only at Alpha?

**Prototype Beta** — before Phase 1 launch.
- Broader tester group — who, and how many?
- Multiple worlds live at once? Any comparison or cross-world capability, or still one-at-a-time?
- First real UI investment — is this where a custom front end actually starts, or still a lightweight surface?

**Phase 1 Launch** — the funding doc calls this "sustainable funding for ongoing operation," implying real, non-trusted-tester users exist by here.
- Public, semi-public (invite/waitlist), or still gated to a known community (churches, a denomination, a seminary)?
- Accounts and saved history, or stateless/anonymous conversations?
- Web, mobile, or both?
- Does a subscription or donation ask live in the product itself at this phase, or is funding still handled entirely outside the app?

**Phase 2+ Growth** — more worlds, more features, first team members (per the funding doc).
- Group/classroom mode (a facilitator running an encounter for several participants)?
- API or embeddable widget for partner institutions (churches, seminaries) rather than only a standalone app?
- Multi-Representative encounters (two traditions in conversation with each other, not just with the participant)?

## Cross-cutting questions — worth deciding early because they're expensive to change later

- **World discovery/selection.** How does a participant choose which world or Representative to talk to, especially once the roster grows past the current nine? This is real UX work, not a dropdown afterthought.
- **Transparency in the UI itself, not just in the build.** The build side already has strict rules about disclosing confidence levels and marking simulated/internal review. Does the participant-facing side need its own version — visible sourcing, a way to see what's confidently attested vs. reconstructed, some visible marker distinguishing "historical witness" from "living tradition's own self-understanding" (the Vision doc draws this line explicitly)?
- **Guardrails against drifting into persuasion.** If a participant pushes a Representative toward advocacy or debate, does the product need any structural cue or boundary, or is that entirely a Representative-design problem rather than a front-end one?
- **Data and privacy.** Is conversation content logged? Used for validation or improvement? What consent does a participant need to see before that happens?
- **Tech stack, phase by phase.** Alpha probably needs almost nothing custom. Phase 1 likely needs accounts, maybe payments, and some way to manage a growing library of worlds/Representatives without hand-editing code per world. These choices drive cost directly — this is the direct link to the funding/org strategy work running in parallel.
- **What "success" looks like in product terms**, translating the Vision doc's four-condition test into something an actual product review could check against a real conversation transcript.

## Concrete questions to answer before a dedicated thread starts deep work

1. Who is the Alpha tester group, and how many people?
2. Is Alpha one world or several?
3. Does Alpha need any custom interface at all, or can it run inside an existing surface?
4. What, if anything, must be visible to an Alpha tester about sourcing/confidence — or is that still deferred?

## Recommended next step

Once you've reacted to the above (especially the four concrete questions), this becomes the launch brief for a dedicated front-end thread — same pattern as the World Build launches: full context, explicit mandate, wait for confirmation before any building starts.
