import json

from ..graphql import client

from .APS import APS_export
from .Springer import Springer_export

def export_LaTeX(id):
    # Create the query string and variables required for the request.
    query = """
        query {
            projectSearch(id: %d) {
                title
                text
                configuration
            }
        }
    """ % (id)
    variables = {}

    # Synchronous request
    data = client.execute(query=query, variables=variables)

    title = data["data"]["projectSearch"]["title"]
    text = json.loads(data["data"]["projectSearch"]["text"])
    configuration = json.loads(data["data"]["projectSearch"]["configuration"])

    latex = None
    if configuration['project']["values"]["Family"] == "APS":
       latex = APS_export(text, configuration)
    elif configuration['project']["values"]["Family"] == "Springer":
       latex = Springer_export(text, configuration)

    file = open(configuration['project']['values']['Output_folder'] + "/" + title + ".tex", "w")
    file.write(latex)
    file.close()


