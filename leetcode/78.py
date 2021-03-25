# Given an integer array nums of unique elements, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.
def subsets(nums):
    res = [[]]
    for num in nums:
        res += [curr + [num] for curr in res]
    return res

nums = [1, 2, 3, 4]
print(subsets(nums))