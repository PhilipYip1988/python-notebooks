# Python Tutorials

The Anaconda 2023-09 Data Science Python Distribution contains Python and Python Standard Modules, the conda package manager, relatively modern versions of the datascience libraries such as numpy, pandas and matplotlib, Python IDEs such as Spyder and JupyterLab. It also includes Python linters such as pylint, flake8 and pyflakes and Python formatters such as autopep8, isort and black which can greatly help improve code quality. 

## Python Installation

Anaconda can be installed on Windows and Linux/Mac for more details see:

* [Anaconda Installation](./anaconda/readme.md)

## Markdown

Markdown uses simple syntax to format text and is commonly used on GitHub and within Interactive Python Notebooks. For mathematical equations it is supplemented using TeX:

* [Markdown and TeX Syntax](./markdown/readme.md)

## Viewing Markdown Files and Notebook Files

These tutorials use markdown and notebook files and can be viewed in the browser or in an IDE or code editor such as JupyterLab or VSCode:

* [Viewing and Running Files](./viewing.md)

## Builtins Module

The builtins module is automatically imported. It contains Pythons fundamental classes. These classes are based around the object class and the builtins module contains the functions which are used to invoke object based datamodel methods:

* [Object Class](./builtins_module_object/notebook.ipynb)
* [Immutable Strings Class](./builtins_module_str/notebook.ipynb)
* [Immutable Bytes Class](./builtins_module_bytes/notebook.ipynb)
* [Mutable ByteArray Class](./builtins_module_bytearray/notebook.ipynb)
* [Immutable Integer Class](./builtins_module_int/notebook.ipynb)
* [Immutable Floating Point Class](./builtins_module_float/notebook.ipynb)
* [Immutable Boolean Class](./builtins_module_bool/notebook.ipynb)
* [Immutable Tuple Class](./builtins_module_tuple/notebook.ipynb)
* [Mutable List Class](./builtins_module_list/notebook.ipynb)
* [Immutable FrozenSet Class](./builtins_module_frozenset/notebook.ipynb)
* [Mutable Set Class](./builtins_module_set/notebook.ipynb)
* [Mutable Dictionary Class](./builtins_module_dict/notebook.ipynb)

## Collections and Code Blocks

A Python code block can be used to direct Python code in response to a condition, loop a series of operations again and again, perform error handling and to create custom functions:

* [Code Blocks](./programming_constructs/notebook.ipynb)

## IPython Magics

The Interactive Python Shell has a number of enhancements over the regular Python Shell. It can be used to run Python code and commonly used Shell commands that have been reimplemented as IPython magics. IPython magics are prefixed with a %. Shell commands that haven't been reimplemented as IPython magics can be run directly by prefixing with a !. The Shell used for these commands will differ depending on the Operating System, Windows will use PowerShell or CMD and Linux/Mac will use bash.

* [IPython Module](./ipython_magics/notebook.ipynb)

## Python Formatters

This tutorial gives an example of using the Python formatters using IPython magic commands. The VSCode installation tutorial demonstrated how to use these via VSCode extensions however it is useful to know how to run these tools using the command line and this tutorial shows an example of using IPython magics previously discussed.

The Automatic Python Enhanced Protocol 8 module is used to process a Python script or interactive Python notebook to autoformat a file to make sure its spacing is compliant with PEP8. 

The import sort module is an additional formatter used to make sure library imports are grouped by standard libraries, third-party libraries and sorted alphabetically in these two categories. 

The black formatter is an opinionated formatter used to standardise other formatting such as string quotations style. Unfortunately, its opinionated choices deviate from the style used in the Python language itself. 

The Rust Fast Formatter is similar to black but can be easily configured for a single quotation option. Ruff is in the early stages of development and is not yet preinstalled with Anaconda.

* [AutoPEP8, Import Sort, Black and Rust Fast Formatter Modules](./formatters/notebook.ipynb)

## Collections Module

The collections module contains a number of supplementary collections based around the collections seen in Python builtins module. This includes the ```namedtuple```, ```deque```, ```Counter``` and ```defaultdict``` classes:

* [Collections Module](./collections_module/notebook.ipynb)

## Itertools Module

The itertools module contains supplementary iterators that are closely related to and extend those found in Python builtins:

