def findThreeLargestNumbers(array):
    """
    Not that elegant solution, but hey it works, and it's pretty straightforward.
    Should there be need for finding more than top 3 numbers, creating functions for shifting and updating would solve it properly.
    """
    res = [-100, -100, -100]
    for elem in array:
        if elem >= res[2]:
            res[0] = res[1]
            res[1] = res[2]
            res[2] = elem
        elif elem >= res[1]:
            res[0] = res[1]
            res[1] = elem
        elif elem >= res[0]:
            res[0] = elem
    return res
