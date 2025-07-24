import os
from pathlib import Path

class Config:
    # Repository settings
    REPO_STORAGE = Path("repos")
    
    # Model settings
    MODEL_NAME = "llama3.2:1b"
    
    # Prompt settings
    PROMPT_DIR = Path("prompt")
    SYSTEM_PROMPT_FILE = PROMPT_DIR / "system_prompt.txt"
    ANALYSIS_PROMPT_FILE = PROMPT_DIR / "prompt.txt"
    
    @classmethod
    def ensure_dirs_exist(cls):
        """Ensure all required directories exist"""
        os.makedirs(cls.REPO_STORAGE, exist_ok=True)
        os.makedirs(cls.PROMPT_DIR, exist_ok=True)