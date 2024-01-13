# The conda Package Manager

The purpose of the conda package manager is to allow cross-platform installation of Python packages and non-Python dependences related to a datascience project in a Python environment. This can include other programming languages such as R.

The conda package manager has two main channels:

|channel name|channel description|
|---|---|
|conda-forge|community channel maintained by developers|
|main|channel maintained by the Anaconda company|

The main channel also known as conda or anaconda is the channel maintained by the Anaconda company. These packages are tested by the Anaconda company for compatibility with the Anaconda Python distribution. As the Anaconda company only test commonly used datascience libraries and it takes time for testing, there are less packages available in the main channel and the package that they have may not be the latest version.

## The base Python Environment

In Anaconda the base Python environment is a Python distribution and should not be modified outwith the standard conda images available from Anaconda. The reason for this is the Python distribution has a large number of packages and changing a package that is a dependency for the other packages will normally result in a number of these packages being removed leading to an unstable Python environment.

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

The bin subfolder which contains binary applications installed in the (base) Python environment. This includes python which has the alias python3.11 and python3 alias:

<img src='images_conda/img_003.png' alt='img_003' width='450'/>

The lib subfolder contains a python3.11 subfolder which contains the Python standard modules:

<img src='images_conda/img_004.png' alt='img_004' width='450'/>

When the module is a single file the name of the file corresponds to the name of the module. When the module is a folder, the folder name corresponds to the name of the module and there is a datamodel initialisation script file called ```__init__.py``` which is imported.

For example the ```datetime``` module is an individual script file:

<img src='images_conda/img_006.png' alt='img_006' width='450'/>

And the ```email``` module which is a folder of multiple Python script files:

<img src='images_conda/img_005.png' alt='img_005' width='450'/>

This folder contains third-party modules also known as libraries. Common libraries are numpy, pandas and matplotlib. 

<img src='images_conda/img_007.png' alt='img_007' width='450'/>

For example ```numpy```:

<img src='images_conda/img_008.png' alt='img_008' width='450'/>

These modules can be imported and the datamodel attribute ```__file__``` can be printed to view the location of the file:

```
(base) username@pc:~$ jupyter-console
Jupyter console 6.6.3

Python 3.11.5 (main, Sep 11 2023, 13:54:46) [GCC 11.2.0]
Type 'copyright', 'credits' or 'license' for more information
IPython 8.15.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import datetime
   ...: import email

In [2]: print(datetime.__file__)
   ...: print(email.__file__)
~/anaconda3/lib/python3.11/datetime.py
~/anaconda3/lib/python3.11/email/__init__.py

In [3]: import numpy as np
   ...: import pandas as pd
   ...: import matplotlib.pyplot as plt

In [4]: print(np.__file__)
   ...: print(pd.__file__)
   ...: print(plt.__file__)
~/anaconda3/lib/python3.11/site-packages/numpy/__init__.py
~/anaconda3/lib/python3.11/site-packages/pandas/__init__.py
~/anaconda3/lib/python3.11/site-packages/matplotlib/pyplot.py

In [5]:
```

## The envs folder

The (base) Python environment also contains an envs folder which is used for Python environments:

```
~\anaconda3\envs
```

<img src='images_conda/img_009.png' alt='img_009' width='450'/>

By default there are no additional Python environments and this folder is empty:

<img src='images_conda/img_010.png' alt='img_010' width='450'/>

A Python environment is essentially a sub-installation of Python. Each Python environment will therefore a substructure similar to the (base) Python environment and will have their own:

* python binary in bin folder
* bin folder
* lib folder
* site-packages subfolder within lib

The use of Python environments for example allows installation of the latest version of each IDE without breaking the functionality of the (base) Python environment.

## conda Package Manager

### Overview

An overview about the conda package manager can be seen by opening up the Terminal and inputting the bash command:

```bash
conda
```

This gives the following output:

