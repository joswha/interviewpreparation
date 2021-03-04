# permutations for all elements of a list 
def permute(s):
    out = []
    if len(s) == 1:
        return s
    else:
        for i,let in enumerate(s):
            a = s[:i]
            b = s[i+1:]
            for perm in permute(a + b):
                out += [let + perm]
    return out

arr = ['1','2','3','5']
# print(permute(arr))

# all permutations for given string
# note that if integer is given, we could simply do integer -> string, calculate permutations, and then revert back
def permute_elem(elem):
    out = []
    if len(elem) == 1:
        out.append(elem)
    else:
        for i in range(len(elem)):
            a = elem[:i]
            b = elem[i + 1:]
            for perm in permute_elem(a + b):
                out.append(elem[i] + perm)
    return out

val = '1234'
print(permute_elem(val))