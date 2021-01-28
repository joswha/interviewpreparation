def oneAway(a, b):
    if(abs(len(a) - len(b)) > 1):
        return False
    
    s1 = a if len(a) < len(b) else b
    s2 = b if len(a) < len(b) else a

    foundDifference = False

    index_s1 = 0
    index_s2 = 0 
    while(index_s1 < len(s1) and index_s2 < len(s2)):
        if(s1[index_s1] != s2[index_s2]):
            if(foundDifference):
                return False
            foundDifference = True

            if (len(s1) == len(s2)):
                index_s1 += 1
            
        else:
            index_s1 += 1
        index_s2 += 1

    return True

print(oneAway("pale", "ple"))