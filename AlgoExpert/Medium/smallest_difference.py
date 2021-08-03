def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()

    min_diff = 1000000
    elems = []
    
    # Some kind of search optimization can be performed?
    for elem1 in arrayOne:
        for elem2 in arrayTwo:
            if min_diff > abs(elem1 - elem2):
                min_diff = abs(elem1 - elem2)
                elems = [elem1, elem2]
    
    return elems
