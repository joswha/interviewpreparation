# Given an image represented by an N x N matrix, where each pixel in the image is represented by an integer, write a metod to rotate the image by 90 degrees.
# Basically it's the transpose of a matrix


def transpose(image, size):
    return [[image[j][i] for j in range(size)] for i in range(size)]

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(matrix)
print(transpose(matrix, 3))