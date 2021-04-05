def setZeroes(matrix):
    pos_set = set()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                pos_set.add((i,j))

    for i, k in pos_set:
        for j in range(len(matrix[0])):
            matrix[i][j] = 0
        for m in range(len(matrix)):
            matrix[m][k] = 0

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
setZeroes(matrix)