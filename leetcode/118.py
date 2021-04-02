def generate(numRows):
    if n == 0:
        return []
    if n == 1:
        return [1]
    res = [[1], [1,1]]
    for i in range(2, numRows):
        magn = [1]
        for j in range(i - 1):
            # print(i)
            magn.append(res[i - 1][j - i] + res[i - 1][j + 1])
        magn.append(1)
        res.append(magn)
    return res

n = 2
print(generate(n))
