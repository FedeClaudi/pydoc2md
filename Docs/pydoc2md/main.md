



Contents
========

* [line: 11 - `get_github_url`](#line-11---get_github_url)
* [line: 34 - `main`](#line-34---main)


&nbsp;

--------
# line: 11 - `get_github_url`
  
Check the [***``source code``***](https://github.com/FedeClaudi/pydoc2md/blob/master/pydoc2md/pydoc2md/main.py#L11) online
#### function definition


```python
def get_github_url(path, githuburl, checkurls):
```
##### docstring
  


```python

"""
 no docstring 
"""
```

&nbsp;

--------
# line: 34 - `main`
  
Check the [***``source code``***](https://github.com/FedeClaudi/pydoc2md/blob/master/pydoc2md/pydoc2md/main.py#L34) online
#### function definition


```python
def main(folder, savefolder, githuburl=None, checkurls=False):
```
##### docstring
  


```python

"""
    Main function used to parse a directory.
    
    corresponding .md files in savefolder
    
    :param folder: str, Path. Path to folder with the .py scripts
    :param savefolder: str, Path. Path to the folder where the .md
            files will be saved
    :param githuburl: str, optional. URL of github repo with
        the same code as `folder`, for creating links
    :param checkurls: bool. If true it checks that the URLs pointing
        to github files work. It needs internet and slows docs creation.
"""
```