# JupyterLab

Jupyter is an acronym for three popular programming languages particularly in the field of data science:

**Ju**pyter: Julia

Ju**py**ter: Python

Jupyte**r**: R

This guide will only focus on Python.

For Python, Jupyter is essentially a browser based implementation of ipython and allows compartmentalisation of code in an Interactive Python Notebook (ipynb file extension). There are two similar programs Jupyter Notebook and JupyterLab. Jupyter Notebook is the legacy program that has a simpler feature set being based only around the notebook (.ipynb file extension) and the associated ipython console. JupyterLab has a richer feature set and also includes a text editor (.txt file extension), markdown editor (.md file extension), python file editor (.py file extension) and a PowerShell prompt. This guide will only focus on JupyterLab.

## Creating a Python Environment

Miniconda will be used to create a Python environment. To install Miniconda and set it up to use the conda-forge channel and libmamba solver see [Miniconda: Install](./Miniconda.md)

The following Python Environment can be created for the JupyterLab IDE:

```
conda create -n jupyterlab python jupyterlab cython seaborn scikit-learn sympy openpyxl xlrd xlsxwriter lxml sqlalchemy nodejs tabulate ipywidgets plotly jupyterlab-variableinspector ipympl pyqt
```

This is covered in more detail in [Miniforge: Python Environments Overview](./environments.md)

<img src='images_jupyterlab/img_001.png' alt='img_001' width='450'/>

The conda package manager will search for all of these packages and their dependencies. Input ```y``` in order to proceed:

<img src='images_jupyterlab/img_002.png' alt='img_002' width='450'/>

The packages will be downloaded and installed:

<img src='images_jupyterlab/img_003.png' alt='img_003' width='450'/>

## Launching JupyterLab

There is no start menu shortcut for JupyterLab and it needs to be launched using the Miniforge Prompt. Activate the Python environment using:

```
conda activate jupyterlab
```

<img src='images_jupyterlab/img_004.png' alt='img_004' width='450'/>

The Python environment will change from (base) to (jupyterlab). Input the PowerSHell command jupyter followed by the option lab:

```
jupyter lab
```

<img src='images_jupyterlab/img_005.png' alt='img_005' width='450'/>

The terminal will remain busy while running a server for JupyterLab:

<img src='images_jupyterlab/img_006.png' alt='img_006' width='450'/>

JupyterLab will start in the default browser:

<img src='images_jupyterlab/img_007.png' alt='img_007' width='450'/>

## JupyterLab

The JupyterLab IDE looks like the following:

<img src='images_jupyterlab/img_008.png' alt='img_008' width='450'/>

To the left in red is a file explorer which opens by default in ```%USERPROFILE%```.

To the top left is a + button which opens a launcher in a new tab. A launcher is opened by default and shown on the right shown in purple.

The laucher has a number of tiles which include:

* text file shown in lime.
* markdown file shown in green, this file can be edited and viewed.
* python file shown in blue. This file can be launched in:
  * PowerShell terminal shown in gold
  * ipython shell shown in orange
* notebook file shown in pink. Each code cell in a notebook file is essentially an ipython cell.

There is also a navigation pane to the left hand side which will show headings from markdown files or notebook files.

There is also an extensions tab... previously this was used to install and remove extensions however this should typically be done using conda and their associated packages from the ```conda-forge``` channel. ```jupyterlab-variableinspector``` is an example of an installed extension.

To the left the Documents folder can be selected and to the right text file cna be selected from the launcher:

<img src='images_jupyterlab/img_009.png' alt='img_009' width='450'/>

The text file can be renamed by use of the file explorer to the left or the file tab. Both of these have a right click context menu which can be used to rename the file. There is also a file menu which includes the usual options to save the file:

<img src='images_jupyterlab/img_010.png' alt='img_010' width='450'/>

Once the file has been saved it can be viewed in Windows Explorer and opened in Notepad:

<img src='images_jupyterlab/img_011.png' alt='img_011' width='450'/>

<img src='images_jupyterlab/img_012.png' alt='img_012' width='450'/>

A markdown file can be created from a new launcher. If the file is right clicked, the markdown preview can be seen:

<img src='images_jupyterlab/img_013.png' alt='img_013' width='450'/>

This opens in a new tab which can be snapped to the side. To the left the table of contents shows. These should allow navigation through both the markdown file and markdown preview however at current has some limitations:

<img src='images_jupyterlab/img_014.png' alt='img_014' width='450'/>

The PowerShell terminal is similar to the Miniconda PowerShell Prompt allowing PowerShell commands such as the conda package manager and python. Notice the jupyterlab Python environment is selected:

<img src='images_jupyterlab/img_015.png' alt='img_015' width='450'/>

The ipython console is similar to ipython which can run Python code, and bash (similar to PowerShell) commands via ipython magics. Possible identifiers display when ```↹``` is pressed:

<img src='images_jupyterlab/img_016.png' alt='img_016' width='450'/>

docstrings will display for a function when the function name is input followed by open parenthesis and the keyboard combination ```⇧``` + ```↹``` are pressed:

