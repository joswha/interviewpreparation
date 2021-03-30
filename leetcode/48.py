def rotate(matrix):
    n = len(matrix)
    for i in range(n // 2 + n % 2):
        for j in range(n // 2):
            tmp = matrix[n - 1 - i][j]
            
    
    print(matrix)


matrix = [[1,2,3],[4,5,6],[7,8,9]]

rotate(matrix)
