# Thonny

The previous tutorial looked at ID**L**E which as the name suggests is a popular Learner IDE. Another popular learner IDE is Thonny and is the Python IDE preinstalled on a Raspberry Pi for example.

## Installing Thonny

Thonny is not installable using conda as it has no package on conda-forge and therefore needs to be installed using its own standalone installer which can be downloaded on the Thonny website [Thonny](https://thonny.org/)

<img src='images_thonny/img_001.png' alt='img_001' width='250'/>

Launch the setup:

<img src='images_thonny/img_002.png' alt='img_002' width='350'/>

Select Install for me only (recommended):

<img src='images_thonny/img_003.png' alt='img_003' width='300'/>

Select next:

<img src='images_thonny/img_004.png' alt='img_004' width='350'/>

Select the license agreement and select next:

<img src='images_thonny/img_005.png' alt='img_005' width='350'/>

Select the default install location and select next:

<img src='images_thonny/img_006.png' alt='img_006' width='350'/>

Use the default start menu folder and select next:

<img src='images_thonny/img_007.png' alt='img_007' width='350'/>

Select next:

<img src='images_thonny/img_008.png' alt='img_008' width='350'/>

Select Install: 

<img src='images_thonny/img_009.png' alt='img_009' width='350'/>

Select Finish:

<img src='images_thonny/img_010.png' alt='img_010' width='350'/>

## Creating a Python Environment

Thonny comes with its own preinstalled Python environment, this lacks the commonly used third-party data science libraries. Thonny has inbuilt utilities to download and install Python packages using pip. Because conda is more reliable Miniconda will be used to create a Python environment. To install Miniconda and set it up to use the conda-forge channel and libmamba solver see [Miniconda: Install](./Miniconda.md)

```
conda create -n thonny python cython seaborn scikit-learn sympy openpyxl xlrd xlsxwriter lxml sqlalchemy tabulate
```

<img src='images_thonny/img_011.png' alt='img_011' width='450'/>

Input ```y```:

<img src='images_thonny/img_012.png' alt='img_012' width='450'/>

The packages will be downloaded and installed:

<img src='images_thonny/img_013.png' alt='img_013' width='450'/>

Details about activating the Python environment are shown. This will need to be done in the Thonny IDE.

## Selecting Python Environment in Thonny

Launch Thonny and select your language and then Lets go:

<img src='images_thonny/img_014.png' alt='img_014' width='300'/>

Select Tools → Options:

<img src='images_thonny/img_015.png' alt='img_015' width='450'/>

In interpreter select ...: 

<img src='images_thonny/img_016.png' alt='img_016' width='450'/>

Navigate to ```%USERPROFILE%\miniconda\envs\thonny``` and select the pythone.exe and then select open. Recall ```%USERPROFILE%``` is the environmental variable that maps in my case to ```C:\Users\Philip``` and will correspond to your own user name respectively:

<img src='images_thonny/img_017.png' alt='img_017' width='450'/>

Select OK:

<img src='images_thonny/img_018.png' alt='img_018' width='450'/>

Select File → Save:

<img src='images_thonny/img_019.png' alt='img_019' width='450'/>

Save the file as a Python Script File (.py extension):

<img src='images_thonny/img_020.png' alt='img_020' width='450'/>

Some Python test code can be added to the script and it can be saved and run:

```
string = 'hello'
bytestring = b'hello'
bytearraystring = bytearray(b'hello')
wholenum = 1
floatingpointnum = 3.14
boolean = True
archive = (string, string, wholenum, floatingpointnum)
active = [string, string, wholenum, floatingpointnum]
unique = {string, string, wholenum, floatingpointnum}
mapping = {'r': 'red', 'g': 'green', 'b': 'blue'}
```

<img src='images_thonny/img_021.png' alt='img_021' width='450'/>

One of Thonnys strengths is it has has an option to view variables. Select View → Variables:

<img src='images_thonny/img_022.png' alt='img_022' width='450'/>

The Variables can be seen to the right. Code completion behaves similarly to IDLE. Inputting ```s``` and pressing ```↹``` will show namespace objects beginning with s. When one of these objects is a function the docstring will display:

<img src='images_thonny/img_023.png' alt='img_023' width='450'/>

The workflow for Thonny is usually to use the console line by line to test each line of code and then for each successful line of code add it to the Python script.

If Stop is selected, the Kernel will be cleared and all Variales will be removed:

<img src='images_thonny/img_024.png' alt='img_024' width='450'/>

Variables from the third-party data science libraries can be created:

```
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
array = np.array([1, 2, 3, 4])
df = pd.DataFrame({'x': np.array([1, 2, 3, 4, 5]),
                   'y': np.array([2, 4, 6, 8, 10])})
```

These are viewable in Vairables, although the DataFrame instance df does not display correctly in my case:

<img src='images_thonny/img_025.png' alt='img_025' width='450'/>

Code can be added to make a plot which displays in a seperate window notice once again the Shell will remain busy until the plot is closed:

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

<img src='images_thonny/img_026.png' alt='img_026' width='450'/>

[Return to Mambaforge Installation](./readme.md)