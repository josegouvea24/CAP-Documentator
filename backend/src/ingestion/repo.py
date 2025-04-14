import os
import tempfile
import git  # GitPython

IRRELEVANT_FILES = [
    "/webapp",
    "/app",
    "/node_modules",
    ".gitignore",
    "package-lock.json",
    "/i18n",
    ".vscode",
    ".env"
]

def clone_and_prepare(repo_url):
    temp_dir = tempfile.mkdtemp()
    git.Repo.clone_from(repo_url, temp_dir)
    return temp_dir

def collect_all_files(project_path, irrelevant_files=IRRELEVANT_FILES):
    relevant_files = []
    
    for root, dirs, files in os.walk(project_path):
        for file in files:
                abs_path = os.path.join(root, file)
                rel_path = os.path.relpath(abs_path, project_path)
            
                relevant_files.append({
                    "name": file,
                    "full_path": abs_path,
                    "rel_path": rel_path,
                    "format": file.split(".")[-1] if "." in file else None,
                    "is_relevant": not any(exclude in rel_path for exclude in irrelevant_files),    
                })

                print(f"Collected file: {file} from {rel_path}")

    return relevant_files