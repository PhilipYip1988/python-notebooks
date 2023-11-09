# The conda Package Manager

The purpose of the conda package manager is to maintain a Python environment. 

## The base Python Environment

In Anaconda the base Python environment is a Python distribution and should not be modified outwith the standard conda images available from Anaconda covered in the Updating Anaconda tutorial. The reason for this is the Python distribution has a large number of packages and changing a package that is a dependency for the other packages will normally result in a number of these packages being removed leading to an unstable Python environment.

To recap the base Python environment is found in:

```
%USERPROFILE%\Anaconda3
```

This contains a python.exe which is the base Python environment:

<img src='images_conda/img_001.png' alt='img_001' width='450'/>

This base Python environment also has a Lib folder which contains the Python standard modules:

<img src='images_conda/img_002.png' alt='img_002' width='450'/>

Such as email (as a subfolder):

<img src='images_conda/img_003.png' alt='img_003' width='450'/>

datetime (as a module):

<img src='images_conda/img_004.png' alt='img_004' width='450'/>

And the site-packages folder which contains the third-party libraries:

<img src='images_conda/img_005.png' alt='img_005' width='450'/>

such as numpy, pandas and matplotlib:

<img src='images_conda/img_006.png' alt='img_006' width='450'/>

## The envs folder

Additional Python environments are found in the environments folder envs:

```
%USERPROFILE%\Anaconda3\envs
```

<img src='images_conda/img_007.png' alt='img_007' width='450'/>

By default there are no additional Python environments and this folder is empty:

<img src='images_conda/img_008.png' alt='img_008' width='450'/>

A Python environment is essentially a sub-installation of Python which is used to install Python alongside a number of third-party Python libraries. 

The use of Python environments for example allows installation of the latest version of each IDE without breaking the functionality of the (base) Python environment.

## conda Package Manager

### Overview

An overview about the conda package manager can be seen by opening up the Anaconda PowerShell Prompt and inputting the PowerShell command:

```
conda
```

<img src='images_conda/img_009.png' alt='img_009' width='450'/>

This gives the following output:

<img src='images_conda/img_010.png' alt='img_010' width='450'/>

|command|description|
|---|---|
|clean|Remove unused packages and caches.|
|compare|Compare packages between conda environments.|
|config|Modify configuration values in .condarc.|
|create|Create a new conda environment from a list of specified packages.|
|doctor|Display a health report for your environment.|
|info|Display information about current conda install.|
|init|Initialize conda for shell interaction.|
|install|Install a list of packages into a specified conda environment.|
|list|List installed packages in a conda environment.|
|notices|Retrieve latest channel notifications.|
|package|Create low-level conda packages.|
|remove|Remove a list of packages from a specified conda environment.|
|rename|Rename an existing environment.|
|run|Run an executable in a conda environment.|
|search|Search for packages and display associated information using the MatchSpec format.|
|update|Update conda packages to the latest compatible version.|
|build|See conda build --help.|
|content-trust|See conda content-trust --help.|
|convert|See conda convert --help.|
|debug|See conda debug --help.|
|develop|See conda develop --help.|
|env|See conda env --help.|
|index|See conda index --help.|
|inspect|See conda inspect --help.|
|metapackage|See conda metapackage --help.|
|pack|See conda pack --help.|
|render|See conda render --help.|
|repo|See conda repo --help.|
|server|See conda server --help.|
|skeleton|See conda skeleton --help.|
|token|See conda token --help.|
|verify|See conda verify --help.|

### Conda Channels

There are two main channels used by the conda package manager:

|channel name|channel description|
|---|---|
|conda-forge|community channel maintained by developers|
|anaconda|channel maintained by the Anaconda company|

The community channel is maintained directly by Python developers. A subset of the packages from the community channel are further tested by the Anaconda company for use in the Anaconda Python distribution.

Therefore popular packages in the community channel are usually more up to date with respect to packages in the conda channel. And less popular packages in the community channel are unlikely to be in the anaconda channel.

