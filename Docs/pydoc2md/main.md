



Contents
========

* [line: 8 - `get_github_url`](#line-8---get_github_url)
* [line: 27 - `main`](#line-27---main)


&nbsp;

--------
# line: 8 - `get_github_url`
  
Check the [***``source code``***](https://github.com/FedeClaudi/pydoc2md/blob/master/pydoc2md/pydoc2md/main.py#L8) online
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
# line: 27 - `main`
  
Check the [***``source code``***](https://github.com/FedeClaudi/pydoc2md/blob/master/pydoc2md/pydoc2md/main.py#L27) online
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