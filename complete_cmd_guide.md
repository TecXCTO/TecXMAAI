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

Option 2: Discard your changes
Use this if you don't care about your local modifications to those two files and want them to match the server exactly.
bash
```
git checkout -- data/raw/.gitignore data/raw/samples.dvc
git pull
```
Use code with caution.
Option 3: Commit your changes 
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

