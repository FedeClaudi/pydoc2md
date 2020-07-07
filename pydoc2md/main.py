from pathlib import Path
from pydoc2md.utils.path_utils import get_subdirs, get_pyfiles
from pydoc2md.utils.parse import parse_pyfile
from pydoc2md.utils.write import py_to_md


def parse_dir(fld, store):
    """
        Iteratively parse a folder and all its subfolders,
        meanwhile storing each file's results in `store`.

        :param fld: pathlib.Path object with a folder
        :param store: dictionary, updated with each file's results
    """
    # Get python files and subdirs
    pyfiles = get_pyfiles(fld)
    subdirs = get_subdirs(fld)

    # Get funcs
    for fl in pyfiles:
        store[fl] = parse_pyfile(fl)

    for sd in subdirs:
        parse_dir(sd, store)


def main(folder, savefolder):
    """
        Main function used to parse a directory.

        corresponding .md files in savefolder

        :param folder: str, Path. Path to folder with the .py scripts
        :param savefolder: str, Path. Path to the folder where the .md
                files will be saved
    """
    folder = Path(folder)
    savefolder = Path(savefolder)

    # Check that folder exists
    if not folder.exists():
        raise ValueError(f"Folder {str(folder)} does not exist.")

    # Parse files
    store = {}
    parse_dir(folder, store)

    # Create save folder
    savefolder.mkdir(exist_ok=True)

    # save markdowns
    for fp, data in store.items():
        savepath = savefolder / fp.name
        savepath = str(savepath).replace(".py", ".md")

        if data:
            py_to_md(data, savepath)
