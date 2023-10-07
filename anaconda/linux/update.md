# Updating Anaconda

The following instructions will work for updating Anaconda 2023-07 or newer to the latest version. Previous versions do not have the libmamba solver and therefore the update procedure may not be as reliable. It is probably easier to uninstall these and install the latest version directly.

The update procedure is different for Anaconda and Miniconda, because Anaconda is a large data science Python distribution and should only be updated collectively using Anaconda's standalone images. Updating a component individually or installing a package from a different channel in the Anaconda base Python environment generally leads to a package that is a dependency for most other packages being removed and most of the packages in the base Python environment being removed, generally making it unstable.

Miniconda is lightweight and because there are only a handful of packages in the Miniconda base Python environment, each package can be updated to the latest version.

## Anaconda

### Avoid

The Anaconda base Python environment is a Python distribution and should be updated collectively using the standalone images put together by Anaconda.

The following command should generally be **avoided** in the base Python environment:

```
conda update --all
```

The reason for this is it will attempt to individually update packages and will lead to an unstable base Python environment. Essentially when one package is updated that is a dependency for other packages, the other packages may be removed and therefore the Python environment becomes unstable.

Separate Python environments should be used if you need to use a newer version of a package outside of Anacondas standard image or a package only available on the community channel conda-forge.

### Editing the .condarc

Open the Home folder and view Hidden Files. Look for a .condarc file: 

<img src='images_update/img_001.png' alt='img_001' width='350'/>

The Terminal opens in Home by default and the .condarc can be opened in the nano text editor using the command:

```
nano .condarc
```

<img src='images_update/img_002.png' alt='img_002' width='350'/>

The default should look like the following:

<img src='images_update/img_003.png' alt='img_003' width='350'/>

Press ```Ctrl``` + ```x``` to exit. If the .condarc does specifies different channels, remove it using:

```
rm .condarc
```

<img src='images_update/img_004.png' alt='img_004' width='350'/>

<img src='images_update/img_005.png' alt='img_005' width='350'/>

Create a new .condarc file that is configured to use the default channels and libmamba solver using:

```
conda config --set solver libmamba
```

<img src='images_update/img_006.png' alt='img_006' width='350'/>

<img src='images_update/img_007.png' alt='img_007' width='350'/>

This gives an updated .condarc file and its contents can be checked in the terminal text-editor nano using:

```
nano .condarc
```

<img src='images_update/img_008.png' alt='img_008' width='350'/>

Press ```Ctrl``` + ```x``` to exit:

<img src='images_update/img_009.png' alt='img_009' width='350'/>

### Deactivate base

Deactivate the base Python environment using:

```
conda deactivate
```

<img src='images_update/img_010.png' alt='img_010' width='350'/>

### Update the conda Package Manager and Anaconda Distribution

Then use:

```
conda update conda
```

<img src='images_update/img_011.png' alt='img_011' width='350'/>


Note when updating some packages may be downgraded, this happens when Anaconda deem a version of a package unsuitable and revert to an older version. Confer with [Anaconda Release Notes](https://docs.anaconda.com/free/anaconda/reference/release-notes/) for more details. 

Input ```y``` in order to proceed with the changes:

<img src='images_update/img_012.png' alt='img_012' width='350'/>

The packages will be downloaded and installed:

<img src='images_update/img_013.png' alt='img_013' width='350'/>

### Update Anaconda Navigator

The Anaconda Navigator should also be updated using:

```
conda update anaconda-navigator
```

<img src='images_update/img_014.png' alt='img_014' width='350'/>

Input ```y``` in order to proceed with the changes:

<img src='images_update/img_015.png' alt='img_015' width='350'/>

The packages will be downloaded and installed:

<img src='images_update/img_016.png' alt='img_016' width='350'/>

The Anaconda Python distribution is now up to date. 

### LibGL Error

There is a ```LibGL error: mesa iris driver error``` when Anaconda Navigator or any programs which use QT are launched. 

This error is due to the old version of ```libstdcxx-ng``` in the Anaconda base Python environment. Check to see whether or not you have this error by running Anaconda Navigator in the Terminal using:

```
anaconda-navigator
```

<img src='images_update/img_017.png' alt='img_017' width='450'/>

```
Warning: Ignoring XDG_SESSION_TYPE=wayland on Gnome. Use QT_QPA_PLATFORM=wayland to run on Wayland anyway.
libGL error: MESA-LOADER: failed to open iris: /usr/lib/dri/iris_dri.so: cannot open shared object file: No such file or directory (search paths /usr/lib/x86_64-linux-gnu/dri:\$${ORIGIN}/dri:/usr/lib/dri, suffix _dri)
libGL error: failed to load driver: iris
libGL error: MESA-LOADER: failed to open swrast: /usr/lib/dri/swrast_dri.so: cannot open shared object file: No such file or directory (search paths /usr/lib/x86_64-linux-gnu/dri:\$${ORIGIN}/dri:/usr/lib/dri, suffix _dri)
libGL error: failed to load driver: swrast
```

<img src='images_update/img_018.png' alt='img_018' width='450'/>

At the time of writing, the [main libstdcxx-ng channel](https://anaconda.org/main/libstdcxx-ng) is at 11.2.0 and the [community libstdcxx-ng channel](https://anaconda.org/conda-forge/libstdcxx-ng) is at 13.2.0. 

I have submitted a bug on [GitHub Anaconda Navigator Hangs at Loading User... on Ubuntu 23.10 #13278](https://github.com/ContinuumIO/anaconda-issues/issues/13278)

The error message can be addressed by installing the newer version from the community channel using:

```
conda install -c conda-forge libstdcxx-ng
```

**However it is generally bad practice to install packages from mixed channels.** and may lead to an unstable base Python environment when later attempting to update.

<img src='images_update/img_019.png' alt='img_029' width='450'/>

Input ```y``` in order to proceed:

<img src='images_update/img_020.png' alt='img_020' width='450'/>

The package is now installed:

<img src='images_update/img_021.png' alt='img_021' width='450'/>

When Anaconda Navigator is relaunched using:

```
anaconda-navigator
```

There should now just be a warning about using Wayland.

<img src='images_update/img_022.png' alt='img_022' width='450'/>

```
Warning: Ignoring XDG_SESSION_TYPE=wayland on Gnome. Use QT_QPA_PLATFORM=wayland to run on Wayland anyway.
```

<img src='images_update/img_018.png' alt='img_018' width='450'/>

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

### Updating Miniconda

Because the ```base``` Python distribution is minimal it is possible to update the packages in the Miniconda base environment individually using the command:

```
conda update -c conda-forge --all
```


Details about the changes will be listed:


Review the changes and input ```y``` in order to proceed:


Miniconda will now be updated:


[Return to Anaconda Tutorial](./readme.md)