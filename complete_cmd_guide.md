To resolve this error, you must decide whether to save or discard your local changes to .gitignore and samples.dvc before Git can pull the new updates.
# Option 1: Save your changes (Recommended) 
Use this if you want to keep your local work. This "stashes" your changes, pulls the updates, and then reapplies your work on top. 
bash
```
git stash
git pull
git stash pop
```
Use code with caution.

#Option 2: Discard your changes
Use this if you don't care about your local modifications to those two files and want them to match the server exactly.
bash
```
git checkout -- data/raw/.gitignore data/raw/samples.dvc
git pull
```
Use code with caution.
#Option 3: Commit your changes 
If these changes are intentional and ready to be part of the history, commit them first. 
bash
```
git add data/raw/.gitignore data/raw/eci_samples.dvc
git commit -m "Keep local changes to data config"
git pull
```
Use code with caution.

Note: If you commit, Git will likely prompt you to "Merge" or "Rebase" when you pull.


To manage Python dependencies for development (linters, type checkers, and testing frameworks), it is best practice to list them in a requirements-dev.txt file or a [project.optional-dependencies] section in your pyproject.toml. 
Common Development Dependencies
Here are the industry-standard tools for a robust development environment:
```
Category 	Tool	Purpose
Linting	Ruff	Extremely fast replacement for Flake8, Isort, and more.
Formatting	Black	The "uncompromising" code formatter.
Type Checking	Mypy	Optional static typing for Python.
Testing	Pytest	The standard framework for writing and running tests.
Coverage	Coverage.py	Measures how much of your code is covered by tests.
Pre-commit	Pre-commit	Automatically runs linters before every git commit.
```
1. Using requirements-dev.txt
Create a file named requirements-dev.txt and include: 
text
-r requirements.txt  # Includes your main app dependencies
```
pytest>=8.0.0
pytest-cov
ruff
black
mypy
pre-commit
```
Use code with caution.

To install: pip install -r requirements-dev.txt 

2. Using pyproject.toml (Modern Standard)
If you are using a modern build system (like Setuptools, Flit, or Hatch), add this to your pyproject.toml: 
```
toml
[project.optional-dependencies]
dev = [
    "pytest>=8.0.0",
    "ruff",
    "black",
    "mypy",
    "pre-commit",
]
```
Use code with caution.

To install: pip install -e ".[dev]" 

# Recommended Quick-Start Commands
If you want to install them immediately via terminal:
```
bash
pip install ruff black mypy pytest pytest-cov pre-commit

```
Use code with caution.

For professional projects, I highly recommend setting up a Pre-commit configuration to ensure your code is linted and formatted automatically before it ever reaches GitHub.



To enable GPU support in 2026, Python dependencies typically depend on your hardware (NVIDIA or AMD) and the specific library (PyTorch, TensorFlow, or JAX) you are using. Modern frameworks now require Python 3.10+ and updated pip versions. 
1. PyTorch (Recommended for Deep Learning)
In 2026, the stable version (e.g., v2.9+) supports CUDA 12.6, 12.8, and 13.0 for NVIDIA GPUs. 
NVIDIA (CUDA 12.6):
bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu126
Use code with caution.

AMD (ROCm 6.4):
bash
pip install torch torchvision torchaudio --index-url download.pytorch.org
Use code with caution.

2. TensorFlow (For Production & Serving)
TensorFlow has unified its CPU and GPU packages for Linux and WSL2. Windows native support remains restricted to older versions (2.10 and below) or requires WSL2 for modern GPU support. 
Linux / WSL2 (NVIDIA GPU):
bash
pip install tensorflow[and-cuda]
Use code with caution.

Checking Installation:
python
import tensorflow as tf
print(tf.config.list_physical_devices('GPU'))
Use code with caution.

3. JAX (For Research & High-Performance Computing)
JAX requires two separate components: the jax Python library and jaxlib, which contains the compiled GPU binaries. 
NVIDIA (CUDA 13):
bash
pip install -U "jax[cuda13]"
Use code with caution.

Google TPU:
bash
pip install -U "jax[tpu]"
Use code with caution.

Important Prerequisites
Before installing these libraries, ensure your system meets the following requirements:
NVIDIA GPU Drivers: Version 525.60+ for Linux or 528.33+ for Windows WSL2.
CUDA Toolkit: Most 2026 releases target CUDA 12.x or 13.x.
Environment Check: Use nvidia-smi in your terminal to verify your driver is installed and recognize your GPU. 
If you are using a requirements file, use a standard URL link in your documentation to guide users to the correct hardware-specific command, as GPU dependencies are often too large for standard PyPI mirrors.



