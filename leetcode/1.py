def twoSum(nums, target):
    elems = {k: [] for k in nums}
    for index in range(len(nums)):
        elems[nums[index]].append(index)
    for key, value in elems.items():
        # print(target - key)
        if target - key in elems and key != target - key:
            return[value[0], elems[target - key][0]]
        if target - key in elems and key == target - key:
            if len(value) > 1:
                return[value[0], value[1]]
    return []

nums = [3,3]
print(twoSum(nums, 6))