import sys

from export.latex.export import export_LaTeX
from export.docx.export import export_Docx

def export(id, mode):
    if mode == "LaTeX":
        export_LaTeX(id)

    if mode == "Docx":
        export_Docx(id)

export(int(sys.argv[1]), sys.argv[2])