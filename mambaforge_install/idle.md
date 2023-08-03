# IDLE

IDLE is an abbreviation for the Integrated Development Learner Environment. 

IDLE is a preinstalled Python IDE that is written using the Python standard library tkinter. tkinter is a Python standard library which is used for graphical user interfaces.

## IDLE Shell

The IDLE Shell can be launched from the Mambaforge Prompt using the CMD command:

```
idle
```

Notice that when idle is launched, the Mambaforge Prompt is busy. It will remain busy until IDLE is closed:



The IDLE Shell looks similar to a terminal and can be used to input Python code:



## Code Completion and Docstrings

If ```p``` is input followed by a ```↹```, a list of Python builtins identifiers displays:



And if a function is input with open parenthesis for example ```print(``` a docstring will display:




If a Python standard module is imported such as:

```
builtins
```

And if ```builtins.``` is input followed by a ```↹```, a list of Python identifiers from that module displays:



If the following two instances are created:

```
obj1 = object()
str1 = 'hello'
```



Inputting ```obj1.``` followed by a ```↹```, shows a list of Python object based data model identifiers:



Inputting ```str1.``` followed by a ```↹```, shows a list of Python str identifiers:



Inputting ```str1._``` followed by a ```↹```, shows a list of Python object based data model identifiers that the str class also has:



## IDLE Doc

The IDLE Doc is essentially an equivalent to Notepad that shows code completion.