"""FastAPI application for the CiC POC backend."""

import uuid
from contextlib import asynccontextmanager
from typing import Optional

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from langchain_core.messages import HumanMessage
from pydantic import BaseModel

from app.config import settings
from app.graph.builder import get_compiled_graph
from app.graph.nodes import get_retriever, representative_engages
from app.graph.state import ConversationState


# In-memory session storage (POC only)
sessions: dict[str, ConversationState] = {}


def load_world_content(world_id: str = "syriac-edessa-nisibis") -> tuple[str, str]:
    """Load the permanent prompt and world capsule content for a specific world."""
    world_config = settings.get_world_config(world_id)
    permanent_prompt = world_config.permanent_prompt_path.read_text(encoding="utf-8")
    world_capsule = world_config.world_capsule_path.read_text(encoding="utf-8")
    return permanent_prompt, world_capsule


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan handler."""
    # Pre-load the RAG indexes for all worlds on startup
    print("Loading RAG indexes for all worlds...")
    for world in AVAILABLE_WORLDS:
        try:
            get_retriever(world.id)
            print(f"  {world.name}: loaded successfully")
        except Exception as e:
            print(f"  {world.name}: Warning - Could not load index: {e}")
            print(f"    RAG retrieval will be attempted on first request")

    yield

    # Cleanup
    sessions.clear()


app = FastAPI(
    title="Church in Conversation POC",
    description="The Table - Engaging conversations with voices from Christian history",
    version="0.1.0",
    lifespan=lifespan,
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Request/Response models
class StartSessionRequest(BaseModel):
    """Request to start a new session."""

    world_id: str = "syriac-edessa-nisibis"  # For single-world (backwards compat)
    world_ids: list[str] = []  # For multi-world table (1-5 worlds)


class StartSessionResponse(BaseModel):
    """Response for starting a new session."""

    session_id: str
    messages: list[dict]
    world_id: str  # Primary world (first in list)
    world_ids: list[str] = []  # All worlds at table


class SendMessageRequest(BaseModel):
    """Request to send a message."""

    message: str
    close_requested: bool = False


class SendMessageResponse(BaseModel):
    """Response after sending a message."""

    messages: list[dict]
    phase: str
    turn_count: int


class SessionResponse(BaseModel):
    """Response for getting session state."""

    session_id: str
    messages: list[dict]
    phase: str
    turn_count: int


def state_to_messages(state: ConversationState) -> list[dict]:
    """Convert state messages to serializable dicts."""
    result = []
    for msg in state.messages:
        role = "assistant"
        name = None

        if isinstance(msg, HumanMessage):
            role = "user"
        elif hasattr(msg, "name"):
            name = msg.name

        # Handle extended thinking responses where content is a list of blocks
        content = msg.content
        if isinstance(content, list):
            # Extract text content from content blocks
            text_parts = []
            for block in content:
                if isinstance(block, dict) and block.get("type") == "text":
                    text_parts.append(block.get("text", ""))
                elif isinstance(block, str):
                    text_parts.append(block)
            content = "\n".join(text_parts)

        citations = None
        if hasattr(msg, "additional_kwargs"):
            citations = msg.additional_kwargs.get("citations") or None

        result.append({
            "role": role,
            "content": content,
            "name": name,
            "citations": citations,
        })

    return result


@app.post("/api/session/start", response_model=StartSessionResponse)
async def start_session(request: StartSessionRequest):
    """
    Start a new conversation session.

    This initializes the conversation with the facilitator's welcome
    and introduction of the representative(s) for the selected world(s).

    Supports both single-world (world_id) and multi-world (world_ids) modes.
    Multi-world tables allow 1-5 representatives to engage together.
    """
    from app.graph.state import WorldContext

    session_id = str(uuid.uuid4())
    valid_world_ids = [w.id for w in AVAILABLE_WORLDS]

    # Determine which worlds are at the table
    if request.world_ids:
        # Multi-world mode
        world_ids = request.world_ids[:5]  # Cap at 5 worlds max
        for wid in world_ids:
            if wid not in valid_world_ids:
                raise HTTPException(
                    status_code=400,
                    detail=f"Invalid world_id '{wid}'. Must be one of: {valid_world_ids}"
                )
        world_id = world_ids[0]  # Primary world is first in list
    else:
        # Single-world mode (backwards compatible)
        world_id = request.world_id
        if world_id not in valid_world_ids:
            raise HTTPException(
                status_code=400,
                detail=f"Invalid world_id. Must be one of: {valid_world_ids}"
            )
        world_ids = [world_id]

    # Load world content for primary world (legacy fields)
    permanent_prompt, world_capsule = load_world_content(world_id)

    # Build WorldContext for all worlds at the table
    worlds_at_table = []
    for wid in world_ids:
        w_prompt, w_capsule = load_world_content(wid)
        worlds_at_table.append(WorldContext(
            world_id=wid,
            permanent_prompt=w_prompt,
            world_capsule=w_capsule,
        ))

    # Create initial state
    initial_state = ConversationState(
        session_id=session_id,
        world_id=world_id,
        world_ids=world_ids,
        worlds_at_table=worlds_at_table,
        permanent_prompt=permanent_prompt,
        world_capsule_core=world_capsule,
        current_world_id=world_id,  # First representative speaks first
    )

    # Run the graph through reception and handoff
    graph = get_compiled_graph()
    result = graph.invoke(initial_state)

    # Convert result to ConversationState if needed
    if isinstance(result, dict):
        # Update state with results
        state = ConversationState(
            messages=result.get("messages", []),
            phase=result.get("phase", "active_encounter"),
            current_speaker=result.get("current_speaker", "representative"),
            turn_count=result.get("turn_count", 0),
            session_id=session_id,
            world_id=world_id,
            world_ids=world_ids,
            worlds_at_table=worlds_at_table,
            current_world_id=result.get("current_world_id", world_id),
            permanent_prompt=permanent_prompt,
            world_capsule_core=world_capsule,
        )
    else:
        state = result

    # Store session
    sessions[session_id] = state

    return StartSessionResponse(
        session_id=session_id,
        messages=state_to_messages(state),
        world_id=world_id,
        world_ids=world_ids,
    )


@app.post("/api/session/{session_id}/message", response_model=SendMessageResponse)
async def send_message(session_id: str, request: SendMessageRequest):
    """
    Send a message in an existing conversation.

    The message is processed by the representative (with RAG augmentation)
    and then monitored for drift by the facilitator.
    """
    if session_id not in sessions:
        raise HTTPException(status_code=404, detail="Session not found")

    state = sessions[session_id]

    # Handle close request
    if request.close_requested:
        state.close_requested = True

        # Run closing node
        from app.graph.nodes import facilitator_closes
        result = facilitator_closes(state)

        # Update state
        state.messages = list(state.messages) + result.get("messages", [])
        state.phase = result.get("phase", "closing")

        sessions[session_id] = state

        return SendMessageResponse(
            messages=state_to_messages(state),
            phase=state.phase,
            turn_count=state.turn_count,
        )

    # Add the participant's message
    state.messages = list(state.messages) + [HumanMessage(content=request.message)]

    # For multi-world tables, determine turn type (single or all representatives)
    from app.graph.nodes import determine_turn_type, multi_representative_engages

    if state.world_ids and len(state.world_ids) > 1:
        turn_type, responding_worlds = determine_turn_type(state)

        if turn_type == "all" and len(responding_worlds) > 1:
            # Multiple representatives should respond - each sees what others said
            state.current_world_id = responding_worlds[0]
            result = multi_representative_engages(state)
        else:
            # Single representative responds
            state.current_world_id = responding_worlds[0]
            result = representative_engages(state)
    else:
        # Single-world table
        result = representative_engages(state)

    # Update state with representative's response(s)
    state.messages = list(state.messages) + result.get("messages", [])
    state.turn_count = result.get("turn_count", state.turn_count)
    state.requires_reroot = result.get("requires_reroot", False)
    state.retrieved_context = result.get("retrieved_context")
    state.current_world_id = result.get("current_world_id", state.current_world_id)

    # Run monitoring
    from app.graph.nodes import facilitator_monitors, facilitator_reroots

    monitor_result = facilitator_monitors(state)
    state.requires_reroot = monitor_result.get("requires_reroot", False)

    if monitor_result.get("drift_signals"):
        state.drift_signals = list(state.drift_signals) + monitor_result["drift_signals"]

    # If reroot needed, run reroot (invisible to participant)
    if state.requires_reroot:
        reroot_result = facilitator_reroots(state)
        if reroot_result.get("drift_signals"):
            state.drift_signals = list(state.drift_signals) + reroot_result["drift_signals"]
        state.requires_reroot = reroot_result.get("requires_reroot", False)

    # Store updated session
    sessions[session_id] = state

    return SendMessageResponse(
        messages=state_to_messages(state),
        phase=state.phase,
        turn_count=state.turn_count,
    )


@app.get("/api/session/{session_id}", response_model=SessionResponse)
async def get_session(session_id: str):
    """
    Get the current state of a conversation session.

    Useful for reconnection or state inspection.
    """
    if session_id not in sessions:
        raise HTTPException(status_code=404, detail="Session not found")

    state = sessions[session_id]

    return SessionResponse(
        session_id=session_id,
        messages=state_to_messages(state),
        phase=state.phase,
        turn_count=state.turn_count,
    )


class Representative(BaseModel):
    """A representative from a world."""

    id: str
    name: str
    title: str
    description: str


class World(BaseModel):
    """A world/tradition available for conversation."""

    id: str
    name: str
    period: str
    region: str
    description: str
    representative: Representative
    color: str  # For UI theming


class WorldsResponse(BaseModel):
    """Response containing available worlds."""

    worlds: list[World]


# Define available worlds (hardcoded for POC, would come from config/DB later)
AVAILABLE_WORLDS = [
    World(
        id="syriac-edessa-nisibis",
        name="Syriac Christianity",
        period="200–410 CE",
        region="Edessa & Nisibis",
        description="A community shaped by persecution under Persian rule, holding together through covenant vows and typological reading of Scripture. Their bishops were martyred, their see stood empty for decades, yet their teaching endured.",
        representative=Representative(
            id="mar-yausep",
            name="Mar Yausep",
            title="Teacher of the Covenant Order",
            description="A teacher formed within the community that reads Scripture by raza, keeps the qyama vow, and gathers under one harmonized Gospel. He speaks from the tradition's own life, not as one defending it from outside.",
        ),
        color="#b45309",  # Warm amber
    ),
    World(
        id="post-apostolic-house-church",
        name="Post-Apostolic House-Church",
        period="70–200 CE",
        region="Antioch, Asia Minor, Rome",
        description="The scattered household gatherings that held together after the apostles were gone — connected by letters, formed by the table, still arguing about who should lead and what the body's suffering truly means.",
        representative=Representative(
            id="amma",
            name="Amma",
            title="Household Leader",
            description="A woman whose door opens for the gathering, who teaches those preparing for the water, who receives the letters that travel between one ekklesia and another. She speaks as 'we' because she carries this people's whole life, not one witness within it.",
        ),
        color="#7c3aed",  # Deep purple
    ),
]


class LexiconTerm(BaseModel):
    """A lexicon term with its definitions."""

    term: str
    aliases: list[str]
    quick_meaning: str
    full_content: str
    related_terms: list[str]


class LexiconResponse(BaseModel):
    """Response containing all lexicon terms."""

    terms: list[LexiconTerm]


@app.get("/api/lexicon", response_model=LexiconResponse)
async def get_lexicon(world_id: str = "syriac-edessa-nisibis"):
    """
    Get all lexicon terms for a specific world.

    Returns terms with their quick meanings (for tooltips)
    and full content (for detail views).
    """
    from app.rag.indexer import LexiconIndexer

    # Validate world_id
    valid_world_ids = [w.id for w in AVAILABLE_WORLDS]
    if world_id not in valid_world_ids:
        raise HTTPException(status_code=400, detail=f"Invalid world_id. Must be one of: {valid_world_ids}")

    world_config = settings.get_world_config(world_id)
    indexer = LexiconIndexer()
    lexicon_path = world_config.lexicon_chunks_path

    terms = []
    for file_path in sorted(lexicon_path.glob("*.md")):
        # Read full file content to extract Quick Meaning
        full_content = file_path.read_text(encoding="utf-8")
        entry = indexer.parse_lexicon_file(file_path)

        # Extract quick meaning - it's between first --- and second ---
        quick_meaning = ""
        if "## Quick Meaning" in full_content:
            parts = full_content.split("## Quick Meaning", 1)
            if len(parts) > 1:
                # Get text after "## Quick Meaning" until next "---" or "##"
                remaining = parts[1]
                # Find end of quick meaning section
                end_markers = ["---", "## "]
                end_pos = len(remaining)
                for marker in end_markers:
                    pos = remaining.find(marker)
                    if pos > 0 and pos < end_pos:
                        end_pos = pos
                quick_meaning = remaining[:end_pos].strip()

        terms.append(LexiconTerm(
            term=entry.term,
            aliases=entry.aliases,
            quick_meaning=quick_meaning,
            full_content=entry.content,
            related_terms=entry.related_terms,
        ))

    return LexiconResponse(terms=terms)


@app.get("/api/worlds", response_model=WorldsResponse)
async def get_worlds():
    """
    Get all available worlds for conversation.

    Returns worlds with their representatives and metadata.
    """
    return WorldsResponse(worlds=AVAILABLE_WORLDS)


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "version": "0.1.0"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host=settings.host, port=settings.port)
