# VSCode

Visual Studio Code is a general purpose code editor maintained by Microsoft. 

## WinGet

VSCode can be installed with WinGet using the command:

```
WinGet install Microsoft.VisualStudioCode
```

## conda Initialisation

VSCode uses the Windows Terminal PowerShell and therefore requires the Anaconda base environment to be initialised or added to the Windows Environmental Variable Path otherwise the following error message will display when attempting to run a Python Script:

```
conda : The term 'conda' is not recognized as the name of a cmdlet, function, script 
file, or operable program. Check the spelling of the name, or if a path was included, 
verify that the path is correct and try again.
At line:1 char:1
+ conda activate vscode
+ ~~~~~
    + CategoryInfo          : ObjectNotFound: (conda:String) [], CommandNotFoundExceptio 
   n
    + FullyQualifiedErrorId : CommandNotFoundException
```

To initialise Anaconda in PowerShell right click the Windows 11 Start Button and open up the Windows Terminal (Admin) and change the execution policy:

```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned
```

Then initialise Anaconda:

```
Anaconda3\Scripts\conda init powershell
```

Close the Windows Terminal and close VSCode and relaunch to refresh the changes.

## conda Environment

The Anaconda base Python environment can be used with VSCode.

Alternatively a Python environment should be setup using the latest packages from the community channel conda-forge by opening up the Anaconda PowerShell Prompt and inputting:

```
conda create -n vscode-env -c conda-forge python jupyterlab jupyter cython seaborn scikit-learn sympy openpyxl xlrd xlsxwriter lxml sqlalchemy tabulate nodejs ipywidgets plotly ipympl pyqt autopep8 isort black pylint flake8 ruff
```

## Launching VSCode

VSCode can be launched using its Start Menu shortcut or using the PowerShell command in the Anaconda PowerShell Prompt:

```
code
```

## Selecting the Color Theme

The VSCode welcome screen will allow you to change the color scheme from dark modern (default):

<img src='images_vscode/img_010.png' alt='img_010' width='450'/>

To light modern for example:

<img src='images_vscode/img_011.png' alt='img_011' width='450'/>

## Configuring VSCode for Python

Visual Studio code is a general purpose code editor and appropriate extensions need to be installed for each programming language.

VSCode is a general purpose code editor. For Python development, the Python extension needs to be installed. This enables the ability to work with Python Script Files:

<img src='images_vscode/img_012.png' alt='img_012' width='450'/>

Installation of python will install Pylance which is used for Python code completion:

<img src='images_vscode/img_013.png' alt='img_013' width='450'/>

For Interactive Python Noteboooks, the Jupyter extension should also be installed: 

<img src='images_vscode/img_014.png' alt='img_014' width='450'/>

This will install other Notebook related extensions:

<img src='images_vscode/img_015.png' alt='img_015' width='450'/>

The intellicode extension by Microsoft will add commonly used snippets above the identifiers shown by the pylance extension in response to the current line of code being input.

The autopep8, isort and black extensions by Microsoft allow use of code formatters from libraries included in the Anaconda base Python environment. 

The pylint and flake8 extensions by Microsoft will apply additional Python linting.

The ruff extension by Astral software will allow use of the ruff formatter.

Close and relaunch VSCode after installing extensions.

## Selecting the Python Interpretter

Select the Files Tab:

<img src='images_vscode/img_016.png' alt='img_016' width='450'/>

Then press ```Ctrl```, ```⇧``` and ```p``` to open the command palette and search for Python. Use Python Select Interpretter:

<img src='images_vscode/img_017.png' alt='img_017' width='450'/>

Change the Python Environment to (base):

<img src='images_vscode/img_018.png' alt='img_018' width='450'/>

## Setting Up a Project

A project is essentially a folder that contains Python script files. Select Open Folder:

<img src='images_vscode/img_019.png' alt='img_019' width='450'/>

Navigate to Documents and create a folder called project:

<img src='images_vscode/img_020.png' alt='img_020' width='350'/>

Select I trust the authors:

<img src='images_vscode/img_021.png' alt='img_021' width='250'/>

Use the file explorer to the left to create a new Python script file with a .py file extension:

<img src='images_vscode/img_022.png' alt='img_022' width='450'/>

To the bottom the Python environment should display:

