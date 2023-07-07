# Installation

## Install VSCode

Install VSCode Individual.

## Install Python Extension

VSCode is a general purpose code editor. Install the Python and Jupyter Extensions in VSCode.

## Install Mambaforge

Launch the Mambaforge/Miniforge prompt. To get the latest version of the Mamba package manager input:

```
mamba update --all
```

To create a new Python environment for VSCode use:

```
mamba create -n vscode python=3.11 notebook cython seaborn scikit-learn sympy openpyxl xlrd xlsxwriter lxml sqlalchemy nodejs ipywidgets plotly ipympl pyqt
```

## Select Python Interpretter

Press Ctrl, Shift and p to open up the command palette. Search for Python: Select Interpretter and change the Python Interpretter to the Python Environment vscode.

## Test 

Open up the folder and run everything in the notebook.