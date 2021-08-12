def largestRange(array):
    table = { x : 1 for x in array }
    
    if len(array) == 1:
        return [array[0], array[0]]
    
    curr_len = 0
    max_len = 0
    curr_start = 0
    curr_end = 0
    max_start = 0
    max_end = 0
    
    for elem in array:
        
        curr_elem = elem
        table[elem] = 2
        
        while curr_elem + 1 in table and table[curr_elem + 1] != 2:
            table[curr_elem + 1] = 2
            curr_len += 1
            curr_elem += 1

        curr_end = curr_elem
        curr_elem = elem

        while curr_elem - 1 in table and table[curr_elem - 1] != 2:
            table[curr_elem - 1] = 2
            curr_len += 1
            curr_elem -= 1
        
        curr_start = curr_elem

        if curr_len > max_len:
            max_len = curr_len
            max_start = curr_start
            max_end = curr_end

        curr_len = 0

    return [max_start, max_end]