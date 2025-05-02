from flask import Flask, request, jsonify
from flask_cors import CORS

from ingestion.repo import clone_repo, section_files

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
        local_path = clone_repo(repo_url)
        sectioned_files = section_files(local_path)
        
                
    except Exception as e:
        print(f"❌ Error processing repo: {e}")
        return jsonify({"error": "Failed to fetch README."}), 500
