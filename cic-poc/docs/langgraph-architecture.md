# LangGraph Architecture

## Conversation Flow Diagram

```mermaid
flowchart TD
    subgraph Entry["Session Start"]
        START((START))
    end

    subgraph Reception["Reception Phase"]
        FR[/"facilitator_receives<br/>─────────────<br/>Warm welcome<br/>(1-2 sentences)"/]
    end

    subgraph Handoff["Handoff Phase"]
        FH[/"facilitator_handoff<br/>─────────────<br/>Introduce Mar Yausep<br/>(2-3 sentences)"/]
    end

    subgraph ActiveEncounter["Active Encounter Phase"]
        WAIT((Wait for<br/>Input))
        RE[["representative_engages<br/>─────────────<br/>RAG-augmented response<br/>• Retrieves lexicon context<br/>• Builds demonstration<br/>• Speaks as 'we'"]]
        FM{{"facilitator_monitors<br/>─────────────<br/>Drift detection<br/>(invisible)"}}
        FRR[/"facilitator_reroots<br/>─────────────<br/>Correction guidance<br/>(invisible)"/]
    end

    subgraph Closing["Closing Phase"]
        FC[/"facilitator_closes<br/>─────────────<br/>Brief goodbye<br/>(no summary)"/]
        END((END))
    end

    START --> FR
    FR --> FH
    FH --> WAIT

    WAIT -->|"participant<br/>message"| RE
    RE --> FM

    FM -->|"no drift"| WAIT
    FM -->|"drift detected"| FRR
    FM -->|"close requested"| FC

    FRR --> WAIT

    FC --> END

    classDef facilitator fill:#e8f0ea,stroke:#7c9885,stroke-width:2px,color:#2d5a3d
    classDef representative fill:#fef3e2,stroke:#b45309,stroke-width:2px,color:#92400e
    classDef invisible fill:#f3f4f6,stroke:#9ca3af,stroke-width:2px,stroke-dasharray: 5 5,color:#6b7280
    classDef control fill:#fff,stroke:#374151,stroke-width:1px
    classDef endpoint fill:#374151,stroke:#374151,color:#fff

    class FR,FH,FC facilitator
    class RE representative
    class FM,FRR invisible
    class WAIT control
    class START,END endpoint
```

## Node Descriptions

### Facilitator Nodes (Visible to Participant)

| Node | Phase | Purpose |
|------|-------|---------|
| `facilitator_receives` | Reception | Warm, brief welcome (1-2 sentences) |
| `facilitator_handoff` | Handoff | Introduce Mar Yausep, step back |
| `facilitator_closes` | Closing | Brief goodbye, no summary |

### Facilitator Nodes (Invisible to Participant)

| Node | Phase | Purpose |
|------|-------|---------|
| `facilitator_monitors` | Active | Check for drift signals after each response |
| `facilitator_reroots` | Active | Inject correction guidance if drift detected |

### Representative Node

| Node | Phase | Purpose |
|------|-------|---------|
| `representative_engages` | Active | RAG-augmented response from Mar Yausep |

## Drift Signals Monitored

```mermaid
mindmap
  root((Drift<br/>Detection))
    Smoothing
      Making harsh truths comfortable
    Generating
      Inventing personal memories
    Agreeing
      Abandoning position to please
    First-Person
      Using "I" instead of "we"
    Anachronism
      Speaking beyond 410 CE
    Fabrication
      Creating unattested details
    Apologetics
      Defending rather than witnessing
```

## State Schema

```mermaid
classDiagram
    class ConversationState {
        +List~Message~ messages
        +String phase
        +String current_speaker
        +int turn_count
        +List~DriftSignal~ drift_signals
        +bool requires_reroot
        +RetrievedContext retrieved_context
        +String world_capsule_core
        +String permanent_prompt
        +String session_id
        +bool close_requested
    }

    class DriftSignal {
        +String signal_type
        +String description
        +String severity
    }

    class RetrievedContext {
        +List~String~ chunks
        +List~String~ terms
        +List~String~ sources
    }

    ConversationState "1" --> "*" DriftSignal
    ConversationState "1" --> "0..1" RetrievedContext
```

## RAG Integration

```mermaid
sequenceDiagram
    participant P as Participant
    participant RE as representative_engages
    participant RET as LexiconRetriever
    participant VS as FAISS VectorStore
    participant LLM as Claude API

    P->>RE: Send message
    RE->>RET: get_context_for_response(query)
    RET->>VS: similarity_search(query)
    VS-->>RET: candidate documents

    loop For each candidate
        RET->>LLM: Evaluate Retrieve-When conditions
        LLM-->>RET: RETRIEVE or SKIP
    end

    RET-->>RE: filtered context
    RE->>LLM: Generate response with context
    LLM-->>RE: Mar Yausep's response
    RE-->>P: Display response
```
