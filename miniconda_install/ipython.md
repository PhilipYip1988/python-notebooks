# Interactive Python

Previously PowerShell and Python were used. PowerShell is a scripting language used to navigate throughout the operating system, essentially a Terminal based version of Windows Explorer. Unfortunately the Miniconda Prompt at the time of writing hasn't been updated to PowerShell. Python is a scripting program for general purposes. 

The disadvantage of this setup is the Python program needs to be exited in order to return to the PowerShell Prompt:

<img src='images_ipython/img_001.png' alt='img_001' width=450/>

In addition the IDLE shell was examined which was seen to be terminal like but included additional functionality like code completion and docstrings.

ipython is an abbreviation for **i**nteractive **Python** and incorporates all the functionality of Python and has the commonly used system shell commands accessed from PowerShell albeit being more closely related to the open-source counterpart in Linux known as bash. It also includes similar code-completion to the IDLE shell although the docstrings do not display as popup balloons and have to be outputted to an ipython cell.

ipython is not included in the Miniconda (base) environment and can be added using:

```
conda install ipython
```

A better practice is to leave the (base) Python environment unmodified and therefore create a new Python environment.

Miniconda will be used to create a Python environment. To install Miniconda and set it up to use the conda-forge channel and libmamba solver see [Miniconda: Install](./Miniconda.md)

The following Python Environment can be created for ipython:

```
conda create -n ipython python ipython cython seaborn scikit-learn sympy openpyxl xlrd xlsxwriter lxml sqlalchemy nodejs tabulate 
```

This is covered in more detail in [Miniconda: Python Environments Overview](./environments.md)

<img src='images_ipython/img_002.png' alt='img_002' width=450/>

The conda package manager will search for all of these packages and their dependencies. Input ```y``` in order to proceed:

<img src='images_ipython/img_003.png' alt='img_003' width=450/>

The packages will be downloaded and installed. This Python environment can be activated using:

```
conda activate ipython
```

<img src='images_ipython/img_004.png' alt='img_004' width=450/>

To launch ipython from the Python environment ipython use:

```
ipython
```

<img src='images_ipython/img_005.png' alt='img_005' width=450/>

Notice that when ```p``` is input the last command inputting beginning with p displays. The previous few commands can be cycled through using the ``` ↑``` and ```↓``` arrow keys:

<img src='images_ipython/img_006.png' alt='img_006' width=450/>

If the ```↹``` key is pressed a list of builtins identifiers and IPython magics display. IPython magics are distingished from Python objects as they begin with a %:

<img src='images_ipython/img_007.png' alt='img_007' width=450/>

Using ? followed by a Python function will display the functions docstring:

```
? print
```

<img src='images_ipython/img_008.png' alt='img_008' width='450'/>

If a module such as builtins is imported using:

```
import builtins
```

A list of identifiers can be seen by inputting ```builtins.``` followed by a ```↹```. There are a large number of idnetifiers and the arrow keys can be used to cycle through them:

<img src='images_ipython/img_009.png' alt='img_009' width='450'/>

If ```c``` is input the Python builtins beginning with c are displayed. The ones with parenthesis are functions and the ones beginning with % are ipython magics:

<img src='images_ipython/img_010.png' alt='img_010' width='450'/>

To clear the screen, the ipython magic %cls can be used:

```
%cls
```

<img src='images_ipython/img_011.png' alt='img_011' width='450'/>

The ipython number will continue from the previous cell:

<img src='images_ipython/img_012.png' alt='img_012' width='450'/>

If ```%``` and ```↹``` are input, all the ipython magics display:

<img src='images_ipython/img_013.png' alt='img_013' width='450'/>

The print working directory magic command %pwd will print the current working directory as a Python string (formal representation):

<img src='images_ipython/img_014.png' alt='img_014' width='450'/>

The change directory command %cd will also print the working current directory displayed as a Windows path:

<img src='images_ipython/img_015.png' alt='img_015' width='450'/>

The default location for the Miniconda Prompt is the %USERPROFILE%:

<img src='images_ipython/img_016.png' alt='img_016' width='450'/>

This maps to C:\Users\Philip:

<img src='images_ipython/img_017.png' alt='img_017' width='450'/>

Notice that the Documents folder is a subfolder. The directory can be changed using:

```
%cd Documents
```

<img src='images_ipython/img_018.png' alt='img_018' width='450'/>

<img src='images_ipython/img_019.png' alt='img_019' width='450'/>

The %USERPROFILE% can be accessed using ```~``` and set to the current directory using:

```
%cd ~
```

<img src='images_ipython/img_020.png' alt='img_020' width='450'/>

<img src='images_ipython/img_021.png' alt='img_021' width='450'/>

Documents can be reselected using:

```
%cd ~\Documents
```

