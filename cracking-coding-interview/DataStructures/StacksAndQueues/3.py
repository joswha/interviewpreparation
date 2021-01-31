def splitStacks(stack, limit):

    sets_of_stacks = [[]] * 4

    # print(sets_of_stacks)
    k = 0
    length = len(stack) // limit

    for i in range(length):
        for j in range(limit):
            sets_of_stacks[k].append(stack.pop())
        k += 1 
    
    print(sets_of_stacks)
        


n1 = "1"
n2 = "2"
n3 = "3"
n4 = "4"
n5 = "5"
n6 = "6"
n7 = "7"
n8 = "8"
n9 = "9"
n10 = "10"
n11 = "11"
n12 = "12"


stack = []
stack.append(n1)
stack.append(n2)
stack.append(n3)
stack.append(n4)
stack.append(n5)
stack.append(n6)
stack.append(n7)
stack.append(n8)
stack.append(n9)
stack.append(n10)
stack.append(n11)
stack.append(n12)

# print(stack)
# stack.pop()
# print(stack)
splitStacks(stack, 3)