import os

# Define the project name and structure
project_name = "TecXMAAI"
directories = [
    f"{project_name}/.github",
    f"{project_name}/.github/workflows",
    f"{project_name}/config",
    f"{project_name}/config/agents",
    f"{project_name}/data",
    f"{project_name}/data/cad_library",
    f"{project_name}/data/materials_db",
    f"{project_name}/data/processed",
    f"{project_name}/data/processed/design_datasets",
    f"{project_name}/data/processed/simulation_datasets",
    f"{project_name}/data/raw",
    f"{project_name}/data/raw/cad_models",
    f"{project_name}/data/raw/simulation_results",
    f"{project_name}/data/samples",
    f"{project_name}/data/evolved_variants",
    f"{project_name}/data/external",
    f"{project_name}/scripts",
    f"{project_name}/docs",
    f"{project_name}/docs/api",
    f"{project_name}/docs/architecture",
    f"{project_name}/docs/installation",
    f"{project_name}/docs/usage",
    f"{project_name}/docs/development",
    f"{project_name}/docs/research",
    f"{project_name}/docs/tutorials",
    f"{project_name}/src",
    f"{project_name}/src/domain",
    f"{project_name}/src/use_cases",
    f"{project_name}/src/repositories",
    f"{project_name}/src/adapters",
    f"{project_name}/src/agents",
    f"{project_name}/src/agents/orchestration_agent",
    f"{project_name}/src/agents/lifecycle_agent",
    f"{project_name}/src/agents/design_agent",
    f"{project_name}/src/agents/simulation_agent",
    f"{project_name}/src/agents/analysis_agent",
    f"{project_name}/src/agents/manufacturing_agent",
    f"{project_name}/src/engines",
    f"{project_name}/src/evolution",
    f"{project_name}/src/core",
    f"{project_name}/src/core/data_processing",
    f"{project_name}/src/core/models",
    f"{project_name}/src/core/models/evolved_models",
    f"{project_name}/src/core/algorithms",
    f"{project_name}/src/core/knowledge_base",
    f"{project_name}/src/integrations",
    f"{project_name}/src/integrations/ai_models",
    f"{project_name}/src/integrations/analysis",
    f"{project_name}/src/integrations/cad_interfaces",
    f"{project_name}/src/integrations/simulation_interfaces",
    f"{project_name}/src/integrations/manufacturing_interfaces",
    f"{project_name}/src/integrations/supply_chain",
    f"{project_name}/src/tools",
    f"{project_name}/src/utils/",
    f"{project_name}/notebooks",
    f"{project_name}/notebooks/experiments",
    f"{project_name}/notebooks/demos",
    f"{project_name}/tests",
    f"{project_name}/tests/agents",
    f"{project_name}/tests/core",
    f"{project_name}/tests/integrations",
    f"{project_name}/tests/modules",
    f"{project_name}/tests/modules/cad",
    f"{project_name}/tests/modules/simulation",
    
]

# File content definitions
files = {
    f"{project_name}/.env": "GEMINI_API_KEY=your_gemini_api_key_here\nTAVILY_API_KEY=your_search_api_key_here\n",
    f"{project_name}/requirements.txt": "google-generativeai\npython-dotenv\nrequests\n",
    f"{project_name}/.github/": "",
    f"{project_name}/.github/workflows/": "",
    f"{project_name}/config/": "",
    f"{project_name}/config/agents/": "",
    f"{project_name}/data/": "",
    f"{project_name}/data/cad_library/": "",
    f"{project_name}/data/materials_db/": "",
    f"{project_name}/data/processed/": "",
    f"{project_name}/data/processed/design_datasets/": "",
    f"{project_name}/data/processed/simulation_datasets/": "",
    f"{project_name}/data/raw/": "",
    f"{project_name}/data/raw/cad_models/": "",
    f"{project_name}/data/raw/simulation_results/": "",
    f"{project_name}/data/samples/": "",
    f"{project_name}/data/evolved_variants/": "",
    f"{project_name}/data/external/": "",
    f"{project_name}/scripts/": "",
    f"{project_name}/docs/": "",
    f"{project_name}/docs/api/": "",
    f"{project_name}/docs/architecture/": "",
    f"{project_name}/docs/installation/": "",
    f"{project_name}/docs/usage/": "",
    f"{project_name}/docs/development/": "",
    f"{project_name}/docs/research/": "",
    f"{project_name}/docs/tutorials/": "",
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
    f"{project_name}/src/": "",
    f"{project_name}/src/domain/": "",
    f"{project_name}/src/use_cases/": "",
    f"{project_name}/src/repositories/": "",
    f"{project_name}/src/adapters/": "",
    f"{project_name}/src/agents/": "",
    f"{project_name}/src/agents/orchestration_agent/": "",
    f"{project_name}/src/agents/lifecycle_agent/": "",
    f"{project_name}/src/agents/design_agent/": "",
    f"{project_name}/src/agents/simulation_agent/": "",
    f"{project_name}/src/agents/analysis_agent/": "",
    f"{project_name}/src/agents/manufacturing_agent/": "",
    f"{project_name}/src/engines/": "",
    f"{project_name}/src/evolution/": "",
    f"{project_name}/src/core/": "",
    f"{project_name}/src/core/data_processing/": "",
    f"{project_name}/src/core/models/": "",
    f"{project_name}/src/core/models/evolved_models/": "",
    f"{project_name}/src/core/algorithms/": "",
    f"{project_name}/src/core/knowledge_base/": "",
    f"{project_name}/src/integrations/": "",
    f"{project_name}/src/integrations/ai_models/": "",
    f"{project_name}/src/integrations/analysis/": "",
    f"{project_name}/src/integrations/cad_interfaces/": "",
    f"{project_name}/src/integrations/simulation_interfaces/": "",
    f"{project_name}/src/integrations/manufacturing_interfaces/": "",
    f"{project_name}/src/integrations/supply_chain/": "",
    f"{project_name}/src/tools/": "",
    f"{project_name}/src/utils//": "",
    f"{project_name}/notebooks/": "",
    f"{project_name}/notebooks/experiments/": "",
    f"{project_name}/notebooks/demos/": "",
    f"{project_name}/tests/": "",
    f"{project_name}/tests/agents/": "",
    f"{project_name}/tests/core/": "",
    f"{project_name}/tests/integrations/": "",
    f"{project_name}/tests/modules/": "",
    f"{project_name}/tests/modules/cad/": "",
    f"{project_name}/tests/modules/simulation/": "",
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