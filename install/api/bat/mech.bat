# 1. Primary Installation Command

# Upgrade pip first
python -m pip install -U pip

# Install the full PyAnsys suite
python -m pip install pyansys[all]

# 2. Specialized AI & Digital Twin Libraries

# Ansys SimAI: 
python -m pip install ansys-simai-core
# Ansys TwinAI: 
python -m pip install pytwin
# Data Processing (DPF): 
python -m pip install ansys-dpf-core[graphics]

# 

# Python Integration for Agents

# Essential for local COM interaction
pip install pywin32 

# Optional community-based Python wrapper (verify latest 2026 compatibility)
pip install pyinventor

#
# 1. Simulation & Physics (PyAnsys)

# Complete Suite:
python -m pip install -U pip
python -m pip install pyansys[all]

# Targeted Solvers (Fluid or Structural):
# For Fluid Dynamics agents
python -m pip install pyansys[fluent-all]

# For Structural Analysis agents
python -m pip install ansys-mapdl-core


# 2. Cloud CAD & Generative Design (Autodesk)

# APS Python Toolkit:
python -m pip install aps-toolkit

# Design Automation Utilities:
dotnet add package Autodesk.Forge.DesignAutomation.Inventor.Utils


# 3. Robotics & AI Orchestration (NVIDIA)

# NeMo Agent Toolkit:
# Clone and sync environment
git clone -b main git@github.com:NVIDIA/NeMo-Agent-Toolkit.git
cd nemo-agent-toolkit
uv sync --all-groups --all-extras


# 4. Manufacturing Agent Environment (Acuvate/Databricks)


# Summary of Quick Install Commands
# Category	Primary Library	Install Command
#Simulation	PyAnsys	
pip install pyansys
# CAD Automation	APS Toolkit	
pip install aps-toolkit
# Robotics Agents	NeMo Agent	
pip install nemo-agent-toolkit
# Control Systems	Python-COM	
pip install pywin32



