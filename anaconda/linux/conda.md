# The conda Package Manager

The purpose of the conda package manager is to maintain a Python environment. 

## The base Python Environment

In Anaconda the base Python environment is a Python distribution and should not be modified outwith the standard conda images available from Anaconda covered in the Updating Anaconda tutorial. The reason for this is the Python distribution has a large number of packages and changing a package that is a dependency for the other packages will normally result in a number of these packages being removed leading to an unstable Python environment.

To recap the base Python environment is found in:

```
~/anaconda3
```

<img src='images_conda/img_001.png' alt='img_001' width='450'/>

There is a bin subfolder and a lib subfolder:

```
~/anaconda3/bin
~/anaconda3/lib
```

<img src='images_conda/img_002.png' alt='img_002' width='450'/>

The bin folder contains the python3.11 program which has a python and python3 alias:

<img src='images_conda/img_003.png' alt='img_003' width='450'/>

The lib folder contains a python3.11 which contains the Python standard modules:

<img src='images_conda/img_004.png' alt='img_004' width='450'/>

For example the ```email``` module which is a folder of multiple Python script files:

<img src='images_conda/img_005.png' alt='img_005' width='450'/>

And the ```datetime``` module which is an individual script file:

<img src='images_conda/img_006.png' alt='img_006' width='450'/>

There is also the ```site-packages``` subfolder which contains the third-party libraries:

<img src='images_conda/img_007.png' alt='img_007' width='450'/>

For example ```numpy```:

<img src='images_conda/img_008.png' alt='img_008' width='450'/>

## The envs folder

Additional Python environments are found in the environments folder envs:

```
~\anaconda3\envs
```

<img src='images_conda/img_009.png' alt='img_009' width='450'/>

By default there are no additional Python environments and this folder is empty:

<img src='images_conda/img_010.png' alt='img_010' width='450'/>

A Python environment is essentially a sub-installation of Python which is used to install Python alongside a number of third-party Python libraries.

The use of Python environments for example allows installation of the latest version of each IDE without breaking the functionality of the (base) Python environment.

## conda Package Manager

### Overview

An overview about the conda package manager can be seen by opening up the Terminal and inputting the bash command:

```
conda
```

<img src='images_conda/img_011.png' alt='img_011' width='450'/>

This gives the following output:

<img src='images_conda/img_012.png' alt='img_012' width='450'/>

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

where "notbase" is the environment name. 

<img src='images_conda/img_019.png' alt='img_019' width='450'/>

Input ```y``` to proceed:

<img src='images_conda/img_020.png' alt='img_020' width='450'/>

<img src='images_conda/img_021.png' alt='img_021' width='450'/>

Notice in envs, the notbase subfolder is created:

<img src='images_conda/img_022.png' alt='img_022' width='450'/>

<img src='images_conda/img_023.png' alt='img_023' width='450'/>

### Activate

Once the Python environment is created it can be activated (selected) using:

```
conda activate notbase
```

<img src='images_conda/img_024.png' alt='img_024' width='450'/>

Once activated, any changes made using the conda package manager in the Linux Terminal will apply to this Python environment instead of base. The prompt now has the (notbase) prefix indicating that the (notbase) Python is selected:

<img src='images_conda/img_025.png' alt='img_025' width='450'/>

If the Linux Terminal is closed and reopened, the default Python environment base will be selected. The Python environment notbase will have to be activated.

The command option ```list``` will list all the packages in the currently selected Python environmment, this Python environment notbase is empty:

```
conda list
```

<img src='images_conda/img_026.png' alt='img_026' width='450'/>

### Search

The conda-forge community channel can be searched for a package in this case the package "python" using:

```
conda search -c conda-forge python
```

<img src='images_conda/img_027.png' alt='img_027' width='450'/>

Notice each Python has a version, a build number and a channel:

<img src='images_conda/img_028.png' alt='img_028' width='450'/>

Specifying the channel is not necessary as the .condarc file already specifies use of the conda-forge channel however it is good practice when using the conda package manager to specify the channel in order to prevent confusion. The package ipython can be searched for using:

```
conda search -c conda-forge ipython
```

<img src='images_conda/img_029.png' alt='img_029' width='450'/>

<img src='images_conda/img_030.png' alt='img_030' width='450'/>

### Install

Multiple packages can be installed using the syntax:

```
conda install -c conda-forge python ipython
```

<img src='images_conda/img_031.png' alt='img_031' width='450'/>

Details about the packages to be installed are listed:

<img src='images_conda/img_032.png' alt='img_032' width='450'/>

Input ```y``` in order to proceed:

<img src='images_conda/img_033.png' alt='img_033' width='450'/>
<img src='images_conda/img_034.png' alt='img_034' width='450'/>

Notice the Python environment notbase, now has its own bin and lib subfolder:

<img src='images_conda/img_035.png' alt='img_035' width='450'/>

