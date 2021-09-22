def indexEqualsValue(array):
    left = 0
    right = len(array) - 1

    while left <= right:
        middle = left + (right - left) // 2
        
        if array[middle] < middle:
            left = middle + 1
        elif array[middle] == middle and middle == 0:
            return middle
        elif array[middle] == middle and array[middle - 1] < middle - 1:
            return middle
        else:
            right = middle - 1
        
    return -1