# Miniconda Install

Miniconda is an Anaconda based installer, which has a lightweight base Python environment instead of a data science distribution. This base Python environment contains Python 3.11 and the conda package manager which can be used to create Python environments. The conda-libmamba-solver is included with Miniconda which greatly increases its performance. 

The conda package manager has two channels:

* conda: default
* conda-forge: community channel

The conda-forge channel is the community channel and is maintained directly by project developers. The conda channel is a channel maintained by anaconda developers who test packages for compatibility with their Anaconda Python Distribution. As it takes time to test packages and they only test more popular packages, this channel is usually behind the community conda-forge channel. It is generally more reliable to use the conda-forge channel when creating custom environments. 

Unfortunately neither the conda-forge channel or conda-libmamba-solver are enabled by default but can easily be enabled post-installation by a .condarc configuration file. 

Miniforge and Mambaforge were modified Miniconda installers that are defaulted to the conda-forge channel and in the case of Mambaforge included the mamba package manager. These installers are outdated on Windows (have old Python versions) and lack some features (using the depreciated CMD instead of PowerShell).

## Uninstall

Miniconda may not work as intended when another Anaconda based Python distribution is installed such as Anaconda, Miniconda (including Miniforge, Miniconda). 

If you have an old Python installation follow the instructions to [Uninstall and Purge old Python Distributions](./uninstall.md). This will allow Miniconda to be installed properly.

## Download

