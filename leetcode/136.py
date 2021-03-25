# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
def singleNumber(nums):
    print(set(nums))
    return 2 * sum(set(nums)) - sum(nums)

a = [1, 2, 3, 2, 1]
print(singleNumber(a))