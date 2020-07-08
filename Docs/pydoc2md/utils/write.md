



Contents
========

* [line: 4 - `add_header`](#line-4---add_header)
* [line: 12 - `add_github_link`](#line-12---add_github_link)
* [line: 23 - `add_docstring`](#line-23---add_docstring)
* [line: 36 - `add_class_to_md`](#line-36---add_class_to_md)
* [line: 69 - `add_func_to_md`](#line-69---add_func_to_md)
* [line: 89 - `py_to_md`](#line-89---py_to_md)
* [line: 118 - `folder_md`](#line-118---folder_md)
* [line: 124 - `write_summary_file`](#line-124---write_summary_file)


&nbsp;

--------
# line: 4 - `add_header`
  
Check the [***``source code``***](https://github.com/FedeClaudi/pydoc2md/blob/master/pydoc2md/utils/write.py#L4) online
#### function definition


```python
def add_header(md, nlines, level, title):
```
##### docstring
  


```python

"""
 no docstring 
"""
```

&nbsp;

--------
# line: 12 - `add_github_link`
  
Check the [***``source code``***](https://github.com/FedeClaudi/pydoc2md/blob/master/pydoc2md/utils/write.py#L12) online
#### function definition


```python
def add_github_link(md, githubpath, lineno):
```
##### docstring
  


```python

"""
 no docstring 
"""
```

&nbsp;

--------
# line: 23 - `add_docstring`
  
Check the [***``source code``***](https://github.com/FedeClaudi/pydoc2md/blob/master/pydoc2md/utils/write.py#L23) online
#### function definition


```python
def add_docstring(md, doc):
```
##### docstring
  


```python

"""
 no docstring 
"""
```

&nbsp;

--------
# line: 36 - `add_class_to_md`
  
Check the [***``source code``***](https://github.com/FedeClaudi/pydoc2md/blob/master/pydoc2md/utils/write.py#L36) online
#### function definition


```python
def add_class_to_md(md, cl, githubpath=None):
```
##### docstring
  


```python

"""
    Adds a class docstring and definition to the
    md file, including all class methods.
"""
```

&nbsp;

--------
# line: 69 - `add_func_to_md`
  
Check the [***``source code``***](https://github.com/FedeClaudi/pydoc2md/blob/master/pydoc2md/utils/write.py#L69) online
#### function definition


```python
def add_func_to_md(md, cl, githubpath=None):
```
##### docstring
  


```python

"""
    Adds a function docstring and definition to the
    md file
"""
```

&nbsp;

--------
# line: 89 - `py_to_md`
  
Check the [***``source code``***](https://github.com/FedeClaudi/pydoc2md/blob/master/pydoc2md/utils/write.py#L89) online
#### function definition


```python
def py_to_md(data, savepath, githubpath=None):
```
##### docstring
  


```python

"""
    Writes to a markdown file the content of a .py file.
    It writes the name of all the classes and their methods with
    the corresponding docstrings as well as all functions that
    are not class methods.
    
    :param data: dictionary of classes that belong to a .py,
                    from parse_pyfile
    :param savepath: str, path to the .md file to save
    :param githubpath: str, optional. URL to the same .py on github
"""
```

&nbsp;

--------
# line: 118 - `folder_md`
  
Check the [***``source code``***](https://github.com/FedeClaudi/pydoc2md/blob/master/pydoc2md/utils/write.py#L118) online
#### function definition


```python
def folder_md(savepath):
```
##### docstring
  


```python

"""
 no docstring 
"""
```

&nbsp;

--------
# line: 124 - `write_summary_file`
  
Check the [***``source code``***](https://github.com/FedeClaudi/pydoc2md/blob/master/pydoc2md/utils/write.py#L124) online
#### function definition


```python
def write_summary_file(paths, leaves, savepath):
```
##### docstring
  


```python

"""
 no docstring 
"""
```