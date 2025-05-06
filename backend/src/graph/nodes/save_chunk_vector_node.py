from models.doc_chunk import DocChunk
from db.vector_hanaDB import CAPVectorDBHelper


def save_chunk_to_vector_db_node(state: dict[str, DocChunk]) -> dict[str, DocChunk]:
    chunk = state["chunk"]
    db = CAPVectorDBHelper()

    if not chunk.summary or "ERROR" in chunk.summary:
        print(f"⚠️ Skipping chunk {chunk.name} due to missing or invalid summary.")
        return {"chunk": chunk}

    metadata = {
        "name": chunk.name,
        "path": chunk.path,
        "section": chunk.section,
        "type": chunk.type,
    }

    db.add_summary(content=chunk.summary, metadata=metadata)
    return {"chunk": chunk}
