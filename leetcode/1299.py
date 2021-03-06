def replaceElements(arr):
    """
    :type arr: List[int]
    :rtype: List[int]
    """
    curr_max = arr[len(arr) - 1]
    arr[len(arr) - 1] = - 1
    copy_max = 0
    for index in range(len(arr) - 2, -1, -1):
        if arr[index] > curr_max:
            copy_max = curr_max
            curr_max = arr[index]
            arr[index] = copy_max
        else:
            arr[index] = curr_max      

    return arr

array = [17, 18, 5, 4, 6, 1]
replaceElements(array)