def minRewards(array):

    min_val = float('inf')
    min_index = 0

    for i in range(len(array)):
        if array[i] < min_val:
            min_index = i
            min_val = array[i]
    
    array[min_index] = 1
    cp_min_index = min_index
    while cp_min_index > 0:
        if array[cp_min_index] < array[cp_min_index - 1]:
            array[cp_min_index - 1] = array[cp_min_index] + 1
        else:
            array[cp_min_index - 1] = array[cp_min_index] - 1
        cp_min_index -= 1

    cp_min_index = min_index
    while cp_min_index < len(array) - 1:
        if array[cp_min_index] < array[cp_min_index + 1]:
            array[cp_min_index + 1] = array[cp_min_index] + 1
        else:
            array[cp_min_index + 1] = array[cp_min_index] - 1
        cp_min_index += 1
        
    print(array)
arr = [8, 4, 2, 1, 3, 6, 7, 9, 5]
# # res = 25 # [4,3,2,1,2,3,4,5,1]
minRewards(arr)