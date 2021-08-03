# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def helper(root, runningSum, sums):
	
	if root is None:
		return
	
	newSum = runningSum + root.value
	
	if root.left is None and root.right is None:
		sums.append(newSum)
		return
	
	helper(root.left, newSum, sums)
	helper(root.right, newSum, sums)
		
# def branchSums(root):
#     # Write your code here.
# 	sums = []
#     helper(root, 0, sums)
#     return sums
