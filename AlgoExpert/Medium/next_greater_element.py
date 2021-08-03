def nextGreaterElement(array):
    # stack = []
    # res = [-1 for _ in range(len(array))]
    # i = 0
    # max_val = -10000

    # for element in reversed(array):
    #     max_val = max(max_val, element)
    #     stack.append(element)
    
    # cp_stack = [element for element in stack]

    # while stack is not []:
    #     # not necessary
    #     # if stack and array[i] >= stack[len(stack) - 1]: # elements do not match
    #     while stack and array[i] >= stack[len(stack) - 1]:
    #         stack.pop()
    #     if len(stack) == 0:
    #         break

    #     if stack and array[i] < stack[len(stack) - 1]: # found next larger element than curent one
    #         res[i] = stack[len(stack) - 1]

    #     i += 1
    
    # # print(cp_stack)

    # for i in range(len(cp_stack)):
    #     if res[i] == -1:
    #         while cp_stack and array[i] >= cp_stack[len(stack) - 1]:
    #             cp_stack.pop()
    #         if cp_stack and res[i] == -1 and cp_stack and array[i] < cp_stack[len(cp_stack) - 1]: # found next larger element than curent one
    #             res[i] = cp_stack[len(cp_stack) - 1]
    #             print(i) 
    #     # ceva cu max? iei valoarea maxima si fix pe aia o excluzi, doar ocurentele ei ar trebui sa ramana -1

    # # print(stack)
    # return res
    result = [-1 for _ in range(len(array))]
    stack = []

    # only need to iterate two times over the array
    for i in range(2 * len(array) -1, -1, -1):
        circularI = i % len(array)
        
        while len(stack) > 0:
            if stack[len(stack) - 1] <= array[circularI]:
                stack.pop()
            else:
                result[circularI] = stack[len(stack) - 1]
                break

        # my solution was really close, this is what it missed
        print(array[circularI])
        stack.append(array[circularI])
        # construct the stack on the go basically, instead of initializing all the way up
        # re-appending the array value to the stack, and using the circularI 
    
    return result
