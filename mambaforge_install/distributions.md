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

This installer lacks the most commonly used third-party data science libraries such as the **num**eric **Py**thon library (numpy), the **P**ython **an**d **D**ata **A**naly**s**is Library (pandas) and the matrix plotting library (matplotlib). These libraries can be installed with Pythons package manager **P**ython **i**nstall **p**ackage (pip). Note however that pip is the most flexible package manager however it isn't very stringent when it comes to solving package dependencies. As a consequence new users are likely to install incompatible versions of Python libraries which can arise to issues.

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

When additional packages are used they should be installed in a seperate Python environment which can be made and activated using the conda package manager. The conda package manager is more stringent than pip when it comes to dependencies. 

The conda package manager has two channels:

* the conda-forge community channel
* the conda channel maintained by the Anaconda company
 
The Anaconda channel conda is essentially a subset of packages from the community channel conda-forge, that have been tested further by the Anaconda company for use with their distribution that includes the machine learning frameworks. 

Although these packages have been further tested for compatibility with the machine learning frameworks, a major drawback is that they are outdated and often lack some important bugfixes which is particularly prevalent in some of the IDEs. Another drawback is that less common packages from the conda-forge community channel are untested and not available in the conda channel. 

And finally installation of packages using mixed conda and conda-forge channels leads to an unstable Python environment...

## Miniconda

Having a busy base Python environment isn't necessarily desired when using the conda package manager to create custom Python environments. Miniconda is an installer made by Anaconda that has a minimal base Python environment. This minimal base Python environment contains the conda package manager and is defaulted to the conda channel.

The default channel can be changed by creating a ```.condarc``` file in ```%USERPROFILE%``` and then updating the ```base``` Python environment. 

To use the community conda-forge channel the ```.condarc``` file should contain:

```
channel_priority: strict
channels:
  - conda-forge
  - defaults
```

To use the Anaconda conda channel the ```.condarc``` file should contain:

```
channels:
  - defaults
```

The base Python environment can be updated using the channel specified in the ```.condarc``` file with the command:

```
conda update --all
```

There is a third-party (from Anaconda) version of Miniconda called Miniforge which is essentially a version of Miniconda that defaults to the community conda-forge channel however as Anaconda/Miniconda have recently been updated Miniconda is outdated. Also on Windows it lacks the PowerShell Prompt using only the legacy Prompt. Mambaforge is a version of Miniconda that includes mamba, an improved version of the conda package manager written for increase speed and reliability.

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

For installation instructions of Mambaforge see:

* [readme](./readme.md)