# insert // insert value into tree
# get_node_count // get count of values stored
# print_values // prints the values in the tree, from min to max
# delete_tree
# is_in_tree // returns true if given value exists in the tree
# get_height // returns the height in nodes (single node's height is 1)
# get_min // returns the minimum value stored in the tree
# get_max // returns the maximum value stored in the tree
# is_binary_search_tree
# delete_value
# get_successor // returns next-highest value in tree after given value, -1 if none

class Node:
    """
    Single node from the tree
    """
    def __init__(self, value = None):
        self.left = None
        self.right = None
        self.value = value
    
    def PrintNodes(self):
        print(self.value)
        if self.left:
            self.left.PrintNodes()
        if self.right:
            self.right.PrintNodes()

class Tree:
    def __init__(self):
        self.root = None

    def insert(self,value):
        if(self.root is None):
            self.root = value # add Node(value) if we will not insert Nodes directly
        else:
            self._insert(value, self.root)

    def _insert(self, value, current):
        if(current.value > value):
            if(current.left is None):
                current.left = value # add Node(value) if we will not insert Nodes directly
            else:
                self._insert(value, current.left)
        else:
            if(current.right is None):
                current.right = value # add Node(value) if we will not insert Nodes directly
            else:
                self._insert(value, current.right)
    
    def PrintTree(self):
        if self.root is None:
            print("Tree is empty")
            return
        else:
            print(self.root.value)
        if self.root.left:
            self.root.left.PrintNodes()
        if self.root.right:
            self.root.right.PrintNodes()
    
    def deleteTree(self):
        self.root = None
    
def get_node_count(root):
    count = 1
    if root is None:
        return -1
    else:
        if root.left is not None:
            count += get_node_count(root.left)
        if root.right is not None:
            count += get_node_count(root.right)
    return count

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n2_l = Node(4)
n3_r = Node(5)
n3_l = Node(10)

n2.left = n2_l
n3.left = n3_l
n3.right = n3_r

n1.left = n2
n1.right = n3

t = Tree()
t.insert(n1)

# print(t)
# t.PrintTree()
# print(get_node_count(t.root))

t.PrintTree()
t.deleteTree()
t.PrintTree()

# n1.PrintNodes()