A Python environment is normally unstable if it uses mixed channels and most custom end-user Python environments will only use packages in the conda-forge channel.

### Create

A Python environment can be created using the syntax:

```
conda create -n notbase
```

where "notbase" is the environment name. Input ```y``` to proceed:

<img src='images_conda/img_017.png' alt='img_017' width='450'/>

Notice in envs, the notbase subfolder is created:

<img src='images_conda/img_018.png' alt='img_018' width='450'/>

### Activate

The ```conda activate``` command only works in the Anaconda PowerShell Prompt and will not work in the Windows Terminal which instead uses the Python environment specified in the Windows Environmental Variables Path.

Once the Python environment is created it can be activated (selected) using:

```
conda activate notbase
```

<img src='images_conda/img_019.png' alt='img_019' width='450'/>

Once activated, any changes made using the conda package manager in the Anaconda PowerShell Prompt will apply to this Python environment instead of base. The prompt now has the (notbase) prefix indicates the (notbase) Python is selected:

<img src='images_conda/img_020.png' alt='img_020' width='450'/>

If the Anaconda PowerShell Prompt is closed and reopened, the default Python environment base will be selected. The Python environment notbase will have to be activated.

The conda activate comand does not change Python environment in the Windows Terminal because the Windows Terminal always uses the Python environment listed in the Windows Environmental Variables path.

### Search

The conda-forge community channel can be searched for a package in this case the package "python" using:

```
conda search -c conda-forge python
```

<img src='images_conda/img_021.png' alt='img_021' width='450'/>

Notice each Python has a version, a build number and a channel:

<img src='images_conda/img_022.png' alt='img_022' width='450'/>

Specifying the channel is not necessary as the .condarc file already specifies use of the conda-forge channel however it is good practice to specify the channel. The package ipython can be searched for using:

```
conda search -c conda-forge ipython
```

<img src='images_conda/img_023.png' alt='img_023' width='450'/>

<img src='images_conda/img_024.png' alt='img_024' width='450'/>

### Install

Multiple packages can be installed using the syntax:

```
conda install -c conda-forge python ipython
```

<img src='images_conda/img_025.png' alt='img_025' width='450'/>

Details about the packages to be installed are listed:

<img src='images_conda/img_026.png' alt='img_026' width='450'/>

Input ```y``` in order to proceed:

<img src='images_conda/img_027.png' alt='img_027' width='450'/>

<img src='images_conda/img_028.png' alt='img_028' width='450'/>

Notice the Python environment notbase, now has its own python.exe:

<img src='images_conda/img_029.png' alt='img_029' width='450'/>

Its own Lib subfolder:

<img src='images_conda/img_030.png' alt='img_030' width='450'/>

This has the standard modules such as email (which is a multi-file module in a folder):

<img src='images_conda/img_031.png' alt='img_031' width='450'/>

datetime which is a single module:

<img src='images_conda/img_032.png' alt='img_032' width='450'/>

Third party libraries are in the site-packages subfolder:

<img src='images_conda/img_033.png' alt='img_033' width='450'/>

This has ipython and some of its dependencies such as the matplotlib backend matplotlib_inline:

<img src='images_conda/img_034.png' alt='img_034' width='450'/>

The data science libraries numpy, pandas and matplotlib (the full library) as they are not installed as they are not dependencies.

### Remove

The command remove can be used to remove an installed package:

```
conda remove python ipython
```

<img src='images_conda/img_035.png' alt='img_035' width='450'/>

If other packages rely on the packages being removed as dependencies, they will be removed. Since Python itself is being removed, and all packages are in turn dependent on Python, they will all be removed:

<img src='images_conda/img_036.png' alt='img_036' width='450'/>

<img src='images_conda/img_037.png' alt='img_037' width='450'/>

Input ```y``` to proceed with the changes. The changes will then be made:

<img src='images_conda/img_038.png' alt='img_038' width='450'/>

