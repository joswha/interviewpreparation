def spiralTraverse(array):
    res = []
    s_row = 0
    e_row = len(array) - 1
    s_col = 0
    e_col = len(array[0]) - 1

    while s_row <= e_row and s_col <= e_col:
        for col in range(s_col, e_col + 1):
            res.append(array[s_row][col])

        for row in range(s_row + 1, e_row + 1):
            res.append(array[row][e_col])
        
        for col in reversed(range(s_col, e_col)):
            if s_row == e_row:
                break
            res.append(array[e_row][col])
        
        for row in reversed(range(s_row + 1, e_row)):
            if s_col == e_col:
                break
            res.append(array[row][s_col])

        s_col += 1
        s_row += 1

        e_col -= 1
        e_row -= 1

    return res