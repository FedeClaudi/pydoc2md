



Contents
========

* [**Folder**](#folder)
	* [line: 5 - `__init__`](#line-5---__init__)
* [line: 8 - `get_folder_structure`](#line-8---get_folder_structure)
* [line: 17 - `add_subdirs`](#line-17---add_subdirs)
* [line: 40 - `get_files`](#line-40---get_files)
* [line: 52 - `get_pyfiles`](#line-52---get_pyfiles)
* [line: 60 - `get_subdirs`](#line-60---get_subdirs)


&nbsp;

--------

--------
# **Folder**




--------
## line: 5 - `__init__`
  
```  
def __init__(self, path):
```


>  no docstring

&nbsp;

--------
# line: 8 - `get_folder_structure`
  
```  
def get_folder_structure(folder):
```
>Iteratively go through a folderstructure finding subfolders and files. Returns a treelib.Tree object with the fileshierarchy  
:param folder: pathlib.Path object

&nbsp;

--------
# line: 17 - `add_subdirs`
  
```  
def add_subdirs(fld, tree):
```


>  no docstring

&nbsp;

--------
# line: 40 - `get_files`
  
```  
def get_files(folder, restrict_to_folder=False):
```
>Gets all files in a folder + subfolders  
:param folder: pathlib.Path object  
:param restrict_to_folder: bool. If false also    the files in the subdirectories are found

&nbsp;

--------
# line: 52 - `get_pyfiles`
  
```  
def get_pyfiles(folder):
```
>Gets all .py files in a folder + subfolers  
:param folder: pathlib.Path object

&nbsp;

--------
# line: 60 - `get_subdirs`
  
```  
def get_subdirs(folder):
```
>Gets all subdirectories of a folder  
:param folder: pathlib.Path object