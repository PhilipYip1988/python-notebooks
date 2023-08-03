# Windows Environmental Variable Path

During installation of Mambaforge or Anaconda you will be asked whether or not you want to add the Python (base) environment to the Windows Environmental Variables path. 

The Windows Environmental Variables Path is the Python installation accessed by the Windows Terminal.

Adding to the path is not recommended as it can cause conflicts when multiple Python distributions are installed:

<img src='images_path/img_001.png' alt='img_001' width='350'/>

However some IDEs like Visual Studio Code that use the Windows Terminal will display an error message such as:

```
conda : The term 'conda' is not recognized as the name of a cmdlet, function, script 
file, or operable program. Check the spelling of the name, or if a path was included, 
verify that the path is correct and try again.
At line:1 char:1
+ conda activate vscode
+ ~~~~~
    + CategoryInfo          : ObjectNotFound: (conda:String) [], CommandNotFoundExceptio 
   n
    + FullyQualifiedErrorId : CommandNotFoundException
```

<img src='images_path/img_002.png' alt='img_002' width='450'/>

## Modifying the Windows Environmental Variable Path

Right click the start button and select System:

<img src='images_path/img_003.png' alt='img_003' width='250'/>

Select Environmental Variables:

<img src='images_path/img_004.png' alt='img_004' width='350'/>

Then Advanced System Settings:

<img src='images_path/img_005.png' alt='img_005' width='450'/>

Then select the Path and select Edit:

<img src='images_path/img_006.png' alt='img_006' width='350'/>

Add the five entries if they are not present:

```
%USERPROFILE%\Mambaforge
%USERPROFILE%\Mambaforge\Library\mingw-w64\bin
%USERPROFILE%\Mambaforge\Libraryusr\bin
%USERPROFILE%\Mambaforge\Library\bin
%USERPROFILE%\Mambaforge\Scripts
```

<img src='images_path/img_007.png' alt='img_007' width='350'/>

Select OK. Any Terminals or IDEs will need to be closed and reopened to use the updated path. Notice that there is no error in VSCode:

<img src='images_path/img_008.png' alt='img_008' width='450'/>

[Return to Mambaforge Installation](./readme.md)