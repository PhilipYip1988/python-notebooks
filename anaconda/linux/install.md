# Installing Anaconda

## Download and Install

The download link for Anaconda can be found on the [Anaconda](https://www.anaconda.com/download) home page. The Linux installer is a bash script file:

<img src='images_install/img_001.png' alt='img_001' width='450'/>

<img src='images_install/img_002.png' alt='img_002' width='450'/>

Open the Downloads folder and right click the downloaded file and select Rename:

<img src='images_install/img_003.png' alt='img_003' width='450'/>

Copy the file name, including the file extension:

<img src='images_install/img_004.png' alt='img_004' width='450'/>

Right click empty space in the folder and select Open in Terminal:

<img src='images_install/img_005.png' alt='img_005' width='450'/>

To begin executing of the shell script input:

```
bash Anaconda3-2023.09-0-Linux-x86_64.sh
```

Amending for the version if you have downloaded a later version:

<img src='images_install/img_006.png' alt='img_006' width='450'/>

Press ```↵```:

<img src='images_install/img_007.png' alt='img_007' width='450'/>

Press ```q``` to quit scrolling through the license agreement:

<img src='images_install/img_008.png' alt='img_008' width='450'/>

Input:

```
yes
```

to accept the license agreement:

<img src='images_install/img_009.png' alt='img_009' width='450'/>

Use the default install location:

<img src='images_install/img_010.png' alt='img_010' width='450'/>

Anaconda will now install.

<img src='images_install/img_011.png' alt='img_011' width='450'/>


<img src='images_install/img_012.png' alt='img_012' width='450'/>

You will be asked if you want to initialise Anaconda. Input:

```
yes
```

to initialise Anaconda3. Unfortunately the option no is preselected so if you pressed ```↵```, you will have installed Anaconda without initialisation like in this example:

<img src='images_install/img_013.png' alt='img_013' width='450'/>

There is now an anaconda3 folder:

<img src='images_install/img_014.png' alt='img_014' width='450'/>

## Initialising Anaconda

Initialisation can be checked by examining the .bashrc file. This file is hidden by default, to view it select Show Hidden Files:

<img src='images_install/img_015.png' alt='img_015' width='450'/>

The .bashrc file can be viewed in Text Editor:

<img src='images_install/img_016.png' alt='img_016' width='450'/>

If initialised there will be a conda code block:

<img src='images_install/img_017.png' alt='img_017' width='450'/>

In this case conda is not initialised and this code block is not present.

In the anaconda3 folder:

<img src='images_install/img_018.png' alt='img_018' width='450'/>

There is a bin subfolder:

<img src='images_install/img_019.png' alt='img_019' width='450'/>

This bin subfolder contains the conda script (no file extension):

<img src='images_install/img_020.png' alt='img_020' width='450'/>

Anaconda can be initialised using:

```
./anaconda3/bin/conda init
```

<img src='images_install/img_021.png' alt='img_021' width='450'/>

This adds the conda commands to the .bashrc:

<img src='images_install/img_022.png' alt='img_022' width='450'/>

The .bashrc can be seen in Text Editor:

<img src='images_install/img_023.png' alt='img_023' width='450'/>

<img src='images_install/img_024.png' alt='img_024' width='450'/>

Close any open any terminals. New terminals will look at the refreshed .bashrc file for commands. You will see a prefix (base) indicating the base Python environment is selected:

<img src='images_install/img_025.png' alt='img_025' width='450'/>

## Anaconda Navigator

On Linux, no shortcuts for Anaconda or Python IDEs installed in the Anaconda base Python environment have Start Menu shortcuts. The Anaconda Navigator can be launched from the Terminal using the command:

```
anaconda-navigator
```

<img src='images_install/img_026.png' alt='img_026' width='450'/>

The terminal will remain busy when the Anaconda Navigator is launched:

<img src='images_install/img_027.png' alt='img_027' width='450'/>

The most commonly used Python IDEs can be launched using their respective tiles in the Anaconda Navigator:

<img src='images_install/img_028.png' alt='img_028' width='450'/>

Anaconda is now installed.

## LibGL Error

There is a ```LibGL error: mesa iris driver error``` when Anaconda Navigator or any programs which use QT are launched. This error is due to the old version of ```libstdcxx-ng``` in the Anaconda base Python environment. This should be fixed when Anaconda is updated. For more details see Updating Anaconda. 

[Return to Anaconda Tutorial](./readme.md)