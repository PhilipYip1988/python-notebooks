# Installing Anaconda

## Download

The download link for Anaconda can be found on the [Anaconda](https://www.anaconda.com/download) home page. The Linux installer is a has a ```.sh``` file extension:

<img src='images_install/img_001.png' alt='img_001' width='450'/>

<img src='images_install/img_002.png' alt='img_002' width='450'/>

## Install

Bourne Again Shell (bash) is the native scripting language of the Linux Terminal. To run a shell script the command ```bash``` is used and the .sh file is supplied as a command line argument.

To get the name of the file. Open the Downloads folder and right click the downloaded file and select Rename:

<img src='images_install/img_003.png' alt='img_003' width='450'/>

Highlight the file name, including the file extension and press ```Ctrl``` + ```c``` to copy:

<img src='images_install/img_004.png' alt='img_004' width='450'/>

If the Terminal is open from All Applications. The Prompt will look like:

```
user@pc~$:
```

where ```~``` is the current working directory. The Linux Terminal uses ```~``` for the Home folder found in Files. To change directory, the command ```cd``` can be used alongside the directory as an input argument:

```
cd ~/Downloads
```

Notice that the prompt is now:

```
user@pc:~/Downloads$
```

Alternatively open the Downloads folder in files and right click empty space in files and select Open in Terminal:

<img src='images_install/img_005.png' alt='img_005' width='450'/>

To begin executing the shell script input:

```bash
bash Anaconda3-2023.09-0-Linux-x86_64.sh
```

Note because the Terminals working directory is Downloads, the directory will not have to be provided as part of the command line argument to the file. Otherwise the following would have to be used:

```bash
bash ~/Downloads/Anaconda3-2023.09-0-Linux-x86_64.sh
```

Note that the Terminal uses the shortcut key ```Ctrl``` + ```c``` to cancel the current running operation. The shortcut keys for Copy and Paste are therefore ```Ctrl```, ```⇧``` + ```c``` and ```Ctrl```, ```⇧``` + ```v``` respectively.

The following output will display:

```
Welcome to Anaconda3 2023.09-0

In order to continue the installation process, please review the license
agreement.
Please, press ENTER to continue
>>> 
```

Press ```↵``` to begin scrolling through the license agreement:

```
==================================================
End User License Agreement - Anaconda Distribution
==================================================

Copyright 2015-2023, Anaconda, Inc.

All rights reserved under the 3-clause BSD License:

This End User License Agreement (the "Agreement") is a legal agreement be
tween you and Anaconda, Inc. ("Anaconda") and governs your use of Anacond
a Distribution (which was formerly known as Anaconda Individual Edition).

Subject to the terms of this Agreement, Anaconda hereby grants you a non-
exclusive, non-transferable license to:

  * Install and use the Anaconda Distribution (which was formerly known a
s Anaconda Individual Edition),
  * Modify and create derivative works of sample source code delivered in
--More--
```

To quit scrolling press ```q```. The following output will now display, prompting to accept of decline the license agreement:

```
Do you accept the license terms? [yes|no]
[no] >>>
```

Input ```yes``` to proceed. The following output will display:

```
Anaconda3 will now be installed into this location:
/home/philip/anaconda3

  - Press ENTER to confirm the location
  - Press CTRL-C to abort the installation
  - Or specify a different location below

[/home/philip/anaconda3] >>> 
```

It is recommended to install anaconda3 in its default location. Press ```↵``` to proceed. The files will extract and the following output will now display when the installation is successful:

```
PREFIX=/home/philip/anaconda3
Unpacking payload ...

Downloading and Extracting Packages

Preparing transaction: done
Executing transaction: / 

    Installed package of scikit-learn can be accelerated using scikit-learn-intelex.
    More details are available here: https://intel.github.io/scikit-learn-intelex

    For example:

        $ conda install scikit-learn-intelex
        $ python -m sklearnex my_application.py

    

done
installation finished.
```

## Initialisation

The following output will display, prompting for initialisation. Initialisation adds a code block to the .condarc file which is a hidden file containing scripts that the Linux Terminal runs when opened and also a list of directories that the Linux Terminal uses when looking for commands:

```
Do you wish to update your shell profile to automatically initialize conda?
This will activate conda on startup and change the command prompt when activated.
If you'd prefer that conda's base environment not be activated on startup,
   run the following command when conda is activated:

conda config --set auto_activate_base false

You can undo this by running `conda init --reverse $SHELL`? [yes|no]
[no] >>> 
```

Unfortunately the default option is no, meaning Anaconda is installed but not the Linux Terminal is initialised with its commands. Input ```yes```. The output will display a list of files which correspond to shell initialisation. Most will be unmodified however the .bashrc file will be modified:

```
no change     ~/anaconda3/condabin/conda
no change     ~/anaconda3/bin/conda
no change     ~/anaconda3/bin/conda-env
no change     ~/anaconda3/bin/activate
no change     ~/anaconda3/bin/deactivate
no change     ~/anaconda3/etc/profile.d/conda.sh
no change     ~/anaconda3/etc/fish/conf.d/conda.fish
no change     ~/anaconda3/shell/condabin/Conda.psm1
no change     ~/anaconda3/shell/condabin/conda-hook.ps1
no change     ~/anaconda3/lib/python3.11/site-packages/xontrib/conda.xsh
no change     ~/anaconda3/etc/profile.d/conda.csh
modified      ~/.bashrc

==> For changes to take effect, close and re-open your current shell. <==

Thank you for installing Anaconda3!
```

The end of the output states **For changes to take effect, close and re-open your current shell**. When a new Terminal instance is opened, it will look at the updated ```.bashrc``` file, run a script to activate the conda (base) environment and therefore look in additional locations for commands.

When the Terminal is open the bash prompt will display:

```
(base) user@pc~$: 
```

Instead of:

```
user@pc~$:
```

This means the conda (base) Python environment is selected.

Because the default option for intialisation is no, many new users to Anaconda install it without initialising it. If this has happened open up the Terminal and input:

```
~/anaconda3/bin/conda init bash
```

This will display the output:

```
no change     ~/anaconda3/condabin/conda
no change     ~/anaconda3/bin/conda
no change     ~/anaconda3/bin/conda-env
no change     ~/anaconda3/bin/activate
no change     ~/anaconda3/bin/deactivate
no change     ~/anaconda3/etc/profile.d/conda.sh
no change     ~/anaconda3/etc/fish/conf.d/conda.fish
no change     ~/anaconda3/shell/condabin/Conda.psm1
no change     ~/anaconda3/shell/condabin/conda-hook.ps1
no change     ~/anaconda3/lib/python3.11/site-packages/xontrib/conda.xsh
no change     ~/anaconda3/etc/profile.d/conda.csh
modified      ~/.bashrc

==> For changes to take effect, close and re-open your current shell. <==
```

When the Terminal is closed and opened the bash prompt should now display:

```
(base) user@pc~$: 
```

Initialisation can be reversed using:

```
~/anaconda3/bin/conda init bash --reverse
```

## Updating Anaconda

To update Anaconda, the (base) Python environment should be deactivated using:

```
conda deactivate
```

This displays a normal bash prompt without the (base) prefix. The conda package manager can be updated using:

```
conda update conda
```

This will look for updates to the conda package manager and in turn update the entire Anaconda Python distribution. The output will display:

```
Collecting package metadata (current_repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: /home/philip/anaconda3

  added / updated specs:
    - conda
```

Followed by details about the number of packages to be downloaded:

```
The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    aiobotocore-2.7.0          |  py311h06a4308_0         149 KB
    aiohttp-3.9.0              |  py311h5eee18b_0         824 KB
    anaconda-cloud-auth-0.1.4  |  py311h06a4308_0          38 KB
    archspec-0.2.1             |     pyhd3eb1b0_0          39 KB
    astropy-5.3.4              |  py311hf4808d0_0         9.9 MB
    async-lru-2.0.4            |  py311h06a4308_0          20 KB
    attrs-23.1.0               |  py311h06a4308_0         161 KB
    black-23.11.0              |  py311h06a4308_0         356 KB
    bokeh-3.3.0                |  py311h92b7b1e_0         5.7 MB
    boost-cpp-1.82.0           |       hdb19cb5_2          11 KB
    botocore-1.31.64           |  py311h06a4308_0         6.9 MB
    brotli-python-1.0.9        |  py311h6a678d5_7         318 KB
    c-blosc2-2.10.5            |       h80c7b02_0         322 KB
    certifi-2023.11.17         |  py311h06a4308_0         159 KB
    cffi-1.16.0                |  py311h5eee18b_0         314 KB
    click-8.1.7                |  py311h06a4308_0         221 KB
    conda-23.11.0              |  py311h06a4308_0         1.3 MB
    conda-build-3.28.1         |  py311h06a4308_0         834 KB
    conda-libmamba-solver-23.11.1|  py311h06a4308_0         104 KB
    contourpy-1.2.0            |  py311hdb19cb5_0         263 KB
    cookiecutter-2.5.0         |  py311h06a4308_0         140 KB
    curl-8.4.0                 |       hdbd6064_1          85 KB
    cytoolz-0.12.2             |  py311h5eee18b_0         417 KB
    dal-2023.1.1               |   hdb19cb5_48680        36.9 MB
    dask-2023.11.0             |  py311h06a4308_0           5 KB
    dask-core-2023.11.0        |  py311h06a4308_0         2.9 MB
    datashader-0.16.0          |  py311h06a4308_0        17.1 MB
    distributed-2023.11.0      |  py311h06a4308_0         1.6 MB
    distro-1.8.0               |  py311h06a4308_0          37 KB
    filelock-3.13.1            |  py311h06a4308_0          24 KB
    frozenlist-1.4.0           |  py311h5eee18b_0          52 KB
    fsspec-2023.10.0           |  py311h06a4308_0         364 KB
    holoviews-1.18.1           |  py311h06a4308_0         5.1 MB
    huggingface_hub-0.17.3     |  py311h06a4308_0         451 KB
    hvplot-0.9.0               |  py311h06a4308_0         3.2 MB
    icu-73.1                   |       h6a678d5_0        25.9 MB
    imageio-2.31.4             |  py311h06a4308_0         625 KB
    imbalanced-learn-0.11.0    |  py311h06a4308_1         376 KB
    intel-openmp-2023.1.0      |   hdb19cb5_46306        17.2 MB
    jmespath-1.0.1             |  py311h06a4308_0          48 KB
    jsonschema-4.19.2          |  py311h06a4308_0         190 KB
    jsonschema-specifications-2023.7.1|  py311h06a4308_0          15 KB
    jupyter-lsp-2.2.0          |  py311h06a4308_0         107 KB
    jupyter_client-8.6.0       |  py311h06a4308_0         233 KB
    jupyter_core-5.5.0         |  py311h06a4308_0          91 KB
    jupyter_events-0.8.0       |  py311h06a4308_0          41 KB
    jupyter_server-2.10.0      |  py311h06a4308_0         577 KB
    jupyter_server_terminals-0.4.4|  py311h06a4308_1          27 KB
    jupyterlab-4.0.8           |  py311h06a4308_0         4.5 MB
    jupyterlab_server-2.25.1   |  py311h06a4308_0         113 KB
    jupyterlab_widgets-3.0.9   |  py311h06a4308_0         194 KB
    lazy_loader-0.3            |  py311h06a4308_0          20 KB
    libboost-1.82.0            |       h109eef0_2        19.5 MB
    libcurl-8.4.0              |       h251f7ec_1         411 KB
    libdeflate-1.17            |       h5eee18b_1          64 KB
    libmamba-1.5.3             |       haf1ee3a_0         1.9 MB
    libmambapy-1.5.3           |  py311h2dafd23_0         314 KB
    libnghttp2-1.57.0          |       h2d74bed_0         674 KB
    libxml2-2.10.4             |       hf1b16e4_1         753 KB
    libxslt-1.1.37             |       h5eee18b_1         266 KB
    llvmlite-0.41.0            |  py311he621ea3_0         3.6 MB
    matplotlib-3.8.0           |  py311h06a4308_0           8 KB
    matplotlib-base-3.8.0      |  py311ha02d727_0         7.7 MB
    menuinst-2.0.0             |  py311h06a4308_0         167 KB
    mistune-2.0.4              |  py311h06a4308_0         107 KB
    mkl-2023.1.0               |   h213fc3f_46344       171.5 MB
    more-itertools-10.1.0      |  py311h06a4308_0         103 KB
    multidict-6.0.4            |  py311h5eee18b_0          59 KB
    nbclient-0.8.0             |  py311h06a4308_0         120 KB
    nbconvert-7.10.0           |  py311h06a4308_0         513 KB
    notebook-7.0.6             |  py311h06a4308_0         3.1 MB
    notebook-shim-0.2.3        |  py311h06a4308_0          26 KB
    numba-0.58.1               |  py311ha02d727_0         5.8 MB
    numexpr-2.8.7              |  py311h65dcdc2_0         167 KB
    numpy-1.26.2               |  py311h08b1b3b_0          10 KB
    numpy-base-1.26.2          |  py311hf175353_0         8.2 MB
    openssl-3.0.12             |       h7f8727e_0         5.2 MB
    overrides-7.4.0            |  py311h06a4308_0          36 KB
    pandas-2.1.1               |  py311ha02d727_0        14.9 MB
    panel-1.3.1                |  py311h06a4308_0        14.7 MB
    param-2.0.1                |  py311h06a4308_0         259 KB
    partd-1.4.1                |  py311h06a4308_0          48 KB
    pillow-10.0.1              |  py311ha6cbd5a_0         896 KB
    py-cpuinfo-9.0.0           |  py311h06a4308_0          64 KB
    pycosat-0.6.6              |  py311h5eee18b_0          90 KB
    pydantic-1.10.12           |  py311h5eee18b_1         2.4 MB
    pyodbc-4.0.39              |  py311h6a678d5_0          78 KB
    pyqt-5.15.10               |  py311h6a678d5_0         5.7 MB
    pyqt5-sip-12.13.0          |  py311h5eee18b_0          95 KB
    pyqtwebengine-5.15.10      |  py311h6a678d5_0         171 KB
    pytoolconfig-1.2.6         |  py311h06a4308_0          35 KB
    pyviz_comms-3.0.0          |  py311h06a4308_0          56 KB
    pyyaml-6.0.1               |  py311h5eee18b_0         210 KB
    pyzmq-25.1.0               |  py311h6a678d5_0         538 KB
    qt-main-5.15.2             |      h53bd1ea_10        53.7 MB
    qtpy-2.4.1                 |  py311h06a4308_0         129 KB
    queuelib-1.6.2             |  py311h06a4308_0          34 KB
    referencing-0.30.2         |  py311h06a4308_0          77 KB
    regex-2023.10.3            |  py311h5eee18b_0         427 KB
    rich-13.3.5                |  py311h06a4308_0         560 KB
    rpds-py-0.10.6             |  py311hb02cf49_0        1007 KB
    s3fs-2023.10.0             |  py311h06a4308_0          78 KB
    safetensors-0.4.0          |  py311h24d97f6_0         1.1 MB
    scikit-learn-1.2.2         |  py311h6a678d5_1         8.8 MB
    scipy-1.11.4               |  py311h08b1b3b_0        22.0 MB
    semver-2.13.0              |     pyhd3eb1b0_0          16 KB
    send2trash-1.8.2           |  py311h06a4308_0          32 KB
    sip-6.7.12                 |  py311h6a678d5_0         603 KB
    soupsieve-2.5              |  py311h06a4308_0          92 KB
    sqlalchemy-2.0.21          |  py311h5eee18b_0         3.8 MB
    sympy-1.12                 |  py311h06a4308_0        14.4 MB
    tabulate-0.9.0             |  py311h06a4308_0          70 KB
    tokenizers-0.13.3          |  py311h22610ee_0         4.4 MB
    tornado-6.3.3              |  py311h5eee18b_0         852 KB
    truststore-0.8.0           |  py311h06a4308_0          43 KB
    urllib3-1.26.18            |  py311h06a4308_0         251 KB
    xz-5.4.5                   |       h5eee18b_0         646 KB
    yaml-cpp-0.8.0             |       h6a678d5_0         607 KB
    yarl-1.9.3                 |  py311h5eee18b_0         127 KB
    zict-3.0.0                 |  py311h06a4308_0         119 KB
    ------------------------------------------------------------
                                           Total:       530.6 MB
```

Followed by details about the number of packages to be installed:

```
The following NEW packages will be INSTALLED:

  archspec           pkgs/main/noarch::archspec-0.2.1-pyhd3eb1b0_0 
  async-lru          pkgs/main/linux-64::async-lru-2.0.4-py311h06a4308_0 
  brotli-python      pkgs/main/linux-64::brotli-python-1.0.9-py311h6a678d5_7 
  distro             pkgs/main/linux-64::distro-1.8.0-py311h06a4308_0 
  jsonschema-specif~ pkgs/main/linux-64::jsonschema-specifications-2023.7.1-py311h06a4308_0 
  jupyter-lsp        pkgs/main/linux-64::jupyter-lsp-2.2.0-py311h06a4308_0 
  jupyter_server_te~ pkgs/main/linux-64::jupyter_server_terminals-0.4.4-py311h06a4308_1 
  menuinst           pkgs/main/linux-64::menuinst-2.0.0-py311h06a4308_0 
  overrides          pkgs/main/linux-64::overrides-7.4.0-py311h06a4308_0 
  referencing        pkgs/main/linux-64::referencing-0.30.2-py311h06a4308_0 
  rich               pkgs/main/linux-64::rich-13.3.5-py311h06a4308_0 
  rpds-py            pkgs/main/linux-64::rpds-py-0.10.6-py311hb02cf49_0 
  semver             pkgs/main/noarch::semver-2.13.0-pyhd3eb1b0_0 
  truststore         pkgs/main/linux-64::truststore-0.8.0-py311h06a4308_0 
```


Followed by details about packages to be removed. Note that this should only be a small number of packages that have become obsolete:

```
The following packages will be REMOVED:

  aiofiles-22.1.0-py311h06a4308_0
  aiosqlite-0.18.0-py311h06a4308_0
  async-timeout-4.0.2-py311h06a4308_0
  brotlipy-0.7.0-py311h5eee18b_1002
  datashape-0.5.4-py311h06a4308_1
  glob2-0.7-pyhd3eb1b0_0
  jinja2-time-0.2.0-pyhd3eb1b0_3
  jupyter_server_fileid-0.9.0-py311h06a4308_0
  jupyter_server_ydoc-0.8.0-py311h06a4308_1
  jupyter_ydoc-0.2.4-py311h06a4308_0
  nbclassic-0.5.5-py311h06a4308_0
  poyo-0.5.0-pyhd3eb1b0_0
  pyrsistent-0.18.0-py311h5eee18b_0
  qtwebkit-5.212-h3fafdc1_5
  y-py-0.5.9-py311h52d8a92_0
  ypy-websocket-0.8.2-py311h06a4308_0
```

Followed by details about packages to be updated:

```
The following packages will be UPDATED:

  aiobotocore                         2.5.0-py311h06a4308_0 --> 2.7.0-py311h06a4308_0 
  aiohttp                             3.8.5-py311h5eee18b_0 --> 3.9.0-py311h5eee18b_0 
  anaconda-cloud-au~                  0.1.3-py311h06a4308_0 --> 0.1.4-py311h06a4308_0 
  astropy                               5.1-py311hbed6279_0 --> 5.3.4-py311hf4808d0_0 
  attrs                              22.1.0-py311h06a4308_0 --> 23.1.0-py311h06a4308_0 
  black                              23.3.0-py311h06a4308_0 --> 23.11.0-py311h06a4308_0 
  bokeh                               3.2.1-py311h92b7b1e_0 --> 3.3.0-py311h92b7b1e_0 
  boost-cpp                              1.73.0-h7f8727e_12 --> 1.82.0-hdb19cb5_2 
  botocore                          1.29.76-py311h06a4308_0 --> 1.31.64-py311h06a4308_0 
  c-blosc2                                 2.8.0-h6a678d5_0 --> 2.10.5-h80c7b02_0 
  certifi                         2023.7.22-py311h06a4308_0 --> 2023.11.17-py311h06a4308_0 
  cffi                               1.15.1-py311h5eee18b_3 --> 1.16.0-py311h5eee18b_0 
  click                               8.0.4-py311h06a4308_0 --> 8.1.7-py311h06a4308_0 
  conda                              23.7.4-py311h06a4308_0 --> 23.11.0-py311h06a4308_0 
  conda-build                        3.26.1-py311h06a4308_0 --> 3.28.1-py311h06a4308_0 
  conda-libmamba-so~                 23.7.0-py311h06a4308_0 --> 23.11.1-py311h06a4308_0 
  contourpy                           1.0.5-py311hdb19cb5_0 --> 1.2.0-py311hdb19cb5_0 
  cookiecutter       pkgs/main/noarch::cookiecutter-1.7.3-~ --> pkgs/main/linux-64::cookiecutter-2.5.0-py311h06a4308_0 
  curl                                     8.2.1-hdbd6064_0 --> 8.4.0-hdbd6064_1 
  cytoolz                            0.12.0-py311h5eee18b_0 --> 0.12.2-py311h5eee18b_0 
  dal                               2023.1.1-hdb19cb5_48679 --> 2023.1.1-hdb19cb5_48680 
  dask                             2023.6.0-py311h06a4308_0 --> 2023.11.0-py311h06a4308_0 
  dask-core                        2023.6.0-py311h06a4308_0 --> 2023.11.0-py311h06a4308_0 
  datashader                         0.15.2-py311h06a4308_0 --> 0.16.0-py311h06a4308_0 
  distributed                      2023.6.0-py311h06a4308_0 --> 2023.11.0-py311h06a4308_0 
  filelock                            3.9.0-py311h06a4308_0 --> 3.13.1-py311h06a4308_0 
  frozenlist                          1.3.3-py311h5eee18b_0 --> 1.4.0-py311h5eee18b_0 
  fsspec                           2023.4.0-py311h06a4308_0 --> 2023.10.0-py311h06a4308_0 
  holoviews                          1.17.1-py311h06a4308_0 --> 1.18.1-py311h06a4308_0 
  huggingface_hub                    0.15.1-py311h06a4308_0 --> 0.17.3-py311h06a4308_0 
  hvplot                              0.8.4-py311h06a4308_0 --> 0.9.0-py311h06a4308_0 
  icu                                       58.2-he6710b0_3 --> 73.1-h6a678d5_0 
  imageio                            2.31.1-py311h06a4308_0 --> 2.31.4-py311h06a4308_0 
  imbalanced-learn                   0.10.1-py311h06a4308_1 --> 0.11.0-py311h06a4308_1 
  intel-openmp                      2023.1.0-hdb19cb5_46305 --> 2023.1.0-hdb19cb5_46306 
  jmespath           pkgs/main/noarch::jmespath-0.10.0-pyh~ --> pkgs/main/linux-64::jmespath-1.0.1-py311h06a4308_0 
  jsonschema                         4.17.3-py311h06a4308_0 --> 4.19.2-py311h06a4308_0 
  jupyter_client                      7.4.9-py311h06a4308_0 --> 8.6.0-py311h06a4308_0 
  jupyter_core                        5.3.0-py311h06a4308_0 --> 5.5.0-py311h06a4308_0 
  jupyter_events                      0.6.3-py311h06a4308_0 --> 0.8.0-py311h06a4308_0 
  jupyter_server                     1.23.4-py311h06a4308_0 --> 2.10.0-py311h06a4308_0 
  jupyterlab                          3.6.3-py311h06a4308_0 --> 4.0.8-py311h06a4308_0 
  jupyterlab_server                  2.22.0-py311h06a4308_0 --> 2.25.1-py311h06a4308_0 
  jupyterlab_widgets                  3.0.5-py311h06a4308_0 --> 3.0.9-py311h06a4308_0 
  lazy_loader                           0.2-py311h06a4308_0 --> 0.3-py311h06a4308_0 
  libboost                               1.73.0-h28710b8_12 --> 1.82.0-h109eef0_2 
  libcurl                                  8.2.1-h251f7ec_0 --> 8.4.0-h251f7ec_1 
  libdeflate                                1.17-h5eee18b_0 --> 1.17-h5eee18b_1 
  libmamba                                 1.5.1-haf1ee3a_0 --> 1.5.3-haf1ee3a_0 
  libmambapy                          1.5.1-py311h2dafd23_0 --> 1.5.3-py311h2dafd23_0 
  libnghttp2                              1.52.0-h2d74bed_1 --> 1.57.0-h2d74bed_0 
  libxml2                                 2.10.4-hcbfbd50_0 --> 2.10.4-hf1b16e4_1 
  libxslt                                 1.1.37-h2085143_0 --> 1.1.37-h5eee18b_1 
  llvmlite                           0.40.0-py311he621ea3_0 --> 0.41.0-py311he621ea3_0 
  matplotlib                          3.7.2-py311h06a4308_0 --> 3.8.0-py311h06a4308_0 
  matplotlib-base                     3.7.2-py311ha02d727_0 --> 3.8.0-py311ha02d727_0 
  mistune                          0.8.4-py311h5eee18b_1000 --> 2.0.4-py311h06a4308_0 
  mkl                               2023.1.0-h213fc3f_46343 --> 2023.1.0-h213fc3f_46344 
  more-itertools     pkgs/main/noarch::more-itertools-8.12~ --> pkgs/main/linux-64::more-itertools-10.1.0-py311h06a4308_0 
  multidict                           6.0.2-py311h5eee18b_0 --> 6.0.4-py311h5eee18b_0 
  nbclient                           0.5.13-py311h06a4308_0 --> 0.8.0-py311h06a4308_0 
  nbconvert                           6.5.4-py311h06a4308_0 --> 7.10.0-py311h06a4308_0 
  notebook                            6.5.4-py311h06a4308_1 --> 7.0.6-py311h06a4308_0 
  notebook-shim                       0.2.2-py311h06a4308_0 --> 0.2.3-py311h06a4308_0 
  numba                              0.57.1-py311ha02d727_0 --> 0.58.1-py311ha02d727_0 
  numexpr                             2.8.4-py311h65dcdc2_1 --> 2.8.7-py311h65dcdc2_0 
  numpy                              1.24.3-py311h08b1b3b_1 --> 1.26.2-py311h08b1b3b_0 
  numpy-base                         1.24.3-py311hf175353_1 --> 1.26.2-py311hf175353_0 
  openssl                                 3.0.10-h7f8727e_2 --> 3.0.12-h7f8727e_0 
  pandas                              2.0.3-py311ha02d727_0 --> 2.1.1-py311ha02d727_0 
  panel                               1.2.3-py311h06a4308_0 --> 1.3.1-py311h06a4308_0 
  param                              1.13.0-py311h06a4308_0 --> 2.0.1-py311h06a4308_0 
  partd                               1.4.0-py311h06a4308_0 --> 1.4.1-py311h06a4308_0 
  pillow                              9.4.0-py311h6a678d5_1 --> 10.0.1-py311ha6cbd5a_0 
  py-cpuinfo         pkgs/main/noarch::py-cpuinfo-8.0.0-py~ --> pkgs/main/linux-64::py-cpuinfo-9.0.0-py311h06a4308_0 
  pycosat                             0.6.4-py311h5eee18b_0 --> 0.6.6-py311h5eee18b_0 
  pydantic                           1.10.8-py311h5eee18b_0 --> 1.10.12-py311h5eee18b_1 
  pyodbc                             4.0.34-py311h6a678d5_0 --> 4.0.39-py311h6a678d5_0 
  pyqt                               5.15.7-py311h6a678d5_0 --> 5.15.10-py311h6a678d5_0 
  pyqt5-sip                         12.11.0-py311h6a678d5_0 --> 12.13.0-py311h5eee18b_0 
  pyqtwebengine                      5.15.7-py311h6a678d5_0 --> 5.15.10-py311h6a678d5_0 
  pytoolconfig                        1.2.5-py311h06a4308_1 --> 1.2.6-py311h06a4308_0 
  pyviz_comms                         2.3.0-py311h06a4308_0 --> 3.0.0-py311h06a4308_0 
  pyyaml                                6.0-py311h5eee18b_1 --> 6.0.1-py311h5eee18b_0 
  pyzmq                              23.2.0-py311h6a678d5_0 --> 25.1.0-py311h6a678d5_0 
  qt-main                                 5.15.2-h7358343_9 --> 5.15.2-h53bd1ea_10 
  qtpy                                2.2.0-py311h06a4308_0 --> 2.4.1-py311h06a4308_0 
  queuelib                            1.5.0-py311h06a4308_0 --> 1.6.2-py311h06a4308_0 
  regex                            2022.7.9-py311h5eee18b_0 --> 2023.10.3-py311h5eee18b_0 
  s3fs                             2023.4.0-py311h06a4308_0 --> 2023.10.0-py311h06a4308_0 
  safetensors                         0.3.2-py311hb02cf49_0 --> 0.4.0-py311h24d97f6_0 
  scipy                              1.11.1-py311h08b1b3b_0 --> 1.11.4-py311h08b1b3b_0 
  send2trash         pkgs/main/noarch::send2trash-1.8.0-py~ --> pkgs/main/linux-64::send2trash-1.8.2-py311h06a4308_0 
  sip                                 6.6.2-py311h6a678d5_0 --> 6.7.12-py311h6a678d5_0 
  soupsieve                             2.4-py311h06a4308_0 --> 2.5-py311h06a4308_0 
  sqlalchemy                         1.4.39-py311h5eee18b_0 --> 2.0.21-py311h5eee18b_0 
  sympy                              1.11.1-py311h06a4308_0 --> 1.12-py311h06a4308_0 
  tabulate                           0.8.10-py311h06a4308_0 --> 0.9.0-py311h06a4308_0 
  tokenizers                         0.13.2-py311h22610ee_1 --> 0.13.3-py311h22610ee_0 
  tornado                             6.3.2-py311h5eee18b_0 --> 6.3.3-py311h5eee18b_0 
  urllib3                           1.26.16-py311h06a4308_0 --> 1.26.18-py311h06a4308_0 
  xz                                       5.4.2-h5eee18b_0 --> 5.4.5-h5eee18b_0 
  yaml-cpp                                 0.7.0-h295c915_1 --> 0.8.0-h6a678d5_0 
  yarl                                1.8.1-py311h5eee18b_0 --> 1.9.3-py311h5eee18b_0 
  zict                                2.2.0-py311h06a4308_0 --> 3.0.0-py311h06a4308_0 
```

Followed by details about packages to be downgraded. A small number of packages will be downgraded, normally to a more stable version:

```
The following packages will be DOWNGRADED:

  scikit-learn                        1.3.0-py311ha02d727_0 --> 1.2.2-py311h6a678d5_1 
```

The output will then prompt to proceed:

```
Proceed ([y]/n)? 
```

Input ```y```. The output will now display:

```
Downloading and Extracting Packages
                                                                                                                              
Preparing transaction: done                                                                                                   
Verifying transaction: done                                                                                                   
Executing transaction: -                                                                                                      
                                                                                                                              
    Installed package of scikit-learn can be accelerated using scikit-learn-intelex.                                          
    More details are available here: https://intel.github.io/scikit-learn-intelex                                             
                                                                                                                              
    For example:                                                                                                              
                                                                                                                              
        $ conda install scikit-learn-intelex                                                                                  
        $ python -m sklearnex my_application.py                                                                               
                                                                                                                              
                                                                                                                              
                                                                                                                              
done    
```

The conda package manager will now be updated alongside most of the other packages in the (base) Python environment. A new prompt will display once the update has finished.

The conda package manager can also be used to update the anaconda-navigator:

```bash
conda update anaconda-navigator
```

The following output will display:

```
Channels:
 - defaults
Platform: linux-64
Collecting package metadata (repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: /home/philip/anaconda3

  added / updated specs:
    - anaconda-navigator


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    anaconda-navigator-2.5.1   |  py311h06a4308_0         5.6 MB
    ------------------------------------------------------------
                                           Total:         5.6 MB

The following packages will be UPDATED:

  anaconda-navigator                  2.5.0-py311h06a4308_0 --> 2.5.1-py311h06a4308_0 


Proceed ([y]/n)?
```

To proceed input ```y```. The output will now display:

```
Downloading and Extracting Packages:
                                                                                                                              
Preparing transaction: done
Verifying transaction: done
Executing transaction: done
```

The Anaconda Python distribution is now up to date. It is recommended to periodically check for updates.

To reactivate the (base) conda Python environment use:

```
conda activate base
```

The (base) prefix should now display in the bash prompt.

## The Bin Folder and Python Applications

In the anaconda3 folder there is a bin subfolder:

<img src='images_install/img_026.png' alt='img_026' width='450'/>

This contains a number of applications:

<img src='images_install/img_027.png' alt='img_027' width='450'/>

### Python

If a search for python is made, notice that there is:

* python
* python3
* python3.1
* python3.11 

These are all the same application... The reason for these aliases is historical. When python3 was first released both python2 and python3 were preinstalled in Linux and the name python3 was used to distinguish between python (which was python2) and python3. Now python2 has reached end of life and only python3 is preinstalled so all of these aliases point to the same version and it is recommended to just use python. 

<img src='images_install/img_028.png' alt='img_028' width='450'/>

Python can be launched using:

```bash
~/anaconda3/bin/python
```

The output will display details about the Python application and then display a Python prompt ```>>>``` from the Python application:

```
Python 3.11.5 (main, Sep 11 2023, 13:54:46) [GCC 11.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

To ```exit``` the Python application, the Python function ```exit``` needs to be used:

```python
exit()
```

A new bash prompt will display.

Because the base Python environment is initialised, the location of the python application does not need to be supplied. Instead the Linux Terminal will look in the ~/anaconda3/bin folder by default and find the python program:

```bash
python
```

Therefore the same output from before will display:

```
Python 3.11.5 (main, Sep 11 2023, 13:54:46) [GCC 11.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

The Python function ```exit``` can be used:

```python
exit()
```

### Interactive Python

There is also Interactive Python (IPython) which can be launched using:

```
ipython
```

The output shown gives details about the Python and Interactive Python version and each Python cell has a numeric index. 

```
Python 3.11.5 (main, Sep 11 2023, 13:54:46) [GCC 11.2.0]
Type 'copyright', 'credits' or 'license' for more information
IPython 8.15.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]:
```

IPython is similar to Python but has enhancements such as the application of Python syntax highlighting and the addition of the ```?``` operator which can be used to examine a Python objects docstring. IPython also has IPython magics which begin with ```%``` and are equivalent to commonly ```bash``` commands. 

### Anaconda Navigator

In the bin folder are a number of other applications such as:

* anaconda-navigator
* conda

<img src='images_install/img_030.png' alt='img_030' width='450'/>


On Linux, no shortcuts for Anaconda or Python IDEs installed in the Anaconda base Python environment have Start Menu shortcuts. The Anaconda Navigator can be launched from the Terminal using the command:

```bash
anaconda-navigator
```

<img src='images_install/img_031.png' alt='img_031' width='450'/>

The terminal will remain busy when the Anaconda Navigator is launched:

<img src='images_install/img_032.png' alt='img_032' width='450'/>

The most commonly used Python IDEs can be launched using their respective tiles in the Anaconda Navigator:

<img src='images_install/img_033.png' alt='img_033' width='450'/>

### LibGL Error

There is a ```LibGL error: mesa iris driver error``` when Anaconda Navigator or any programs which use QT are launched. This error is due to the old version of ```libstdcxx-ng``` in the Anaconda base Python environment and can be ignored. This should eventually be fixed by Anaconda when they update this package.

### Spyder


### JupyterLab


### Python
















[Return to Anaconda Tutorial](./readme.md)