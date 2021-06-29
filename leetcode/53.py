def maxSubArray(nums):
    current_subarray = 0 
    max_subarray = -1000000
    for elem in nums:
        current_subarray += elem
        if current_subarray > max_subarray:
            max_subarray = current_subarray
        if current_subarray < 0:
            current_subarray = 0
    return max_subarray

print(maxSubArray([-1]))