Which contains its own python3.11 application:

<img src='images_conda/img_036.png' alt='img_036' width='450'/>

And python3.11 folder respectively:

<img src='images_conda/img_037.png' alt='img_037' width='450'/>

All the Python standard modules are included in the python3.11 subfolder:

<img src='images_conda/img_038.png' alt='img_038' width='450'/>

<img src='images_conda/img_039.png' alt='img_039' width='450'/>

And third-partylibraries are included in the site-packages subfolder:

<img src='images_conda/img_040.png' alt='img_040' width='450'/>

This has ipython and some of its dependencies such as the matplotlib backend matplotlib_inline:

<img src='images_conda/img_041.png' alt='img_041' width='450'/>

The data science libraries numpy, pandas and matplotlib (the full library) as they are not installed as they are not dependencies.

### Remove

The command remove can be used to remove an installed package:

```
conda remove python ipython
```

<img src='images_conda/img_042.png' alt='img_042' width='450'/>

If other packages rely on the packages being removed as dependencies, they will be removed. Since Python itself is being removed, and all packages are in turn dependent on Python, they will all be removed:

<img src='images_conda/img_043.png' alt='img_043' width='450'/>

Input ```y``` to proceed with the changes. The changes will then be made:

<img src='images_conda/img_044.png' alt='img_044' width='450'/>

