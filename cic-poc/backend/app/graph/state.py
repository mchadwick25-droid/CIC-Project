"""LangGraph state schema for The Table conversation."""

from dataclasses import dataclass, field
from typing import Annotated, Literal, Optional

from langgraph.graph import add_messages
from langchain_core.messages import BaseMessage


@dataclass
class DriftSignal:
    """A detected drift signal in the representative's response."""

    # S4.3 (Pass 1 §6.5): ALL emitted types declared - over_settling and
    # self_narration were emitted by the monitor path but absent here,
    # exactly the two most governance-critical of the set. 17 total.
    signal_type: Literal[
        "smoothing",
        "generating",
        "agreeing",
        "over_producing",
        "temporal_bleed",
        "flattening",
        "fabrication",
        "apologetics",
        "first_person",
        "anachronism",
        "self_narration",
        "over_settling",
        "dominance",
        "convergence",
        "cross_world_vocabulary",
        "length_ceiling",
        "question_stacking",
    ]
    description: str
    severity: Literal["low", "medium", "high"]
    # Which representative this signal concerns - None for the original
    # single-representative signals above, which apply to whoever spoke last.
    # "dominance", "convergence", "cross_world_vocabulary", "length_ceiling",
    # and "question_stacking" are multi-representative-table signals and are
    # always attributed to a specific world_id.
    world_id: Optional[str] = None


@dataclass
class RetrievedContext:
    """Context retrieved from the RAG system."""

    chunks: list[str]
    terms: list[str]
    sources: list[str]
    citations: list[dict] = field(default_factory=list)


@dataclass
class WorldContext:
    """Context for a single world at the table."""

    world_id: str
    permanent_prompt: str
    world_capsule: str


