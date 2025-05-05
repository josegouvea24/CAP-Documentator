from langgraph.graph import StateGraph

from models.chunk import DocChunk
from nodes.summarize_chunk_node import summarize_chunk_node

# Define the state type: just a single DocChunk
State = dict[str, DocChunk]

# Wrap your node in a ToolNode so LangGraph can run it
def summarize_node_tool(state: State) -> State:
    chunk = state["chunk"]
    summarized_chunk = summarize_chunk_node(chunk)
    return {"chunk": summarized_chunk}

def build_summarization_graph():
    graph = StateGraph(State)

    # Add node
    graph.add_node("summarize", summarize_node_tool)

    # Set up flow
    graph.set_entry_point("summarize")
    graph.set_finish_point("summarize")

    return graph.compile()