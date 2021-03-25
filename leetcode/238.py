# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
def productExceptSelf(nums):
    prod = 1
    for num in nums:
        prod *= num
    return [prod // x if x != 0 else 0 for x in nums]

nums = [-1,1,0,-3,3]
print(productExceptSelf(nums))