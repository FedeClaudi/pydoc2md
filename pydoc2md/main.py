from pathlib import Path
from collections import OrderedDict
from pydoc2md.utils.path_utils import (
    get_subdirs,
    get_folder_structure,
)
from pydoc2md.utils.parse import parse_pyfile
from pydoc2md.utils.write import py_to_md, write_summary_file, folder_md


def add_dirs_to_store(fld, store):
    """
        Iteratively parse a folder and all its subfolders,
        meanwhile file's results in `store`.

        :param fld: pathlib.Path object with a folder
        :param store: dictionary, updated with each file's results
    """
    # Create an entry for folder .md overview file
    store[fld / (fld.name + ".md")] = OrderedDict(
        sorted({"isclass": None}.items())
    )

    # Iterate over subdirs
    subdirs = get_subdirs(fld)
    for sd in subdirs:
        add_dirs_to_store(sd, store)


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
    for leaf in leaves:
        end = leaf.pop(-1)
        leaf.append(end.split("+")[-1])

        path = Path(*leaf)
        store[path] = parse_pyfile(folder.parent / path)

    add_dirs_to_store(folder, store)

    # Create save folder
    savefolder.mkdir(exist_ok=True)

    # save markdowns for single files
    paths = {}
    for fp, data in store.items():
        # Get savepath
        if not keep_structure:
            # Save all .md in the same folder
            savepath = savefolder / fp.name
        else:
            # Mirror folder structure
            parent, fl = fp.parent.name, fp.name
            path = [
                leaf
                for leaf in leaves
                if leaf[-1] == fl and leaf[-2] == parent
            ]

            if not path or path[0][-1].endswith(".md"):
                if fp.parent.name.startswith(
                    "__"
                ) or fp.parent.name.startswith("."):
                    continue

                savepath = fp
                path = None
            elif len(path) > 1:
                raise ValueError(
                    "Something went wrong while re-creating folder structure"
                )
            else:
                savepath = savefolder / Path(*path[0][:-1])
                savepath.mkdir(exist_ok=True)

                savepath = savepath / fl

        savepath = str(savepath).replace(".py", ".md")

        if path is not None:
            paths["".join(*path)] = (path[0], Path(savepath))
        else:
            paths[fp.parent.name] = (None, Path(savepath))

        # Save to .md
        if data:
            if "isclass" not in data.keys():
                py_to_md(data, savepath)
            else:
                folder_md(savepath)

    # Create summary file
    write_summary_file(paths, leaves, savefolder / "summary.md")
