# Importing Standard Modules and Data Science Libraries

Anaconda is a Data Science Python Distribution which includes:

* Python
* Python Standard Modules
* The **Num**eric **Py**thon library - numpy
* The **P**ython **an**d **D**ata **A**naly**s**is library - pandas
* The **mat**rix **plot**ting **lib**rary - matplotlib

This tutorial will look at importing these modules and libraries and what it means physically.

## Anaconda PowerShell Prompt

Open the Anaconda PowerShell Prompt from the Start Menu:

<img src='images_imports/img_001.png' alt='img_001' width='350'/>

By default it will open in %USERPROFILE%:

<img src='images_imports/img_002.png' alt='img_002' width='350'/>

<img src='images_imports/img_003.png' alt='img_003' width='350'/>

Notice the Anaconda PowerShell Prompt begins with ```(base)```, this means the (base) Python environment is selected:

<img src='images_imports/img_004.png' alt='img_004' width='350'/>

This is the python.exe found in the Anaconda3 folder:

<img src='images_imports/img_005.png' alt='img_005' width='350'/>

<img src='images_imports/img_006.png' alt='img_006' width='350'/>

The Anaconda PowerShell Prompt uses the Programming Language PowerShell ```PS``` by default:

<img src='images_imports/img_007.png' alt='img_007' width='350'/>

The ```>``` indicates a new prompt:

<img src='images_imports/img_008.png' alt='img_008' width='350'/>

The command prompt has the following syntax:

```
command option -p parametervalue1
```

<img src='images_imports/img_009.png' alt='img_009' width='350'/>

```
command option --parametername2 parametervalue2
```

<img src='images_imports/img_010.png' alt='img_010' width='350'/>

```
command option --parametername3
```

<img src='images_imports/img_011.png' alt='img_011' width='350'/>

## Python

To launch Python from the Anaconda PowerShell Prompt input:

```
python
```

<img src='images_imports/img_012.png' alt='img_012' width='350'/>

Notice details about the Python version display alongside a new Prompt ```>>>```. 

Python uses the following functional syntax which is different to the command line syntax seen above:

```
function(value1, arg2=value2)
```

<img src='images_imports/img_013.png' alt='img_013' width='350'/>

Note that these are two different programming languages.

## Importing Libraries

Notice the base Python environment has a Lib folder:

<img src='images_imports/img_014.png' alt='img_014' width='350'/>

This contains the Python standard modules such as email:

<img src='images_imports/img_015.png' alt='img_015' width='350'/>

If the module is examined it has a \_\_init\_\_.py file which is the default Python file imported when a folder is referenced.

<img src='images_imports/img_016.png' alt='img_016' width='350'/>

The module can be imported using:

```
import email
```

And the path of the physical file can be examined using the data model attribute \_\_file\_\_:

```
email.__file__
```

<img src='images_imports/img_017.png' alt='img_017' width='350'/>

Note every \\ is replaced with \\\\, as \\ is used to insert an escape character in a Python string, in this case the escape character to be inserted is also \\.

The email standard module has submodules which can also be accessed using a ```.``` and in Python the ```.``` essentially means belonging to this object. Note that the ```.py``` file extension is not included in an import statement and therefore there is no confusion with the ```.``` used to indicate a file extension.

For example:

```
email.charset
```

would reference the charset.py in this email folder.

Some standard modules are smaller and are not contained in a folder. For example the datetime module is a single datetime.py file:

<img src='images_imports/img_018.png' alt='img_018' width='350'/>

It can be imported and details of its file can be examined using:

```
import datetime
datetime.__file__
```

<img src='images_imports/img_019.png' alt='img_019' width='350'/>

The third-party data science libraries are found in the site-packages folder:

<img src='images_imports/img_020.png' alt='img_020' width='350'/>

There is normally a folder that is the name of the library containing the Python script files alongside a folder that states the version:

<img src='images_imports/img_021.png' alt='img_021' width='350'/>

The numpy library has a \_\_init\_\_.py file which is the Python file imported when numpy is imported:

<img src='images_imports/img_022.png' alt='img_022' width='350'/>

As numpy is very commonly used it is typically imported using the 2 letter alias:

```
import numpy as np
np.__file__
```

<img src='images_imports/img_023.png' alt='img_023' width='350'/>

The pandas library has a \_\_init\_\_.py file which is the Python file imported when pandas is imported:

<img src='images_imports/img_024.png' alt='img_024' width='350'/>

<img src='images_imports/img_025.png' alt='img_025' width='350'/>

As pandas is very commonly used it is typically imported using the 2 letter alias:

```
import numpy as pd
pd.__file__
```

<img src='images_imports/img_026.png' alt='img_026' width='350'/>

The matplotlib library has a \_\_init\_\_.py file:

<img src='images_imports/img_027.png' alt='img_027' width='350'/>

<img src='images_imports/img_028.png' alt='img_028' width='350'/>

However typically only a module of this library is used called pyplot:

<img src='images_imports/img_029.png' alt='img_029' width='350'/>

As pyplot is very commonly used it is typically imported using the 4 letter alias:

```
import matplotlib.pyplot as plt
plt.__file__
```

<img src='images_imports/img_030.png' alt='img_030' width='350'/>

The locations of these modules and libraries can be seen together:

<img src='images_imports/img_031.png' alt='img_031' width='350'/>

To exit python use the function exit:

<img src='images_imports/img_032.png' alt='img_032' width='350'/>

Notice because this is a function it is followed by parenthesis.

To exit the Anaconda PowerShell Prompt use the command exit:

<img src='images_imports/img_033.png' alt='img_033' width='350'/>

Notice there is no parenthesis. 

There is a difference in syntax as Python and PowerShell are two different programming languages.

[Return to Anaconda Tutorial](./readme.md)