@dataclass
class ConversationState:
    """
    State schema for The Table conversation.

    This tracks the full conversation state including messages,
    conversation phase, speaker turns, and drift detection.

    Supports both single-world and multi-world tables.
    """

    # Core conversation
    messages: Annotated[list[BaseMessage], add_messages] = field(default_factory=list)

    # Conversation phase
    phase: Literal[
        "reception", "handoff", "active_encounter", "reroot", "closing"
    ] = "reception"

    # Current speaker - now tracks which representative
    current_speaker: Literal["facilitator", "representative"] = "facilitator"
    current_world_id: Optional[str] = None  # Which world's representative is speaking

    # Turn tracking
    turn_count: int = 0

    # Drift detection
    drift_signals: list[DriftSignal] = field(default_factory=list)
    requires_reroot: bool = False

    # Per-representative course-correction guidance awaiting delivery, keyed
    # by world_id. S4.3 (Pass 1 §6.5): each world's slot is now a PRIORITY
    # QUEUE (a list of {signal_type, severity, text} entries, kept sorted by
    # the one signal ordering in nodes.py) instead of a single last-writer-
    # wins string - the old shape structurally deprioritized exactly the
    # multi-party table signals, purely by statement order in a background
    # block. Every writer goes through governance.queue_guidance (the one
    # gate); the consumer delivers the highest-priority entry per turn and
    # keeps the rest queued. Kept separate from requires_reroot/
    # drift_signals because those are global to "whoever spoke last," not
    # per-representative.
    pending_guidance: dict[str, list[dict]] = field(default_factory=dict)

    # S3.5 (Pass 1 R9): a standalone retrieval query supplied by an
    # intercept for the NEXT representative turn, consumed once. The
    # bridges set it so retrieval searches the participant's actual
    # subject instead of handback boilerplate written for no world in
    # particular (the modern-term bridge sets the extracted subject; the
    # epistemology bridge sets the participant's own original question -
    # both deterministic, no extra LLM call).
    retrieval_query_override: Optional[str] = None

    # S3.3 (Pass 1 R4): the ID-keyed session exclusion set - chunk ids
    # (source_file stems) already surfaced into a representative's context
    # this session, keyed by world_id. Replaces the two substring de-dup
    # proxies (partition_tier1_short_circuit's already_discussed check and
    # the story vote's "already told earlier" instruction) with a
    # deterministic exclusion: once a chunk has been surfaced, it is
    # filtered at candidate stage, no string-matching or LLM judgment
    # involved. Also deterministically replaces the retired
    # "Capsule-Core has already surfaced this" retrieval-condition class.
    surfaced_chunk_ids: dict[str, list[str]] = field(default_factory=dict)

    # Relational-safety session-level state (Acute Distress / Harmful Dynamic,
    # Facilitator Governance V3.6 Section 12, per the corrected design in
    # CiC_L3D_AcuteDistress_HarmfulDynamic_Mechanism_Proposal_DRAFT.md and its
    # live-tested revision in CiC_W1_Phase5_RelationalSafety_
    # LiveAdversarialTest_CorrectedDesign_Round1/2.md). None of this is ever
    # surfaced to the participant directly - it only governs routing.
    #
    # True once Track A (Acute Distress) has fired at least once this
    # session. Per the design doc's Section 4.4 "sustained attention," every
    # subsequent participant turn is re-evaluated at Track A sensitivity
    # while this is True - concretely, the Representative is withheld from
    # every turn while this flag is set, regardless of that turn's own raw
    # classification, until de-escalation clears it. De-escalation threshold
    # (two consecutive turns classified NO_SIGNAL while active - see nodes.py)
    # is this implementation's own calibration choice, not specified
    # numerically by the design doc - disclosed here as unvalidated, matching
    # the doc's own disclosure discipline for its accumulator threshold.
    track_a_active: bool = False
    # Highest Track A severity reached this session - "A1" (disclosure, no
    # stated plan) or "A2" (explicit plan/means/timeline). Governs which
    # response template a continuation turn implicitly stands behind, and
    # whether a new turn is a fresh escalation (A1 -> A2, fires the full A2
    # script) versus a same-or-lower-severity continuation (lighter
    # acknowledgment only), per the design doc's Section 4.4.
    track_a_severity: Optional[str] = None

    # True once Track B (Harmful Dynamic) has fired - same sustained-
    # attention/de-escalation shape as track_a_active, tracked separately
    # since the two tracks can in principle both be active in one session.
    track_b_active: bool = False

    # Track B's session-level signal accumulator (design doc Section 4.3).
    # Tags: CONFIDANT_LANGUAGE, AFFIRMATION_DEPENDENCE, RETURN_COMPULSION,
    # DISTRESS_ADJACENT. Starting threshold, per the design doc, not a
    # validated result: two CONFIDANT_LANGUAGE/AFFIRMATION_DEPENDENCE tags
    # (pooled), or one RETURN_COMPULSION tag, crosses into firing Track B.
    # Explicit anti-false-positive rule the doc requires: turn count, session
    # length, or "I want to keep exploring" language must never by
    # themselves append a tag - only the specific relational-pattern content
    # in the classifier's taxonomy does.
    relational_safety_tags: list[str] = field(default_factory=list)

    # Consecutive turns classified NO_SIGNAL while either track is active -
    # used to auto-clear track_a_active/track_b_active once de-escalation is
    # observed. HISTORICAL_OTHERNESS_DISORIENTATION and AMBIGUOUS_LOW_
    # CONFIDENCE are deliberately treated as non-clearing (both can co-occur
    # with genuine ongoing distress - see nodes.py). Reset to 0 the moment a
    # HARMFUL_DYNAMIC_SIGNAL turn recurs.
    relational_safety_deescalation_count: int = 0

    # RAG context
    retrieved_context: Optional[RetrievedContext] = None

    # Multi-world support: list of worlds at the table
    worlds_at_table: list[WorldContext] = field(default_factory=list)

    # Legacy single-world fields (for backwards compatibility)
    world_capsule_core: str = ""
    permanent_prompt: str = ""

    # Session management
    session_id: str = ""
    # The signed-in Supabase user this session belongs to (see app/auth.py),
    # None when Supabase isn't configured or the participant isn't signed in.
    # Set once at session creation; read by app/transcript_logging.py so
    # every downstream call site doesn't need its own user parameter.
    user_id: Optional[str] = None
    world_id: str = "syriac-edessa-nisibis"  # Primary/first world (for backwards compat)
    world_ids: list[str] = field(default_factory=list)  # All worlds at table
    close_requested: bool = False

    # Sensed closing sequence (CiC_Sensed_Closing_Sequence_Spec_V0_1.md). The
    # session-level stage of the wind-down flow: sense -> ask "anything else?"
    # -> offer resources -> show -> sensed close. Governs routing only; never
    # surfaced to the participant as a mechanic. "none" = not in a closing
    # sequence. A genuine new question at "anything_else_asked" resets this to
    # "none" and normal flow resumes (the false-positive escape hatch). Distinct
    # from close_requested, which is the untouched explicit-close path.
    closing_stage: Literal[
        "none", "anything_else_asked", "resources_offered", "resources_shown", "closed"
    ] = "none"
