# Write a function to determine the number of bits you would need to flip to convert integer A to integer B

def countFlips(a, b):
    k = 0
    c = a ^ b
    while c != 0:
        k += c & 1
        c >>= 1 # shift right to next digit
    return k

print(countFlips(29, 15))