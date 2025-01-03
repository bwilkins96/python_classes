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
        self.nodes = {}

    def add(self, val):
        node = Node(val)
        node.prev = self.tail
        self.tail.next = node
        self.tail = node

        self.nodes[val] = node
    
    def remove(self, val):
        node = self.get(val)

        if node is None:
            return
        
        node.prev.next = node.next

        if node.next:
            node.next.prev = node.prev

        if node is self.tail:
            self.tail = node.prev
        
        node.next = None
        node.prev = None
        self.nodes.pop(val)

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
        return len(self.nodes)
    
    def __repr__(self):
        return str(self.nodes)