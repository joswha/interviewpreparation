def topKFrequeny(nums, k):
    val_dict = {k: 0 for k in nums}
    for num in nums:
        val_dict[num] += 1
    sorted_dict = sorted(val_dict.items(), key = lambda x: x[1], reverse = True)
    
    res = []
    for x,y in sorted_dict:
        if k > 0:
            res.append(x)
            k -= 1
    return res

nums = [1,1,1,2,2,3,3,3,3]
k = 2
print(topKFrequeny(nums, k))