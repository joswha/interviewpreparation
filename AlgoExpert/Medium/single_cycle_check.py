def hasSingleCycle(array):

    index = 0
    visited_elems = 0

    while visited_elems < len(array):
        if visited_elems > 0 and index == 0:
            return False
        
        visited_elems += 1
        index = calculateNextIndex(index, array)

    return index == 0

def calculateNextIndex(index, array):

    jump = array[index]
    next = (index + jump) % len(array)
    
    if next > 0:
        return next
    else:
        return next + len(array)