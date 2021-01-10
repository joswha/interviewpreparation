def sum_of_multiples(limit, multiples):
    x = [i for i in range(limit) for j in multiples if j!=0 and i % j == 0] # generate the multiples list
    l = sorted(set(x), key = x.index) # sort the list, as there are multiple elements
    return sum(l) # return the sum 