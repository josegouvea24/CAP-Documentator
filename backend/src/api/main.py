from flask import Flask, request, jsonify
from flask_cors import CORS

from utils.repo_loader import clone_repo, section_files
from utils.chunker import chunk_files
from graph.summarization_graph import build_summarization_graph

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def index():
    return jsonify({"message": "CAP Documentator Backend is live."})

@app.route("/readme", methods=["POST"])
def document():
    data = request.json
    repo_url = data.get("url")

    if not repo_url:
        return jsonify({"error": "Missing 'url' in request body"}), 400

    try:
        # 1. Clone repo
        local_repo_path = clone_repo(repo_url)

        # 2. Find files and group by section
        sectioned_files = section_files(local_repo_path)

        # 3. Chunk files into DocChunks
        chunks = chunk_files(local_repo_path, sectioned_files)

        # 4. Build and run LangGraph summarization pipeline
        graph = build_summarization_graph()

        results = []
        for chunk in chunks:
            print(f"📄 Processing: {chunk.path}")
            result = graph.invoke({"chunk": chunk})
            results.append(result["chunk"].path)

        return jsonify({"message": "Documentation completed", "processed_files": results}), 200

    except Exception as e:
        print(f"❌ Error processing repo: {e}")
        return jsonify({"error": "Failed to process repository."}), 500
