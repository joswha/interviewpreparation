def runLengthEncoding(string):
    """
    First solution was really close to the correct one; error was bc of k = 0 at the beginning, while k should start from 1.
    Remember: note string[i] and string[i-1] into variables, thus writing cleaner code.
    """
    res = ""
    k = 1
    for i in range(1, len(string)):
        curr = string[i]
        prev = string[i - 1]

        if curr != prev or k == 9:
            res += (str(k) + prev)
            k = 0
        
        k += 1
    
    res += (str(k) + string[len(string) - 1])
    return res