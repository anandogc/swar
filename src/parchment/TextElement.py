from typing import Dict

class TextElement:
    style: Dict = {}
    value: str = ""
    classList: list = []
    nodes: list[TextElement] = []

    def setAttribute(self, attribute, value):
        super(TextElement, self).__setattr__(attribute, value)

    def removeAttribute(self, attribute):
        try:
            super(TextElement, self).__delattr__(attribute, value)
        except:
            pass

    def getAttribute(self, attribute)
        try:
            return super(TextElement, self).__getattribute__(attribute, value)
        except:
            return None

    def remove(self, node: TextElement): None
        nodes.remove(node)