# Anaconda Python Distribution

There are numerous ways to install Python. These include:

## Anaconda

Anaconda is a Python distribution that includes:

* Python
* Python standard libraries
* Commonly used third-party data science libraries such as:
  * numpy
  * pandas
  * matplotlib
  * seaborn
  * scikit-learn
* The Anaconda PowerShell Prompt
* The conda package manager
* The Anaconda Navigator
* Integrated development environments:
  * IDLE
  * Spyder
  * IPython
  * QTConsole
  * Jupyter Notebook
  * JupyterLab

## Miniconda

Miniconda is a minimal Python Distribution stripped down version of Anaconda that includes:

* Python
* Python standard libraries
* The conda package manager
* Integrated development environments:
  * IDLE

## Python

The Python installer from Python.org contains:

* Python
* Python standard libraries
* The pip package manager
* Integrated development environments:
  * IDLE

## Package Managers

Python has two main package managers:

* pip - included in Python
* conda - included in Anaconda/Miniconda

pip is the most flexible package manager however this flexibility comes at an expense which is particularly felt by begineers as it can lead to installation of incompatible package versions... 

matplotlib the matrix plotting library for example under the hood uses the numeric python library numpy as a dependency and numpy itself uses python as a dependency. If a change is made in numpy that matplotlib doesn't expect it may lead to an error when using a matplotlib function. In turn if a change is made in python that numpy doesn't expect it may lead to an error when using a numpy function.

To avoid the above issues the conda package manager and the conda ecosystem in general is therefore much more stringent when it comes to solving package dependencies.

These guides will focus primarily on Anaconda although will be somewhat applicable to Miniconda because it is a lightweight version of Anaconda:

[Return to Anaconda Tutorial](./readme.md)