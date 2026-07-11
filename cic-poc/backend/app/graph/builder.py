"""Build and compile the LangGraph conversation graph."""

from langgraph.graph import END, START, StateGraph

from app.graph.nodes import (
    facilitator_closes,
    facilitator_handoff,
    facilitator_monitors,
    facilitator_receives,
    facilitator_reroots,
    representative_engages,
    route_after_input,
    route_after_monitoring,
)
from app.graph.state import ConversationState


def build_conversation_graph() -> StateGraph:
    """
    Build the conversation graph for The Table.

    Graph Flow:
        START
          │
          ▼
        facilitator_receives (warm welcome)
          │
          ▼
        facilitator_handoff (introduce Mar Yausep)
          │
          ▼
        ┌─────────────────────────────────┐
        │     wait_for_input              │◄──────────┐
        │         │                       │           │
        │         ▼                       │           │
        │  representative_engages         │           │
        │  (RAG-augmented response)       │           │
        │         │                       │           │
        │         ▼                       │           │
        │  facilitator_monitors           │           │
        │  (invisible drift check)        │           │
        │         │                       │           │
        │    ┌────┴────┐                  │           │
        │    │         │                  │           │
        │  drift?   no drift              │           │
        │    │         │                  │           │
        │    ▼         └──────────────────┼───────────┘
        │  facilitator_reroots            │
        │  (invisible correction)         │
        │    │                            │
        │    └────────────────────────────┘
        │
        │  (on close signal)
        │         │
        │         ▼
        │  facilitator_closes
        │         │
        │         ▼
        │        END
    """
    # Create the graph with our state schema
    graph = StateGraph(ConversationState)

    # Add nodes
    graph.add_node("facilitator_receives", facilitator_receives)
    graph.add_node("facilitator_handoff", facilitator_handoff)
    graph.add_node("representative_engages", representative_engages)
    graph.add_node("facilitator_monitors", facilitator_monitors)
    graph.add_node("facilitator_reroots", facilitator_reroots)
    graph.add_node("facilitator_closes", facilitator_closes)

    # Entry point
    graph.add_edge(START, "facilitator_receives")

    # Reception -> Handoff
    graph.add_edge("facilitator_receives", "facilitator_handoff")

    # Handoff -> End (waits for input via interrupt)
    # In practice, we'll use interrupt_before on representative_engages
    graph.add_edge("facilitator_handoff", END)

    # After representative responds, monitor for drift
    graph.add_edge("representative_engages", "facilitator_monitors")

    # Conditional routing after monitoring
    graph.add_conditional_edges(
        "facilitator_monitors",
        route_after_monitoring,
        {
            "reroot": "facilitator_reroots",
            "wait": END,  # Wait for next input
            "close": "facilitator_closes",
        },
    )

    # After reroot, go back to wait for input
    graph.add_edge("facilitator_reroots", END)

    # Closing ends the conversation
    graph.add_edge("facilitator_closes", END)

    return graph


def compile_graph():
    """Compile the graph for execution."""
    graph = build_conversation_graph()
    return graph.compile()


# Pre-compiled graph instance
compiled_graph = None


def get_compiled_graph():
    """Get or create the compiled graph."""
    global compiled_graph
    if compiled_graph is None:
        compiled_graph = compile_graph()
    return compiled_graph
