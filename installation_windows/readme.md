# Installation

Installation of VSCode itself if quite straightforward however VSCode is a general purpose code editor and the Python and Jupyter extensions need to be installed for use with Python. Finally a Python environment needs to be present which includes python and notebook, alongside some optional additional libraries. 

There are a number of different ways to install Python as Python has a number of different package managers. This guide recommends using Mambaforge as it includes the mamba package manager. The mamba package manager is less flexible than pip however it does a better job of checking and solving for package dependencies meaning you are less likely to install incompatible versions of packages which would otherwise be problematic. The mamba package manager is faster and more reliable than its predecessor conda and uses the community channel conda-forge by default.

It is recommended to only use a single package manager to manage Python environments on a Windows PC in order to avoid confusion.

## Install VSCode

Install VSCode using the User Installer. [VSCode User Installer](https://code.visualstudio.com/download)

## Install Python Extension

VSCode is a general purpose code editor and extensions need to be installed for it to work with other programming languages. Launch VSCode, select the extensions icon on the left hand side menu. Install the Python and Jupyter Extensions. Once installed close VSCode so it can reffresh the extensions.

## Install Mambaforge

Install Mambaforge using the default settings. [MambaForge](https://mamba.readthedocs.io/en/latest/installation.html)

Once installed launch the Mambaforge prompt (it may initially be listed in the start menu as the Miniforge prompt, this is a bug and will be addressed when the base Python environment is updated). To get the latest version of the Mamba package manager input:

```
mamba update --all
```

To create a new Python environment for VSCode use:

```
mamba create -n vscode python=3.11 notebook cython seaborn scikit-learn sympy openpyxl xlrd xlsxwriter lxml sqlalchemy tabulate nodejs ipywidgets plotly ipympl pyqt
```

Installing the data visualisation library seaborn will also install the numeric Python library numpy, the Python data and analysis library pandas and the math plotting library matplotlib. sci-kit learn is a popular machine learning library.

openpyxl, xlrd, xlsxwriter, lxml, sqlalchemy and tabulate are prequisite libraries for reading and exporting data using pandas.  pyqt and ipympl are used for the pyqt or ipympl backends of matplotlib plots. 

notebook, nodejs and ipywidgets are used for interactive Python notebooks. plotly is an interactive plotting library which is commonly used with interactive Python notebooks.

## Select Python Interpretter

Press Ctrl, Shift and p to open up the command palette. Search for Python: Select Interpretter and change the Python Interpretter to the Python Environment vscode.

## Test 

Open up the notebook in this folder. Select clear all outputs, restart and then run all. If the code runs without errors, your Python environment and VSCode IDE should be configured properly.

## Update

It is recommended to update your Python environment periodically. To do this open up the Mambaforge Prompt. To activate your vscode Python environment input:

```
mamba activate vscode
```

Then to update all packages input:

```
mamba update --all
```