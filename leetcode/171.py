def titleToNumber(self, columnTitle):
    """
    :type columnTitle: str
    :rtype: int
    """
    alphabet = {
        'A' : 1, 
        'B' : 2, 
        'C' : 3, 
        'D' : 4, 
        'E' : 5, 
        'F' : 6, 
        'G' : 7, 
        'H' : 8, 
        'I' : 9, 
        'J' : 10, 
        'K' : 11, 
        'L' : 12, 
        'M' : 13, 
        'N' : 14, 
        'O' : 15, 
        'P' : 16, 
        'Q' : 17, 
        'R' : 18, 
        'S' : 19, 
        'T' : 20, 
        'U' : 21, 
        'V' : 22, 
        'W' : 23, 
        'X' : 24, 
        'Y' : 25, 
        'Z' : 26
    }
    
    elem_sum = 0
    length = len(columnTitle)
    for index, elem in enumerate(columnTitle):
        print(length - index)
        elem_sum += (26 ** (length - index - 1) * alphabet[elem])

    return elem_sum