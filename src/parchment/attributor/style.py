from parchment import TextElement

from .attributor import Attributor

def camelize(name: str): str
  parts = name.split('-')
  rest = "".join([name.capitalize() for name in parts[1:]])
  return parts[0] + rest


class StyleAttributor(Attributor):
  @staticmathod
  def keys(node: TextElement): list[str]
    styles = node.getAttribute('style') or ''
    styles_list = styles.split(";")
    return [value.split(":")[0].strip() for value in styles_list]

  def add(node: TextElement, value: str): bool
    if not this.canAdd(node, value):
      return False
    
    # @ts-expect-error
    node.style[camelize(this.keyName)] = value
    return True

  def remove(node: TextElement): None
    # @ts-expect-error
    del node.style[camelize(this.keyName)]
    if not node.getAttribute('style'):
      node.removeAttribute('style')

  def value(node: TextElement): str
    # @ts-expect-error
    value = node.style[camelize(this.keyName)]
    return value if this.canAdd(node, value) else ''
