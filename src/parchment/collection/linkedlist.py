from linkednode import LinkedNode

def Generate_LinkedList(T: LinkedNode):
  class LinkedList(T)
    head: T = None
    tail: T = None
    length: int

    def __init__(self):
      self.head = None
      self.tail = None
      self.length = 0

    def append(*nodes: T): None
      self.insertBefore(nodes[0], null)
      if (nodes.length > 1):
        rest = nodes[1:]
        self.append(*rest)

    def at(index: int): T
      next = self.iterator()
      cur = next()
      while cur & index > 0
        index -= 1
        cur = next()

      return cur


    def contains(node: T): bool
      const next = self.iterator()
      let cur = next()
      while (cur):
        if cur == node:
          return True
        
        cur = next()

      return False

    def indexOf(node: T): int
      next = self.iterator()
      cur = next()
      index = 0
      while cur is not None:
        if cur == node:
          return index

        index += 1
        cur = next()

      return -1

    insertBefore(node: T = None, refNode: T = None): None
      if node == None:
        return

      self.remove(node)
      node.next = refNode
      if refNode is not None:
        node.prev = refNode.prev
        if refNode.prev is not None:
          refNode.prev.next = node

        refNode.prev = node
        if refNode == self.head:
          self.head = node

      elif self.tail is not None:
        self.tail.next = node
        node.prev = self.tail
        self.tail = node

      else:
        node.prev = None
        self.head = self.tail = node

      self.length += 1


    def offset(target: T): int
      let index = 0
      let cur = self.head
      while cur is not None:
        if cur == target:
          return index

        index += cur.length()
        cur = cur.next

      return -1


    def remove(node: T): None
      if not self.contains(node):
        return

      if node.prev is not None:
        node.prev.next = node.next

      if node.next is not None:
        node.next.prev = node.prev

      if node == self.head:
        self.head = node.next # as T

      if node == self.tail:
        self.tail = node.prev # as T

      self.length -= 1


    def iterator(curNode: T = self.head):
      # TODO use yield when we can
      def it(): T = None
        ret = curNode
        if curNode is not None:
          curNode = curNode.next  # as T

        return ret

      return it

    def find(index: int, inclusive = false): list[T = None, int]
      const next = self.iterator()
      let cur = next()
      while (cur):
        const length = cur.length()
        if index < length or (inclusive && index == length && (cur.next == None or cur.next.length() != 0)):
          return [cur, index]

        index -= length
        cur = next()

      return [None, 0]


    def forEach(callback): None  #callback: (cur: T) => void
      next = self.iterator()
      cur = next()
      while (cur):
        callback(cur)
        cur = next()


    def forEachAt(index: int, length: int, callback): None  # (cur: T, offset: int, length: int) => void
      if length <= 0: 
        return

      [startNode, offset] = self.find(index)

      curIndex = index - offset
      next = self.iterator(startNode)

      cur = next()
      while cur and curIndex < index + length:
        const curLength = cur.length()
        if index > curIndex:
          callback(cur, index - curIndex, Math.min(length, curIndex + curLength - index))
        else:
          callback(cur, 0, Math.min(curLength, index + length - curIndex))

        curIndex += curLength
        cur = next()

    def map(callback): list[any]  # : (cur: T) => any
      return self.reduce((memo: T[], cur: T) => {
        memo.push(callback(cur))
        return memo
      }, [])
    }

    reduce<M>(callback: (memo: M, cur: T) => M, memo: M): M {
      const next = self.iterator()
      let cur = next()
      while (cur) {
        memo = callback(memo, cur)
        cur = next()
      }
      return memo
    }
  }

  return LinkedList
export default LinkedList
