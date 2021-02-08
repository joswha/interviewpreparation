# Binary to String: GIven a real number bnetween 0 and 1 that is passed in as  a double, print the binary representation, otherwise "ERROR"

def binaryToString(num):
    if num >= 1 or num <= 0:
        return "ERROR"
    
    binary = ""
    binary += "."
    while num > 0:
        if len(binary) >= 32:
            return "ERROR"
        
        # Shift the nr to left
        r = num * 2
        if r >= 1:
            binary += "1"
            num = r - 1
        else:
            binary += "0"
            num = r
    return binary


print(binaryToString(0.98))