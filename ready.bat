python >3.10 -m venv .tecxmaai
source .tecxmaai/bin/activate
winget install dvc
winget install --id Iterative.DVC
dvc --version
pip install dvc
pip install [all]

gh repo clone TecXCTO/TecXMAAI
cd TecXMAAI
git init
dvc init
git commit -m "Initialize DVC"

dvc add data/raw/samples

git stash
git pull
git stash pop

git add data/raw/.gitignore data/raw/samples.dvc
git commit -m "Keep local changes to data config"
git pull

# For Windows, download the installer from: https://git-lfs.github.com/
# After installation, open your terminal or Git Bash and run:
git lfs install


git lfs track "*.stl"  # Track STL files (3D models)
git lfs track "*.h5"   # Track Keras/TensorFlow model weights
git lfs track "data/raw/*.csv" # Track raw data files
git add .gitattributes
git commit -m "Configure Git LFS tracking"
git push


git add large_model.h5
git commit -m "Add a large trained model"
git push origin main

