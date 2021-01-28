# Write an algorithm such that if an element in an M x N matrix is 0, its entire row and column are set to 0.
def nullifyRow(matrix, row, size):
    for j in range(size):
        matrix[row][j] = 0

def nullifyColumn(matrix, column, size):
    for i in range(size):
        matrix[i][column] = 0

def zeroMatrix(matrix, n, m):
    row_zeroes = [False for i in range(n)]
    column_zeroes = [False for j in range(m)]

    for i in range(n):
        for j in range(m):
            if(matrix[i][j] == 0):
                row_zeroes[i] = True
                column_zeroes[j] = True

    for i in range(n):
        if row_zeroes[i]:
            nullifyRow(matrix, i, n)

    for j in range(m):
        if column_zeroes[j]:
            nullifyRow(matrix, j, m)

    print(matrix)

matrix = [
    [1,2,3],
    [4,0,6],
    [7,8,9]
]

zeroMatrix(matrix, 3, 3)
