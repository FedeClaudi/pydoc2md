from treelib import Tree


class Folder:
    def __init__(self, path):
        self.path = path


def get_folder_structure(folder):
    """
        Iteratively go through a folder
        structure finding subfolders and files.
        Returns a treelib.Tree object with the files
        hierarchy

        :param folder: pathlib.Path object
    """

    def add_subdirs(fld, tree):
        files = get_files(fld, restrict_to_folder=True)
        for fl in files:
            if fl.name.startswith("."):
                continue
            tree.create_node(
                tag=fl.name,
                identifier=fld.name + fl.name,
                parent=fld.name,
                data=Folder(fl),
            )

        for sub in get_subdirs(fld):
            if sub.name.startswith("__"):
                continue
            tree.create_node(
                tag=sub.name,
                identifier=sub.name,
                parent=sub.parent.name,
                data=Folder(sub),
            )
            add_subdirs(sub, tree)

    tree = Tree()
    tree.create_node(
        tag=folder.name, identifier=folder.name, data=Folder(folder)
    )
    add_subdirs(folder, tree)

    return tree


def get_files(folder, restrict_to_folder=False):
    """
        Gets all files in a folder + subfolders
        :param folder: pathlib.Path object
        :param restrict_to_folder: bool. If false also
            the files in the subdirectories are found
    """
    if not restrict_to_folder:
        return [x for x in folder.glob("**/*") if x.is_file()]
    else:
        return [
            x
            for x in folder.glob("**/*")
            if x.is_file() and x.parent.name == folder.name
        ]


def get_pyfiles(folder):
    """
        Gets all .py files in a folder + subfolers
        :param folder: pathlib.Path object
    """
    return [f for f in get_files(folder) if str(f).endswith(".py")]


def get_subdirs(folder):
    """
        Gets all subdirectories of a folder
        :param folder: pathlib.Path object
    """
    return [f for f in folder.iterdir() if f.is_dir()]
