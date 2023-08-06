# Installation

The Python ecosystem is very vast and Python can be installed cross-platform in a variety of ways. This fragmentation can leave begineers feeling a bit confused.

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

Installation of packages using mixed conda and conda-forge channels leads to an unstable Python environment and should be avoided.

The conda package managers solver was rewritten and the conda-libmamba-solver rewrite addressed a number of performance issues previously experienced with conda.

## Miniconda

The Miniconda from Anaconda.com is a Python Distribution that includes:

Python
The Python standard libraries
conda package manager (never use pip)

Having a busy base Python environment isn't necessarily desired when only using the conda package manager to create custom Python environments and the reason for this bootstrap version. 

This minimal base Python environment contains the conda package manager and is defaulted to the conda channel.

## Miniconda 

Miniforge was a modified older version of Miniconda which defaults to the community conda-forge channel instead of the Anaconda conda channel. This installer is outdated containing a legacy version of Python and only has a depreciated CMD Prompt. 

It is recommended to use Miniconda or Anaconda with a .condarc set to use the community channel.

## Mambaforge

Mambaforge was a further modified version of Miniforge which included the 2 package manager. The mamba package manager was a development version of the conda-libmamba-solver. This is preinstalled in Miniconda or Anaconda but unfortunately not enabled by default. 

It is recommended to use Miniconda or Anaconda with a .condarc set to use the community channel and the conda-libmamba-solver.

## pip, conda and mamba

pip and conda package managers use similar syntax to install a package:

```
pip install package
conda install package
```

The channel can be selected for the conda package manager using -c followed by the channel name:

```
conda install -c conda package
conda install -c conda-forge package
```

Note: only use the recommended package manager for the installation (Python.org - pip), (Anaconda.com - conda). Use of mixed package managers and mixed channels will lead to an unstable Python environment.

These guides will focus on Miniconda and the conda package manager. Installation instructions will also be applicable to Anaconda:

* [readme](./readme.md)