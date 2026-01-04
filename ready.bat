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

dvc add data/samples/samples

git add data/samples/.gitignore data/samples/samples.dvc
git commit -m "Keep local changes to data config"
git pull


git stash
git pull
git stash pop