<img src='images_vscode/img_023.png' alt='img_023' width='450'/>

## Microsoft Intellisense

VSCode uses Microsoft's Intellisense which will display a list of identifiers in response to a prefix:

<img src='images_vscode/img_024.png' alt='img_024' width='450'/>

It will also display docstrings for functions when they are typed with open parenthesis:

<img src='images_vscode/img_025.png' alt='img_025' width='450'/>

This can be used for builtins:

<img src='images_vscode/img_026.png' alt='img_026' width='450'/>

Aswell as other Python standard libraries such as datetime:

<img src='images_vscode/img_027.png' alt='img_027' width='450'/>

The datetime class in the datetime module is not confused:

<img src='images_vscode/img_028.png' alt='img_028' width='450'/>

It also works well with third-party libraries such as numpy:

<img src='images_vscode/img_029.png' alt='img_029' width='450'/>

<img src='images_vscode/img_030.png' alt='img_030' width='450'/>

## Running a Script File in the Terminal

The Python script file can be run by selecting Run → Run Python file:

<img src='images_vscode/img_031.png' alt='img_031' width='450'/>

This will open a PowerShell Terminal within VSCode which goes to:

```
%USERPROFILE%/anaconda3/scripts
```

and uses the file ```activate``` to then activate the conda environment (base):

```
conda activate base
```

The current working directory path, Python environment path to the (base) Python.exe and the file path of the Python Script file all display:

```
PS CWDIR & PATH_TO_PYTHON/python.exe PATH_TO_SCRIPT/script.py
```

If Anaconda is not initialised an error will display as previously mentioned.

<img src='images_vscode/img_032.png' alt='img_032' width='450'/>

## Running a Script File in an Interactive Window

A script file with variables can also be ran in an interactive window, which opens an IPython console to the right:

```
string = 'hello'
bytestring = b'hello'
bytearraystring = bytearray(b'hello')
wholenum = 1
floatingpointnum = 3.14
boolean = True
archive = (string, string, wholenum, floatingpointnum)
active = [string, string, wholenum, floatingpointnum]
unique = {string, string, wholenum, floatingpointnum}
mapping = {'r': 'red', 'g': 'green', 'b': 'blue'}
```

<img src='images_vscode/img_033.png' alt='img_033' width='450'/>

All the code is ran in a single ipython cell:

<img src='images_vscode/img_034.png' alt='img_034' width='450'/>

This for some reason does not seem to work well with Jupyter Variables:

<img src='images_vscode/img_035.png' alt='img_035' width='450'/>

If instead cells are are added to the Python Script file using ```#%%``` and Run Cells are selected, the variables display under Jupyter Variables:

<img src='images_vscode/img_036.png' alt='img_036' width='450'/>

Some of the commonly used collections such as the list and mapping can be viewed in more detail:

<img src='images_vscode/img_037.png' alt='img_037' width='450'/>

At current the mapping seems to display with a numeric index instead of the keys:

<img src='images_vscode/img_038.png' alt='img_038' width='450'/>

Cells that import the data science libraries, create variables and plot can be run:

```
#%% Import Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#%% Create Data
x = np.array([0, 1, 2, 3, 4])
y = np.array([0, 2, 4, 6, 8])
df = pd.DataFrame({'x': x, 'y': y})
#%% Plot
plt.plot(df['x'], df['y'])
plt.show()
```

<img src='images_vscode/img_039.png' alt='img_039' width='450'/>

The array and DataFrame instances show on Jupyter Variables and can be viewed in more details:

<img src='images_vscode/img_040.png' alt='img_040' width='450'/>

<img src='images_vscode/img_041.png' alt='img_041' width='450'/>

## Notebook File

A new notebook file can be created by creating a new file, in the file explorer and using the .ipynb file extension:

<img src='images_vscode/img_042.png' alt='img_042' width='450'/>

This can be opened in VSCode and the Python interpretter should be selected. A number of markdown and code cells can be created:

```
# Notebook
```

```
## Import Libraries
```

```
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
```

```
## Create Data
```

```
x = np.array([0, 1, 2, 3, 4])
y = np.array([0, 2, 4, 6, 8])
df = pd.DataFrame({'x': x, 'y': y})
```

```
## Plot Data
```

```
plt.plot(df['x'], df['y'])
```