3333333333

To enable GPU support in 2026, your requirements_gpu.txt must point to specific hardware-optimized builds. Standard pip install commands often default to CPU-only versions for heavy libraries like PyTorch or JAX. 
Recommended requirements_gpu.txt
Choose the section that matches your framework and hardware (NVIDIA or AMD):
For PyTorch (NVIDIA CUDA 12.6/12.8)
text
--extra-index-url https://download.pytorch.org/whl/cu126
torch>=2.9.1
torchvision
torchaudio
Use code with caution.

Note: In 2026, PyTorch 2.9+ supports CUDA 12.6, 12.8, and experimental CUDA 13.0. 
For PyTorch (AMD ROCm 6.4/7.1)
text
--extra-index-url download.pytorch.org
torch>=2.9.1
torchvision
torchaudio
Use code with caution.

For TensorFlow (Linux/WSL2 with NVIDIA)
text
# Standard package now includes GPU support via [and-cuda] extra
tensorflow[and-cuda]>=2.18.0
Use code with caution.

Note: TensorFlow binaries now ship with dedicated kernels for GPUs with compute capability 8.9 (Ada Lovelace) and above. 
For JAX (NVIDIA CUDA 13.0+)
text
jax[cuda13_pip]
-f https://storage.googleapis.com/jax-releases/jax_cuda_releases.html
Use code with caution.

Note: JAX on CUDA 13 requires NVIDIA GPUs with SM version 7.5 or newer. 
2026 Hardware Requirements
NVIDIA Drivers: Ensure you have version 525+ for CUDA 12 or 580+ for CUDA 13 on Linux.
Python Version: Most 2026 GPU libraries require Python 3.10 to 3.14.
Verification: After installation, verify GPU access with the following Python snippet:
python
import torch
print(f"GPU Available: {torch.cuda.is_available()}")
print(f"Device Name: {torch.cuda.get_device_name(0)}")
Use code with caution.

 
To install from this file, run:
Pip Documentation
pip install -r requirements_gpu.txt


In pyproject.toml, GPU-specific dependencies are defined under the [project.optional-dependencies] table. This allows users to opt-in to hardware acceleration during installation (e.g., pip install ".[gpu]").
1. Recommended Structure for 2026
Modern standards distinguish between base requirements and hardware "extras." Use descriptive keys like gpu, cuda, or rocm.
toml
[project]
name = "my_ml_project"
version = "0.1.0"
dependencies = [
    "numpy>=2.0",
    "pandas>=2.2",
]

[project.optional-dependencies]
# Basic GPU extra for standard PyPI packages
gpu = [
    "tensorflow[and-cuda]>=2.18",
]

# Specific hardware extras for PyTorch or JAX
cuda = [
    "torch>=2.9.1",
    "torchvision",
]
rocm = [
    "torch>=2.9.1",
    "torchvision",
]
Use code with caution.

2. Handling Special Repositories (The "Index-URL" Problem)
Standard pyproject.toml (PEP 621) does not support specifying index-url or --extra-index-url directly within the file. This is a known limitation for libraries like PyTorch that host GPU-specific builds on their own servers. 
To resolve this in 2026, you have two primary options:
Option A: Tool-Specific Configuration (e.g., uv or poetry)
If you use modern tools like uv or Poetry, you can specify custom sources directly in the file:
toml
[[tool.uv.index]]
name = "pytorch-cuda"
url = "download.pytorch.org"
explicit = true

[project.optional-dependencies]
cuda = ["torch"]

[tool.uv.sources]
torch = { index = "pytorch-cuda" }
Use code with caution.

Option B: Hybrid Approach (Pip)
If using standard pip, define the package name in pyproject.toml but instruct users to provide the index during installation:
bash
pip install ".[cuda]" --extra-index-url download.pytorch.org
Use code with caution.

3. Comparison of Installation Commands
Requirement	Command
Standard/CPU	pip install .
General GPU	pip install ".[gpu]"
NVIDIA CUDA	pip install ".[cuda]"
AMD ROCm	pip install ".[rocm]"
Key Considerations for 2026
Version Pinning: As of 2026, ensure you pin to at least PyTorch 2.9+ or TensorFlow 2.18+ for compatibility with current CUDA 12.x/13.x drivers.
Dependency Groups: For local development involving GPU testing, you can use the newer [dependency-groups] (PEP 735) for tools that support it, though optional-dependencies remains the standard for published packages.
