def sortedSquaredArray(array):
    powed = [x ** 2 for x in array]
    powed.sort()
    return powed