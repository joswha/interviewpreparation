# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorderSearch(root):
    path = []
    total = 0
    if root:
        if not root.left and not root.right:
        path.append(root.val)
        path += preorderSearch(root.left)
        path += preorderSearch(root.right)
    return path
        

def hasPathSum(root, targetSum):
    """
    :type root: TreeNode
    :type targetSum: int
    :rtype: bool
    """
    cumm = 0
        
    if root:
        cumm += root.val
        if cumm == targetSum:
            return True
        if root.left:
            cumm += hasPathSum(root.left, targetSum)
        else:
            cumm -= root.val
        if root.right:
            cumm += hasPathSum(root.right, targetSum)
        else:
            cumm -= root.val
        
    return False

n1 = TreeNode(5)
n2 = TreeNode(4)
n3 = TreeNode(11)
n4 = TreeNode(7)
n5 = TreeNode(2)
n6 = TreeNode(8)
n7 = TreeNode(13)
n8 = TreeNode(4)
n9 = TreeNode(1)

n1.left = n2
n2.left = n3
n3.left = n4
n4.right = n5

n1.right = n6
n6.left = n7
n6.right = n8
n8.right = n9

print(preorderSearch(n1))