class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBst(nums):
    if not nums:
        return None
    
    mid = len(nums) // 2

    root = TreeNode(nums[mid])
    root.left = sortedArrayToBst(nums[:mid])
    root.right = sortedArrayToBst(nums[mid + 1:])

    return root


nums = [-10,-3,0,5,9]