Notice the python.exe is gone alongside the Lib subfolder.

### Install Specific Package Version

During installation version numbers can be specified:

```
conda install -c conda-forge python=X.Y.Z
```

Where X is the major number, Y is the minor version number and Z is the patch number. For example:

```
conda install -c conda-forge python=3.11.3
```

In the previous output when conda search was used. Each Python version 3.11.1 onwards had a build number of h628c8c_0. This can also be speciifed during installation:

```
conda install -c conda-forge python=3.11.3=h2628c8c_0_cpython
```

Some packages for example ipython have multiple variants that have the same version number, for example ipython has 3 variants that are at version 8.14.0 on the conda-forge channel. These each have unique build numbers pyh08f2357_0, py41d4057_0 and pyhd1c38e8_0 as seen in the previous output when conda search was used. Normally this is because there is a slightly seperate variant for different minor Python versions e.g. Python 3.11, 3.10 and 3.9.

A specific version of python and ipython can be installed:

```
conda install -c conda-forge python=3.11.3=h2628c8c_0_cpython ipython=8.14.0=pyh08f2357_0
```

<img src='images_conda/img_040.png' alt='img_040' width='450'/>

Details about the other packages installed will display. Input ```y``` in order to install the packages:

<img src='images_conda/img_041.png' alt='img_041' width='450'/>

The changes will be made:

<img src='images_conda/img_042.png' alt='img_042' width='450'/>

### Update

A package can be updated to the latest version using:

```
conda update -c conda-forge python
```

<img src='images_conda/img_043.png' alt='img_043' width='450'/>

Since an older version of Python was installed, the newer version 3.11.4 is available. To install it input ```y```:

<img src='images_conda/img_044.png' alt='img_044' width='450'/>

Alternatively all packages in the environment can be updated using:

```
conda update -c conda-forge --all
```

<img src='images_conda/img_045.png' alt='img_045' width='450'/>

Note sometimes some packages may be downgraded in order to upgrade some other packages. Sometimes packages require an older version of another package as a dependency. To install the updates input ```y```:

<img src='images_conda/img_046.png' alt='img_046' width='450'/>

The updates are now installed:

<img src='images_conda/img_047.png' alt='img_047' width='450'/>

### List

Packages can be listed in the Python environment using:

```
conda list
```

<img src='images_conda/img_048.png' alt='img_048' width='450'/>

The conda list command can be used with the option --revisions:

```
conda list --revision
```

<img src='images_conda/img_049.png' alt='img_049' width='450'/>

### Install Revision

The conda install command can be used with the option --revisions and assigned to a revision number. For example, the revision 3 before the update can be reverted to using:

```
conda install -c conda-forge --revision=3
```

<img src='images_conda/img_050.png' alt='img_050' width='450'/>

Details about the changes will be provided including the downgrades:

<img src='images_conda/img_051.png' alt='img_051' width='450'/>

Input ```y``` in order to proceed and the proposed downgrade will be implemented:

<img src='images_conda/img_052.png' alt='img_052' width='450'/>

### Env Export

The currently activated Python environment can also be exported to a **y**et another **m**arkdown **l**anguage yml file:

```
conda env export > Documents\notbase.yml
```

<img src='images_conda/img_053.png' alt='img_053' width='450'/>

This creates a notbase.yml file in Documents:

<img src='images_conda/img_054.png' alt='img_054' width='450'/>

This can be opened in notepad:

<img src='images_conda/img_055.png' alt='img_055' width='450'/>

This is a very small file which can be shared on GitHub or emailed.

### Env Create

An environment can be created from a yml file for example the notbase.yml in the Documents folder using:

```
conda env create -n notbase2 -f Documents\notbase.yml
```

Note this is done with the base Python environment activated.

<img src='images_conda/img_056.png' alt='img_056' width='450'/>

The environment is created and can later be activated:

<img src='images_conda/img_057.png' alt='img_057' width='450'/>

