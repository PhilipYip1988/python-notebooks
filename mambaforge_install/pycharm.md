# PyCharm

PyCharm is an advanced Python IDE used for Python script files (.py file extension). It does not ipython commands or interactive Python notebooks (.ipynb file extension). There is a paid version and a community version. This guide will look at the community version.

## Python Environment

Mambaforge will be used to create a Python environment. To install Mambaforge see [Mambaforge: Install](./mambaforge.md)

The following Python Environment can be created for the JupyterLab IDE:

```
mamba create -n pycharm python=3.11 cython seaborn scikit-learn sympy openpyxl xlrd xlsxwriter lxml sqlalchemy nodejs tabulate pyqt
```

This is covered in more detail in [Mambaforge: Python Environments Overview](./environments.md)



The mamba package manager will search for all of these packages and their dependencies. Input ```y``` in order to proceed:



The packages will be downloaded and installed:



