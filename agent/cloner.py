import os
from git import Repo
from typing import Optional
from pathlib import Path

class RepositoryCloner:
    def __init__(self, base_dir: str = "repos"):
        self.base_dir = Path(base_dir)
        os.makedirs(self.base_dir, exist_ok=True)
    
    def clone_repo(self, repo_url: str) -> Optional[str]:
        """Clone a GitHub repository and return the local path"""
        try:
            repo_name = repo_url.split('/')[-1].replace('.git', '')
            repo_path = self.base_dir / repo_name
            
            if repo_path.exists():
                return str(repo_path)
                
            Repo.clone_from(repo_url, str(repo_path))
            return str(repo_path)
        except Exception as e:
            print(f"Error cloning repository: {e}")
            return None