The name of the new environment notbase2 displays as a subfolder in envs:

<img src='images_conda/img_058.png' alt='img_058' width='450'/>

### Env Remove

An environment can be removed using the command:

```
conda env remove -n notbase
```

Note this is done with the base Python environment activated as a Python environment cannot be removed if it is activated:

<img src='images_conda/img_059.png' alt='img_059' width='450'/>

The operation will proceed:

<img src='images_conda/img_060.png' alt='img_060' width='450'/>

The folder notbase will be removed in envs:

<img src='images_conda/img_061.png' alt='img_061' width='450'/>

### rename

A Python environment can be renamed by using the command:

```
conda rename -n notbase2 notbase
```

notbase2 is the original name and notbase is the new name. Note this is done with the base Python environment activated as a Python environment cannot be renamed if it is activated:

<img src='images_conda/img_062.png' alt='img_062' width='450'/>

The notbase folder in the envs folder is now renamed notbase2:

<img src='images_conda/img_063.png' alt='img_063' width='450'/>

### Env List

To list Python environments use:

```
conda env list
```

<img src='images_conda/img_064.png' alt='img_064' width='450'/>

### Clean

A backup of all previously downloaded versions is available which can occupy a large amount of disk space. These can be cleaned using:

```
conda clean --all
```

<img src='images_conda/img_065.png' alt='img_065' width='450'/>

## Python Environments for IDEs

Previously the commands create and install were used seperately and when the list of revision was examined revision 0 had no packages. The conda create command can be used to list a series of packages to be installed when creating a Python Environment. This command will be used to create a Python Environment suitable for the latest version of each Python IDE discussed.

### IDLE Python Environment

```
conda create -n idle -c conda-forge python cython seaborn scikit-learn sympy openpyxl xlrd xlsxwriter lxml sqlalchemy tabulate
```

Installing seaborn will install numpy, pandas and matplotlib as these are dependencies for seaborn.

openpyxl, xlrd, xlsxwriter, lxml, sqlalchemy and tabulate are file format convertors used for pandas.

IDLE should be launched from its own Python environment using the Anaconda PowerShell Prompt.

### Thonny Python Environment

```
conda create -n thonny -c conda-forge python cython seaborn scikit-learn sympy openpyxl xlrd xlsxwriter lxml sqlalchemy tabulate
```

Installing seaborn will install numpy, pandas and matplotlib as these are dependencies for seaborn.

openpyxl, xlrd, xlsxwriter, lxml, sqlalchemy and tabulate are file format convertors used for pandas.

The Python interpretter needs to be selected in Thonny.

### Spyder Python Environment

#### Spyder 5

```
conda create -n spyder -c conda-forge python spyder cython seaborn scikit-learn sympy openpyxl xlrd xlsxwriter lxml sqlalchemy tabulate pyqt
```

#### Spyder 6 pre-release:

Spyder 6 pre-release can be installed in a new conda environment.

Create a new Python environment with Python 3.11:

```
conda create -n spyder -c conda-forge python=3.11
```

Activate it:

```
conda activate spyder
```

