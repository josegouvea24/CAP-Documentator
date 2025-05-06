import os
import tempfile
import git
from pathlib import Path
from collections import defaultdict

IGNORED_DIRS = {"node_modules", ".git", ".vscode", "i18n", "dist"}
IGNORED_FILES = {".gitignore", "package-lock.json", ".env"}

def clone_repo(repo_url):
    temp_dir = tempfile.mkdtemp()
    git.Repo.clone_from(repo_url, temp_dir)
    return temp_dir

def section_files(repo_path):
    repo_path = Path(repo_path)
    files_by_section = defaultdict(lambda: defaultdict(list))
    all_files = []

    for root, dirs, files in os.walk(repo_path):
        # Filter out ignored directories
        dirs[:] = [d for d in dirs if d not in IGNORED_DIRS]
        
        for file in files:
            # Filter out ignored files
            if file in IGNORED_FILES:
                continue
            
            path = Path(root) / file
            rel_path = path.relative_to(repo_path)
            all_files.append(rel_path)

            # Group by top-level folder (CAP convention)
            parts = rel_path.parts
            section = parts[0] if len(parts) > 1 else "root"
            type = path.suffix.lower()
            type = type if type != "" else "other"
            files_by_section[section][path.suffix.lower()].append(rel_path)

    return files_by_section