def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    k = 0
    for index, value in enumerate(nums):
        if value == 0:
            k += 1
    
    i = 0
    while i < len(nums) - 1:
        if nums[i] == 0 and k > 0:
            nums.pop(i)
            nums.append(0)
            k -= 1
        else:
            i += 1
    
    return nums

nums = [0, 0, 1]
print(moveZeroes(nums))