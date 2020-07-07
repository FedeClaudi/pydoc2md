



Contents
========

* [line: 7 - `parse_dir`](#line-7---parse_dir)
* [line: 27 - `main`](#line-27---main)


&nbsp;

--------
# line: 7 - `parse_dir`
  
```  
def parse_dir(fld, store):
```
>Iteratively parse a folder and all its subfolders,meanwhile storing each file's results in `store`.  
:param fld: pathlib.Path object with a folder  
:param store: dictionary, updated with each file's results

&nbsp;

--------
# line: 27 - `main`
  
```  
def main(folder, savefolder, keep_structure=True):
```
>Main function used to parse a directory.corresponding .md files in savefolder  
:param folder: str, Path. Path to folder with the .py scripts  
:param savefolder: str, Path. Path to the folder where the .md        files will be saved  
:param keep_structure: bool, if True the output .md are saved in     a folder structure mirroring that of folder and its subdirs