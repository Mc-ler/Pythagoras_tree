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
```