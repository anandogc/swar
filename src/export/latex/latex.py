import json
from ..graphql import client
from flask import render_template
from pathlib import Path

import jinja2

swar = Path(__file__).parent.parent.parent


template_loc = swar / "templates"

jinja_loader = jinja2.Environment(loader=jinja2.FileSystemLoader(template_loc))

def render_jinja(file_name,**context):
    return jinja_loader.get_template(file_name).render(context)


def JSON_to_LaTeX(text):

    backup = ""
    document = ""

    for segment in text["ops"]:
        if "attributes" in segment:
            for attribute in segment["attributes"]:
                if "bold" in attribute:
                    document += backup + r"\textbf{" + segment["insert"] + "}"
                    backup = ""
                elif "italic" in attribute:
                    document += backup + r"\textit{" + segment["insert"] + "}"
                    backup = ""
                elif "underline" in attribute:
                    document += backup + r"\underline{" + segment["insert"] + "}"
                    backup = ""
                elif "header" in attribute:
                    if segment["attributes"]["header"] == 1:
                        document += "\n\\section{" + backup + "}\n"
                    elif segment["attributes"]["header"] == 2:
                        document += "\n\\subsection{" + backup + "}\n"
                    elif segment["attributes"]["header"] == 3:
                        document += "\n\\subsubsection{" + backup + "}\n"
                    elif segment["attributes"]["header"] == 4:
                        document += "\n\\subsubsubsection{" + backup + "}\n"
                    backup = ""


        elif type(segment["insert"]) == dict:
            if "formula" in segment["insert"]:
                    document += backup + r"\(" + segment["insert"]["formula"] + r" \)"
                    backup = ""
            elif "equation" in segment["insert"]:
                    document += backup + "\n" + segment["insert"]["equation"] + "\n"
                    backup = ""
            elif "figure" in segment["insert"]:
                    document += backup + """
\\begin{figure}
\\includegraphics[width=""" + segment["insert"]["figure"]["width"].replace("%", r"\\lineqidth") + """]{""" + segment["insert"]["figure"]["src"] + """}
\\caption{""" + segment["insert"]["figure"]["caption"] + """}
\\label{fig:boat1}
\\end{figure}
"""
                    backup = ""
        elif type(segment["insert"]) == str:
            document += backup.replace("\n", "\n\n")

            backup = segment["insert"]
        else:
            print("Unknown element: ", segment["insert"])

    document += backup.replace("\n", "\n\n")

    return document
