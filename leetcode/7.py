def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    if x < 0:
        x = str(x)
        x = x[1:]
        x = -1 * int(x[::-1])
        if x < -2 ** 31:
            return 0
        return x

    x = str(x)
    x = int(x[::-1])
    if x >= 2 ** 31:
        return 0
    return x

a = 1534236469
print(reverse(a))