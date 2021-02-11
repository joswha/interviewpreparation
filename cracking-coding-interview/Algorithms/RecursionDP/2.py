def search(r, d, a):
    if r == 3 and d == 3:
        print(a[r][d])
        return a[r][d]
    else:
        if a[r + 1][d + 1] == 0:
            if a[r + 1][d] == 0:
                return search(r, d + 1, a)
            else:
                return search(r + 1, d, a)
        else:
            print(a[r][d])
            return search(r + 1, d + 1, a)


a = [
    [1, 1, 1, 0],
    [1, 2, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 4],
]

search(0, 0, a)