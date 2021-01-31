# Program to sort a stack such that the smallest items are on the top. YOu can use an additional temporray stack, but may not copy the elements into any other data structures.

def peek(stack):
    if stack:
        return stack[-1]

def orderAppend(stack, elem):
    # print(peek(stack))
    if not stack:
        stack.append(elem)
    else:
        temp_stack = []
        while peek(stack) != None and elem > peek(stack):
            temp_stack.append(stack.pop())
        stack.append(elem)
        for elem in temp_stack:
            orderAppend(stack, elem)

stack = []

orderAppend(stack, 2)
orderAppend(stack, 3)
orderAppend(stack, 11)
orderAppend(stack, 5)
orderAppend(stack, 4)
orderAppend(stack, 9)
orderAppend(stack, 6)
orderAppend(stack, 7)
orderAppend(stack, 8)
orderAppend(stack, 12)
orderAppend(stack, 1)
orderAppend(stack, 10)

print(stack)

# print(stack.pop())