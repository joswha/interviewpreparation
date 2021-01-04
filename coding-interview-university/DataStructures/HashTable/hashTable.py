# Implement with array using linear probing
# hash(k, m) - m is size of hash table
# add(key, value) - if key already exists, update value
# exists(key)
# get(key)
# remove(key)

"""
Note that this does function does not solve the anagrams problem
"""
def hash(k, m):
    sum = 0
    for pos in range(len(k)):
        sum += ord(k[pos])
    return sum % m

def add(k, v, table):
    table[k] = v

def exists(k, table):
    for key in table.keys():
        if k == key:
            return True
    return False

def get(k, table):
    return table[k]

def remove(k, table):
    return table.remove(k)


D = {'a': 1, 'c': 3, 'b': 2}
# add('c', 2, D)
# print(exists('e', D))
print(get('c', D))
