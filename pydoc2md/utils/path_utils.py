def get_folder_structure(folder):
    """
        Gets the structure of subdirectories of
        a given folder.
        :param folder: pathlib.Path object

    """

    a = 1
    print(a)


def get_pyfiles(folder):
    """
        Gets all .py files in a folder
        :param folder: pathlib.Path object
    """
    files = [x for x in folder.glob("**/*") if x.is_file()]
    return [f for f in files if str(f).endswith(".py")]


def get_subdirs(folder):
    """
        Gets all subdirectories of a folder
        :param folder: pathlib.Path object
    """
    return [f for f in folder.iterdir() if f.is_dir()]
