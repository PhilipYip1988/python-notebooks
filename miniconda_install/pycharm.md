# PyCharm

PyCharm is an advanced Python IDE used for Python script files (.py file extension). It does not ipython commands or interactive Python notebooks (.ipynb file extension). 

## Installing PyCharm

The download link for PyCharm is here:

[PyCharm Community](https://www.jetbrains.com/pycharm/)

There is a paid version and a free community version:

<img src='images_pycharm/img_001.png' alt='img_001' width='400'/>

Make sure to scroll down to the bottom of the page and select PyCharm community version:

<img src='images_pycharm/img_002.png' alt='img_002' width='400'/>

DOwnload the .exe, it should contain the word community in the file name:

<img src='images_pycharm/img_003.png' alt='img_003' width='400'/>

## Installing PyCharm

Launch the setup.exe:

<img src='images_pycharm/img_004.png' alt='img_004' width='450'/>

Accept the User Account Control Prompt:

<img src='images_pycharm/img_005.png' alt='img_005' width='350'/>

The setup will begin:

<img src='images_pycharm/img_006.png' alt='img_006' width='350'/>

Select the default install location:

<img src='images_pycharm/img_007.png' alt='img_007' width='350'/>

Select installation options:

<img src='images_pycharm/img_008.png' alt='img_008' width='350'/>

Select install:

<img src='images_pycharm/img_009.png' alt='img_009' width='350'/>

Select Finish:

<img src='images_pycharm/img_010.png' alt='img_010' width='350'/>

## Python Environment

Miniconda will be used to create a Python environment. To install Miniconda and set it up to use the conda-forge channel and libmamba solver see [Miniconda: Install](./Miniconda.md)

The following Python Environment can be created for the PyCharm IDE:

```
mamba create -n pycharm python cython seaborn scikit-learn sympy openpyxl xlrd xlsxwriter lxml sqlalchemy nodejs tabulate pyqt
```

This is covered in more detail in [Miniconda: Python Environments Overview](./environments.md)

<img src='images_pycharm/img_011.png' alt='img_011' width='450'/>

The mamba package manager will search for all of these packages and their dependencies. Input ```y``` in order to proceed:

<img src='images_pycharm/img_012.png' alt='img_012' width='450'/>

The packages will be downloaded and installed:

<img src='images_pycharm/img_013.png' alt='img_013' width='450'/>

## Customising PyCharm

Launch PyCharm from the Start Menu shortcut:

<img src='images_pycharm/img_014.png' alt='img_014' width='450'/>

Select customise and choose your color scheme:

<img src='images_pycharm/img_015.png' alt='img_015' width='450'/>

## Selecting the Python Interpreter

Like VSCode Pycharm expects a project (folder). Select projects and select New Project:

<img src='images_pycharm/img_016.png' alt='img_016' width='450'/>

Select Previously Configured Interpreter:

<img src='images_pycharm/img_017.png' alt='img_017' width='450'/>

Select conda environment and use existing conda environment. Select the pycharm conda environment:
 
<img src='images_pycharm/img_018.png' alt='img_018' width='450'/>

Select OK:

<img src='images_pycharm/img_019.png' alt='img_019' width='450'/>

Select create a main.py welcome script and select create:

<img src='images_pycharm/img_020.png' alt='img_020' width='450'/>

Pycharm will take a moment to index after selecting an interpreter for a new project. It essentially examines and processes the docstrings of all available modules.

## Running a Script File

There is a default script file ```main.py```. To understand its contents, it will be simplified to:

```
identifiers = dir()
print(dir)
```

This will print the data model identifiers that are included in this module:

```__name__``` and ```__file__``` are the name of the script file and the location of the file in Windows Explorer:

<img src='images_pycharm/img_021.png' alt='img_021' width='450'/>

The values of these data model attributes can be printed:

<img src='images_pycharm/img_022.png' alt='img_022' width='450'/>

Notice the location of the file is:

```%USERPROFILE%\Documents\project\main.py```

However the name is:

```__main__``` instead of ```main```

When Python runs a script file directly, it calls it ```__main__```.

If a new Python script file is created called ```script.py```:

<img src='images_pycharm/img_023.png' alt='img_023' width='450'/>

<img src='images_pycharm/img_024.png' alt='img_024' width='250'/>

And it includes code:

```
import main
```

When this file is run:

<img src='images_pycharm/img_025.png' alt='img_025' width='450'/>

The code in main.py is run:

<img src='images_pycharm/img_026.png' alt='img_026' width='450'/>

Notice the location of the file is:

```%USERPROFILE%\Documents\project\main.py```

And the name is:

```main```

The code in ```main.py``` can be modified to:

```
print(__name__)
print(__file__)

if __name__ == '__main__':
    print('Executred Directly)
else:
    print('Imported')
```

Now compare the difference to ```main.py``` being execurted directly:

<img src='images_pycharm/img_027.png' alt='img_027' width='450'/>

And it being imported in ```script.py```:

<img src='images_pycharm/img_028.png' alt='img_028' width='450'/>

## Code Completion

PyCharm has very good code completion and identifiers will display as you type:

<img src='images_pycharm/img_029.png' alt='img_029' width='450'/>
<img src='images_pycharm/img_030.png' alt='img_030' width='450'/>

A docstring will display as a one line pop up balloon by default:

<img src='images_pycharm/img_031.png' alt='img_031' width='450'/>

Pressing ```Ctrl```+```q``` will display a more detailed docstring as a pop up balloon:

<img src='images_pycharm/img_032.png' alt='img_032' width='450'/>

Since Pycharm has indexed the Python environment, identifiers display for third-party libraries:

<img src='images_pycharm/img_033.png' alt='img_033' width='450'/>

## Debugger and Variables

In the Script Editor breakpoints can be added. When the script is run in debug mode more information displays:

<img src='images_pycharm/img_034.png' alt='img_034' width='450'/>

The script data model attributes display as special variables:

<img src='images_pycharm/img_035.png' alt='img_035' width='450'/>

If resume program is selected the builtins instances instantiated in the script will display as variables:

<img src='images_pycharm/img_036.png' alt='img_036' width='450'/>

The collection instances can be examined in more detail:

<img src='images_pycharm/img_037.png' alt='img_037' width='450'/>

This works with variables created from the commonly used data science libraries:

<img src='images_pycharm/img_038.png' alt='img_038' width='450'/>

Plots show by default using the pyqt5 gui backend:

<img src='images_pycharm/img_039.png' alt='img_039' width='450'/>

[Return to Miniconda Installation](./readme.md)

















