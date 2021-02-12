# Powerset: Write a method to return all subsets of a set.

def powerset(x):
    res = []
    if not x: # set is empty
        res.append(x)
    else:     # set is not empty, continue the algorithm
        a = x[0] # current starting character
        b = x[1:] # rest of the total elements
        for elem in powerset(b): # powerset of the remaining total elements
            res.append(elem) # append each to the result
            r = [a] + elem
            res.append(r)
    return res

s = ['a', 'b', 'c']
print(powerset(s))