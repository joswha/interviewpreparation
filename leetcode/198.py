def rob(nums):
    maximum_sum = 0
    current_sum = 0
    for i in range(1, len(nums) - 1, 2):
        if nums[i] < (nums[i + 1] + nums[i - 1]):
            current_sum += nums[i - 1]
        else:
            current_sum += nums[i]
    print(current_sum)

nums = [1,2,3,1]
rob(nums)