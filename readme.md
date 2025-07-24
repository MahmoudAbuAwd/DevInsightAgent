# DevInsight Agent

A Python-based tool for analyzing GitHub repositories using local LLM models. Provides insights into code quality, tech stack detection, and generates improvement suggestions.

## Features

- **Repository Analysis**: Clone and analyze any public GitHub repository
- **Code Quality Assessment**: Identify potential issues and code smells
- **Technology Detection**: Automatically detect programming languages and frameworks
- **Documentation Generation**: Create structured analysis reports
- **Local Processing**: Works entirely offline using Ollama

## Requirements

- Python 3.8 or higher
- Git installed on your system
- Ollama for local LLM inference

## Installation

1. **Install Ollama** (if not already installed):
   ```bash
   curl -fsSL https://ollama.ai/install.sh | sh
   ```

2. **Pull the required model**:
   ```bash
   ollama pull llama3.2:1b
   ```

3. **Clone this repository**:
   ```bash
   git clone https://github.com/yourusername/DevInsightAgent.git
   cd DevInsightAgent
   ```

4. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Command Line Interface

```bash
python analyze.py <repository-url>
```

Example:
```bash
python analyze.py https://github.com/user/sample-project.git
```

### Web Interface (Optional)

If you prefer a web interface:

```bash
streamlit run app.py
```

Then navigate to `http://localhost:8501` in your browser.

## Configuration

Edit `config.py` to customize analysis parameters:

```python
# Model settings
OLLAMA_MODEL = "llama3.2:1b"
MAX_FILE_SIZE = 1024 * 1024  # 1MB
SUPPORTED_EXTENSIONS = ['.py', '.js', '.java', '.cpp', '.c', '.go']

# Analysis settings
IGNORE_DIRS = ['node_modules', '.git', '__pycache__', 'venv']
MAX_FILES_TO_ANALYZE = 100
```

## Project Structure

```
devinsight-agent/
├── src/
│   ├── analyzer.py          # Core analysis logic
│   ├── repo_handler.py      # Repository cloning and management
│   ├── llm_client.py        # Ollama integration
│   └── report_generator.py  # Report creation
├── templates/
│   └── analysis_prompts.py  # LLM prompt templates
├── config.py                # Configuration settings
├── analyze.py               # Main CLI script
├── app.py                   # Streamlit web interface
├── requirements.txt
└── README.md
```

## Sample Output

```
=== Repository Analysis Report ===

Repository: sample-project
Analyzed: 23 files
Languages detected: Python (85%), JavaScript (15%)

Key Findings:
• Found 2 potential security issues
• 5 functions missing documentation
• Code complexity score: 6.2/10
• Detected frameworks: Flask, React

Recommendations:
1. Add input validation in user_controller.py (line 45)
2. Consider breaking down large functions in data_processor.py
3. Add unit tests for core functionality
4. Update dependencies (3 outdated packages found)

Analysis completed in 34 seconds.
```

## Limitations

- Currently supports repositories up to 50MB
- Analysis quality depends on the LLM model used
- Some complex codebases may require manual review of suggestions
- Limited support for proprietary or domain-specific languages

## Dependencies

```
streamlit>=1.28.0
GitPython>=3.1.0
requests>=2.31.0
python-dotenv>=1.0.0
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Troubleshooting

**Issue**: "Model not found" error
**Solution**: Make sure you've pulled the required model with `ollama pull llama3.2:1b`

**Issue**: Out of memory errors
**Solution**: Reduce `MAX_FILES_TO_ANALYZE` in config.py or use a smaller model

**Issue**: Repository cloning fails
**Solution**: Check your internet connection and ensure the repository URL is correct

## Acknowledgments

- Uses Ollama for local LLM inference
- Built with Streamlit for the web interface
- Inspired by various code analysis tools in the open source community


