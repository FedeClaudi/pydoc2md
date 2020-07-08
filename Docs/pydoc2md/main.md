



Contents
========

* [**`get_github_url`** [#8]](#get_github_url-8)
* [**`main`** [#27]](#main-27)


&nbsp;

--------
# **`get_github_url`** [#8]
  
Check the [***``source code``***](https://github.com/FedeClaudi/pydoc2md/blob/master/pydoc2md/main.py#L8) online

```python
def get_github_url(path, githuburl, checkurls):
```

&nbsp;  
docstring:

no docstring

&nbsp;

--------
# **`main`** [#27]
  
Check the [***``source code``***](https://github.com/FedeClaudi/pydoc2md/blob/master/pydoc2md/main.py#L27) online

```python
def main(folder, savefolder, githuburl=None, checkurls=False):
```

&nbsp;  
docstring:

```text
Main function used to parse a directory.

corresponding .md files in savefolder

:param folder: str, Path. Path to folder with the .py scripts

:param savefolder: str, Path. Path to the folder where the .md

files will be saved

:param githuburl: str, optional. URL of github repo with

the same code as `folder`, for creating links

:param checkurls: bool. If true it checks that the URLs pointing

to github files work. It needs internet and slows docs creation.

```