```
(base) username@pc:~$ conda
usage: conda [-h] [-v] [--no-plugins] [-V] COMMAND ...

conda is a tool for managing and deploying applications, environments and packages.

options
```
|flag or option|purpose|
|---|---|
|-h, --help|Show this help message and exit.|
|-v, --verbose|Can be used multiple times. Once for detailed output, twice for INFO logging, thrice for DEBUG logging, four times for TRACE logging.|
|--no-plugins|Disable all plugins that are not built into conda.|
|-V, --version|Show the conda version number and exit.|
```
commands:
  The following built-in and plugins subcommands are available.
```
|command|description|
|---|---|
|activate|Activate a conda environment.|
|build|Build conda packages from a conda recipe.|
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
```bash
(base) username@pc:~$
```

### Create

A Python environment can be created using the syntax:

```bash
conda create -n notbase
```

where "notbase" is the environment name. The longer ```--name``` can also be used in place of the ```-n```.

The following will be output:

```
(base) username@pc:~$ conda create -n notbase
Channels:
 - defaults
Platform: linux-64
Collecting package metadata (repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: ~/anaconda3/envs/notbase



Proceed ([y]/n)?
```

Input ```y``` to proceed. The Python environment is now created:

```
Preparing transaction: done
Verifying transaction: done
Executing transaction: done
#
# To activate this environment, use
#
#     $ conda activate notbase
#
# To deactivate an active environment, use
#
#     $ conda deactivate

(base) username@pc:~$
```

Notice in envs, the notbase subfolder is created:

<img src='images_conda/img_022.png' alt='img_022' width='450'/>

<img src='images_conda/img_023.png' alt='img_023' width='450'/>

### Activate

The ```activate``` subcommand is used to active a Python environment. When a Python environment is activated the:

* python binary in bin folder
* bin folder
* lib folder
* site-packages subfolder within lib

associated with the Python environment will preferentially be used over their respective locations in (base).

The notbase Python environment can be activated using:

```bash
conda activate notbase
```

The output now looks like:

```
(base) username@pc:~$ conda activate notbase
(notbase) username@pc:~$
```

Notice that the prompt now has the (notbase) prefix indicating that the (notbase) Python is activated.

When the Terminal is closed and reopened, the default Python environment (base) will be activated. The Python environment notbase will have to be activated.

### Search

A package can be searched for using the ```search``` subcommand followed by the package name:

```bash
conda search package_name
```

The channel to search for packages in can be specified using ```-c``` or the long form ```--channel``` followed by the name of the channel. The default channel is ```main``` but it is more common to use the ```conda-forge``` community channel when creating a custom Python environment. 

```bash
conda search -c conda-forge package_name
```

or example a search of the package python:

```bash
conda search python
```

Outputs:

```
(notbase) username@pc:~$ conda search python
Loading channels: done
```
|Name|Version|Build|Channel|
|---|---|---|---|
|python|3.11.5|h7a1cb2a_0|pkgs/main|
|python|3.11.5|h955ad1f_0|pkgs/main|
|python|3.11.7|h955ad1f_0|pkgs/main|
|python|3.12.0|h996f2a0_0|pkgs/main|
```
(notbase) username@pc:~$
```

And if the channel is change to conda-forge:

```bash
conda search -c conda-forge python
```

Outputs:

```
(notbase) username@pc:~$ conda search -c conda-forge python
Loading channels: done
```
|Name|Version|Build|Channel|
|---|---|---|---|
|python|3.11.7|h955ad1f_0|pkgs/main|
|python|3.11.7|hab00c5b_0_cpython|conda-forge|
|python|3.11.7|hab00c5b_1_cpython|conda-forge|
|python|3.12.0rc3|rc3_hab00c5b_1_cpython|conda-forge|
|python|3.12.0|h996f2a0_0|pkgs/main|
|python|3.12.0|hab00c5b_0_cpython|conda-forge|
|python|3.12.1|hab00c5b_0_cpython|conda-forge|
|python|3.12.1|hab00c5b_1_cpython|conda-forge|
```
(notbase) username@pc:~$
```