* [Itertools Module](./itertools_module/notebook.ipynb)

## Math and Complex Math Modules

The math and complex math modules contain commonly used mathematical functions typically returning scalar values:

* [Math and Complex Math Modules](./math_module/notebook.ipynb)

## Random Module

The random module is used to generate a random scalar number, often from a distribution:

* [Random Module](./random_module/notebook.ipynb)

## Datetime Module

The datetime module is used to generate scalar date, times, datetimes and timedeltas (time differences):

* [Datetime Module](./datetime_module/notebook.ipynb)

## Statistics Module

The statistics module is a functional module covering basic statistics normally returning a scalar from a list:

* [Statistics Module](./statistics_module/notebook.ipynb)

## Input Output Module

The Input and Output module is used for reading and writing text files .txt and binary files .bin. It can also be used for a Python Script file .py or Markdown file .py as these are fundamentally text files with a different file extension:

* [Input and Output Module](./io_module/notebook.ipynb)

## Comma Separated Values Module

The Comma Separated Values module expands the functionality of the io module allowing manipulation of files which have rows and columns opposed to just rows. It can be used with .csv, .txt and .prn files for example:

* [Comma Separated Values](./csv_module/notebook.ipynb)

## Operating System Module

The Operating System module is a Python implementation of the bash or Powershell programming languages and contains commands to navigate around the Operating System. Functions in the Operating System module typically return a file path in the form of a Unicode string:

* [Operating System Module](./os_module/notebook.ipynb)

## Path Library Module

The Path and Library module is similar to the Operating System Module however uses an Object Orientated Programming (OOP) approach to file paths and libraries within the user profile or home directory. File paths are returned as instances of the Path class which have a number of useful attributes and the datamodel method ```__truediv__``` (*dunder truediv*) is defined so the ```/``` operator can be used for folder and file concatenation:

* [Path and Library](./pathlib_module/notebook.ipynb)

## System Module

The System module provides access to some variables used or maintained by the Python interpreter and to functions that interact strongly with the interpreter:

* [System Module](./sys_module/notebook.ipynb)

## The Numeric Python Library

The Numeric Python library is based upon the data structure of the NDArray. This is a datastructure that is a collection however unlike ```builtins``` collections, all the datamodel methods are configured for numeric operations. numpy also scales the functions found in the math, datetime and random modules to ndarrays:

* [NDArray Class](./numpy_library/notebook.ipynb)

## The Python and Data Analysis Library

The Python and Data Analysis library builds upon the data structure of the ndarray, creating a Series which is a NDArray (1D) with a column name and a DataFrame which is a grouping of Series analogous in form to an Excel SpreadSheet. The Python and Data analysis library can be used to programically manipulate the data stored in the DataFrame analogous to any data operations that would be carried out manually in Excel:

* [Index, Series and DataFrame Classes](./pandas_library/notebook.ipynb)

## The Matrix Plotting Library

The matrix plotting library encompasses a large group of modules compartmentalising objects used for visual elements in a plot. As a user generally only the Python Plot Module is used which allows manipulation of the above objects using a simplified functional and object-orientated programming syntax:

* [Python Plot Module](./matplotlib_library/notebook.ipynb)
* [Plot Backends Comparison](./matplotlib_library/notebook_backends.ipynb)

## The Data Visualisation Library

seaborn is a wrapper library for matplotlib which greatly simplifies the code required to create plots that are commonly used for data visualisation of data stored in a DataFrame:

* [Data Visualisation Library](./seaborn_library/notebook.ipynb)

## The Plotly Library

plotly is a Python plotting library that creates plots using nodejs. This allows plots to be displayed interactively in the cell output of an interactive Python notebook. The plotly express module use syntax similar to seaborn:

* [Plotly Library](./plotly_library/notebook.ipynb)

## The Python Imaging Library

The Python Imaging Library contains the Image module which contains the Image data structure. This module is used for Image construction from an ndarray or an image file taken from another image manipulation program or camera. Note that the modern version of the Python Imaging Library is called PILLOW. PILLOW was originally a fork from PIL. PIL was Python 2 based and has been discontinued:

* [The Python Imaging Library](./pillow_library/notebook.ipynb)