<img src='images_vscode/img_043.png' alt='img_043' width='450'/>

Selecting Run All will display the formatted markdown or code as an ipython cell with an integer prompt:

<img src='images_vscode/img_044.png' alt='img_044' width='450'/>

Variables once again display in Jupyter Variables and can also be explored in more detail using a cell output:

<img src='images_vscode/img_045.png' alt='img_045' width='450'/>

ipython magics can be used in an ipython cell for example to change the backend of the plot from inline which recall is nested in an ipython cell to qt5 which displays the plot in a seperate window. Both of these use QT to display graphics; the qt5 backend does not hang the notebook to maintain a plot like the tkagg backend does:

<img src='images_vscode/img_046.png' alt='img_046' width='450'/>

Docstings can be viewed in a cell output:

<img src='images_vscode/img_047.png' alt='img_047' width='450'/>

If they are too long only part of them will display:

<img src='images_vscode/img_048.png' alt='img_048' width='450'/>

These can be viewed in a text editor or a scrollable element for more details.

## Formatters

autopep8, isort, and black are preinstalled in the conda base environment. These are used to format Python code. To use these in VSCode the autopep8, isort and black extensions maintained by Microsoft need to be installed:

<img src='images_vscode/img_050.png' alt='img_050' width='450'/>

<img src='images_vscode/img_051.png' alt='img_051' width='450'/>

If sloppy code that violates pep8 is input:

```
var1='Hello'
var2="World"
import numpy as np
x=np.array([0,1,2,3,4])
y=np.array([0,2,4,6,8])
import pandas as pd
df=pd.DataFrame({'x':x,"y":y})
import datetime
now=datetime.datetime(year=2023,month=12,day=1)
hour=datetime.timedelta(hours=1)
import collections
counts=collections.Counter([1,2,2,2,3,3])
import itertools
cycle=itertools.cycle([1,2,3])
```

<img src='images_vscode/img_052.png' alt='img_052' width='450'/>

It can be formatted using Format Document. Press ```Ctrl```, ```⇧``` and ```p``` to open the command palette and search for Format Document With...

<img src='images_vscode/img_053.png' alt='img_053' width='450'/>

Select Configure Default Formatter:

<img src='images_vscode/img_054.png' alt='img_054' width='450'/>

Select autopep8:

<img src='images_vscode/img_055.png' alt='img_055' width='450'/>

Press ```Ctrl```, ```⇧``` and ```p``` to open the command palette and search for Format Document. Use the comand Format Document:

<img src='images_vscode/img_056.png' alt='img_056' width='450'/>

Notice that all the import statements are at the top with Python standard modules followed by third-party library imports. Notice that the spacing around assignment operators is consistent, highlighting the assignment of a variable. In collections or functions whitespacing is used to highlight the delimiter.

<img src='images_vscode/img_057.png' alt='img_057' width='450'/>

For an interactive Python Notebook, the analogous command Format Notebook can be used. With autopep8 the quotations are still inconsistent as pep8 doesn't explicitly state a preference for single quotations over double quotations. 

The imports are grouped by type: standard module and then third-party library but these categories aren't worted by category. Press ```Ctrl```, ```⇧``` and ```p``` to open the command palette and search for organize imports and this should use ```isort``` to properly sort the imports. Note using isort without previously formatting the code with autopep8 does not always work properly.

Black is an opinioned formatter that will carry out additional opinionated formatting. Select Format Document With:

<img src='images_vscode/img_058.png' alt='img_058' width='450'/>

Select Black Formatter:

<img src='images_vscode/img_059.png' alt='img_059' width='450'/>

Notice the blank line added after all the import statements to further highlight the dependencies of the script file. Notice also that all the strings are enclosed in double quotations:

<img src='images_vscode/img_060.png' alt='img_060' width='450'/>

Black does not sort imports and relies on isort to sort imports. Recall isort often does not work properly unless the code has previously been formatted by autopep8. If using black it is recommended to use autopep8, isort and then black. Note that some of the opinioned choices made in black are contentious. The most contentious choice is the enforcement of double quotes as the Python interpretter prefers single quotes. I personally do not use black because of this reason. An alternative formatter ruff is available which can be configured to use single quotes. This will be covered in a subsequent notebook.

[Return to Anaconda Tutorial](./readme.md)
