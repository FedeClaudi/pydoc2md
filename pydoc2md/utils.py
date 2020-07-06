from mdutils.mdutils import MdUtils
import ast
from astunparse import unparse
import collections

# ----------------------------------- paths ----------------------------------#


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


# ----------------------------------- parse ----------------------------------#


def parse_pyfile(filepath):
    """
        Given a .py file, uses AST to find all classes defined in it
        with their methods, docstrings etc.
        :param filepath: str, path to a .py
    """

    with open(filepath, "r") as f:
        p = ast.parse(f.read())

    # get all classes from the given python file.
    classes = [c for c in ast.walk(p) if isinstance(c, ast.ClassDef)]
    functions = [c for c in ast.walk(p) if isinstance(c, ast.FunctionDef)]

    out = dict()
    for x in classes:
        funcs = [
            fun for fun in ast.walk(x) if isinstance(fun, ast.FunctionDef)
        ]
        out[x.lineno] = {}
        out[x.lineno]["isclass"] = True
        out[x.lineno]["name"] = x.name
        out[x.lineno]["funcs"] = [fun.name for fun in funcs]
        out[x.lineno]["cls"] = x
        out[x.lineno]["line"] = x.lineno
        out[x.lineno]["doc"] = ast.get_docstring(x)
        out[x.lineno]["funcs_docs"] = [ast.get_docstring(fun) for fun in funcs]
        out[x.lineno]["funcs_lines"] = [func.lineno for func in funcs]

        out[x.lineno]["def"] = []  # the def func(args) line of each function
        for fun in funcs:
            out[x.lineno]["def"].append(
                [l for l in unparse(fun).split("\n") if "def " in l][0]
            )

    # Get the lineno of all functions that are classes methods
    methods = []
    for x in out.values():
        methods.extend(x["funcs_lines"])

    for f in functions:
        if f.lineno in methods:
            continue
        out[f.lineno] = dict(
            name=f.name,
            isclass=False,
            func=f,
            line=f.lineno,
            doc=ast.get_docstring(f),
        )
        out[f.lineno]["def"] = [
            l for l in unparse(f).split("\n") if "def " in l
        ][0]

    return collections.OrderedDict(sorted(out.items()))


# -------------------------------- Write to md -------------------------------#
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


def write_to_md(data, savepath):
    """
        Writes to a markdown file the content of a .py file.
        It writes name of all the classes and their methods with
        the corresponding docstrings.

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
