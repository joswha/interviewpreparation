def kadanesAlgorithm(array):
    max_to_here = array[0]
    max_global = array[0]
    for elem in array[1:]:
        max_to_here = max(elem, max_to_here + elem)
        max_global = max(max_global, max_to_here)
    return max_global     
    # left = 0
    # total_left_sum = 0

    # right = len(array) - 1
    # total_right_sum = 0

    # while left < right:
    #     print(f"LEFT: {left} -> {array[left]}")
    #     if array[left] < 0:
    #         if array[left - 1] and total_left_sum + array[left] < 0:
    #             total_left_sum = 0
    #             print(f"Tipping left point at {array[left]}")
    #             # left += 1
    #         else:
    #             total_left_sum += array[left]
    #     else:
    #         total_left_sum += array[left]
        
    #     print(f"RIGHT: {right} -> {array[right]}")
    #     if array[right] < 0:
    #         if array[right + 1] and total_right_sum + array[right] < 0:
    #             total_right_sum = 0
    #             print(f"Tipping right point at {array[right]}")
    #             # right -= 1
    #         else:
    #             total_right_sum += array[right]
    #     else:
    #         total_right_sum += array[right]
        
    #     left += 1
    #     right -= 1

    # return (total_left_sum + total_right_sum)