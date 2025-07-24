# 🚀 DevInsight Agent - GitHub Repository Analyzer

![Project Banner](https://github.com/yourusername/DevInsight-Agent/raw/main/assets/banner.gif)

<div align="center">
  
[![GitHub Stars](https://img.shields.io/github/stars/yourusername/DevInsight-Agent?style=for-the-badge&logo=github)](https://github.com/yourusername/DevInsight-Agent/stargazers)
[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

</div>

## 🌟 Features

<div align="center">
  
```mermaid
pie
    title Key Features
    "Code Analysis" : 35
    "Tech Stack Detection" : 25
    "Documentation Review" : 20
    "Improvement Suggestions" : 20
```

</div>

- 🔍 **Deep Code Analysis** with LLaMA 3.2:1b
- 📊 **Technology Stack Visualization**
- 🐛 **Bug & Smell Detection**
- 📝 **Auto-Generated Documentation**
- 🚀 **Performance Optimization Tips**
- 💻 **100% Offline Operation**

## 🛠️ Tech Stack

<div align="center">
  
| Component        | Technology                          |
|------------------|-------------------------------------|
| **LLM Engine**   | LLaMA 3.2:1b (Local)               |
| **Backend**      | Python 3.8+                        |
| **Web Interface**| Streamlit                          |
| **Repo Handling**| GitPython                          |
| **Visualization**| Mermaid.js, Plotly                 |

</div>

## 🎯 Quick Start

### Prerequisites
```bash
curl -fsSL https://ollama.com/install.sh | sh
ollama pull llama3:2b  # LLaMA 3.2:1b variant
```

### Installation
```bash
git clone https://github.com/yourusername/DevInsight-Agent.git
cd DevInsight-Agent
pip install -r requirements.txt
```

### Usage
#### CLI Version
```bash
python main.py https://github.com/username/repository.git
```

#### Web Interface
```bash
streamlit run app.py
```

![Interface Demo](https://github.com/yourusername/DevInsight-Agent/raw/main/assets/interface-demo.gif)

## 📊 Sample Report Output

```markdown
# DevInsight Analysis Report

## 🔍 Repository Overview
**Project**: WriteWiseAI  
**Analysis Date**: 2023-11-15  
**Total Files**: 142  
**Code Files**: 87  

## 🧩 Technology Stack
```mermaid
graph TD
    A[Python] --> B[Flask]
    A --> C[Pandas]
    A --> D[NLTK]
    B --> E[API Endpoints]
```

## 🚨 Potential Issues
1. **Security**: Found 3 hardcoded API keys
2. **Performance**: Unoptimized database queries in `data_processor.py`
3. **Documentation**: 62% of functions lack docstrings

## 💡 Recommendations
✅ Implement environment variables for configuration  
✅ Add pagination to large database queries  
✅ Write unit tests for core modules  
```

## 🏗️ Project Structure

```bash
.
├── agent/                # Core analysis modules
│   ├── cloner.py         # Repository cloning
│   ├── analyzer.py       # Code analysis engine
│   └── reporter.py       # Report generation
├── prompts/              # LLM prompt templates
├── app.py                # Streamlit web interface
├── main.py               # CLI interface
├── config.py             # Configuration settings
└── Requirements.txt
   ```

## 📜 License
MIT © 2023 [Your Name]

---

<div align="center">
  
[![Buy Me A Coffee](https://img.shields.io/badge/Buy_Me_A_Coffee-FFDD00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/yourusername)
[![Twitter Follow](https://img.shields.io/badge/Follow-%40yourhandle-1DA1F2?style=for-the-badge&logo=twitter)](https://twitter.com/yourhandle)

</div>
