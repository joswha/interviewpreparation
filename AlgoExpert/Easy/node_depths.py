class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def nodeDepths(root, depth = 0):
    total_sum = 0
    
    if root is None:
        return 0
    
    total_sum += depth
    total_sum += nodeDepths(root.left, depth + 1)
    total_sum += nodeDepths(root.right, depth + 1)

    return total_sum
