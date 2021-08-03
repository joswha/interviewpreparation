# Majority element
# nums = [2,2,1,1,1,2,2]
# Output: 2
# Runtime: 144 ms, faster than 50.92% of Python online submissions for Majority Element.
# Memory Usage: 14.6 MB, less than 87.19% of Python online submissions for Majority Element.
def majorityElement(nums):
    nrs_dict = {k: 0 for k in nums}
    max_len = 0
    max_elem = 0
    for elem in nums:
        nrs_dict[elem] += 1
        if nrs_dict[elem] > max_len:
            max_len = nrs_dict[elem]
            max_elem = elem

    print(f"Max length: {max_len} with maximum element {max_elem}")

# alternative:
# n = len(nums)
# nums.sort()
# return nums[n/2] ;basically the median