"""The Track B accumulator, and the Track A audit record - what the sealed
safety call already tells us, kept instead of thrown away.

THIS MODULE RECORDS. IT DECIDES NOTHING. There is no threshold here and no
routing here, deliberately: engine.m5.routing still fires Track B on a
single HARMFUL_DYNAMIC_SIGNAL exactly as it did before this module existed,
and the accumulator it builds is read by no one who can act on it yet.

That is the whole point. CiC_L3D_AcuteDistress_HarmfulDynamic_Mechanism_
Proposal_DRAFT.md SS4.3 proposes a threshold - two CONFIDANT_LANGUAGE or
AFFIRMATION_DEPENDENCE tags in a session, or one clear RETURN_COMPULSION -
and says of it, in its own words, "proposed, not validated, and explicitly
flagged as calibration work for live testing rather than a claimed-correct
number". Nothing about writing the plumbing makes that number right. The
writer can run and gather the real distribution; the threshold is a
separate decision on separate evidence.

The accumulator is also NOT fed back to the safety call. engine.m5.
live_calls.call_safety accepts recent_window and accumulator and formats
both into its prompt, and the turn loop still passes neither. Feeding it
back would change the sealed call's own input, which under CiC-Program-Spec
SS210 obliges the full live safety script rerun at a 19/20 floor - against a
corpus whose 33 scenarios were every one authored as a single message with
an empty window. That corpus cannot regression-test an accumulating gate;
it would have to be rewritten first. So: recorded, not consulted.

Standing rules from the spec, enforced here rather than trusted to
whoever reads this later:

- "engagement length, depth, and turn count NEVER increment the
  accumulator" (Program-Spec SS72, SS210; Artifact-4 SS2). Nothing in this
  module can see a turn count. It counts tags the classifier returned and
  nothing else.
- "historical-otherness disorientation is the encounter working, never
  harm" (same). HISTORICAL_OTHERNESS_DISORIENTATION is not an accumulating
  signal here, so a tag arriving alongside one is discarded rather than
  banked.
"""

# The two signals SS4.2 says are logged rather than acted on alone:
# HARMFUL_DYNAMIC_SIGNAL "logged to the accumulator ... rather than firing
# immediately on its own", AMBIGUOUS_LOW_CONFIDENCE "logged to the
# accumulator as a weak signal". Every other signal banks nothing - NO_SIGNAL
# because there is nothing to bank, HISTORICAL_OTHERNESS_DISORIENTATION
# because the spec forbids it, ACUTE_DISTRESS because Track A acts on the
# single message and does not accumulate at all (Program-Spec SS210).
ACCUMULATING_SIGNALS = {"HARMFUL_DYNAMIC_SIGNAL", "AMBIGUOUS_LOW_CONFIDENCE"}

# SS4.2's own instruction for the ambiguous case. The classifier returns no
# dynamic_tags for it in practice (measured live: two ambiguous
# messages, both with an empty tag list), so the weak signal has to be named
# by code or it is not recorded at all - which is exactly the hole this
# module was built to close. The check-in turn asks the participant a
# question; without this line the answer arrives at a gate with no memory of
# having asked.
WEAK_SIGNAL_TAG = "DISTRESS_ADJACENT"

# Track B has no computed level until a threshold exists. Writing "none"
# here would be a claim - it reads as "evaluated, below threshold" - and no
# evaluation happens in this build. This says what is true instead.
TRACK_B_LEVEL_UNEVALUATED = "not_evaluated"


def tags_for(safety: dict) -> list[str]:
    """Which tags this one classification banks. Empty for every signal the
    spec says must not accumulate, whatever tags came back with it."""
    if safety.get("signal") not in ACCUMULATING_SIGNALS:
        return []
    # A HARMFUL_DYNAMIC_SIGNAL that names no tag banks nothing, and that is
    # not a hole: the classification itself is already on the turn's
    # gate_decision event in full. This accumulator exists to count the
    # specific tags SS4.3's threshold is written in, not to be a second
    # record of what the classifier said.
    tags = list(safety.get("dynamic_tags") or [])
    if safety["signal"] == "AMBIGUOUS_LOW_CONFIDENCE" and WEAK_SIGNAL_TAG not in tags:
        tags.append(WEAK_SIGNAL_TAG)
    return tags


def track_b_state(previous: dict | None, safety: dict) -> dict | None:
    """The next Track B safety_state payload, or None when this turn banks
    nothing.

    None means no event: the fold is "take the latest safety_state event per
    track" and every event carries its own full current accumulator
    (Artifact-3 SS2, engine.m4.projection), so a turn that changes nothing has
    nothing to say. That keeps the log to what actually happened rather than
    one row per turn forever.

    A tag counts once per turn, not once per occurrence - SS4.3's threshold
    is written in turns ("two CONFIDANT_LANGUAGE tags within a session"),
    and counting mentions inside one message would inflate it against its
    own wording.
    """
    tags = tags_for(safety)
    if not tags:
        return None
    accumulator = dict(previous or {})
    for tag in dict.fromkeys(tags):
        accumulator[tag] = accumulator.get(tag, 0) + 1
    return {"track": "B", "level": TRACK_B_LEVEL_UNEVALUATED, "accumulator": accumulator}


def track_a_state(safety: dict) -> dict | None:
    """Track A's audit record. "Both route identically ... the level
    recorded for audit priority" (Program-Spec SS210) - the level was being
    recorded nowhere, so a1 and a2 have been indistinguishable in every log
    this build has ever written.

    accumulator is {} and not omitted: Artifact-3 requires the key, and
    Track A does not accumulate by design. Empty is the honest value, not a
    placeholder.
    """
    if safety.get("signal") != "ACUTE_DISTRESS":
        return None
    return {
        "track": "A",
        "level": safety.get("acute_level"),
        "accumulator": {},
        # Carried so the audit trail can address whose risk was disclosed
        # rather than assuming the participant's own (Artifact-4 SS2,
        # risk_subject, added after live batch 3 scenario s12).
        "risk_subject": safety.get("risk_subject"),
    }


def safety_state_events(previous_accumulator: dict | None, safety: dict | None) -> list[dict]:
    """Every safety_state this turn should append, in log order. Empty when
    the safety call failed - there is no classification to record, and
    inventing a neutral one would put a claim in the log that no classifier
    made."""
    if not safety:
        return []
    return [state for state in (track_a_state(safety), track_b_state(previous_accumulator, safety)) if state]
