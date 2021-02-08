# Given a binary tree in which each node contains an integer(positive or negative) Design an algorithm to count the number of paths that sum to a 
# given value. THe path does not need to start or end at the root or a leaf, but it must go downwards

class Node:
    def __init__(self, name):
        self.name = name
        self.right = None
        self.left = None

    def __repr__(self):
        return self.name

k = 0

def pathSums(root, total_sum, current_sum):
    sum_left = 0
    sum_right = 0
    if root:
        print(root, current_sum)
        current_sum += int(root.name)
        if current_sum != total_sum:
            sum_left = pathSums(root.left, total_sum, current_sum)
            sum_right = pathSums(root.right, total_sum, current_sum)
            if sum_left != 0:
                return sum_left
            else:
                return sum_right
        else:
            print ("Found sum " + str(total_sum))
            current_sum = 0
    else:
        current_sum = 0


node1 = Node("2")
node2 = Node("3")
node3 = Node("5")
node4 = Node("10")
node5 = Node("6")
node6 = Node("9")
node7 = Node("1")
node8 = Node("5")

node1.left = node2
node1.right = node3

node3.right = node6

node2.left = node4
node2.right = node5

node4.right = node7
node5.right = node8

pathSums(node1, 16, 0)