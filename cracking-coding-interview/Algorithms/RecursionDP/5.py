# Recursive Multipy : write a recursive function to multiply two positive integers without using the * operator; can use: addition, subtraction and bit shifting
# and minimize the nr of those operations.

def multiply(x, y):
    if x > 0 and y > 0:
        return y + multiply(x - 1 ,y)
    else:
        return 0

# To minimize, we could also do a while instead of return each time, though it kinda seems the same thing; also we could compare the numbers so that
# we get the max and sum on that, counting the minimal one times (less nr of operations in total)

print(multiply(318,389))