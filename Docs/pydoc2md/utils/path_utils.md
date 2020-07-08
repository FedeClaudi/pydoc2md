



Contents
========

* [**Folder**](#folder)
* [line: 6 - `__init__`](#line-6---__init__)
* [line: 10 - `get_folder_structure`](#line-10---get_folder_structure)
* [line: 56 - `get_files`](#line-56---get_files)
* [line: 73 - `get_pyfiles`](#line-73---get_pyfiles)
* [line: 81 - `get_subdirs`](#line-81---get_subdirs)
* [line: 20 - `add_subdirs`](#line-20---add_subdirs)


&nbsp;

--------

--------
# **Folder**




&nbsp;

--------
# line: 6 - `__init__`
  
Check the [***``source code``***](https://github.com/FedeClaudi/pydoc2md/blob/master/pydoc2md/utils/path_utils.py#L6) online
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
# line: 10 - `get_folder_structure`
  
Check the [***``source code``***](https://github.com/FedeClaudi/pydoc2md/blob/master/pydoc2md/utils/path_utils.py#L10) online
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
# line: 56 - `get_files`
  
Check the [***``source code``***](https://github.com/FedeClaudi/pydoc2md/blob/master/pydoc2md/utils/path_utils.py#L56) online
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
# line: 73 - `get_pyfiles`
  
Check the [***``source code``***](https://github.com/FedeClaudi/pydoc2md/blob/master/pydoc2md/utils/path_utils.py#L73) online
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
# line: 81 - `get_subdirs`
  
Check the [***``source code``***](https://github.com/FedeClaudi/pydoc2md/blob/master/pydoc2md/utils/path_utils.py#L81) online
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

&nbsp;

--------
# line: 20 - `add_subdirs`
  
Check the [***``source code``***](https://github.com/FedeClaudi/pydoc2md/blob/master/pydoc2md/utils/path_utils.py#L20) online
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