```
To resolve this error, you must decide whether to save or discard your local changes to .gitignore and eci_samples.dvc before Git can pull the new updates.
Option 1: Save your changes (Recommended) 
Use this if you want to keep your local work. This "stashes" your changes, pulls the updates, and then reapplies your work on top. 
bash
```
git stash
git pull
git stash pop
'''
Use code with caution.

Option 2: Discard your changes
Use this if you don't care about your local modifications to those two files and want them to match the server exactly.
bash
'''
git checkout -- data/raw/.gitignore data/raw/eci_samples.dvc
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
```
