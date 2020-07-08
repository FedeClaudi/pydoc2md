from mdutils.mdutils import MdUtils


def add_header(md, nlines, level, title):
    # header
    md.new_paragraph("&nbsp;")
    for n in range(nlines):
        md.new_paragraph("--------")

    md.new_header(level=level, title=title)


def add_github_link(md, githubpath, lineno):
    if githubpath is not None:
        url = githubpath + f"#L{lineno}"
        md.new_line(
            "Check the "
            + md.new_inline_link(
                link=url, text="source code", bold_italics_code="cbi"
            )
            + " online"
        )


def add_docstring(md, doc):
    md.new_header(level=5, title="docstring")
    md.new_line()
    if doc is None:
        doc = """ no docstring """
    else:
        doc = "    " + doc.replace("\n", "\n    ")

    md.insert_code('\n"""\n' + doc + '\n"""', language="python")


def add_class_to_md(md, cl, githubpath=None):
    """
        Adds a class docstring and definition to the
        md file, including all class methods.
    """
    # header
    add_header(md, 2, 1, f'**{cl["name"]}**')

    # class docstring
    if cl["doc"] is not None:
        md.insert_code(cl["doc"])

    else:
        md.new_paragraph("")

    # for each class method
    for func, doc, lineno, df in zip(
        cl["funcs"], cl["funcs_docs"], cl["funcs_lines"], cl["def"]
    ):
        # header
        add_header(md, 1, 1, f"line: {lineno} - `{func}`")

        # github link
        add_github_link(md, githubpath, lineno)

        # function def
        md.new_header(level=4, title="function definition")
        md.insert_code(df, language="python")

        # docstring
        add_docstring(md, doc)


def add_func_to_md(md, cl, githubpath=None):
    """
        Adds a function docstring and definition to the
        md file
    """
    # header
    add_header(md, 1, 1, f"line: {cl['line']} - `{cl['name']}`")

    # github line link
    add_github_link(md, githubpath, cl["line"])

    # function definition
    md.new_header(level=4, title="function definition")
    md.insert_code(cl["def"], language="python")

    # docstring
    add_docstring(md, cl["doc"])


def py_to_md(data, savepath, githubpath=None):
    """
        Writes to a markdown file the content of a .py file.
        It writes the name of all the classes and their methods with
        the corresponding docstrings as well as all functions that
        are not class methods.

        :param data: dictionary of classes that belong to a .py,
                        from parse_pyfile
        :param savepath: str, path to the .md file to save
        :param githubpath: str, optional. URL to the same .py on github
    """
    print(f"writing - {savepath}")
    md = MdUtils(file_name=savepath)

    # Iterate classes
    for cl in data.values():

        # class/function specific
        if cl["isclass"]:
            add_class_to_md(md, cl, githubpath=githubpath)
        else:
            add_func_to_md(md, cl, githubpath=githubpath)

    md.new_table_of_contents(table_title="Contents", depth=2)
    md.create_md_file()


def folder_md(savepath):
    print(f"writing - {savepath}")
    md = MdUtils(file_name=str(savepath))
    md.create_md_file()


def write_summary_file(paths, leaves, savepath):
    print(f"writing - {savepath}")
    md = MdUtils(file_name=str(savepath))

    for leaf in sorted(leaves):
        try:
            name = [
                name
                for name, (path, filepath) in paths.items()
                if path == leaf
            ][0]
        except IndexError:
            path, filepath = paths[leaf[-2]]
        else:
            path, filepath = paths[name]

        if path is None:
            tabs = len(leaf) - 3
        else:
            tabs = len(path) - 2

        md.new_line("    " * tabs + "* " + f"[{filepath.name}]({filepath})")

    md.create_md_file()
