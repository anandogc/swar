import json

from flask import Flask
from flask_jsonrpc import JSONRPC

from export.latex import export_LaTeX

app = Flask('application')
jsonrpc = JSONRPC(app, '/api', enable_web_browsable_api=True)

@jsonrpc.method('App.LaTeX')
def to_LaTeX(data: str) -> str:
    pass

def export(id, mode):
    if mode == "LaTeX":
        print(export_LaTeX(id))

export(2, "LaTeX")

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)