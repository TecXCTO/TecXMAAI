# 1. Unified Installation Command (PowerShell/Terminal)

# Upgrade the core package manager
python -m pip install -U pip setuptools wheel

# Install all primary 2026 engineering & AI libraries
python -m pip install pyansys[all] pywin32 aps-toolkit solid-client-python pytwin ansys-simai-core

# 2. Specialized AI Orchestration (NVIDIA NeMo)

git clone -b main git@github.com:NVIDIA/NeMo-Agent-Toolkit.git
cd nemo-agent-toolkit

# Use uv for modern 2026 environment management

pip install uv
uv sync --all-groups --all-extras

# 3. Create an "Agency" Requirement File

# 2026 Mechanical Engineering Agentic AI Stack

# pyansys[all]>=2025.1.0        # Comprehensive Ansys simulation suite
# aps-toolkit                   # Autodesk Platform Services (Cloud CAD)
# pytwin                        # Digital Twin management
# ansys-simai-core              # AI-accelerated physics prediction
# solid-client-python           # Decentralized data Pod access
# pywin32                       # Local COM bridge for Desktop Inventor/SolidWorks
# langgraph                     # Agentic workflow orchestration (optional but recommended)

pip install -r agency_install.txt

# 4. Desktop Setup for Local CAD Agents

# If your agents must control Autodesk Inventor or SOLIDWORKS on a local desktop: 
# Register Inventor SDK: Open a command prompt as Administrator and run:

C:\[Inventor Path]\Bin\ApprenticeRegSrv.exe /install

# SOLIDWORKS API: Run the SOLIDWORKS Installation Manager, select Modify, and ensure the API SDK is checked.
