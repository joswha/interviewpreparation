def checkIfExist(arr):
    """
    :type arr: List[int]
    :rtype: bool
    """
    mapping = {}

    for i, elem in enumerate(arr):
        if elem * 2 in mapping or (elem % 2 == 0 and elem / 2 in mapping):
            return True
        
        if elem not in mapping:
            mapping[elem] = i
    
    return False


print(checkIfExist([-2,0,10,-19,4,6,-8]))