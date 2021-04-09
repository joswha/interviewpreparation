def findKthLargest(nums, k):
    nums.sort()
    return nums[-k]


nums = [3,2,3,1,2,4,5,5,6]
k = 4
print(findKthLargest(nums,k))