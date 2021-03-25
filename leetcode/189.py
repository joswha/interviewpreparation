def rotate(nums, k): 
    while k:
        val = nums.pop()
        nums = [val] + nums
        k -= 1
    print(nums)

a = [1,2,3,4,5,6,7]
k = 3
rotate(a, k)