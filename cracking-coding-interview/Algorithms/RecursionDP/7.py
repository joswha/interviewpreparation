# Write a method to compute all permutations of a string of unique characters

def permWithoutDups(string):
    res = []
    if not string:
        res.append(string)
    else:
        a = string[0]
        b = string[1:]
        for elem in permWithoutDups(b):
            res.append(elem)
            r = a + elem
            res.append(r)
            r = elem + a
            res.append(r)

    return res



a = "abc"

no_dups = []

for x in permWithoutDups(a):
    if x not in no_dups:
        no_dups.append(x) 

print(no_dups)