<img src='images_conda/img_045.png' alt='img_045' width='450'/>

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
conda install -c conda-forge python=3.11.3=h2755cc3_0_cpython
```

Some packages for example ipython have multiple variants that have the same version number, for example ipython has 3 variants that are at version 8.14.0 on the conda-forge channel. These each have unique build numbers pyh08f2357_0, py41d4057_0 and pyhd1c38e8_0 as seen in the previous output when conda search was used. Normally this is because there is a slightly seperate variant for different minor Python versions e.g. Python 3.11, 3.10 and 3.9.

A specific version and build of python and ipython can be installed:

```
conda install -c conda-forge python=3.11.3=h2755cc3_0_cpython ipython=8.14.0=pyh08f2357_0
```

Specifying the version number without the build is more commonly used:

```
conda install -c conda-forge python=3.11.3=h2755cc3_0_cpython ipython=8.14.0=pyh08f2357_0
```

<img src='images_conda/img_046.png' alt='img_046' width='450'/>

Details about the other packages installed will display. Input ```y``` in order to install the packages:

<img src='images_conda/img_047.png' alt='img_047' width='450'/>

The changes will be made:

<img src='images_conda/img_048.png' alt='img_048' width='450'/>

### Update

Packages can be updated to the latest version using:

```
conda update -c conda-forge ipython
```

<img src='images_conda/img_049.png' alt='img_049' width='450'/>

Since an older version of ipython was installed, the newer version 8.15.0 is available:

<img src='images_conda/img_050.png' alt='img_050' width='450'/>

To install it input ```y```. In this case ```n``` will be selected:

<img src='images_conda/img_051.png' alt='img_051' width='450'/>

Alternatively all packages in the environment can be updated using:

```
conda update -c conda-forge --all
```

<img src='images_conda/img_052.png' alt='img_052' width='450'/>

Note sometimes some packages may be downgraded in order to upgrade some other packages. Sometimes packages require an older version of another package as a dependency. To install the updates input ```y```:

<img src='images_conda/img_053.png' alt='img_053' width='450'/>

The updates are now installed:

<img src='images_conda/img_054.png' alt='img_054' width='450'/>

### List

Packages can be listed in the Python environment using:

```
conda list
```

<img src='images_conda/img_055.png' alt='img_055' width='450'/>
<img src='images_conda/img_056.png' alt='img_056' width='450'/>

The conda list command can be used with the option --revisions:

```
conda list --revision
```

<img src='images_conda/img_057.png' alt='img_057' width='450'/>
<img src='images_conda/img_058.png' alt='img_058' width='450'/>
<img src='images_conda/img_059.png' alt='img_059' width='450'/>

### Install Revision

The conda install command can be used with the option --revisions and assigned to a revision number. For example, the revision 3 before the update can be reverted to using:

```
conda install -c conda-forge --revision=3
```

<img src='images_conda/img_060.png' alt='img_060' width='450'/>

Details about the changes will be provided including the downgrades:

<img src='images_conda/img_061.png' alt='img_061' width='450'/>

Input ```y``` in order to proceed and the proposed downgrade will be implemented:

<img src='images_conda/img_062.png' alt='img_062' width='450'/>

### Env Export

The currently activated Python environment can also be exported to a **y**et another **m**arkdown **l**anguage yml file:

```
conda env export > Documents/notbase.yml
```

<img src='images_conda/img_063.png' alt='img_063' width='450'/>

This creates a notbase.yml file in Documents:

<img src='images_conda/img_064.png' alt='img_064' width='450'/>

This can be opened in text editor:

<img src='images_conda/img_065.png' alt='img_065' width='450'/>

This is a very small file which can be shared on GitHub or emailed.

### Env Create

An environment can be created from a yml file for example the notbase.yml in the Documents folder using:

```
conda env create -n notbase2 -f Documents/notbase.yml
```

<img src='images_conda/img_066.png' alt='img_066' width='450'/>

The environment is created and can later be activated:

<img src='images_conda/img_067.png' alt='img_067' width='450'/>

The name of the new environment notbase2 displays as a subfolder in envs:

<img src='images_conda/img_068.png' alt='img_068' width='450'/>

### Env Remove

Note that an active Python environment cannot be removed. To remove an environment, activate another Python environment such as the base Python environment:

```
conda activate base
```

Then use the command:

```
conda env remove -n notbase
```

<img src='images_conda/img_069.png' alt='img_069' width='450'/>

The operation will proceed:

<img src='images_conda/img_070.png' alt='img_070' width='450'/>

The folder notbase will be removed in envs:

<img src='images_conda/img_071.png' alt='img_071' width='450'/>

### rename

A Python environment can be renamed by using the command:

```
conda rename -n notbase2 notbase
```

notbase2 is the original name and notbase is the new name. Note this is done with the base Python environment activated as a Python environment cannot be renamed if it is activated:

<img src='images_conda/img_072.png' alt='img_072' width='450'/>

The notbase folder in the envs folder is now renamed notbase2:

<img src='images_conda/img_073.png' alt='img_073' width='450'/>

### Env List

To list Python environments use:

```
conda env list
```

<img src='images_conda/img_074.png' alt='img_074' width='450'/>

### Clean

A backup of all previously downloaded versions is available which can occupy a large amount of disk space. These can be cleaned using:

```
conda clean --all
```

<img src='images_conda/img_075.png' alt='img_075' width='450'/>

Input ```y``` in ordee to proceed with the removal:

<img src='images_conda/img_076.png' alt='img_076' width='450'/>

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

```
conda create -n vscode -c conda-forge python notebook cython seaborn scikit-learn sympy openpyxl xlrd xlsxwriter lxml sqlalchemy tabulate nodejs ipywidgets plotly ipympl pyqt blue
```

Installing seaborn will install numpy, pandas and matplotlib as these are dependencies for seaborn.

openpyxl, xlrd, xlsxwriter, lxml, sqlalchemy and tabulate are file format convertors used for pandas.

nodejs allows installation of JupyterLab extensions.ipywidgets and plotly can be used to create widgets and plots using Python code, under the hood JavaScript is used to display these in VSCode which behaves like a browser. 

pyqt and ipympl are required for an interactive matplotlib plotting backends. The Python interpretter needs to be selected in VSCode as seen before.

### PyCharm Python Environment

```
conda create -n pycharm -c conda-forge python cython seaborn scikit-learn sympy openpyxl xlrd xlsxwriter lxml sqlalchemy tabulate pyqt
```

Installing seaborn will install numpy, pandas and matplotlib as these are dependencies for seaborn.

openpyxl, xlrd, xlsxwriter, lxml, sqlalchemy and tabulate are file format convertors used for pandas.

pyqt is required for an interactive matplotlib plotting backends.

The Python interpretter needs to be selected in PyCharm.

### Config and .condarc file

The conda config command is used to create a .condarc file which can be used to change the solver used by the conda package manager and the channel and channel priority used by the conda package manager. This is normally not recommended.

Open the Linux Terminal. Recall the default location the Linux Terminal opens in is ```~``` This is the location a ```.condarc``` file gets placed.

Note that this file is hidden. To view it in files, Show Hidden Files needs to be enabled:

<img src='images_conda/img_013.png' alt='img_013' width='450'/>

If an old .condarc file is present delete it using:

```
rm .condarc
```

<img src='images_conda/img_014.png' alt='img_014' width='450'/>

<img src='images_conda/img_015.png' alt='img_015' width='450'/>


The community conda-forge can be added:

```
conda config --add channels conda-forge
```

And the anaconda channel (defaults) can be removed:

```
conda config --remove channels defaults
```

Additional performance can be achieved by setting the channel priority to strict:

```
conda config --set channel_priority strict
```

<img src='images_conda/img_016.png' alt='img_016' width='450'/>

This .condarc is optimised for creating new Python environments using packages from the community channel conda-forge. It should not be used to update Anaconda; which should only use the anaconda package from the anaconda channel.

The contents of the ```.condarc``` file can be viewed in the Terminal using the command:

```
nano .condarc
```

<img src='images_conda/img_017.png' alt='img_017' width='450'/>

```
channels:
  - conda-forge
  - defaults
channel_priority: strict
```

<img src='images_conda/img_018.png' alt='img_018' width='450'/>

[Return to Anaconda Tutorial](./readme.md)