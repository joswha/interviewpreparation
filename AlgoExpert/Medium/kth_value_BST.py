# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def inorderTraverse(tree, array):
    if tree is None:
        return array

    inorderTraverse(tree.left, array)
    array.append(tree.value)
    inorderTraverse(tree.right, array)

    return array

def findKthLargestValueInBst(tree, k):
    return inorderTraverse(tree, [])[-k]
