import os

# Define the project name and structure
project_name = "gemini_deep_research"
directories = [
    f"{project_name}/src",
    f"{project_name}/data",
]

# File content definitions
files = {
    f"{project_name}/.env": "GEMINI_API_KEY=your_gemini_api_key_here\nTAVILY_API_KEY=your_search_api_key_here\n",
    f"{project_name}/requirements.txt": "google-generativeai\npython-dotenv\nrequests\n",
    f"{project_name}/src/agent.py": """import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

class DeepResearchAgent:
    def __init__(self, model_name="gemini-2.0-flash-exp"):
        self.model = genai.GenerativeModel(model_name)

    def plan_research(self, topic):
        prompt = f"Break down the following research topic into 3-5 specific search queries: {topic}"
        response = self.model.generate_content(prompt)
        return response.text

    def synthesize_report(self, findings):
        prompt = f"Based on these findings, write a comprehensive report with citations: {findings}"
        response = self.model.generate_content(prompt)
        return response.text
""",
    f"{project_name}/main.py": """from src.agent import DeepResearchAgent

def main():
    topic = input("Enter research topic: ")
    agent = DeepResearchAgent()
    
    print("\\n--- Planning Research ---")
    plan = agent.plan_research(topic)
    print(plan)
    
    # In a full implementation, you would execute searches here.
    print("\\n--- Generating Mock Report ---")
    report = agent.synthesize_report("Simulated findings based on the plan.")
    print(report)

if __name__ == "__main__":
    main()
"""
}

# Create directories and files
def create_repo():
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
    
    for file_path, content in files.items():
        with open(file_path, "w") as f:
            f.write(content)
    
    print(f"Successfully created repository structure in ./{project_name}")

if __name__ == "__main__":
    create_repo()
