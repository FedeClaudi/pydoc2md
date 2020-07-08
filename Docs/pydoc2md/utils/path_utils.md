



Contents
========

* [**Folder**](#folder)
* [line: 5 - `__init__`](#line-5---__init__)
* [line: 9 - `get_folder_structure`](#line-9---get_folder_structure)
* [line: 19 - `add_subdirs`](#line-19---add_subdirs)
* [line: 55 - `get_files`](#line-55---get_files)
* [line: 72 - `get_pyfiles`](#line-72---get_pyfiles)
* [line: 80 - `get_subdirs`](#line-80---get_subdirs)


&nbsp;

--------

--------
# **Folder**




&nbsp;

--------
# line: 5 - `__init__`
  
Check the [***``source code``***](https://github.com/FedeClaudi/pydoc2md/blob/master/pydoc2md/utils/path_utils.py#L5) online
#### function definition


```python
def __init__(self, path):
```
##### docstring
  


```python

"""
 no docstring 
"""
```

&nbsp;

--------
# line: 9 - `get_folder_structure`
  
Check the [***``source code``***](https://github.com/FedeClaudi/pydoc2md/blob/master/pydoc2md/utils/path_utils.py#L9) online
#### function definition


```python
def get_folder_structure(folder):
```
##### docstring
  


```python

"""
    Iteratively go through a folder
    structure finding subfolders and files.
    Returns a treelib.Tree object with the files
    hierarchy
    
    :param folder: pathlib.Path object
"""
```

&nbsp;

--------
# line: 19 - `add_subdirs`
  
Check the [***``source code``***](https://github.com/FedeClaudi/pydoc2md/blob/master/pydoc2md/utils/path_utils.py#L19) online
#### function definition


```python
def add_subdirs(fld, tree):
```
##### docstring
  


```python

"""
 no docstring 
"""
```

&nbsp;

--------
# line: 55 - `get_files`
  
Check the [***``source code``***](https://github.com/FedeClaudi/pydoc2md/blob/master/pydoc2md/utils/path_utils.py#L55) online
#### function definition


```python
def get_files(folder, restrict_to_folder=False):
```
##### docstring
  


```python

"""
    Gets all files in a folder + subfolders
    :param folder: pathlib.Path object
    :param restrict_to_folder: bool. If false also
        the files in the subdirectories are found
"""
```

&nbsp;

--------
# line: 72 - `get_pyfiles`
  
Check the [***``source code``***](https://github.com/FedeClaudi/pydoc2md/blob/master/pydoc2md/utils/path_utils.py#L72) online
#### function definition


```python
def get_pyfiles(folder):
```
##### docstring
  


```python

"""
    Gets all .py files in a folder + subfolers
    :param folder: pathlib.Path object
"""
```

&nbsp;

--------
# line: 80 - `get_subdirs`
  
Check the [***``source code``***](https://github.com/FedeClaudi/pydoc2md/blob/master/pydoc2md/utils/path_utils.py#L80) online
#### function definition


```python
def get_subdirs(folder):
```
##### docstring
  


```python

"""
    Gets all subdirectories of a folder
    :param folder: pathlib.Path object
"""
```