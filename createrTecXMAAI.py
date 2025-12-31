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
    f"{project_name}/agent.py": "'
    f"{project_name}/docker-compose.yml": "# For orchestrating multi-container Docker applications",
    f"{project_name}/Dockerfile": "# For containerized deployment # For containerizing the application",
    f"{project_name}/.env": "GEMINI_API_KEY=your_gemini_api_key_here\nTAVILY_API_KEY=your_search_api_key_here\n",
    f"{project_name}/.env.template": "#                           <-- [ADD] For OPENAI_API_KEY & GOOGLE_API_KEY",
    f"{project_name}/.gitignore": "# Standard Python and large data exclusions # Files and directories to ignore by Git",
    #f"{project_name}/LICENSE": "# Project license (e.g., MIT, Apache 2.0)",
    f"{project_name}/pyproject.toml": "# Modern dependency management",
    f"{project_name}/README.md": "# TecXMAAI\nTecX Mechanical Agentic AI\n# Project overview and lifecycle goals, Documentation of the self-evolving PLM system\n

```

TecX-plm-agent-system/
├── .github/                # CI/CD workflows for testing agents,  # GitHub-specific configurations
|   ├── workflows/          # Automated testing (CI/CD) and security scans, # CI/CD pipelines (GitHub Actions)
│   │   ├── ci.yml          # Continuous Integration pipeline
│   │   ├── cd.yml          # Continuous Deployment pipeline (optional)
│   │   └── linting.yml     # Code linting and formatting checks
│   ├── ISSUE_TEMPLATE.md   # Template for bug reports and feature requests
│   └── PULL_REQUEST_TEMPLATE.md # Template for pull requests
│
├── config/                 # YAML/JSON configs for models & GA params
│   ├── agents/
│   │   ├── analysis_agent.yaml
│   │   ├── main_config.yaml
│   │   ├── manufacturing_agent.yaml
│   │   └── simulation_agent.yaml
│   ├── agents.yaml         # Configuration for OpenAI and Google model roles
│   ├── evolution.yaml      # Genetic Algorithm parameters (mutation rate, etc.)
│   └── lifecycle.yaml      # PLM specific constraints (ISO standards)
├── data/                   # Raw scans and CAD specs (gitignored) # raw/ and
│   │                         processed/  engineering data # Datasets (consider large file
│   │                         storage like Git LFS or external services)
│   ├── cad_library/        # Versioned .STEP/.STL files
│   ├── materials_db/       # CSV/JSON material properties
│   ├── processed/          # Processed engineering data # Cleaned, transformed, and ready-to-use data
│   │   ├── design_datasets/
│   │   └── simulation_datasets/
│   ├── raw/                # Raw engineering data # Original, unprocessed data
│   │   ├── cad_models/
│   │   └── simulation_results/
│   ├── samples/                  <-- [ADD] Dataset for fiber strength/images
│   ├── evolved_variants/              <-- [ADD] Storage for generated model weights
│   ├── external/           # Data from external sources
│   └── README.md           # README explaining data structure and licensing
│
├── scripts/                # Helper scripts for common tasks
│   ├── download_data.sh    # Script to download datasets
│   ├── generate_cad.py
│   ├── train_model.py      # Script to launch model training
│   ├── run_simulation.py   # Script to trigger a simulation via agent
│   ├── run_evolution.py               <-- [ADD] Start the Genetic Algorithm loop
│   └── README.md           # README for the scripts directory
├── .env.template                      <-- [ADD] For OPENAI_API_KEY & GOOGLE_API_KEY
├── docs/                   # Technical documentation for PLM workflows, spec.md, design decisions, and manuals,
│   │                       Engineering specs & Life Cycle maps # Keep your Documentation structure,
│   │                       # Documentation for the project
│   ├── spec.md
│   ├──api/                  # API documentation (if applicable)
│   │   ├──index.md
│   │   └──README.md
│   ├──architecture/
│   │   ├── agent_interaction_diagram.svg
│   │   ├── data_flow_diagram.svg
│   │   ├── module_dependencies.md
│   │   └── overall_architecture.md             
│   ├── architecture.md     # High-level architecture overview (this document!)
│   ├── installation/       # Installation and setup guides
│   │   ├── index.md
│   │   └── requirements.md # Software/hardware prerequisites
│   ├── usage/              # User guides and tutorials
│   │   ├── index.md
│   │   ├── design_automation.md
│   │   ├── simulation_automation.md
│   │   └── manufacturing_automation.md
│   ├── development/        # Guides for contributors
│   │   ├── index.md
│   │   ├── contributing.md # How to contribute
│   │   ├── testing.md      # How to run and write tests
│   │   └── coding_standards.md
│   ├── research/           # Papers, surveys, or internal research notes
│   │   └── index.md
│   └── tutorials
│   │   ├── configuring_your_environment.md
│   │   ├── first_design_agent_run.md
│   │   └── getting_started.md
│   └── README.md           # Main README for the docs directory
│
├── src/                    # Primary source code
│   ├── domain/             # UNIT 1: Pure Engineering Rules # Pure physics and engineering models
│   │   ├── physics.py      # Stress/Strain formulas
│   │   └── materials.py    # Material entity definitions
│   ├── use_cases/          # Lifecyle workflows (e.g. design_validation.py)
│   │   └── design_validation.py
│   ├── repositories/       # Repository interfaces and implementations # UNIT 2: The Data Gate (Interfaces)
│   │   ├── base_repo.py    # ABC for data access
│   │   └── cad_repo.py     # ABC for CAD file management
│   ├── adapters/           # UNIT 3: External Tool Connections
│   │   ├── cad/            # SolidWorks/FreeCAD specific code
│   │   ├── llm/            # LangChain/AI agent logic
│   │   └── database/       # PostgreSQL/SQLAlchemy logic
│   ├── agents/             # UNIT 4: Orchestration # AI reasoning and tool-calling logic, Role-based agent
│   │   │                       definition, # Individual AI agent modules,  # MULTIMODAL AGENT ORCHESTRATION
│   │   ├── __init__.py
│   │   ├── base_agent.py   # Abstract base class for all agents
│   │   ├── orchestration_agent/      # Agent responsible for coordinating others
│   │   │   ├── __init__.py
│   │   │   ├── workflow_manager.py
│   │   │   └── multimodal_bridge.py   <-- [ADD] Logic to swap GPT-4o (OpenAI) & Gemini (Google)
│   │   └── lifecycle_agent/      <-- [ADD] Specific Agent for Mechanical Properties
│   │   │   ├── fiber_analysis.py      # Microscopic image analysis (Multimodal)
│   │   │   └── sustainability_lca.py  # Life cycle/degradability tracking (Biodegradability, corrosion, etc.)
│   │   ├── design_agent/
│   │   │   ├── __init__.py
│   │   │   ├── concept_exploration.py
│   │   │   ├── concept_generation.py
│   │   │   ├── generative_design.py
│   │   │   ├── feature_recognition.py
│   │   │   ├── parametric_modeling.py
│   │   │   ├──  optimization.py
│   │   │   ├── design_optimization.py
│   │   │   └── knowledge-based_design.py
│   │   ├── simulation_agent/
│   │   │   ├── __init__.py
│   │   │   ├── meshing_automation.py
│   │   │   ├── solver_setup.py
│   │   │   └── reduced_order_modeling.py
│   │   ├── analysis_agent/
│   │   │   ├── __init__.py
│   │   │   ├── result_interpretation.py
│   │   │   └── validation.py
│   │   ├── manufacturing_agent/
│   │   │   ├── __init__.py
│   │   │   ├── process_selection.py
│   │   │   ├── cam_toolpath.py
│   │   │   └── quality_control.py
│   │   ├── design_agent.py # The AI "Mechanical Agent" loop # Uses for 3D generative CAD
│   │   ├──analysis_agent.py
│   │   ├──manufacturing_agent.py
│   │   ├──simulation_agent.py
│   │   ├──orchestration_agent.py
│   │   ├──lifecycle_agent.py
│   │   ├──orchestration_agent
│   │   ├── inspector.py    # Uses Google Gemini for vision/video QA
│   │   ├── supervisor.py   # Multi-agent orchestrator, LangGraph/CrewAI orchestrator to manage handoffs
│   │   │                   # MULTIMODAL AGENT ORCHESTRATION
│   │   ├── openai_agent.py # Handles high-level design reasoning (GPT-4o)
│   │   └── google_agent.py # Handles vision/video inspection (Gemini 2.5)
│   ├── engines/            # CORE COMPUTATIONAL MODELS
│   │   ├── generative.py   # Generative algorithms for 3D structures
│   │   └── deep_learning.py# Deep learning for predictive maintenance
│   │
│   ├── evolution/          # Genetic Algorithm engine, <-- [ADD] THE SELF-GENERATION ENGINE # THE NEUROEVOLUTION ENGINE
│   │   ├── __init__.py
│   │   ├── crossover.py    # Logic for merging model architectures # Logic for merging neural network "genomes"
│   │   ├── fitness.py      # PLM-specific evaluation metrics
│   │   ├── mutation.py     # Hyperparameter and layer mutations, # Handles stochastic layer/param changes
│   │   │── population.py   # Manages generations of neural networks
│   │   ├── genome_handler.py # Encodes Neural Net layers as "Genes"
│   │   ├── crossover_mutation.py      # Genetic Algorithm operators
│   │   ├── fitness_evaluator.py       # Tests evolved models against Wool data
│   │   ├── fitness_engine.py   # Evaluates models on wool mechanical properties
│   │   └── model_generator.py         # AUTO-WRITES NEW PYTHON MODEL CODE,  # SCRIPT TO GENERATE NEW NEURAL NETWORKS 
│   │
│   ├── core/               # Core utilities, data structures, and algorithms
│   │   ├── __init__.py
│   │   ├── data_processing/
│   │   │   ├── __init__.py
│   │   │   ├── geometry_utils.py
│   │   │   └── simulation_data_parser.py             
│   │   ├── models/           # Pre-trained and evolved model classes, Pre-trained or base model architectures
│   │   │   ├── __init__.py
│   │   │   ├── generative_models.py # e.g., GANs, VAEs
│   │   │   └── surrogate_models.py
│   │   │   ├── base_architectures.py
│   │   │   ├── base_network.py # Blueprint for deep learning models
│   │   │   │── multimodal.py   # Fusion logic for text/image/audio inputs
│   │   │   └── evolved_models/        <-- [ADD] Destination for GA-generated models
│   │   ├── algorithms/     # General algorithms used across agents
│   │   │   ├── __init__.py
│   │   │   └── optimization_algorithms.py
│   │   └── knowledge_base/ # Interfaces for accessing engineering knowledge
│   │       ├── __init__.py
│   │       ├── design_rules.py
│   │       ├── material_database.py   # Add Grade/Micron data here
│   │       └── physics_rules.py <-- [ADD] Mechanical rules
│   │
│   ├── integrations/       # Code for interacting with external tools/APIs, # Keep your SolidWorks/Ansys APIs
│   │   ├── __init__.py
│   │   ├── ai_models/
│   │   │   ├─ __init__.py
│   │   │   ├─ generative_design.py
│   │   │   └─ reinforcement_learning.py
│   │   ├─ analysis/
│   │   │   ├─ __init__.py
│   │   │   ├─ cf_analyzer.py
│   │   │   └─ fe_analyzer.py
│   │   ├── cad_interfaces/
│   │   │   ├─ __init__.py
│   │   │   ├─ cad_interface.py
│   │   │   ├─ solidworks_api.py
│   │   │   └─ fusion360_api.py
│   │   ├── simulation_interfaces/
│   │   │   ├─ __init__.py
│   │   │   ├─ abaqus.py
│   │   │   ├─ ansys_api.py
│   │   │   ├─ sim_interface.py
│   │   │   └─ comsol_api.py
│   │   ├── manufacturing_interfaces/
│   │   │    ├─ __init__.py
│   │   │    ├─ cam_interface.py
│   │   │    ├─ robot_control.py
│   │   │    └─ cnc_controller_api.py      
│   │   └── supply_chain/         <-- [ADD] API for sourcing/farming data
│   │   │   ├── __init__.py
│   │   │   └──
│   ├── tools/              # Specialized mechanical engineering tools,    # MECHANICAL ENGINEERING UTILITIES
│   │   ├── cad_exporter.py # Export to STEP/STL for wool-composite parts
│   │   ├── lca_analyzer.py # Life Cycle Assessment for sustainability
│   │   ├── lca_calc.py     # Sustainability/LCA reporting tools
│   │   └── simulation.py   # Physics-based simulation wrappers
│   ├── utils/            # Helper(General utility) functions for API and data handling, not specific to agents
│   │   ├── __init__.py
│   │   ├── logging_config.py
│   │   └── config_loader.py
│   └── main.py             # Entry point for running the AI system (often a FastAPI app), (Triggers either
│                             Agent mode or Evolution mode)
├── notebooks/              # Keep for experimentation # Jupyter notebooks for experimentation and demos
│   ├── experiments/        # Notebooks for testing specific algorithms/models
│   │   ├── design_exploration.ipynb
│   │   └── simulation_surrogate.ipynb
│   ├── demos/              # Notebooks demonstrating agent capabilities
│   │   ├── design_to_sim_workflow.ipynb
│   │   └── manufacturing_planning_demo.ipynb
│   ├──data_exploration.ipynb
│   └── README.md           # README for the notebooks directory
│
├── tests/                  # Unit tests for agents and GA logic # Keep for quality control # integration tests
│   ├── __init__.py
│   ├── agents/
│   │   ├── test_design_agent.py
│   │   └── test_simulation_agent.py
│   ├── core/
│   │   ├──__init__.py
│   │   ├──test_config.py
│   │   ├──test_data_manager.py
│   │   ├── test_data_processing.py
│   │   └── test_models.py
│   ├── integrations/
│   │   └── test_cad_interface.py
│   └── modules
│       ├──__init__.py
│       ├──cad
│       │   ├──__init__.py
│       │   └──test_solidworks.py
│       └──simulation
│           ├──__init__.py
│           └──test_ansys.py
│  
├── .gitignore              # Standard Python and large data exclusions # Files and directories to ignore by Git
├── pyproject.toml          # Modern dependency management
├── requirements.txt        # Python dependencies for general use # Legacy dependency list (PyTorch, LangChain, torch, langchain-google-genai, openai, pygad)
├── requirements_dev.txt    # Python dependencies for development (linters, testers, etc.)
├── requirements_gpu.txt    # Python dependencies if GPU support is required
├── Dockerfile              # For containerized deployment # For containerizing the application
├── docker-compose.yml      # For orchestrating multi-container Docker applications
├── LICENSE                 # Project license (e.g., MIT, Apache 2.0) 
├── README.md               # Project overview and lifecycle goals, Documentation of the self-evolving PLM system
└── setup.py   

```",
    f"{project_name}/requirements.txt": "google-generativeai\npython-dotenv\nrequests\nPyTorch\nLangChain\ntorch\nlangchain-google-genai\nopenai\npygad # Python dependencies for general use",
    f"{project_name}/requirements_dev.txt": "# Python dependencies for development (linters, testers, etc.)",
    f"{project_name}/requirements_gpu.txt": "# Python dependencies if GPU support is required",
    f"{project_name}/setup.py": "",
    #f"{project_name}/.github/": "# CI/CD workflows for testing agents,  # GitHub-specific configurations",
    f"{project_name}/.github/ISSUE_TEMPLATE.md": "# Template for bug reports and feature requests",
    f"{project_name}/.github/PULL_REQUEST_TEMPLATE.md": "# Template for pull requests",
    #f"{project_name}/.github/workflows/": "# Automated testing (CI/CD) and security scans, # CI/CD pipelines (GitHub Actions)",
    f"{project_name}/.github/workflows/ci.yml": "# Continuous Integration pipeline",
    f"{project_name}/.github/workflows/cd.yml": "# Continuous Deployment pipeline (optional)",
    f"{project_name}/.github/workflows/linting.yml": "# Code linting and formatting checks",
    #f"{project_name}/config/": "# YAML/JSON configs for models & GA params",
    f"{project_name}/config/agents.yaml": "# Configuration for OpenAI and Google model roles",
    f"{project_name}/config/evolution.yaml": "# Genetic Algorithm parameters (mutation rate, etc.)",
    f"{project_name}/config/lifecycle.yaml": "# PLM specific constraints (ISO standards)",
    #f"{project_name}/config/agents/": "",
    f"{project_name}/config/agents/analysis_agent.yaml": "",
    f"{project_name}/config/agents/main_config.yaml": "",
    f"{project_name}/config/agents/manufacturing_agent.yaml": "",
    f"{project_name}/config/agents/simulation_agent.yaml": "",
    #f"{project_name}/data/": "",
    f"{project_name}/data/README.md": "# README explaining data structure and licensing",
    #f"{project_name}/data/cad_library/": "",
    #f"{project_name}/data/materials_db/": "",
    #f"{project_name}/data/processed/": "",
    #f"{project_name}/data/processed/design_datasets/": "",
    #f"{project_name}/data/processed/simulation_datasets/": "",
    #f"{project_name}/data/raw/": "",
    #f"{project_name}/data/raw/cad_models/": "",
    #f"{project_name}/data/raw/simulation_results/": "",
    #f"{project_name}/data/samples/": "",
    #f"{project_name}/data/evolved_variants/": "",
    #f"{project_name}/data/external/": "",
    #f"{project_name}/scripts/": "# Helper scripts for common tasks",
    f"{project_name}/scripts/download_data.sh": "# Script to download datasets",
    f"{project_name}/scripts/generate_cad.py": "",
    f"{project_name}/scripts/train_model.py": "# Script to launch model training",
    f"{project_name}/scripts/run_simulation.py": "# Script to trigger a simulation via agent",
    f"{project_name}/scripts/ run_evolution.py": " #          <-- [ADD] Start the Genetic Algorithm loop",
    f"{project_name}/scripts/README.md": "# README for the scripts directory",
    #f"{project_name}/docs/": "# Technical documentation for PLM workflows, spec.md, design decisions, and manuals, Engineering specs & Life Cycle maps # Keep your Documentation structure, # Documentation for the project",
    f"{project_name}/docs/spec.md": "",
    f"{project_name}/docs/architecture.md": "# High-level architecture overview (this document!)",
    f"{project_name}/docs/ README.md": " # Main README for the docs directory",
    #f"{project_name}/docs/api/": "# API documentation (if applicable)",
    f"{project_name}/docs/api/index.md": "",
    f"{project_name}/docs/api/README.md": "",
    #f"{project_name}/docs/architecture/": "",
    f"{project_name}/docs/architecture/agent_interaction_diagram.svg": "",
    f"{project_name}/docs/architecture/data_flow_diagram.svg": "",
    f"{project_name}/docs/architecture/module_dependencies.md": "",
    f"{project_name}/docs/architecture/overall_architecture.md": "",
    #f"{project_name}/docs/installation/": " # Installation and setup guides",
    f"{project_name}/docs/installation/index.md": "",
    f"{project_name}/docs/installation/requirements.md": "# Software/hardware prerequisites",
    #f"{project_name}/docs/usage/": "# User guides and tutorials",
    f"{project_name}/docs/usage/index.md": "",
    f"{project_name}/docs/usage/design_automation.md": "",
    f"{project_name}/docs/usage/simulation_automation.md": "",
    f"{project_name}/docs/usage/manufacturing_automation.md": "",
    #f"{project_name}/docs/development/": "# Guides for contributors",
    f"{project_name}/docs/development/index.md": "",
    f"{project_name}/docs/development/contributing.md": "# How to contribute",
    f"{project_name}/docs/development/testing.md": "# How to run and write tests",
    f"{project_name}/docs/development/coding_standards.md": "",
    f"{project_name}/docs/research/": "# Papers, surveys, or internal research notes",
    f"{project_name}/docs/research/index.md": "",
    #f"{project_name}/docs/tutorials/": "",
    f"{project_name}/docs/tutorials/configuring_your_environment.md": "",
    f"{project_name}/docs/tutorials/first_design_agent_run.md": "",
    f"{project_name}/docs/tutorials/getting_started.md": "",
    #f"{project_name}/src/": " # Primary source code",
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
    f"{project_name}/src/main.py": " # Entry point for running the AI system (often a FastAPI app), (Triggers either Agent mode or Evolution mode)",
    f"{project_name}/src/domain/": "",
    f"{project_name}/src/domain/": "",
    f"{project_name}/src/domain/": "",
    f"{project_name}/src/use_cases/": "",
    f"{project_name}/src/use_cases/": "",
    f"{project_name}/src/repositories/": "",
    f"{project_name}/src/repositories/": "",
    f"{project_name}/src/repositories/": "",
    f"{project_name}/src/adapters/": "",
    f"{project_name}/src/adapters/": "",
    f"{project_name}/src/adapters/": "",
    f"{project_name}/src/adapters/": "",
    #f"{project_name}/src/agents/": "",
    f"{project_name}/src/agents/": "",
    f"{project_name}/src/agents/": "",
    f"{project_name}/src/agents/": "",
    f"{project_name}/src/agents/": "",
    f"{project_name}/src/agents/": "",
    f"{project_name}/src/agents/": "",
    f"{project_name}/src/agents/": "",
    f"{project_name}/src/agents/": "",
    f"{project_name}/src/agents/": "",
    f"{project_name}/src/agents/": "",
    f"{project_name}/src/agents/": "",
    f"{project_name}/src/agents/": "",
    #f"{project_name}/src/agents/orchestration_agent/": "",
    f"{project_name}/src/agents/orchestration_agent/": "",
    f"{project_name}/src/agents/orchestration_agent/": "",
    f"{project_name}/src/agents/orchestration_agent/": "",
    #f"{project_name}/src/agents/lifecycle_agent/": "",
    f"{project_name}/src/agents/lifecycle_agent/": "",
    f"{project_name}/src/agents/lifecycle_agent/": "",
    #f"{project_name}/src/agents/design_agent/": "",
    f"{project_name}/src/agents/design_agent/": "",
    f"{project_name}/src/agents/design_agent/": "",
    f"{project_name}/src/agents/design_agent/": "",
    f"{project_name}/src/agents/design_agent/": "",
    f"{project_name}/src/agents/design_agent/": "",
    f"{project_name}/src/agents/design_agent/": "",
    f"{project_name}/src/agents/design_agent/": "",
    #f"{project_name}/src/agents/simulation_agent/": "",
    f"{project_name}/src/agents/simulation_agent/": "",
    f"{project_name}/src/agents/simulation_agent/": "",
    f"{project_name}/src/agents/simulation_agent/": "",
    f"{project_name}/src/agents/simulation_agent/": "",
    #f"{project_name}/src/agents/analysis_agent/": "",
    f"{project_name}/src/agents/analysis_agent/": "",
    f"{project_name}/src/agents/analysis_agent/": "",
    f"{project_name}/src/agents/analysis_agent/": "",
    #f"{project_name}/src/agents/manufacturing_agent/": "",
    f"{project_name}/src/agents/manufacturing_agent/": "",
    f"{project_name}/src/agents/manufacturing_agent/": "",
    f"{project_name}/src/agents/manufacturing_agent/": "",
    f"{project_name}/src/agents/manufacturing_agent/": "",
    #f"{project_name}/src/engines/": "",
    f"{project_name}/src/engines/": "",
    f"{project_name}/src/engines/": "",
    #f"{project_name}/src/evolution/": "",
    f"{project_name}/src/evolution/": "",
    f"{project_name}/src/evolution/": "",
    f"{project_name}/src/evolution/": "",
    f"{project_name}/src/evolution/": "",
    f"{project_name}/src/evolution/": "",
    f"{project_name}/src/evolution/": "",
    f"{project_name}/src/evolution/": "",
    f"{project_name}/src/evolution/": "",
    f"{project_name}/src/evolution/": "",
    f"{project_name}/src/evolution/": "",
    #f"{project_name}/src/core/": "",
    f"{project_name}/src/core/": "",
    #f"{project_name}/src/core/data_processing/": "",
    f"{project_name}/src/core/data_processing/": "",
    f"{project_name}/src/core/data_processing/": "",
    f"{project_name}/src/core/data_processing/": "",
    #f"{project_name}/src/core/models/": "",
    f"{project_name}/src/core/models/": "",
    f"{project_name}/src/core/models/": "",
    f"{project_name}/src/core/models/": "",
    f"{project_name}/src/core/models/": "",
    f"{project_name}/src/core/models/": "",
    f"{project_name}/src/core/models/": "",
    #f"{project_name}/src/core/models/evolved_models/": "",
    #f"{project_name}/src/core/algorithms/": "",
    f"{project_name}/src/core/algorithms/": "",
    f"{project_name}/src/core/algorithms/": "",
    #f"{project_name}/src/core/knowledge_base/": "",
    f"{project_name}/src/core/knowledge_base/": "",
    f"{project_name}/src/core/knowledge_base/": "",
    f"{project_name}/src/core/knowledge_base/": "",
    f"{project_name}/src/core/knowledge_base/": "",
    #f"{project_name}/src/integrations/": "",
    f"{project_name}/src/integrations/": "",
    #f"{project_name}/src/integrations/ai_models/": "",
    f"{project_name}/src/integrations/ai_models/": "",
    f"{project_name}/src/integrations/ai_models/": "",
    f"{project_name}/src/integrations/ai_models/": "",
    #f"{project_name}/src/integrations/analysis/": "",
    f"{project_name}/src/integrations/analysis/": "",
    f"{project_name}/src/integrations/analysis/": "",
    f"{project_name}/src/integrations/analysis/": "",
    #f"{project_name}/src/integrations/cad_interfaces/": "",
    f"{project_name}/src/integrations/cad_interfaces/": "",
    f"{project_name}/src/integrations/cad_interfaces/": "",
    f"{project_name}/src/integrations/cad_interfaces/": "",
    f"{project_name}/src/integrations/cad_interfaces/": "",
    #f"{project_name}/src/integrations/simulation_interfaces/": "",
    f"{project_name}/src/integrations/simulation_interfaces/": "",
    f"{project_name}/src/integrations/simulation_interfaces/": "",
    f"{project_name}/src/integrations/simulation_interfaces/": "",
    f"{project_name}/src/integrations/simulation_interfaces/": "",
    f"{project_name}/src/integrations/simulation_interfaces/": "",
    #f"{project_name}/src/integrations/manufacturing_interfaces/": "",
    f"{project_name}/src/integrations/manufacturing_interfaces/": "",
    f"{project_name}/src/integrations/manufacturing_interfaces/": "",
    f"{project_name}/src/integrations/manufacturing_interfaces/": "",
    f"{project_name}/src/integrations/manufacturing_interfaces/": "",
    #f"{project_name}/src/integrations/supply_chain/": "",
    f"{project_name}/src/integrations/supply_chain/": "",
    #f"{project_name}/src/tools/": "",
    f"{project_name}/src/tools/": "",
    f"{project_name}/src/tools/": "",
    f"{project_name}/src/tools/": "",
    f"{project_name}/src/tools/": "",
    #f"{project_name}/src/utils//": "",
    f"{project_name}/src/utils//": "",
    f"{project_name}/src/utils//": "",
    f"{project_name}/src/utils//": "",
    #f"{project_name}/notebooks/": "",
    f"{project_name}/notebooks/": "",
    f"{project_name}/notebooks/": "",
    #f"{project_name}/notebooks/experiments/": "",
    f"{project_name}/notebooks/experiments/": "",
    f"{project_name}/notebooks/experiments/": "",
    #f"{project_name}/notebooks/demos/": "",
    f"{project_name}/notebooks/demos/": "",
    f"{project_name}/notebooks/demos/": "",
    #f"{project_name}/tests/": "",
    f"{project_name}/tests/": "",
    #f"{project_name}/tests/agents/": "",
    f"{project_name}/tests/agents/": "",
    f"{project_name}/tests/agents/": "",
    #f"{project_name}/tests/core/": "",
    f"{project_name}/tests/core/": "",
    f"{project_name}/tests/core/": "",
    f"{project_name}/tests/core/": "",
    f"{project_name}/tests/core/": "",
    f"{project_name}/tests/core/": "",
    #f"{project_name}/tests/integrations/": "",
    f"{project_name}/tests/integrations/": "",
    #f"{project_name}/tests/modules/": "",
    f"{project_name}/tests/modules/": "",
    #f"{project_name}/tests/modules/cad/": "",
    f"{project_name}/tests/modules/cad/": "",
    f"{project_name}/tests/modules/cad/": "",
    #f"{project_name}/tests/modules/simulation/": "",
    f"{project_name}/tests/modules/simulation/": "",
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