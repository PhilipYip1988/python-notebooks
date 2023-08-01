# Managing Python Environments

The main purpose of Mambaforge is to create and maintain a Python Environment. 

## base Python Environment

In [Mambaforge Installation](./mambaforge.md) the concept of the (base) Python environment was examined. This is the main Python environment of the Mambaforge installation and contains the mamba package manager.

The location of the (base) Python environment is in:

```
%UserProfile%/Mambaforge
```

While it is possible to install packages in the (base) Python environment, it is not recommended to do so. For best performance this Python environment should be kept as basic as possible being used mainly by the package manager.

It is recommended to instead create a seperate Python, in essence a subinstallation of Python for each IDE and for advanced users for each project.

In the (base) Python environment is an envs subfolder:

<img src='images_vscode/img_001.png' alt='img_001' width='450'/>

This is empty by default:

<img src='images_vscode/img_002.png' alt='img_002' width='450'/>

## mamba Package Manager Overview

An overview of the mamba package manager can be seen by inputting:

```
mamba
```

A Python environment can be created using the syntax:

```
mamba create -n ENVNAME
```

where ENVNAME is a placeholder for the environment name which is in lower case.

Once the Python environment is created it can be activated using:

```
mamba activate ENVNAME
```

Packages can be listed in the Python environment using:

```
mamba list
```

The conda-forge community channel can be searched for a package using:

```
mamba search PACKAGENAME1
```

Packages can be installed using:

```
mamba install PACKAGENAME1 PACKAGENAME2 ...
```

A package can be removed using:

```
mamba remove PACKAGENAME1 PACKAGENAME2 ...
```

Version numbers can be specified:

```
mamba install PACKAGENAME1=X.Y.Z
```

Where X is the major number, Y is the minor version number and Z is the patch number.

A package can be updated using:

```
mamba update PACKAGENAME
```

All packages can be updated using:

```
mamba update --all
```

A backup of all previously downloaded versions is available which can occupy a large amount of disk space. These can be cleaned using:

```
mamba clean --all
```

The create and install commands can be combined using:

```
mamba create -n ENVNAME PACKAGENAME1 PACKAGENAME2 ...
```

There is a legacy env command that is currently only available using conda (mamba is based upon conda) and won't act upon the selected environment, instead -n ENVNAME needs to be provided. This includes exporting the Environment to a yml file: 

```
conda env export -n ENVNAME > Documents\ENVNAME.yml
```

And deleting the Python environment

```
conda env remove -n ENVNAME 
```

## Example Python Environment

The following Python Environment can be created for the VSCode IDE.

```
mamba create -n vscode python=3.11 notebook cython seaborn scikit-learn sympy openpyxl xlrd xlsxwriter lxml sqlalchemy tabulate nodejs ipywidgets plotly ipympl pyqt
```

In this case:

ENVNAME is vscode

The packages to be installed are Python with the major and minor version number 3.11 specified. The latest patch for this minor version will be selected where available.

notebook, nodejs and ipywidgets are used for interactive Python notebooks. plotly is an interactive plotting library which is commonly used with interactive Python notebooks.

Installing the data visualisation library seaborn will also install the numeric Python library numpy, the Python data and analysis library pandas and the math plotting library matplotlib. sci-kit learn is a popular entry machine learning library.

openpyxl, xlrd, xlsxwriter, lxml, sqlalchemy and tabulate are prequisite libraries for reading and exporting data using pandas. pyqt and ipympl are used for the pyqt or ipympl backends of matplotlib plots.

<img src='images_vscode/img_003.png' alt='img_003' width='450'/>

The mamba package manager will search for all of these packages and their dependencies. Input ```y``` in order to proceed:

<img src='images_vscode/img_004.png' alt='img_004' width='450'/>

The packages will be downloaded and installed:

<img src='images_vscode/img_005.png' alt='img_005' width='450'/>

The Mambaforge Prompt can be cleared using:

```
cls
```

<img src='images_vscode/img_006.png' alt='img_006' width='450'/>

In Windows Explorer, there is now a vscode folder in the envs subfolder:

<img src='images_vscode/img_007.png' alt='img_007' width='450'/>

