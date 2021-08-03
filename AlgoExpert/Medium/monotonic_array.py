def isMonotonic(array):
    if len(array) == 0 or len(array) == 1:
        return True
    
    first = array[0]
    last = array[len(array) - 1]
    
    cond = 0
    
    if first <= last:
        cond = -1
    elif first >= last:
        cond = 1
    
    for i in range(len(array) - 1):
        if cond == -1:
            if array[i] > array[i + 1]:
                return False
        elif cond == 1:
            if array[i] < array[i + 1]:
                return False
    return True