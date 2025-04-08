import os
import tempfile
import git  # GitPython

def clone_and_prepare(repo_url):
    temp_dir = tempfile.mkdtemp()
    git.Repo.clone_from(repo_url, temp_dir)
    return temp_dir


def extract_readme(path):
    candidates = ["README.md", "readme.md", "README.MD"]
    for name in candidates:
        readme_path = os.path.join(path, name)
        if os.path.exists(readme_path):
            with open(readme_path, "r", encoding="utf-8") as f:
                return f.read()
    return None