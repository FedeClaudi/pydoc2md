from mdutils.mdutils import MdUtils
from pathlib import Path


def add_class_to_md(md, cl):
    """
        Adds a class docstring and definition to the
        md file, including all class methods.
    """
    # header
    md.new_paragraph("&nbsp;")
    md.new_paragraph("--------")
    md.new_paragraph("--------")
    md.new_header(level=1, title=f'**{cl["name"]}**')

    if cl["doc"] is not None:
        md.new_line("```")
        md.new_line(cl["doc"])
        md.new_line("```")
    else:
        md.new_paragraph("")

    for func, doc, lineno, df in zip(
        cl["funcs"], cl["funcs_docs"], cl["funcs_lines"], cl["def"]
    ):
        md.new_paragraph("--------")
        md.new_header(level=2, title=f"line: {lineno} - `{func}`")

        md.new_line("```")
        md.new_line(df + "\n```\n")

        if doc is not None:
            for n, par in enumerate(doc.split("\n")):
                if ":param" not in par:
                    md.write(f'{">" if n ==0 else ""}{par}')
                else:
                    md.new_line(par)
        else:
            md.new_paragraph(f">  no docstring")


def add_func_to_md(md, cl):
    """
        Adds a function docstring and definition to the
        md file
    """
    md.new_paragraph("&nbsp;")
    md.new_paragraph("--------")
    md.new_header(level=1, title=f"line: {cl['line']} - `{cl['name']}`")

    md.new_line("```")
    md.new_line(cl["def"] + "\n```\n")

    if cl["doc"] is not None:
        for n, par in enumerate(cl["doc"].split("\n")):
            if ":param" not in par:
                md.write(f'{">" if n ==0 else ""}{par}')
            else:
                md.new_line(par)
    else:
        md.new_paragraph(f">  no docstring")


def py_to_md(data, savepath):
    """
        Writes to a markdown file the content of a .py file.
        It writes the name of all the classes and their methods with
        the corresponding docstrings as well as all functions that
        are not class methods.

        :param data: dictionary of classes that belong to a .py,
                        from parse_pyfile
        :param savepath: str, path to the .md file to save
    """
    print(f"writing - {savepath}")
    md = MdUtils(file_name=savepath)

    # Iterate classes
    for cl in data.values():

        # class/function specific
        if cl["isclass"]:
            add_class_to_md(md, cl)
        else:
            add_func_to_md(md, cl)

    md.new_table_of_contents(table_title="Contents", depth=2)
    md.create_md_file()


def write_summary_file(pathtree, savepath):
    print(f"writing - {savepath}")
    md = MdUtils(file_name=str(savepath))

    # Save path trees to a temp file
    temp = str(savepath.parent / "temp.txt")
    pathtree.save2file(temp)

    with open(temp, "r") as tmp:
        tree = tmp.read()

    Path(temp).unlink()

    # Add the path tree as tree view
    md.new_paragraph("```\n" + tree + "\n```")

    md.create_md_file()
