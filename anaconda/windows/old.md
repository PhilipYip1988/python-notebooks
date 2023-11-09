
## Initialising the Windows Terminal (Optional)

The Windows Terminal can be initialised directly by using a modified PowerShell Profile that runs the conda activation script. Unfortunately to use this modified profile, the PowerShell Script Execution Policy needs to be set to Unrestricted and this therefore lowers the base security of the Windows OS making it more vulnerable to other malicious scripts. This security Execution Policy is the main reason there is a seperate Anaconda PowerShell Prompt on Windows instead of direct integration with the Windows Terminal.

To initialise Anaconda in PowerShell open up the Windows Terminal and input:

```
Anaconda3\Scripts\conda.exe init powershell
```

<img src='images_install/img_017.png' alt='img_017' width='350'/>

<img src='images_install/img_018.png' alt='img_018' width='350'/>

Once this is done, there is an error message any time the Windows Terminal is opened stating the PowerShell Profile cannot be loaded because running scripts is disabled on this system:

<img src='images_install/img_019.png' alt='img_019' width='350'/>

In order to use this PowerShell Profile, the Script Execution Policy needs to be set to Unrestricted, recall that this lowers the base security of your system leaving it open to other poptentially malicious scripts.

To change this setting the Terminal (Admin) needs to be used:

<img src='images_install/img_020.png' alt='img_020' width='200'/>

Input:

```
Set-ExecutionPolicy -ExecutionPolicy Unrestricted
```

<img src='images_install/img_021.png' alt='img_021' width='350'/>

Close any Terminals. Now the Windows Terminal (User) can be used and the conda environment shows:

<img src='images_install/img_022.png' alt='img_022' width='350'/>

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

## The Windows Environmental Variables Path (Not Recommended)

Adding Anaconda to the Windows Environmental Variables Path adds the following 5 locations to the Windows Environmental Variables Path:

```
%USERPROFILE%\Anaconda3
%USERPROFILE%\Anaconda3\Library\mingw-w64\bin
%USERPROFILE%\Anaconda3\Libraryusr\bin
%USERPROFILE%\Anaconda3\Library\bin
%USERPROFILE%\Anaconda3\Scripts
```

This is automatically carried out when the following option is selected:

<img src='images_install/img_023.png' alt='img_023' width='350'/>

The Windows Terminal essentially checks the folders listed in the Windows Environmental Variables Path for equivalent Windows Applications. For example if the command 

```
python
```

is used in the Windows Terminal. The Windows Terminal will search the first location ```%USERPROFILE%\Anaconda3``` and finds the ```python.exe``` and executes it.

If the commands 

```
conda
idle
spyder
jupyter lab
```

are used in the Windows Terminal. The Windows Terminal will search the first-fourth location and not find anything and then get to the fifth location ```%USERPROFILE%\Anaconda3\Scripts``` and finds the respective ```conda.exe```, ```idle.exe```, ```spyder.exe```, or ```jupyter-lab.exe``` and executes it.

One major drawback of adding the (base) Python environment to the Windows Environmental Path is the Windows Terminal is "locked" to the Windows Environmental Variable Path. 

When multiple Python environments have been created. Notice that activation of a Python environment does nothing and that the base Python environment and Python modules in the base Python environment continue to be used:

<img src='images_install/img_024.png' alt='img_024' width='350'/>

<img src='images_install/img_025.png' alt='img_025' width='350'/>

To manually update the Windows Environmental Variables Path. Right click the start button and select System:

<img src='images_install/img_026.png' alt='img_026' width='150'/>

Select Advanced System Settings:

<img src='images_install/img_027.png' alt='img_027' width='300'/>

Then Environmental Variables:

<img src='images_install/img_028.png' alt='img_028' width='300'/>

Select Path and then Edit. 

If only a single entry is present (default) you may get a single element display:

<img src='images_install/img_029.png' alt='img_029' width='300'/>

Add a semicolon at the end and select OK:

<img src='images_install/img_030.png' alt='img_030' width='300'/>

Then reselect the path and select Edit again:

<img src='images_install/img_031.png' alt='img_031' width='300'/>

This should display the path as a list:

<img src='images_install/img_032.png' alt='img_032' width='300'/>

 The default entry is:

```
%USERPROFILE%\AppData\Local\Microsoft\WindowsApps
```

If Anaconda was added to path the following entries will have been added, the hard path will vary depending on the location of your User Profile:

<img src='images_install/img_033.png' alt='img_033' width='300'/>

If adding the entries manually you can use the environmental variable %USERPROFILE% in the following 5 entries. These 5 entires should be moved to the top:

```
%USERPROFILE%\Anaconda3
%USERPROFILE%\Anaconda3\Library\mingw-w64\bin
%USERPROFILE%\Anaconda3\Libraryusr\bin
%USERPROFILE%\Anaconda3\Library\bin
%USERPROFILE%\Anaconda3\Scripts
```

<img src='images_install/img_034.png' alt='img_034' width='300'/>

For VSCode the following entry should automatically be added:

```
%LOCALAPPDATA%\Programs\Microsoft VS Code\bin
```

The above 5 entries can be removed from the Windows Environmental Variables Path following a similar procedure.