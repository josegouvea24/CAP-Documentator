import os
from models.doc_chunk import DocChunk
from llm.prompts import get_chunk_summary_prompt
from llm.llm import call_llm

def summarize_chunk_node(state: dict[str, DocChunk]) -> dict[str, DocChunk]:
    try:
        chunk = state["chunk"]
        prompt = get_chunk_summary_prompt(chunk)
        summary = call_llm(prompt, model=os.getenv("MODEL_CHUNK_SUMMARY"), temperature=0)
        chunk.summary = summary.strip()
        return {"chunk": chunk}
    
    except Exception as e:
        chunk.summary = f"[SUMMARY ERROR: {e}]"
        return {"chunk": chunk}
