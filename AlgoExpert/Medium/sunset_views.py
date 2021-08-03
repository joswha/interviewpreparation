def sunsetViews(buildings, direction):
    stack = []

    if direction == "EAST":
        for i in range(len(buildings)):
            if stack is []:
                stack.append(i)
                continue
            
            # if direction == "EAST":
            while stack and buildings[stack[len(stack) - 1]] <= buildings[i]:
                # print(f"Stack compared: {buildings[stack[len(stack) - 1]]} with next val: {buildings[i]}")
                stack.pop()
            
            # if stack and stack[len(stack) - 1] >= buildings[i]:
            stack.append(i)
    else:
        for i in reversed(range(len(buildings))):
            if stack is []:
                stack.append(i)
                continue
            
            while stack and buildings[stack[len(stack) - 1]] <= buildings[i]:
                stack.pop()
            
            stack.append(i)
    if direction == "WEST":
        return stack[::-1]
    return stack