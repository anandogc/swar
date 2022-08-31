import re
from parchment import TextElement


from .attributor import Attributor

def match(node: TextElement, prefix: str): list[str]
  className = node.getAttribute('class') or ''
  
  return list(re.split(r'\s+',className).filter(lambda name: name.index(prefix) == 0, my_list))


class ClassAttributor(Attributor):
  def keys(node: TextElement): list[str]
    classNames = node.getAttribute('class') or ''
    return re.split(r'\s+', classNames).filter(lambda name: "-".join(name.split('-')[0:-1]))

  def add(node: TextElement, value: str): bool
    if not self.canAdd(node, value):
      return False

    self.remove(node)
    node.classList.insert(f"{self.keyName}-{value}")
    return True

  def remove(node: TextElement): None
    matches = match(node, self.keyName)
    matches = map(lambda name: node.classList.remove(name), matches)

    if len(node.classList) == 0:
      node.removeAttribute('class')

  def value(node: TextElement): str
    result = match(node, self.keyName)[0] or ''
    value = result[:self.keyName.length + 1] # +1 for hyphen
    return value if self.canAdd(node, value) else ''
