# VSCode Setup

## Python Environment

Miniconda will be used to create a Python environment. To install Miniconda and set it up to use the conda-forge channel and libmamba solver see [Miniconda: Install](./Miniconda.md)

The following Python Environment can be created for the VSCode IDE.

```
conda create -n vscode python notebook cython seaborn scikit-learn sympy openpyxl xlrd xlsxwriter lxml sqlalchemy tabulate nodejs ipywidgets plotly ipympl pyqt
```

This is covered in more detail in [Miniconda: Python Environments Overview](./environments.md)

<img src='images_vscode/img_001.png' alt='img_001' width='450'/>

The conda package manager will search for all of these packages and their dependencies. Input ```y``` in order to proceed:

<img src='images_vscode/img_002.png' alt='img_002' width='450'/>

The packages will be downloaded and installed:

<img src='images_vscode/img_003.png' alt='img_003' width='450'/>

## VSCode Download

Go to the [VSCode](https://code.visualstudio.com/download) website and download the 64 Bit Windows User Installer:

<img src='images_vscode/img_004.png' alt='img_004' width='150'/>

Once the download completes:

<img src='images_vscode/img_005.png' alt='img_005' width='250'/>

## VSCode Install

Go to the Download folder and launch the setup.exe:

<img src='images_vscode/img_006.png' alt='img_006' width='450'/>

Accept the License Agreement and select Next:

<img src='images_vscode/img_007.png' alt='img_007' width='350'/>

Select the default destination folder and select Next:

<img src='images_vscode/img_008.png' alt='img_008' width='350'/>

Select the default Start Menu folder and select Next:

<img src='images_vscode/img_009.png' alt='img_009' width='350'/>

Select the default options and select Next:

<img src='images_vscode/img_010.png' alt='img_010' width='350'/>

Select Install:

<img src='images_vscode/img_011.png' alt='img_011' width='350'/>

Then Finish:

<img src='images_vscode/img_012.png' alt='img_012' width='350'/>

## VSCode Theme

When VSCode is first launch you will be prompted to select your theme. Dark Modern is the default.

<img src='images_vscode/img_013.png' alt='img_013' width='450'/>

This is commonly changed to light Modern:

<img src='images_vscode/img_014.png' alt='img_014' width='450'/>

## Python Extensions

VSCode is a general purpose code editor. For Python development, the Python extension needs to be installed. This enables the ability to work with Python Script Files:

<img src='images_vscode/img_015.png' alt='img_015' width='450'/>

Installation of python will install Pylance which is used for Python code completion:

<img src='images_vscode/img_016.png' alt='img_016' width='450'/>

For Interactive Python Noteboooks, the Jupyter extension should also be installed: 

<img src='images_vscode/img_017.png' alt='img_017' width='450'/>

This will install other Notebook related extensions:

<img src='images_vscode/img_018.png' alt='img_018' width='450'/>

Close and relaunch VSCode after installing extensions.

## Selecting the Python Interpretter

Select the Files Tab:

<img src='images_vscode/img_019.png' alt='img_019' width='450'/>

Then press ```Ctrl```, ```⇧``` and ```p``` to open the command palette and search for Python. Use Python Select Interpretter:

<img src='images_vscode/img_020.png' alt='img_020' width='450'/>

Change the Python Envirionment to vscode:

<img src='images_vscode/img_021.png' alt='img_021' width='450'/>

## Python Script File

VSCode is project based. In the simplest case a project is a folder which contains Python Script files. Select Open Folder:

<img src='images_vscode/img_022.png' alt='img_022' width='450'/>

Go to Documents, create a new folder for example called project and select it:

<img src='images_vscode/img_023.png' alt='img_023' width='450'/>

Select yes to trust the authors of the folder (you):

<img src='images_vscode/img_024.png' alt='img_024' width='450'/>

To the left select new file and create a file with a .py extension for example script.py notice that the file icon will change to a Python file:

<img src='images_vscode/img_025.png' alt='img_025' width='450'/>

Pylance will show code completion options as you type:

<img src='images_vscode/img_026.png' alt='img_026' width='450'/>

And function docstrings when functions are input followed by open parenthesis:

<img src='images_vscode/img_027.png' alt='img_027' width='450'/>

Pylance will show identifiers will show from Python objects:

<img src='images_vscode/img_028.png' alt='img_028' width='450'/>

A simple script file can be made:

```
print('Hello World!')
```

<img src='images_vscode/img_029.png' alt='img_029' width='450'/>

The file can be saved using ```Ctrl``` + ```s``` and run by right clicking and selecting Run Python File in Terminal:

<img src='images_vscode/img_030.png' alt='img_030' width='450'/>

In my case the following displays, this is because Miniconda is not added to the Windows Environmental Variables Path and the (base) Python environment is not used. 

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

This message can be ignored and the code otherwise runs as expected. To get rid of this error message, the (base) Python environment can be added to the Windows Environmental Variables path see [Adding Miniconda to the Windows Environmental Variables Path](./path.md)

<img src='images_vscode/img_031.png' alt='img_031' width='450'/>

## Interactive Python Notebook

To the left select new file and create a file with a .ipynb extension for example notebook.ipynb notice that the file icon will change to a Python file:

<img src='images_vscode/img_032.png' alt='img_032' width='450'/>

Create a code cell and input:

```
print('Hello World!')
```

Run the cell:

<img src='images_vscode/img_033.png' alt='img_033' width='450'/>

Select Python Environments:

<img src='images_vscode/img_034.png' alt='img_034' width='450'/>

Select the vscode Python environment:

<img src='images_vscode/img_035.png' alt='img_035' width='450'/>

The notebook runs a server in the background allow access through the Windows Firewall to proceed: 

<img src='images_vscode/img_036.png' alt='img_036' width='450'/>

the code now executes:

<img src='images_vscode/img_037.png' alt='img_037' width='450'/>

A test of the data science libraries can be made using the following four code cells:

```
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
```

```
df = pd.DataFrame({'x': np.array([0, 1, 2, 3, 4, 5]),
                   'y': np.array([0, 2, 4, 6, 8, 10])})
```

```
df
```

```
plt.plot(df['x'], df['y'])
```

<img src='images_vscode/img_038.png' alt='img_038' width='450'/>

[Return to Miniconda Installation](./readme.md)
