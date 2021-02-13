# Permutations with Dups: Write a method to compute all permutations of a string whose characters are not necessarily unique. 
# The list of permutations should not have duplicates
def permWithDups(string):
    res = []
    if not string:
        res.append(string)
    else:
        a = string[0]
        b = string[1:]
        for elem in permWithDups(b):
            res.append(elem)
            r = a + elem
            res.append(r)
            r = elem + a
            res.append(r)
    
    good = []
    for elem in res:
        if elem not in good:
            good.append(elem)
    
    return good


a = "abca"
print(permWithDups(a))
