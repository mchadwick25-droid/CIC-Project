"""LangGraph state schema for The Table conversation."""

from dataclasses import dataclass, field
from typing import Annotated, Literal, Optional

from langgraph.graph import add_messages
from langchain_core.messages import BaseMessage


@dataclass
class DriftSignal:
    """A detected drift signal in the representative's response."""

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
        "dominance",
        "convergence",
    ]
    description: str
    severity: Literal["low", "medium", "high"]
    # Which representative this signal concerns - None for the original
    # single-representative signals above, which apply to whoever spoke last.
    # "dominance" and "convergence" are multi-representative-table signals
    # and are always attributed to a specific world_id.
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
    # by world_id - populated by dominance/convergence checks after a
    # multi-representative round, consumed (and cleared) the next time that
    # representative speaks. Kept separate from requires_reroot/drift_signals
    # because those are global to "whoever spoke last," not per-representative.
    pending_guidance: dict[str, str] = field(default_factory=dict)

    # RAG context
    retrieved_context: Optional[RetrievedContext] = None

    # Multi-world support: list of worlds at the table
    worlds_at_table: list[WorldContext] = field(default_factory=list)

    # Legacy single-world fields (for backwards compatibility)
    world_capsule_core: str = ""
    permanent_prompt: str = ""

    # Session management
    session_id: str = ""
    world_id: str = "syriac-edessa-nisibis"  # Primary/first world (for backwards compat)
    world_ids: list[str] = field(default_factory=list)  # All worlds at table
    close_requested: bool = False
