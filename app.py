import streamlit as st
from agent.cloner import RepositoryCloner
from agent.analyzer import CodeAnalyzer
from agent.reporter import ReportGenerator
from config import Config
import os
from pathlib import Path
import time

# Streamlit app configuration
st.set_page_config(
    page_title="DevInsight Agent",
    page_icon="🔍",
    layout="wide"
)

# Custom CSS for better appearance
st.markdown("""
<style>
    .stProgress > div > div > div > div {
        background-color: #1DA1F2;
    }
    .stTextInput > div > div > input {
        font-family: monospace;
    }
    .report-box {
        border: 1px solid #e1e4e8;
        border-radius: 6px;
        padding: 16px;
        margin-top: 16px;
        background-color: #f6f8fa;
    }
</style>
""", unsafe_allow_html=True)

def main():
    st.title("🔍 DevInsight Agent")
    st.caption("Your Personal GitHub Repository Analyzer")
    
    with st.expander("ℹ️ About this tool"):
        st.markdown("""
        This tool analyzes GitHub repositories to:
        - Identify the technology stack
        - Detect potential issues
        - Suggest improvements
        - Generate comprehensive reports
        
        Works 100% offline using local LLM (LLaMA 3).
        """)
    
    # Repository input
    col1, col2 = st.columns([3, 1])
    with col1:
        repo_url = st.text_input(
            "GitHub Repository URL",
            placeholder="https://github.com/username/repo.git",
            help="Both HTTPS and SSH URLs are supported"
        )
    with col2:
        st.markdown("<br>", unsafe_allow_html=True)
        analyze_btn = st.button("Analyze Repository", type="primary")
    
    if analyze_btn and repo_url:
        if not (repo_url.startswith('http') or repo_url.startswith('git@')):
            st.error("Please enter a valid GitHub repository URL")
            st.stop()
        
        with st.spinner("Initializing analysis..."):
            Config.ensure_dirs_exist()
            
            # Initialize components
            cloner = RepositoryCloner(str(Config.REPO_STORAGE))
            analyzer = CodeAnalyzer("")
            reporter = ReportGenerator(Config.MODEL_NAME)
            
            # Load prompts
            with open(Config.ANALYSIS_PROMPT_FILE, 'r') as f:
                prompt_template = f.read()
        
        # Setup progress container
        progress_bar = st.progress(0)
        status_text = st.empty()
        report_container = st.empty()
        
        try:
            # Clone repository
            status_text.markdown("**Step 1/3:** Cloning repository...")
            progress_bar.progress(20)
            
            repo_path = cloner.clone_repo(repo_url)
            if not repo_path:
                st.error("Failed to clone repository")
                st.stop()
            
            # Analyze repository
            status_text.markdown("**Step 2/3:** Analyzing repository structure...")
            progress_bar.progress(40)
            
            analyzer.repo_path = Path(repo_path)
            analysis = analyzer.analyze_repo()
            
            # Generate report
            status_text.markdown("**Step 3/3:** Generating analysis report...")
            progress_bar.progress(70)
            
            report = reporter.generate_report(analysis, prompt_template)
            progress_bar.progress(100)
            
            # Display results
            status_text.markdown("✅ Analysis complete!")
            time.sleep(0.5)
            progress_bar.empty()
            
            with report_container.container():
                st.markdown("## 📝 Analysis Report")
                st.markdown(f"**Repository:** `{repo_url}`")
                st.markdown(f"**Analyzed on:** {time.strftime('%Y-%m-%d %H:%M:%S')}")
                
                # Report download button
                repo_name = repo_url.split('/')[-1].replace('.git', '')
                st.download_button(
                    label="Download Report",
                    data=report,
                    file_name=f"DEVINSIGHT_{repo_name}.md",
                    mime="text/markdown"
                )
                
                # Display report in expandable sections
                st.markdown('<div class="report-box">', unsafe_allow_html=True)
                st.markdown(report, unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)
                
        except Exception as e:
            progress_bar.empty()
            status_text.error(f"Analysis failed: {str(e)}")
            st.exception(e)

if __name__ == "__main__":
    main()