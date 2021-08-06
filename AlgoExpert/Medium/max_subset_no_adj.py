def maxSubsetNoAdj(array):
    if len(array) == 0:
        return 0
    if len(array) == 1:
        return 1

    adj_sums = [array[0], array[1]]

    for index in range(2, len(array)):
        if index - 3 >= 0:
            adj_sums.append(max(array[index] + adj_sums[index - 2], array[index] + adj_sums[index - 3]))
        else:
            if index - 2 >= 0:
                adj_sums.append(max(array[index] + adj_sums[index - 2], adj_sums[index - 1]))
    
    return adj_sums[-1]