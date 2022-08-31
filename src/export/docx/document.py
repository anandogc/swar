import json
from ..graphql import client

from docx import Document
from docx.shared import Inches

def JSON_to_Docx(text, values):

    backup = ''
    skip_para = False
    document = Document()

    document.add_heading(values["Title"], 0)

    p = document.add_paragraph('')

    for segment in text["ops"]:
        if "attributes" in segment:
            for attribute in segment["attributes"]:
                if "bold" in attribute:
                    p.add_run(backup)
                    p.add_run(segment["insert"]).bold = True
                    backup = ""

                elif "italic" in attribute:
                    p.add_run(backup)
                    p.add_run(segment["insert"]).italic = True
                    backup = ""

                elif "underline" in attribute:
                    p.add_run(backup)
                    p.add_run(segment["insert"]).underline = True
                    backup = ""

                elif "header" in attribute:
                    document.add_heading(backup, level=segment["attributes"]["header"])
                    p = document.add_paragraph('')
                    backup = ""
                    # skip_para = True

        elif type(segment["insert"]) == str:
            if len(backup) > 0:
                parts = backup.split("\n")
                if len(parts)>0:
                    for i in range(len(parts)):
                        p.add_run(parts[i])
                        if i<len(parts)-1:
                            p = document.add_paragraph('')

            backup = segment["insert"]

        else:
            print("Unknown element: ", backup)

    if len(backup) > 0:
        parts = backup.split("\n")
        if len(parts)>0:
            for i in range(len(parts)):
                p.add_run(parts[i])
                if i<len(parts)-1:
                    p = document.add_paragraph('')
        backup = ''

    return document