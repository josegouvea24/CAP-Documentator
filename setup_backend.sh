#!/bin/bash

# ─────────────────────────────────────────────
# CAP Documentator – Flask Backend Setup Script (SAP CF + README Generator)
# ─────────────────────────────────────────────

echo "📁 Creating project and backend folder structure..."
mkdir -p CAP-Documentator/backend/src/{api,ingestion,processing,rag,generation,models,utils}
cd CAP-Documentator

echo "🐍 Creating Python virtual environment with virtualenvwrapper..."
export WORKON_HOME=$HOME/.virtualenvs
source $(which virtualenvwrapper.sh)
mkvirtualenv cap-documentator-env
workon cap-documentator-env

cd backend

echo "📦 Writing Python dependencies to requirements.txt..."
cat <<EOF > requirements.txt
flask
gitpython
langchain
chromadb
python-docx
openai
requests
flask-cors
EOF

pip install -r requirements.txt

echo "📝 Creating Flask API entrypoint..."
cat <<EOF > src/api/main.py
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
EOF

echo "🐙 Adding repo ingestion module..."
cat <<EOF > src/ingestion/repo.py
import os
from git import Repo
import shutil

def clone_and_prepare(repo_url: str, clone_dir="tmp_project") -> str:
    if os.path.exists(clone_dir):
        shutil.rmtree(clone_dir)
    Repo.clone_from(repo_url, clone_dir)
    return clone_dir
EOF

echo "📄 Creating documentation generation mock..."
cat <<EOF > src/generation/report.py
def generate_doc(local_path: str) -> str:
    # Placeholder: integrate LangChain and docx later
    return f"{local_path}/mock_documentation.docx"
EOF

echo "⚙️ Creating Cloud Foundry manifest..."
cat <<EOF > manifest.yml
applications:
- name: cap-documentator-backend
  memory: 512M
  buildpacks:
    - python_buildpack
  command: python src/api/main.py
  path: .
EOF

echo "📝 Creating README.md..."
cat <<EOF > README.md
# 📄 CAP Documentator

> ⚙️ AI-powered documentation generator for SAP CAP projects using LangChain, Flask, and SAP Fiori/UI5.

---

## 📌 Overview

**CAP Documentator** is an intelligent documentation assistant for SAP CAP projects. It ingests a GitHub repository, analyzes the structure and metadata of the CAP framework, and generates a polished, Word-format documentation report using a retrieval-augmented generation (RAG) pipeline.

---

## 🚀 Features

- 🔗 **GitHub/GitHub Enterprise Integration** — Input a repo URL, and the app ingests it automatically
- 📘 **CAP-Aware File Analysis** — Parses .cds, package.json, srv/, db/, app/ and more
- 🧠 **LangChain + LLM-Powered Documentation** — Generates contextual documentation using RAG
- 📝 **Word Document Output** — Generates .docx with structure, models, logic & services
- 🌐 **Freestyle UI5 Frontend** — Built with SAP Fiori design principles
- ☁️ **Cloud Foundry Deployment Ready** — Backend and frontend deployable on SAP BTP

---

## 📂 Project Structure

\`\`\`bash
CAP-Documentator/
├── app/                            # Frontend application
│   └── fiori-ui/                   # Freestyle SAPUI5 Fiori app
│       ├── webapp/                 # Main source folder for the UI app
│       │   ├── controller/         # Handles event logic for views
│       │   ├── css/                # Custom stylesheets (optional)
│       │   ├── i18n/               # Internationalization (i18n) resource bundles
│       │   ├── model/              # Data models (OData, JSON)
│       │   ├── test/               # UI unit/integration tests
│       │   └── view/               # XML views that define the UI layout
│       ├── Component.ts            # Main entry module for the UI5 app
│       ├── index.html              # App entry HTML file
│       ├── manifest.json           # App descriptor (routes, dataSources, models)
│       ├── xs-app.json             # CF HTML5 app router config
│       ├── xs-security.json        # Security descriptor (used with XSUAA)
│       ├── mta.yaml                # Multi-target application descriptor (for CF)
│       ├── ui5.yaml                # UI5 tooling configuration
│       ├── ui5-deploy.yaml         # UI5 deployer config for CF HTML5 repo
│       ├── ui5-local.yaml          # UI5 tooling config for local run
│       ├── package.json            # NPM project metadata
│       └── package-lock.json       # NPM dependency lock file
├── backend/                        # Python backend (Flask, LangChain)
│   ├── src/
│   │   ├── api/                    # API endpoints
│   │   ├── ingestion/              # GitHub repo cloning and preparation
│   │   ├── processing/             # File structure + CAP metadata parsing
│   │   ├── rag/                    # LangChain logic and vector store setup
│   │   ├── generation/             # .docx file generation using python-docx
│   │   ├── models/                 # Embedding & LLM initialization
│   │   └── utils/                  # Logging, common utilities
│   ├── manifest.yml                # Cloud Foundry deployment descriptor
│   ├── requirements.txt            # Python dependencies
│   └── src/api/main.py             # Flask app entrypoint
\`\`\`

---

## 💻 Local Development Setup

### 🔧 Prerequisites
- Python 3.9+
- Node.js (for UI5 frontend)
- virtualenvwrapper
- SAP Cloud Foundry CLI (cf)

### 🧠 Python Backend
\`\`\`bash
workon cap-documentator-env
cd backend
python src/api/main.py
\`\`\`

### 🌐 UI5 Frontend
\`\`\`bash
cd app/fiori-ui
npm install
npm start
\`\`\`

---

## ☁️ Deploying to SAP BTP Cloud Foundry

\`\`\`bash
cf login -a https://api.cf.<region>.hana.ondemand.com
cd backend
cf push
\`\`\`

> For MTA-based deployment:

\`\`\`bash
mbt build
cf deploy mta_archives/CAP-Documentator.mtar
\`\`\`

---

## 🛠️ Tech Stack

| Component       | Tech Stack                |
|----------------|---------------------------|
| Frontend        | SAPUI5 (freestyle), Fiori |
| Backend         | Python, Flask             |
| AI & RAG        | LangChain, OpenAI         |
| File Generation | python-docx               |
| Deployment      | SAP BTP Cloud Foundry     |

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

## 👥 Contributors

- [Your Name / Team]
- Open to contributions — PRs and ideas welcome!

---
EOF

echo "✅ Flask backend setup complete with README.md generated!"
echo "👉 Activate your env with: workon cap-documentator-env"
echo "👉 Run locally: python src/api/main.py"
echo "👉 Push to Cloud Foundry: cf push"