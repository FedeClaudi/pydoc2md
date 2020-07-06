



Contents
========

* [line: 9 - `get_pyfiles`](#line-9---get_pyfiles)
* [line: 18 - `get_subdirs`](#line-18---get_subdirs)
* [line: 29 - `parse_pyfile`](#line-29---parse_pyfile)
* [line: 80 - `add_class_to_md`](#line-80---add_class_to_md)
* [line: 117 - `add_func_to_md`](#line-117---add_func_to_md)
* [line: 139 - `write_to_md`](#line-139---write_to_md)


&nbsp;

--------
# line: 9 - `get_pyfiles`
  
```  
def get_pyfiles(folder):
```
>Gets all .py files in a folder  
:param folder: pathlib.Path object

&nbsp;

--------
# line: 18 - `get_subdirs`
  
```  
def get_subdirs(folder):
```
>Gets all subdirectories of a folder  
:param folder: pathlib.Path object

&nbsp;

--------
# line: 29 - `parse_pyfile`
  
```  
def parse_pyfile(filepath):
```
>Given a .py file, uses AST to find all classes defined in itwith their methods, docstrings etc.  
:param filepath: str, path to a .py

&nbsp;

--------
# line: 80 - `add_class_to_md`
  
```  
def add_class_to_md(md, cl):
```
>Adds a class docstring and definition to themd file, including all class methods. 

&nbsp;

--------
# line: 117 - `add_func_to_md`
  
```  
def add_func_to_md(md, cl):
```
>Adds a function docstring and definition to themd file

&nbsp;

--------
# line: 139 - `write_to_md`
  
```  
def write_to_md(data, savepath):
```
>Writes to a markdown file the content of a .py file.It writes name of all the classes and their methods withthe corresponding docstrings.  
:param data: dictionary of classes that belong to a .py,                from parse_pyfile  
:param savepath: str, path to the .md file to save