def constructMinHeightBst(array, start, end):
    if end < start:
        return None
    
    mid = (end + start) // 2
    root = BST(array[mid])
    root.left = constructMinHeightBst(array, start, mid - 1)
    root.right = constructMinHeightBst(array, mid + 1, end)

    return root

def minHeightBst(array):
    return constructMinHeightBst(array, 0, len(array) - 1)

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
