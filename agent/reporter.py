import ollama
from typing import Dict, Any
import time

class ReportGenerator:
    def __init__(self, model_name: str = "llama3.2:1b"):
        self.model_name = model_name
        self.max_context_size = 3000  # chars
        self.chunk_size = 1000  # chars per chunk

    def generate_report(self, analysis: Dict[str, Any], prompt_template: str) -> str:
        """Optimized reporting with chunking"""
        context = self._prepare_context(analysis)
        prompt = f"{prompt_template}\n\nContext:\n{context[:self.max_context_size]}"
        
        try:
            start_time = time.time()
            print("Generating report (this may take a few minutes)...")
            
            response = ollama.generate(
                model=self.model_name,
                prompt=prompt,
                options={
                    'temperature': 0.7,
                    'num_ctx': 4096  # Larger context window
                },
                stream=False
            )
            
            print(f"Report generated in {time.time()-start_time:.1f} seconds")
            return response['response']
        except Exception as e:
            print(f"Error generating report: {str(e)}")
            return "# Report Generation Failed\n" + str(e)

    def _prepare_context(self, analysis: Dict[str, Any]) -> str:
        """Prepare optimized context for LLM"""
        return (
            f"Repo Structure:\n{analysis['structure']}\n\n"
            f"README:\n{analysis['readme'] or 'None'}\n\n"
            f"Requirements:\n{analysis['requirements'] or 'None'}\n\n"
            f"Code Samples:\n{self._format_code_samples(analysis['main_files'])}\n\n"
            f"Stats:\nFiles: {analysis['stats']['files']}, "
            f"Code Files: {analysis['stats']['code_files']}, "
            f"Size: {analysis['stats']['total_size']/1024/1024:.1f}MB"
        )

    def _format_code_samples(self, samples: Dict[str, str]) -> str:
        """Format code samples efficiently"""
        return '\n'.join(
            f"{path}:\n{content[:500]}{'...' if len(content)>500 else ''}"
            for path, content in samples.items()
        )