def magicIndex(index, a):
    if a[index] == index:
        return index
    else:
        return magicIndex(index + 1, a)


a = [-3, 0, 2, 3, 6]
print(magicIndex(0, a))