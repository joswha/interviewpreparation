# Combination Sum
# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.

def combinationSum(candidates, target):
    res = []
    candidates.sort()
    backtrack(res, [], candidates, target, 0)
    return res

def backtrack(lst, tempList, nums, remain, start):
    if remain < 0:
        return
    elif remain == 0:
        lst.append(tempList)
    else:
        for i in range(start, len(nums)):
            tempList.append(nums[i])
            backtrack(lst, tempList, nums, remain - nums[i], i)
            tempList.remove(len(tempList) - 1)
             