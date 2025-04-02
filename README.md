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

```bash
CAP-Documentator/
├── app/                            # Frontend application
│   └── fiori-ui/                   # Freestyle SAPUI5 Fiori app
│       ├── webapp/                 # Main source folder for the UI app
│       │   ├── controller/         # Handles event logic for views
│       │   ├── css/                # Custom .css stylesheets
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
│       ├── package.json            # NPM UI package metadata
│       └── package-lock.json       # NPM UI package dependency lock file
├── backend/                        # Python backend (Flask, LangChain)
│   ├── src/
│   │   ├── api/                    # API endpoints
│   │   ├── ingestion/              # GitHub repo cloning and preparation
│   │   ├── processing/             # File structure + CAP metadata parsing
│   │   ├── rag/                    # LangChain logic and vector store setup
│   │   ├── generation/             # .docx file generation using python-docx
│   │   ├── models/                 # Embedding & LLM initialization
│   │   └── utils/                  # Logging, common utilities
│   ├── manifest.yml                # Backend deployment descriptor
│   ├── requirements.txt            # Python dependencies
│   └── src/api/main.py             # Flask app entrypoint
├── package.json                    # NPM project metadata
├── package-lock.json               # NPM project dependency lock file
```

---

## 💻 Local Development Setup

### 🔧 Prerequisites
- Python 3.9+
- Node.js (for UI5 frontend)
- virtualenvwrapper
- SAP Cloud Foundry CLI (cf)

### 🧠 Python Backend
```bash
workon cap-documentator-env
cd backend
python src/api/main.py
```

### 🌐 UI5 Frontend
```bash
cd app/fiori-ui
npm install
npm start
```

---

## ☁️ Deploying to SAP BTP Cloud Foundry

```bash
cf login -a https://api.cf.<region>.hana.ondemand.com
cd backend
cf push
```

> For MTA-based deployment:

```bash
mbt build
cf deploy mta_archives/CAP-Documentator.mtar
```

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
