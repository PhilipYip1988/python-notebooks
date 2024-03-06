# Installing Anaconda

## Download Links

The latest Anaconda and Miniconda installer can be downloaded from:

* [Anaconda](https://www.anaconda.com/download)
* [Miniconda](https://docs.anaconda.com/free/miniconda/miniconda-install/)

## Anaconda vs Miniconda 

Anaconda is a Python distribution that has a base Python environment that is designed to be used *as is*. The base Python environment has the conda package manager that can be used to create a separate Python environment (subinstallation of Python) for a custom configuration of packages. 

Miniconda is a bootstrap version of Anaconda, that only contains the conda package manager and can likewise be used to create Python environments.

When only custom Python environments are being used, Miniconda should be used in preference to Anaconda.

### Anaconda Python Distribution

The Anaconda Python distribution comes with its own base Python environment that contains:

* Python
* Python Standard Libraries
* The conda Package Manager
* The Anaconda Navigator
* Third Party Libraries:
  * numpy
  * pandas
  * matplotlib
  * seaborn
  * plotly
  * pillow
  * scikit-learn
  * scikit-image
  * ⁝
* Third-party IDEs:
  * Spyder
  * Jupyter
    * JupyterLab
    * Jupyter Notebook
    * Jupyter QTConsole
    * Jupyter Console
* Third-party formatters:
  * autopep8
  * isort
  * black

### Miniconda

Miniconda is a stripped down version of Anaconda containing only:

* Python
* Python Standard Libraries
* The conda Package Manager

## conda

Anaconda and Miniconda have the conda package manager which should be used in preference to the native Python package manager pip. 

* conda
* ~~pip~~

pip is strictly a package manager for Python packages. However many datascience projects under the hood, use code that is written in C++ for performance gains. The conda package manager manages both the Python and non-Python dependencies. The conda package manager has also been written in C++ for increased performance and reliability. This was separately developed as mamba and the conda package manager uses the libmamba (C++) solver by default.

The conda package manager uses two channels:

* conda-forge
* anaconda

The first channel community forge is the community channel and has the largest number of packages available.

The second channel is the channel maintained by Anaconda Inc. Anaconda Inc test packages for compatibility with the Anaconda Python Distribution. 

As a consequence the latest version of a package available on the anaconda channel may be dated with respect to the package on the conda-forge channel as it takes Anaconda Inc some time to test packages. Moreover Anaconda Inc only test the most commonly used datascience libraries and therefore more niche packages will only be available on conda-forge.

In the Anaconda base environment the following commands should never be used:

* ~~pip install package~~
* ~~conda install conda-forge::package~~
* ~~conda install -c conda-forge package~~

This is because use of multiple package managers and use of multiple channels will make the Anaconda base Python environment unstable.

Only packages available from the anaconda channel should be installed in base:

* conda install anaconda::package
* conda install -c anaconda package

The base Python environment is normally used *as is* and instead a custom Python environment is used to install a subinstallation of Python and custom packages from the conda-forge community channel.

## Removing Old Installations

Anaconda should be installed on a Windows 11 PC that has no previous Python installations. 

If Python installations are present they should be uninstalled. Note that uninstallation leaves behind a large number of configuration files that often results in a problematic setting that persists after a reinstall. For best results it is recommended to purge these configuration files. For more details see [Uninstall](./uninstall.md).


## Installation

Run the graphical user interface installer:

<img src='images_install/img_001.png' alt='img_001' width='450'/>

Select Next:

<img src='images_install/img_002.png' alt='img_002' width='450'/>

Select I Agree:

<img src='images_install/img_003.png' alt='img_003' width='450'/>

Select Just Me and then Next:

<img src='images_install/img_004.png' alt='img_004' width='450'/>

Install in the default location:

```powershell
%USERPROFILE%\anaconda3
%USERPROFILE%\miniconda3
```

Select Next:

<img src='images_install/img_005.png' alt='img_005' width='450'/>


Select Install:

<img src='images_install/img_006.png' alt='img_006' width='450'/>

Select Next:

<img src='images_install/img_007.png' alt='img_007' width='450'/>

Select Next:

<img src='images_install/img_008.png' alt='img_008' width='450'/>

Select Finish:

<img src='images_install/img_009.png' alt='img_009' width='450'/>

Select Start → All Apps:

<img src='images_install/img_010.png' alt='img_010' width='450'/>

There will be a Start Menu shortcut to the Anaconda or Miniconda folder:

<img src='images_install/img_011.png' alt='img_011' width='450'/>

The Start Menu shortcuts contains shortcut to two shells initialised with the conda package manager:

* Anaconda PowerShell Prompt 
* Anaconda (CMD) Prompt 

The newer shell PowerShell should be used in preference to the older shell CMD.

## Updating Anaconda

The conda package manager should be updated using the command:

```powershell
conda update conda
```

For Anaconda, updating the conda package manager will also update other components in the Anaconda Python distribution:

<img src='images_install/img_012.png' alt='img_012' width='450'/>

For Anaconda, the Anaconda Navigator should also be updated:

```powershell
conda update anaconda-navigator
```

<img src='images_install/img_013.png' alt='img_013' width='450'/>

Input ```y``` to proceed with the changes:

<img src='images_install/img_014.png' alt='img_014' width='450'/>

## Windows Environmental Variables Path

The option to Add Anaconda/Miniconda to the Windows Environmental Variables path is disabled by default and **not recommended**. 

Instead the Anaconda PowerShell Prompt is used in preference to the Windows Terminal as it has support for activation of other Python environments:

<img src='images_install/img_015.png' alt='img_015' width='450'/>

The Windows Terminal by default looks for applications in the locations specified in the Windows Environment Path. If the path is updated to include these, the Windows Terminal will only have access to applications in the base Python environment.

The Windows Environmental Variables path can be viewed by right clicking the Start Button and selecting System:

<img src='images_install/img_016.png' alt='img_016' width='200'/>

Then Advanced System Options:

<img src='images_install/img_017.png' alt='img_017' width='450'/>

Then select the Advanced tab and Environmental Variables:

<img src='images_install/img_018.png' alt='img_018' width='450'/>

Then Edit the Path:

<img src='images_install/img_019.png' alt='img_019' width='450'/>

The default entry is:

```powershell
%USERPROFILE%\AppData\Local\Microsoft\WindowsApps
```

If Anaconda is added to the path the following 5 entries will be added:

```powershell
%USERPROFILE%\anaconda3
%USERPROFILE%\anaconda3\Library\mingw-w64\bin
%USERPROFILE%\anaconda3\Library\usr\bin
%USERPROFILE%\anaconda3\Library\bin
%USERPROFILE%\anaconda3\Scripts
```

If Miniconda is added to the path the following 5 entries will be added:

```powershell
%USERPROFILE%\Miniconda3
%USERPROFILE%\Miniconda3\Library\mingw-w64\bin
%USERPROFILE%\Miniconda3\Library\usr\bin
%USERPROFILE%\Miniconda3\Library\bin
%USERPROFILE%\Miniconda3\Scripts
```

<img src='images_install/img_020.png' alt='img_020' width='450'/>

## Initialising the Windows Terminal

It is generally recommended to use the Anaconda PowerShell Prompt over the Windows Terminal where possible, however some IDEs such as VSCode use the Windows Terminal and will display errors unless the Windows Terminal has been initialised.

To initialise the Windows Terminal, right click the Start Button and select Terminal (Admin):

<img src='images_install/img_021.png' alt='img_021' width='200'/>

Input the following:

```powershell
Set-ExecutionPolicy RemoteSigned
```

<img src='images_install/img_022.png' alt='img_022' width='450'/>

For Anaconda input:

```powershell
anaconda3\Scripts\conda init powershell
```

For Miniconda input:

```powershell
miniconda3\Scripts\conda init powershell
```

<img src='images_install/img_023.png' alt='img_023' width='450'/>

The following changes will be made:

<img src='images_install/img_024.png' alt='img_024' width='450'/>

Any shells open should now be closed. Right click the Start Button and select Terminal:

<img src='images_install/img_025.png' alt='img_025' width='200'/>

All shells now have the (base) prefix and the conda activate command can be used to switch between Python environments:

<img src='images_install/img_026.png' alt='img_026' width='450'/>

Anaconda or Miniconda is now installed, updated and initialised.

## MikTeX Installation

A number of the datascience packages such as nbconvert and matplotlib can use TeX. On Windows MikTex should be installed. MikTeX can be downloaded from:

* [MikTeX](https://miktex.org/download)

Launch the graphical user interface setup:

<img src='images_install/img_027.png' alt='img_027' width='450'/>

Accept the License Agreement and select Next:

<img src='images_install/img_028.png' alt='img_028' width='450'/>

Select Install MikTeX only for me and then Next:

<img src='images_install/img_029.png' alt='img_029' width='450'/>

Use the default install location and select Next:

<img src='images_install/img_030.png' alt='img_030' width='450'/>

Select Next:

<img src='images_install/img_031.png' alt='img_031' width='450'/>

Select Start:

<img src='images_install/img_032.png' alt='img_032' width='450'/>

Select Next:

<img src='images_install/img_033.png' alt='img_033' width='450'/>

Select Close:

<img src='images_install/img_034.png' alt='img_034' width='450'/>

Launch the MikTeX Console:

<img src='images_install/img_035.png' alt='img_035' width='450'/>

Select the Updates tab, the Check for Updates:

<img src='images_install/img_036.png' alt='img_036' width='450'/>

Select Update Now:

<img src='images_install/img_037.png' alt='img_037' width='450'/>

Close MikTex when prompted:

<img src='images_install/img_038.png' alt='img_038' width='450'/>

Launch the MikTex-Console.exe and go to the packages tab. Sort by Installed On. Select all packages that do not have an Installed On date, then select +:

<img src='images_install/img_064.png' alt='img_064' width='450'/>

Select OK to install the packages:

<img src='images_install/img_065.png' alt='img_065' width='450'/>

Note unfortunately selecting all the packages (inclusive of the installed packages) will grey out the + button.

## Programs

If the following location is input into the address bar:

```powershell
%USERPROFILE%
```

<img src='images_install/img_039.png' alt='img_039' width='450'/>

Then the anaconda3 or miniconda3 can be selected:

<img src='images_install/img_040.png' alt='img_040' width='450'/>

### python

These folders contain a python.exe and this can be run in the terminal using:

```powershell
~\anaconda3\python.exe
```

<img src='images_install/img_041.png' alt='img_041' width='450'/>

When the base Python environment is activated, the Windows Terminal will look in the location ```~\anaconda3``` for a program by default and so this can also be launched using:

```powershell
python.exe
```

And for convenience the .exe does not need to be specified:

```powershell
python
```

### conda

The Scripts folder contains a number of additional programs:

<img src='images_install/img_042.png' alt='img_042' width='450'/>

Such as the conda.exe which can be launched using:

```python
~\anaconda3\Scripts\conda.exe
conda.exe
conda
```

<img src='images_install/img_043.png' alt='img_043' width='450'/>

This will display the list of commands which can be used by the application:

```
(base) PS ~> conda
usage: conda-script.py [-h] [-v] [--no-plugins] [-V] COMMAND ...

conda is a tool for managing and deploying applications, environments and packages.

options:
  -h, --help          Show this help message and exit.
  -v, --verbose       Can be used multiple times. Once for
                      detailed output, twice for INFO logging,
                      thrice for DEBUG logging, four times for
                      TRACE logging.
  --no-plugins        Disable all plugins that are not built
                      into conda.
  -V, --version       Show the conda version number and exit.

commands:
  The following built-in and plugins subcommands are available.

  COMMAND
    activate          Activate a conda environment.
    build             Build conda packages from a conda recipe.
    clean             Remove unused packages and caches.
    compare           Compare packages between conda
                      environments.
    config            Modify configuration values in .condarc.
    content-trust     Signing and verification tools for Conda
    convert           Convert pure Python packages to other
                      platforms (a.k.a., subdirs).
    create            Create a new conda environment from a list
                      of specified packages.
    deactivate        Deactivate the current active conda
                      environment.
    debug             Debug the build or test phases of conda
                      recipes.
    develop           Install a Python package in 'development
                      mode'. Similar to `pip install
                      --editable`.
    doctor            Display a health report for your
                      environment.
    index             Update package index metadata files.
    info              Display information about current conda
                      install.
    init              Initialize conda for shell interaction.
    inspect           Tools for inspecting conda packages.
    install           Install a list of packages into a
                      specified conda environment.
    list              List installed packages in a conda
                      environment.
    metapackage       Specialty tool for generating conda
                      metapackage.
    notices           Retrieve latest channel notifications.
    pack              See `conda pack --help`.
    package           Create low-level conda packages.
                      (EXPERIMENTAL)
    remove (uninstall)
                      Remove a list of packages from a specified
                      conda environment.
    rename            Rename an existing environment.
    render            Expand a conda recipe into a platform-
                      specific recipe.
    repo              See `conda repo --help`.
    repoquery         Advanced search for repodata.
    run               Run an executable in a conda environment.
    search            Search for packages and display associated
                      information using the MatchSpec format.
    server            See `conda server --help`.
    skeleton          Generate boilerplate conda recipes.
    token             See `conda token --help`.
    update (upgrade)  Update conda packages to the latest
                      compatible version.
    verify            See `conda verify --help`.
(base) PS ~>
```

### Anaconda Navigator

The Anaconda Python distribution will also have the anaconda-navigator.exe:

<img src='images_install/img_044.png' alt='img_044' width='450'/>

```powershell
~\anaconda3\scripts\anaconda-navigator.exe
anaconda-navigator.exe
anaconda-navigator
```

The Anaconda Navigator has an Enable High DPI Setting which unfortunately often does not work very well:

<img src='images_install/img_045.png' alt='img_045' width='450'/>

When File → Preferences are selected:

<img src='images_install/img_046.png' alt='img_046' width='450'/>

The settings box appears offscreen and therefore the settings cannot be applied:

<img src='images_install/img_047.png' alt='img_047' width='450'/>

Since the GUI cannot be used correctly to change the settings. The file anaconda-navigator.ini in the location:

```
%APPDATA%\.anaconda\navigator
```

can be modified in notepad:

<img src='images_install/img_049.png' alt='img_049' width='450'/>

The line:

```python
enable_high_dpi_scaling = False
```

Can be changed to:

```python
enable_high_dpi_scaling = True
```
<img src='images_install/img_050.png' alt='img_050' width='450'/>

The Anaconda Navigator should now display correctly:

<img src='images_install/img_051.png' alt='img_051' width='450'/>

The Anaconda Navigator displays additional shortcuts to IDEs installed in the Anaconda base Python environment.

### IPython

Interactive Python is an improved Python shell:

```powershell
~\anaconda3\scripts\ipython.exe
ipython.exe
ipython
```

<img src='images_install/img_052.png' alt='img_052' width='450'/>

Pressing ↹ after a prefix will display a list of identifiers:

<img src='images_install/img_053.png' alt='img_053' width='450'/>

There are Python commands and IPython Magics (commands beginning with %). The ? command is also recognised and can be used to print a docstring:

<img src='images_install/img_054.png' alt='img_054' width='450'/>

### Jupyter

Jupyter is an acronym for Python, Julia and R. 

<img src='images_install/img_055.png' alt='img_055' width='450'/>

The jupyter program can be used with a command option which can be used to specify the program. For example:

```powershell
~\anaconda3\scripts\jupyter.exe lab
jupyter.exe lab
jupyter lab
```

However it is more typical to use the program directly:

```powershell
~\anaconda3\scripts\jupyter-lab.exe
jupyter-lab.exe
jupyter-lab
```

<img src='images_install/img_056.png' alt='img_056' width='450'/>

The main programs are:

```powershell
jupyter-console
jupyter-qtconsole
jupyter-notebook
jupyter-lab
```

jupyter-console.exe is very similar to ipython.exe, the only difference is it can be used to switch between a Python, Julia or R kernel (Python is the default so by default both consoles behave identically).

jupyter-qtconsole.exe is rewritten using QT and therefore has additional UI elements such as the ability to view docstrings as popup balloons:

<img src='images_install/img_057.png' alt='img_057' width='450'/>

And graphics can be nested into the QT console, which isn't supported by the non-QT console:

<img src='images_install/img_058.png' alt='img_058' width='450'/>

jupyter-lab.exe uses nodejs and a server is run in the terminal:

<img src='images_install/img_059.png' alt='img_059' width='450'/>

And the visual elements display in a browser. JupyterLab has a file explorer and a launcher which can be used to create a new text file, markdown file, python script or interactive python notebook:

<img src='images_install/img_060.png' alt='img_060' width='450'/>

The interactive Python notebook consists of ipython cells. Pressing ↹ will display a list of identifiers:

<img src='images_install/img_061.png' alt='img_061' width='450'/>

Pressing ⇧ and ↹ will display a docstring as a popup balloon:

<img src='images_install/img_062.png' alt='img_062' width='450'/>

Plots are by default displayed as inline. If MikTeX has been setup properly, the following code should run without any errors:

```python
import numpy as np
import matplotlib.pyplot as plt
x = np.array([0, 1, 2, 3, 4])
y = 2 * x
plt.plot(x, y)
plt.xlabel(r'$x$', usetex=True)
```

<img src='images_install/img_063.png' alt='img_063' width='450'/>

Note when JupyterLab is closed in the browser, the server will still be running in the terminal. Press Ctrl + c to close the server, this will take you to a new prompt:

<img src='images_install/img_066.png' alt='img_066' width='450'/>

The program jupyter-notebook.exe is a simplified version of jupyter-lab.exe and works in a similar manner for a notebook.

### Spyder

The program spyder.exe is another IDE preinstalled by Anaconda and can be launched using:

```powershell
~\anaconda3\scripts\spyder.exe
spyder.exe
spyder
```

<img src='images_install/img_067.png' alt='img_067' width='450'/>

Spyder has a user interface similar to Matlab or RStudio and has a script editor, ipython console and variable explorer:

<img src='images_install/img_068.png' alt='img_068' width='450'/>

[Return to Python Tutorials](../../readme.md)