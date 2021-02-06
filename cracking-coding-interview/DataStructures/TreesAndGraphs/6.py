class Node:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None
        self.parent = None

    def __repr__(self):
        return self.name

def inorderSucc(root):
    if root == None:
        return None

    # Found right children -> need leftmost node of that subtree
    if root.right != None:
        return leftMostChild(root.right)
    else:
        q = root
        x = q.parent
        # No more nodes on the right subtree, we want to go up and then left when we find the previous left subtree
        while x is not None and x.left != q:
            q = x
            x = x.parent
    return x

# Return the leftmost child of the current subtree
def leftMostChild(root):
    if root == None:
        return None
    while root.left != None:
        root = root.left
    return root