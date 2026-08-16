"""Replicates cic/runtime/app/graph/nodes.py get_llm + _cached_system_message
exactly, then reports RAW API usage vs what log_llm_usage would extract."""
import os, json
from pathlib import Path
from langchain_anthropic import ChatAnthropic
from langchain_core.messages import SystemMessage, HumanMessage

KEY = os.environ["CIC_ANTHROPIC_KEY"]
MODEL = "claude-sonnet-5"                       # render.yaml LLM_MODEL
STATIC = Path("/tmp/pay_syriac_static.txt").read_text()
DYNAMIC = ("# Context That May Be Relevant\nThe following may be relevant to what the "
           "participant is asking. Draw on this naturally if it fits - do not force it.\n\n"
           "## Retrieved Lexicon Context\n### qyama\nA covenant of consecrated life entered "
           "at baptism.\n---\n")
CONT = "The participant says: What is your community's hope for the dead?\n\nRespond as yourself."

def get_llm(max_tokens):                        # verbatim from nodes.py get_llm
    kwargs = {"model": MODEL, "anthropic_api_key": KEY}
    if max_tokens:
        kwargs["max_tokens"] = max_tokens
        kwargs["thinking"] = {"type": "disabled"}
    return ChatAnthropic(**kwargs)

def cached_system_message(static, reactive, dynamic, ttl):   # verbatim shape
    blocks = [{"type": "text", "text": static,
               "cache_control": {"type": "ephemeral", "ttl": ttl}}]
    if reactive:
        blocks.append({"type": "text", "text": reactive,
                       "cache_control": {"type": "ephemeral", "ttl": ttl}})
    if dynamic:
        blocks.append({"type": "text", "text": dynamic})
    return SystemMessage(content=blocks)

def extract_like_logger(resp):                  # verbatim from usage_logging.py
    um = getattr(resp, "usage_metadata", None) or {}
    it, ot = um.get("input_tokens", 0), um.get("output_tokens", 0)
    rm = getattr(resp, "response_metadata", None) or {}
    raw = rm.get("usage") or {}
    cc = raw.get("cache_creation_input_tokens", 0)
    cr = raw.get("cache_read_input_tokens", 0)
    if not raw:
        d = um.get("input_token_details") or {}
        cc, cr = d.get("cache_creation", 0), d.get("cache_read", 0)
    return it, ot, cc, cr, raw, um

def run(mode, ttl, label):
    llm = get_llm(1200)
    msgs = [cached_system_message(STATIC, "", DYNAMIC, ttl), HumanMessage(content=CONT)]
    if mode == "stream":
        acc = None
        for ch in llm.stream(msgs):
            acc = ch if acc is None else acc + ch
        resp = acc
    else:
        resp = llm.invoke(msgs)
    it, ot, cc, cr, raw, um = extract_like_logger(resp)
    print(f"\n=== {label}  [{mode}, ttl={ttl}] ===")
    print(f"  logger would record: input={it} output={ot} cache_creation={cc} cache_read={cr}")
    print(f"  raw response_metadata['usage'] = {json.dumps(raw)}")
    print(f"  usage_metadata               = {json.dumps({k:v for k,v in um.items()})}")
    return cc, cr, it, ot

print("langchain_anthropic test; static prompt = syriac, %d chars" % len(STATIC))
a1 = run("stream", "1h", "A1 first call (expect cache WRITE)")
a2 = run("stream", "1h", "A2 second call (expect cache READ)")
a3 = run("invoke", "1h", "A3 non-streaming (expect cache READ)")
if a2[1] == 0:
    b1 = run("stream", "5m", "B1 default 5m TTL, first")
    b2 = run("stream", "5m", "B2 default 5m TTL, second (expect READ)")
