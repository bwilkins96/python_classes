class Node:
    def __init__(self, val):
        self.next = None
        self.val = val
    
    def __repr__(self):
        return f'({self.val}) -> {self.next}'

class SinglyLinkedList:

    def __init__(self):
        self.head = Node(0)
        self.tail = self.head
        self.len = 0        

    def _get(self, index: int) -> Node:
        i = 0
        cur = self.head.next

        while i < index:
            cur = cur.next
            i += 1

        return cur
    
    def get(self, index: int) -> int:
        if index >= self.len:
            return -1

        return self._get(index).val

    def addAtHead(self, val: int) -> None:
        node = Node(val)

        node.next = self.head.next
        self.head.next = node

        self.len += 1
        
        if self.len == 1:
            self.tail = node

    def addAtTail(self, val: int) -> None:
        node = Node(val)

        self.tail.next = node
        self.tail = node

        self.len += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.len:
            return
        elif index == self.len:
            return self.addAtTail(val)
        elif index == 0:
            return self.addAtHead(val)

        node = Node(val)
        cur = self._get(index - 1)

        node.next = cur.next
        cur.next = node
        
        self.len += 1     

    def _deleteHead(self):
        if self.len == 0:
            return

        self.head.next = self.head.next.next

        self.len -= 1
    
    def _deleteTail(self):
        if self.len == 0:
            return

        prev = self._get(self.len - 2)
        prev.next = None
        self.tail = prev

        self.len -= 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.len:
            return
        elif self.len == 0:
            return
        elif index == 0:
            return self._deleteHead()
        elif index == self.len - 1:
            return self._deleteTail()
        
        prev = self._get(index - 1)
        prev.next = prev.next.next

        self.len -= 1
    
    def __repr__(self):
        return f'{self.head}'


def test():
    lst = SinglyLinkedList()
    
    lst.addAtHead(1)
    print(lst)

    lst.addAtTail(4)
    print(lst)

    lst.addAtIndex(1, 2)
    print(lst)

    lst.addAtIndex(3, 5)
    print(lst)

    lst.addAtIndex(0, -1)
    print(lst)

    lst.deleteAtIndex(2)
    print(lst)

    lst.deleteAtIndex(0)
    print(lst)

    lst.deleteAtIndex(2)
    print(lst)

    print(lst.get(0))

if __name__ == '__main__':
    test()