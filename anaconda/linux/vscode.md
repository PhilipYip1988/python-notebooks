# VSCode

Visual Studio Code is a general purpose code editor maintained by Microsoft.

## Installation

VSCode can be installed in Ubuntu from Software using the snap package. Open up softwaree and search for vscode:

<img src='images_vscode/img_001.png' alt='img_001' width='350'/>

Select install:

<img src='images_vscode/img_002.png' alt='img_002' width='350'/>

VSCode is now installed:

<img src='images_vscode/img_003.png' alt='img_003' width='350'/>

## Launching VSCode

VSCode can be launched from its Start Screen shortcut or by using the bash command:

```
code
```

<img src='images_vscode/img_004.png' alt='img_004' width='350'/>

## Selecting Syntax Highlighting Theme

The welcome screen will give you the option to select the syntax highlighting scheme. Dark Modern is the default theme and can be changed to Light Modern:

<img src='images_vscode/img_005.png' alt='img_005' width='350'/>

<img src='images_vscode/img_006.png' alt='img_006' width='350'/>

## Installing Python Extensions

Visual Studio code is a general purpose code editor and appropriate extensions need to be installed for each programming language.

VSCode is a general purpose code editor. For Python development, the Python extension needs to be installed. This enables the ability to work with Python Script Files:

<img src='images_vscode/img_007.png' alt='img_007' width='350'/>

For Interactive Python Notebooks, the Jupyter extension should also be installed:

<img src='images_vscode/img_008.png' alt='img_008' width='350'/>

A welcome tab will display for each extension:

<img src='images_vscode/img_009.png' alt='img_009' width='350'/>

Installation of the Python extension will install Pylance which is used for Python code completion. The Jupyter extension will install other Notebook related extensions:

<img src='images_vscode/img_010.png' alt='img_010' width='350'/>

## VSCode Project

VSCode is project based; a project is essentially a folder which contains a number of code files.

The Files Tab can be used to open a folder:

<img src='images_vscode/img_011.png' alt='img_011' width='350'/>

A new folder can be created in file explorer:

<img src='images_vscode/img_012.png' alt='img_012' width='350'/>

It can be called ```project1```:

<img src='images_vscode/img_013.png' alt='img_013' width='350'/>

And the code files can be moved to it:

<img src='images_vscode/img_014.png' alt='img_014' width='350'/>


This folder ```project1``` can be opened in VSCode by using Open Folder:

<img src='images_vscode/img_015.png' alt='img_015' width='350'/>

Then selecting ```project1``` and selecting Open:

<img src='images_vscode/img_016.png' alt='img_016' width='350'/>

There will be a security prompt, select Yes I trust the authors:

<img src='images_vscode/img_017.png' alt='img_017' width='250'/>

## Markdown

VSCode is a general purpose code editor and has inbuilt support for markdown files. Normally a project has a ```readme.md``` file, which is used to give an overview of the project. The ```markdown.md``` file can be renamed to ```readme.md```:

<img src='images_vscode/img_018.png' alt='img_018' width='350'/>

<img src='images_vscode/img_019.png' alt='img_019' width='350'/>

The formatted markdown file can also be be viewed by right clicking it and selecting Open Preview:

<img src='images_vscode/img_020.png' alt='img_020' width='350'/>

Both views are linked and this allows editing in real time.The markdown file alongside its preview can be viewed side by side. The markdown headings can be selected in the files navigation pane:

<img src='images_vscode/img_021.png' alt='img_021' width='350'/>

## Selecting the Python Interpretter

To use Python, the Python Interpretter (Python environment) needs to be selected. This can be done using the command palette.

Press ```Ctrl```, ```⇧``` and ```p`` to open the command palette and search for Python. Use Python Select Interpretter:

<img src='images_vscode/img_022.png' alt='img_022' width='350'/>

Change the Python Environment to (base):

<img src='images_vscode/img_023.png' alt='img_023' width='350'/>

## Microsoft IntelliSense

VSCode uses Microsoft's Intellisense which will display a list of identifiers in response to a prefix:

<img src='images_vscode/img_024.png' alt='img_024' width='350'/>

It will also display docstrings for functions when they are typed with open parenthesis:

<img src='images_vscode/img_025.png' alt='img_025' width='350'/>

## bash Terminal

A script file can be run in the Terminal by selecting run to the top right. This script file creates a plot which displays interactively in a seperate window:

<img src='images_vscode/img_026.png' alt='img_026' width='350'/>

## Interactive Python Terminal

Cells can be added in a Python script file using ```#%%```. When a cell is run, it is executed in an Ipython console opposed to a bash terminal:

