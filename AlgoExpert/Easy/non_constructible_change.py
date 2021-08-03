# Given array of integers, find smallest nr that CANNOT be constructed using elements from that array.
def nonConstructibleChange(coins):
    coins.sort()
    s = 0
    for coin in coins:
        if s + 1 < coin:
            return s + 1
        else:
            s += coin
    return s + 1