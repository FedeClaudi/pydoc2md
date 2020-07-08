import textwrap


def wrap_string(string, max_length=70, indent=True):
    string = textwrap.wrap(string, width=max_length)

    if indent:
        string = ["    " + s if n > 0 else s for n, s in enumerate(string)]

    return "\n".join(string)


def strip_wrap_string(string, **kwargs):
    lines = []
    for line in string.split("\n"):
        if line.strip() == "":
            continue
        lines.append(wrap_string(line, **kwargs) + "\n")
    return "\n".join(lines)
