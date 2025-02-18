from collections import defaultdict

class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None
    
    def __repr__(self):
        return f'({self.val})'

class LinkedList:
    def __init__(self):
        self.head = Node('head')
        self.tail = self.head
        self.nodes = defaultdict(set)
        self.size = 0

    def add(self, val):
        node = Node(val)
        node.prev = self.tail
        self.tail.next = node
        self.tail = node

        self.nodes[val].add(node)
        self.size += 1
    
    def addFront(self, val):
        if self.empty():
            self.add(val)
            return
        
        node = Node(val)
        node.next = self.head.next
        self.head.next = node
        node.prev = self.head

        if node.next:
            node.next.prev = node

        self.nodes[val].add(node)
        self.size += 1
    
    def _remove(self, node):
        if node is None:
            return
        
        node.prev.next = node.next

        if node.next:
            node.next.prev = node.prev

        if node is self.tail:
            self.tail = node.prev
        
        node.next = None
        node.prev = None
        self.nodes[node.val].remove(node)
        self.size -= 1

    def remove(self, node):
        self._remove(node)
       
    def removeHead(self):
        head = self.getHead()
        self._remove(head)
        return head
    
    def removeTail(self):
        tail = self.getTail()
        self._remove(tail)
        return tail

    def empty(self):
        return self.head.next is None

    def getHead(self):
        return self.head.next
    
    def getHeadVal(self):
        head = self.getHead()

        if head is None:
            return ''
        
        return head.val
    
    def getTail(self):
        if self.head is self.tail:
            return None
        
        return self.tail

    def get(self, val):
        return self.nodes.get(val, None) 
    
    def contains(self, val):
        return self.get(val) is not None
    
    def getNodes(self):
        nodes = []
        cur = self.head.next

        while cur:
            nodes.append(cur)
            cur = cur.next

        return nodes
    
    def __len__(self):
        return self.size
    
    def __repr__(self):
        return str(self.nodes)