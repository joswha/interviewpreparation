import math

def isPowerOfThree(n):
    if n == 0:
        return False
    if n == 1:
        return True
    while n % 3 == 0:
        n //= 3
    return n == 1
    # k=[3**i for i in range(100)]
    # if n in k:
    #     return True
    # else:
    #     return False

    # for i in range(3, n + 1, 3):
    #     # print(i)
    #     if n % i == 0:
    #         c_n = n
    #         while c_n > 1:
    #             if c_n % i == 0:
    #                 c_n //= i
    #                 print(c_n)
    #             else:
    #                 break
    #         if c_n == 1:
    #             return True
    #         else:
    #             c_n = n
    # return False

print(isPowerOfThree(0))