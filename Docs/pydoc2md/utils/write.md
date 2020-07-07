



Contents
========

* [line: 4 - `add_class_to_md`](#line-4---add_class_to_md)
* [line: 49 - `add_func_to_md`](#line-49---add_func_to_md)
* [line: 82 - `py_to_md`](#line-82---py_to_md)
* [line: 111 - `folder_md`](#line-111---folder_md)
* [line: 117 - `write_summary_file`](#line-117---write_summary_file)


&nbsp;

--------
# line: 4 - `add_class_to_md`

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
# line: 49 - `add_func_to_md`

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
# line: 82 - `py_to_md`

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
# line: 111 - `folder_md`

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
# line: 117 - `write_summary_file`

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