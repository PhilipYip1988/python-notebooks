# Uninstall

## Anaconda Based Installers

Miniconda is an Anaconda based installer. Other Anaconda based installers include:

|Distribution|base|default channel|official|
|---|---|---|---|
|Anaconda|python conda numpy pandas matplotlib seaborn jupyterlab spyder|conda|yes|
|Miniconda|python conda|conda|yes|
|Miniforge|python conda|conda-forge|no|
|Mambaforge|python mamba|conda-forge|no|

Where ```conda``` is the channel maintained by the Anaconda company and ```conda-forge``` is the community channel. The community conda-forge channel is larger and more up to date than the Anaconda conda channel.

Having multiple Anaconda based installers on your machine can result in conflicts as configuration files may alter some default properties such as the default channel changing the behaviour of the other configurations. 

Moreover these files are typically left behind after an uninstall and not overwritten after a reinstall.

When Anaconda and Miniconda are installed for a User (default), the installation files are in:

```
%USERPROFILE%
```

<img src='images_uninstall/img_001.png' alt='img_001' width='450'/>

Notice that the Anaconda installation has added a ```.condarc``` file:

<img src='images_uninstall/img_002.png' alt='img_002' width='450'/>

This sets the channel to defaults which is ```conda```. Having this file will make the mamba package manager use the ```conda``` channel opposed to the ```conda-forge``` channel resulting in unstable python environments that have mixed channels:

<img src='images_uninstall/img_003.png' alt='img_003' width='450'/>

The .condarc file created by the Anaconda installer which uses ```conda``` channel by default:

```
channels:
  - defaults
```

A .condarc file modified to use the ```conda-forge``` channel and libmamba solver:

```
channels:
   - conda-forge
   - defaults
solver: libmamba
channel_priority: strict
```

## Uninstall

To Uninstall, right click the Start Button and select Installed Apps:

<img src='images_uninstall/img_004.png' alt='img_004' width='250'/>

Uninstall Anaconda, Miniconda, Miniforge or Mambaconda if present. Also uninstall Python if present. You may also want to uninstall any standalone Python IDEs:

<img src='images_uninstall/img_005.png' alt='img_005' width='450'/>

To uninstall an Anaconda based installer double click on its name. Select next:

<img src='images_uninstall/img_006.png' alt='img_006' width='350'/>

Select Uninstall:

<img src='images_uninstall/img_007.png' alt='img_007' width='350'/>

Select yes:

<img src='images_uninstall/img_008.png' alt='img_008' width='300'/>

Select next:

<img src='images_uninstall/img_009.png' alt='img_009' width='350'/>

Select Finish:

<img src='images_uninstall/img_010.png' alt='img_010' width='350'/>

## Windows Environmental Variables Path

Right click the Start button and select System:

<img src='images_uninstall/img_011.png' alt='img_011' width='250'/>

Select Advanced system Settings:

<img src='images_uninstall/img_012.png' alt='img_012' width='400'/>

Select Environmental Variables:

<img src='images_uninstall/img_013.png' alt='img_013' width='400'/>

Then select Path:

<img src='images_uninstall/img_014.png' alt='img_014' width='400'/>

Remove any entries that contain Anaconda, Miniconda, Miniforge, Mambaforge or Python:

<img src='images_uninstall/img_015.png' alt='img_015' width='400'/>

## Purging Configuration Files

The default locations for Anaconda installers are in ```%USERPROFILE%``` if installed as a single user (default) or ```%PROGRAMDATA%``` if installed for all users.

Open up File Explorer. In the addressbar type in:

```
%USERPROFILE%
```

```
%PROGRAMDATA%
```


In either location delete the folders:

* .conda
* .continuum
* .idlerc
* .ipython
* .jupyter
* .matplotlib
* .spyder-py3
* .vscode
* anaconda3
* miniconda3
* miniforge
* mambaforge

And the file:

* .condarc

Open up File Explorer. In the addressbar type in:

```
%APPDATA%
```

Delete the folders:

* .anaconda
* Code
* jupyter
* Thonny

Open up File Explorer. In the addressbar type in:

```
%LOCALAPPDATA%
```

Delete the folders:

* conda
* Jedi
* pip
* scikit-image
* Spyder
* thonny

Delete any left over shortcuts from the two locations:

```
%APPDATA%\Microsoft\Windows\Start Menu\Programs
```

```
%PROGRAMDATA%\Microsoft\Windows\Start Menu\Programs
```

[Return to Miniconda Installation](./readme.md)