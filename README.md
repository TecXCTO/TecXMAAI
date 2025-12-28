# TecXMAAI
TecX Mechanical Agentic AI

```

wool-plm-agent-system/
├── .github/                # CI/CD workflows for testing agents,  # GitHub-specific configurations
|   ├── workflows/          # Automated testing (CI/CD) and security scans, # CI/CD pipelines (GitHub Actions)
│   │   ├── ci.yml          # Continuous Integration pipeline
│   │   ├── cd.yml          # Continuous Deployment pipeline (optional)
│   │   └── linting.yml     # Code linting and formatting checks
│   └── ISSUE_TEMPLATE.md   # Template for bug reports and feature requests
│   └── PULL_REQUEST_TEMPLATE.md # Template for pull requests
│
├── config/                 # YAML/JSON configs for models & GA params
│   ├── agents.yaml         # Configuration for OpenAI and Google model roles
│   ├── evolution.yaml      # Genetic Algorithm parameters (mutation rate, etc.)
│   └── lifecycle.yaml      # Wool PLM specific constraints (ISO standards)
├── data/                   # Raw wool fiber scans and CAD specs (gitignored) # raw/ and processed/ engineering data
│   ├── cad_library/        # Versioned .STEP/.STL files
│   ├── materials_db/       # CSV/JSON material properties
│   ├── processed/          # Processed engineering data
│   ├── raw/                # Raw engineering data
│   ├── wool_samples/                  <-- [ADD] Dataset for fiber strength/images
│   └── evolved_variants/              <-- [ADD] Storage for generated model weights
├── scripts/                
│   └── run_evolution.py               <-- [ADD] Start the Genetic Algorithm loop
├── .env.template                      <-- [ADD] For OPENAI_API_KEY & GOOGLE_API_KEY
├── docs/                   # Technical documentation for PLM workflows, spec.md, design decisions, and manuals,    │   │                       Engineering specs & Life Cycle maps # Keep your Documentation structure,                │   │                         # Documentation for the project
│   ├── spec.md             
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
│   ├── api/                # API documentation (if applicable)
│   │   └── index.md
│   ├── research/           # Papers, surveys, or internal research notes
│   │   └── index.md
│   └── README.md           # Main README for the docs directory
│
├── src/                    # Primary source code
│   ├── domain/             # UNIT 1: Pure Engineering Rules # Pure physics and engineering models
│   │   ├── physics.py      # Stress/Strain formulas
│   │   └── materials.py    # Material entity definitions
│   ├── use_cases/          # Lifecyle workflows (e.g. design_validation.py)
│   │   ├── design_validation.py
│   ├── repositories/       # Repository interfaces and implementations # UNIT 2: The Data Gate (Interfaces)
│   │   ├── base_repo.py    # ABC for data access
│   │   └── cad_repo.py     # ABC for CAD file management
│   ├── adapters/           # UNIT 3: External Tool Connections
│   │   ├── cad/            # SolidWorks/FreeCAD specific code
│   │   ├── llm/            # LangChain/AI agent logic
│   │   └── database/       # PostgreSQL/SQLAlchemy logic
│   ├── agents/             # UNIT 4: Orchestration # AI reasoning and tool-calling logic, Role-based agent    │   │   │                       definition, # Individual AI agent modules,  # MULTIMODAL AGENT ORCHESTRATION
│   │   ├── __init__.py
│   │   ├── base_agent.py   # Abstract base class for all agents
│   │   ├── orchestration_agent/      # Agent responsible for coordinating others
│   │   │   ├── __init__.py
│   │   │   ├── workflow_manager.py
│   │   │   └── multimodal_bridge.py   <-- [ADD] Logic to swap GPT-4o (OpenAI) & Gemini (Google)
│   │   └── wool_lifecycle_agent/      <-- [ADD] Specific Agent for Wool Mechanical Properties
│   │   │   ├── fiber_analysis.py      # Microscopic image analysis (Multimodal)
│   │   │   └── sustainability_lca.py  # Life cycle/Biodegradability tracking
│   │   ├── design_agent/
│   │   │   ├── __init__.py
│   │   │   ├── generative_design.py
│   │   │   ├── optimization.py
│   │   │   └── feature_recognition.py
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
│   │   ├── designer_agent.py # The AI "Mechanical Agent" loop
│   │   ├── designer.py     # Uses OpenAI for 3D generative CAD
│   │   ├── inspector.py    # Uses Google Gemini for vision/video QA
│   │   ├── supervisor.py   # Multi-agent orchestrator, LangGraph/CrewAI orchestrator to manage handoffs
│   │   │                   # MULTIMODAL AGENT ORCHESTRATION
│   │   ├── openai_agent.py # Handles high-level design reasoning (GPT-4o)
│   │   ├── google_agent.py # Handles vision/video inspection (Gemini 2.5)
│   ├── engines/            # CORE COMPUTATIONAL MODELS
│   │   ├── generative.py   # Generative algorithms for 3D wool structures
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
│   │   ├── cad_interfaces/
│   │   │   ├── __init__.py
│   │   │   ├── solidworks_api.py
│   │   │   └── fusion360_api.py
│   │   ├── simulation_interfaces/
│   │   │   ├── __init__.py
│   │   │   ├── ansys_api.py
│   │   │   └── comsol_api.py
│   │   └── manufacturing_interfaces/
│   │       ├── __init__.py
│   │       └── cnc_controller_api.py       
│   │   └── supply_chain/         <-- [ADD] API for wool sourcing/farming data
│   ├── tools/              # Specialized mechanical engineering tools,    # MECHANICAL ENGINEERING UTILITIES
│   │   ├── cad_exporter.py # Export to STEP/STL for wool-composite parts
│   │   ├── lca_analyzer.py # Life Cycle Assessment for sustainability
│   │   ├── lca_calc.py     # Sustainability/LCA reporting tools
│   │   └── simulation.py   # Physics-based simulation wrappers
│   ├── utils/            # Helper(General utility) functions for API and data handling, not specific to agents
│   │   ├── __init__.py
│   │   ├── logging_config.py
│   │   └── config_loader.py
│   └── main.py             # Entry point for running the AI system (often a FastAPI app), (Triggers either    │                             Agent mode or Evolution mode)
├── notebooks/              # Keep for experimentation
├── tests/                  # Unit tests for agents and GA logic # Keep for quality control
├── .gitignore              # Standard Python and large data exclusions
├── pyproject.toml          # Modern dependency management
├── requirements.txt        # Legacy dependency list (PyTorch, LangChain, torch, langchain-google-genai, openai, pygad)
├── Dockerfile              # For containerized deployment
└── README.md               # Project overview and lifecycle goals, # Documentation of the self-evolving PLM system

```
