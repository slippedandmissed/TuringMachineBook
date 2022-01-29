#!/mnt/c/Users/gbt50/AppData/Local/Programs/Python/Python39/python.exe
import pyperclip


def generate_diagram(state, cells, current_index, min_length=21):

    while len(cells) < min_length:
        cells.append("")
        if len(cells) < min_length:
            cells = [""] + cells
            current_index += 1

    cells = ["..."] + cells + ["..."]
    current_index += 1

    cols = [
        f"\\multicolumn{{1}}{{c{'|' if i<len(cells)-1 else ''}}}{{\\symb{{{x}}}}}" for i, x in enumerate(cells)]

    return f"""\\begin{{center}}
\\fbox{{\\begin{{minipage}}{{\\textwidth}}
\\begin{{table}}[H]
\\begin{{center}}
\\begin{{tabular}}{{{'c'*len(cells)}}}
\\multicolumn{{{len(cells)}}}{{l}}{{\\statename{{{state}}}}} \\\\
\\\\ \\hline
{' & '.join(cols)}
\\\\ \\hline
{'& '*current_index}$\\uparrow${' &'*(len(cells)-current_index-1)}
\\end{{tabular}}
\\end{{center}}
\\end{{table}}
\\end{{minipage}}}}
\\end{{center}}
"""


def print_and_copy(s):
    print(s)
    pyperclip.copy(pyperclip.paste() + s)


pyperclip.copy("")
print_and_copy(generate_diagram(
    "X", ["*", "-", "4", "5", ",", "0b255", ",", "NULL", ",", "(", "2", ";", "3", ";", "[", "4", ";", "5", "]", ")"], 19))