<img src='images_jupyterlab/img_017.png' alt='img_017' width='450'/>

A Python script file can be created using a new launcher. Code completion will not display until the file is right clicked and a console for the editor is created:

<img src='images_jupyterlab/img_018.png' alt='img_018' width='450'/>

Select Python3:

<img src='images_jupyterlab/img_019.png' alt='img_019' width='450'/>

Then code completion in the script editor can be used by pressing ```↹``` and docstrings can be examined for functions by pressing ```⇧``` + ```↹``` respectively:

<img src='images_jupyterlab/img_020.png' alt='img_020' width='450'/>

<img src='images_jupyterlab/img_021.png' alt='img_021' width='450'/>

Identifiers from builtins and Pythons standard modules will display by default:

<img src='images_jupyterlab/img_022.png' alt='img_022' width='450'/>

Identifiers and docstrings from the data science libraries do not display in the script editor:

<img src='images_jupyterlab/img_023.png' alt='img_023' width='450'/>

Until the import is run in the ipython console by using Run and run selected code:

<img src='images_jupyterlab/img_024.png' alt='img_024' width='450'/>

<img src='images_jupyterlab/img_025.png' alt='img_025' width='450'/>

Once this is done code completion from objects imported into the ipython console work in the script editor. Pressing ```np.``` followed by a ```↹``` for example shows the identifiers in the numpy library:

<img src='images_jupyterlab/img_026.png' alt='img_026' width='450'/>

Since this is an ipython console, ipython magics can be used. These can be included in the script file but these won't be recognised if the script file is later ran using a PowerShell console:

<img src='images_jupyterlab/img_027.png' alt='img_027' width='450'/>

If a number of builtins instances are instantiated

<img src='images_jupyterlab/img_028.png' alt='img_028' width='450'/>

<img src='images_jupyterlab/img_029.png' alt='img_029' width='450'/>

They can be viewed by right clicking and selecting open variable inspector:

<img src='images_jupyterlab/img_030.png' alt='img_030' width='450'/>

This opens in a new tab that can be repositioned and looks similar to Variables in Thonny:

<img src='images_jupyterlab/img_031.png' alt='img_031' width='450'/>

Instances from classes in the data science libraries can be instantiated and a plot can be created which displays in the ipython cell:

<img src='images_jupyterlab/img_032.png' alt='img_032' width='450'/>

The instances display on the variable inspector:

<img src='images_jupyterlab/img_033.png' alt='img_033' width='450'/>

A notebook file can be created from a new launcher. It can have markdown and code cells:

<img src='images_jupyterlab/img_034.png' alt='img_034' width='450'/>

When these are run the markdown preview and Python code are respectively executed:

<img src='images_jupyterlab/img_035.png' alt='img_035' width='450'/>

<img src='images_jupyterlab/img_036.png' alt='img_036' width='450'/>

There are a number of useful shortcuts for JupyterLab.

The following toggle the cell type (these work when the cell is selected but the cursor is not in the input field):

|Keyboard Shortcut|Description|
|---|---|
|```y```|Change selected cell to code cell|
|```m```|Change selected cell to markdown cell|
|```r```|Change selected cell to raw cell|

The following run the cell (these work when the cell is selected and/or when the cursor is in the input field):

|Keyboard Shortcut|Description|
|---|---|
|```⇧```+```↵```|Run cell|
|```Alt```+```↵```|Run cell and add blank cell below it|

The following make changes to the Kernel and work when the cursor is not in the input field of a cell:

|Keyboard Shortcut|Description|
|---|---|
|```0```+```0```|Restart Kernel|

More details will show when Help → Show Keyboard Shortcuts is used.

Since ipython magics are available, the backend for matplotlib can be changed for example to the gui library pyqt5:

```
%matplotlib pyqt5
```

Notice the difference in the plot now, it displays in its own seperate window and has customisation options:

<img src='images_jupyterlab/img_037.png' alt='img_037' width='450'/>

Only toggling between inline and a single GUI toolkit is supported. If this is changed to:

```
%matplotlib ipympl
```

A warning ```Cannot change to a different GUI toolkit``` displays if another toolkit is displayed:

<img src='images_jupyterlab/img_038.png' alt='img_038' width='450'/>

Going to Kernel and restarting the Kernel and running all cells will switch to the ipympl GUI toolkit:

<img src='images_jupyterlab/img_039.png' alt='img_039' width='450'/>

The plot is now in the cell output but interactive opposed to a static image. This toolkit is still really limited compared to the pyqt5 toolkit used earlier:

<img src='images_jupyterlab/img_040.png' alt='img_040' width='450'/>

## Closing JupyterLab

After closing the tab in the browser or the browser itself:

<img src='images_jupyterlab/img_041.png' alt='img_041' width='450'/>

The server continues to run in the console:

<img src='images_jupyterlab/img_042.png' alt='img_042' width='450'/>

To close this press ```Ctrl``` + ```c```:

<img src='images_jupyterlab/img_043.png' alt='img_043' width='450'/>

[Return to Miniforge Installation](./readme.md)
