# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
def getProduct(nums):
    prod = 0
    for num in nums:
        if num != 0:
            if prod == 0:
                prod = 1
            prod *= num
    return prod

def productExceptSelf(nums):
    prod = 1
    for num in nums:
        prod *= num
    
    return [prod // x if x != 0 else getProduct(nums) for x in nums]
    # res = []
    # for i, val in enumerate(nums):
    #     prod = 1
    #     for elem in nums[:i] + nums[i + 1:]:
    #         prod *= elem
    #     res.append(prod)
    # return res

nums = [1,2,3,4]
print(productExceptSelf(nums))