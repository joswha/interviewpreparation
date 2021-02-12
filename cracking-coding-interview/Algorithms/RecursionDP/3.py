# A magic index in an array is defined to be the index such that a[i] = i. Given a sorted array with distinct integers, the index
# write a method to find a magic index, if one exists, in a.

# Follow up: what if the values were not distinct

# If the values were not distinct, the algorithm would still work in this manner

def magicIndex(index, a):
    if a[index] == index:
        return index
    else:
        return magicIndex(index + 1, a)


a = [-3, 0, 2, 3, 6]
print(magicIndex(0, a))

# An improvment would be to check if the last character is a[i] < index and that means that no matter which value we would take from the left hadn side of that 
# index, we would still get a value that does not correspond to the index at hand? possibility