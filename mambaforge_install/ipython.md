# Interactive Python

IPython is an abbreviation for **i**nteractive **Python** and is an improved version of the Python shell. It is not included in the Mambaforge (base) environment and can be added using:

```
mamba install ipython
```

A better practice is to leave the (base) Python environment unmodified and therefore create a new Python environment using:

```
mamba create -n ipython python=3.11 ipython
```

This Python environment can be activated using:

```
mamba activate ipython
```

To launch ipython from the Python environment ipython use:

```
ipython
```


p

p tab

? print






The command change directory cd can be used to view the current directory:

```
cd
```

By default the current directory (also known as a folder in Windows) will be the Windows environmental variable ```%USERPROFILE%``` which in my case is ```C:\Users\Philip``` and in your case will correspond to your equivalent user name. The Documents folder is a subfolder of this location and can be selected using:

```
cd Documents
```

This returns the current directory ```C:\Users\Philip\Documents```. ```~``` is used to return %USERPROFILE$

```
cd ~
```

In my case this gives ```C:\Users\Philip```. ```~\Documents``` can be used to get to the Documents from ```~```: 

```
~\Documents
```

In my case this returns ```C:\Users\Philip\Documents```. The command list ls lists all files and folders in a directory:

```
ls
```

A new folder can be created using the command mkdir:

```
mkdir newfolder
```

A file name can't contain any of the following characters ```\ / : * ? " < > |``` as they are reserved.

It is not normally good practice to include spaces in the folder names. If spaces are included they should be wrapped around in the reserved double quotations:

```
mkdir "new folder"
```

Note the single quotations are not reserved and can be included in the folder name;

```
mkdir 'new folder'
```

This results in two new folders ```'new``` and ```folder'```.

These can be removed using the remove dir command rmdir:

```
rmdir 'new
rmdir folder'
rmdir "new folder"
```

The newfolder can be selected using:

```
cd ~\Documents\NewFolder
```

A Python


The . is used to explicity

The ..


cd

cd

cd ~

cd ~/Documents

edit test.py
run test.py

