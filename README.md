# pydoc2md
Inspired by https://github.com/gbowerman/py2md

----
`pydoc2md` is lightweight python application that generates markdown (`.md`) files from a repository of `.py`. The idea is to easily generate bare bones documentation for a python project by providing a list of all classes and functions, each with their docstring. 

----
`pydoc2md` creates a `.md` file for every `.py` file in your project. The `.md` file lists all the classes and functions defined in the `.py` displaying docstrings and other useful information. Check the markdown files in `Docs` or in the [`brainrender` docs](https://docs.brainrender.info/autogenerated-docs/overview) to get an idea of what the output looks like.

## Features
- [x] a single command to create all your docs
- [x] folder structure: the output `.md` are organised in a folder structure mirroring that of your package
- [x] summary: `summary.md` includes a table of content pointing towards each individual `.md` thus refelicting the structure of your package
- [x] **github links**: if you provide a link to the github repository with your code, for each function in your `.md` files `pydoc2md` will link generate links to the corresponding line in the `.py` files on github. 



## Usage
**using pydoc2md** is very simple. From the command line:
```
    pydoc2md project/path output/path
```

For instance, the `.md` files in [Docs](Docs) where generated with
```
    pydoc2md Github/pydoc2md/pydoc2md Github/pydoc2md/Docs
```

## Installation
You can install  with:

```
pip install pydoc2md
```

