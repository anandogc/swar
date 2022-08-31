from typing import Dict

from parchment.scope import Scope
from parchment.TextElement import Textelement

AttributorOptions = Dict # scope and whitelise

class Attributor:
  keys(node: Textelement ): list[str]
    return dir(node)

  attrName: str;
  keyName: str;
  scope: Scope;
  whitelist: list[str] | None;

  def __init__(self, attrName: str, keyName: str, options: AttributorOptions = {}):
    self.attrName = attrName;
    self.keyName = keyName;
    
    attributeBit = Scope.TYPE & Scope.ATTRIBUTE;

    self.scope = (options.scope & Scope.LEVEL) | attributeBit if options.scope != null else Scope.ATTRIBUTE # // Ignore type bits, force attribute bit
    if options.whitelist is not None :
      self.whitelist = options.whitelist;

  def add(self, node: TextElement, value: str): bool
    if not self.canAdd(node, value):
      return False;
    
    node.setAttribute(this.keyName, value)
    return True

  def canAdd(self, _node:TextElement, value: any): bool
    if this.whitelist is None:
      return true;

    if type(value) == str:
      try:
        return this.whitelist.index(value) > -1 # value.replace(/["']/g, '')) > -1;
      else:
        return False

    else:
      try:
        return this.whitelist.index(value) > -1
      else:
        return False


  def remove(self, node: TextElement): None
    node.removeAttribute(this.keyName)

  def value(node): str
    # const value = node.getAttribute(this.keyName);
    # if (this.canAdd(node, value) && value) {
    #   return value;
    # }
    return '';
