def getPermutations(array):
    permutations = []
    permutationsHelper(array, [], permutations)
    return permutations

def permutationsHelper(array, currentPerm, permutations):
    if not len(array) and len(currentPerm):
        permutations.append(currentPerm)
    else:
        for i in range(len(array)):
            newArray = array[:i] + array[i + 1:]
            newPerm = currentPerm + [array[i]]
            permutationsHelper(newArray, newPerm, permutations)