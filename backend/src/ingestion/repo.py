import os
from git import Repo
import shutil

def clone_and_prepare(repo_url: str, clone_dir="tmp_project") -> str:
    if os.path.exists(clone_dir):
        shutil.rmtree(clone_dir)
    Repo.clone_from(repo_url, clone_dir)
    return clone_dir
