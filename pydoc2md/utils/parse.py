import ast
from astunparse import unparse
import collections


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

    # Get all functions
    functions = [c for c in ast.walk(p) if isinstance(c, ast.FunctionDef)]

    # Get classes data
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
    # To avoid taking them twice,
    methods = []
    for x in out.values():
        methods.extend(x["funcs_lines"])

    # Get all functions that are not class methods
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