<img src='images_vscode/img_027.png' alt='img_027' width='350'/>

Plots display in an IPython kernel.

Jupyter: Variables will display Variables only from Ipython console. No Variables will display when the script is run using a bash terminal:

<img src='images_vscode/img_028.png' alt='img_028' width='350'/>

Jupyter: Variables is basic, similar to Variables in Thonny:

<img src='images_vscode/img_029.png' alt='img_029' width='350'/>

There is some additional functionality and a small number of the Variables can be opened in a new tab to view them in more detail. At present the number of supported datatypes are limited:

<img src='images_vscode/img_030.png' alt='img_030' width='350'/>

## Notebook

With the Jupyter extension installed, VSCode has support for interactive Python notebooks. To run the code in these a kernel should be selected, select Select Kernel to the right:

<img src='images_vscode/img_031.png' alt='img_031' width='350'/>

Select Python environments:

<img src='images_vscode/img_032.png' alt='img_032' width='350'/>

Then select the base Python environment:

<img src='images_vscode/img_033.png' alt='img_033' width='350'/>

Use Clear All Outputs and Restart the Kernel:

<img src='images_vscode/img_034.png' alt='img_034' width='350'/>

Select Restart:

<img src='images_vscode/img_035.png' alt='img_035' width='200'/>

Jupyter based shortcut keys are available. A cell can be toggled between from Code (default) to Markdown using the shortcut keys ```Esc```+```m```. A cell can be toggled between from Markdown to Code using the shortcut keys ```Esc```+```y```. The keyboard shortcut ```⇧```+```↵``` will run a cell. The keyboard shortcut ```Alt```+```↵``` will run a cell and insert an empty cell below it. The cells can be run individually by selecting each cell and pressing run.

All cells can be run by using the Run All button:

<img src='images_vscode/img_036.png' alt='img_036' width='350'/>

Once again a variable or docstring can be viewed using the cell output:

<img src='images_vscode/img_037.png' alt='img_037' width='350'/>

<img src='images_vscode/img_038.png' alt='img_038' width='350'/>

Long output is truncated and can be viewed in a text editor tab:

<img src='images_vscode/img_039.png' alt='img_039' width='350'/>

Clicking View as Scrollable Element does not work. [GitHub: View as Scrollable Element Does Not Work](https://github.com/microsoft/vscode/issues/189699):

<img src='images_vscode/img_040.png' alt='img_040' width='350'/>

Plots are plotted by default as inline:

<img src='images_vscode/img_041.png' alt='img_041' width='350'/>

The IPython notebook uses Microsoft's intellisense which lists identifiers:

<img src='images_vscode/img_042.png' alt='img_042' width='350'/>

And displays docstrings:

<img src='images_vscode/img_043.png' alt='img_043' width='350'/>

## AutoFormat

Notice the poor formatting in the script file below particularly on line 6 and 7:

<img src='images_vscode/img_044.png' alt='img_044' width='350'/>

A Python Script file can be formatted using the format command. Press ```Ctrl```, ```⇧``` and ```p``` to open the command palette and search for Format Document. Select Format Document with and then in the dropdown select Configure Default Formatter and select AutoPEP8. 

The command Format Document can now be used which will use this specified default formatter. The command Format Document with can also be used to format the document with another formatter or to change the default:

<img src='images_vscode/img_045.png' alt='img_045' width='350'/>

This will correct the spacing in accordance to AutoPEP8:

<img src='images_vscode/img_046.png' alt='img_046' width='350'/>

Notice the poor formatting in some of the notebook cells:

<img src='images_vscode/img_047.png' alt='img_047' width='350'/>

The command Format Notebook can be used with an Interactive Python Notebook:

<img src='images_vscode/img_048.png' alt='img_048' width='350'/>

It is also possible to use an opinionated formatter such as black, which is preinstalled in the Anaconda base Python environment. To use black in VSCode, the black formatter extension needs to be installed in VSCode. Once installed select Format Document with and then in the dropdown select Configure Default Formatter and select Black.

[Return to Anaconda Tutorial](./readme.md)
