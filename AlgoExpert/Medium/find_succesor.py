# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

def inorderTraverse(root, array):
    if root is None:
        return array
    
    inorderTraverse(root.left, array)
    array.append(root) # this is broken in their compiler, it should be root.value here
    inorderTraverse(root.right, array)

    return array
    
def findSuccessor(tree, node):
    inorder = inorderTraverse(tree, [])

    for index in range(len(inorder)):
        if inorder[index] == node:
            if index + 1 < len(inorder):
                return inorder[index + 1]
            else:
                return None

six = BinaryTree(6, None, None)
five = BinaryTree(5, None, None)
four = BinaryTree(4, six, None)
three = BinaryTree(3, None, None)
two = BinaryTree(2, four, five)
one = BinaryTree(1, two, three)

# print(inorderTraverse(one, []))
print(findSuccessor(one, 5))
