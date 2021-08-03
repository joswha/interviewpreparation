def sortStack(stack):
    if len(stack) == 0:
        return stack
    tail = stack.pop()
    sortStack(stack)
    insertSorted(stack, tail)
    return stack

def insertSorted(stack, element):
    if len(stack) == 0 or stack[len(stack) - 1] <= element:
        stack.append(element)
        return
    tail = stack.pop()
    insertSorted(stack, element)
    stack.append(tail)