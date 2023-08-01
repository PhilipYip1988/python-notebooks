# Installation

The Python ecosystem is very vast and Python can be installed cross-platform in a variety of ways. There are also numerous integrated development environments (IDE), that is graphical user interfaces that programmers use to code in Python. 

# Python Distributions and Package Managers

## Python

Python is available as a standalone installer from Python.org, this standalone installer includes:

* Python
* The Python standard libraries
* pip package manager
* IDE: IDLE

The Integrated Developer Learning Environment (IDLE) is written in tkinter, a basic inbuilt graphical user interface Python library. 

This installer lacks the most commonly used third-party data science libraries such as the **num**eric **Py**thon library (numpy), the **P***ython **an**d **D**ata **A**naly**s**is Library (pandas) and the matrix plotting library (matplotlib). These libraries can be installed with Pythons package manager **P**ython **i**nstall **p**ackage (pip). Note however that pip is the most flexible package manager however it isn't very stringent when it comes to solving package dependencies. As a consequence new users are likely to install incompatible versions of Python libraries which can arise to issues.

## Anaconda

The Anaconda Individual Installer from Anaconda.com is a Python Distribution that includes:

* Python
* The Python standard libraries
* The data science libraries - numpy, pandas and matplotlib
* Machine learning frameworks - pytorch
* conda package manager (never use pip)
* IDEs: IDLE, Spyder and JupyterLab 

The Anaconda Python Distribution attempts to package the most commonly used data science libraries numpy, pandas, matplotlib in addition to large machine learning frameworks Pytorch and some of the most commonly used Python IDEs such as **Ju**lia **Pyt**hon and **R** Lab (JupyterLab) and the **S**cientific **Py**thon **D**evelopment **E**nvi**r**onment (Spyder) in its **base** Python environment, in addition to the conda package manager. 

A drawback of the Anaconda **base** environment has so many packages it becomes difficult to install additional packages without conflicts because of the large number of dependences required by the machine learning frameworks. As a consequence the base Python environment is supposed to be used "as is" and is updated by Anaconda using a standalone installer bi-annually. 

When additional packages are used they should be installed in a seperate Python environment which can be made and activated using the conda package manager. The conda package manafer is more stringent than pip when it comes to dependencies. 

The conda package manager has two channels:

* the conda-forge community channel
* the conda channel maintained by the Anaconda company
 
The Anaconda channel conda is essentially a subset of packages from the community channel conda-forge, that have been tested further by the Anaconda company for use with their distribution that includes the machine learning frameworks. 

Although these packages have been further tested for compatibility with the machine learning frameworks, a major drawback is that they are outdated and often lack some important bugfixes which is particularly prevalent in some of the IDEs. Another drawback is that less common packages from the conda-forge community channel are untested and not available in the conda channel. And finally installation of packages using mixed conda and conda-forge channels leads to an unstable Python environment.

## Mambaforge

The Mambaforge installer comes with:

* Python
* The Python standard libraries
* mamba package manager (never use conda or pip)
* IDEs: IDLE

Mambaforge is essentially a lightweight version of Anaconda with a basic **base** Python environment. The mamba package manager is an improved version of the conda package manager that is faster and better at solving dependencies. Mambaforge installs packages only from the community channel conda-forge by default. 

Mambaforge is recommended over Anaconda when creating custom Python envrionments for commonly used Python IDEs and data science libraries.

## pip, conda and mamba

pip, conda and mamba package managers use the same syntax to install a package:

```
pip install package
conda install package
mamba install package
```

The default channels will be conda for the conda package manager and conda-forge for the mamba package manager respectively. These can be explicitly specified using:

```
pip install package
conda install -c conda package
mamba install -c conda-forge package
```

Note: only use the recommended package manager for the installation (Python.org - pip), (Anaconda.com - conda) and (Mambaforge - mamba). Use of mixed package managers will lead to an unstable Python environment.

## Mambaforge Installation

These guides will focus only on Mambaforge:

* [Installation](./mambaforge.md)
* Updating the base Python Environment
* Python from Terminal
* IDLE
* Python Environment and Visual Studio Code
* Python Environment for JupyterLab
* Python Environment for Spyder
