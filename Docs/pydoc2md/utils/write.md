



Contents
========

* [**`add_header`** [#6]](#add_header-6)
* [**`add_github_link`** [#15]](#add_github_link-15)
* [**`add_def_and_docstring`** [#28]](#add_def_and_docstring-28)
* [**`add_class_to_md`** [#56]](#add_class_to_md-56)
* [**`add_func_to_md`** [#84]](#add_func_to_md-84)
* [**`py_to_md`** [#99]](#py_to_md-99)
* [**`folder_md`** [#126]](#folder_md-126)
* [**`write_summary_file`** [#132]](#write_summary_file-132)


&nbsp;

--------
# **`add_header`** [#6]
  
Check the [***``source code``***](https://github.com/FedeClaudi/pydoc2md/blob/master/pydoc2md/utils/write.py#L6) online

```python
def add_header(md, nlines, level, title):
```

&nbsp;  
docstring:

no docstring

&nbsp;

--------
# **`add_github_link`** [#15]
  
Check the [***``source code``***](https://github.com/FedeClaudi/pydoc2md/blob/master/pydoc2md/utils/write.py#L15) online

```python
def add_github_link(md, githubpath, lineno):
```

&nbsp;  
docstring:

no docstring

&nbsp;

--------
# **`add_def_and_docstring`** [#28]
  
Check the [***``source code``***](https://github.com/FedeClaudi/pydoc2md/blob/master/pydoc2md/utils/write.py#L28) online

```python
def add_def_and_docstring(md, definition, doc):
```

&nbsp;  
docstring:

no docstring

&nbsp;

--------
# **`add_class_to_md`** [#56]
  
Check the [***``source code``***](https://github.com/FedeClaudi/pydoc2md/blob/master/pydoc2md/utils/write.py#L56) online

```python
def add_class_to_md(md, cl, githubpath=None):
```

&nbsp;  
docstring:

```text
Adds a class docstring and definition to the

md file, including all class methods.

```

&nbsp;

--------
# **`add_func_to_md`** [#84]
  
Check the [***``source code``***](https://github.com/FedeClaudi/pydoc2md/blob/master/pydoc2md/utils/write.py#L84) online

```python
def add_func_to_md(md, cl, githubpath=None):
```

&nbsp;  
docstring:

```text
Adds a function docstring and definition to the

md file

```

&nbsp;

--------
# **`py_to_md`** [#99]
  
Check the [***``source code``***](https://github.com/FedeClaudi/pydoc2md/blob/master/pydoc2md/utils/write.py#L99) online

```python
def py_to_md(data, savepath, githubpath=None):
```

&nbsp;  
docstring:

```text
Writes to a markdown file the content of a .py file.

It writes the name of all the classes and their methods with

the corresponding docstrings as well as all functions that

are not class methods.

:param data: dictionary of classes that belong to a .py,

from parse_pyfile

:param savepath: str, path to the .md file to save

:param githubpath: str, optional. URL to the same .py on github

```

&nbsp;

--------
# **`folder_md`** [#126]
  
Check the [***``source code``***](https://github.com/FedeClaudi/pydoc2md/blob/master/pydoc2md/utils/write.py#L126) online

```python
def folder_md(savepath):
```

&nbsp;  
docstring:

no docstring

&nbsp;

--------
# **`write_summary_file`** [#132]
  
Check the [***``source code``***](https://github.com/FedeClaudi/pydoc2md/blob/master/pydoc2md/utils/write.py#L132) online

```python
def write_summary_file(summary, savepath):
```

&nbsp;  
docstring:

no docstring