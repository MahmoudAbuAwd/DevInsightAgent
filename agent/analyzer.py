import os
from pathlib import Path
from typing import Dict, Any, Optional
import fnmatch

class CodeAnalyzer:
    def __init__(self, repo_path: str):
        self.repo_path = Path(repo_path)
        self.ignore_dirs = {'.git', '__pycache__', 'node_modules', 'venv'}
        self.ignore_files = {'*.pyc', '*.o', '*.so', '*.dll'}
        self.max_file_size = 1 * 1024 * 1024  # 1MB
        self.sample_size = 2000  # chars to sample from each file

    def analyze_repo(self) -> Dict[str, Any]:
        """Optimized repository analysis"""
        return {
            "structure": self._get_repo_structure(),
            "readme": self._find_file_content('README*'),
            "requirements": self._find_file_content('requirements*'),
            "main_files": self._sample_code_files(),
            "stats": self._get_repo_stats()
        }

    def _should_ignore(self, path: Path) -> bool:
        """Check if path should be ignored"""
        if any(part.startswith('.') for part in path.parts):
            return True
        if any(part in self.ignore_dirs for part in path.parts):
            return True
        if any(fnmatch.fnmatch(path.name, pattern) for pattern in self.ignore_files):
            return True
        return False

    def _get_repo_structure(self) -> list:
        """Fast directory scanning with ignores"""
        structure = []
        for root, dirs, files in os.walk(self.repo_path):
            dirs[:] = [d for d in dirs if not self._should_ignore(Path(root)/d)]
            files = [f for f in files if not self._should_ignore(Path(root)/f)]
            
            level = root.replace(str(self.repo_path), '').count(os.sep)
            indent = ' ' * 4 * (level)
            structure.append(f"{indent}{os.path.basename(root)}/")
            structure.extend(f"{indent}    {f}" for f in files)
        return structure[:1000]  # Limit output

    def _find_file_content(self, pattern: str) -> Optional[str]:
        """Find first matching file and return sample"""
        for f in self.repo_path.rglob(pattern):
            if not self._should_ignore(f) and f.is_file():
                try:
                    return self._safe_read_file(f)
                except:
                    continue
        return None

    def _sample_code_files(self) -> Dict[str, str]:
        """Sample relevant code files"""
        code_extensions = {'.py', '.js', '.java', '.go', '.rs', '.ts'}
        samples = {}
        
        for ext in code_extensions:
            for f in self.repo_path.rglob(f'*{ext}'):
                if not self._should_ignore(f) and f.is_file():
                    try:
                        samples[str(f.relative_to(self.repo_path))] = self._safe_read_file(f)
                        if len(samples) >= 20:  # Limit to 20 files
                            return samples
                    except:
                        continue
        return samples

    def _safe_read_file(self, filepath: Path) -> str:
        """Safe file reading with size limits"""
        if filepath.stat().st_size > self.max_file_size:
            return f"[Large file truncated] {filepath.name}"
        
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            return f.read(self.sample_size)

    def _get_repo_stats(self) -> Dict[str, int]:
        """Get basic repository statistics"""
        stats = {'files': 0, 'code_files': 0, 'total_size': 0}
        for root, _, files in os.walk(self.repo_path):
            if self._should_ignore(Path(root)):
                continue
            for f in files:
                filepath = Path(root)/f
                if not self._should_ignore(filepath):
                    stats['files'] += 1
                    stats['total_size'] += filepath.stat().st_size
                    if filepath.suffix in {'.py', '.js', '.java', '.go', '.rs', '.ts'}:
                        stats['code_files'] += 1
        return stats