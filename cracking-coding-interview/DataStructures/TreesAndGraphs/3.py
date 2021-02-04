# List of Depths: Given a binary tree, design an algorithm which creates a linked list of all the nodes at each depth(eg, if you have a tree with depth D, D linked lists)
class Node:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None

    def __repr__(self):
        return self.name

# class BinaryTree:
#     def __init__(self):
#        self.nodes = []

# binary = BinaryTree()

# binary.nodes.append(n1)
# binary.nodes.append(n2)
# binary.nodes.append(n3)
# binary.nodes.append(n4)
# binary.nodes.append(n5)
# binary.nodes.append(n6)
# binary.nodes.append(n7)

# print(binary.nodes)

def createLevelList(root):
    result = [[]]
    current = []
    
    if root != None:
        current.append(root)

    while(len(current) > 0):
        result.append(current)
        parents = current
        current = []
        for parent in parents:
            if parent.left != None:
                current.append(parent.left)
            if parent.right != None:
                current.append(parent.right)

    return result

# Driver code
#            [1]
#      [2]         [3]
#   [4]   [5]   [6]   [7]
#

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

n3.left = (n6)
n3.right = (n7)

print(createLevelList(n1))