Notice each Python has a version number of the format X.Y.Z where X is the major build, Y is the minor build and Z is the patch number. The build number consists of a hash followed by a revision. If prefixed with py it is a pure Python package.

The package ipython can be searched for using:

```bash
conda search -c conda-forge ipython
```

This outputs:

```
(notbase) username@pc:~$ conda search -c conda-forge ipython
Loading channels: done
```
|Name|Version|Build|Channel|
|---|---|---|---|
|ipython|8.19.0|pyh707e725_0|conda-forge|
|ipython|8.19.0|pyh7428d3b_0|conda-forge|
|ipython|8.20.0|py310h06a4308_0pyh707e725_0|pkgs/main|
|ipython|8.20.0|py311h06a4308_0|pkgs/main|
|ipython|8.20.0|py312h06a4308_0|pkgs/main|
|ipython|8.20.0|pyh707e725_0|conda-forge|
|ipython|8.20.0|pyh7428d3b_0|conda-forge|
```
(notbase) username@pc:~$
```

### Install

The subcommand ```install``` can be used to install a package:

```bash
conda install package_name
```

Multiple packages can be installed using the syntax:

```bash
conda install package_name1 package_name2
```

Once again the channel to install from should be specified:

```bash
conda install -c conda-forge package_name1 package_name2
```

The packages python and ipython can be installed from the community channel using:

```bash
conda install -c conda-forge python ipython
```

This outputs:

```
(notbase) username@pc:~$ conda install -c conda-forge python ipython
Channels:
 - conda-forge
 - defaults
Platform: linux-64
Collecting package metadata (repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: ~/anaconda3/envs/notbase

  added / updated specs:
    - ipython
    - python


The following packages will be downloaded:
```
|package|build|size|channel|
|---|---|---|---|
|exceptiongroup-1.2.0|pyhd8ed1ab_2|20 KB|conda-forge|
|ipython-8.20.0|pyh707e725_0|577 KB|conda-forge|
|setuptools-69.0.3|pyhd8ed1ab_0|460 KB|conda-forge|
|traitlets-5.14.1|pyhd8ed1ab_0|108 KB|conda-forge|
|wcwidth-0.2.13|pyhd8ed1ab_0|32 KB|conda-forge|
```
Total: 1.2 MB
The following NEW packages will be INSTALLED:
```
|package|details|
|---|---|
|_libgcc_mutex|conda-forge/linux-64::_libgcc_mutex-0.1-conda_forge|
|_openmp_mutex|conda-forge/linux-64::_openmp_mutex-4.5-2_gnu|
|asttokens|conda-forge/noarch::asttokens-2.4.1-pyhd8ed1ab_0|
|bzip2|conda-forge/linux-64::bzip2-1.0.8-hd590300_5|
|ca-certificates|conda-forge/linux-64::ca-certificates-2023.11.17-hbcca054_0|
|decorator|conda-forge/noarch::decorator-5.1.1-pyhd8ed1ab_0|
|exceptiongroup|conda-forge/noarch::exceptiongroup-1.2.0-pyhd8ed1ab_2|
|executing|conda-forge/noarch::executing-2.0.1-pyhd8ed1ab_0|
|ipython|conda-forge/noarch::ipython-8.20.0-pyh707e725_0|
|jedi|conda-forge/noarch::jedi-0.19.1-pyhd8ed1ab_0|
|ld_impl_linux-64|conda-forge/linux-64::ld_impl_linux-64-2.40-h41732ed_0|
|libexpat|conda-forge/linux-64::libexpat-2.5.0-hcb278e6_1|
|libffi|conda-forge/linux-64::libffi-3.4.2-h7f98852_5|
|libgcc-ng|conda-forge/linux-64::libgcc-ng-13.2.0-h807b86a_3|
|libgomp|conda-forge/linux-64::libgomp-13.2.0-h807b86a_3|
|libnsl|conda-forge/linux-64::libnsl-2.0.1-hd590300_0|
|libsqlite|conda-forge/linux-64::libsqlite-3.44.2-h2797004_0|
|libuuid|conda-forge/linux-64::libuuid-2.38.1-h0b41bf4_0|
|libxcrypt|conda-forge/linux-64::libxcrypt-4.4.36-hd590300_1|
|libzlib|conda-forge/linux-64::libzlib-1.2.13-hd590300_5|
|matplotlib-inline|conda-forge/noarch::matplotlib-inline-0.1.6-pyhd8ed1ab_0|
|ncurses|conda-forge/linux-64::ncurses-6.4-h59595ed_2|
|openssl|conda-forge/linux-64::openssl-3.2.0-hd590300_1|
|parso|conda-forge/noarch::parso-0.8.3-pyhd8ed1ab_0|
|pexpect|conda-forge/noarch::pexpect-4.8.0-pyh1a96a4e_2|
|pickleshare|conda-forge/noarch::pickleshare-0.7.5-py_1003|
|pip|conda-forge/noarch::pip-23.3.2-pyhd8ed1ab_0|
|prompt-toolkit|conda-forge/noarch::prompt-toolkit-3.0.42-pyha770c72_0|
|ptyprocess|conda-forge/noarch::ptyprocess-0.7.0-pyhd3deb0d_0|
|pure_eval|conda-forge/noarch::pure_eval-0.2.2-pyhd8ed1ab_0|
|pygments|conda-forge/noarch::pygments-2.17.2-pyhd8ed1ab_0|
|python|conda-forge/linux-64::python-3.12.1-hab00c5b_1_cpython|
|readline|conda-forge/linux-64::readline-8.2-h8228510_1|
|setuptools|conda-forge/noarch::setuptools-69.0.3-pyhd8ed1ab_0|
|six|conda-forge/noarch::six-1.16.0-pyh6c4a22f_0|
|stack_data|conda-forge/noarch::stack_data-0.6.2-pyhd8ed1ab_0|
|tk|conda-forge/linux-64::tk-8.6.13-noxft_h4845f30_101|
|traitlets|conda-forge/noarch::traitlets-5.14.1-pyhd8ed1ab_0|
|typing_extensions|conda-forge/noarch::typing_extensions-4.9.0-pyha770c72_0|
|tzdata|conda-forge/noarch::tzdata-2023d-h0c530f3_0|
|wcwidth|conda-forge/noarch::wcwidth-0.2.13-pyhd8ed1ab_0|
|wheel|conda-forge/noarch::wheel-0.42.0-pyhd8ed1ab_0|
|xz|conda-forge/linux-64::xz-5.2.6-h166bdaf_0|
```bash
Proceed ([y]/n)?
```

Input ```y``` in order to proceed. This outputs:

```
Downloading and Extracting Packages:

Preparing transaction: done
Verifying transaction: done
Executing transaction: done
(notbase) username@pc:~$
```

A new prompt is available when the operation is finished.




jupyter-console can be used from this Python environment. Notice when the standard modules are imported, the modules from the perspective Python environment are used:

```
(base) username@pc:~$ conda activate notbase
(notbase) username@pc:~$ ipython
Python 3.12.1 | packaged by conda-forge | (main, Dec 23 2023, 08:03:24) [GCC 12.3.0]
Type 'copyright', 'credits' or 'license' for more information
IPython 8.20.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import datetime
   ...: import email
   ...:
   ...: print(datetime.__file__)
   ...: print(email.__file__)
~/anaconda3/envs/notbase/lib/python3.12/datetime.py
~/anaconda3/envs/notbase/lib/python3.12/email/__init__.py

In [2]: import numpy as np
   ...: import pandas as pd
   ...: import matplotlib.pyplot as plt
---------------------------------------------------------------------------
ModuleNotFoundError                       Traceback (most recent call last)
Cell In[2], line 1
----> 1 import numpy as np
      2 import pandas as pd
      3 import matplotlib.pyplot as plt

ModuleNotFoundError: No module named 'numpy'

In [3]:
```