The download link for Miniconda can be found on the [Miniconda](https://docs.conda.io/en/latest/miniconda.html) home page. Select Miniconda3-Windows-64_bit:

<img src='images_miniconda/img_001.png' alt='img_001' width='400'/>

The setup should now be in the Downloads folder:

<img src='images_miniconda/img_002.png' alt='img_002' width='250'/>

## Installation

Launch the setup:

<img src='images_miniconda/img_003.png' alt='img_003' width='400'/>

The setup will begin:

<img src='images_miniconda/img_004.png' alt='img_004' width='350'/>

Accept the License Agreement:

<img src='images_miniconda/img_005.png' alt='img_005' width='350'/>

Select just me (recommended):

<img src='images_miniconda/img_006.png' alt='img_006' width='350'/>

The default install location will be in:

```
%USERPROFILE%\Miniconda3
%USERPROFILE%\Anaconda3
```

The environmental variable %USERPROFILE% maps to the location of your User Profile, in this case C:\\Users\\Philip

<img src='images_miniconda/img_007.png' alt='img_007' width='350'/>

Installation options will display:

<img src='images_miniconda/img_008.png' alt='img_008' width='350'/>

A common option the I recommend enabling (although shown as not recommended) is to add Miniconda to the Windows Environmental Variables Path which makes the (base) Python environment available in the Windows Terminal. 

Note that leaving this option unchecked may cause a minor issue with VSCode. VSCode uses the Windows Terminal and shows an error message when launching a Python script when the (base) Python environment is not added to the path. If this option has not been checked, Miniconda can be manually added to the Windows Environmental Variables path see:
[Adding Miniconda to the Windows Environmental Variables Path](./path.md). 

The reason this option is not recommended by default is it can arise to conflicts when multiple Python distributions are installed/uninstalled. In general it is not recommended to install multiple Python distributions and a better practice to stick to only using Miniconda.

<img src='images_miniconda/img_009.png' alt='img_009' width='350'/>

Select Next:

<img src='images_miniconda/img_010.png' alt='img_010' width='350'/>

Select Finish:


<img src='images_miniconda/img_011.png' alt='img_011' width='350'/>

## Exploring the base Python Environment

Miniconda should be installed in:

```
%UserProfile%/Miniconda3
%UserProfile%/Anaconda3
```

<img src='images_miniconda/img_012.png' alt='img_012' width='350'/>

<img src='images_miniconda/img_013.png' 
alt='img_013' width='350'/>


In this folder is a python.exe

<img src='images_miniconda/img_014.png' alt='img_014' width='400'/>

And a Lib subfolder:

<img src='images_miniconda/img_015.png' 
alt='img_015' width='400'/>

This Lib subfolder contains Python standard modules. 

These can be in the form of packages and the folder name is essentially the package name. For example in the case of email:

<img src='images_miniconda/img_016.png' alt='img_016' width='450'/>

In the email folder is a \_\_init\_\_.py which is the initialisation module of the folder:

<img src='images_miniconda/img_017.png' alt='img_017' width='450'/>

Or in the form of a module.py for example datetime.py

<img src='images_miniconda/img_018.png' alt='img_018' width='450'/>

## Miniconda PowerShell Prompt

The Miniconda PowerShell Prompt is a Windows PowerShell Prompt that also has access to the conda package manager and supports switching between Python environments:

<img src='images_miniconda/img_019.png' alt='img_019' width='300'/>

This opens a Terminal similar to the Windows Terminal. 

```(base)``` indicates that the Miniconda Python base environment is selected.

```C:\Users\Philip``` indicates the file path which is ```%UserProfile%``` by default.

```>``` indicates a new prompt.

<img src='images_miniconda/img_020.png' alt='img_020' width='450'/>

The programming language used by the Miniconda Prompt by default is PowerShell. PowerShell is a scripting language that is essentially a terminal based equivalent of Windows Explorer. It is used essentially to navigate around the Operating System. 

PowerShell uses a syntax of the form:

```
command option -p parametervalue1
command option --parametername2 parametervalue2
command option --parametername3
```

Whereas Python uses the following syntax:

```
function(value1, arg2=value2)
```

The Miniconda PowerShell Prompt can be used to invoke Python from the (base) Python environment using:

```
python
```

<img src='images_miniconda/img_021.png' alt='img_021' width='450'/>

Details about the Python version in (base) will display. Notice the prompt change from ```>``` (PowerShell) to ```>>>``` (Python):

<img src='images_miniconda/img_022.png' alt='img_022' width='450'/>

The email package can be imported and the file of its intialisation module viewed using:

```
import email
email.__file__
```

<img src='images_miniconda/img_023.png' alt='img_023' width='450'/>

The datetime module can be imported and its file viewed using:

```
import datetime
datetime.__file__
```

<img src='images_miniconda/img_024.png' alt='img_024' width='450'/>

To exit Python the function:

```
exit()
```

can be used. Notice the prompt returns to ```>``` indicating PowerShell.

<img src='images_miniconda/img_025.png' alt='img_025' width='450'/>


To exit PowerShell use the command:

```
exit
```

<img src='images_miniconda/img_026.png' alt='img_026' width='450'/>

Notice the differences in the two syntaxes as the two different programming languages are used.

Python uses parenthesis to call functions and enclose any function input arguments. PowerShell, instead uses a space between the command and its input arguments. Do not confuse the two programming languages!

Third-party packages are in the site-packages subfolder

<img src='images_miniconda/img_027.png' alt='img_027' width='450'/>

In the (base) Python environment this includes the conda package manager:

<img src='images_miniconda/img_028.png' alt='img_028' width='450'/>

The packages can be viewed by inputting:

```
conda list
```

<img src='images_miniconda/img_029.png' alt='img_029' width='450'/>

<img src='images_miniconda/img_030.png' alt='img_030' width='450'/>

The PowerShell command cls can be used to clear the screen:

```
cls
```

<img src='images_miniconda/img_031.png' alt='img_031' width='450'/>

## Configuring Channels and Solver

The Miniconda PowerShell Prompt opens in %USERPROFILE% by default:

<img src='images_miniconda/img_032.png' alt='img_032' width='450'/>

This location can be viewed in Windows Explorer:

<img src='images_miniconda/img_033.png' alt='img_033' width='450'/>

A .condarc file can be created in this location to configure to conda-forge select conda-forge as the default channel with a strict channel priority and to use the libmamba solver:

```
conda config --add channels conda-forge
conda config --set solver libmamba
conda config --set channel_priority strict
```

<img src='images_miniconda/img_034.png' alt='img_034' width='450'/>

This updates the .condarc file:

<img src='images_miniconda/img_035.png' alt='img_035' width='450'/>

This can be seen by opening it in notepad using:

```
notepad .condarc
```

<img src='images_miniconda/img_036.png' alt='img_036' width='450'/>

This has the form:

```
channels:
   - conda-forge
   - defaults
solver: libmamba
channel_priority: strict
```

<img src='images_miniconda/img_037.png' alt='img_037' width='450'/>

## Updating the (base) Python Distribution

**THIS COMMAND SHOULD NEVER BE USED WITH THE ANACONDA PYTHON DISTRIBUTION AS IT WILL LEAD TO AN UNSTABLE BASE PYTHON ENVIRONMENT EFFECTIVELY PURGING THE DATA SCIENCE DISTRIBUTION.**

The conda package manager in the Anaconda base distribution can be used *as is* to make Python environments. The base Python environment should only be updated via a standalone installer when made available (usually bi-annually by Anaconda).

The PowerShell command conda can be used with option and named parameter --all to update all packages:

```
conda update --all
```

This will update all packages in the base Python environment.

<img src='images_miniconda/img_038.png' alt='img_038' width='450'/>

Notice that this switches the channel from conda to conda-forge for all packages in the base Python environment. Input ```y``` to proceed:

<img src='images_miniconda/img_039.png' alt='img_039' width='450'/>

The base Python environment is now ready:

<img src='images_miniconda/img_040.png' alt='img_040' width='450'/>

And the changes can be seen in Windows Explorer:

<img src='images_miniconda/img_041.png' alt='img_041' width='450'/>

More details can be sen using:

```
conda list
```

<img src='images_miniconda/img_042.png' alt='img_042' width='450'/>

<img src='images_miniconda/img_043.png' alt='img_043' width='450'/>

## Useful PowerShell Commands

The most commonly used PowerShell commands are:

|command|command description|
|---|---|
|cd|Change Directory|
|cls|Clears the Screen|
|mkdir|Make a Directory|
|rmdir|Removes a Directory|
|type|Displays the contents of a text file|

PowerShell can also be used to launch Windows Applications for example:

|command|command description|
|---|---|
|notepad|launches notepad|
|calc|launches calculator|
|mspaint|launches paint|

The Miniconda (base) environment also includes:

|command|command description|
|---|---|
|conda|conda package manager|
|python|Python|
|idle|Launches IDLE|

If other IDEs are installed:

|command|command description|
|---|---|
|jupyter lab|Launches JupyterLab (lab gives the option lab)|
|jupyter|Launches Jupyter Notebook (legacy)|
|spyder|Launches Spyder|
|code|Launches VSCode|

The Miniconda Prompt opens in the environmental variable ```%USERPROFILE%``` by default which in my case is ```C:\Users\Philip```. 

<img src='images_miniconda/img_044.png' alt='img_044' width='450'/>

Documents is a subfolder and the directory can be changed to Documents using:

```
cd Documents
```

<img src='images_miniconda/img_045.png' alt='img_045' width='450'/>

<img src='images_miniconda/img_046.png' alt='img_046' width='450'/>

In PowerShell ```~``` is a shortcut to the Windows Environmental Variable ```$USERPROFILE%```. The ```./``` and ```../``` mean in the same folder as and up a level respectively:

<img src='images_miniconda/img_047.png' alt='img_047' width='450'/>

To clear the screen use:

```
cls
```

<img src='images_miniconda/img_048.png' alt='img_048' width='450'/>

<img src='images_miniconda/img_049.png' alt='img_049' width='450'/>

A new Python script file can be created in PowerShell using:

```
ni script.py
```

<img src='images_miniconda/img_050.png' alt='img_050' width='450'/>

To list all directories and files use:

```
ls
```

<img src='images_miniconda/img_051.png' alt='img_051' width='450'/>

This can be opened in notepad using:

```
notepad script.py
```

<img src='images_miniconda/img_052.png' alt='img_052' width='450'/>

The following Python code can be added to the script file using notepad:

```
print('Hello World!')
```

<img src='images_miniconda/img_053.png' alt='img_053' width='450'/>

The Python script file can be ran using:

```
python script.py
```

<img src='images_miniconda/img_054.png' alt='img_054' width='450'/>

<img src='images_miniconda/img_055.png' alt='img_055' width='450'/>

If the code in the script file is changed to:

```
import time
time.sleep(5000)
```

<img src='images_miniconda/img_056.png' alt='img_056' width='450'/>

The console will hang for 5000 seconds while running the script file:

<img src='images_miniconda/img_057.png' alt='img_057' width='450'/>

The keyboard shortcut ```Ctrl``` + ```c``` is used to close an operation that is running in terminal. 

<img src='images_miniconda/img_058.png' alt='img_058' width='450'/>

To copy from the terminal the keyboard shortcut ```Ctrl``` + ```⇧``` + ```c``` is used. 

To paste to the terminal the keyboard shortcut ```Ctrl``` + ```⇧``` + ```p``` is used.

[Return to Miniconda Installation](./readme.md)