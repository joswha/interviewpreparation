# Minimal Tree: Given a sorted array with unieuq integer elements write an algorithm to create a binary search tree with minimal height.
class Node:
    def __init__(self, name):
        self.name = name
        self.right = None
        self.left = None

    # def __iter__(self):
    #     return self
    
    def __repr__(self):
        return self.name

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.name)
        if self.right:
            self.right.printTree()

def minimal_tree(array, start, end):
    if end < start:
        return None
    
    mid = (start + end) // 2
    
    n = Node(arr[mid])
    
    n.left = minimal_tree(arr, start, mid - 1)
    n.right = minimal_tree(arr, mid + 1, end)
    
    return n




arr = ["1","2","3","4","5","6","7","8","9"]
# print(minimal_tree(arr, 0, 8))
tree = minimal_tree(arr, 0, 8)
tree.printTree()


