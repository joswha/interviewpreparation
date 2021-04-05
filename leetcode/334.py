def increasingTriplet(nums):
    for index in range(len(nums) - 2):
        stack = [nums[index]]
        for elem in nums[index:]:
            if elem > nums[index]:
                stack.append(elem)
            if len(stack) >= 3:
                if stack[-2] < stack[-1]:
                    print(stack)
                    return True
    return False

nums = [1, 2, 2, 1]
print(increasingTriplet(nums))