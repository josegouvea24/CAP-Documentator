# 🧠 CAP Documentator – Backend

> Flask + LangChain backend service that ingests SAP CAP projects from GitHub and generates detailed documentation in Word format.

---

## 📌 Overview

This is the **Python-based backend** of the CAP Documentator system. It is designed to:

- Clone a GitHub repository containing a SAP CAP project
- Analyze the file structure, services, and metadata
- Use a LangChain-based pipeline to generate rich documentation
- Export a \`.docx\` file representing the full project description

---

## 📂 Folder Structure

```bash
backend/
├── src/
│   ├── api/             # Flask API endpoints (main app logic)
│   ├── ingestion/       # GitHub repo cloning and preparation
│   ├── processing/      # CAP metadata parsing (planned)
│   ├── rag/             # LangChain vector store and QA pipeline
│   ├── generation/      # Word document generation logic
│   ├── models/          # Embeddings / LLM initialization (planned)
│   └── utils/           # Logging, helpers (planned)
├── requirements.txt     # Python package dependencies
├── manifest.yml         # Cloud Foundry deployment descriptor
├── README.md            # You are here
└── src/api/main.py      # Flask entrypoint
```

---

## 🛠️ Setup (Local Development)

### 🔧 Prerequisites
- Python 3.9+
- \`virtualenvwrapper\` installed (\`pip install virtualenvwrapper\`)
- Git

### 🧪 Initialize environment
```bash
mkvirtualenv cap-documentator-env
workon cap-documentator-env
pip install -r requirements.txt
python src/api/main.py
```

---

## ☁️ Deploy to SAP BTP (Cloud Foundry)

### 🔐 Login
```bash
cf login -a https://api.cf.<region>.hana.ondemand.com
```

### 🚀 Deploy the backend
```bash
cd backend
cf push
```

This uses the included \`manifest.yml\` to deploy the Flask app using the \`python_buildpack\`.

---

## 🔄 API Endpoints

| Method | Path         | Description                             |
|--------|--------------|-----------------------------------------|
| GET    | \`/\`          | Health check / welcome message          |
| POST   | \`/document\`  | Accepts JSON payload with \`repo_url\` and returns \`.docx\` path |

Example POST request:
```json
{
  "repo_url": "https://github.com/org/my-cap-project"
}
```

---

## 📦 Technologies Used

- **Flask** – Lightweight web framework
- **GitPython** – Clone GitHub repositories
- **LangChain** – Retrieval-augmented document generation (planned)
- **python-docx** – Word document generation
- **Cloud Foundry** – Deploy to SAP BTP

---

## 📄 License

This backend module is part of the CAP Documentator project and is licensed under the MIT License.

---
