import json

from ..graphql import client
from .document import JSON_to_Docx

def export_Docx(id):
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

    document = JSON_to_Docx(text, configuration['project']['values'])

    document.save(configuration['project']['values']['Output_folder'] + '/' + title + '.docx')

