def intersect(nums1, nums2):

    if len(nums1) > len(nums2):
        smaller_dict = {k:0 for k in nums2}
        for elem in nums2:
            smaller_dict[elem] += 1
        larger_dict = {k:0 for k in nums1}
        for elem in nums1:
            larger_dict[elem] += 1
    else:
        smaller_dict = {k:0 for k in nums1}
        for elem in nums1:
            smaller_dict[elem] += 1
        larger_dict = {k:0 for k in nums2}
        for elem in nums2:
            larger_dict[elem] += 1

    res = []
    for key, val in smaller_dict.items():
        if key in larger_dict:
            times = min(larger_dict[key], smaller_dict[key])
            for i in range(times):
                res.append(key)
    return res
    
# nums1 = [1,2,2,1]
# nums2 = [2,2]

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

intersect(nums1, nums2)
