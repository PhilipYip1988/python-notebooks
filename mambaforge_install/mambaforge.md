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

Installation options will display. Mambaforge can optionally be added to the Windows Path however it is not recommended by default. In this example, the options will be left at their defaults: 

<img src='images_mambaforge/img_011.png' alt='img_011' width='350'/>

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

The programming language used by the Mambaforge Prompt is Windows PowerShell which is inbuilt into Windows. It can be used to invoke Python from the (base) Python environment using:

```
python
```

<img src='images_mambaforge/img_022.png' alt='img_022' width='450'/>

Details about the Python version in (base) will display. Notice the prompt change from ```>``` (PowerShell) to ```>>>``` (Python):

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

A PowerShell command such as:

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

And the PowerShell command:

```
exit
```

Python uses parenthesis to call functions and enclose any function input arguments. Powershell, instead uses a space between the command and its input arguments. Do not confuse the two programming languages!

Third-party packages are in the site-packages subfolder

<img src='images_mambaforge/img_029.png' alt='img_029' width='450'/>

In the (base) Python environment this includes te mamba package manager:

<img src='images_mambaforge/img_030.png' alt='img_030' width='450'/>

This can be imported in Python and its initialisation file examined:

<img src='images_mambaforge/img_031.png' alt='img_031' width='450'/>

## Updating the (base) Python Distribution

The PowerShell command:

```
mamba update --all
```

can be used to update all packages in the base Python environment:

<img src='images_mambaforge/img_032.png' alt='img_032' width='450'/>

Notice this searchss for updates to all the preinstalled packages:

<img src='images_mambaforge/img_033.png' alt='img_033' width='450'/>

Input ```y``` to proceed with the changes:

<img src='images_mambaforge/img_034.png' alt='img_034' width='450'/>

The changes will be made:

<img src='images_mambaforge/img_035.png' alt='img_035' width='450'/>

They can be seen in the File Explorer:

<img src='images_mambaforge/img_036.png' alt='img_036' width='450'/>

The Mambaforge Prompt should now have the correct name in the Start Menu:

<img src='images_mambaforge/img_037.png' alt='img_037' width='450'/>
