



Contents
========

* [**Folder**](#folder)
	* [**`__init__`** [#6]](#__init__-6)
* [**`get_folder_structure`** [#10]](#get_folder_structure-10)
* [**`get_files`** [#56]](#get_files-56)
* [**`get_pyfiles`** [#73]](#get_pyfiles-73)
* [**`get_subdirs`** [#81]](#get_subdirs-81)
* [**`add_subdirs`** [#20]](#add_subdirs-20)


&nbsp;

--------
# **Folder**




&nbsp;
## **`__init__`** [#6]
  
Check the [***``source code``***](https://github.com/FedeClaudi/pydoc2md/blob/master/pydoc2md/utils/path_utils.py#L6) online

```python
def __init__(self, path):
```

&nbsp;  
docstring:

no docstring

&nbsp;

--------
# **`get_folder_structure`** [#10]
  
Check the [***``source code``***](https://github.com/FedeClaudi/pydoc2md/blob/master/pydoc2md/utils/path_utils.py#L10) online

```python
def get_folder_structure(folder):
```

&nbsp;  
docstring:

```text
Iteratively go through a folder

structure finding subfolders and files.

Returns a treelib.Tree object with the files

hierarchy

:param folder: pathlib.Path object

```

&nbsp;

--------
# **`get_files`** [#56]
  
Check the [***``source code``***](https://github.com/FedeClaudi/pydoc2md/blob/master/pydoc2md/utils/path_utils.py#L56) online

```python
def get_files(folder, restrict_to_folder=False):
```

&nbsp;  
docstring:

```text
Gets all files in a folder + subfolders

:param folder: pathlib.Path object

:param restrict_to_folder: bool. If false also

the files in the subdirectories are found

```

&nbsp;

--------
# **`get_pyfiles`** [#73]
  
Check the [***``source code``***](https://github.com/FedeClaudi/pydoc2md/blob/master/pydoc2md/utils/path_utils.py#L73) online

```python
def get_pyfiles(folder):
```

&nbsp;  
docstring:

```text
Gets all .py files in a folder + subfolers

:param folder: pathlib.Path object

```

&nbsp;

--------
# **`get_subdirs`** [#81]
  
Check the [***``source code``***](https://github.com/FedeClaudi/pydoc2md/blob/master/pydoc2md/utils/path_utils.py#L81) online

```python
def get_subdirs(folder):
```

&nbsp;  
docstring:

```text
Gets all subdirectories of a folder

:param folder: pathlib.Path object

```

&nbsp;

--------
# **`add_subdirs`** [#20]
  
Check the [***``source code``***](https://github.com/FedeClaudi/pydoc2md/blob/master/pydoc2md/utils/path_utils.py#L20) online

```python
def add_subdirs(fld, tree):
```

&nbsp;  
docstring:

no docstring