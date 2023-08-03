# MambaForge Install

## Download

The download link for MambaForge can be found on the [Mambaforge](https://mamba.readthedocs.io/en/latest/installation.html) home page. It redirects to GitHub whic will give download links for each Operating System. Select the Windows-x86_64 link:

<img src='images_mambaforge/img_001.png' alt='img_001' width='400'/>

This download may be blocked by downloads:

<img src='images_mambaforge/img_002.png' alt='img_002' width='400'/>

Select Keep:

<img src='images_mambaforge/img_003.png' alt='img_003' width='400'/>

And Keep Anyway:

<img src='images_mambaforge/img_004.png' alt='img_004' width='400'/>

The setup should now be in the Downloads folder:

<img src='images_mambaforge/img_005.png' alt='img_005' width='400'/>

## Installation

Launch the setup:

<img src='images_mambaforge/img_006.png' alt='img_006' width='400'/>

Select Next:

<img src='images_mambaforge/img_007.png' alt='img_007' width='350'/>

Select I Agree:

<img src='images_mambaforge/img_008.png' alt='img_008' width='350'/>

Select next:

<img src='images_mambaforge/img_009.png' alt='img_009' width='350'/>

The default install location will be in:

```
%USERPROFILE%\Mambaforge
```

The environmental variable %USERPROFILE% maps to the location of your User Profile, in this case C:\\Users\\Philip

<img src='images_mambaforge/img_010.png' alt='img_010' width='350'/>

Installation options will display. In this example, the options shown are the defaults. 

<img src='images_mambaforge/img_011.png' alt='img_011' width='350'/>

A common option (although shown as not recommended) is to add Mambaforge to the Windows Environmental Variables Path. This makes the (base) Python environment available in the Windows Terminal. Note that leaving this option unchecked may cause a minor issue with VSCode. VSCode uses the Windows Terminal and shows an error message when launching a Python script if the (base) Python environment is not added to the path. If this option has not been checked, Mambaforge can be manually added to the Windows Environmental Variables path see:
[Adding Mambaforge to the Windows Environmental Variables Path](./path.md). 

The reason this option is not recommended by default is it can arise to conflicts when multiple Python distributions are installed/uninstalled. In general it is not recommended to install multiple Python distributions and a better practice to stick to only using Mambaforge.

Select Next:

<img src='images_mambaforge/img_012.png' alt='img_012' width='350'/>

Select Finish:

<img src='images_mambaforge/img_013.png' 
alt='img_013' width='350'/>

## Exploring the base Python Environment

Mambaforge should be installed in:

```
%UserProfile%/Mambaforge
```

<img src='images_mambaforge/img_014.png' alt='img_014' width='400'/>

In this folder is a python.exe

<img src='images_mambaforge/img_015.png' 
alt='img_015' width='400'/>

And a Lib subfolder:

<img src='images_mambaforge/img_016.png' alt='img_016' width='450'/>

This Lib subfolder contains Python standard modules. 

These can be in the form of packages and the folder name is essentially the package name. For example in the case of email:

<img src='images_mambaforge/img_017.png' alt='img_017' width='450'/>

In the email folder is a \_\_init\_\_.py which is the initialisation module of the folder:

<img src='images_mambaforge/img_018.png' alt='img_018' width='450'/>

Or in the form of a module.py for example datetime.py

<img src='images_mambaforge/img_019.png' alt='img_019' width='450'/>

## Mambaforge Prompt

The Mambaforge Prompt is used to interact with the Mambaforge installation. In the Start menu this should show as Mambaforge Prompt however it may display as Miniforge Prompt. This is a common bug that is fixed when the installation is updated:

<img src='images_mambaforge/img_020.png' alt='img_020' width='350'/>

This opens a Terminal similar to the Windows Terminal. 

```(base)``` indicates that the Mambaforge Python base environment is selected.

```C:\Users\Philip``` indicates the file path which is ```%UserProfile%``` by default.

```>``` indicates a new prompt.

<img src='images_mambaforge/img_021.png' alt='img_021' width='450'/>

The programming language used by the Mambaforge Prompt by default is CMD. Unfortunately at the time of writing there is no MambaForge PowerShell Prompt. Windows PowerShell (Windows 10/11) and CMD (Legacy Windows 7) are scripting languages that are essentially terminal based equivalents of Windows Explorer. They are used essentially to navigate around the Operating System. In the Mambaforge Prompt, the commands mamba and python are added.

CMD/PowerShell use a syntax of the form:

```
command option -p parametervalue1
command option --parametername2 parametervalue2
command option --parametername3
```

Whereas Python uses the following syntax:

```
function(value1, arg2=value2)
```

The Mambaforge Prompt can be used to invoke Python from the (base) Python environment using:

```
python
```

<img src='images_mambaforge/img_022.png' alt='img_022' width='450'/>

Details about the Python version in (base) will display. Notice the prompt change from ```>``` (CMD) to ```>>>``` (Python):

<img src='images_mambaforge/img_023.png' alt='img_023' width='450'/>

The email package can be imported and the file of its intialisation module viewed using:

```
import email
email.__file__
```

<img src='images_mambaforge/img_024.png' alt='img_024' width='450'/>

The datetime module can be imported and its file viewed using:

```
import datetime
datetime.__file__
```

<img src='images_mambaforge/img_025.png' alt='img_025' width='450'/>

To exit Python the function:

```
exit()
```

can be used. Notice the prompt returns to ```>``` indicating PowerShell.

<img src='images_mambaforge/img_026.png' alt='img_026' width='450'/>

A CMD command such as:

```
cls
```

can be used to clear the screen:

<img src='images_mambaforge/img_027.png' alt='img_027' width='450'/>

And the command:

```
exit
```

can be used to close the Mambaforge Prompt:

<img src='images_mambaforge/img_028.png' alt='img_028' width='450'/>

Notice the subtle difference between the Python function call:

```
exit()
```

And the CMD command:

```
exit
```

Python uses parenthesis to call functions and enclose any function input arguments. CMD, instead uses a space between the command and its input arguments. Do not confuse the two programming languages!

Third-party packages are in the site-packages subfolder

<img src='images_mambaforge/img_029.png' alt='img_029' width='450'/>

In the (base) Python environment this includes te mamba package manager:

<img src='images_mambaforge/img_030.png' alt='img_030' width='450'/>

This can be imported in Python and its initialisation file examined:

<img src='images_mambaforge/img_031.png' alt='img_031' width='450'/>

## Updating the (base) Python Distribution

The CMD command mamba can be used with option and named parameter --all to update all packages:

```
mamba update --all
```

can be used to update all packages in the base Python environment:

<img src='images_mambaforge/img_032.png' alt='img_032' width='450'/>

Notice this searches for updates to all the preinstalled packages:

<img src='images_mambaforge/img_033.png' alt='img_033' width='450'/>

Input ```y``` to proceed with the changes:

<img src='images_mambaforge/img_034.png' alt='img_034' width='450'/>

The changes will be made:

<img src='images_mambaforge/img_035.png' alt='img_035' width='450'/>

They can be seen in the File Explorer:

<img src='images_mambaforge/img_036.png' alt='img_036' width='450'/>

The Mambaforge Prompt should now have the correct name in the Start Menu:

<img src='images_mambaforge/img_037.png' alt='img_037' width='450'/>

## MambaForge Prompt

If the command help is pressed a list of preinstalled CMD commands display. These are shown in upper case but are case insensitive. The most commonly preinstalled commands are:

|command|command description|
|---|---|
|cd|Change Directory|
|cls|Clears the Screen|
|mkdir|Make a Directory|
|rmdir|Removes a Directory|
|type|Displays the contents of a text file|

CMD can also be used to launch Windows Applications for example:

|command|command description|
|---|---|
|notepad|launches notepad|
|calc|launches calculator|
|mspaint|launches paint|

The Mambaforge (base) environment includes:

|command|command description|
|---|---|
|mamba|Mamba package manager|
|python|Python|
|idle|Launches IDLE|

If other IDEs are installed:

|command|command description|
|---|---|
|jupyter lab|Launches JupyterLab (lab gives the option lab)|
|jupyter|Launches Jupyter Notebook (legacy)|
|spyder|Launches Spyder|
|code|Launches VSCode|

In PowerShell most of these commands act as an alias for equivalent an cmdlet.

The Mambaforge Prompt opens in the environmental variable ```%USERPROFILE%``` by default which in my case is ```C:\Users\Philip```. 

Documents is a subfolder and the directory can be changed to Documents using:

```
cd Documents
```

A new Python script file can be created in CMD using:

```
type NUL > script.py
```

In Powershell this is simplified using new item:

```
ni script.py
```


This can be opened in notepad using:

```
notepad script.py
```

The following Python code can be added to the script file using notepad:

```
print('Hello World!')
```

The contents of the file can be viewed using:

```
type script.py
```

The file can be ran in Python using:

```
python script.py
```
