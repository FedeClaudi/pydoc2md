



Contents
========

* [line: 12 - `add_dirs_to_store`](#line-12---add_dirs_to_store)
* [line: 34 - `main`](#line-34---main)


&nbsp;

--------
# line: 12 - `add_dirs_to_store`

#### function definition


```python
def add_dirs_to_store(fld, store, savefolder):
```
##### docstring
  


```python

"""
    Iteratively parse a folder and all its subfolders,
    meanwhile file's results in `store`.
    
    :param fld: pathlib.Path object with a folder
    :param store: dictionary, updated with each file's results
    :param savefolder: str, Path. Path to the folder where the .md
            files will be saved
"""
```

&nbsp;

--------
# line: 34 - `main`

#### function definition


```python
def main(folder, savefolder, keep_structure=True, githuburl=None, checkurls=False):
```
##### docstring
  


```python

"""
    Main function used to parse a directory.
    
    corresponding .md files in savefolder
    
    :param folder: str, Path. Path to folder with the .py scripts
    :param savefolder: str, Path. Path to the folder where the .md
            files will be saved
    :param keep_structure: bool, if True the output .md are saved in
        a folder structure mirroring that of folder and its subdirs
    :param githuburl: str, optional. URL of github repo with
        the same code as `folder`, for creating links
    :param checkurls: bool. If true it checks that the URLs pointing
        to github files work. It needs internet and slows docs creation.
"""
```