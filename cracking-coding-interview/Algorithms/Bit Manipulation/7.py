# Swap odd and even bits in an integer with as few instructions as possible

def swapOddEven(x):
    return ( ((x & 0xaaaaaaaa) >> 1 ) | (( x & 0xaaaaaaaa) << 1))

