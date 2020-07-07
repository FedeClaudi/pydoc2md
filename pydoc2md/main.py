from pathlib import Path
from pydoc2md.utils.path_utils import (
    get_subdirs,
    get_pyfiles,
    get_folder_structure,
)
from pydoc2md.utils.parse import parse_pyfile
from pydoc2md.utils.write import py_to_md, write_summary_file


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


def main(folder, savefolder, keep_structure=True):
    """
        Main function used to parse a directory.

        corresponding .md files in savefolder

        :param folder: str, Path. Path to folder with the .py scripts
        :param savefolder: str, Path. Path to the folder where the .md
                files will be saved
        :param keep_structure: bool, if True the output .md are saved in
            a folder structure mirroring that of folder and its subdirs
    """
    folder = Path(folder)
    savefolder = Path(savefolder)

    # Check that folder exists
    if not folder.exists():
        raise ValueError(f"Folder {str(folder)} does not exist.")

    # Get folder structure
    pathtree = get_folder_structure(folder)
    leaves = pathtree.paths_to_leaves()

    # Parse files
    store = {}
    parse_dir(folder, store)

    # Create save folder
    savefolder.mkdir(exist_ok=True)

    # Create summary file
    write_summary_file(pathtree, savefolder / "summary.md")

    # save markdowns for single files
    for fp, data in store.items():
        # Get savepath
        if not keep_structure:
            # Save all .md in the same folder
            savepath = savefolder / fp.name
        else:
            # Mirror folder structure
            parent, fl = fp.parent.name, fp.name
            path = [leaf for leaf in leaves if leaf[-1] == parent + fl]

            if not path or len(path) > 1:
                raise ValueError(
                    "Something went wrong while re-creating folder structure"
                )
            else:
                savepath = savefolder / Path(*path[0][:-1])
                savepath.mkdir(exist_ok=True)

                savepath = savepath / fl
        savepath = str(savepath).replace(".py", ".md")

        # Save to .md
        if data:
            py_to_md(data, savepath)
