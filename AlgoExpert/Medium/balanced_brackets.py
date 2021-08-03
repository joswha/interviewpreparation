def balancedBrackets(string):
    brackets = {"}":"{",")":"(","]":"["}
    opening = "([{"
    stack = []
    
    for char in string:
        if char in opening:
            stack.append(char)
        elif char in brackets:
            if len(stack) == 0:
                return False
            if stack[-1] == brackets[char]:
                stack.pop()
            else:
                return False
                
    return len(stack) == 0
