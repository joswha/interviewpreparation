def missingNumber(nums):
    n = len(nums)
    nr_set = set(range(n + 1))
    return sum(nr_set) - sum(nums)


nums = [1,2,3,4,0]
print(missingNumber(nums))