<img src='images_ipython/img_022.png' alt='img_022' width='450'/>

<img src='images_ipython/img_023.png' alt='img_023' width='450'/>

```.\``` explicitly means in the same directory as notice the directory has not changed:

```
cd .\
```

<img src='images_ipython/img_024.png' alt='img_024' width='450'/>

```..\``` means the parent directory:

```
cd ..\
```

which in the case of Documents is the %USERPROFILE%:

<img src='images_ipython/img_025.png' alt='img_025' width='450'/>

Returning back to Documents using:

```
cd ~\Documents
```

<img src='images_ipython/img_026.png' alt='img_026' width='450'/>

If a new file is created in Windows Explorer and a forbidden character used a message displays stating that a file name can't contain any of the following characters ```\ / : * ? " < > |``` as they are reserved:

<img src='images_ipython/img_027.png' alt='img_027' width='450'/>

The ipython make directory command can be used to make a directory:

```
mkdir test.py
```

Notice that this command always creates a directory and the . is included in the folder name which is bad practice for a folder name:

<img src='images_ipython/img_028.png' alt='img_028' width='450'/>

<img src='images_ipython/img_029.png' alt='img_029' width='450'/>

The related ipython magic command remove directory can be used to remove this directory:

```
rmdir test.py
```

<img src='images_ipython/img_030.png' alt='img_030' width='450'/>

It is good practice to use a folder name without spaces:

```
mkdir newfolder
```

<img src='images_ipython/img_031.png' alt='img_031' width='450'/>

<img src='images_ipython/img_032.png' alt='img_032' width='450'/>

If spaces are added, two folders will be created:

```
mkdir new folder
```

<img src='images_ipython/img_033.png' alt='img_033' width='450'/>

<img src='images_ipython/img_034.png' alt='img_034' width='450'/>

To get around this the reserved double quotations " " can be used to enclose the folder name:

```
mkdir "new folder"
```

<img src='images_ipython/img_035.png' alt='img_035' width='450'/>

<img src='images_ipython/img_036.png' alt='img_036' width='450'/>

The Python language typically uses single quotations however these can be included in a directory name:

```
mkdir 'new folder'
```

so instead a directory ```'new``` and a directory ```folder'``` are created:

<img src='images_ipython/img_037.png' alt='img_037' width='450'/>

<img src='images_ipython/img_038.png' alt='img_038' width='450'/>

The command list will list all the files in the directory:

```
ls
```

<img src='images_ipython/img_039.png' alt='img_039' width='450'/>

If ```%%``` is input followed by a ```↹``` a list of multiline ipython magic commands display:

<img src='images_ipython/img_040.png' alt='img_040' width='450'/>

If the following is input:

```
%%writefile script.py
```

Then lines of code can be added to the Python file. Lines of code will continue to be added until there are 2 blank lines at which point, the file will be saved, closed and executed:

<img src='images_ipython/img_041.png' alt='img_041' width='450'/>

The ipython magic command run can be used to run a file:

```
%run script.py
```

<img src='images_ipython/img_042.png' alt='img_042' width='450'/>

The ipython magic command run can be used to edit a file:

```
%edit script.py
```

This will open in notepad by default and the console will hang on editing... until notepad is closed by the user:

<img src='images_ipython/img_043.png' alt='img_043' width='450'/>

The file can be modified to include:

```
print('Hello World!')
```

<img src='images_ipython/img_044.png' alt='img_044' width='450'/>

Then notepad can be closed and the file is executed:

<img src='images_ipython/img_045.png' alt='img_045' width='450'/>

The default text editor can be changed to another program such as Notepad++

<img src='images_ipython/img_046.png' alt='img_046' width='450'/>

To do this an environmental variable EDITOR needs to be added. Right click the Start button and select System:

<img src='images_ipython/img_047.png' alt='img_047' width='250'/>

Select Advanced System Settings: 

<img src='images_ipython/img_048.png' alt='img_048' width='400'/>

Then Environmental Variables:

<img src='images_ipython/img_049.png' alt='img_049' width='350'/>

Then select New:

<img src='images_ipython/img_050.png' alt='img_050' width='350'/>

Store the Variable Name as ```EDITOR``` and the Variable Value as ```"C:\Program Files\Notepad++\notepad++.exe"```, note the quotations as there is a space in Program Files:

<img src='images_ipython/img_051.png' alt='img_051' width='350'/>

Select OK:

<img src='images_ipython/img_052.png' alt='img_052' width='350'/>

Close all open Miniconda Prompts and relaunch to refresh the Environmental Variables:

<img src='images_ipython/img_053.png' alt='img_053' width='450'/>

Notice that Notepad++ is now the default editor and has some syntax highlighting for Python code.

[Return to Miniconda Installation](./readme.md)