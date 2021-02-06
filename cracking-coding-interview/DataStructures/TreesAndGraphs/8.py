# First common ancestor: Design an algorithm and write code to find the first common ancestor of two nodes in a binary tree. Avoid storing additional nodes in a data structure. NOTE:
# It is not necesasrily a binary search tree

class Node:
    def __init__(self, name):
        self.name = name
        self.parent = None

    def __repr__(self):
        return self.name


def findCommonParent(p, q):
    delta = depth(p) - depth(q)
    first = q if delta > 0 else p
    second = p if delta > 0 else q

    # Move the node that is deeper up
    second = goUp(second, abs(delta))

    while first != second and first != None and second != None:
        first = first.parent
        second = second.parent
    
    return (None if first == None or second == None else first)

def goUp(node, delta):
    while delta:
        node = node.parent
        delta -= 1
    return node

def depth(node):
    depth = 0
    while node:
        node = node.parent
        depth += 1
    return depth

node1 = Node("a")
node2 = Node("b")
node3 = Node("c")
node4 = Node("d")
node5 = Node("e")
node6 = Node("f")
node7 = Node("g")
node8 = Node("h")

node8.parent = node1
node2.parent = node1

node3.parent = node2
node4.parent = node2

node5.parent = node4
node6.parent = node4

node7.parent = node3

print(findCommonParent(node6, node7))