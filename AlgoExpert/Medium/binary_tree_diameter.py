class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class TreeHelper:
    def __init__(self, diameter, height):
        self.diameter = diameter
        self.height = height

def getTreeHelper(tree):
    if tree is None:
        return TreeHelper(0, 0)
    
    leftTree = getTreeHelper(tree.left)
    rightTree = getTreeHelper(tree.right)

    longestPath = leftTree.height + rightTree.height
    maxDiameter = max(leftTree.diameter, rightTree.diameter)
    currentDiameter = max(longestPath, maxDiameter)
    currentHeight = 1 + max(leftTree.height, rightTree.height)

    return TreeHelper(currentDiameter, currentHeight)

def binaryTreeDiameter(tree):
    return getTreeHelper(tree).diameter

