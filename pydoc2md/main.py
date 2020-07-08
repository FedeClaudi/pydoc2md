from pathlib import Path
from pydoc2md.utils.path_utils import get_folder_structure
from pydoc2md.utils.parse import parse_pyfile
from pydoc2md.utils.write import py_to_md, write_summary_file, folder_md
from pydoc2md.utils.web import check_url


def get_github_url(path, githuburl, checkurls):
    # Get github path
    if githuburl is not None:
        fileurl = githuburl + "/blob/master/" + path.replace("\\", "/")

        if checkurls:
            if not check_url(fileurl):
                raise ValueError(
                    f"Something went wrong while getting \
                            the url for {path}."
                    + f"Got {fileurl} but it doesnt seem to \
                            exist or your internet \
                                    connection is down."
                )
        return fileurl
    else:
        return None


def main(folder, savefolder, githuburl=None, checkurls=False):
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
    folder = Path(folder)
    savefolder = Path(savefolder)
    savefolder.mkdir(exist_ok=True)

    # Check that folder exists
    if not folder.exists():
        raise ValueError(f"Folder {str(folder)} does not exist.")

    # Get folder structure
    pathtree = get_folder_structure(folder)

    # Iterate over items in pathtree
    summary = {}
    for nid, node in pathtree.nodes.items():
        depth = pathtree.depth(nid)

        if nid.endswith(".py"):
            # parse python file and add the .md
            fld, name = nid.split("+")
            parsed = parse_pyfile(node.data.path)

            if parsed:
                if depth < 2:
                    sfld = savefolder / fld
                else:
                    sfld = savefolder / folder.name / fld
                sfld.mkdir(exist_ok=True)

                savepath = str(sfld / name.replace(".py", ".md"))

                fileurl = get_github_url(
                    str(Path(*[folder.name, fld, name])), githuburl, checkurls
                )
                py_to_md(parsed, savepath, githubpath=fileurl)

                summary[nid] = (depth, Path(savepath))

        else:
            # Create a folder .md file
            if nid != folder.name:
                savepath = str(savefolder / folder.name / nid / (nid + ".md"))
                Path(savepath).parent.mkdir(exist_ok=True)
            else:
                savepath = str(savefolder / (nid + ".md"))

            folder_md(savepath)
            summary[nid] = (depth, Path(savepath))

    # Create summary file
    write_summary_file(summary, str(savefolder / "summary.md"))