Notice it has its own python.exe:

<img src='images_vscode/img_008.png' alt='img_008' width='450'/>

Lib subfolder:

<img src='images_vscode/img_009.png' alt='img_009' width='450'/>

Standard Modules such as the package email:

<img src='images_vscode/img_010.png' alt='img_010' width='450'/>

<img src='images_vscode/img_011.png' alt='img_011' width='450'/>

And the module datetime:

<img src='images_vscode/img_012.png' alt='img_012' width='450'/>

It also has its own site-packages folder which contains the third-party packages:

<img src='images_vscode/img_013.png' alt='img_013' width='450'/>

This includes numpy:

<img src='images_vscode/img_014.png' alt='img_014' width='450'/>

<img src='images_vscode/img_015.png' alt='img_015' width='450'/>

And matplotlib:

<img src='images_vscode/img_016.png' alt='img_016' width='450'/>

<img src='images_vscode/img_017.png' alt='img_017' width='450'/>

<img src='images_vscode/img_018.png' alt='img_018' width='450'/>

Typically only the pyplot module is used in matplotlib.

## Activating Python Environments

By default the base Python environment is selected and this can be seen by checking:

```
import email
email.__file__
import datetime
datetime.__file__
```

If the following is input:

```
import numpy as np
```

there is a ModuleNotFoundError because there is no numpy folder in the (base) Python environment:

<img src='images_vscode/img_019.png' alt='img_019' width='450'/>

In other words packages are being searched for in:

```
%USERPROFILE%/Mambaforge/Lib
```

<img src='images_vscode/img_020.png' alt='img_020' width='450'/>

And not:

```
%USERPROFILE%/Mambaforge/envs/vscode/Lib
```

<img src='images_vscode/img_021.png' alt='img_021' width='450'/>

If the following is input:

```
mamba list
```

there is no mention of numpy:

<img src='images_vscode/img_022.png' alt='img_022' width='450'/>

If the following is input:

```
mamba activate vscode
```

<img src='images_vscode/img_023.png' alt='img_023' width='450'/>

Notice the (base) changes to (vscode) indicating a different Python environment is selected. **Pay attention to this as it indicates what Python environment is activated and is being changed**.

<img src='images_vscode/img_024.png' alt='img_024' width='450'/>

Notice the difference in Python version when the following is input:

```
python
```

And:

```
import email
email.__file__
import datetime
datetime.__file__
import numpy as np
np.__file__
import pandas as pd
pd.__file__
import matplotlib.pyplot as plt
plt.__file__
```

<img src='images_vscode/img_025.png' alt='img_025' width='450'/>

If the following is now input:

```
mamba list
```

there is a much longer list and numpy is listed.


<img src='images_vscode/img_026.png' alt='img_026' width='450'/>

## Updating Python Environments

The Python environment can periodically be checked for updates using:

```
mamba update --all
```

<img src='images_vscode/img_027.png' alt='img_027' width='450'/>

Since this Python environment was just created, it will be up to date:

<img src='images_vscode/img_028.png' alt='img_028' width='450'/>

## Exporting Python Environments

This Python environment can be exported to a file in Documents:

```
conda env export -n vscode > Documents\vscode.yml
```

<img src='images_vscode/img_029.png' alt='img_029' width='450'/>

Once exported a new prompt displays:

<img src='images_vscode/img_030.png' alt='img_030' width='450'/>

The yml file can be viewed in File Explorer:

<img src='images_vscode/img_031.png' alt='img_031' width='450'/>

And opened in Notepad:

<img src='images_vscode/img_032.png' alt='img_032' width='450'/>

## Deleting a Python Environment

## Creating a Python Environment from a File




<img src='images_vscode/img_033.png' alt='img_033' width='450'/>
<img src='images_vscode/img_034.png' alt='img_034' width='450'/>
<img src='images_vscode/img_035.png' alt='img_035' width='450'/>
<img src='images_vscode/img_036.png' alt='img_036' width='450'/>
<img src='images_vscode/img_037.png' alt='img_037' width='450'/>
<img src='images_vscode/img_038.png' alt='img_038' width='450'/>
