def isValidSudoku(board):
    # row_dict = [{k: 0 for k in board[i]} for i in range(len(board))]
    # column_dict = 
    # for i in range(len(board)):
    #     for j in range(len(board)):
    #         row_dict[i][board[i][j]] += 1
    # print(row_dict)
    # print(column_dict)
    rows = [{} for i in range(9)]
    columns = [{} for i in range(9)]
    boxes = [{} for i in range(9)]

    for i in range(9):
        for j in range(9):
            elem = board[i][j]
            if elem != '.':
                elem = int(elem)
                box_i = (i // 3) * 3 + j // 3

                rows[i][elem] = rows[i].get(elem, 0) + 1
                columns[j][elem] = columns[j].get(elem, 0) + 1
                boxes[box_i][elem] = boxes[box_i].get(elem, 0) + 1
    
                if rows[i][elem] > 1 or columns[j][elem] > 1 or boxes[box_i][elem] > 1:
                    return False
    return True

board = [
     ["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]
]

print(isValidSudoku(board))