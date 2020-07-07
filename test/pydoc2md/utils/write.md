



Contents
========

* [line: 5 - `add_class_to_md`](#line-5---add_class_to_md)
* [line: 42 - `add_func_to_md`](#line-42---add_func_to_md)
* [line: 64 - `py_to_md`](#line-64---py_to_md)
* [line: 91 - `write_summary_file`](#line-91---write_summary_file)


&nbsp;

--------
# line: 5 - `add_class_to_md`
  
```  
def add_class_to_md(md, cl):
```
>Adds a class docstring and definition to themd file, including all class methods.

&nbsp;

--------
# line: 42 - `add_func_to_md`
  
```  
def add_func_to_md(md, cl):
```
>Adds a function docstring and definition to themd file

&nbsp;

--------
# line: 64 - `py_to_md`
  
```  
def py_to_md(data, savepath):
```
>Writes to a markdown file the content of a .py file.It writes the name of all the classes and their methods withthe corresponding docstrings as well as all functions thatare not class methods.  
:param data: dictionary of classes that belong to a .py,                from parse_pyfile  
:param savepath: str, path to the .md file to save

&nbsp;

--------
# line: 91 - `write_summary_file`
  
```  
def write_summary_file(paths, leaves, savepath):
```


>  no docstring