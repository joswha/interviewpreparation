# O(log n) time | O(1) space ~ itterative solution
def binarySearch(array, target):
    left = 0
    right = len(array) - 1
    while left <= right: # Only check if left <= right
        middle = (left + right) // 2  + (left + right) % 2 # initialize middle for every particular search
        if array[middle] == target:
            return middle
        if target > array[middle]: # search to the right of middle     | ->
            left = middle + 1
        elif target < array[middle]: # search to the left of middle <- | 
            right = middle - 1
    return -1