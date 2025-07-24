from agent.cloner import RepositoryCloner
from agent.analyzer import CodeAnalyzer
from agent.reporter import ReportGenerator
from config import Config
import argparse
import sys
import os
from pathlib import Path
def print_usage_examples():
    print("\nExamples:")
    print("  python main.py https://github.com/username/repository.git")
    print("  python main.py https://github.com/tensorflow/tensorflow.git")
    print("  python main.py git@github.com:torvalds/linux.git")

def main():
    Config.ensure_dirs_exist()
    
    parser = argparse.ArgumentParser(
        description="DevInsight Agent - GitHub Repository Analyzer",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=print_usage_examples()
    )
    parser.add_argument(
        "repo_url", 
        help="GitHub repository URL to analyze (https or ssh format)"
    )
    
    # If no arguments provided, show help
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    
    args = parser.parse_args()
    
    # Validate URL format
    if not (args.repo_url.startswith('http') or args.repo_url.startswith('git@')):
        print("Error: Repository URL should be in format:")
        print("  https://github.com/username/repo.git")
        print("  git@github.com:username/repo.git")
        sys.exit(1)

    try:
        # Clone the repository
        print(f"Cloning repository: {args.repo_url}")
        cloner = RepositoryCloner(str(Config.REPO_STORAGE))
        repo_path = cloner.clone_repo(args.repo_url)
        
        if not repo_path:
            print("Failed to clone repository.")
            return
        
        # Analyze the repository
        print("Analyzing repository structure...")
        analyzer = CodeAnalyzer(repo_path)
        analysis = analyzer.analyze_repo()
        
        # Generate report
        print("Generating analysis report...")
        with open(Config.ANALYSIS_PROMPT_FILE, 'r') as f:
            prompt = f.read()
        
        reporter = ReportGenerator(Config.MODEL_NAME)
        report = reporter.generate_report(analysis, prompt)
        
        # Save the report
        report_path = Path(repo_path) / "DEVINSIGHT_REPORT.md"
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(report)
        
        print(f"\nAnalysis complete! Report saved to:\n{report_path}")
    
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()