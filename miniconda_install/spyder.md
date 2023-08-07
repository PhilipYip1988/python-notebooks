# Spyder

Spyder is an abbreviation for the **S**cientific **Py**thon **D**evelopment **E**nvi**r**onment and is a Python IDE similar to MATLAB or R-Studio.

Spyder is used for editing Python script files (.py file extension) and sadly does not have native support for notebook files (.ipynb file estension). There is a pluggin spyder-notebook in early development for this purpose however it is not completely stable yet.

## Python Environment

Miniconda will be used to create a Python environment. To install Miniconda and set it up to use the conda-forge channel and libmamba solver see [Miniconda: Install](./Miniconda.md)

The following Python Environment can be created for the Spyder IDE:
```
conda create -n spyder python spyder cython seaborn scikit-learn sympy openpyxl xlrd xlsxwriter lxml sqlalchemy nodejs tabulate pyqt
```

This is covered in more detail in [Miniforge: Python Environments Overview](./environments.md)

<img src='images_spyder/img_001.png' alt='img_001' width='450'/>

The conda package manager will search for all of these packages and their dependencies. Input ```y``` in order to proceed:

<img src='images_spyder/img_002.png' alt='img_002' width='450'/>

The packages will be downloaded and installed:

<img src='images_spyder/img_003.png' alt='img_003' width='450'/>

## Launching Spyder

Spyder can be launched by activating the spyder Python environment using the PowerShell command:

```
conda activate spyder
```

And using the PowerShell command:

```
spyder
```

Alternatively it can be launched from its start menu shortcut.

<img src='images_spyder/img_004.png' alt='img_004' width='450'/>

## Customisation

The Spyder IDE displays using the Spyder Dark Theme by default. The is can be changed in Tools → Preferences:

<img src='images_spyder/img_005.png' alt='img_005' width='450'/>

Select Appearance and the Spyder:

<img src='images_spyder/img_006.png' alt='img_006' width='450'/>

Spyder will restart to make the changes.

## Variable Explorer

Spyder has a very powerful Variable Explorer supporting most of builtins and the commonly used data structures in the data science libraries:

<img src='images_spyder/img_007.png' alt='img_007' width='450'/>

<img src='images_spyder/img_008.png' alt='img_008' width='450'/>

## Files

The FIle Panes shows the current working directory:

<img src='images_spyder/img_009.png' alt='img_009' width='450'/>

## Plots

Plots are shown as static images in the plots pane by default:

<img src='images_spyder/img_010.png' alt='img_010' width='450'/>

The backend for matplotlib can be changed for example to the gui library pyqt5 using tools → preferences, then IPyhon console, graphics and then changing the backend:

<img src='images_spyder/img_011.png' alt='img_011' width='450'/>

The Kernel needs to be restarted by going to Console → Restart Kernel:

<img src='images_spyder/img_012.png' alt='img_012' width='450'/>

The plot now displays in a seperate window as an interactive plot:

<img src='images_spyder/img_013.png' alt='img_013' width='450'/>

Support for using ipython magics in the ipython console to change the plot backend is added in Spyder 6 which is currently in the alpha stage.

## Help and Code Completions

Spyder displays code completions and docstrings for Python builtins and standard libraries:

<img src='images_spyder/img_014.png' alt='img_014' width='450'/>

If completions from third-party libraries are required, they need to be imported in the script and the imports need to be run in the IPython console. In Python a line beginning with ```#``` is a comment. In Spyder ```#%%``` changes a comment into a cell which can be ran seperately in the console. These cells can be ran seperately in the console using the appropriate run command e.g. run cell or run cell and advance. There is also an option to run a selection. When the entire script file is ran, the ```#%%``` are instead recognised as comments:

<img src='images_spyder/img_015.png' alt='img_015' width='450'/>

Pressing ```Ctrl```+```i``` will inspect an object opening its help in the help pane. This works better at present for builtins functions:

<img src='images_spyder/img_016.png' alt='img_016' width='450'/>

For third-party libraries it gives the home page fo the libraries documentation and doesn't focus on the specific function:

<img src='images_spyder/img_017.png' alt='img_017' width='450'/>

[Return to Miniconda Installation](./readme.md)
