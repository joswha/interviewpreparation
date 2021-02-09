# Given a positive integer, print the next smallest and the next largest number that have the same number of 1 bits in their binary representation
def getNext(n):
    c = n
    c0 = 0
    c1 = 0
    while((c & 1) == 0 and (c != 0)):
        c0 += 1
        c >>= 1
    
    while((c & 1) == 1):
        c1 += 1
        c >>= 1
    
    if c0 + c1 == 31 or c0 + c1 == 0:
        return -1
    
    p = c0 + c1 # position of right most non-trailing zero
    
    n |= (1 << p) # flip rightmost non-trailing zero
    n &= ~((1 << p) - 1) # clear all bits to the right of p
    n |= (1 << (c1-1)) - 1 # insert c1 - 1 ones on the right

    return n

def getPrev(n):
    temp = n
    c0 = 0
    c1 = 0
    while (temp & 1 == 1):
        c1 += 1
        temp >>= 1

    if temp == 0:
        return -1
    
    while(((temp & 1) == 0) and (temp != 0)):
        c0 += 1
        temp >>= 1
    
    p = c0 + c1 # position of right most non-trailing zero
    n &= ((~0) << (p + 1)) # clears from bit p onwards
 
    mask = (1 << (c1 + 1)) - 1 # sequence of (c1+1) ones
    n |= mask << (c0 - 1)

    return n


print(getPrev(1775))