# Validate BST: Implement a function to check if a binary tree is a binary search tree

class Node:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None

    def __repr__(self):
        return self.name

def checkSearchTree(root, min, max):
    if root == None:
        return True
    
    if (min != None and int(root.name) <= min) or (max != None and int(root.name) > max):
        return False
    
    if not checkSearchTree(root.left, min, int(root.name)) or not checkSearchTree(root.right, int(root.name), max):
        return False
    
    return True

#           8
#       4       10
#    2    6         20
#
#

n1 = Node("8")
n2 = Node("4")
n3 = Node("10")
n4 = Node("2")
n5 = Node("6")
# n6 = Node("6")
n7 = Node("20")

n1.left = (n2)
n1.right = (n3)

n2.left = (n4)
n2.right = (n5)

# n4.left = (n6)
n3.right = (n7)

print(checkSearchTree(n1, None, None))