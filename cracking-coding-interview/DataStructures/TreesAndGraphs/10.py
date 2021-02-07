# Given two binary trees T1 and T2, check if T2 is a subtree of T1

class Node:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None

    def __repr__(self):
        return self.name

def findFirstRoot(root1, root2):
    var_left = None
    var_right = None
    if root1 and root2: 
        if root1.name != root2.name:
            # print(root1)
            var_left = findFirstRoot(root1.left, root2)
            var_right = findFirstRoot(root1.right, root2)
            if var_left != None:
                return var_left
            else:
                return var_right
        else:
            return root1

# tree = []
def preorderSearch(root, tree):    
    if root:
        tree.append(root)  
        preorderSearch(root.left, tree)
        preorderSearch(root.right, tree)
    return tree
        
def checkSubtree(root1, root2):
    gasit = findFirstRoot(root1, root2)
    if gasit:
        tree1 = preorderSearch(gasit, [])
        print(tree1)
        tree2 = preorderSearch(root2, [])
        print(tree2)
        response = False
        for node1, node2 in zip(tree1, tree2):
            if node1.name == node2.name:
                response = True
        return response
    else:
        return False


# Driver code
node1 = Node("1")
node2 = Node("2")
node3 = Node("3")
node4 = Node("4")
node5 = Node("5")
node6 = Node("6")
node7 = Node("7")
node8 = Node("8")
node9 = Node("9")
node10 = Node("10")

node11 = Node("1")
node22 = Node("2")
node33 = Node("3")
node44 = Node("4")


node11.right = node44
node11.left = node22
node22.right = node33


node5.right = node7
node5.left = node6
node6.right = node8
node8.left = node1
node1.right = node4
node1.left = node2
node2.right = node3
node7.right = node9
node7.left = node10

print(checkSubtree(node5, node11))
# print([node11, node1] == [node1, node11])
# print(gasit)
# print(gasit)
# print(preorderSearch(node11, []))
# print(preorderSearch(node5, []))
# checkSubtree(node5, node11)
# print(preorderSearch(node11, []) in preorderSearch(node5, []))
# resultTree1 = preorderSearch(node5, [])
# resultTree2 = preorderSearch(node11, [])

