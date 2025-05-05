import os
from models.chunk import DocChunk
from templates.prompts import get_chunk_summary_prompt
from services.llm import call_llm

def summarize_chunk_node(chunk: DocChunk) -> DocChunk:
    """
    LangGraph node: generates a structured LLM summary for a given DocChunk.
    """
    try:
        prompt = get_chunk_summary_prompt(chunk)
        summary = call_llm(prompt, model= os.getenv("MODEL_CHUNK_SUMMARY"), temperature=0)
        chunk.metadata["summary"] = summary.strip()
        return chunk

    except Exception as e:
        chunk.metadata["summary_error"] = str(e)
        return chunk