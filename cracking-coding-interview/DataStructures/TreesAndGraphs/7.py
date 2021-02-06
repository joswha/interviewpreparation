# You are given a list of projects and a list of dependencies(which is a list of pairs of projects, where the second project is dependend on the first project.) ALl of a project's dependencies must be built
# before the project is. Find a build order that will allow the projects to be built. If there is no valid build order, return an error.

# projects: a, b, c, d, e, f
# dependencies: (a,d), (f,b), (b,d), (f,a), (d,c)

class Node:
    def __init__(self, name):
        self.name = name
        self.ancestors = []

    def __repr__(self):
        return self.name

class QueueNodes:
    def __init__(self, nodes):
        self.nodes = nodes


node1 = Node("a")
node2 = Node("b")
node3 = Node("c")
node4 = Node("d")
node5 = Node("e")
node6 = Node("f")

# Manually rewriting the dependencies as how we would have interpreted them
node1.ancestors.append(node4)
node6.ancestors.append(node2)
node2.ancestors.append(node4)
node6.ancestors.append(node1)
node4.ancestors.append(node3)

queue = QueueNodes([node1, node2, node3, node4, node5, node6])
ancestorList = []

for node in queue.nodes:
    # print(node)
    if node.ancestors != []:
        for ancestor in node.ancestors:
            if ancestor not in ancestorList:
                ancestorList.append(ancestor)

# print(ancestorList)
for node in queue.nodes:
    if node not in ancestorList:
        print(node)

for node in ancestorList:
    print(node)
