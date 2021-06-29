def isHappy(n):
    """
    :type n: int
    :rtype: bool
    """
    s = set()
    while n!= 1:
        if n in s:
            return False
        s.add(n)
        n = sum([int(i) ** 2 for i in str(n)])
    return True


print(isHappy(2))
# isHappy(19)