Install Spyder using the conda-forge, spyder_dev and spyder_kernels_rc channels see latest Advance Installation instructions. Since this is undergoing rapid development, see [Spyder Releases: Advanced Installation](https://github.com/spyder-ide/spyder/releases) for more details and the latest version numbers:

```
conda install -c conda-forge/label/spyder_dev -c conda-forge/label/spyder_kernels_rc -c conda-forge spyder=6.0.0a2
```

Install the data science libraries:

```
conda install -c conda-forge cython seaborn scikit-learn sympy openpyxl xlrd xlsxwriter lxml sqlalchemy tabulate pyqt
```

Installing seaborn will install numpy, pandas and matplotlib as these are dependencies for seaborn.

openpyxl, xlrd, xlsxwriter, lxml, sqlalchemy and tabulate are file format convertors used for pandas.

pyqt is required for an interactive matplotlib plotting backend.

Spyder should be launched from its own Python environment using the Anaconda PowerShell Prompt or its own Start Menu Shortcut.

### JupyterLab Python Environment

```
conda create -n jupyterlab -c conda-forge python jupyterlab cython seaborn scikit-learn sympy openpyxl xlrd xlsxwriter lxml sqlalchemy tabulate nodejs ipywidgets plotly jupyterlab-variableinspector ipympl pyqt
```

Installing seaborn will install numpy, pandas and matplotlib as these are dependencies for seaborn.

openpyxl, xlrd, xlsxwriter, lxml, sqlalchemy and tabulate are file format convertors used for pandas.

nodejs allows installaiton of JupyterLab extensions.ipywidgets and plotly can be used to create widgets and plots using Python code, under the hood JavaScript is used to display these in the browser. The variableinspector gives a variable inspector, similar in functionality to variables in Thonny.

pyqt and ipympl are required for an interactive matplotlib plotting backends.

JupyterLab should be launched from its own Python environment using the Anaconda PowerShell Prompt.

### JupyterLab with R

Recall that Jupyter is a loose acronym for Julia Python and R. To install R activate the jupyterlab Python environment created above using:

```
conda activate jupyterlab
```

The R Kernel (r-irkernel) and R language server protocol for JupyterLab (jupyter-lsp-r) required for R code completions can be installed from conda-forge alongside other common R libraries such as the Tidyverse packages for Data Science (r-tidyverse) can be installed using:

```
conda install -c conda-forge r-irkernel jupyter-lsp-r r-tidyverse r-ggthemes r-palmerpenguins r-writexl
```

This will set it up for use with R. An R option will display under Notebook and Console allowing the R programming language to be ran in an interactive notebook or console instead of Python.

Details about all R packages are available on the CRAN website, for example the readxl package [writexl cran](https://cran.r-project.org/web/packages/writexl/index.html). 

Because the conda package manager is used, the package should be installed using conda. The package is normally found on conda-forge with a r- prefix. For example [r-writexl conda-forge](https://anaconda.org/conda-forge/r-writexl)

Details about the tidyverse packages are available here[tidyverse](https://www.tidyverse.org/)

### VSCode Python Environment

Install VSCode using WinGet:

```
WinGet install Microsoft.VisualStudioCode
```

Create a Python environment for VSCode:

```
conda create -n vscode -c conda-forge python notebook cython seaborn scikit-learn sympy openpyxl xlrd xlsxwriter lxml sqlalchemy tabulate nodejs ipywidgets plotly ipympl pyqt autopep8 black
```

Installing seaborn will install numpy, pandas and matplotlib as these are dependencies for seaborn.

openpyxl, xlrd, xlsxwriter, lxml, sqlalchemy and tabulate are file format convertors used for pandas.

nodejs allows installation of JupyterLab extensions.ipywidgets and plotly can be used to create widgets and plots using Python code, under the hood JavaScript is used to display these in VSCode which behaves like a browser. 

pyqt and ipympl are required for an interactive matplotlib plotting backends. 

Install the Python, Jupyter, autopep8, isort and black extensions in VSCode.

The Python interpretter needs to be selected in VSCode.

### PyCharm Python Environment

Install PyCharm using WinGet:

```
WinGet install JetBrains.PyCharm.Professional
```

Create a Python environment for PyCharm:

```
conda create -n pycharm -c conda-forge python cython seaborn scikit-learn sympy openpyxl xlrd xlsxwriter lxml sqlalchemy tabulate pyqt autopep8 black
```

Installing seaborn will install numpy, pandas and matplotlib as these are dependencies for seaborn.

openpyxl, xlrd, xlsxwriter, lxml, sqlalchemy and tabulate are file format convertors used for pandas.

pyqt is required for an interactive matplotlib plotting backends.

The Python interpretter needs to be selected in PyCharm.

## Config and .condarc file (optional)

The ```conda config``` command is used to create a ```.condarc``` file which can be used to change the settings used by the conda package manager... 

When the ```conda``` package manager is used in Anaconda a ```.condarc``` file is created in ```%USERPROFILE%```:

<img src='images_conda/img_072.png' alt='img_072' width='450'/>

with the following content:

```
channels:
  - defaults
```

<img src='images_conda/img_073.png' alt='img_073' width='450'/>

For Anaconda or Miniconda ```defaults``` mean the ```anaconda``` channel is selected. This is the channel maintained by the Anaconda company.

The community channel ```conda-forge``` is more commonly used for custom Python environments. To change the channel used to ```conda-forge``` the following commands can be used:

```
conda config --remove channels defaults
conda config --add channels conda-forge
```

<img src='images_conda/img_074.png' alt='img_074' width='450'/>

This updates the ```.condarc``` to the following:

<img src='images_conda/img_075.png' alt='img_075' width='450'/>

```
channels:
  - conda-forge
```

Note that a ```.condarc``` with a default channel of ```conda-forge``` should not be used when updating the Anaconda base Python environment as it will result in an unstable configuration. Miniconda does not have the same issue as there are a small number of packages in the Miniconda base Python environment.

## Initialising the Windows Terminal (optional)

The Windows Environmental Variable Path has the following 5 entries:

```
%USERPROFILE%\Anaconda3
%USERPROFILE%\Anaconda3\Library\mingw-w64\bin
%USERPROFILE%\Anaconda3\Libraryusr\bin
%USERPROFILE%\Anaconda3\Library\bin
%USERPROFILE%\Anaconda3\Scripts
```

This is the location which the Windows Terminal looks for the ```python.exe``` and other applications such as the ```spyder.exe``` and ```jupyter-lab.exe```.

The Anaconda PowerShell Prompt is essentially the Windows Terminal that runs an additional conda activation script that allows change of Python environments:

```
%windir%\System32\WindowsPowerShell\v1.0\powershell.exe -ExecutionPolicy ByPass -NoExit -Command "& 'C:\Users\Phili\anaconda3\shell\condabin\conda-hook.ps1' ; conda activate 'C:\Users\Phili\anaconda3' "
```

Notice that this has to bypass ExecutionPolicy to allow the activation script to run. 

The Windows Terminal can be initialised directly by using a modified PowerShell Profile that runs the conda activation script. Unfortunately to use this modified profile, the PowerShell Script Execution Policy needs to be set to Unrestricted and this therefore lowers the base security of the Windows OS making it more vulnerable to other malicious scripts. This security Execution Policy is the main reason there is a seperate Anaconda PowerShell Prompt on Windows instead of direct integration with the Windows Terminal.

To initialise Anaconda in PowerShell open up the Windows Terminal and input:

```
Anaconda3\Scripts\conda.exe init powershell
```

Once this is done, there is an error message any time the Windows Terminal is opened stating the PowerShell Profile cannot be loaded because running scripts is disabled on this system:

In order to use this PowerShell Profile, the Script Execution Policy needs to be set to Unrestricted, recall that this lowers the base security of your system leaving it open to other poptentially malicious scripts.

To change this setting the Terminal (Admin) needs to be used. Input:

```
Set-ExecutionPolicy -ExecutionPolicy Unrestricted
```

Close any Terminals. Now the Windows Terminal (User) can be used and the conda environment shows:

The Windows Terminal can be used in an identical manner to the Anaconda PowerShell Prompt and any Python IDEs that use the Windows Terminal will use it with an activation script making it equivalent to using the Anaconda PowerShell Prompt.

To undo the initialisation, the following command can be used:

```
Anaconda3\Scripts\conda.exe init powershell --reverse
```

To revert to the default Execution Policy, the following command can be used. Recall that administrative privileges
 are required so use Windows Terminal (Admin):

```
Set-ExecutionPolicy -ExecutionPolicy Default
```

[Return to Anaconda Tutorial](./readme.md)
