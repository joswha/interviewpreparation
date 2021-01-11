def transpose(lines):
    max_length = -1

    for line in lines:
        if len(line) > max_length:
            max_length = len(line)
    
    for index, line in enumerate(lines): # pad with 0 
        if max_length > len(line):
            lines[index] += ' ' * (max_length - len(line))

    res = [[ '' for i in range(len(lines))] for j in range(max_length)]

    for index in range(max_length):
        # line_nr = ""
        for number in range(len(lines)):
            res[index][number] = lines[number][index]
        # print(line_nr)

    
    return(res)
    



# lines = ["AB ", "DEF"]
lines = ["A", "1"]

print(transpose(lines))
# expected = ["A1", "B2", "C3"]
    
