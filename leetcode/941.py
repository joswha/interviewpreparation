def validMountainArray(self, arr):
    """
    :type arr: List[int]
    :rtype: bool
    """
    n = len(arr)
    i = 0

    while i < n - 1 and arr[i] < arr[i + 1]:
        i += 1
    
    if i == 0 or i == n - 1:
        return False

    while i < n - 1 and arr[i] > arr[i + 1]: 
        i += 1

    return i == n-1