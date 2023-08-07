# IDLE

IDLE is an abbreviation for the Integrated Development Learner Environment. 

IDLE is a preinstalled Python IDE that is written using the Python standard library tkinter. tkinter is a Python standard library which is used for graphical user interfaces.

## IDLE Shell

The IDLE Shell can be launched from the Miniconda PowerShell Prompt using the PowerShell command:

```
idle
```

<img src='images_idle/img_001.png' alt='img_001' width='450'/>

Notice that when idle is launched, the Miniconda Prompt is busy. It will remain busy until IDLE is closed:

<img src='images_idle/img_002.png' alt='img_002' width='450'/>

The IDLE Shell looks similar to a PowerShell Prompt running Python and can be used to input Python code:

<img src='images_idle/img_003.png' alt='img_003' width='450'/>


## Code Completion and Docstrings

If ```p``` is input followed by a ```↹```, a list of Python builtins identifiers displays:

<img src='images_idle/img_004.png' alt='img_004' width='450'/>

And if a function is input with open parenthesis for example ```print(``` a docstring will display:

<img src='images_idle/img_005.png' alt='img_005' width='450'/>

If a Python standard module is imported such as:

```
import builtins
```

And if ```builtins.``` is input followed by a ```↹```, a list of Python identifiers from that module displays:

<img src='images_idle/img_006.png' alt='img_006' width='450'/>

If the following two instances are created:

```
obj1 = object()
str1 = 'hello'
```

<img src='images_idle/img_007.png' alt='img_007' width='450'/>


Inputting ```obj1.``` followed by a ```↹```, shows a list of Python object based data model identifiers:

<img src='images_idle/img_008.png' alt='img_008' width='450'/>

Inputting ```str1.``` followed by a ```↹```, shows a list of Python str identifiers:

<img src='images_idle/img_009.png' alt='img_009' width='450'/>

Inputting ```str1._``` followed by a ```↹```, shows a list of Python object based data model identifiers that the str class also has:

<img src='images_idle/img_010.png' alt='img_010' width='450'/>


## IDLE Doc

The IDLE Doc is essentially an equivalent to Notepad that shows code completion.

To open IDLE Doc, select File → New File in the IDLE Shell:

<img src='images_idle/img_011.png' alt='img_011' width='450'/>

This will open up IDLE Doc in a seperate Window. Select File → Save As...

<img src='images_idle/img_012.png' alt='img_012' width='450'/>

Then save the file as a Python Script file (.py file extension):

<img src='images_idle/img_013.png' alt='img_013' width='450'/>

Code completion will now work in a similar manner to seen in the IDLE Shell:

<img src='images_idle/img_014.png' alt='img_014' width='450'/>

<img src='images_idle/img_015.png' alt='img_015' width='450'/>

<img src='images_idle/img_016.png' alt='img_016' width='450'/>

<img src='images_idle/img_017.png' alt='img_017' width='450'/>

To Run a Python Script file select Run → Run Module:

<img src='images_idle/img_018.png' alt='img_018' width='450'/>

This will run the Python Script File in the IDLE Shell:

<img src='images_idle/img_019.png' alt='img_019' width='450'/>

## Third Party Libraries

If third-party data science libraries are to be used IDLE needs to be installed in its own Python environment.

Miniconda will be used to create a Python environment. To install Miniconda and set it up to use the conda-forge channel and libmamba solver see [Miniconda: Install](./Miniconda.md)

The following Python Environment can be created for the IDLE IDE:

```
conda create -n idle python cython seaborn scikit-learn sympy openpyxl xlrd xlsxwriter lxml sqlalchemy tabulate
```

This is covered in more detail in [Miniconda: Python Environments Overview](./environments.md)

<img src='images_idle/img_020.png' alt='img_020' width='450'/>

The conda package manager will search for all of these packages and their dependencies. Input ```y``` in order to proceed:

<img src='images_idle/img_021.png' alt='img_021' width='450'/>

The packages will be downloaded and installed:

<img src='images_idle/img_022.png' alt='img_022' width='450'/>

To activate the idle Python environment use:

```
conda activate idle
```

Then to launch idle use:

```
idle
```

<img src='images_idle/img_023.png' alt='img_023' width='450'/>

Code completion with the IDLE Doc is not as good for third-party libraries. If a script file includes

```
import numpy as np
```

And ```np.``` is input followed by a ```↹``` no completions display:

<img src='images_idle/img_024.png' alt='img_024' width='450'/>

This only works if numpy is imported in the IDLE Console:

```
import numpy as np
```

<img src='images_idle/img_025.png' alt='img_025' width='450'/>

The data science libraries can be tested using:

```
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
array = np.array([1, 2, 3, 4])
df = pd.DataFrame({'x': np.array([1, 2, 3, 4, 5]),
                   'y': np.array([2, 4, 6, 8, 10])})
plt.plot(df['x'], df['y'])
plt.show()
```

IDLE uses the TkAgg backend for Matplotlib and the plot displays in a seperate window. The console will remain busy until the plot is closed:

<img src='images_idle/img_026.png' alt='img_026' width='450'/>

[Return to Miniconda Installation](./readme.md)