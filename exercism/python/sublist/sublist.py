"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 0
SUPERLIST = 1
EQUAL = 2
UNEQUAL = 3


def check(list_one, list_two):
    n = min(len(list_one), len(list_two))
    if len(list_one) > len(list_two):
        return any(list_one[i: i + n] == list_two for i in range(len(list_one) - n + 1))
    else:
        return any(list_one == list_two[i: i + n] for i in range(len(list_two) - n + 1))

def sublist(list_one, list_two):
    if check(list_one, list_two):
        if len(list_one) > len(list_two):
            return SUPERLIST
        else:
            if list_one == list_two:
                return EQUAL
            else:
                return SUBLIST
    else:
        return UNEQUAL
        
B = [1, 2, 3, 1, 1, 2, 2] 
A = [1, 2, 3] 
print(sublist(A, B)) 


