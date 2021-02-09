# You have an integer and you can flip exactly one bit from a 0 to a 1. Write code to find the length of the longest sequence of 1s you could create



def intToBinary(integer):
    return "{0:b}".format(integer)

def countOnes(integer):
    MAX_LENGTHS = -1000000
    string = intToBinary(integer)
    result = string.split('0')
    # print(result)
    k = 0
    for index in range(len(result) - 1):
        if len(result[index]) + len(result[index + 1]) > MAX_LENGTHS:
            MAX_LENGTHS = len(result[index]) + len(result[index + 1])
            k = len(result[index]) + len(result[index + 1]) + 1

    print(k)

print(intToBinary(1352))
countOnes(1352) 