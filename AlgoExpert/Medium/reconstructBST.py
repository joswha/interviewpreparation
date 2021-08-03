# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

class TreeInfo:
    def __init__(self, rootIdx):
        self.rootIdx = rootIdx

def reconstructBst(preOrderTraversalValues):
    treeInfo = TreeInfo(0)
    return reconstructBSTFromRange(float('-inf'), float('inf'), preOrderTraversalValues, treeInfo)

def reconstructBSTFromRange(lower_bound, upper_bound, preOrderTraversalValues, currentInfo):
    if currentInfo.rootIdx == len(preOrderTraversalValues):
        return None

    rootValue = preOrderTraversalValues[currentInfo.rootIdx]

    if rootValue < lower_bound or rootValue >= upper_bound:
        return None
        
    currentInfo.rootIdx += 1
    
    leftSubtree = reconstructBSTFromRange(lower_bound, rootValue, preOrderTraversalValues, currentInfo)
    rightSubtree = reconstructBSTFromRange(rootValue, upper_bound, preOrderTraversalValues, currentInfo)

    return BST(rootValue, leftSubtree, rightSubtree)

# def reconstructBst(preOrderTraversalValues):
#     return constructHelper(preOrderTraversalValues[::-1], float('inf'))

# def constructHelper(array, max_val):
#     if not array or array[-1] > max_val:
#         return None
    
#     root = BST(array.pop())
#     root.left = constructHelper(array, root.value)
#     root.right = constructHelper(array, max_val)

#     return root
