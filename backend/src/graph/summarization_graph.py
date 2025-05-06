from langgraph.graph import StateGraph

from models.doc_chunk import DocChunk
from graph.nodes.summarize_chunk_node import summarize_chunk_node
from graph.nodes.save_chunk_vector_node import save_chunk_to_vector_db_node

# Define the state type: just a single DocChunk
State = dict[str, DocChunk]

# Wrap your node in a ToolNode so LangGraph can run it
def summarize_node_tool(state: State) -> State:
    return summarize_chunk_node(state)

def save_node_tool(state: State) -> State:
    return save_chunk_to_vector_db_node(state)

def build_summarization_graph():
    graph = StateGraph(State)

    # Add node
    graph.add_node("summarize", summarize_node_tool)
    graph.add_node("store", save_node_tool)

    # Set up flow
    graph.set_entry_point("summarize")
    graph.add_edge("summarize", "store")
    graph.set_finish_point("store")

    return graph.compile()