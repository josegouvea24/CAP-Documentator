from flask import Flask, request, jsonify
from flask_cors import CORS

from ingestion.repo import clone_and_prepare, collect_all_files
from processing.file_loader import load_file_content
from generation.llm import generate_cds_documentation

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
        local_path = clone_and_prepare(repo_url)
        files = collect_all_files(local_path)
        file_content = load_file_content(files)
        llm_response = generate_cds_documentation(file_content)
        
        return jsonify({"readme": llm_response}), 200
        
    except Exception as e:
        print(f"❌ Error processing repo: {e}")
        return jsonify({"error": "Failed to fetch README."}), 500
