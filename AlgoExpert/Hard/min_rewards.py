def minRewards(scores):
    res = [1 for i in scores]

    left = 1
    while left < len(scores):
        if scores[left] > scores[left - 1]:
            res[left] = res[left - 1] + 1
        left += 1

    right = len(scores) - 2
    while right >= 0:
        if scores[right] > scores[right + 1]:
            res[right] = max(res[right], res[right + 1] + 1)
        right -= 1

    return sum(res)


    # min_val = float('inf')
    # min_index = 0

    # for i in range(len(array)):
    #     if array[i] < min_val:
    #         min_index = i
    #         min_val = array[i]
    
    # array[min_index] = 1
    # cp_min_index = min_index
    # while cp_min_index > 0:
    #     if array[cp_min_index] < array[cp_min_index - 1]:
    #         array[cp_min_index - 1] = array[cp_min_index] + 1
    #     else:
    #         array[cp_min_index - 1] = array[cp_min_index] - 1
    #     cp_min_index -= 1

    # cp_min_index = min_index
    # while cp_min_index < len(array) - 1:
    #     if array[cp_min_index] < array[cp_min_index + 1]:
    #         array[cp_min_index + 1] = array[cp_min_index] + 1
    #     else:
    #         array[cp_min_index + 1] = array[cp_min_index] - 1
    #     cp_min_index += 1
        
    # print(array)


arr = [8, 4, 2, 1, 3, 6, 7, 9, 5]
arr2 = [8, 4, 2, 1, 2, 3, 1, 2]
# # res = 25 # [4,3,2,1,2,3,4,5,1]
minRewards(arr)