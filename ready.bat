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


git stash
git pull
git stash pop


