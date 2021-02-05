# Check balanced: Implement a function to check if a binary tree is balanced. For the purpose of this question, a balanced tree is defined to be a tree such that the heights of the two subtrees of any
# node never differ by more than one

MINVAL = -1000000000

class Node:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None

    def __repr__(self):
        return self.name

def checkSubtree(root):
    if root == None:
        return -1

    left = checkSubtree(root.left)
    right = checkSubtree(root.right)

    if left == MINVAL:
        return MINVAL
    
    if right == MINVAL:
        return MINVAL
    
    if abs(right - left) > 1:
        return MINVAL
    else:
        return max(right, left) + 1

def isBalanced(root):
    return checkSubtree(root) != MINVAL


n1 = Node("1")
n2 = Node("2")
n3 = Node("3")
n4 = Node("4")
n5 = Node("5")
n6 = Node("6")
n7 = Node("7")

n1.left = (n2)
n1.right = (n3)

n2.left = (n4)
n2.right = (n5)

n4.left = (n6)
# n3.right = (n7)

print(isBalanced(n1))