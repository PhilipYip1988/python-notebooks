# Updating Anaconda

The following instructions will work for updating Anaconda 2023-07 or newer to the latest version. Previous versions do not have the libmamba solver and therefore the update procedure may not be as reliable. It is probably easier to uninstall these and install the latest version directly.

The update procedure is different for Anaconda and Miniconda, because Anaconda is a large data science Python distribution and should only be updated collectively using Anaconda's standalone images. Updating a component individually or installing a package from a different channel in the Anaconda base Python environment generally leads to a package that is a dependency for most other packages being removed and most of the packages in the base Python environment being remvoed, generally making it unstable.

Miniconda is lightweight and because there are only a handful of packages in the Miniconda base Python environment, each package can be updated to the latest version.

## Anaconda

### Avoid

The Anaconda base Python environment is a Python distribution and should be updated collectively using the standalone images put together by Anaconda.

The following command should generally be **avoided** in the base Python environment:

```
conda update --all
```

The reason for this is it will attempt to individually update packages to their latest versions and will lead to an unstable base Python environment. Essentially when one package is updated that is a dependency for other packages, the other packages may be removed and therefore the Python environment becomes unstable.

Separate Python environments should be used if you need to use a newer version of a package outside of Anacondas standard image or a package only available on the community channel conda-forge.

### Editing the .condarc

Open the Anaconda PowerShell Prompt from the Start Menu:

<img src='images_update/img_001.png' alt='img_001' width='350'/>

By default it will open in %USERPROFILE%:

<img src='images_update/img_002.png' alt='img_002' width='350'/>

<img src='images_update/img_003.png' alt='img_003' width='350'/>

If a .condrc file is present, it should be deleted using:

```
del .condarc
```

<img src='images_update/img_004.png' alt='img_004' width='350'/>

<img src='images_update/img_005.png' alt='img_005' width='350'/>

A new .condarc file using the libmamba solver and default channels can be created using:

```
conda config --set solver libmamba
```

<img src='images_update/img_006.png' alt='img_006' width='350'/>

<img src='images_update/img_007.png' alt='img_007' width='350'/>

The .condarc file looks like the following:

<img src='images_update/img_008.png' alt='img_008' width='350'/>

## Deactivating the base Environment

To update Anaconda, you will first want to deactivate the base Python environment. To do this use:

```
conda deactivate
```

<img src='images_update/img_009.png' alt='img_009' width='350'/>

Notice there is now no longer any (base) prefix.

### Updating Anaconda

To update the ```conda``` package manager use the command:

```
conda update conda
```

<img src='images_update/img_010.png' alt='img_010' width='350'/>

Notice that this will update the package manager and the entire base Anaconda Python distribution.

Note when updating some packages may be downgraded, this happens when Anaconda deem a version of a package unsuitable and revert to an older version. Confer with [Anaconda Release Notes](https://docs.anaconda.com/free/anaconda/reference/release-notes/) for more details. 

Input 

```
y
``` 

in order to proceed with the changes:

<img src='images_update/img_011.png' alt='img_011' width='350'/>

Anaconda will now be updated:

<img src='images_update/img_012.png' alt='img_012' width='350'/>

The Anaconda Navigator should also be updated using:

```
conda update anaconda-navigator
```

<img src='images_update/img_018.png' alt='img_018' width='350'/>

Input ```y``` in order to proceed with the changes:

<img src='images_update/img_019.png' alt='img_019' width='350'/>

The packages will be downloaded and installed:

<img src='images_update/img_020.png' alt='img_020' width='350'/>

The Anaconda Python distribution is now up to date. 

[Return to Anaconda Tutorial](./readme.md)

## Miniconda

### Editing the .condarc

The conda package manager uses the legacy solver by default. The newer solver libmamba should be used instead:

```
conda config --set solver libmamba
```

For Miniconda, the community conda-forge should be added:

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

<img src='images_update/img_013.png' alt='img_013' width='350'/>

### Updating Miniconda

Because the ```base``` Python distribution is minimal it is possible to update the packages in the Miniconda base environment individually using the command:

```
conda update -c conda-forge --all
```

<img src='images_update/img_014.png' alt='img_014' width='350'/>

Details about the changes will be listed:

<img src='images_update/img_015.png' alt='img_015' width='350'/>

Review the changes and input ```y``` in order to proceed:

<img src='images_update/img_016.png' alt='img_016' width='350'/>

Miniconda will now be updated:

<img src='images_update/img_017.png' alt='img_017' width='350'/>

[Return to Anaconda Tutorial](./readme.md)