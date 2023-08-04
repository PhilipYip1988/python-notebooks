# Spyder

Spyder is an abbreviation for the **S**cientific **Py**thon **D**evelopment **E**nvi**r**onment and is a Python IDE similar to MATLAB or R-Studio.

## Python Environment

Mambaforge will be used to create a Python environment. To install Mambaforge see [Mambaforge: Install](./mambaforge.md)

The following Python Environment can be created for the JupyterLab IDE:

```
mamba create -n spyder python=3.11 spyder cython seaborn scikit-learn sympy openpyxl xlrd xlsxwriter lxml sqlalchemy nodejs tabulate pyqt
```

This is covered in more detail in [Mambaforge: Python Environments Overview](./environments.md)



The mamba package manager will search for all of these packages and their dependencies. Input ```y``` in order to proceed:



The packages will be downloaded and installed:

## Launching Spyder

Spyder can be launched from its start menu shortcut.

## Update 

Update this guide when Spyder 6 is released.
