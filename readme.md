# Python Tutorials

## Python Installation

The Anaconda Data Science Python Distribution contains Python and Python Standard Modules, the conda package manager, relatively modern versions of the data science libraries such as numpy, pandas and matplotlib, python formatters such as autopep8 and black and Python IDEs such as Spyder and JupyterLab.

This markdown tutorial will instruct on the setup and installation of Anaconda on Windows and Linux/Mac in addition to use of Python via the Terminal. Python is often used alongside the PowerShell or bash shell based scripting languages to navigate around the Operating System and differences in these languages will be highlighted.

This setup tutorial also discusses setting up VSCode and PyCharm with the Anaconda Python base environment.

Advanced use of Anaconda to create custom Python environments for the latest version of the Spyder and JupyterLab IDEs is also discussed. These instructions can be used with the lightweight Anaconda counterpart Miniconda:

* [Anaconda and Python Setup Markdown File](./anaconda/readme.md)

## Downloading from GitHub

These set of tutorials are in markdown and notebook format and stored on GitHub. GitHub has some limitations for displaying notebooks and many of these limitations are addressed using [Notebook Viewer](https://nbviewer.org/).

It is recommended to instead download this repository as a zip file. Select code and download zip, then extract the zip and open the extracted folder in VSCode or JupyterLab. Use VSCode or JupyterLab to clear all outputs and run each cell as you examine the notebook.

## Markdown

The markdown syntax is used with interactive Python notebooks. Before looking at these it is worthwhile reviewing the basic syntax:

* [Markdown syntax Markdown File](./markdown/readme.md)

## Builtins Module

The builtins module is automatically imported. It contains Pythons fundamental classes. These classes are based around the object class and the builtins module contains the functions which are used to invoke object based datamodel methods:

* [Object Notebook](./builtins_module_object/notebook.ipynb)
* [Immutable Strings Notebook](./builtins_module_str/notebook.ipynb)
* [Immutable Bytes Notebook](./builtins_module_bytes/notebook.ipynb)
* [Mutable ByteArray Notebook](./builtins_module_bytearray/notebook.ipynb)
* [Immutable Integer Notebook](./builtins_module_int/notebook.ipynb)
* [Immutable Boolean Notebook](./builtins_module_bool/notebook.ipynb)
* [Immutable Floating Point Notebook](./builtins_module_float/notebook.ipynb)
* [Immutable Tuple Notebook](./builtins_module_tuple/notebook.ipynb)
* [Mutable List Notebook](./builtins_module_list/notebook.ipynb)
* [Immutable FrozenSet Notebook](./builtins_module_frozenset/notebook.ipynb)
* [Mutable Set Notebook](./builtins_module_set/notebook.ipynb)
* [Mutable Dictionary Notebook](./builtins_module_dict/notebook.ipynb)

## Programming Constructs

A Python code block can be used to direct Python code in response to a condition, loop a series of operations again and again, perform error handling and to create custom functions:

* [Code Blocks Notebook](./programming_constructs/notebook.ipynb)

## Collections Module

The collections module contains a number of supplementary collections based around the collections seen in Python builtins module. This includes the ```namedtuple```, ```deque```, ```Counter``` and ```defaultdict``` classes:

* [Collections Module Notebook](./collections_module/notebook.ipynb)

## Itertools Module

The itertools module contains supplementary iterators that are closely related to and extend those found in Python builtins:

* [Itertools Module Notebook](./itertools_module/notebook.ipynb)

## Math and Complex Math Modules

The math and complex math modules contain commonly used mathematical functions typically returning scalar values:

* [Math and Complex Math Modules Notebook](./math_module/notebook.ipynb)

## Random Module

The random module is used to generate a random scalar number, often from a distribution:

* [Random Module Notebook](./random_module/notebook.ipynb)

## Datetime Module

The datetime module is used to generate scalar date, times, datetimes and timedeltas (time differences):

* [Datetime Module Notebook](./datetime_module/notebook.ipynb)

## Statistics Module

The statistics module is a functional module covering basic statistics normally returning a scalar from a list:

* [Statistics Module Notebook](./statistics_module/notebook.ipynb)

## System Module

* System Module Notebook

## Input Output Module

The Input and Output module is used for reading and writing text files .txt and binary files .bin. It can also be used for a Python Script file .py or Markdown file .py as these are fundamentally text files with a different file extension:

* [Input and Output Module Notebook](./io_module/notebook.ipynb)

## Comma Seperated Values Module

The Comma Seperated Values module expands the functionality of the io module allowing manipulation of files which have rows and columns opposed to just rows. It can be used with .csv, .txt and .prn files for example:

* [Comma Seperated Values Notebook](./csv_module/notebook.ipynb)

## Operating System Module

The Operating System module is a Python implementation of the bash or Powershell programming languages and contains commands to navigate around the Operating System. Functions in the Operating System module typically return a file path in the form of a Unicode string:

* [Operating System Module Notebook](./os_module/notebook.ipynb)

## Path Library Module

The Path Library Module is similar to the Operating System Module however uses an Object Orientated Programming (OOP) approach to file paths. File paths are returned as instances of the Path class which have a number of useful attributes and the datamodel method ```__truediv__``` (*dunder truediv*) is defined so the ```/``` operator can be used for folder and file concatenation:

* [Path Library Module](./pathlib/notebook.ipynb)

## Pickle Module

* Pickle Module Notebook

## Java Script Object Notation Module

* Java Script Object Notation Notebook

## The Numeric Python Library

* NDArray Notebook

## The Python and Data Analysis Library

* [Series and DataFrame Notebook](./pandas_library/notebook.ipynb)

## The Matrix Plotting Library

* [The Python Plot Module Introduction Notebook](./matplotlib_library/notebook_introduction.ipynb)
* [The Python Plot Module Backends Notebook](./matplotlib_library/notebook_backends.ipynb)

## The Data Visualisation Library

* Data Visualisation Notebook
