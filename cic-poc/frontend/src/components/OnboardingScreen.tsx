/**
 * OnboardingScreen component - the pre-encounter screen shown once per
 * tester, before they ever pick a world.
 *
 * Text is the exact draft from Ministry/Operations/
 * CiC_Prototype_Testing_Pilot_Plan_DRAFT_V0_1.md, Section 3, approved by
 * the project lead - not paraphrased or shortened here. The "known
 * limitation" paragraph from that draft is deliberately NOT included below;
 * per that same section's own note, it's shown instead in the table bar's
 * consolidated status line during the conversation itself (see TheTable's
 * table bar, Increment 1 §2), since it's the one thing a tester needs to
 * remember *during* the conversation, not just before it.
 *
 * Three additions beyond that draft, all 2026-08-05, all small and flagged
 * rather than woven silently into the approved text:
 *  1. A link to the new cic-website/privacy.html in the cataloging
 *     paragraph, closing the full-system review's Participant Readiness
 *     finding P0-2 (the app told testers their conversation was saved and
 *     read, with no page anywhere saying what that meant).
 *  2. One clause naming "the Table" in the opening paragraph, closing
 *     Accessibility finding P1-1 - the app's own page title, the tray's
 *     "Sit down at the Table" button, and the closing screen's "The
 *     conversation has ended" all use "the Table" as this project's name
 *     for the space itself, but nothing ever said so before a tester's
 *     first conversation.
 *  3. A new, self-contained "what brings you here?" question appended
 *     after the last approved paragraph, before the begin button - not
 *     inserted into the approved text itself (Readiness P0-3b). The
 *     landing page recruits across four perspectives (general / pastor or
 *     teacher / academic / re-examining their faith) that the product
 *     itself never asked or distinguished; this stores the answer for
 *     feedback correlation only (sessions.persona) - it does NOT set
 *     participant_role or touch the paused Representative Modes
 *     lane-ceiling system in any way, and it changes no Representative's
 *     voice. Optional; skippable.
 * Everything else in this component is unchanged.
 */

import { useState } from 'react';

const ONBOARDING_SEEN_KEY = 'cic_onboarding_seen';

// Same option set as pilot-feedback.html's own "Perspective" field, on
// purpose - one shared vocabulary for "who is this participant" across the
// app rather than two similar-but-different lists drifting apart.
const PERSONA_OPTIONS = [
  'General',
  'Pastor or Teacher',
  'Academic',
  'Re-examining my faith',
  'Not sure / more than one',
];

export function hasSeenOnboarding(): boolean {
  return localStorage.getItem(ONBOARDING_SEEN_KEY) === 'true';
}

interface OnboardingScreenProps {
  onContinue: (persona?: string) => void;
}

export function OnboardingScreen({ onContinue }: OnboardingScreenProps) {
  const [persona, setPersona] = useState<string | undefined>(undefined);

  const handleContinue = () => {
    localStorage.setItem(ONBOARDING_SEEN_KEY, 'true');
    onContinue(persona);
  };

  return (
    <div className="onboarding-screen">
      <div className="onboarding-screen__content">
        <h2>Before you begin</h2>

        <h3>What this is</h3>
        <p>
          The Church in Conversation lets you talk with a Representative — a voice built from the
          historical record of a specific Christian community, formed entirely from what that
          community actually wrote, believed, and lived. You're not talking to a single historical
          person. You're talking to a voice shaped by the whole documented life of that community —
          its arguments, its certainties, and the questions it never settled. We call this space
          "the Table" — one seat for you, one for each Representative you invite to sit down with.
        </p>

        <h3>This is a prototype, not a finished product</h3>
        <p>
          You're testing an early build. Scholarly review of this work is still ongoing — it has
          not yet been checked by outside historians and theologians the way it eventually will be.
          What you're about to read has been built with real care and real rigor, but treat it as a
          serious first draft, not a finished, fully vetted work. If something feels off, thin, or
          wrong, that's exactly the kind of thing we need you to tell us.
        </p>

        <h3>We're cataloging this conversation</h3>
        <p>
          Your conversation in this session is being saved and cataloged for learning purposes — so
          the project team can see what's working and what isn't before this goes any further. It's
          reviewed by the project team only. See our{' '}
          <a href="https://churchinconversation.com/privacy.html" target="_blank" rel="noopener noreferrer">
            privacy page
          </a>{' '}
          for what's stored, how long, and how to ask us to delete it.
        </p>

        <h3>What a "world" and a "Representative" are</h3>
        <p>
          A world is a specific historical Christian community — a time, a place, a way of life —
          that's been carefully reconstructed from real sources: letters, sermons, rules of life,
          sayings, disputes. A Representative speaks <em>for</em> that world, in its own voice, using
          its own vocabulary, holding its own arguments — including the ones it never resolved. A
          Representative will not modernize itself, defend itself like a lawyer, or tell you what to
          think. It will tell you honestly what its world held to be true, and where its world was
          still arguing.
        </p>

        <h3>Reading the highlights</h3>
        <p>
          As you talk, some words and phrases will be highlighted in the text. These are terms this
          world used in a specific way, or claims and stories drawn from a real source. Hover over a
          highlight for a short explanation. Click it for the fuller picture — what it's based on,
          and how confident the reconstruction is. Nothing behind a highlight is ever hidden from
          you or locked behind anything — that's a rule of how this whole project is built, not just
          a feature of this screen.
        </p>

        <h3>The one honest distinction that matters most</h3>
        <p>
          Some of these worlds are directly connected to Christian communities that are still alive
          today — their descendants still gather, still worship, in some cases still speak the
          language you'll hear. Where that's true, the Representative speaks only for its own
          historical moment. It is not a spokesperson for how that living community understands or
          practices its faith right now — that community has its own voice, and it isn't this one.
          Other worlds you'll meet don't continue in that direct line at all; where that's the case,
          the Representative will tell you so. Either way: this is history speaking for itself, not
          a stand-in for anyone's faith today, including yours.
        </p>

        <h3>What we're asking of you</h3>
        <p>
          Bring real questions. Push back if something doesn't sit right. Try to notice not just
          whether you <em>liked</em> the conversation, but whether it felt honestly <em>itself</em> —
          a real voice with real edges, not a smoothed-over answer trying to please you.
        </p>

        <div className="onboarding-screen__persona">
          <h3>One quick, optional question</h3>
          <p>
            What brings you here today? This is just for us, to understand who's actually using this —
            it doesn't change how any Representative speaks with you.
          </p>
          <div className="onboarding-screen__persona-options" role="group" aria-label="What brings you here today?">
            {PERSONA_OPTIONS.map((option) => (
              <button
                key={option}
                type="button"
                className={`onboarding-screen__persona-option${persona === option ? ' onboarding-screen__persona-option--selected' : ''}`}
                aria-pressed={persona === option}
                onClick={() => setPersona(persona === option ? undefined : option)}
              >
                {option}
              </button>
            ))}
          </div>
        </div>

        <button className="chat-button chat-button--primary chat-button--large" onClick={handleContinue}>
          I understand — let's begin
        </button>
      </div>
    </div>
  );
}
