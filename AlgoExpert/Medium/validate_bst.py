# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def validateBst(tree):
    return validateHelper(tree, float("-inf"), float("inf"))

def validateHelper(tree, minVal, maxVal):
    if not tree:
        return True
    
    if tree.value < minVal and tree.value >= maxVal:
        return False
    
    leftValid = validateHelper(tree.left, minVal, tree.value)
    rightValid = validateHelper(tree.right, tree.value, maxVal)

    return leftValid and rightValid