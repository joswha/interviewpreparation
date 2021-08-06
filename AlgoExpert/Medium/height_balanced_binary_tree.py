# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class TreeInfo:
    def __init__(self, isBalanced, height):
        self.isBalanced = isBalanced
        self.height = height

def heightBalancedBinaryTree(tree):
    # Write your code here.
    treeInfo = getTreeInfo(tree)
    return treeInfo.isBalanced

def getTreeInfo(tree):
    if tree is None:
        return TreeInfo(True, -1)
    
    leftSubtree = getTreeInfo(tree.left)
    rightSubtree = getTreeInfo(tree.right)

    isBalanced = (leftSubtree.isBalanced and rightSubtree.isBalanced and abs(leftSubtree.height - rightSubtree.height) <= 1)

    height = max(leftSubtree.height, rightSubtree.height) + 1
    return TreeInfo(isBalanced, height)