Note attempting to import numpy, pandas and matplotlib gives a ```ModuleNotFoundError``` as they are not installed in this Python environment.

### Remove

The ```remove``` subcommand can be used to remove an installed package:

```bash
conda remove package_name1 package_name2
```

For example the package python can be removed using:

```bash
conda remove python
```

This outputs:

```
(notbase) username@pc:~$ conda remove python
Channels:
 - defaults
 - conda-forge
Platform: linux-64
Collecting package metadata (repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: ~/anaconda3/envs/notbase

  removed specs:
    - python


The following packages will be REMOVED:
```
|details|
|---|
|asttokens-2.4.1-pyhd8ed1ab_0|
|bzip2-1.0.8-hd590300_5|
|decorator-5.1.1-pyhd8ed1ab_0|
|exceptiongroup-1.2.0-pyhd8ed1ab_2|
|executing-2.0.1-pyhd8ed1ab_0|
|ipython-8.20.0-pyh707e725_0|
|jedi-0.19.1-pyhd8ed1ab_0|
|ld_impl_linux-64-2.40-h41732ed_0|
|libexpat-2.5.0-hcb278e6_1|
|libffi-3.4.2-h7f98852_5|
|libnsl-2.0.1-hd590300_0|
|libsqlite-3.44.2-h2797004_0|
|libuuid-2.38.1-h0b41bf4_0|
|libxcrypt-4.4.36-hd590300_1|
|libzlib-1.2.13-hd590300_5|
|matplotlib-inline-0.1.6-pyhd8ed1ab_0|
|ncurses-6.4-h59595ed_2|
|parso-0.8.3-pyhd8ed1ab_0|
|pexpect-4.8.0-pyh1a96a4e_2|
|pickleshare-0.7.5-py_1003|
|pip-23.3.2-pyhd8ed1ab_0|
|prompt-toolkit-3.0.42-pyha770c72_0|
|ptyprocess-0.7.0-pyhd3deb0d_0|
|pure_eval-0.2.2-pyhd8ed1ab_0|
|pygments-2.17.2-pyhd8ed1ab_0|
|python-3.12.1-hab00c5b_1_cpython|
|readline-8.2-h8228510_1|
|setuptools-69.0.3-pyhd8ed1ab_0|
|six-1.16.0-pyh6c4a22f_0|
|stack_data-0.6.2-pyhd8ed1ab_0|
|tk-8.6.13-noxft_h4845f30_101|
|traitlets-5.14.1-pyhd8ed1ab_0|
|typing_extensions-4.9.0-pyha770c72_0|
|tzdata-2023d-h0c530f3_0|
|wcwidth-0.2.13-pyhd8ed1ab_0|
|wheel-0.42.0-pyhd8ed1ab_0|
|xz-5.2.6-h166bdaf_0|
```
Proceed ([y]/n)?
```

Because Python is being removed which is a dependency for everything else, everything else is also removed. To proceed with the changes input ```y```. This outputs:

```
Preparing transaction: done
Verifying transaction: done
Executing transaction: done
(notbase) PS ~>
```

A new prompt is available when the operation is finished.









Notice the Python environment notbase, now has its own bin and lib subfolder:

<img src='images_conda/img_035.png' alt='img_035' width='450'/>

Which contains its own python application:

<img src='images_conda/img_036.png' alt='img_036' width='450'/>

And python 3.12 folder respectively:

<img src='images_conda/img_037.png' alt='img_037' width='450'/>

All the Python standard modules are included in the python3.12 subfolder:

<img src='images_conda/img_038.png' alt='img_038' width='450'/>

<img src='images_conda/img_039.png' alt='img_039' width='450'/>

And third-party libraries are included in the site-packages subfolder:

<img src='images_conda/img_040.png' alt='img_040' width='450'/>

This has ipython and some of its dependencies such as the matplotlib backend matplotlib_inline:

<img src='images_conda/img_041.png' alt='img_041' width='450'/>

The data science libraries numpy, pandas and matplotlib (the full library) are not installed as they are not dependencies.

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