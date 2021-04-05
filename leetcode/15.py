def threeSum(nums):
    def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        elems = {k: [] for k in nums}
        for index in range(len(nums)):
            elems[nums[index]].append(index)
        for key, value in elems.items():
            # print(target - key)
            if target - key in elems and key != target - key:
                return[key, target - key]
            if target - key in elems and key == target - key:
                if len(value) > 1:
                    return[value[0], value[1]]
        return []
    res = []
    for i in range(len(nums) - 3):
        a = twoSum(nums[i:], 0 - nums[i])
        if a:
            res.append([nums[i]] + a)

    print(res)

nums = [-1,0,1,2,-1,-4]
threeSum(nums)