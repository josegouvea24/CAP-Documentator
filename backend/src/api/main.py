from flask import Flask, request, jsonify
from flask_cors import CORS
from ingestion.repo import clone_and_prepare
from generation.report import generate_doc

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def index():
    return jsonify({"message": "CAP Documentator Backend is live."})

@app.route("/document", methods=["POST"])
def document_project():
    data = request.json
    repo_url = data.get("repo_url")
    local_path = clone_and_prepare(repo_url)
    doc_path = generate_doc(local_path)
    return jsonify({"doc_path": doc_path})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
