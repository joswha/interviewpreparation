discount = {1: 1, 2: 0.95, 3: 0.9, 4: 0.8, 5: 0.75}

# basket = [1,2,1,3,4,5,6]
# print(basket)
# print(set(basket))
def total(basket):
    for item in basket:
        if item < 1 or item > 5:
            raise Exception("Book does not exist in the library")
    
    found = []
    while len(basket):
        unique = set(basket)
        found.append(len(unique))
        for title in unique:
            basket.remove(title)
    
    # We know that groups of 4 area cheaper than groups of 3 and 5 so we swap them.
    while 3 in found and 5 in found:
        found.remove(3)
        found.remove(5)
        found += [4,4]

    return sum((s * 800) * discount[s] for s in found)