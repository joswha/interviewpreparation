class TreeNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_first(self, node):
        node.next = self.head
        self.head = node

    def add_last(self, node):
        if not self.head:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node

    

def allSequences(node):
    result = []

    if node == None:
        result.append(LinkedList())
        return result

    prefix = LinkedList()
    prefix.add_last(node.data)
    
    leftSeq = allSequences(node.left)
    rightSeq = allSequences(node.right)

    for left in leftSeq:
        for right in rightSeq:
            weaved = []
            weaveLists(left, right, weaved, prefix)
            result.append(weaved)
    
    return result

def weaveLists(first, second, results, prefix):
    
    if first.head == None or second.head == None:
        result = prefix
        result.append(first)
        result.append(second)
        results.append(result)
        return
    
    headFirst = first.removeFirst()
    prefix.addLast(headFirst)
    weaveLists(first, second, results, prefix)
    prefix.removeLast()
    first.addFirst(headFirst)

    headSecond = second.removeFirst()
    prefix.addLast(headSecond)
    weaveLists(first, second, results, prefix)
    prefix.removeLast()
    first.addFirst(headSecond)


# NOT TESTED, simply translated the solution from the BOOK