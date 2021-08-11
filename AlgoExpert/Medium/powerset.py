def powerset(array):
    sets = [[]]
    for elem in array:
        for i in range(len(sets)):
            curr_set = sets[i]
            sets.append(curr_set + [elem])
    return sets