



Contents
========

* [line: 5 - `parse_dir`](#line-5---parse_dir)
* [line: 25 - `main`](#line-25---main)


&nbsp;

--------
# line: 5 - `parse_dir`
  
```  
def parse_dir(fld, store):
```
>Iteratively parse a folder and all its subfolders,meanwhile storing each file's results in `store`.  
:param fld: pathlib.Path object with a folder  
:param store: dictionary, updated with each file's results

&nbsp;

--------
# line: 25 - `main`
  
```  
def main(folder, savefolder):
```
>Main function used to parse a directory.corresponding .md files in savefolder  
:param folder: str, Path. Path to folder with the .py scripts  
:param savefolder: str, Path. Path to the folder where the .md        files will be saved