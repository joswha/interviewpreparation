def findDisappearedNumbers(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    # result = []
    # needed = {k: 0 for k in range(1, len(nums) +  1)}
    # for elem in nums:
    #     needed[elem] += 1
    
    # for key, value in needed.items():
    #     if value == 0:
    #         result.append(key)

    # return result
    required = set(range(1, len(nums) + 1))
    for num in nums:
        if num in required:
            required.remove(num)

    return list(required)  


test = [4,3,2,7,8,2,3,1]
print(findDisappearedNumbers(test))