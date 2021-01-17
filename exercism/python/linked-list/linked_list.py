class Node:
    def __init__(self, value, succeeding=None, previous=None):
        self.value = value
        self.succeeding = succeeding
        self.previous = previous


class LinkedList:
    def __init__(self):
        self.head = None
        self._len = 0

    def __len__(self):
        return self._len

    def __iter__(self):
        h = self.head
        while h is not None:
            yield h.previous.value
            h = h.previous
            if h == self.head:
                return
    
    def push(self, value):
        self._len += 1
        node = Node(value)
        if self.head == None:
            self.head = node.next = node.previous = node
        else:
            node.next = self.head
            node.previous = self.head.previous
            self.head.previous.next = self.head.previous = self.head = node

    def pop(self):
        self._len = -1
        node = self.head
        if self.head.next == self.head:
            self.head = None
        else:
            node.previous.next = self.head = node.next
            self.head.previous = node.previous
    
        return node.value
    
    def shift(self):
        self.head = self.head.previous
        value = self.pop()
        return value

    def unshift(self, value):
        if self.head is not None:
            self.head = self.head.previous
        self.push(value)
        self.head = self.head.next

