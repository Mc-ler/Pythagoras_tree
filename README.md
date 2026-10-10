# Pythagoras_tree
Aha Moment from a mate's image

# method of create one venv

```**code black**
# make preparations
mkdir project_folder
cd .\project_folder\

# Create with uv module
uv venv --python=py_v .venv_name

# Activate venv
[cmd/powershell] .venv\Scripts\Activate.bat

# deactivate
uv pip uninstall packages_name
deactivate

# remove folder and other cats and dogs
cd .\project_folder\
Remove-Item -recurse -Force(opt) .venv/

# freeze the venv
uv pip freeze > requirements.txt

# review the requirements.txt
cat requirements.txt
```

# method of How to use Git version control.

```**bash**
<!-- Had project already  -->
# Preparation
git init
git add .(filename)  -> git reset _(wrong_file_name) | git rm _(wrong_file_name)
git commit -m (messages)
git add README.md 
touch .gitignore

# Link to remote repo(Created in github.com)
git remote (https/SSH link from github)

# push and sync repo of local and remote.
git -M main
git push -u origin main

# Clone repo from github.com
git clone (https/SSH link from github)
```